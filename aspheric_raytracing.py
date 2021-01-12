import numpy as np
import matplotlib.pyplot as plt
import math

# Define user parameters
# kappa: conic constant
# d: diameter of the plano convex lens
# R: radius of curvature of the lens
# n: refractive index of the lens
# L: propagation length behind the lens
# n_ray: number of rays incident on the surface
# m: number of points that constitute the aspheric surface
kappa = 0
d = 60
R = -50.23
n = 1.5168
L = 150
n_ray = 11
n_pt = 100
w = 50

if (d < w):
    exit('The beam diameter cannot be larger than the diameter of the lens')

rmax = d/2
f = -1/((1/R)*(n-1))
print("The focal length is:", f, "mm")

# Calculate the surface of the lens and plot

r_surf = np.arange(-rmax, rmax, rmax/n_pt)
z = []
for i in range(len(r_surf)):
    z.append(r_surf[i]**2/(R*(1+math.sqrt(1-(1+kappa)*r_surf[i]**2/R**2))))
plt.plot(z, r_surf)


# Raytracing

# Incident rays tracing
r_ray = np.arange(-w/2, w/2, w/n_ray)
z_ray = []
for i in range(len(r_ray)):
    z_ray.append(r_ray[i]**2/(R*(1+math.sqrt(1-(1+kappa)*r_ray[i]**2/R**2))))

for i in range(len(r_ray)):
    x = [min(z)-2, z_ray[i]]
    y = [r_ray[i], r_ray[i]]
    plt.plot(x, y, color='red')

# Calculate the angle of the ray to the normal
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
    x2 = [z_ray[i], z_ray[i]+L]
    y2 = [r_ray[i], L*np.tan(theta_2[i]) + r_ray[i]]
    plt.plot(x2, y2, color='red')
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('Axial distance [mm]')
plt.ylabel('Height [mm]')
plt.show()

# Zoom plot on the focal spot
# zrtrace = plt.figure(2)
# for i in range(len(r_ray)):
    # x2 = [z_ray[i], z_ray[i]+L]
    # y2 = [r_ray[i], L*np.tan(theta_2[i]) + r_ray[i]]
    # plt.plot(x2, y2, color='red')
# plt.xlim(f-0.1*f, f+0.1*f)
# plt.ylim(-0.2, 0.2)
# plt.show()

# Ray fan plot
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
