from scipy.special import expit      #to encounter the problem of exp Overflow
import numpy as np
def sigmoidReg(z):
  '''Returns sigmoid of z
  np.exp(A)==> returns element each element X in the form e^X'''
  sgm= 1/(1+np.exp(-z))
  return expit(sgm)
  
