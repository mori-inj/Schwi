from geo import *
import copy
import string

P = 'Point'
C = 'Circle'
N = 'new name'
axiom_list = {
        'eq_trans': [P,P,P],
        'cong_trans': [P,P,P,P,P,P],
        'eq_refl': [P],
        'cong_refl': [P,P],
        'eq_rev': [P,P],
        'eq_sub': [P,P,P,P],
        'circle': [P,P,P,N],
        'inside_circle': [P,P,P,P,C],
        'inside_circle_re': [P,P,P,P,C,N,N],
        'outside_circle': [P,P,P,C,P],
        'outside_circle_re': [P,P,P,C,P,N],
        'on_circle': [P,P,P,P,C],
        'bet_id': [P,P],
        'bet_sym': [P,P,P],
        'inner_trans': [P,P,P,P],
        'connectivity': [P,P,P,P],
        'null_seg1': [P,P,P],
        'null_seg2': [P,P],
        'null_seg3': [P,P,P,P],
        'five_line': [P,P,P,P,P,P,P,P],
        'ext1': [P,P,P,P,N],
        'ext2': [P,P,P,P,N],
        'pasch_inner': [P,P,P,P,P,N],
        'pasch_outer': [P,P,P,P,P,N],
        'line_circle': [P,P,P,P,P,C,N,N],
        'circle_circle': [P,P,P,P,C,C,P,P,P,P,N],
        'euclid5': [P,P,P,P,P,P,N],

        'lem_cong_sym': [P,P,P,P],
        'lem_cong_trans': [P,P,P,P,P,P],
        'lem_3_5b': [P,P,P,P],
        'lem_3_6a': [P,P,P,P],
        'lem_3_6b': [P,P,P,P],
        'lem_3_7a': [P,P,P,P],
        'lem_ext_uniq': [P,P,P,P],
        'lem_bet_not_eq': [P,P,P],
        'contrapos_lem_part_not_eq_whole': [P,P,P]
}



class Node:
    def __init__(self, axiom, depth, init_names, init_conds):
        self.child_set = Set([])
        self.axiom = axiom
        self.depth = depth
        self.names = copy.deepcopy(init_names)
        self.conds = copy.deepcopy(init_conds)
    def __hash__(self):
        hash_value = len(self.conds)
        for cond in self.conds:
            hash_value = hash_value ^ cond.__hash__()
        return hash_value
    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def proove(self, lev, end_cond):
        if lev is 0:
            return

        for axiom in axiom_list:
            param_list = []
            self.fill_params(0, axiom_list[axiom], [], param_list)
            for param in param_list:
                Geo.names = copy.deepcopy(self.names)
                Geo.conds = copy.deepcopy(self.conds)
                try:
                    exec 'G.'+axiom+'(*param)'
                except:
                    pass
                else:
                    self.child_set.add(Node(axiom, self.depth+1, Geo.names, Geo.conds))
                    """print str(axiom) +" "+ str(param)
                    for cond in Geo.conds:
                        print str(cond)"""
                    
        for child in self.child_set:
            print '   '*child.depth + child.axiom
            for cond in child.conds:
                print '   '*(child.depth+1)+'  ' + str(cond)
            child.proove(lev-1, end_cond)


    def fill_params(self, lev, param_format_list, cur_param_list, param_list):
        if len(param_format_list) is lev:
            param_list.append(copy.deepcopy(cur_param_list))  
        else:
            for nameX in G.names:
                X = G.names[nameX]
                if X.__class__.__name__ is param_format_list[lev]:
                    cur_param_list.append(nameX)
                    self.fill_params(lev+1, param_format_list, cur_param_list, param_list)
                    del cur_param_list[-1]
                elif param_format_list[lev] is N:
                    alphabet = set(string.ascii_uppercase)
                    alphabet = alphabet.difference(Geo.names.keys())
                    alphabet = sorted(list(alphabet))
                    new_name = alphabet[0]
                    cur_param_list.append(new_name)
                    self.fill_params(lev+1, param_format_list, cur_param_list, param_list)
                    del cur_param_list[-1]



class Schwi:
    init_names = {}
    init_conds = Set([])

    def set_init(self):
        G.clear()
        G.Point('A')
        G.Point('B')
        G.nEq('A','B')
        self.init_names = copy.deepcopy(G.names)
        self.init_conds = copy.deepcopy(G.conds)

    def check_conclusion():
        size = len(G.conds)
        ret = False
        for nameX in G.names:
            X = G.names[nameX]
            if X.__class__.__name__ is P:
                eqi = G.equilateral('A','B',nameX)
                if len(G.conds) > size:
                    G.conds.remove(eqi)
                tri = G.triangle('A','B',nameX)
                if len(G.conds) > size:
                    G.conds.remove(tri)
                if eqi in G.conds and tri in G.conds:
                    ret = True
                    break
        return ret

    def __init__(self):
        self.set_init()
        self.root = Node('init',0,self.init_names, self.init_conds)

    def proove(self):
        self.root.proove(2, self.check_conclusion)

G = Geo()
S = Schwi()
S.proove() 
