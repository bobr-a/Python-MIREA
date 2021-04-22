#!/usr/bin/env python
# coding: utf-8

# In[4]:


import struct


# In[109]:


def f31(data):
    wgr = data[:5]
    
    E_struct = '<LHLHH'
    D_struct = '<ihfhI'
    C_struct = '<qQdfq'
    B_struct = 'Ib3HHIH'
    A_struct = '<hIH' + B_struct + '3d'
    
    A = data[5:(5 + struct.calcsize(A_struct))]
    
    result = {}
    
    A_res = struct.unpack(A_struct, A)
    result['A1'] = A_res[0]
    result['A2'] = A_res[1]
    result['A3'] = A_res[2]
    
    C_res = struct.unpack(C_struct, data[A_res[3]:(A_res[3] + struct.calcsize(C_struct))])
    
    D1_res = struct.unpack(D_struct, data[A_res[5]:(A_res[5] + struct.calcsize(D_struct))])
    D2_res = struct.unpack(D_struct, data[A_res[6]:(A_res[6] + struct.calcsize(D_struct))])
    D3_res = struct.unpack(D_struct, data[A_res[7]:(A_res[7] + struct.calcsize(D_struct))])
    
    print(A_res[9])
    E_res = struct.unpack(E_struct, data[A_res[9]:(A_res[9] + 14)])
    print(E_res)
    
    result['A4'] = {
        'B1': {
            'C1': C_res[0],
            'C2': C_res[1],
            'C3': C_res[2],
            'C4': C_res[3],
            'C5': C_res[4]
        },
        'B2': A_res[4],
        'B3': [
            {
                'D1': D1_res[0],
                'D2': D1_res[1],
                'D3': D1_res[2],
                'D4': D1_res[3],
                'D5': D1_res[4]
            },
            {
                'D1': D2_res[0],
                'D2': D2_res[1],
                'D3': D2_res[2],
                'D4': D2_res[3],
                'D5': D2_res[4]
            },
            {
                'D1': D3_res[0],
                'D2': D3_res[1],
                'D3': D3_res[2],
                'D4': D3_res[3],
                'D5': D3_res[4]
            }
        ],
        'B4': A_res[8],
        'B5': {
            'E1': list(struct.unpack('<' + str(E_res[0]) + 'h', data[E_res[1]:(E_res[1] + struct.calcsize('<' + str(E_res[0]) + 'h'))])),
            'E2': list(struct.unpack('<' + str(E_res[2]) + 'h', data[E_res[3]:(E_res[3] + struct.calcsize('<' + str(E_res[2]) + 'h'))])),
            'E3': E_res[4]
        },
        'B6': A_res[10]
    }
    result['A5'] = [A_res[11], A_res[12], A_res[13]]
        
    return result

