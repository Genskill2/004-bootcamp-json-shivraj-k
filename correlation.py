import json
from math import sqrt

def load_journal(jsonfile):
    with open(jsonfile) as j:
        data = json.load(j)
        return data

def compute_phi(jsonfile, event):
    phi = 0
    n11, n00, n10, n01 = 0,0,0,0
    n1_, n0_, n_1, n_0 = 0,0,0,0
    with open(jsonfile) as j:
        data = json.load(j)
        for d in data:
            if event in d['events']:
                n1_ += 1
                if d['squirrel']:
                    n_1 += 1
                    n11 += 1
                else:
                    n_0 += 1
                    n10 += 1
            else:
                n0_ += 1
                if d['squirrel']:
                    n_1 += 1
                    n01 += 1
                else:
                    n_0 += 1
                    n00 += 1        
    phi = (n11 * n00 - n10 * n01)/sqrt(n1_ * n0_ * n_1 * n_0)
    return phi
    

def compute_correlations(jsonfile):
    data = load_journal(jsonfile)
    corr_dict = {}
    for d in data:
        for event in d['events']:
            if event not in corr_dict.keys():
                corr_dict[event] = compute_phi(jsonfile, event)
    return corr_dict

def diagnose(jsonfile):
    corr_dict = compute_correlations(jsonfile)
    max_corr_event = max(corr_dict, key = corr_dict.get)
    min_corr_event = min(corr_dict, key = corr_dict.get)
    return max_corr_event,min_corr_event
    
