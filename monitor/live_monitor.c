#include <stdio.h>
#include "bgpstream.h"

int main(int argc, const char **argv){
    bgpstream_t *bs = bgpstream_create();
    bgpstream_record_t *record = bgpstream_record_create();
    bgpstream_elem_t *elem = NULL;
    char buffer[1024];

    /* Define the prefix to monitor for (2403:f600::/32) */
    bgpstream_pfx_storage_t my_pfx;
    my_pfx.address.version = BGPSTREAM_ADDR_VERSION_IPV6;
    inet_pton(BGPSTREAM_ADDR_VERSION_IPV6, "2403:f600::", &my_pfx.address.ipv6);
    my_pfx.mask_len = 32;

    /* Set metadata filters */
    bgpstream_add_filter(bs, BGPSTREAM_FILTER_TYPE_COLLECTOR, "rrc00");
    bgpstream_add_filter(bs, BGPSTREAM_FILTER_TYPE_COLLECTOR, "route-views2");
    bgpstream_add_filter(bs, BGPSTREAM_FILTER_TYPE_RECORD_TYPE, "updates");
    /* Time interval */
    bgpstream_add_interval_filter(bs, 1407806410, 1407826135);

    /* Start the stream */
    bgpstream_start(bs);

    /* Read the stream of records */
    while (bgpstream_get_next_record(bs, record) > 0) {
        /* Ignore invalid records */
        if (record->status != BGPSTREAM_RECORD_STATUS_VALID_RECORD){
            continue;
        }
        /* Read the stream of records */
        while((elem = bgpstream_record_get_next_elem(record)) != NULL){
            /* Select only announcements and withdrawals */
            /* and only elems that carry information for 2403:f600::/32 */
            if ((elem->type == BGPSTREAM_ELEM_TYPE_ANNOUNCEMENT || 
                        elem->type == BGPSTREAM_ELEM_TYPE_WITHDRAWAL) &&
                    bgpstream_pfx_storage_equal(&my_pfx, &elem->prefix)) {
                /* Print the BGP information */
                bgpstream_elem_snprintf(buffer, 1024, elem);
                fprintf(stdout, "%s\n", buffer);
            }
        }
    }

    bgpstream_destroy(bs);
    bgpstream_record_destroy(record);
    return 0;
}
