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

<img src="/Users/mireillequemener/Documents/GitHub/aspheric/raytracing.png" alt="raytracing" style="zoom:33%;" />

### Ray fan plot



## Examples

### Paraxial approximation

