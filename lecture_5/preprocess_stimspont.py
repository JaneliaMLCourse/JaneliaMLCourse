
def bin2d(x,tbin,dim):
    nb = int(np.floor(float(x.shape[dim])/float(tbin)))
    print(nb)
    if x.ndim==1:
        x = x[:,np.newaxis]
    if dim==0:
        x  = np.reshape(x[:nb*tbin,:],(nb,tbin,x.shape[1])).sum(axis=1)
        x2 = x.sum(axis=1)
    else:
        x  = np.reshape(x[:,:nb*tbin],(x.shape[0],nb,tbin))
        x2 = x.sum(axis=2)
    return x2
    
import scipy.io
from scipy.sparse.linalg import eigsh
import numpy as np
dat = scipy.io.loadmat('D:/grive/10krecordings/spont_paper/stimspont_M150824_MP019_2016-03-23.mat', squeeze_me=True)

resp = dat['stim']['resp'].item()
istim = dat['stim']['istim'].item().flatten()
resp = resp[istim<33,:]
istim = istim[istim<33]
istim = istim-1

# normalize stim responses and spont by spont mean and std
S = resp
spont = dat['Fsp'][:,np.squeeze(dat['stimtpt'])==0]
tbin = 3
spont = bin2d(spont, tbin, 1)
S -= spont.mean(axis=1)[:,np.newaxis].T
S /= spont.std(axis=1)[:,np.newaxis].T
spont -= spont.mean(axis=1)[:,np.newaxis]
spont /= spont.std(axis=1)[:,np.newaxis]

# bin before taking svd
sv,u = eigsh(spont @ spont.T, k=32)

S = S - S.mean(axis=0)[np.newaxis,:]

# find 1D projection that's shared btw/ stim and spont
C = S @ u[:,:32] # project top spont PCs
sv,ua = eigsh(C @ C.T, k=1) # find top PC
ushared = S.T @ ua

dat = {'resp': S, 'istim': istim, 'spont': spont}
np.save('data/stimspont.npy', dat)