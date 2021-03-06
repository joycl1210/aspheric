# Aspheric aberration and raytracing

This script helps understanding the raytracing of the plano-convex aspheric lenses, the motivation of the use of the paraxial approximation and how to choose the right conic constant for the lens design.

Note that this code is limited to incident collimated beam while supposing that the aperture stop is placed at the plano-convex lens position. 

## User parameters

The user specifies in the code various parameters for the lens and the simulation.

- `kappa`: conic constant $\kappa$ ;
- `d`: diameter of the plano convex lens [mm] ;
- `R`: radius of curvature of the lens [mm]. For a convex lens, the radius of curvature must be a negative value.
- `n`: refractive index of the lens ;
- `L`: propagation length behind the lens [mm] ;
- `n_ray`: number of rays incident on the surface ;
- `n_pt`: number of points that constitute the aspheric surface ;
- `w`: incident beam diameter [mm].



## Outputs graphs

### Raytracing

The first figure shows the sag of the plano-convex lens (blue line on the left) and the specified number of rays equally repartited on the surface according to the beam diameter. The rays propagate for the distance specified by the user. Note that the vertex of the lens is coincident with the axial distance equal to zero. One can rapidly and qualitatively observe the amount of spherical aberration by the spread of the focal spot.

<img src="images/raytracing_spheric.png" alt="raytracing_spheric" width="50%" />



### Transverse spherical aberration

The second figure displays the ray intercept plot: the vertical distance to the axis at the focal spot in respect to the height of the incident ray. Each ray constitutes a point in the figure. This plots gives rapid information about the amount of spherical aberration produced by the lens. A perfect aberration-free lens would produce a ray intercept plot which is a straight horizontal line. 

<img src="images/rayfanplot.png" alt="rayfanplot" width="50%" />

### Longitudinal spherical aberration plot

The third graph gives an idea about the longitudinal spread of the focus point. The position (0,0) on the graph represents the paraxial focus. For an abberated lens, only the ray which pass right in the middle of the lens without being deviated goes to the real (or paraxial) focal point. For higher incident rays in respect to the optical axis, the amount of aberration is larger, thus the distance to the real focal point is longer.

### <img src="images/longitudinal_aberration.png" alt="longitudinal_aberration" width="50%" /> 

## Theory behind the code

Aspheric lenses are used to compensate spherical aberrations (spread of the focal point on the axis). By optimizing the shape of the lens, one can control the deflection of the rays in order to make them converge on a single point. 

Let's define $z$ being the axial distance from the origin and $y$ the height. An aspheric surface has a profile given by:
$$
z = \frac{y^2}{R\left(1+\sqrt{1-(1+\kappa)\frac{y^2}{R}}\right)},
$$
Where $R$ is the radius of curvature of the lens and $\kappa$ is the conic constant of the surface. The choice of $R$ is directly linked to the focal length $f$ of the lens in the following way:
$$
f = \frac{-1}{\frac{1}{R}(n-1)},
$$
where $n$ is the refractive index of the material of the lens. Note that we assume that the lens is surrounded by air of refractive index of 1. 



## Examples

### Understanding the type of spherical aberration

The type of spherical aberration can be found with the sign of the longitudinal aberration equation. When the spherical aberration has a negative sign, we say it is undercorrected. On the raytrace, one can see that as the ray height increases, the position of the ray intersection with the optical axis moves closer to the vertex of the lens. Similarly, positive spherical is called overcorrected and is generally associated with diverging elements. 

Let's run the code for a BK7 lens ($n=1.5168$) with an illumination diameter close to the aperture of the lens. We will compare two lenses, one with a spherical shape ($\kappa=0$), and one with an hyperbolic shape with $\kappa=-5$. 

<img src="images/aberration_type.png" alt="aberration_type" width="70%" />

The figure above shows the typical ray intercept plots for both overcorrected and undercorrected spherical aberrations. 

### Spherical lens and paraxial approximation

For a spherical lens, $\kappa=0$. In general, in optics, we assume that lenses have a spherical shape since we often use paraxial approximation. In this example, we will show that a spherical lens is free of sperical aberration only for rays in the paraxial region. 

As an input, let's define the parameters to have a sperical lens made of BK7 glass ($n=1.5168$) with a focal length of 100 mm:

```python
kappa = 0
d = 60
f = 100
n = 1.5168
L = 150
n_ray = 13
n_pt = 100
w = 50
```

Notice that we chose a lens diameter of 60 mm and a beam diameter that almost covers all its aperture (50 mm). On the raytracing figure, one can clearly see the presence of the spherical aberration.

<img src="images/raytracing_spheric.png" alt="raytracing_spheric" width="50%" />



When we rise the number of rays $n_{ray}$ to 500 to have a smoother rayfan plot, one can get the following graph:

<img src="images/rayfanplot_spheric.png" alt="rayfanplot_spheric" width="50%" /> 

The obtained value of $y'=10$ confirms that we have great amount of transverrse aberration. Let's run the code again, but with lower values of the beam diameter.

<img src="images/spheric_beam_diameter.png" width="100%"  />

Thus, we conclude that the use of a spherical lens is a good choice when the paraxial approximation is valid.

### Spherical abberation correction for a plano-convex lens

Is there a value of $\kappa$ that leads to an optimized correction of the spherical aberration? In the case of our plano-convex lens, the answer is yes. It can be found in the litterature that a conic constant of $\kappa = -n^2$ minimizes the spherical aberration. Let's confirm this with our code.

In the script, we choose a BK7 lens ($n=1.5168$) with a beam diameter that is close to the aperture of the lens. We define `k=-1.5168**2` . Below are the obtained figures:

### Axicon

In this example, we will show that the refractive axicon is simply an aspheric lens with an hyperbolic shape and a radius of curvature that tends to zero (in orde to get a sharp cone tip). 

In the script, 
