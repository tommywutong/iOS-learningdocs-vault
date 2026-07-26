---
title: Exploring GPGPU on iOS – Bartosz Ciechanowski
source: Bartosz Ciechanowski
source_key: ciechanowski
source_url: 'https://ciechanow.ski/exploring-gpgpu-on-ios/'
original_language: en
published: ''
status: active
license: Copyright © Bartosz Ciechanowski（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:9f6625113183869e'
translated: false
---

> 原文：[Exploring GPGPU on iOS – Bartosz Ciechanowski](https://ciechanow.ski/exploring-gpgpu-on-ios/)　·　Bartosz Ciechanowski

# [Exploring GPGPU on iOS](https://ciechanow.ski/exploring-gpgpu-on-ios/)

**Note:** this article is obsolete as there are [better ways](https://developer.apple.com/documentation/metal/basic_tasks_and_concepts/performing_calculations_on_a_gpu) of doing GPU computation on modern iOS devices. I’m keeping it here as a historical reference.

---

I’ve always wanted to try some [GPGPU](http://en.wikipedia.org/wiki/GPGPU) programming on iOS. The idea of harnessing the highly parallelized power just tickled my inner geek. Using GPU to run image processing is already [a solved problem](https://github.com/BradLarson/GPUImage). Unfortunately, fragment shader calculations do not support the notion of more general computation. With advent of A7 chip and OpenGL ES 3.0, I’ve decided to tackle this problem and I’ve managed to get some exceptionally good results. Granted, the method I rolled in has some limitations and performs well only in fairly computationally heavy situations, but when it works, it works like _magic_.

As a companion to this article, I created a [GitHub repo](https://github.com/Ciechan/Exploring-GPGPU-on-iOS) that contains the source code for many discussed concepts, as well as benchmarks that were run to measure the effectiveness of GPU computation.

# Why?[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#why)

Why on earth would one want to use GPU for calculations? The answer is obvious – blazingly fast speed. The following paragraphs consider three different use cases, each with increasing complexity. While the presented examples are somehow naïve, the intention is to highlight the typical patterns of applications that _might_ benefit from GPU-powered calculations. Each example contains a CPU vs GPU comparison chart – a result of direct computation of the presented problem. The timings were measured on the iPad Air (5^th generation iPad) with iOS 7.1 beta 2.

## The Disappointing Linear Function[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#the-disappointing-linear-function)

Let’s start with the most basic function there is – a linear function. There are countless of applications for linear functions, so let’s pick one and see how well it performs:

```objc
f(x) = 3.4 * x + 10.2;
```

How should we compare the performance of GPU to CPU? While using time is the obvious choice, we shouldn’t focus on raw milliseconds. Comparing run-time for small and large input sets, would render the former one useless, as they would be merely visible on the plot, pitifully overlapping horizontal axis. Instead, we should consider the _ratio_ of CPU to GPU time. Making CPU performance normalized at 1.0, makes the GPU value easy to interpret – if the GPU performs twice as fast as the CPU, then the GPU’s value is 2.0. Here’s the comparison chart for GPU vs CPU for the computed linear function:

GPU vs CPU comparison

The horizontal axis of the chart represents the number of input `float` values and is in _logarithmic_ scale.

As you can see, GPU sucks in this case. Even for the very large input set (2^24 = over 16 million values), the GPU runs 0.31 times as “fast” as CPU i.e. it runs over 3 times _slower_. The only promising result is that the performance increases with input size. For sufficiently large data set, the GPU would overcome the CPU. Notice, however, that representing 2^24 `float` values already takes 64 MB of memory. Surely we’d hit memory limits before reaching any beneficial performance level.

## The Promising Complication[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#the-promising-complication)

Since linear function was so disappointing let’s reach into some more complicated functions from our math repository. The exponential function transpires in many natural phenomena e.g. [exponential decay](http://en.wikipedia.org/wiki/Exponential_decay). Paired with basic trigonometry functions it forms a solution of many differential equations, like the ones that rule the [damping](http://en.wikipedia.org/wiki/Damping). Let’s consider the following complicated mixture of exponent, sine, and cosine with some random coefficients:

```objc
f(x) = 2.0 * exp(-3.0 * x) * (sin(0.4 * x) + cos(-1.7 * x)) + 3.7;
```

Here’s the comparison chart for GPU vs CPU execution time:

GPU vs CPU comparison

First success! As soon as the input size crosses 2^16 (little over 65k values), the GPU is faster than the CPU. For very large data sets, the GPU is over 5 times faster.

## The Amazing Iteration[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#the-amazing-iteration)

As exciting as the results of the previous example were, we can do even better. Let’s consider an iterative computation. Imagine a simulation of huge number of bodies in a central gravitational field. Let’s make a few assumptions:

- each body has the same mass
- each body has the same initial position, but different initial velocity
- we can ignore body-to-body interaction
- the problem is two dimensional

The goal of the calculation is to answer the question: how far have the bodies flown in 10 seconds? In other words, what is the position of every single body after 10 seconds?

Reaching back to fundamentals of physics this simple equation comes to mind:

```objc
p(t) = p0 + v0 * t + 0.5 * a0 * t * t;
```

Unfortunately we can’t merely plug the values in and get the result in one step, because the acceleration of the body is not constant – it depends on the distance from field’s center. A very simple solution is to run the calculation in an iterative fashion, just like most of the physics engines do.

For a given position in space, we can get the body’s acceleration by measuring the value of gravitational force which is governed by [Newton’s law of universal gravitation](http://en.wikipedia.org/wiki/Newton's_law_of_universal_gravitation). Since this is merely an example, we can ignore all the constant coefficients and just notice that the force is proportional to the distance squared and points at the center of the field.

Let’s focus on the gist of the iteration itself. Each step will evaluate the current acceleration value, and then update values of both position and velocity using a forward [Euler method](http://en.wikipedia.org/wiki/Euler_method). The body of the iterative loop goes as follows:

```
1
2
3
4
5
6
7
8
9
```

```objc
float l = 1.0f/sqrtf(x*x + y*y);
float ax = -x*l*l*l;
float ay = -y*l*l*l;

x += vx*dt;
y += vy*dt;

vx += ax*dt;
vy += ay*dt;
```

Let’s settle for a time step of 0.1 seconds. Running the loop 100 times will result in good approximation of body’s position at t = 10s. Without further ado, here’s the GPU vs CPU comparison for the computation:

GPU vs CPU comparison

That’s right, the GPU was over 64 times faster. Sixty four. Times. Faster. While this example is somehow contrived (2D over 3D space, ignoring body to body collisions), the result is astonishing. In terms of absolute time, the CPU calculation took over 21 seconds, while the GPU took a _third_ of a second to do the work. Even for as few as 4096 `float` input values (2048 two dimensional vectors), the GPU is almost twice as fast as the CPU.

# How?[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#how)

From developer’s perspective the typical GPU programming works as follow:

- submit some vertex geometry
- process it in vertex shader
- let the GPU figure out the triangles
- process each fragment in fragment shader
- present result on the screen

While both vertex and fragment shader are customizable, so far only the fragment shader’s output was accessible to the developer in form of the generated framebuffer.

Long story short, using a new feature of OpenGL ES 3.0 called Transform Feedback, we _do_ have access to the output of the vertex shader.

## Transform Feedback[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#transform-feedback)

Here’s the excerpt from [the definition](http://www.opengl.org/wiki/Transform_Feedback) of Transform Feedback:

> Transform Feedback is the process of capturing Primitives generated by the Vertex Processing step(s), recording data from those primitives into Buffer Objects. This allows one to preserve the post-transform rendering state of an object and resubmit this data multiple times.

The crucial part is “preserve the post-transform rendering state”. Basically, we let the GPU do the work on the vertex data and then we can access the computed output. Actually, it doesn’t even have to be _vertex_ data per se, the GPU will happily make operations on whatever `float` values we provide. This is the essence of my method.

Setting up the Transform Feedback in OpenGL takes a dozen lines of code and I’ve done this with help of [this short article](http://prideout.net/blog/?p=67) and [this much longer tutorial](http://ogldev.atspace.co.uk/www/tutorial28/tutorial28.html). The setup can be split into two different steps.

First of all, we should inform OpenGL which shader variables should be used to write output data into the memory buffer. This stage _must_ happen before the shader gets linked. The following two lines of code present the setup, the crucial call being [glTransformFeedbackVaryings](http://www.khronos.org/opengles/sdk/docs/man3/xhtml/glTransformFeedbackVaryings.xml):

```c
const char * varyings[] = {"nameOfOutput1", "nameOfOutput2"};
glTransformFeedbackVaryings(program, sizeof(varyings)/sizeof(*varyings), varyings, GL_INTERLEAVED_ATTRIBS);
```

The second stage is very similar to a regular draw call setup, although enriched with some additional API calls:

```c
glUseProgram(program);
    
glEnable(GL_RASTERIZER_DISCARD); // discard primitives before rasterization stage
    
glBindBuffer(GL_ARRAY_BUFFER, readBuffer);
    
/* bind VAO or configure vertex attributes */
    
glBindBufferBase(GL_TRANSFORM_FEEDBACK_BUFFER, 0, writeBuffer); // the output should be written to writeBuffer
    
glBeginTransformFeedback(GL_POINTS);
glDrawArrays(GL_POINTS, 0, count);
glEndTransformFeedback();
    
glDisable(GL_RASTERIZER_DISCARD);
        
glFinish(); // force the calculations to happen NOW
```

Note, that there are some differences between desktop and mobile OpenGL implementations. For instance, I couldn’t compile my vertex shader on its own, I had to provide the dummy implementation of fragment shader as well (which apparently is not a requirement on desktop OpenGL).

As a final step, remember to include `OpenGLES/ES3/gl.h` header.

## Writing and Reading to Buffers[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#writing-and-reading-to-buffers)

Unlike traditional PCs, all iOS devices have Unified Memory Architecture. It doesn’t matter whether you read or write from “regular” memory or OpenGL allocated buffer – it’s all the same pool of on-device transistors.

I’ve done some crude tests and in fact, reading from “OpenGL” and “regular” memory takes the same amount of time and this is true for writing to memory as well.

On the desktop PCs, the RAM→VRAM memory transfer usually takes nontrivial amount of time. On the iOS, however, not only can you generate your data directly into OpenGL accessible memory, but also you can read back from it as well, without any apparent penalty! This is fantastic feature of iOS as mobile GPGPU platform.

Accessing data pointer for reading is super easy:

```objc
glBindBuffer(GL_ARRAY_BUFFER, sourceGPUBuffer);
float *memoryBuffer = glMapBufferRange(GL_ARRAY_BUFFER, 0, bufferSize, GL_MAP_READ_BIT);
    
//read from memoryBuffer
    
glUnmapBuffer(GL_ARRAY_BUFFER);
```

And so is accessing pointer for writing:

```objc
glBindBuffer(GL_ARRAY_BUFFER, targetGPUBuffer);
float *memoryBuffer = glMapBufferRange(GL_ARRAY_BUFFER, 0, bufferSize, GL_MAP_WRITE_BIT);
    
//write to memoryBuffer
    
glUnmapBuffer(GL_ARRAY_BUFFER);
```

Wrapping up data reading/writing logic in 3 additional lines of OpenGL boilerplate is surely worth the added benefits.

## Shader Calculations[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#shader-calculations)

OpenGL ES shaders are written in GLSL ES which is very much C-like with some sweet vector and matrix additions.

### Simple Vector Operations[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#simple-vector-operations)

GLSL defines `vec4` type that is a four component vector (with x, y, z, and w components). While the [language specification](http://www.khronos.org/registry/gles/specs/3.0/GLSL_ES_Specification_3.00.3.pdf) is the definite guide on the matter, there are few simple operations that are worth glancing over.

Let `a` and `b` be GLSL variables of `vec4` type. One can easily multiply all vector components by scalar:

```glsl
float c = 2.0;
vec4 r = a * c; // r.x = a.x * c, r.y = a.y * c...
```

One can also multiply two vectors component-wise:

```glsl
vec4 r = a * b; // r.x = a.x * b.x, r.y = a.y * b.y...
```

As well as feed entire vector into plethora of built-in functions:

```glsl
vec4 r = exp(a); // r.x = exp(a.x), r.y = exp(a.y)...
```

I highly recommend [OpenGL ES 3.0 API Reference Card](http://www.khronos.org/files/opengles3-quick-reference-card.pdf) which is a short primer on OpenGL API as well as GLSL cheat sheet. It contains a list of all built-in functions and it is generally recommended to use them instead of manually recoding even the trivial functionality. Built-ins may have direct hardware implementation and thus should be faster than their hand-written counterparts.

### Example Shader[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#example-shader)

Here’s the simplest shader written in GLSL ES 3.0 that doubles the input vector:

```
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
```

```glsl
#version 300 es

in  vec4 inVec;
out vec4 outVec;

vec4 f(vec4 x)
{
    return 2.0 * x;
}

void main()
{
    outVec = f(inVec);
}
```

As you can see, it’s very readable. We return a transformed input vector (marked as `in`) as an output vector (marked as `out`).

## Processing Power[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#processing-power)

Why do we bother doing four calculations at once in a `vec4` operations, instead of calculating single `float` values separately? Because crunching entire vectors is way faster. Some quick benchmarks showed using one `vec4` operation instead of four `float` ones is 3.5 times faster.

What’s even more surprising, we don’t even have to return just one `vec4` in a single shader calculation. We can use up to 16 `in` vectors to feed data to the shader. This seemingly arbitrary number is a platform specific value of `MAX_VERTEX_ATTRIBS` constant and is set in stone for all A7 devices. For the output vectors we’re limited by the `GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS` constant which for A7 is equal to 64. This means that we can define at most 16 `out` variables of `vec4` type (since each `vec4` has 4 components).

With that knowledge we can extend our shader to take in more input and generate more output:

```
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
```

```glsl
#version 300 es

in vec4 inVec1;    
in vec4 inVec2;    
in vec4 inVec3;    
in vec4 inVec4;

out vec4 outVec1;
out vec4 outVec2;
out vec4 outVec3;
out vec4 outVec4;

vec4 f(vec4 x)
{    
    return 2.0 * x;
}

void main()
{
    outVec1 = f(inVec1);
    outVec2 = f(inVec2);
    outVec3 = f(inVec3);
    outVec4 = f(inVec4);
}
```

By utilizing this method one achieves much faster execution. For instance going from 1 `in`/`out` vector pairs to 16 `in`/`out` vector pairs results in over 4 times performance increase (_The Disappointing Raise example_). In some cases however, the sweet spot is at 8 (_The Promising Plot_) or even 2 vector pairs (_The Amazing Simulation_), so this must be tuned manually on a case-by-case basis.

Obviously, writing that much code by hand and changing pieces of function calls all over the place is tedious, so my GitHub implementation generates the shader for a given number of vectors. The only responsibility of programmer is to provide a source for `vec4 f(vec4 x)` function.

## Multi-argument Functions[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#multi-argument-functions)

Throughout previous examples I’ve used a simple function that takes one argument and returns one value. However, it’s not that hard to write more complicated functions that take arbitrary (with some moderation) number of arguments.

Let’s consider a multi-argument function y = f(a, b, c) = a*b + c. In terms of math definitions this function is R³ → R. We don’t want to calculate just a single `float` value (it’s slow), so instead, we will calculate four values at once (an entire `vec4` of values). Therefore, a simple shader would have three `in` vectors and one `out` vector. Assuming `inVec1` contains a₀a₁a₂… values, `inVec2` contains b₀b₁b₂… values and so on, the shader code is trivial:

```glsl
vec4 f(vec4 a, vec4 b, vec4 c)
{
    return a * b + c; // adding vectors here!
}
```

While another option is for the data to be fetched from a single continuous buffer with a₀b₀c₀a₁b₁c₁a₂… ordering, notice that the shader would have to pick separate components from a vector and perform calculations one by one, which is hardly optimal.

## Single Argument Multivalued Functions[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#single-argument-multivalued-functions)

Let’s consider a multi-argument function (a, b) = f(x) = (cos(x), sin (x)), which means f is R → R². This function calculates location of point on a unit circle for a given angle x.

We can’t use a regular `vec4 f(vec4 x)` since we can’t output two vectors from on function. Instead, we could make use of a `vec4 f(vec2 x)` function, that would transform two input values into four output values. Clearly, the number of `out` shader vectors would have to be twice as large as number of `in` vectors.

## Multi-argument Multivalued Functions[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#multi-argument-multivalued-functions)

Finally, let’s consider a function (r, s) = f(a, b). This function takes in a 2D vector and returns a 2D vector (R² → R²). Considering previous cases one might argue this decays into calculating two values of regular y = f(x) function, however, this is hardly the case. For instance we can define a function that returns a perpendicular vector f(x, y) = (-y, x). We _couldn’t_ have done that in the plain old f(x) = y. On a side note, since we’re doing calculations on `vec4` technically we could look up the next component, but this technique is fairly limited, not to mention the extreme abuse of blindly reducing R² → R² to R → R.

As usual, we want to return as much data as possible, so we’re going to calculate two values of a function at once, packing them into one `vec4`:

```glsl
vec4 f(vec4 a)
{
    return vec4(-a.y, a.x, -a.w, a.z);
}
```

Speaking of crazy R² → R² to R → R reductions, consider function f(x, y) = (3.0 * x, 2.0 * y). In this case the calculation _does_ decay into regular f(x) = y calculation:

```glsl
vec4 f(vec4 a)
{
    return vec4(3.0, 2.0, 3.0, 2.0) * a;
}
```

Notice, that this is merely a technical twist since a shader doesn’t care whether the function is R² → R² or R → R, it’s just patiently crunching the numbers.

## Build Settings and Caveats[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#build-settings-and-caveats)

For my CPU vs GPU comparison I’ve compiled all programs with following settings.

- Optimization Level — Fastest, Aggressive Optimizations [-Ofast]
- Vectorize Loops — Yes
- Relax IEEE Compliance — Yes

The application was built using Xcode 5.1 (5B45j). I ran the tests on the iOS 7.1 beta2. Due to a [bug](https://devforums.apple.com/message/929561#929561) (Apple Developer account required) in iOS 7.0.x, one can’t apply user defined functions inside shaders used for Transform Feedback. Only `main()` and built-ins work.

Unsurprisingly, manual “inlining” the body of `f` function into `main` _did_ work. If you want to use Transform Feedback on iOS 7.0.x you can’t use function calls, so you’ll have to write a lot of code to make use of all 16 `in` vectors.

The time measurements were taken by running each test 8 times and then taking the average.

# When[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#when)

Now that we’ve seen how much performance the GPU offers and how to use it, let’s discuss the factors that can influence the application of the method.

## Data Size and Computation Complexity[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#data-size-and-computation-complexity)

Basically, there are two requirements for the GPU powered computation to triumph: large data sets and non trivial calculations.

The simple polynomial evaluation inside [The Disappointing Linear Function](#the-disappointing-linear-function) case is the best example of low-overhead calculations. This calculation is an example of [fused multiply-add](http://en.wikipedia.org/wiki/Multiply%E2%80%93accumulate_operation) which usually can be executed with just a single instruction. Moreover, clang is smart enough to generate vectorized code – the A7 computes _four_ fused multiply-adds at once. It’s an additional performance boost explaining why the CPU is running circles around the GPU in this case.

The more complex evaluation of [The Promising Complication](#the-promising-complication) case shows the benefits of parallelization. For large enough inputs, the simultaneous calculation performed by GPU starts winning.

Finally, [The Amazing Iteration](#the-amazing-iteration) allows the GPU to show its potential. While the CPU has to calculate each case one by one, the GPU crunches multiple cases at once, leaving the CPU in the dust.

The conclusion here is obvious. There is a huge overhead of firing up the OpenGL machinery, so once started it’s better to keep it rolling. There is one more amazing benefit of running the calculations on the GPU. After firing the calculations, the CPU is free to do whatever it wants.

## Precision[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#precision)

It must be noted that values returned by GPU calculations _might_ not be equal to the values returned by CPU. Are the GPU vs CPU errors large?

### Comparisons[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#comparisons)

[Bruce Dawson](http://randomascii.wordpress.com/about/) wrote an amazing [article series on floating point format](http://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition/). In part 4 of thereof, he presented a genuinely cool way to compare floating point values. Basically, due to the internal representation of floating point format, interpreting bits of `float` as `int`, incrementing that integer, and reinterpreting those new bits as `float` again, creates the next representable `float` number. To quote “Dawson’s obvious-in-hindsight theorem”:

> If the integer representations of two same-sign floats are subtracted then the absolute value of the result is equal to one plus the number of representable floats between them.

For instance, if the integer difference between two `float` values is 4, it means that one could fit 3 other `float` values in between. Quoting Dawson just once more:

> The difference between the integer representations tells us how many Units in the Last Place the numbers differ by. This is usually shortened to ULP, as in “these two floats differ by two ULPs.”

Just for the reference, I’ve also calculated the value of relative `float` error, defined as:

```c
fabsf((cpu_value - gpu_value)/cpu_value);
```

For the evaluated examples, I will refer to the integer difference as ULP, and to the relative float value error as FLT.

Unfortunately, both methods have some issues for comparing near-zero values, but in general they provide a good overview of what’s going on.

#### The Disappointing Linear Function[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#the-disappointing-linear-function-1)

```plain
ULP: avg: 0.0620527
     max: 1
     min: 0
FLT: avg: 6.24647e-09
     max: 1.19209e-07
     min: 0
```

The values calculated by GPU are as little as 1 ULP away from the CPU’s result and the average being so low, shows that less than 7% of values were not exactly equal to the CPU computation.

#### The Promising Complication[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#the-promising-complication-1)

```plain
ULP: avg: 0.527707
     max: 3
     min: 0
    
FLT: avg: 3.34232e-08
     max: 2.49631e-07
     min: 0
```

The maximum ULP error jumped to 3 and the average ULP error increased as well. The relative error still provides a good indication that the value of error is insignificant.

##### The Amazing Iteration[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#the-amazing-iteration-1)

```plain
ULP: avg: 46.6319
     max: 100
     min: 0

FLT: avg: 3.49051e-06 
     max: 8.61719e-06
     min: 0
```

The maximum value of 100 ULPs is a hint that each iteration accumulated some error. The relative error is still low at 3.49×10^-4%.

### Reasons[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#reasons)

By default the precision of `float` (and, as direct result, of `vec2`, `vec3` and `vec4` as well) inside vertex shader is set to `highp` (GLSL ES 3.0 spec 4.5.4) which essentially is regular [IEEE 754](http://en.wikipedia.org/wiki/IEEE_floating_point) `float`. Where do the differences in comparison to CPU results come from?

My familiarity with secrets of floating point values is not that great (despite _starting_ to read [What Every Computer Scientist Should Know About Floating-Point Arithmetic](http://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html) a couple of times). I have some hypotheses, but you should take them with a grain of salt.

One of the reasons for these effects could be slightly different implementations of `exp`, `pow` and trigonometry functions. However, _The Disappointing Linear Function_ doesn’t use any built-ins and the small errors are still there. I suspect the most important reason is that the [rounding mode](http://en.wikipedia.org/wiki/Floating_point#Rounding_modes) inside GLSL computation is not defined by the specification. This could explain why doing 100 iterations of an algorithm inside GPU results in at most 100 ULPs difference.

### Does it Matter?[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#does-it-matter)

Obviously, if precision is mission critical you wouldn’t use `float` anyway, jumping to `double` instead, thus skipping the GPU calculations entirely. Just for the record (and for the sake of linking to an interesting rant), [you shouldn’t rely on the math library to perform _exact_ calculations](http://lists.apple.com/archives/mac-games-dev/2007/Oct/msg00188.html) anyway.

For the more mundane tasks, the precision doesn’t matter, unless you do thousands of iterations inside a shader. For games and simple simulations you shouldn’t care at all.

# Final Words[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exploring-gpgpu-on-ios/#final-words)

I’m extremely pleased with the results. It really shows that GPUs inside iOS devices are extremely powerful. I expected perhaps a 3-5x speed improvement, but the extremity of 64x is a shocker. In case of highly iterative calculations, you can reduce the wait time for the user from about a minute to a little under one second. Even though the presented examples were somehow artificial, the benefits of huge performance gains and offloading the CPU are of utmost importance. Without a doubt, using Transform Feedback limits the effectiveness of the method to the brand new devices powered by A7 chip, but as time goes, this will become less of an issue.

As for the further work, a lot can still be done. Now that iOS7 enables reading textures in vertex shader (although [some claim](http://stackoverflow.com/a/6754705/558816) it was possible in previous releases as well), one could treat a float texture as a source of truly random (as in random _access_, not random value) memory resulting in much more advanced vertex shader computation techniques. However, this still doesn’t solve the random write problem.

On the other hand, one might also try going the fragment shader way, using float textures as input and half float textures as output, but it still does not provide full featured GPGPU capabilities.

All those effort will become vein, when Apple provides access to the now [private](https://github.com/EthanArbuckle/IOS-7-Headers/tree/master/PrivateFrameworks/OpenCL.framework) [OpenCL](http://www.khronos.org/opencl/) framework. Until then, OpenGL abuse is the primary toy for us to play.
