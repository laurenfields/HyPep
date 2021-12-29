# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 16:46:42 2021

@author: lawashburn
"""

#This is a limited version of my PTM.py algorithm. This is for testing the code on a "smaller" scale prior to
#a long sequence with more PTMs. 

#this serves as the PTM values for the database
import itertools
from itertools import repeat
from itertools import product
import collections
from collections import defaultdict

all_combos = [] #appending all combos into a list

from User_input2 import lst_seq
for a in lst_seq:
    query = a

    #a dictionary of mods, all masses are in Da
    Hydroxylation = 16 #K,N,P
    Carboxylation = 44 #K,D,E
    Phosphorylation = 80 #S,T,Y
    Acetylation = 42 #K, X @ N term
    Lactylation = 71 #K
    Formylation = 28 #K, X @ N term
    Methylation =  14 #K,R, X at C term
    Dimethylation = 28 #K,R
    Trimethylation = 42 #K
    Sulfonation = 80 #Y, T ,S
    Citrullination = 31 #R
    Nitrosylation = 47 #Y
    Butyrylation = 70 #K
    Crotonylation = 68 #K
    Glutarylation = 114 #K
    Hydroxybutyrylation = 87 #K
    Malonylation = 125 #K
    Succinylation = 100 #K
    Glu_to_PyroGlu = 17 #Q, E
    #Homoserine_lactone = -48 #M
    #Homoserine = -30 #M
    #Dehydration = -18 #C
    #Loss_Ammonia = -17 #C
    Amidation = -1 #X at C-term
    Deamidation = 1 #N,Q
    Oxidation_or_Hydroxylation = 16 #W,H,M
    Sodium_adduct = 22 #D, E, X at C-term
    Dihydroxy = 32 #M
    S_carbamoylmethylcysteine_cyclization = 40 #C @ N term
    Carbamylation = 43 #K, X @ N term
    Ethanolation = 44 #C
    Beta_methylthiolation = 46 #C
    Iodoacetamide_derivative = 57 #C
    Iodoacetic_acid_derivative = 58 #C
    Acrylamide_adduct = 71 #C
    N_isopropylcarboxamidomethyl = 99 #C
    S_pyridylethylation = 105 #C
    Hexose = 162 #S,T
    N_Acetylhexosamine = 203 #N
    Myristoylation = 210 #K,C,G
    Biotinylation = 226 #K, X @ N term
    no_mod = 0 #allows for no modification to be present

    #lysine combinations
    k_instances = query.count('K')
    k_modifications = [Hydroxylation, Carboxylation, Acetylation, Lactylation, Formylation,
                    Methylation, Dimethylation, Trimethylation, Butyrylation, Crotonylation,
                    Glutarylation, Hydroxybutyrylation, Malonylation, Succinylation
                    ,Sodium_adduct,Carbamylation,Myristoylation,Biotinylation,
                    no_mod
                    ]
    k_combinations = itertools.combinations_with_replacement(k_modifications, k_instances)
    k_comb_l = list(k_combinations)
    k_comb_sum = ([sum(x) for x in k_comb_l])
    k_comb_sum_list = list(k_comb_sum)

    #asparaginine combinations
    n_instances = query.count('N')
    n_modifications = [Hydroxylation, no_mod, Deamidation, Methylation,
                       Sodium_adduct, Formylation, Acetylation,Carbamylation,N_Acetylhexosamine,
                       Biotinylation
                    ]
    n_combinations = itertools.combinations_with_replacement(n_modifications, n_instances)
    n_comb_l = list(n_combinations)
    n_comb_sum = ([sum(x) for x in n_comb_l])
    n_comb_sum_list = list(n_comb_sum)

    #proline combinations
    p_instances = query.count('P')
    p_modifications = [Hydroxylation, Methylation, Sodium_adduct,Formylation,
                       Acetylation,Carbamylation,Biotinylation,no_mod]
    p_combinations = itertools.combinations_with_replacement(p_modifications, p_instances)
    p_comb_l = list(p_combinations)
    p_comb_sum = ([sum(x) for x in p_comb_l])
    p_comb_sum_list = list(p_comb_sum)

    #aspartic acid combinations
    d_instances = query.count('D')
    d_modifications = [Carboxylation,Methylation, Sodium_adduct,Formylation,
                       Acetylation,Carbamylation,Biotinylation,no_mod]
    d_combinations = itertools.combinations_with_replacement(d_modifications, d_instances)
    d_comb_l = list(d_combinations)
    d_comb_sum = ([sum(x) for x in d_comb_l])
    d_comb_sum_list = list(d_comb_sum)

    #glutamic acid combinations
    e_instances = query.count('E')
    e_modifications = [Carboxylation,Glu_to_PyroGlu,Methylation,Sodium_adduct,
                       Formylation, Acetylation,Carbamylation,Biotinylation,no_mod]
    e_combinations = itertools.combinations_with_replacement(e_modifications, e_instances)
    e_comb_l = list(e_combinations)
    e_comb_sum = ([sum(x) for x in e_comb_l])
    e_comb_sum_list = list(e_comb_sum)

    #serine combinations
    s_instances = query.count('S')
    s_modifications = [Phosphorylation,Methylation,Sodium_adduct,Formylation, 
                       Acetylation,Carbamylation,Sulfonation,Hexose,Biotinylation,no_mod]
    s_combinations = itertools.combinations_with_replacement(s_modifications, s_instances)
    s_comb_l = list(s_combinations)
    s_comb_sum = ([sum(x) for x in s_comb_l])
    s_comb_sum_list = list(s_comb_sum)

    #threonine combinations
    t_instances = query.count('T')
    t_modifications = [Phosphorylation,Methylation,Sodium_adduct, Formylation,
                       Acetylation,Carbamylation,Sulfonation,Hexose,Biotinylation,no_mod]
    t_combinations = itertools.combinations_with_replacement(t_modifications, t_instances)
    t_comb_l = list(t_combinations)
    t_comb_sum = ([sum(x) for x in t_comb_l])
    t_comb_sum_list = list(t_comb_sum)

    #tyrosine combinations
    y_instances = query.count('Y')
    y_modifications = [Phosphorylation, Sulfonation, Nitrosylation,
                       Methylation,Sodium_adduct, Formylation,Acetylation,Carbamylation,Biotinylation,
                       no_mod]
    y_combinations = itertools.combinations_with_replacement(y_modifications, y_instances)
    y_comb_l = list(y_combinations)
    y_comb_sum = ([sum(x) for x in y_comb_l])
    y_comb_sum_list = list(y_comb_sum)

    #arginine combinations
    r_instances = query.count('R')
    r_modifications = [Methylation, Dimethylation, Citrullination,Sodium_adduct,
                       Formylation,Acetylation,Carbamylation,Biotinylation,no_mod]
    r_combinations = itertools.combinations_with_replacement(r_modifications, r_instances)
    r_comb_l = list(r_combinations)
    r_comb_sum = ([sum(x) for x in r_comb_l])
    r_comb_sum_list = list(r_comb_sum)

    #glutamine combinations
    q_instances = query.count('Q')
    q_modifications = [Glu_to_PyroGlu, Deamidation, Methylation,Sodium_adduct,
                       Formylation,Acetylation,Carbamylation,Biotinylation,no_mod]
    q_combinations = itertools.combinations_with_replacement(q_modifications, q_instances)
    q_comb_l = list(q_combinations)
    q_comb_sum = ([sum(x) for x in q_comb_l])
    q_comb_sum_list = list(q_comb_sum)
    
    #methionine combinations
    m_instances = query.count('M')
    m_modifications = [Methylation,Oxidation_or_Hydroxylation,
                       Sodium_adduct,Formylation,Dihydroxy, Acetylation,Carbamylation,Biotinylation,no_mod]
    m_combinations = itertools.combinations_with_replacement(m_modifications, m_instances)
    m_comb_l = list(m_combinations)
    m_comb_sum = ([sum(x) for x in m_comb_l])
    m_comb_sum_list = list(m_comb_sum)

    #methionine combinations
    c_instances = query.count('C')
    c_modifications = [Methylation,Sodium_adduct,Formylation, 
                       S_carbamoylmethylcysteine_cyclization,Acetylation,Carbamylation,Ethanolation,
                       Beta_methylthiolation,Iodoacetamide_derivative, Iodoacetic_acid_derivative,
                       Acrylamide_adduct,N_isopropylcarboxamidomethyl,S_pyridylethylation,Myristoylation,
                       Biotinylation,
                       no_mod]
    c_combinations = itertools.combinations_with_replacement(c_modifications, c_instances)
    c_comb_l = list(c_combinations)
    c_comb_sum = ([sum(x) for x in c_comb_l])
    c_comb_sum_list = list(c_comb_sum)
    
    
    #alanine combinations
    a_instances = query.count('A')
    a_modifications = [Amidation,Methylation,Sodium_adduct, Formylation,Acetylation,Carbamylation,Biotinylation,
                       no_mod]
    a_combinations = itertools.combinations_with_replacement(a_modifications, a_instances)
    a_comb_l = list(a_combinations)
    a_comb_sum = ([sum(x) for x in a_comb_l])
    a_comb_sum_list = list(a_comb_sum)
    
    #glycine combinations
    g_instances = query.count('G')
    g_modifications = [Amidation,Methylation, Sodium_adduct,Formylation,Acetylation,Carbamylation,
                       Myristoylation,Biotinylation,no_mod]
    g_combinations = itertools.combinations_with_replacement(g_modifications, g_instances)
    g_comb_l = list(g_combinations)
    g_comb_sum = ([sum(x) for x in g_comb_l])
    g_comb_sum_list = list(g_comb_sum)    
    
    #isoleucine combinations
    i_instances = query.count('I')
    i_modifications = [Amidation,Methylation,Sodium_adduct, Formylation,Acetylation,Carbamylation,
                       Biotinylation,no_mod]
    i_combinations = itertools.combinations_with_replacement(i_modifications, i_instances)
    i_comb_l = list(i_combinations)
    i_comb_sum = ([sum(x) for x in i_comb_l])
    i_comb_sum_list = list(i_comb_sum)     
 
    #leucine combinations
    l_instances = query.count('L')
    l_modifications = [Amidation,Methylation,Sodium_adduct, Formylation,Acetylation,Carbamylation,
                       Biotinylation,no_mod]
    l_combinations = itertools.combinations_with_replacement(l_modifications, l_instances)
    l_comb_l = list(l_combinations)
    l_comb_sum = ([sum(x) for x in l_comb_l])
    l_comb_sum_list = list(l_comb_sum)       
 
    #valine combinations
    v_instances = query.count('V')
    v_modifications = [Amidation, Methylation,Sodium_adduct,Formylation,Acetylation,Carbamylation,Biotinylation,
                       no_mod]
    v_combinations = itertools.combinations_with_replacement(v_modifications, v_instances)
    v_comb_l = list(v_combinations)
    v_comb_sum = ([sum(x) for x in v_comb_l])
    v_comb_sum_list = list(v_comb_sum)       

    #phenylalanine combinations
    f_instances = query.count('F')
    f_modifications = [Amidation,Methylation,Sodium_adduct,Formylation,Acetylation,Carbamylation,Biotinylation,
                       no_mod]
    f_combinations = itertools.combinations_with_replacement(f_modifications, f_instances)
    f_comb_l = list(f_combinations)
    f_comb_sum = ([sum(x) for x in f_comb_l])
    f_comb_sum_list = list(f_comb_sum)     

    #tryptophan combinations
    w_instances = query.count('W')
    w_modifications = [Amidation,Methylation,Oxidation_or_Hydroxylation, Sodium_adduct,
                       Formylation,Acetylation,Carbamylation,Biotinylation,no_mod]
    w_combinations = itertools.combinations_with_replacement(w_modifications, w_instances)
    w_comb_l = list(w_combinations)
    w_comb_sum = ([sum(x) for x in w_comb_l])
    w_comb_sum_list = list(w_comb_sum)       
    
    #histidine combinations
    h_instances = query.count('H')
    h_modifications = [Amidation,Methylation,Oxidation_or_Hydroxylation, Sodium_adduct,
                       Formylation,Acetylation,Carbamylation,Biotinylation,no_mod]
    h_combinations = itertools.combinations_with_replacement(h_modifications, h_instances)
    h_comb_l = list(h_combinations)
    h_comb_sum = ([sum(x) for x in h_comb_l])
    h_comb_sum_list = list(h_comb_sum) 
 
    ptm_list = []

    if k_instances != 0:
        ptm_list.append(k_comb_sum_list) #makes sure each AA is accounted for in mass
    if n_instances != 0:
        ptm_list.append(n_comb_sum_list)
    if p_instances != 0:
        ptm_list.append(p_comb_sum_list)
    if d_instances != 0:
        ptm_list.append(d_comb_sum_list)
    if e_instances != 0:
        ptm_list.append(e_comb_sum_list)
    if s_instances != 0:
        ptm_list.append(s_comb_sum_list)
    if t_instances != 0:
        ptm_list.append(t_comb_sum_list)
    if y_instances != 0:
        ptm_list.append(y_comb_sum_list)
    if r_instances != 0:
        ptm_list.append(r_comb_sum_list)
    if q_instances != 0:
        ptm_list.append(q_comb_sum_list)
    if m_instances != 0:
        ptm_list.append(m_comb_sum_list)
    if c_instances != 0:
        ptm_list.append(c_comb_sum_list)       
    if a_instances != 0:
        ptm_list.append(a_comb_sum_list)    
    if g_instances != 0:
        ptm_list.append(g_comb_sum_list)         
    if i_instances != 0:
        ptm_list.append(i_comb_sum_list)         
    if l_instances != 0:
        ptm_list.append(l_comb_sum_list)          
    if v_instances != 0:
        ptm_list.append(v_comb_sum_list)
    if f_instances != 0:
        ptm_list.append(f_comb_sum_list)
    if w_instances != 0:
        ptm_list.append(w_comb_sum_list)
    if h_instances != 0:
        ptm_list.append(h_comb_sum_list)
        
    #print(ptm_list)

    combos = list(itertools.product(*ptm_list))
    
    #print(combos)
    
    combos_comb_sum = ([sum(x) for x in combos])

    combos_comb_sum_list = list(combos_comb_sum)
    #print('the mass for', a,'equals',combos_comb_sum_list)

    all_combos.append(combos_comb_sum_list)
 

#for a in lst_seq:
 #   data.append(combos_comb_sum_list)
#print(data)