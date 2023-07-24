'''
(C) Copyright Siemens AG 2023

SPDX-License-Identifier: MIT
'''
from __future__ import division
import numpy as np

from industrial_benchmark_python.IDS import IDS

class IDS(IDS):
    '''
    Lightweight python implementation of the industrial benchmark'''

    def __init__(self,p=50,stationary_p=True, inital_seed=None):
        '''
        p sets the setpoint hyperparameter (between 1-100) which will
        affect the dynamics and stochasticity.

        stationary_p = False will make the setpoint vary over time. This
        will make the system more non-stationary.
        '''

        super().__init__(p, stationary_p, inital_seed)

        # observables
        self.observable_keys = ['v','g','f','c','reward']

    def step(self,delta):
        delta = np.concatenate([delta, [0.0]])
        super().step(delta)
    
    def updateOperationalCosts(self):
        eNewHidden = self.state['coc']
        operationalcosts = eNewHidden - np.random.randn()*(1+0.005*eNewHidden)
        self.state['c'] = operationalcosts