import numpy as np
import matplotlib.pyplot as plt
import math

kappa = 0
d = 60
f = 100
n = 1.5168
L = 150
n_ray = 200
n_pt = 13
w = 50

# Condition on illumination
if (d < w):
    exit('The beam diameter cannot be larger than the diameter of the lens')

rmax = d/2
R = -(n-1)*f

# Calculate the sag of the lens (z) and plot
# Height parameter of the surface
r_surf = np.arange(-rmax, rmax, rmax/n_pt)
z = []
for i in range(len(r_surf)):
    z.append(r_surf[i]**2/(R*(1+math.sqrt(1-(1+kappa)*r_surf[i]**2/R**2))))
plt.plot(z, r_surf)


# RAYTACING

# Incident rays tracing
# Height of the incident rays:
r_ray = np.arange(-w/2, w/2, w/n_ray)
# Calculation of the sag at ray height
z_ray = []
for i in range(len(r_ray)):
    z_ray.append(r_ray[i]**2/(R*(1+math.sqrt(1-(1+kappa)*r_ray[i]**2/R**2))))

for i in range(len(r_ray)):
    x = [min(z)-2, z_ray[i]]
    y = [r_ray[i], r_ray[i]]
    plt.plot(x, y, color='red')

# Calculate the angle of the ray to the normal of the lens
diff = []
for i in range(len(r_ray)):
    diff.append(r_ray[i]/(R*math.sqrt(1-((kappa+1)*r_ray[i]**2/R**2)))) 
diff = np.arctan(diff)


# Calculate the angle of deflection of the rays after the lens
theta_2 = []
for i in range(len(r_ray)):
    theta_2.append(np.arcsin(n*np.sin(diff[i])) - diff[i])

# Ray tracing of the deflected rays
rtrace = plt.figure(1)
for i in range(len(r_ray)):
    x2 = [z_ray[i], L]
    y2 = [r_ray[i], (L+abs(z_ray[i]))*np.tan(theta_2[i]) + r_ray[i]]
    plt.plot(x2, y2, color='red')
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('Axial distance [mm]')
plt.ylabel('Height [mm]')
plt.show()

# RAY INTERCEPT PLOT
# y_f is the height of each ray at the paraxial focus
y_f = []
for i in range(len(r_ray)):
    y_f.append((f + abs(z_ray[i]))*np.tan(theta_2[i]) + r_ray[i])
rfp = plt.figure(3)
axs = plt.gca()
axs.plot(r_ray, y_f)
axs.grid(True)
axs.spines['left'].set_position('zero')
axs.spines['right'].set_color('none')
axs.spines['bottom'].set_position('zero')
axs.spines['top'].set_color('none')
plt.xlabel('y')
plt.ylabel("y'")
plt.show()

# LONGITUDINAL ABERRATION PLOT
# f_L is the focal distance of each rays and LA is the longitudinal aberration
f_L = []
LA = []
for i in range(len(z_ray)):
    f_L.append(abs(r_ray[i]/math.tan(theta_2[i])) + z_ray[i])
    LA.append(f_L[i]-f)

print(LA)
plt.figure(4)
plt.plot(LA, r_ray)
plt.ylim(0, max(r_ray))
plt.xlabel('Longitudinal aberration [mm]')
plt.ylabel('Ray height [mm]')
axs.grid(True)
plt.show()