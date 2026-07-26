---
title: Fluid Simulation for Dummies
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/fluid-simulation-for-dummies.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:8453bfb1133efe18'
translated: false
---

> 原文：[Fluid Simulation for Dummies](https://www.mikeash.com/pyblog/fluid-simulation-for-dummies.html)　·　mikeash.com Friday Q&A

Posted at 2006-03-13 00:00 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Cocoa SIMBL Plugins](https://www.mikeash.com/pyblog/cocoa-simbl-plugins.html)  
Previous article: [NSOpenGLContext and one-shot](https://www.mikeash.com/pyblog/nsopenglcontext-and-one-shot.html)  
Tags: [fluid](https://www.mikeash.com/pyblog/?tag=fluid) [simulation](https://www.mikeash.com/pyblog/?tag=simulation)

Fluid Simulation for Dummies

by [Mike Ash](https://www.mikeash.com/)

[Real-Time Fluid Dynamics for Games](http://www.dgp.toronto.edu/people/stam/reality/Research/pdf/GDC03.pdf). If you want a more in-depth look at what's going on, that's the place to go. You can also read all about how to parallelize the simulation and render the output in 3D in my [Master's thesis](http://www.mikeash.com/?page=thesis/).

### Basics

Fluid simulation is based on the Navier-Stokes equations, which are fundamental, interesting, and difficult to understand without a good background in physics and differential equations. To that end, I'm going to pretty much ignore them except to very briefly explain what they say.

Think of a fluid as a collection of boxes or cells. Each box has various properties, like velocity and density. These boxes interact with their neighbors, affecting their velocity and density. A real-world fluid can be seen as having a huge number of absolutely miniscule boxes, all interacting with their neighbors a zillion times a second.

Of course, a real computer can't handle a zillion interactions per second, nor can it handle a zillion little boxes, so we have to compromise. We'll break the fluid up into a reasonable number of boxes and try to do several interactions per second.

To make things simpler, we're only going to examine incompressible fluid. Air is an example of a compressible fluid; you squish it and it gets smaller. Water is an example of an incompressible fluid; you squish it and it pushes back, and doesn't get any smaller. Incompressible fluids are simpler to simulate because their density and pressure is always constant.

Of course, moving water is really boring if there's nothing in it, because you can't see it moving! So we'll add some dye so we can actually see it moving around. The water is equally dense everywhere, but some of it has more dye than others, and this variation lets us see things moving. So remember, whenever I'm talking about "density", I'm actually talking about the density of the _dye_, not the density of the _fluid_. (This took me about six months to figure out, that's why I'm so insistent.)

### Data Structures

These boxes will be represented as several 3D arrays. Of course, since C hates multidimensional arrays, we'll use 1D arrays and fake the extra two dimensions. To that end, we have our very first code: a #define which takes three coordinates, and dumps out the corresponding array index in a one-dimensional array:

```
#define IX(x, y, z) ((x) + (y) * N + (z) * N * N)
```

Next, let's actually look at how we represent a cube of fluid. We're going to need its size (this code only handles perfect cubes which have the same length on each size), the length of the timestep, the amount of diffusion (how fast stuff spreads out in the fluid), and the viscosity (how thick the fluid is). We also need a density array and three velocity arrays, one for x, y, and z. We also need scratch space for each array so that we can keep old values around while we compute the new ones.

Putting all of this together, we get our fluid cube structure.

```
struct FluidCube {
    int size;
    float dt;
    float diff;
    float visc;
    
    float *s;
    float *density;
    
    float *Vx;
    float *Vy;
    float *Vz;

    float *Vx0;
    float *Vy0;
    float *Vz0;
};
typedef struct FluidCube FluidCube;
```

To make sure everything gets set up properly, we need a function that will fill out this whole structure for us:

```
FluidCube *FluidCubeCreate(int size, int diffusion, int viscosity, float dt)
{
    FluidCube *cube = malloc(sizeof(*cube));
    int N = size;
    
    cube->size = size;
    cube->dt = dt;
    cube->diff = diffusion;
    cube->visc = viscosity;
    
    cube->s = calloc(N * N * N, sizeof(float));
    cube->density = calloc(N * N * N, sizeof(float));
    
    cube->Vx = calloc(N * N * N, sizeof(float));
    cube->Vy = calloc(N * N * N, sizeof(float));
    cube->Vz = calloc(N * N * N, sizeof(float));
    
    cube->Vx0 = calloc(N * N * N, sizeof(float));
    cube->Vy0 = calloc(N * N * N, sizeof(float));
    cube->Vz0 = calloc(N * N * N, sizeof(float));
    
    return cube;
}
```

And finally we need to be able to destroy this thing once we're done with it:

```
void FluidCubeFree(FluidCube *cube)
{
    free(cube->s);
    free(cube->density);
    
    free(cube->Vx);
    free(cube->Vy);
    free(cube->Vz);
    
    free(cube->Vx0);
    free(cube->Vy0);
    free(cube->Vz0);
    
    free(cube);
}
```

Since this just initializes a motionless cube with no dye, we need a way both to add some dye:

```
void FluidCubeAddDensity(FluidCube *cube, int x, int y, int z, float amount)
{
    int N = cube->size;
    cube->density[IX(x, y, z)] += amount;
}
```

And to add some velocity:

```
void FluidCubeAddVelocity(FluidCube *cube, int x, int y, int z, float amountX, float amountY, float amountZ)
{
    int N = cube->size;
    int index = IX(x, y, z);
    
    cube->Vx[index] += amountX;
    cube->Vy[index] += amountY;
    cube->Vz[index] += amountZ;
}
```

### Simulation Outline

There are three main operations that we'll use to perform a simulation step.

**diffuse** - Put a drop of soy sauce in some water, and you'll notice that it doesn't stay still, but it spreads out. This happens even if the water and sauce are both perfectly still. This is called diffusion. We use diffusion both in the obvious case of making the dye spread out, and also in the less obvious case of making the velocities of the fluid spread out.

**project** - Remember when I said that we're only simulating incompressible fluids? This means that the amount of fluid in each box has to stay constant. That means that the amount of fluid going in has to be exactly equal to the amount of fluid going out. The other operations tend to screw things up so that you get some boxes with a net outflow, and some with a net inflow. This operation runs through all the cells and fixes them up so everything is in equilibrium.

**advect** - Every cell has a set of velocities, and these velocities make things move. This is called advection. As with diffusion, advection applies both to the dye and to the velocities themselves.

There are also two subroutines that are used by these operations.

**set_bnd** - This is short for "set bounds", and it's a way to keep fluid from leaking out of your box. Not that it could really leak, since it's just a simulation in memory, but not having walls really screws up the simulation code. Walls are added by treating the outer layer of cells as the wall. Basically, every velocity in the layer next to this outer layer is mirrored. So when you have some velocity towards the wall in the next-to-outer layer, the wall gets a velocity that perfectly counters it.

**lin_solve** - I honestly don't know exactly what this function does or how it works. What I do know is that it's used for both **diffuse** and **project**. It's solving a linear differential equation of some sort, although how and what is not entirely clear to me.

OK, now we're ready to see the main simulation function:

```
void FluidCubeStep(FluidCube *cube)
{
    int N          = cube->size;
    float visc     = cube->visc;
    float diff     = cube->diff;
    float dt       = cube->dt;
    float *Vx      = cube->Vx;
    float *Vy      = cube->Vy;
    float *Vz      = cube->Vz;
    float *Vx0     = cube->Vx0;
    float *Vy0     = cube->Vy0;
    float *Vz0     = cube->Vz0;
    float *s       = cube->s;
    float *density = cube->density;
    
    diffuse(1, Vx0, Vx, visc, dt, 4, N);
    diffuse(2, Vy0, Vy, visc, dt, 4, N);
    diffuse(3, Vz0, Vz, visc, dt, 4, N);
    
    project(Vx0, Vy0, Vz0, Vx, Vy, 4, N);
    
    advect(1, Vx, Vx0, Vx0, Vy0, Vz0, dt, N);
    advect(2, Vy, Vy0, Vx0, Vy0, Vz0, dt, N);
    advect(3, Vz, Vz0, Vx0, Vy0, Vz0, dt, N);
    
    project(Vx, Vy, Vz, Vx0, Vy0, 4, N);
    
    diffuse(0, s, density, diff, dt, 4, N);
    advect(0, density, s, Vx, Vy, Vz, dt, N);
}
```

To summarize, this does the following steps:

- Diffuse all three velocity components.
- Fix up velocities so they keep things incompressible
- Move the velocities around according to the velocities of the fluid (confused yet?).
- Fix up the velocities _again_
- Diffuse the dye.
- Move the dye around according to the velocities.

So that's the basics of it. Now we'll get into the implementation of each function.

### set_bnd

As noted above, this function sets the boundary cells at the outer edges of the cube so they perfectly counteract their neighbors.

There's a bit of oddness here which is, what is this b pramaeter? It can be 0, 1, 2, or 3, and each value has a special meaning which is not at all obvious. The answer lies is what kind of data can be passed into this function.

We have four different kinds of data (x, y, and z velocities, plus density) floating around, and any of those four can be passed in to set_bnd. You may notice that this is exactly the number of values this parameter can have, and this is not a coincidence.

Let's look at a boundary cell (horrible ASCII art warning):

```
+---+---+
|   |^  |
|   |  |
|   |  |
+---+---+
```

Here we're at the left edge of the cube. The left cell is the boundary cell that needs to counteract its neighbor, the right cell. The right cell has a velocity that's up and to the left.

The boundary cell's **x** velocity needs to be _opposite_ its neighbor, but its **y** velocity needs to be _equal_ to its neighbor. This will produce a result like so:

```
+---+---+
|  ^|^  |
| / |  |
|/  |  |
+---+---+
```

This counteracts the motion of the fluid which would take it through the wall, and preserves the rest of the motion. So you can see that what action is taken depends on which array we're dealing with; if we're dealing with x velocities, then we have to set the boundary cell's value to the opposite of its neighbor, but for everything else we set it to be the same.

That is the answer to the mysterious b. It tells the function which array it's dealing with, and so whether each boundary cell should be set equal or opposite its neighbor's value.

This function also sets corners. This is done very simply, by setting each corner cell equal to the average of its three neighbors.

Without further ado, the code:

```
static void set_bnd(int b, float *x, int N)
{
    for(int j = 1; j < N - 1; j++) {
        for(int i = 1; i < N - 1; i++) {
            x[IX(i, j, 0  )] = b == 3 ? -x[IX(i, j, 1  )] : x[IX(i, j, 1  )];
            x[IX(i, j, N-1)] = b == 3 ? -x[IX(i, j, N-2)] : x[IX(i, j, N-2)];
        }
    }
    for(int k = 1; k < N - 1; k++) {
        for(int i = 1; i < N - 1; i++) {
            x[IX(i, 0  , k)] = b == 2 ? -x[IX(i, 1  , k)] : x[IX(i, 1  , k)];
            x[IX(i, N-1, k)] = b == 2 ? -x[IX(i, N-2, k)] : x[IX(i, N-2, k)];
        }
    }
    for(int k = 1; k < N - 1; k++) {
        for(int j = 1; j < N - 1; j++) {
            x[IX(0  , j, k)] = b == 1 ? -x[IX(1  , j, k)] : x[IX(1  , j, k)];
            x[IX(N-1, j, k)] = b == 1 ? -x[IX(N-2, j, k)] : x[IX(N-2, j, k)];
        }
    }
    
    x[IX(0, 0, 0)]       = 0.33f * (x[IX(1, 0, 0)]
                                  + x[IX(0, 1, 0)]
                                  + x[IX(0, 0, 1)]);
    x[IX(0, N-1, 0)]     = 0.33f * (x[IX(1, N-1, 0)]
                                  + x[IX(0, N-2, 0)]
                                  + x[IX(0, N-1, 1)]);
    x[IX(0, 0, N-1)]     = 0.33f * (x[IX(1, 0, N-1)]
                                  + x[IX(0, 1, N-1)]
                                  + x[IX(0, 0, N)]);
    x[IX(0, N-1, N-1)]   = 0.33f * (x[IX(1, N-1, N-1)]
                                  + x[IX(0, N-2, N-1)]
                                  + x[IX(0, N-1, N-2)]);
    x[IX(N-1, 0, 0)]     = 0.33f * (x[IX(N-2, 0, 0)]
                                  + x[IX(N-1, 1, 0)]
                                  + x[IX(N-1, 0, 1)]);
    x[IX(N-1, N-1, 0)]   = 0.33f * (x[IX(N-2, N-1, 0)]
                                  + x[IX(N-1, N-2, 0)]
                                  + x[IX(N-1, N-1, 1)]);
    x[IX(N-1, 0, N-1)]   = 0.33f * (x[IX(N-2, 0, N-1)]
                                  + x[IX(N-1, 1, N-1)]
                                  + x[IX(N-1, 0, N-2)]);
    x[IX(N-1, N-1, N-1)] = 0.33f * (x[IX(N-2, N-1, N-1)]
                                  + x[IX(N-1, N-2, N-1)]
                                  + x[IX(N-1, N-1, N-2)]);
}
```

### lin_solve

As stated before, this function is mysterious, but it does some kind of solving. this is done by running through the whole array and setting each cell to a combination of its neighbors. It does this several times; the more iterations it does, the more accurate the results, but the slower things run. In the step function above, four iterations are used. After each iteration, it resets the boundaries so the calculations don't explode.

Here's the code:

```
static void lin_solve(int b, float *x, float *x0, float a, float c, int iter, int N)
{
    float cRecip = 1.0 / c;
    for (int k = 0; k < iter; k++) {
        for (int m = 1; m < N - 1; m++) {
            for (int j = 1; j < N - 1; j++) {
                for (int i = 1; i < N - 1; i++) {
                    x[IX(i, j, m)] =
                        (x0[IX(i, j, m)]
                            + a*(    x[IX(i+1, j  , m  )]
                                    +x[IX(i-1, j  , m  )]
                                    +x[IX(i  , j+1, m  )]
                                    +x[IX(i  , j-1, m  )]
                                    +x[IX(i  , j  , m+1)]
                                    +x[IX(i  , j  , m-1)]
                           )) * cRecip;
                }
            }
        }
        set_bnd(b, x, N);
    }
}
```

### diffuse

Diffuse is really simple; it just precalculates a value and passes everything off to lin_solve. So that means, while I know what it does, I don't really know how, since all the work is in that mysterious function. Code:

```
static void diffuse (int b, float *x, float *x0, float diff, float dt, int iter, int N)
{
    float a = dt * diff * (N - 2) * (N - 2);
    lin_solve(b, x, x0, a, 1 + 6 * a, iter, N);
}
```

### project

This function is also somewhat mysterious as to exactly how it works, but it does some more running through the data and setting values, with some calls to lin_solve thrown in for fun. Code:

```
static void project(float *velocX, float *velocY, float *velocZ, float *p, float *div, int iter, int N)
{
    for (int k = 1; k < N - 1; k++) {
        for (int j = 1; j < N - 1; j++) {
            for (int i = 1; i < N - 1; i++) {
                div[IX(i, j, k)] = -0.5f*(
                         velocX[IX(i+1, j  , k  )]
                        -velocX[IX(i-1, j  , k  )]
                        +velocY[IX(i  , j+1, k  )]
                        -velocY[IX(i  , j-1, k  )]
                        +velocZ[IX(i  , j  , k+1)]
                        -velocZ[IX(i  , j  , k-1)]
                    )/N;
                p[IX(i, j, k)] = 0;
            }
        }
    }
    set_bnd(0, div, N); 
    set_bnd(0, p, N);
    lin_solve(0, p, div, 1, 6, iter, N);
    
    for (int k = 1; k < N - 1; k++) {
        for (int j = 1; j < N - 1; j++) {
            for (int i = 1; i < N - 1; i++) {
                velocX[IX(i, j, k)] -= 0.5f * (  p[IX(i+1, j, k)]
                                                -p[IX(i-1, j, k)]) * N;
                velocY[IX(i, j, k)] -= 0.5f * (  p[IX(i, j+1, k)]
                                                -p[IX(i, j-1, k)]) * N;
                velocZ[IX(i, j, k)] -= 0.5f * (  p[IX(i, j, k+1)]
                                                -p[IX(i, j, k-1)]) * N;
            }
        }
    }
    set_bnd(1, velocX, N);
    set_bnd(2, velocY, N);
    set_bnd(3, velocZ, N);
}
```

### advect

This function is responsible for actually moving things around. To that end, it looks at each cell in turn. In that cell, it grabs the velocity, follows that velocity back in time, and sees where it lands. It then takes a weighted average of the cells around the spot where it lands, then applies that value to the current cell.

Here's the code:

```
static void advect(int b, float *d, float *d0,  float *velocX, float *velocY, float *velocZ, float dt, int N)
{
    float i0, i1, j0, j1, k0, k1;
    
    float dtx = dt * (N - 2);
    float dty = dt * (N - 2);
    float dtz = dt * (N - 2);
    
    float s0, s1, t0, t1, u0, u1;
    float tmp1, tmp2, tmp3, x, y, z;
    
    float Nfloat = N;
    float ifloat, jfloat, kfloat;
    int i, j, k;
    
    for(k = 1, kfloat = 1; k < N - 1; k++, kfloat++) {
        for(j = 1, jfloat = 1; j < N - 1; j++, jfloat++) { 
            for(i = 1, ifloat = 1; i < N - 1; i++, ifloat++) {
                tmp1 = dtx * velocX[IX(i, j, k)];
                tmp2 = dty * velocY[IX(i, j, k)];
                tmp3 = dtz * velocZ[IX(i, j, k)];
                x    = ifloat - tmp1; 
                y    = jfloat - tmp2;
                z    = kfloat - tmp3;
                
                if(x < 0.5f) x = 0.5f; 
                if(x > Nfloat + 0.5f) x = Nfloat + 0.5f; 
                i0 = floorf(x); 
                i1 = i0 + 1.0f;
                if(y < 0.5f) y = 0.5f; 
                if(y > Nfloat + 0.5f) y = Nfloat + 0.5f; 
                j0 = floorf(y);
                j1 = j0 + 1.0f; 
                if(z < 0.5f) z = 0.5f;
                if(z > Nfloat + 0.5f) z = Nfloat + 0.5f;
                k0 = floorf(z);
                k1 = k0 + 1.0f;
                
                s1 = x - i0; 
                s0 = 1.0f - s1; 
                t1 = y - j0; 
                t0 = 1.0f - t1;
                u1 = z - k0;
                u0 = 1.0f - u1;
                
                int i0i = i0;
                int i1i = i1;
                int j0i = j0;
                int j1i = j1;
                int k0i = k0;
                int k1i = k1;
                
                d[IX(i, j, k)] = 
                
                    s0 * ( t0 * (u0 * d0[IX(i0i, j0i, k0i)]
                                +u1 * d0[IX(i0i, j0i, k1i)])
                        +( t1 * (u0 * d0[IX(i0i, j1i, k0i)]
                                +u1 * d0[IX(i0i, j1i, k1i)])))
                   +s1 * ( t0 * (u0 * d0[IX(i1i, j0i, k0i)]
                                +u1 * d0[IX(i1i, j0i, k1i)])
                        +( t1 * (u0 * d0[IX(i1i, j1i, k0i)]
                                +u1 * d0[IX(i1i, j1i, k1i)])));
            }
        }
    }
    set_bnd(b, d, N);
}
```

### Wrapping Up

And there you have it, everything you need to make your own 3D fluid simulation.

[View the full source](https://www.mikeash.com/pyblog/blog/images/fluid.c.file)

Note that actually _displaying_ this animation is a bit more difficult. This was actually the primary topic of my thesis, as the fluid simulation was pretty much just borrowed from Stam and pulled into 3D. This kind of three-dimensional grid data is not something that most graphics hardware and APIs know how to render, and so it's a fairly challenging topic.

If you want to show the results of the simulation, you have several choices. One would be to rewrite the simulator in two dimensions instead of three, and you can then just display the density pointer onscreen as a regular image. Another choice would be to run the full 3D simulation but only display 2D slice of it. And finally, another choice would be to run a simulation small enough that you can just draw one polygon per cell without taking too much of a speed hit.

Of course, if you like a challenge, feel free to check out the various techniques for volumetric rendering.

I hope you enjoyed this whirlwind tour through fluid simulation. Have fun!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/fluid-simulation-for-dummies.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
