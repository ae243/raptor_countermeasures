/* 
 * 	Copyright (c) 2010 Colorado State University
 *	
 *	Permission is hereby granted, free of charge, to any person
 *	obtaining a copy of this software and associated documentation
 *	files (the "Software"), to deal in the Software without
 *	restriction, including without limitation the rights to use,
 *	copy, modify, merge, publish, distribute, sublicense, and/or
 *	sell copies of the Software, and to permit persons to whom
 *	the Software is furnished to do so, subject to the following
 *	conditions:
 *
 *	The above copyright notice and this permission notice shall be
 *	included in all copies or substantial portions of the Software.
 *
 *	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 *	EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 *	OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 *	NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 *	HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 *	WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 *	FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 *	OTHER DEALINGS IN THE SOFTWARE.
 * 
 * 
 *  File: backlogUtils_t.h
 *  Authors: M. Lawrence Weikum
 *  Date: April 2014
 */
#ifndef BACKLOGTEST_H_
#define BACKLOGTEST_H_

#include "backlogUtil.h"
#include <CUnit/Basic.h>
#include <stdlib.h>
#include <stdio.h>

void testMRT_backlog_read();
void testMRT_backlog_write();
void testMRT_backlog_init();
void testMRT_backlog_resize();
void testMRT_backlog_wrap();
void testMRT_backlog_fastforward();
void testXML_backlog_read();
void testXML_backlog_write();
void testXML_backlog_fastforward();
int init_mrtUtils(void);
int clean_mrtUtils(void);

void help_load_test_MRT(MRTheader* mrtHeader1, uint8_t* rawMessage1);
#endif
