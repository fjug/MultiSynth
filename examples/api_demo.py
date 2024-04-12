from sillytissue.cells.celltypes import CCType, LC1Type, LC2Type, LWCType, NCType, RLCType
from sillytissue.phantoms.CirclePhantomDistribution import CirclePhantomDistribution
from sillytissue.phantoms.CirclePhantom import CirclePhantom
from sillytissue.phantoms.CirclePhantomSample import CirclePhantomSample
from sillytissue.utils.PlotUtils import PlotUtils
import numpy as np
import random

seed = 1
random.seed(seed)
np.random.seed(seed)

circle_phantom_distribution = CirclePhantomDistribution(1, 2, 1, .3, .1)
circle_phantom = CirclePhantom(circle_phantom_distribution)

# PlotUtils.plotCirclePhantom(circle_phantom, z=0.5)

rlct = RLCType(num_mean=50, num_sigma=5, 
               r_mean=0.01, r_sigma=0.0005, color=(0,.2,1) )
cct  = CCType (attempts_to_add=10, dist_from_circle_sigma=0.02, 
               r_mean=0.02, r_sigma=0.001, color=(1,0,0) )
lc1t = LC1Type(attempts_to_add=7, norm_dist_from_center_sigma=0.3, 
               r_mean=0.03, r_sigma=0.003, color=(0,.5,0) )
lc2t = LC2Type(attempts_to_add=7, norm_dist_from_center_mu=0.7, norm_sigma=0.25, 
               r_mean=0.01, r_sigma=0.001, color=(0,1,0) )
nct  = NCType (attempts_to_add=10, norm_dist_from_center_mu=1.05, norm_sigma=0.05, 
               r_mean=0.015, r_sigma=0.00075, color=(1,0.65,0) )
lwct = LWCType(attempts_to_add=4, norm_min_dist_from_center=1.2, 
               r_mean=0.0175, r_sigma=0.005, color=(.93,.5,.93,.5) )
circle_phantom_sample = CirclePhantomSample(circle_phantom, rlct, cct, lc1t, lc2t, nct, lwct)

PlotUtils.plotCirclePhantomSample(circle_phantom_sample, z=0.5)
PlotUtils.plotCirclePhantomSample3d(circle_phantom_sample)