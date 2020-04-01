#coding=utf8
def param_handle(param):
    d={}
    for i in param.split(','):
        s=i.split('=')
        d[s[0]]=s[1]
    return d
def getkeys(dic):
    lis=[]
    for k,v in dic.items():
	    lis.append(k)
	    if isinstance(v,list):
		    for i in v:
			    for ks,vs in i.items():
				    lis.append(ks)
    return lis