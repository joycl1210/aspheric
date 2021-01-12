# Aspheric

This code helps understanding the raytracing of the plano-convex aspheric lenses, the motivation of the use of the paraxial approximation and how to choose the right conic constant for the design.

## User parameters

The user specifies in the code various parameters for the lens and the simulation.

- `kappa`: conic constant 
- `d`: diameter of the plano convex lens [mm]
- `R`: radius of curvature of the lens [mm]. For a convex lens, the radius of curvature must be a negative value.
- `n`: refractive index of the lens
- `L`: propagation length behind the lens [mm]
- `n_ray`: number of rays incident on the surface
- `n_pt`: number of points that constitute the aspheric surface
- `w`: beam diameter [mm]



## Outputs graphs

### Raytracing

The first figure shows the sag of the plano-convex lens (blue line on the left) and the specified number of rays equally repartited on the surface according to the beam diameter. The rays propagate for the distance specified by the user. Note that the vertex of the lens is coincident with the axial distance equal to zero. 

<img src="/Users/mireillequemener/Documents/GitHub/aspheric/images/raytracing.png" alt="raytracing" style="zoom:50%;" />



### Ray fan plot

The second figure displays the ray fan plot: the distance to the axis at the focal spot in respect to the height of the incident ray. This plots gives rapid information about the amount of spherical aberration produced by the lens. 

<img src="/Users/mireillequemener/Documents/GitHub/aspheric/images/rayfanplot.png" alt="rayfanplot" style="zoom:50%;" />

## Examples

### Paraxial approximation

