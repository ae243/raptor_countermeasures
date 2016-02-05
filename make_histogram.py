import sys
import numpy
import matplotlib.pyplot as plt
import collections

# usage: python make_graphs.py

def plot_data(data, color):
    n, bins, patches = plt.hist(data, 50, facecolor='green', alpha=0.75)
    plt.xlabel('Resilience')
    plt.ylabel('# of ASes')
    plt.title('Histogram of Tor-related AS Resiliency')
    plt.axis([0, 1, 0, 40])
    plt.show()

data_map = {"35540": 0.0, "20910": 0.45675893124040484, "41011": 0.4460608758401916, "18881": 0.5947648036394693, "35238": 0.3047714958052462, "39651": 0.3749290183031727, "8304": 0.6048561067597819, "48683": 0.6000097649072765, "6724": 0.5077025451412602, "5563": 0.6642975800035504, "10103": 0.6707298174131976, "8866": 0.35672873664890425, "21409": 0.42102820572662514, "14987": 0.6668912618081291, "29632": 0.7665343522359872, "21769": 0.30968445778545806, "57043": 0.44044357863012595, "3257": 0.302470009322807, "38895": 0.4715192214719592, "20857": 0.6130345055303521, "5650": 0.45035676756975845, "197288": 0.2650316968598787, "8905": 0.5843549824443565, "812": 0.5154746180642344, "18779": 0.7424784345374117, "2914": 0.32003353763323206, "719": 0.3370359700599792, "2852": 0.48304998332325905, "2854": 0.6121953269859193, "33885": 0.4342978275568186, "29854": 0.5062507848317991, "6848": 0.4175977558713068, "6849": 0.30518053828622704, "12705": 0.2801384728286723, "35530": 0.27079442179318375, "35533": 0.4553034362707707, "42516": 0.31509353899755566, "8468": 0.663777537456948, "41557": 0.40634972367279387, "6128": 0.47072789556378214, "23969": 0.4886413710800358, "49902": 0.30476400612268834, "30517": 0.5670815661606501, "6659": 0.0, "51167": 0.49314687020383957, "29456": 0.2842550839104823, "34934": 0.2822863412541753, "4739": 0.6693150063383342, "30693": 0.7004075620478515, "6799": 0.48393896606328923, "16276": 0.7173711097607, "23367": 0.4036791189368233, "32780": 0.6589349887584854, "21107": 0.18519156296777814, "199894": 0.0, "194": 0.2508530489577428, "2856": 0.5876386342654134, "8607": 0.7094918542008373, "25528": 0.3449845784665624, "30833": 0.5227177998623954, "50266": 0.6005298772830003, "6389": 0.46391994108128587, "37989": 0.18572016205123104, "19817": 0.6779814124993788, "5410": 0.35676615502650433, "12513": 0.3495440071678612, "14754": 0.4407428877374939, "196689": 0.43745642024193226, "2603": 0.432161913115487, "39301": 0.5802830875453536, "42352": 0.3781882015135175, "2381": 0.712348975935805, "1133": 0.4370171162917257, "51013": 0.3725145343260541, "43050": 0.5200674995145343, "34240": 0.29611714075240125, "15517": 0.664688232484201, "1403": 0.6837127774118903, "1102": 0.0, "15763": 0.4621377354282948, "41691": 0.7075616521934257, "1103": 0.6202023651506549, "46261": 0.6188526271022653, "12597": 0.3348114702286331, "8047": 0.5532842315386046, "197422": 0.5284678045671192, "40156": 0.45647598771540093, "9158": 0.3963015065720468, "24806": 0.4847186385773323, "20807": 0.6341233232969684, "18106": 0.7639452080872584, "8283": 0.5759295519292699, "103": 0.6378670893697382, "17547": 0.7036296302299815, "29169": 0.5636804033239073, "44869": 0.35685468563091755, "49562": 0.7334497695941222, "28717": 0.5597686735388131, "50463": 0.5106711606840295, "2044": 0.7429970331386699, "50465": 0.4887502300427076, "5577": 0.6785043377680972, "26615": 0.4267015571004621, "31": 0.5556833909016679, "15497": 0.48083444216806853, "28719": 0.2800924602465322, "1241": 0.318070832919617, "12083": 0.5230270448264801, "23148": 0.8447721967388825, "42730": 0.354527988738068, "6079": 0.3602158939479832, "10143": 0.5666894562707065, "2614": 0.41892506227597903, "35376": 0.35687360436248694, "9737": 0.6463602700470508, "32475": 0.6415542229161726, "2529": 0.3711053196578449, "9318": 0.7585501003685363, "44244": 0.4829165683676512, "27992": 0.7211644557159446, "34610": 0.29482754253026017, "16245": 0.35615204651793886, "40475": 0.6057266161428672, "8342": 0.6325879593074822, "10796": 0.14972460797911621, "42831": 0.4906569775206032, "38731": 0.5956674889915213, "3292": 0.4157611958088889, "558": 0.672455988911071, "197328": 0.27973955523369537, "8943": 0.4738128040577564, "32875": 0.6036694949397934, "24751": 0.47757312427597637, "45204": 0.3433232966669606, "41232": 0.6064252657256028, "5483": 0.6471000866469806, "12337": 0.5865160332966372, "46193": 0.5359107577607596, "36024": 0.6478943225625559, "57378": 0.5325030655650734, "35470": 0.5317980784661718, "15868": 0.46742769017963437, "9329": 0.687831340153208, "33604": 0.5105482741747759, "32613": 0.4799038663311546, "6805": 0.716561745961972, "41164": 0.4401401072566132, "25653": 0.44741620328152654, "48781": 0.6504871638928247, "13647": 0.39893662133979696, "34971": 0.3780351702936069, "20001": 0.14845142082196996, "4771": 0.43239758720198834, "29084": 0.5254882501367415, "3462": 0.6107860685728522, "13768": 0.7454164301748692, "6893": 0.6006024205082945, "3209": 0.6678472350227662, "13110": 0.4906448512455368, "14813": 0.30115107121598017, "2108": 0.21421428019517988, "18515": 0.49997158882298637, "39138": 0.6321345209321224, "13054": 0.36034718957018097, "13055": 0.6125984709317412, "2860": 0.2579653584955386, "63949": 0.0, "21021": 0.30683474889892776, "43948": 0.7591840516234571, "24971": 0.6501146460537859, "553": 0.4844431295104746, "24238": 0.5780806710972324, "16586": 0.728516743898107, "25019": 0.49915253076969573, "131": 0.474711822586998, "237": 0.3949384077359587, "4616": 0.5082987566266746, "43541": 0.6121665144330217, "11404": 0.6442513471261702, "11051": 0.6945586077757732, "54046": 0.7338637501476964, "47869": 0.7181870392212247, "29562": 0.3443926343369217, "55577": 0.3362007334959032, "9790": 0.4725494274496983, "30528": 0.11175292382952508, "1759": 0.180434613186919, "9370": 0.36619051022859483, "40749": 0.2563611812841626, "30158": 0.39829947037467506, "12025": 0.5727684509518797, "27229": 0.43644615638239614, "8167": 0.6721619354565526, "29580": 0.43391727745725905, "47215": 0.40101531573191185, "31127": 0.4752234335696538, "9443": 0.6336134797540283, "12880": 0.6742700975341555, "9116": 0.6094845113743256, "39351": 0.37840236912866554, "36375": 0.2610923900303373, "60781": 0.0, "11403": 0.7362148011639646, "25577": 0.4567073772040552, "47692": 0.6940523364998178, "1280": 0.8023391879798076, "36275": 0.6384922471580976, "26068": 0.7023975771786916, "23028": 0.6773462288207609, "8764": 0.6682572857201866, "15962": 0.5482834648784827, "3330": 0.5337846830007057, "42065": 0.4975616032619448, "15969": 0.4138521756218856, "17183": 0.3989391868809749, "680": 0.6784613722041817, "8426": 0.6952371710975126, "9120": 0.2733095404840746, "20676": 0.3666387326635093, "39792": 0.5200332427606913, "8422": 0.6322262881180057, "23205": 0.31829198712324247, "41268": 0.6468316401709641, "31342": 0.46795303445464437, "28917": 0.663404836418216, "45230": 0.4898331639696895, "21378": 0.28418673173092224, "137": 0.6736042348482575, "48815": 0.48372723345541574, "23089": 0.6449101465268, "34556": 0.46978499814591135, "198599": 0.463754224075285, "20773": 0.5945024676061237, "8542": 0.372498170388538, "35382": 0.3229285549994688, "10835": 0.8150713679001363, "1836": 0.710795567230101, "3595": 0.6536145700247851, "3790": 0.41399716088164934, "5588": 0.6408864992697333, "6327": 0.6174031203699577, "50821": 0.6110128511722379, "35017": 0.7981420524277304, "2152": 0.6661433867082156, "12271": 0.14805850323294245, "28745": 0.4707709802141425, "42005": 0.5487477823076631, "7753": 0.6898253172633607, "198185": 0.4456075977927802, "5384": 0.4699350011130846, "45753": 0.7062355406709481, "33480": 0.681513701878989, "31012": 0.6001941130850065, "33724": 0.5708370699467264, "18566": 0.3647496603533395, "45758": 0.7722710136393367, "11831": 0.4556355792720478, "13722": 0.7524035226486574, "28982": 0.10800038523581486, "8334": 0.4552295387029386, "35632": 0.30476400612268834, "6714": 0.01107460736650664, "30496": 0.40878254621892485, "35637": 0.35685468563091755, "50673": 0.6910947145452961, "12668": 0.64416313005685, "8877": 0.48782481015244944, "3243": 0.401487009792315, "18809": 0.3235680212368424, "3842": 0.17625751918184498, "8972": 0.33328517653654405, "38922": 0.5210563391578357, "51290": 0.36832999762422236, "19202": 0.5686238815773215, "32097": 0.6906437173398485, "701": 0.21849097790776148, "62207": 0.0, "14618": 0.6481075133374712, "3308": 0.17983267374460363, "12715": 0.6273709099957446, "5669": 0.4339142354627057, "14613": 0.6906205046398358, "27823": 0.3260533412464067, "49855": 0.2883992715916643, "13618": 0.25323506425346126, "21502": 0.4337341013919787, "197637": 0.4236530592719798, "11288": 0.1556693086886399, "32220": 0.1999319221497317, "1653": 0.2909989353229036, "19662": 0.6561982017411792, "15527": 0.3682892853224959, "25538": 0.4412430014415062, "31122": 0.6600031370389392, "47886": 0.0, "44988": 0.3953288206276935, "31246": 0.5245629337625157, "3741": 0.7475962169258541, "12993": 0.5294503180306483, "19969": 0.7297042670428968, "24560": 0.5197591666883538, "36236": 0.7040945228229518, "41733": 0.7042346284133043, "11696": 0.3259040982912623, "39309": 0.5956598869643911, "17971": 0.5375663983348392, "5408": 0.21363782557276312, "56617": 0.372629189272563, "29028": 0.5771971219647651, "34232": 0.5218742951903443, "47531": 0.5823334842390534, "33070": 0.5701339465417552, "39642": 0.3568736566754576, "46375": 0.4576783127011024, "12874": 0.6943498398131062, "12872": 0.6504574869570883, "13977": 0.3148762465687384, "20880": 0.5334868782236132, "49770": 0.2906068842483854, "20738": 0.3852730798908759, "47678": 0.27079442179318375, "20634": 0.7607800542817205, "49776": 0.37101368917598543, "15557": 0.516336413305719, "55329": 0.4335700396189575, "15003": 0.7709779188256546, "25229": 0.6945074521089155, "47206": 0.30476400612268834, "6739": 0.39193539356437174, "13285": 0.6684859360286197, "174": 0.362393087685161, "6921": 0.6104800118360028, "26669": 0.13730398863797272, "2118": 0.5555416276681931, "45570": 0.5959313902556825, "2119": 0.6093631348257778, "14536": 0.5295719468422825, "57172": 0.49356523212218034, "11013": 0.3906371962182671, "8615": 0.6038655359231195, "21844": 0.5950566898500046, "8612": 0.2981078161209127, "29691": 0.6514931889601617, "2116": 0.4844780413346357, "6364": 0.3990027325162907, "31333": 0.5230101215190474, "199558": 0.0, "34764": 0.656067928003448, "62378": 0.0, "20940": 0.8926287854416148, "45711": 0.22323235808586808, "53264": 0.7508940820831319, "17552": 0.4294389924229371, "201011": 0.0, "8477": 0.41601471828254344, "34568": 0.44532330018226174, "8473": 0.4977296525923852, "6400": 0.38711045434061103, "13213": 0.5996939760180158, "36012": 0.5907102877324645, "17": 0.4879389200739214, "39369": 0.46978499814591135, "13193": 0.5420034885568075, "19108": 0.4660119335693116, "5769": 0.4686586065541297, "53785": 0.28801261818144325, "35807": 0.41184072964103224, "48031": 0.3447976979629779, "47544": 0.467477982449301, "41075": 0.38183568087585273, "15879": 0.6780502480445504, "54665": 0.2861632878786974, "51399": 0.3048645563664484, "47381": 0.47976401485800063, "53667": 0.6358674634777369, "4765": 0.680267063008986, "16509": 0.865107711379459, "4766": 0.7944426193539064, "9050": 0.6149140638402322, "4768": 0.47090063519396475, "48133": 0.4154415316099272, "11398": 0.440027705314726, "29278": 0.5629283489022839, "47269": 0.4578970433963551, "57963": 0.5052507417286387, "43146": 0.5307711840136675, "8767": 0.6092150833723265, "26599": 0.5084293641008496, "20507": 0.617207135050638, "20495": 0.6475701565069745, "40244": 0.4553721774373219, "41454": 0.26141225573541554, "204274": 0.0, "35366": 0.6415349212588689, "8928": 0.6049686891495076, "18978": 0.7614294049625141, "16202": 0.49209970708729767, "52284": 0.4041304471136329, "51815": 0.5680235159789141, "2875": 0.3732696247409605, "15673": 0.6186447581123594, "209": 0.2824114010063726, "29873": 0.33152872062422145, "35361": 0.43741049782009633, "29182": 0.6915068438862254, "73": 0.4316653100825177, "3352": 0.5113855145988833, "22747": 0.5309402601804951, "4713": 0.1937473412951651, "6130": 0.7315626191323477, "1680": 0.5780473471982914, "33588": 0.46283327840723265, "30058": 0.6865281712726135, "34011": 0.6208320485226334, "8624": 0.4310603925849477, "1267": 0.7955346425942136, "33837": 0.3228295999872382, "1221": 0.2815924510445407, "45629": 0.7367542707360885, "33363": 0.36619556590170915, "15657": 0.4602340522992675, "17676": 0.583870513343149, "42038": 0.5641124204071755, "3651": 0.046423157385939606, "56813": 0.46692134537939217, "15516": 0.30483556743578927, "2527": 0.72129391753425, "11664": 0.329095476808912, "29695": 0.28090834106496865, "15682": 0.6530298483036637, "15685": 0.6846871945972786, "24900": 0.45815939547057566, "50716": 0.6057439183091105, "197019": 0.543057292470456, "46457": 0.6755193967509199, "24961": 0.5863972942763427, "1312": 0.27090633906486516, "8437": 0.12882327015931874, "9371": 0.3623972074252086, "45595": 0.4854919574151514, "12578": 0.726565685661102, "15425": 0.48467711242778133, "12436": 0.48951660595435786, "7961": 0.19889943743029084, "22927": 0.5114464721085628, "9822": 0.43875109478534263, "20766": 0.5166673198649524, "48823": 0.43564777257871695, "14": 0.5124680940126474, "1136": 0.355486422257232, "44925": 0.12629392444946758, "12389": 0.6670221352414899, "5610": 0.5102282256126067, "5617": 0.20333084278180277, "5615": 0.6199698408773109, "198093": 0.6284405854414494, "35141": 0.43427371486508165, "6315": 0.559814085506108, "16223": 0.4315200697076879, "42610": 0.5696317083111385, "31708": 0.628503253901308, "20931": 0.2968288510419541, "22561": 0.6009533364659545, "35425": 0.34192714389349055, "18618": 0.23027130134892526, "12576": 0.08830610814261854, "44266": 0.4704211694208986, "62282": 0.0, "8447": 0.6946600284455455, "48666": 0.44897848500202375, "20115": 0.7570815091377875, "34823": 0.35685513127727697, "47145": 0.28697308847560454, "22394": 0.22857435361035938, "21743": 0.46573917552474287, "56420": 0.5904696964576248, "44581": 0.31514929522097956, "133481": 0.0, "8881": 0.6517189041054245, "197301": 0.25430006145365674, "6828": 0.2803109325995277, "3": 0.6659632188325625, "12312": 0.26253164095729237, "36049": 0.32714966861251055, "20597": 0.6431306270562159, "22363": 0.7144095942598232, "2510": 0.6826978465353304, "6821": 0.5565103480096942, "38930": 0.41030133845109046, "44565": 0.2352582914168018, "38935": 0.15080912351248724, "30176": 0.3722607631351837, "16652": 0.38736898987902574, "1239": 0.23033400823681746, "27364": 0.4052216678167925, "6672": 0.5400939591030717, "33785": 0.4427621005581285, "7029": 0.6256350927385007, "2764": 0.28018301474658047, "16086": 0.4717394566789676, "9008": 0.307049277207522, "786": 0.4569199192852753, "29302": 0.3850059213368923, "39608": 0.5328182201145543, "49964": 0.3099932574997953, "15830": 0.8054808952069643, "43289": 0.5097869945275839, "31549": 0.4678914973776329, "50613": 0.3476650903678681, "44066": 0.6140866740885051, "13037": 0.28414702810173315, "13030": 0.7677986689164448, "50618": 0.6283730252748897, "8819": 0.36484098260102826, "8218": 0.41344074314807505, "25133": 0.6333787956600079, "21127": 0.471178152813143, "29944": 0.6533355155613545, "15085": 0.6947038312169225, "24956": 0.5531551939836129, "577": 0.43556664348982504, "59469": 0.36186649076745087, "250": 0.38919948878942956, "36223": 0.5385653270071725, "30036": 0.6639349125742966, "29017": 0.578247955215374, "13489": 0.515686600278089, "6939": 0.8157257757004787, "27866": 0.4092538419565921, "196752": 0.6151130134431898, "7155": 0.2875318570138337, "59686": 0.27210953789352643, "31334": 0.4056197028251991, "31042": 0.6683589147011944, "8121": 0.6697275567719344, "34224": 0.713867464402056, "48039": 0.6077545974027474, "29838": 0.7539607529260681, "37153": 0.5958481694370166, "29422": 0.5059526973065238, "11427": 0.14916724006496032, "11426": 0.14947983186619565, "10318": 0.39902375895126796, "20723": 0.6044520272366726, "9105": 0.42806708579618996, "7922": 0.6492414855177367, "8100": 0.4355167525710156, "35177": 0.42937115126943987, "34171": 0.6264968384995122, "9506": 0.5222558746961525, "57858": 0.5592276274525632, "49120": 0.5398899263561593, "32107": 0.5090927330032282, "13354": 0.40524369749787964, "167": 0.22978259296346507, "15467": 0.3704192430527273, "49544": 0.8394482207289152, "4685": 0.682649026273471, "57489": 0.47511140899293236, "5578": 0.423958625754084, "36252": 0.6561982017411792, "6503": 0.7201646457378118, "47241": 0.5683655726702836, "2518": 0.34381999902190763, "6058": 0.14615397771551855, "6775": 0.5840876895101413, "2514": 0.7172108053720062, "2516": 0.45002203081385556, "46664": 0.4923803469199901, "42322": 0.5584393360661893, "9433": 0.4558001503045164, "9617": 0.6948175502455561, "46841": 0.6906224771266032, "34779": 0.39027124483231973, "48235": 0.5614639763775933, "55470": 0.4123325576268953, "13184": 0.6071892149152427, "8560": 0.6769167037327718, "6535": 0.291152871111366, "20454": 0.49245345981747585, "8402": 0.7585833190803097, "17746": 0.4402925194322054, "18182": 0.5877454844544937, "12129": 0.4781647096934085, "16904": 0.7406191920496129, "12464": 0.35001881066089696, "27747": 0.5520507476761837, "10489": 0.21370729369050967, "46562": 0.7632531144778174, "31435": 0.5277870607661388, "9": 0.6669244447015524, "10481": 0.5268887743176861, "48309": 0.3909921958477424, "35816": 0.5632700983249558, "12357": 0.318065705474008, "393249": 0.4774416740269001, "5390": 0.6535538865239128, "58940": 0.0, "14901": 0.5871579920959135, "35492": 0.3231543021924873, "35228": 0.6102478264526581, "6730": 0.6560284406032985, "10508": 0.2167987786359703, "26347": 0.6919907998222148, "34702": 0.19318280654294495, "20473": 0.7843261543322674, "11492": 0.32356371600340617, "12605": 0.45178410514324424, "9044": 0.3580386479845343, "21412": 0.5431971978560901, "12714": 0.4765042666926148, "13703": 0.6225477412431615, "3226": 0.6041030464256093, "3549": 0.40802656141700366, "3223": 0.0, "26464": 0.6880950862126924, "46": 0.17721242343918803, "41440": 0.562770243709512, "24989": 0.6590725253887569, "30475": 0.741753836696356, "13170": 0.44279728805747554, "11841": 0.6647720138267376, "22773": 0.4874238822184623, "29492": 0.3717537904258214, "56322": 0.27378802065271673, "760": 0.21207297582582862, "41786": 0.515039517441391, "766": 0.6275691509678545, "47165": 0.6382365265141617, "2840": 0.4838086714539498, "3320": 0.26015160304456797, "54290": 0.0, "29194": 0.5161387706782822, "40092": 0.5379547060334043, "6876": 0.6774877219695109, "41661": 0.5325055061299924, "29208": 0.7122225542400888, "6871": 0.5597629751742922, "40824": 0.6773158599478788, "38758": 0.4420377573357982, "34533": 0.5325059183341138, "12676": 0.6377533332162109, "20375": 0.702540909853174, "19182": 0.39074667570398985, "33984": 0.5417093087415729, "15943": 0.5136334707184401, "52201": 0.6694069938516887, "286": 0.4648566219153215, "196968": 0.4363889328858513, "16462": 0.47744167402689996, "15500": 0.27990784424902854, "679": 0.21206788684348415, "30764": 0.5092806485926608, "38499": 0.1601833077115414, "20207": 0.3260853938610792, "24955": 0.7519725208718685, "38285": 0.5608026603521554, "41715": 0.5881159399945984, "36351": 0.7951108662659271, "36352": 0.7858290027764393, "40788": 0.707241238333119, "25899": 0.641769567244869, "57169": 0.6455121158873091, "12530": 0.6416610853303596, "17858": 0.5440476393658364, "31669": 0.47286028373302996, "29685": 0.4803415931596362, "2497": 0.3932308352778943, "60295": 0.0, "47447": 0.5841108124426807, "29518": 0.32559323874633866, "43350": 0.6079957882929253, "8708": 0.7133630604130854, "31214": 0.5268923750488662, "31400": 0.4033222245121854, "9269": 0.7326737621843012, "36850": 0.28801261818144325, "35041": 0.5351248286554676, "3061": 0.2297137110565224, "12859": 0.6940347392764538, "5607": 0.6120825378549799, "8681": 0.3692374504104513, "111": 0.38083719131487864, "5603": 0.37576412268665005, "5602": 0.6821514572574237, "9143": 0.6320401977726805, "16125": 0.4468366517557976, "12586": 0.5192229492521129, "9145": 0.6262784558711622, "35916": 0.4992004743826158, "4802": 0.5517117318656235, "50472": 0.4973488946052691, "4804": 0.531352966994329, "1853": 0.3685984088308903, "12392": 0.4571510543833893, "12390": 0.5532528408970369, "13301": 0.4975239031482472, "1257": 0.262502773205484, "17090": 0.21370729369050967, "24466": 0.44117485646149435, "23242": 0.6125898313621244, "12093": 0.5150171959021651, "31103": 0.4958243080405452, "1901": 0.48512968071456225, "42964": 0.38183568087585273, "42965": 0.29864185346236805, "5432": 0.5063242569915966, "35612": 0.554428961077226, "22653": 0.6282154457293403, "20712": 0.48413690524510355, "35592": 0.5874687748375069, "9082": 0.45581316298104496, "8359": 0.7501166111318802, "8455": 0.5519111372764167, "3265": 0.7341784239309658, "18712": 0.3430260031272824, "21599": 0.40871890704224917, "3269": 0.518753989034181, "46816": 0.6384922471580976, "42825": 0.27990784424902854, "47155": 0.6086898922200942, "51054": 0.5536403619919625, "19165": 0.7150309710283186, "5089": 0.5774338522438022, "57239": 0.36107716206581136, "852": 0.4637505392042417, "8896": 0.39777916592604307, "11351": 0.1487143668205791, "51059": 0.2912811984483334, "33387": 0.4644522263678752, "12322": 0.5538521498602098, "55430": 0.5429126419224762, "35415": 0.6613867088300839, "31364": 0.3830262094619563, "23387": 0.5442381570065714, "50113": 0.36440580999112016, "7545": 0.7811932753038212, "22030": 0.5207664980203459, "6830": 0.6328482546707166, "15895": 0.6806360641657861, "40191": 0.7001215251855735, "197922": 0.3854935413035362, "41508": 0.22844616539350765, "29314": 0.6644551613087991, "15747": 0.4707492288492708, "7018": 0.24947287008283278, "35662": 0.6768639986752188, "6167": 0.4263575823311535, "3215": 0.08867306494316, "3216": 0.7545407344831413, "39756": 0.40192631830122433, "49879": 0.37356341218382294, "29256": 0.29054356076088733, "13127": 0.4624968889609041, "13124": 0.497452810657133, "12338": 0.45182267624620726, "198414": 0.41357312972553717, "8339": 0.5697905345371677, "8779": 0.49515509932844515, "33843": 0.2929133586453769, "18047": 0.5422247927486339, "46475": 0.5428757029629698, "30640": 0.5828750718631981, "24940": 0.727185908913908, "25720": 0.5967058113663396, "17813": 0.521813486393482, "16186": 0.3042621451756623, "15659": 0.1805249011224421, "25795": 0.6532354127779365, "16637": 0.7485005087522516, "224": 0.27426527366911646, "13237": 0.6794994650277248, "20248": 0.5914409954497404, "28573": 0.5416224360451714, "197043": 0.6663071904306315, "42003": 0.19996909218487804, "43847": 0.0, "30266": 0.5462065047024938, "19994": 0.5892265052838703, "34218": 0.0, "10929": 0.5513009386530177, "2683": 0.49522681026201126, "6697": 0.7459359492536413, "7065": 0.6526316417833646, "11232": 0.5055041822907362, "32748": 0.5919593156801951, "48475": 0.5430723729307333, "44734": 0.44942185778623406, "12898": 0.37324560153402103, "2586": 0.3322973901509455, "12897": 0.6701519841737907, "48172": 0.6684657849114229, "20860": 0.42387305828130595, "52048": 0.38895621259777147, "12414": 0.7069751776868541, "28685": 0.6740913547499748, "39288": 0.1953556033577746, "40459": 0.5469257442118564, "17511": 0.6951666228535774, "5645": 0.7391947972441177, "35475": 0.6307324525337176, "4922": 0.3149244240516556, "42708": 0.7703305563472526, "3303": 0.6159840344083286, "31148": 0.546590030024655, "17216": 0.4668767107003883, "1299": 0.3006557662048287, "9031": 0.41962838558379123, "30722": 0.44654541271155807, "29073": 0.6231196770344399, "31229": 0.37714675547932863, "3301": 0.18124748185552123, "23033": 0.4904207730725901, "30083": 0.2297137110565224, "49156": 0.46742769017963437, "9351": 0.5184854174880904, "49335": 0.597857449097832, "14517": 0.3012723480138053, "197540": 0.48957920282254713, "8551": 0.8444479736798005, "9198": 0.6544542038118062, "8559": 0.3917919605926123, "21366": 0.43688761383316177, "197197": 0.47065280918067465, "30880": 0.6802655735997469, "50010": 0.5999589367932963, "6461": 0.31512369711510824, "38478": 0.6771760312035504, "8997": 0.5983886772620919, "27699": 0.3893444801100758, "28753": 0.37182314594656746, "34145": 0.5672886456328969, "57381": 0.5639546952099421, "4581": 0.763657468222408, "28615": 0.4933116945791006}

# To plot histogram of resiliency
data_list = data_map.values()
plot_data(data_list, 'blue')