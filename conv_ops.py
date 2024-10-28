# conv_ops.py
#
# Usage: python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p
# This program determines the output shape and operation count of a convolution layer

# Input Parameters:
# c_in: count for input channel 
# h_in: count for input height
# w_in: count for input width
# n_filt: amount of filters in convolution layer
# h_filt: count for filter height 
# w_filt: count for filter width 
# s: stride of convolution filters
# p: amount of padding on every map side

# Output Variables:
# c_out:  count for output channel 
# h_out:  count for output height
# w_out:  count for output width 
# adds:   # of additions 
# muls:   # of multiplications 
# divs:   # of divisions 
#
# Written by Vineet Keshavamurthy

# import Python modules
import math # math module
import sys # argv

# constants
R_E_KM = 6378.137
E_E    = 0.081819221456

# initialize input variables
c_in = float('nan') 
h_in = float('nan') 
w_in = float('nan') 
n_filt = float('nan')
h_filt = float('nan')
w_filt = float('nan')
s = float('nan')
p = float('nan')

# check for the correct number of arguments
if len(sys.argv) == 9:
  c_in = int(sys.argv[1])
  h_in = int(sys.argv[2])
  w_in = int(sys.argv[3])
  n_filt = int(sys.argv[4])
  h_filt = int(sys.argv[5])
  w_filt = float(sys.argv[6])
  s = float(sys.argv[7])
  p = float(sys.argv[8])
else:
  print(\
    'Usage: '\
    'Incorrect amount of arguments passed for conv_ops.py'\
  )
  exit()

# Code written here
h_out_term = h_in+p*2-h_filt #calculation of inside term for h_out
h_out = 1+(h_out_term/s) #h_out equation
w_out_term = w_in+p*2-w_filt #calculation of inside term for w_out
w_out = 1+(w_out_term)/s #w_out equation
muls=n_filt*h_out*w_out*c_in*h_filt*w_filt # of multiplication calculation
adds=n_filt*h_out*w_out*c_in*h_filt*w_filt # of additions calculation

divs = 0

c_out = n_filt 

#print statements for code
# count for output channel
print(int(c_out)) 
# count for output height
print(int(h_out)) 
# count for output width 
print(int(w_out)) 
# of additions performed
print(int(adds)) 
# of multiplications
print(int(muls))  
# of divisions performed
print(int(divs)) 