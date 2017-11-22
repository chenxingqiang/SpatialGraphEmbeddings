from algRealEmbeddings import *
#import time
from random import uniform
import copy

v2, v3, v1 = [0, -2.3418234786589167, 0], [0, 6.327508996139455, 0], [3.697464444401205, 0.017900844941222793, 0]
v4 = [3.2930168732119, -0.157944798200452, -1.95429223125632]
v5 = [2.82039958291193, 0.679610905369317, -1.67465679235168]
v6 = [2.47296030555702, 0.342686069384568, -1.46758104891375]
v7 = [-2.63035589169772, 0, -10.6657888907962]
v8 = [1.0, 1.0, 1.0]
a = -0.1
b = 0.1

#v1 = [uniform(a, b), uniform(a, b), uniform(a, b)]
#v7 = [uniform(a, b), uniform(a, b), uniform(a, b)]
#
#v2 = [1.0+uniform(a, b), uniform(a, b), uniform(a, b)]
#v5 = [1.0+uniform(a, b), uniform(a, b), uniform(a, b)]
#
#v3 = [uniform(a, b), 1.0+uniform(a, b), uniform(a, b)]
#
#v6 = [uniform(a, b), uniform(a, b), 1.0+uniform(a, b)]
#
#v4 = [1.0+uniform(a, b), 1.0+uniform(a, b), uniform(a, b)]
#
#v8 = [ 1.0 + uniform(a, b),uniform(a, b), 1.0+uniform(a, b)]


#v1 = [uniform(a, b), 1.0 + uniform(a, b), uniform(a, b)]
#v8 = [uniform(a, b), 1.0 + uniform(a, b), uniform(a, b)]

#v4 = [-1.0+uniform(a, b), uniform(a, b), uniform(a, b)]
#v2 = [-1.0+uniform(a, b), uniform(a, b), uniform(a, b)]

#v3 = [1.0+uniform(a, b), uniform(a, b), uniform(a, b)]
#v5 = [1.0+uniform(a, b), uniform(a, b), uniform(a, b)]

#v6 = [uniform(a, b), 0.5 + uniform(a, b), 1.0+uniform(a, b)]

#v7 = [uniform(a, b), 0.5 + uniform(a, b), -1.0+uniform(a, b)]

def dist( u, v):
    return float(np.sqrt( (u[0]-v[0])**2 + (u[1]-v[1])**2 + (u[2]-v[2])**2))

lengths = {
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

#lengths = {(1, 2): 4.386290254987835, (4, 7): 10.5579448289947, (2, 6): 2.1695833997369136, (4, 5): 1.6940062148563753, (2, 8): 16.83405853179157,
#           (1, 4): 1.8084396572052768, (1, 3): 11.026883517351973, (1, 6): 5.8450130495737325, (3, 7): 13.787489684821617, (5, 8): 13.075209742298672, 
#           (2, 7): 11.232184203671995, (6, 8): 18.368267879186273, (1, 5): 2.00289249524296, (7, 8): 18.762183274653285, (5, 7): 10.536273659997796, 
#           (5, 6): 5.918182159410676, (2, 3): 11.29840753979362, (3, 4): 10.81796534240893}
#start = time.time()
#G = GraphEmbedding(lengths, 'Max8vertices')
#sols = G.findEmbeddings()
#print len(sols['real'])
#print len(sols['complex'])
#end = time.time()
#print 'Time: ' , end - start

lengths = {(1, 2): 3.2154982220265746, (4, 7): 17.87967729573084, (2, 6): 1.0237800945583875, (4, 5): 17.84906203635929, (2, 8): 1.0222718473388588, 
           (1, 4): 18.1376750081305, (1, 3): 9.972794388417462, (1, 6): 3.032569805432945, (3, 7): 9.215048223037243, (5, 8): 0.09782324287506733,
           (2, 7): 1.436434819135262, (6, 8): 0.044659851199770367, (1, 5): 3.032338165266229, (3, 4): 19.765613007713764, (5, 7): 1.0123496857434562, 
           (5, 6): 0.09495461781471154, (2, 3): 8.476438875510395, (7, 8): 1.0091111235946963}

lengths = {(1, 2): 3.2154982220265746, (2, 7): 1.436434819135262, (4, 7): 17.87967729573084, (2, 6): 1.0237800945583875, (6, 8): 0.04465985119977037, 
           (4, 5): 17.84906203635929, (2, 8): 1.0222718473388588, (5, 7): 1.0123496857434562, (7, 8): 1.0091111235946963, (1, 4): 18.1376750081305,
           (1, 5): 3.032338165266229, (1, 3): 9.972794388417462, (1, 6): 3.032569805432945, (5, 6): 0.09495461781471154, (3, 7): 9.215048223037243, 
           (3, 4): 19.765613007713764, (2, 3): 8.476438875510395, (5, 8): 0.09782324287506733}
           
alg = AlgRealEmbeddings('Max8vertices', name='8vert')
#alg.findMoreEmbeddings(lengths)

#start = time.time()
#G = GraphEmbedding(lengths, 'Max8vertices')
#sols = G.findEmbeddings()
#print len(sols['real'])
#print len(sols['complex'])
#end = time.time()
#print 'Time: ' , end - start



new_lengths = copy.copy(lengths)
#n_L = {}
#for e in lengths:
#    print e,  lengths[e]
#    m,  Ls = alg.sampleEdge(lengths, e, 50)
#    print m,  Ls
#    n_L[e] = [m, Ls]
##    if Ls:
##        new_lengths[e] = sum(Ls)/float(len(Ls))

#print n_L

n_L = {(1, 2): [96, [3.214648729657953, 3.230452288093884, 3.246255846529815, 3.2620594049657456, 3.2778629634016765, 3.2936665218376073]], (2, 7): [96, [1.3814359510899563, 1.3972395095258874, 1.4130430679618184, 1.4288466263977495]], (4, 7): [96, [17.88035095820198]], (2, 6): [0, []], (6, 8): [96, [0.03813348403581635]], (4, 5): [96, [17.84874384133012]], (2, 8): [0, []], (5, 7): [0, []], (1, 4): [96, [18.101600776305006, 18.117404334740936, 18.133207893176866, 18.149011451612797]], (1, 5): [0, []], (1, 3): [96, [9.28321516905548, 9.29901872749141, 9.31482228592734, 9.33062584436327, 9.3464294027992, 9.362232961235131, 9.378036519671062, 9.393840078106992, 9.409643636542922, 9.425447194978853, 9.441250753414783, 9.457054311850714, 9.472857870286644, 9.488661428722574, 9.504464987158505, 9.520268545594435, 9.536072104030366, 9.551875662466296, 9.567679220902226, 9.583482779338157, 9.599286337774087, 9.615089896210018, 9.630893454645948, 9.646697013081878, 9.662500571517809, 9.67830412995374, 9.69410768838967, 9.7099112468256, 9.72571480526153, 9.74151836369746, 9.757321922133391, 9.773125480569322, 9.788929039005252, 9.804732597441182, 9.820536155877113, 9.836339714313043, 9.852143272748974, 9.867946831184904, 9.883750389620834, 9.899553948056765, 9.899553948056798, 9.915357506492729, 9.93116106492866, 9.94696462336459, 9.96276818180052, 9.97857174023645, 9.99437529867238, 10.010178857108311]], (1, 6): [0, []], (5, 8): [0, []], (5, 6): [0, []], (3, 7): [96, [9.204197376875827, 9.220000935311758, 9.235804493747688, 9.251608052183618, 9.267411610619549, 9.28321516905548, 9.29901872749141]], (3, 4): [96, [19.65034950302625, 19.66615306146218, 19.68195661989811, 19.69776017833404, 19.71356373676997, 19.7293672952059, 19.74517085364183, 19.76097441207776, 19.77677797051369, 19.792581528949622, 19.808385087385552, 19.824188645821483, 19.839992204257413, 19.855795762693344, 19.871599321129274, 19.887402879565204]], (2, 3): [96, [8.398215896643343, 8.414019455079274, 8.429823013515204, 8.445626571951134, 8.461430130387065, 8.477233688822995]], (7, 8): [0, []]}
for e in lengths:
#    print e,  lengths[e]
    m,  Ls = n_L[e]
#    print m,  Ls
    if Ls:
#        new_lengths[e] = sum(Ls)/float(len(Ls))
        if abs(min(Ls)-lengths[e])<abs(max(Ls)-lengths[e]):
            new_lengths[e] = min(Ls)
        else:
            new_lengths[e] = max(Ls)


G = GraphEmbedding(new_lengths, 'Max8vertices')
sols = G.findEmbeddings()
print 'Embeddings after resampling:'
print len(sols['real'])
print new_lengths
#print len(sols['complex'])

   

alg = AlgRealEmbeddings('Max8vertices', name='8vertAfterResampling_bug_fixed')
alg.findMoreEmbeddings(new_lengths)










