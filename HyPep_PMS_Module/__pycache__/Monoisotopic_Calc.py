# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 14:07:08 2021

@author: lawashburn
"""

#dictionary of amino acid masses
List_seq = [('AGRRAHIL'),('RAHLKMP')]
for a in List_seq:
    A = 89.10
    R = 174.20
    N = 132.12
    D = 133.11
    C = 121.16
    E = 147.13
    Q = 146.15
    G = 75.07
    H = 155.16
    O = 131.13
    I = 131.18
    L = 131.18
    K = 146.19
    M = 149.21
    F = 165.19
    P = 115.13
    S = 105.09
    T = 119.12
    W = 204.23
    Y = 181.19
    V = 117.15

for x in List_seq:
    mass_total = []
    a_instances = x.count('A')
    if a_instances != 0:
        mass_total.append(a_instances * A)
    r_instances = x.count('R')
    if r_instances != 0:
        mass_total.append(r_instances * R)
    n_instances = x.count('N')
    d_instances = x.count('D')
    c_instances = x.count('C')
    e_instances = x.count('E')
    q_instances = x.count('Q')
    g_instances = x.count('G')
    h_instances = x.count('H')
    o_instances = x.count('O')
    i_instances = x.count('I')
    l_instances = x.count('L')
    k_instances = x.count('K')
    m_instances = x.count('M')
    f_instances = x.count('F')
    p_instances = x.count('P')
    s_instances = x.count('S')
    t_instances = x.count('T')
    w_instances = x.count('W')
    y_instances = x.count('Y')
    v_instances = x.count('V')
    

        
print(mass_total)