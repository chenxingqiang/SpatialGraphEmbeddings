from algRealEmbeddings import *

#lengths_7 = {(1, 2): 5.7322526571145165, (2, 7): 5.026767140924392, (4, 7): 1.5859742422378464, (2, 6): 4.942519597534114, (6, 7): 1.0460328780197365, 
#             (5, 6): 0.22790172904533793, (5, 7): 1.0571151960916287, (1, 4): 3.273043816331718, (1, 5): 3.0531426208724093, (1, 3): 3.308244239022385, 
#             (1, 6): 3.044838116183432, (4, 5): 1.3350982559642988, (3, 7): 4.116856477203278, (3, 4): 4.437418243490294, (2, 3): 6.488691014736114}
##             /home/jan/Research/MaximumReal3dEmbeddings/CouplerCurve/important/7vert/48_embd_from_16_random_TBR.txt
#name7 = '48_embd_from_16_random_TBR'
#lengths_7 = {(1, 2): 6.274873914397456, (2, 7): 12.093170928755793, (4, 7): 10.52881316000657, (2, 6): 10.479941653322763, (6, 7): 8.11321631042846, 
#             (5, 6): 9.459324566316262, (5, 7): 10.73159467196586, (1, 4): 1.9761239449935557, (1, 5): 2.8483166740669206, (1, 3): 1.9564840951854308, 
#             (1, 6): 9.4046159048512159, (4, 5): 2.313950594269001, (3, 7): 10.525064001461296, (3, 4): 0.47038007668728976, (2, 3): 5.952813550679546}
##/home/jan/Research/MaximumReal3dEmbeddings/CouplerCurve/important/7vert/48_embd_from_28_7vert_53129440.txt
#name7 = '48_embd_from_28_7vert_53129440'

#lengths_7 = {(1, 2): 3.2154982220265791, (2, 7): 1.4364348191352576, (4, 7): 17.879677295730822, (2, 6): 1.0237800945583886, (6, 7): 1.0148514465978793, 
#             (5, 6): 0.09495461781463814, (5, 7): 1.012349685743454, (1, 4): 18.137675008130483, (1, 5): 3.0323381652662267, (1, 3): 9.97279438841746, 
#             (1, 6): 3.0325698054329457, (4, 5): 17.849062036359275, (3, 7): 9.215048223037243, (3, 4): 19.765613007713743, (2, 3): 8.476438875510395}
##/home/jan/Research/MaximumReal3dEmbeddings/CouplerCurve/important/7vert/48_embd_from_20_random7vert_TBR_new_starting_point.txt
#name7 = '48_embd_from_20_random7vert_TBR_new_starting_point'

lengths_7 = {(1, 2): 3.6547267239838073, (2, 7): 10.931902209424029, (4, 7): 10.528964771703047, (2, 6): 12.36535326089277, (6, 7): 6.614718312956418, 
              (5, 6): 15.12587430560531, (5, 7): 13.990265768289897, (1, 4): 1.9423383670562493, (1, 5): 9.822922401885547, (1, 3): 1.9354608517198846, 
              (1, 6): 11.884171167050836, (4, 5): 9.723833100136652, (3, 7): 10.524273284504055, (3, 4): 0.5383946923429196, (2, 3): 3.283167602028824}
#/home/jan/Research/MaximumReal3dEmbeddings/CouplerCurve/important/7vert/48_embd_from_Vangelis28_all_subgraphs_draft.txt
name7 = '48_embd_from_Vangelis28_all_subgraphs_draft'
#
#lengths_7 = {(1, 2): 4.1414653501173975, (2, 7): 11.139850811829968, (4, 7): 10.523551385333088, (2, 6): 4.1677512911570815, (6, 7): 10.542828736351707, 
#              (5, 6): 1.0309584430720742, (5, 7): 10.533375487651346, (1, 4): 1.9363529242001118, (1, 5): 1.9873340498152834, (1, 3): 5.959257111560759, 
#              (1, 6): 2.0323899508242214, (4, 5): 0.4412801229952831, (3, 7): 11.949398151358958, (3, 4): 5.6557115598418122, (2, 3): 7.295330049669027}
##/home/jan/Research/MaximumReal3dEmbeddings/CouplerCurve/important/7vert/48_embd_from_Vangelis28_only_GUI_subgraphs_53183a41.txt
#name7 = '48_embd_from_Vangelis28_only_GUI_subgraphs_53183a41'
#
#lengths_7 = {(1, 2): 1.99993774567597, (2, 7): 10.53609172287933, (4, 7): 11.847062363994983, (2, 6): 1.001987710974071, (6, 7): 10.53647884635266, 
#              (5, 6): 4.444937549609401, (5, 7): 11.239645246227646, (1, 4): 5.79633829024753, (1, 5): 4.402427328037957, (1, 3): 1.9944376255112493, 
#              (1, 6): 2.000134247468136, (4, 5): 7.07440359713745, (3, 7): 10.536252631111296, (3, 4): 5.8856444203840832, (2, 3): 0.9982585379475678}
##/home/jan/Research/MaximumReal3dEmbeddings/CouplerCurve/important/7vert/48_embd_from_Vangelis28_MoreDirect_draft.txt
#name7 = '48_embd_from_Vangelis28_MoreDirect_draft'




G = GraphEmbedding(lengths_7, 'Max7vertices')
v1, v2, v3, v4, v5, v6, v7 = G.getEmbedding()

def dist( u, v):
    return float(np.sqrt( (u[0]-v[0])**2 + (u[1]-v[1])**2 + (u[2]-v[2])**2))

v8 = [0, 0, 0]

lengths_1st_phase = {
           (2, 1) : dist(v2,v1),
            (2, 7) : dist(v2,v7),
            (2, 6) : dist(v2,v6),
            (3, 1) : dist(v3,v1),
            (3, 7) : dist(v3,v7),
            (3, 2) : dist(v3,v2),
            (4, 1) : dist(v4,v1),
            (4, 7) : dist(v4,v7),
            (4, 3) : dist(v4,v3),
            (5, 1) : dist(v5,v1),
            (5, 7) : dist(v5,v7),
            (5, 4) : dist(v5,v4),
            (6, 1) : dist(v6,v1),
            (6, 5) : dist(v6,v5),
            (5, 8) : dist(v5,v8),
            (6, 8) : dist(v6,v8),
            (7, 8) : dist(v7,v8),
            (2, 8) : dist(v2,v8),
           }

all_comb = [[3, 7, 2, 4, 1], [6, 8, 2, 5, 1], [4, 5, 1, 7, 3], [8, 7, 2, 5, 6], [4, 3, 1, 7, 5], [6, 2, 1, 8, 5], [3, 2, 1, 7, 4], [8, 5, 7, 6, 2], 
                                  [4, 1, 3, 5, 7], [6, 5, 1, 8, 2], [3, 1, 2, 4, 7], [8, 2, 7, 6, 5], [4, 7, 3, 5, 1], [6, 1, 2, 5, 8], [3, 4, 1, 7, 2], [8, 6, 2, 5, 7]]

print '********************* 1st phase starts *****************************************'
alg = AlgRealEmbeddings('Max8vertices', name='8vert_from_7vert_1st_phase_'+name7)
name1st=alg._fileNamePref
lengths_2nd_phase = alg.findMoreEmbeddings(lengths_1st_phase, combinations=[comb for comb in all_comb if comb[0]==8], required_num=96)

print '********************* 2nd phase starts *****************************************'

alg2 = AlgRealEmbeddings('Max8vertices', name='2nd_phase_'+name1st)
alg2.findMoreEmbeddings(lengths_2nd_phase)

