import sys
import numpy
import matplotlib.pyplot as plt
import collections

# usage: python make_graphs.py

def plot_data(data, color):
    n, bins, patches = plt.hist(data, 50, facecolor='green', alpha=0.75)
    plt.xlabel('Resilience')
    plt.ylabel('# of ASes')
    plt.title('Histogram of Tor-related AS Resiliency to Tier1 ASes')
    plt.axis([0, 1, 0, 360])
    plt.show()

data_map = {"35540": 0.5467962194906808, "33083": 0.9285013590910777, "1853": 0.9462993281516698, "20910": 0.9296081839868844, "27889": 0.8964641158379338, "41011": 0.529617398163682, "35549": 0.8762738318502629, "46475": 0.6543747035533554, "59729": 0.9418540496868866, "46606": 0.5892353694042136, "18881": 0.47923517259844217, "16075": 0.572945379034152, "61102": 0.9361974440772508, "37692": 0.9367919357075843, "39651": 0.9426664703972096, "9676": 0.9366705133981996, "8304": 0.9288293574971404, "57944": 0.937407647542006, "12390": 0.5602192501842227, "4788": 0.9382857219186754, "28762": 0.9172024108273596, "50577": 0.9026544694937709, "49349": 0.9347299178702216, "10103": 0.9366088064198141, "3927": 0.2584801327740403, "8866": 0.583913620463563, "7303": 0.32313307515823003, "197999": 0.5429881624954035, "21409": 0.928938470648914, "14987": 0.935695159073773, "48904": 0.431050427391725, "30740": 0.8840121925366655, "11260": 0.4525716606594071, "3254": 0.939236436900306, "44050": 0.8982492626046229, "3257": 0.22614881177925206, "47206": 0.9286406954231387, "18420": 0.9370514409511728, "20857": 0.6711394737705063, "196752": 0.4014114156143412, "393406": 0.3975705309586191, "22281": 0.4693196004643046, "62638": 0.9379863427920978, "30036": 0.8993948608116191, "39102": 0.6101087517228997, "4721": 0.8740376396472991, "41653": 0.9303172261282591, "12093": 0.7815498470109548, "719": 0.8884764358665203, "202194": 0.9194911068231393, "2857": 0.761236778686075, "29854": 0.5575464669812222, "197726": 0.937014359507963, "6849": 0.5417013177527006, "12705": 0.9005059931477988, "58319": 0.9376267651609728, "12714": 0.9015796069118865, "41557": 0.935906410932059, "6128": 0.6781868361270054, "42455": 0.4297894497456193, "39554": 0.431050427391725, "6659": 0.9395772050787854, "51167": 0.9304015021355541, "29456": 0.9004947563468261, "4739": 0.9380736915072788, "30693": 0.8787919989482355, "200702": 0.937428997463854, "6799": 0.8883297956138271, "27176": 0.9399224435996867, "8767": 0.9306282821876343, "51765": 0.5768928672158465, "1835": 0.38360768743378476, "200938": 0.0, "43802": 0.9373458451366563, "32780": 0.9403820173531245, "25668": 0.8838857699012395, "802": 0.878803235749208, "14576": 0.9001997403420864, "49048": 0.6368726634476978, "21844": 0.9347625045930424, "4323": 0.4202205427597791, "6724": 0.9332324937110351, "46720": 0.7172391253818448, "39369": 0.44768201651135536, "50266": 0.9024128782728588, "2607": 0.9310600621372573, "2828": 0.12087854149950474, "19975": 0.4525655302140723, "21069": 0.884942443034019, "6389": 0.6537626989896992, "11138": 0.8874578198583489, "196682": 0.7284267467326192, "5410": 0.4832403697647724, "57611": 0.6745361729478512, "5413": 0.9424888891743081, "14754": 0.851216889361334, "196689": 0.2982224504541353, "15756": 0.9318491220750447, "17864": 0.9373615766580181, "24900": 0.9296239155082461, "43146": 0.9047120686031679, "34240": 0.547036471659477, "56813": 0.2982224504541353, "201229": 0.40103844667918714, "59970": 0.9348087608842464, "1403": 0.8787538326726339, "1102": 0.3795645290151056, "34989": 0.7423390300168664, "9085": 0.4180594020327658, "49604": 0.9036927499036445, "3582": 0.7203811972361964, "20742": 0.8851407914977869, "8047": 0.8950128256747892, "197422": 0.6030963036056294, "20625": 0.4470078084529959, "1101": 0.37975122818857726, "62512": 0.894777472011938, "31246": 0.9347844818805167, "17139": 0.8787492991045394, "20807": 0.9046575513904488, "18106": 0.9394707242005859, "57188": 0.9347647519532369, "8283": 0.9048359101582184, "12843": 0.9297337316962592, "133165": 0.934302796418398, "6939": 0.9145432704172065, "29169": 0.575980419368257, "12844": 0.4820520196464228, "40529": 0.8945426228716095, "42632": 0.9039363189899936, "14": 0.4697538656387692, "5578": 0.49923986123790004, "5577": 0.8894444862703147, "32": 0.9345950762585498, "31": 0.9345827157774799, "133803": 0.9431687554006875, "16814": 0.347104876350024, "21195": 0.431933471162608, "1241": 0.8779186299745873, "1930": 0.4909166768797094, "29141": 0.5997908005676975, "24872": 0.931864533622194, "35548": 0.5209967218035838, "5603": 0.5698541258556468, "42730": 0.9303161024481619, "47385": 0.9303857706141923, "24282": 0.8973259784725367, "6079": 0.3650040614515304, "10143": 0.9354182509683371, "35370": 0.9362569991224059, "35377": 0.9373840502599634, "35376": 0.5562373796679075, "2611": 0.5481412968044292, "32475": 0.4717217491679065, "18451": 0.8790077455269104, "18450": 0.9297517675802855, "42148": 0.9031095599331636, "3269": 0.9365409226976626, "34610": 0.5935013262981985, "16245": 0.599380157917989, "10796": 0.7241899858378853, "20130": 0.9348254306784893, "38731": 0.9367581604457864, "3292": 0.4343164607639906, "63294": 0.9293688401261668, "197328": 0.9451969979762521, "855": 0.9293068690971751, "8943": 0.7760785455027567, "39145": 0.8835995649711124, "16923": 0.8977462348289141, "62904": 0.5699895708305175, "8369": 0.9311571088175754, "201206": 0.9356771801922167, "41998": 0.6405549631264376, "51852": 0.7132261605268674, "53850": 0.7119996673906912, "57370": 0.6744709995022097, "12334": 0.49000430369477255, "7552": 0.9368203925290826, "12337": 0.9359495850631188, "24971": 0.46246111894158937, "36024": 0.5337110679600862, "39389": 0.4084251286332791, "35470": 0.9030005629637288, "59610": 0.47851467470023024, "33604": 0.8932372280797067, "32613": 0.5562902340014005, "6805": 0.5502221406525534, "7162": 0.8436150009409904, "41164": 0.4311484533101635, "4181": 0.4518488951849687, "10561": 0.7300088883095693, "34971": 0.9576282708923032, "553": 0.5978494770482693, "20001": 0.7231254862257421, "4771": 0.448233883899125, "10242": 0.8863972619121414, "812": 0.7263701540031416, "13649": 0.5709708409377049, "3462": 0.936661108236182, "12353": 0.8881623672793345, "10091": 0.9349243145270487, "29580": 0.710861379452161, "13768": 0.6201085271047714, "6752": 0.8762659660895821, "25019": 0.8895534832397495, "3209": 0.9290734103224683, "39135": 0.9418540496868866, "56478": 0.40482071581972123, "8839": 0.9369659092163434, "41585": 0.9309228897006854, "13118": 0.900491947146583, "17": 0.8933110694850062, "39138": 0.9303318339695236, "2860": 0.600917814611738, "63949": 0.9310744212585529, "21021": 0.36524644099857767, "559": 0.5891613364171943, "43948": 0.7446487052866353, "25408": 0.9047501328751715, "34274": 0.9291355754596748, "30633": 0.6000766349826335, "5602": 0.5200098264082603, "30968": 0.9162279783069255, "22759": 0.8949842291498349, "16586": 0.6901160036069003, "15782": 0.9317273763881381, "18779": 0.8966263448098905, "197071": 0.9356861696329949, "20657": 0.9427911988880062, "32354": 0.38045325574295813, "55870": 0.9353434472033287, "12513": 0.5619366851212395, "1312": 0.7204969362862148, "43541": 0.6855360906960111, "29405": 0.33226549927610544, "12695": 0.9019568789707252, "11051": 0.4655631774721178, "28908": 0.931562753966447, "6106": 0.9345827157774799, "62160": 0.9347647519532369, "47869": 0.9428855880161765, "29562": 0.4785494225331902, "43939": 0.4023797297099894, "31078": 0.48812525917289834, "1759": 0.25101432930701884, "48347": 0.9043137546093385, "15320": 0.8788144725501807, "10838": 0.7226337207369594, "6718": 0.6745361729478512, "17506": 0.8577370346848506, "35158": 0.4457358025828911, "8167": 0.6391093865672467, "12494": 0.7250118829170286, "49527": 0.9444632348727376, "200519": 0.9358996688514754, "12499": 0.9311689756419865, "52173": 0.931881388823653, "35592": 0.5905969764067424, "9443": 0.9365322601554771, "19108": 0.5296911752903205, "35154": 0.9004902616264371, "39351": 0.4470398828693186, "33824": 0.9308273768924178, "60168": 0.9418540496868866, "33885": 0.9315105743915553, "6453": 0.1857472348369057, "36375": 0.893314440525298, "11403": 0.9305134848572466, "5539": 0.9304856008861148, "25577": 0.9433271942944019, "24482": 0.9391764511893964, "56724": 0.9000059555045155, "47692": 0.5429640854303749, "12436": 0.9358535979674875, "6848": 0.6188432330973326, "4662": 0.9366660186778106, "29066": 0.5076287927984215, "8764": 0.9297700370252376, "15962": 0.5796784287410177, "47264": 0.4735880397951624, "680": 0.5375461892078867, "29107": 0.933111818530159, "44923": 0.9377222779692403, "8426": 0.5097359707776972, "8427": 0.6910025810931835, "20676": 0.4455400459802502, "39792": 0.5966493264676795, "8422": 0.5973502971240042, "21483": 0.8902760095422914, "31342": 0.11057911101172785, "28917": 0.696488449779071, "9822": 0.936510950824388, "1136": 0.8898347151003237, "13926": 0.843053841467829, "200429": 0.7284267467326192, "39180": 0.5384298047135916, "49185": 0.9296643679917477, "48815": 0.9365221876253605, "4224": 0.8787789179435243, "35463": 0.9300408008243317, "34602": 0.9376485446218552, "198599": 0.9358981229993462, "34550": 0.6110179080897101, "20773": 0.5893628538368831, "7385": 0.5562791331268018, "16276": 0.5476035080681365, "3595": 0.46586636814204296, "54858": 0.8949606318677923, "50009": 0.9025482357116414, "12400": 0.9362008151175426, "20880": 0.9292457439052583, "44724": 0.9004902616264371, "46562": 0.9345390750121935, "5588": 0.5506157978679771, "7459": 0.8865308180642506, "6327": 0.5374269967409685, "50245": 0.9287690136005208, "31514": 0.9004093566594339, "44133": 0.9294070452494738, "35017": 0.6437642442264099, "2152": 0.9389583260762328, "31510": 0.6182398000748371, "12271": 0.7227086240967061, "62000": 0.8762682134497766, "35018": 0.9013251559387055, "15728": 0.48474997555995786, "49981": 0.9292882071240199, "5381": 0.42317727728579235, "9063": 0.6406425144732412, "20454": 0.6313798903962433, "9066": 0.5877172320898939, "20712": 0.9346382772573942, "61440": 0.936930302365659, "59711": 0.886392571126141, "11831": 0.6739619724181484, "1955": 0.49105113303359715, "43266": 0.5940716885428453, "8331": 0.932295555423694, "43260": 0.9362607447227301, "49776": 0.5768917435357493, "49350": 0.9004902616264371, "43478": 0.6368726634476978, "13319": 0.8917716277517521, "29208": 0.48296745353861353, "8339": 0.9302988660797457, "202109": 0.4982071684048125, "14061": 0.43000777086044456, "8870": 0.9391844105118026, "3249": 0.2689470446592199, "39709": 0.9180264132243663, "50673": 0.7294699732401649, "12668": 0.9321948955707902, "8877": 0.9418540496868866, "3243": 0.5099653569426013, "3242": 0.9035826292541124, "12306": 0.4504402231637896, "12301": 0.6011754597214318, "41307": 0.9300239456228727, "23342": 0.6017610522573524, "8972": 0.6675052900752135, "38333": 0.936031148863809, "24700": 0.9298789908903254, "6503": 0.8435681550059262, "36114": 0.9347894729153767, "44575": 0.9322375954144863, "32645": 0.3904451233969299, "7018": 0.07947133941902387, "51290": 0.6878956056242437, "15626": 0.936853673254054, "57860": 0.0, "15399": 0.9325570411737935, "701": 0.07654056180373293, "25820": 0.9400831298535958, "31863": 0.4254099824717746, "58243": 0.9303136412663733, "3308": 0.25095917855747635, "12715": 0.8768878219531445, "14615": 0.8787639069458038, "44185": 0.9310477665243914, "3303": 0.5522960256759448, "14613": 0.8787459280642476, "3301": 0.2513642364562148, "49855": 0.9306621959181197, "35041": 0.931703847368285, "174": 0.3255789880997643, "201133": 0.936836818052595, "60295": 0.6863954926943938, "6789": 0.9176161688090113, "25151": 0.5382744790455685, "51191": 0.5419239425889365, "131178": 0.9342242618264521, "60011": 0.9284833802095214, "34011": 0.9358422656696992, "24989": 0.5876058648678469, "7684": 0.8583960815027648, "32220": 0.13118965135577623, "40029": 0.8950752472377134, "31127": 0.9323690659858663, "1653": 0.3836518766020347, "45899": 0.9353791856956479, "26496": 0.899426190126292, "59444": 0.9296643679917477, "8758": 0.7139733071851385, "25535": 0.9326376255291129, "3663": 0.8871813945544215, "15527": 0.8958359786635623, "31242": 0.9349596410374534, "24806": 0.691571159580393, "8201": 0.8763035385797258, "3253": 0.8902760095422914, "50212": 0.8966899755374843, "19969": 0.8787470517443448, "24560": 0.8586904856882485, "36236": 0.9435890383135537, "59567": 0.9351232059042647, "1249": 0.7203946813973636, "35986": 0.7153819444834612, "41733": 0.6368749108078923, "47956": 0.5635394556807448, "394362": 0.4742835326489857, "10508": 0.7203935577172663, "17971": 0.9364749930612754, "21502": 0.9288325655189832, "42431": 0.9427957486457877, "18747": 0.8996290731998926, "29028": 0.9030807734645396, "34232": 0.9323758080664499, "33070": 0.7499328601141884, "24931": 0.4787578707567743, "39642": 0.49202805154994816, "46375": 0.6046297867367544, "9121": 0.9347738270364366, "12874": 0.6162444982105645, "34555": 0.9290748531537417, "39857": 0.3834209991089217, "12871": 0.8932980979489673, "31019": 0.9345775235520748, "49770": 0.884280425633298, "20738": 0.6880066679289504, "23655": 0.8976074486377383, "9534": 0.9336134632092814, "31012": 0.8815820966297463, "17439": 0.9283968568420319, "34695": 0.33486828004796754, "15557": 0.9292333621505461, "5390": 0.9032464687631963, "201814": 0.9295823393446473, "25229": 0.9372594787726956, "6739": 0.9289201680012483, "48917": 0.9427979960059822, "13285": 0.9348831098136517, "5668": 0.1321447794384521, "11492": 0.3903779036929079, "34383": 0.9286406954231387, "46652": 0.5254362127326622, "39309": 0.8901886877244769, "5541": 0.41204221853704, "6280": 0.5399246010177898, "12605": 0.9290324432574593, "8615": 0.9020886108933135, "2119": 0.9319909057527953, "16652": 0.2982224504541353, "20836": 0.6485590499370587, "1161": 0.3795645290151056, "16302": 0.8958393497038541, "2110": 0.36749906769281276, "28099": 0.8229462217942249, "57891": 0.8769457925484277, "42331": 0.8937393736489091, "22709": 0.34865610472690156, "6364": 0.8864425748904693, "31333": 0.8897490035766737, "47172": 0.9033187806813442, "44789": 0.8886174577187271, "62471": 0.9399033410380332, "31334": 0.8882842068672379, "54489": 0.4150368623255908, "35366": 0.9299451027714825, "45711": 0.9281886109798889, "53264": 0.6476735677166486, "58666": 0.9366615239574215, "201773": 0.9346029420192307, "17055": 0.756865966314318, "21453": 0.9374157105233982, "50472": 0.9300834948749863, "10013": 0.22694011796393662, "11232": 0.8978519009227224, "200831": 0.9030005629637288, "35492": 0.9300745112272497, "47074": 0.9344197821633763, "8473": 0.2934786063243561, "3280": 0.0, "12578": 0.9302965034863026, "45470": 0.8893152630591292, "198156": 0.8787526701448312, "36012": 0.895291400466873, "53292": 0.5429269301023953, "44716": 0.9296812231932067, "13193": 0.308505420852464, "133752": 0.8734354159245696, "12479": 0.3486675030653742, "15318": 0.8787616595856093, "12576": 0.15204481848946655, "8447": 0.5994618572988372, "46573": 0.9279372716822503, "2116": 0.4272180340231062, "13703": 0.5923670370027188, "13188": 0.7530171495692004, "42152": 0.9285967178532135, "62874": 0.7133615676685773, "35807": 0.5879993212972212, "36493": 0.87911717730691, "203523": 0.0, "16509": 0.9388086753546621, "393552": 0.8787470517443448, "33616": 0.3485363504893065, "48039": 0.9356824240326705, "8717": 0.711991781065302, "44020": 0.7251101527228269, "3549": 0.46863141921076146, "9304": 0.9345911716556844, "53667": 0.9413877224465212, "43317": 0.8999406797600005, "53508": 0.8985777581008907, "11013": 0.8939656131416635, "4766": 0.9222503267099883, "9050": 0.6020646502811081, "4768": 0.9344332663245435, "20500": 0.9393032958660933, "12611": 0.9298412767482181, "49409": 0.9314993375905827, "62567": 0.40366399924869534, "23028": 0.9342315586488119, "198385": 0.6848910783816767, "6702": 0.9373492161769481, "60876": 0.5502818751523991, "57963": 0.7423390300168664, "42695": 0.5555028945777837, "199417": 0.686188735556497, "41440": 0.9012938801759983, "26599": 0.08419173128763625, "20507": 0.7140515072482985, "35244": 0.9306825400712063, "23881": 0.939623544693814, "13101": 0.9398460737163765, "33028": 0.2982224504541353, "54934": 0.34861798819721357, "16202": 0.9364008301748559, "19255": 0.934692836427012, "24466": 0.9357429900894638, "198203": 0.9029996049062725, "133229": 0.6684027619310585, "132335": 0.9576271472122059, "209": 0.1454914584176335, "51819": 0.6368726634476978, "29870": 0.8949606318677923, "18712": 0.41512675673337207, "32329": 0.8950224617560634, "16591": 0.4479375800943135, "29182": 0.9378971706939652, "16391": 0.39847381769189366, "24940": 0.9365219107283653, "35411": 0.9319252123474464, "38197": 0.9367317594610619, "15774": 0.6910248674151126, "6866": 0.9349268576860984, "41676": 0.929582688654886, "29471": 0.6936342398809798, "196750": 0.9319159137870627, "43557": 0.4920123200285864, "4713": 0.22711748415995986, "12688": 0.5409721855465524, "201292": 0.8787448043841503, "25795": 0.5861820881852908, "42575": 0.5670479364560189, "1680": 0.937500912990079, "47530": 0.9039219806434866, "21017": 0.9004902616264371, "18624": 0.469385298566866, "61272": 0.9295946998257172, "199118": 0.9296250391883434, "29802": 0.6704306564285677, "34892": 0.9309453633026307, "27357": 0.7499328601141884, "25486": 0.9356805512325085, "30058": 0.5929390190048015, "15600": 0.6021926015603822, "38895": 0.593647460304506, "1267": 0.9412270361926123, "20845": 0.9348523990008236, "60118": 0.9345647368959237, "1221": 0.9345093396878563, "8788": 0.9392381224204519, "33363": 0.7467981910931291, "24554": 0.889855753185914, "24557": 0.9360420192401139, "15657": 0.9296812231932067, "17676": 0.8831198660312133, "44265": 0.7012730171821924, "30836": 0.8851407914977869, "60117": 0.934680475945942, "15516": 0.5175650997640198, "2527": 0.8836684515776188, "199669": 0.7509052085943548, "20590": 0.9373391030560727, "29695": 0.485212901354544, "25926": 0.935399631208192, "31595": 0.943754192731363, "15682": 0.9042909811159713, "29691": 0.6862345830747679, "36903": 0.43090659633927497, "43679": 0.48419838699432166, "197019": 0.6970974219407529, "24964": 0.7428491807810251, "34300": 0.9034835805858333, "46457": 0.8787448043841503, "41754": 0.6368726634476978, "56630": 0.0, "20766": 0.6204871041062807, "25596": 0.31457733733229915, "2876": 0.6745361729478512, "1916": 0.7547776814153153, "760": 0.9292722036378019, "31200": 0.9303228995661379, "49743": 0.929991358900052, "41786": 0.6368726634476978, "24904": 0.5268060682190787, "8437": 0.5200560042160477, "9371": 0.8584301043847186, "9370": 0.8585146808813533, "2701": 0.8941347269963019, "42298": 0.9284867512498132, "21348": 0.8910108963259031, "49586": 0.42703664208429176, "37589": 0.43953983052656775, "41783": 0.9376941859668088, "12430": 0.9288255407991388, "12824": 0.9440710705187919, "45785": 0.9389336051140929, "48823": 0.8897490035766737, "21263": 0.5494718686776682, "14361": 0.9353792156729968, "44925": 0.5945559946647669, "12389": 0.9008729310293522, "51034": 0.9012999522617264, "9143": 0.4877549078040759, "59253": 0.9023302546625451, "5610": 0.29828074981523883, "25189": 0.9380056425744627, "5617": 0.2755582744867321, "5615": 0.8899531382796325, "198093": 0.6672450589438362, "29605": 0.9337369874280156, "200130": 0.49617916799744294, "35141": 0.7108862446623879, "6315": 0.8949316403660275, "137": 0.49155380198225657, "42610": 0.9034787519622968, "10753": 0.9401915649829818, "41887": 0.9037251166513123, "203734": 0.0, "22561": 0.13225152904769236, "58305": 0.9289845415329019, "31983": 0.7406433967500924, "198031": 0.8788976248773784, "59702": 0.2513481351966946, "62282": 0.9301430557131829, "23265": 0.940820263997402, "49367": 0.4189233952460014, "6876": 0.9372811211630538, "20115": 0.8883859518220921, "14051": 0.3438388994826952, "48666": 0.9370461888068664, "21581": 0.933479261921965, "47323": 0.9042927950755844, "18978": 0.9297329868990951, "197308": 0.3481478188122154, "201401": 0.9031567544972486, "39087": 0.7515648404540117, "8881": 0.6214786349872974, "197301": 0.44576585946549824, "6828": 0.9005003747473125, "3": 0.9401653951928942, "42655": 0.9300655217864716, "12312": 0.3635632458222242, "36049": 0.893889656761617, "35328": 0.9310341340303147, "47066": 0.8787448043841503, "6870": 0.903479250685164, "21232": 0.7342501094576246, "59675": 0.9368752096866318, "43859": 0.7012730171821924, "15732": 0.35000527988648145, "58130": 0.9323690659858663, "38935": 0.9345692316163127, "30176": 0.455333851592806, "41108": 0.36950309742418813, "32107": 0.894962130107922, "2933": 0.9358682058087519, "45538": 0.9353940128077057, "1239": 0.09590512745485039, "8121": 0.44407357231152056, "6677": 0.4284295342187019, "58277": 0.939225761939382, "57172": 0.9394051584592671, "33785": 0.9283328070764878, "7029": 0.6195387323192794, "35518": 0.7322540011439064, "5483": 0.7027685900897741, "10929": 0.658593369124123, "9009": 0.9348324555515155, "9008": 0.5133280145345513, "12406": 0.9322937794193495, "57858": 0.775999932451971, "56510": 0.9354142390494565, "16125": 0.9318386889799569, "20021": 0.5675160166689044, "6775": 0.7343687670869605, "46261": 0.934515294971644, "39608": 0.932011481120445, "6772": 0.6798916322914197, "3790": 0.9018881196674357, "15830": 0.9307152680948926, "43289": 0.9357189436358317, "15836": 0.9444632348727376, "50613": 0.49388605659077706, "44068": 0.9377349512135498, "21637": 0.8787459280642476, "44066": 0.7327248496045776, "11290": 0.7405781623345776, "13037": 0.9335941106450284, "13030": 0.6886356679119259, "50618": 0.39543013911021624, "48707": 0.9295823393446473, "9002": 0.5801267955392324, "8218": 0.9297089291884871, "32097": 0.878749860944588, "55053": 0.8790077455269104, "21040": 0.8875061806021116, "48031": 0.936853673254054, "24955": 0.7343661710868991, "15943": 0.9389706865573026, "15085": 0.8872926388840509, "24956": 0.5974494709152262, "15083": 0.49894972404522436, "29": 0.7204194023595034, "38987": 0.6356269239935936, "2586": 0.88846014250511, "4385": 0.49942523763024854, "7657": 0.9356794275524113, "250": 0.9296564992170837, "60781": 0.5264091785212949, "5432": 0.8900193904832787, "13489": 0.7795137386747092, "47800": 0.9320106120348386, "51395": 0.9005441982711058, "1426": 0.8965259182432835, "16086": 0.6093800828153696, "42038": 0.9004902616264371, "59682": 0.9327623540199094, "59686": 0.20896100214162142, "44869": 0.49199771218732197, "34224": 0.9348345340551467, "47610": 0.5069033286775522, "42831": 0.539551603728022, "44581": 0.47053052929420625, "37153": 0.9335069907146682, "45447": 0.9369334545409598, "29422": 0.646246763186381, "11427": 0.7235304150505071, "11426": 0.7229367975962663, "10318": 0.8973574415152601, "1213": 0.5368599699090464, "9105": 0.9344602346468779, "7922": 0.42424796744952276, "9136": 0.46939765904793596, "21226": 0.9004936326667289, "73": 0.7412142262395034, "34171": 0.9292702623726736, "31027": 0.4927920792382769, "28715": 0.478285443960388, "10316": 0.47711344561893987, "2588": 0.6629948546688346, "16347": 0.9302867722569127, "42116": 0.6368726634476978, "60414": 0.6450856412786131, "13354": 0.692730407665984, "38843": 0.9366401740355734, "167": 0.7478304546522041, "25255": 0.9304551715405395, "202018": 0.4482731877758205, "5650": 0.44735862531073706, "49544": 0.9305715933355084, "50448": 0.9374942115069699, "42473": 0.9582620209226952, "4685": 0.8740139193503937, "61382": 0.9302285104379676, "42244": 0.6931443153585719, "14420": 0.7764269894475202, "4760": 0.939767375746264, "27699": 0.08419173128763625, "198717": 0.8787810034840207, "41843": 0.6368726634476978, "36252": 0.8787717727064847, "7992": 0.6868020161608233, "52022": 0.9181309154734121, "15497": 0.9298912897600525, "2518": 0.8585731861309042, "1103": 0.5251769354357175, "23005": 0.631245994617449, "2514": 0.9366482650986957, "197043": 0.6901023198154912, "2516": 0.859124227921259, "286": 0.12353814376126836, "2510": 0.8577766498656823, "43082": 0.9358266296451531, "62403": 0.7284267467326192, "46844": 0.6046838321249698, "49895": 0.4213816578497792, "46841": 0.8787464899042962, "49320": 0.9376469914027236, "33182": 0.9345265097207354, "34779": 0.7022819326369636, "35425": 0.4732015094946502, "39288": 0.932469073514523, "55470": 0.9285901298187617, "198889": 0.33867605763579955, "13184": 0.5504156392418907, "47069": 0.8949808581095431, "21250": 0.4518094302921666, "31463": 0.9286103560605125, "8560": 0.4518582284896295, "8401": 0.9285140573310021, "8402": 0.8998547046305455, "17746": 0.8974636292844518, "49713": 0.9097662408293659, "42682": 0.6368726634476978, "12129": 0.7798092665402901, "23138": 0.20777182102472883, "27747": 0.5145376112583756, "197226": 0.9296025655863981, "48971": 0.8789371671542778, "30217": 0.886386390885606, "10489": 0.6314629629456852, "42926": 0.9451969979762521, "2033": 0.8787459280642476, "36086": 0.8864964272624751, "9": 0.9348063281168357, "10481": 0.8973613743956006, "12350": 0.48292749569654403, "50923": 0.9373305665351951, "6517": 0.9284086554830534, "28769": 0.5409721855465524, "44684": 0.928916090230043, "196653": 0.46226176577337846, "44136": 0.5220426706280136, "3651": 0.08485245518482852, "14907": 0.42483513692194697, "6730": 0.5200568136733155, "63157": 0.9346204007993741, "29278": 0.8852004770172025, "26347": 0.9355518857463044, "11557": 0.2066016165069427, "34702": 0.6633533086198624, "20473": 0.9402484610772648, "62317": 0.621216428652494, "52284": 0.7555209212378909, "42868": 0.0, "9044": 0.6616106028982988, "6893": 0.901466739630961, "197988": 0.7155729700999963, "6428": 0.5325893447409337, "55286": 0.9399157015191031, "9318": 0.8939753427894984, "43711": 0.8851441625380787, "3221": 0.6127016733619702, "42841": 0.9312446169717985, "3223": 0.9348338107087661, "36077": 0.9287305898309198, "55772": 0.9368778809212552, "13272": 0.6634190054501768, "50297": 0.9374065238619087, "803": 0.9012870650879506, "49352": 0.9318409363401514, "44634": 0.9297480349691022, "15169": 0.5588059822291288, "44454": 0.36872499119140334, "16097": 0.5691739593212145, "22773": 0.8802468068798115, "22772": 0.903528130769395, "56322": 0.7024967048081148, "47165": 0.691011880688524, "39473": 0.8848712619392464, "766": 0.6620518917571052, "54728": 0.8787448043841503, "2840": 0.51515226427158, "3320": 0.09625634843591943, "58302": 0.3834535858317424, "41668": 0.6368726634476978, "3323": 0.49090212409248785, "20718": 0.45076909664742426, "54290": 0.5226738586687311, "17924": 0.9365472745049713, "25513": 0.43803634655642615, "20278": 0.6476737115992672, "3329": 0.5268153256701774, "41661": 0.6368726634476978, "26827": 0.5205695613716892, "6714": 0.9362311544801687, "6871": 0.9359665148570482, "62639": 0.9279462611230284, "1659": 0.9370514409511728, "12392": 0.9285124834085345, "9737": 0.8892691921751412, "55536": 0.9292647869568617, "20375": 0.8798156715168445, "43561": 0.9358201523628963, "12876": 0.5222711733848903, "29076": 0.7989067049059343, "13213": 0.945013551269935, "33984": 0.6778206898721589, "52201": 0.9325394256439039, "48514": 0.38768761243823974, "52207": 0.6368726634476978, "8220": 0.5153416550633254, "57286": 0.46938305120667145, "12083": 0.8940255300340076, "679": 0.9292722036378019, "30764": 0.934766716520607, "577": 0.5039516887691172, "49505": 0.9375134975022764, "200533": 0.9427968172884925, "47236": 0.9015229236358243, "5518": 0.9296196119400317, "28481": 0.8171682587340845, "41715": 0.7321753435370978, "19940": 0.3903666668919353, "25454": 0.9318398126600542, "25512": 0.45826016374848105, "36351": 0.9374313506136164, "36352": 0.9399157015191031, "25106": 0.9322937794193495, "40788": 0.8919970070768122, "25515": 0.9034702612443858, "2856": 0.9357652834447181, "25899": 0.6143836004485744, "57169": 0.9363637487316461, "55": 0.720371084115321, "27725": 0.6099380515162377, "2497": 0.36633240163239683, "262933": 0.8969911218035514, "57230": 0.9345276554527139, "47447": 0.5511161098529908, "15594": 0.9303819543177305, "29518": 0.41882209568512746, "43350": 0.6920965596540959, "8708": 0.949236758027918, "31214": 0.9034691375642886, "8890": 0.930634103915688, "34102": 0.5771240381839913, "200019": 0.945065527404872, "9264": 0.9370119068533196, "23679": 0.9430833557132953, "31400": 0.517620789719277, "9269": 0.9343587564614141, "36850": 0.7603583640566199, "46887": 0.8794601578620717, "58010": 0.9303295618448294, "5607": 0.3355228642978759, "15435": 0.4958845686171656, "51515": 0.9005217246691605, "8684": 0.7081207236949298, "5769": 0.5880207485289765, "21211": 0.932279171578085, "12850": 0.4635016016524387, "21213": 0.6308486144462561, "2496": 0.8941347269963019, "63037": 0.8940830377118277, "12586": 0.9378301512585779, "5760": 0.520106040272599, "9145": 0.5871715667015729, "35916": 0.7306101260933472, "43234": 0.9344602346468779, "4804": 0.8740826556605946, "15672": 0.9090295435054383, "42621": 0.6100728931279096, "1851": 0.9355670595426847, "60422": 0.4457358025828911, "8334": 0.93764024932214, "25198": 0.9298059516840032, "13301": 0.9297767360014743, "1257": 0.5208466848942206, "57043": 0.7286926659485237, "3842": 0.934693596361258, "58073": 0.9155071224462965, "49112": 0.9286406954231387, "31103": 0.5429132253270139, "17098": 0.9089852831617661, "1901": 0.598107947452224, "45102": 0.935162534707669, "59491": 0.6366692030591258, "35598": 0.9045623376532513, "45671": 0.9358945611533201, "2603": 0.39114982550406024, "11955": 0.7234848016648444, "34781": 0.6878979528110851, "62292": 0.885175678645867, "54540": 0.3403862280111347, "55720": 0.9396018810340345, "45634": 0.9366165767535309, "50989": 0.62992383698103, "8359": 0.441197361850047, "5408": 0.49090212409248785, "3262": 0.48888468933917056, "3265": 0.8798423686500867, "43205": 0.9427619832054772, "200651": 0.9374537184259939, "34743": 0.9319420675489054, "200185": 0.46938305120667145, "42825": 0.9004902616264371, "201719": 0.8769615240697896, "16863": 0.878756041185123, "19165": 0.8939595385466923, "5089": 0.9489530333991847, "852": 0.514115201994227, "30962": 0.4446794005503833, "22989": 0.9285013590910777, "11351": 0.7227745154490764, "60630": 0.2982224504541353, "51059": 0.9284878749299105, "33387": 0.8787504227846366, "12322": 0.9286985457928159, "3356": 0.35014646354026785, "23387": 0.5555564295289646, "43139": 0.9395506303408359, "50113": 0.9181410285942875, "35728": 0.43803297551613435, "7545": 0.9402808975507145, "61046": 0.5862677302673347, "198310": 0.9176859381548949, "6830": 0.48780463218706954, "40193": 0.557378140596583, "15895": 0.890480320149696, "197922": 0.5264987737264422, "51904": 0.751043170483885, "3352": 0.07671470669035733, "36149": 0.3788970630373298, "9031": 0.43435047427083034, "58269": 0.9318622862619995, "12637": 0.5424599214319209, "35662": 0.9348308597007193, "22422": 0.8787459280642476, "59764": 0.9302734026044658, "12620": 0.5488975012725678, "42525": 0.44616501451064, "12737": 0.0, "1739": 0.3834209991089217, "3215": 0.0499889454936501, "3216": 0.8911412506046672, "133579": 0.8968911142748949, "5739": 0.9345827157774799, "197595": 0.5510633455322, "2108": 0.490894258331807, "31250": 0.9427947654257026, "29252": 0.933078108127241, "11814": 0.6185844736233348, "13127": 0.7105742708594505, "8820": 0.48064039508651657, "8821": 0.6878078822148305, "13122": 0.6024441487608215, "32244": 0.540091764075551, "30164": 0.9100055846900834, "51731": 0.9361850835961808, "201011": 0.5419239425889365, "198414": 0.9325353706402617, "13045": 0.586573371253791, "5563": 0.9375376875293578, "44306": 0.49679256556764523, "202155": 0.9176331251903234, "19531": 0.6049621360978962, "8779": 0.9300473493879023, "15154": 0.7332495817100838, "29485": 0.9345866486578203, "53755": 0.8787481754244421, "50543": 0.6368726634476978, "60496": 0.43803634655642615, "29951": 0.9021510371894464, "7643": 0.9353962120696881, "17813": 0.9283957331619347, "22047": 0.47321652304162226, "50542": 0.6368726634476978, "18403": 0.9344746015732932, "15659": 0.9315034117236123, "41665": 0.764857579166072, "3786": 0.8950997908909033, "225": 0.7205705393202785, "224": 0.38346475765360466, "59504": 0.9181410285942875, "14618": 0.9381414106455205, "29550": 0.9349326152205442, "36436": 0.8787481754244421, "201270": 0.8902760095422914, "262463": 0.9357536362473922, "28573": 0.7172546879496, "42005": 0.9323583910249423, "12741": 0.4026864420805938, "8680": 0.4113186291035916, "51645": 0.6368726634476978, "29791": 0.9353839906198286, "43847": 0.9343433719167623, "30266": 0.9334781382418676, "19994": 0.7499328601141884, "44395": 0.3429235684034641, "111": 0.7203913103570718, "44397": 0.9322937794193495, "1741": 0.38345501101566715, "32748": 0.6687952913309204, "35100": 0.4519711034426187, "44734": 0.9042838056348063, "40475": 0.4205766052051109, "156": 0.7203901866769745, "197706": 0.9086279528908356, "12897": 0.5766274458922798, "48172": 0.9380036934934419, "8075": 0.9368160790770084, "20860": 0.5967951442883307, "52048": 0.9318589152217077, "12414": 0.5493496087104933, "40676": 0.9289382121101679, "39326": 0.46333601544488234, "25560": 0.28306476460544144, "16353": 0.8892161877576436, "34533": 0.6368726634476978, "3737": 0.48669916222402837, "20392": 0.39489826762239405, "47583": 0.9346490129032186, "28192": 0.9374346158643404, "5645": 0.929645664992334, "24961": 0.9301197971863454, "35415": 0.8893304327404422, "8100": 0.9282067986685084, "10474": 0.4404818897791288, "31034": 0.9376673102412684, "4694": 0.8839822773175059, "57494": 0.9323402997753764, "29670": 0.9332089878618525, "42708": 0.5483993521080875, "34168": 0.9004913853065343, "21396": 0.9323325071760203, "31148": 0.9373514635371427, "34820": 0.9407202564687454, "51815": 0.4470100558131904, "40065": 0.9350143549223365, "30722": 0.9288769380617014, "29073": 0.9389788533360177, "52423": 0.93530187103973, "57423": 0.7423390300168664, "201952": 0.6385424520722347, "23033": 0.9415068325368314, "30083": 0.41695386057152617, "53111": 0.8985386821503074, "4589": 0.9560787448874758, "49335": 0.9374005309013901, "48635": 0.9339088357003271, "9609": 0.8830361800062608, "9506": 0.9349536119115597, "50498": 0.6368726634476978, "197540": 0.9361067223779987, "12659": 0.7473641274118389, "39909": 0.9295351447805621, "8553": 0.9290783056051526, "12552": 0.49110076196370983, "8551": 0.9304078112803003, "37560": 0.6000159562573811, "25653": 0.39690127832382965, "6181": 0.5029534221376797, "46816": 0.8787448043841503, "9198": 0.9323432213436292, "34549": 0.9356776296642555, "8559": 0.9301048505898759, "21365": 0.43808241744041404, "8416": 0.9015251709960188, "54334": 0.8874286041758199, "35393": 0.2918983422396735, "42174": 0.532171523024767, "35395": 0.20622642991379106, "6461": 0.17722753731746252, "38478": 0.9376590876571409, "8997": 0.9020418996893366, "197216": 0.9427968172884925, "39194": 0.8884758740264717, "28753": 0.506606677131874, "200052": 0.934186639465991, "34145": 0.6910701624247475, "12161": 0.8869881215776918, "50837": 0.8791952950979569, "197288": 0.5522280890808634, "42892": 0.9049108191290806, "199374": 0.49199771218732197, "50392": 0.9373346083356837}

# To plot histogram of resiliency
data_list = data_map.values()
plot_data(data_list, 'blue')
