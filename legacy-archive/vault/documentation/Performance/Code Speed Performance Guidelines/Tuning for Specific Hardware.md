---
title: Code Speed Performance Guidelines
apple_id: 10000150i
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/CodeSpeed/Articles/HardwareTuning.html
archived_at: '2026-07-18T01:47:01.154729Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Code Speed Performance Guidelines](Introduction%20to%20Code%20Speed%20Performance%20Guidelines.md)


[Next](Tuning%20Your%20Java%20Code.md)[Previous](Notifications.md)

# Tuning for Specific Hardware

Not all processors are alike. Each new processor design brings with it a new way of thinking about your code and new techniques for improving performance. By taking advantage of the latest features on the newest processors, you can often see significant speed increases in your software. If you support the right features, you can also gain speed on the new processor without losing speed on older processor models.

The following sections offer tips primarily aimed at improving performance on the G5 processor. However, using these techniques should not hurt performance on older processors. Most of the techniques simply make it easier for the compiler and instruction scheduler to tune your code.

The G5 processor uses a massively parallel execution core to perform multiple instructions simultaneously. In addition to Velocity Engine support, the processor includes two separate floating-point instruction units, two integer processing units, and several other units for managing the flow of instructions. Maximizing the performance of your software means keeping these instruction units busy as much as possible. This means you need to write your code with the following in mind:

- Do more work in parallel. Consider intermixing unrelated floating-point and integer-based operations to keep more instruction units busy.
- Manually unroll important loops, or use the `-funroll-loops` option with GCC. Partially unrolling a loop might let you do more work within each loop iteration.
- Enable instruction scheduling in your Xcode project, or pass the `-mtune=G5` option to GCC.

Bottlenecks in the execution of G5 instructions often occur because code was written with a serial flow in mind. If your code computes a number of similar (but independent) values, it is advantageous to arrange your code in a way that lets the instruction scheduler fill the instruction unit pipelines.

Consider the simple function in Listing 1, which computes a sum and returns the value. This function takes advantage of only one instruction unit, which leaves other instruction units sitting idle.

__Listing 1__  Computing a sum the slow way

```
double ComputeSum_slow(int numIterations)
{
    int i;
    double sum = 0.0;

    for (i = 0; i < numIterations; i++)
    {
        sum += 1.0;
    }
    return sum;
}
```

If the number of iterations is guaranteed to be large enough, consider what happens if you take this code and partially unroll the loop. Listing 2 shows an updated version of this code, but in this revised edition the loop now performs eight floating-point operations through each iteration. The instruction scheduler sees this as a way to fill the pipelines of both floating-point instruction units. Although the same amount of work is being done, the distributed nature of the work results in code that is up to 10 times faster than the original.

__Listing 2__  Computing a sum in parallel

```
double ComputeSum_fast(int numIterations)
{
    double sum0, sum1, sum2, sum3, sum4, sum5, sum6, sum7;
    int i;

    sum0 = sum1 = sum2 = sum3 = sum4 = sum5 = sum6 = sum7 = 0.0;

    for (i = 0; (i+7) < numIterations; i += 8)
    {
        sum0 += 1.0;
        sum1 += 1.0;
        sum2 += 1.0;
        sum3 += 1.0;
        sum4 += 1.0;
        sum5 += 1.0;
        sum6 += 1.0;
        sum7 += 1.0;
    }
    return (sum0 + sum1 + sum2 + sum3 +sum4 +sum5 + sum6 + sum7);
}
```

Although the preceding example shows a simple case, it hopefully demonstrates the effect of doing more work in parallel. Applied to your own code, you should be able to find similar improvements by breaking out parallel calculations. Especially for critical operations, such as large scientific calculations, this kind of optimization can lead to tremendous performance gains.

To process floating-point values efficiently, processors typically require that they be aligned along certain memory boundaries. Floating-point alignment is especially important for the G5 processor, where misaligned values can cause a processor exception. Given that Carbon and Cocoa both use floating-point numbers extensively for working with graphical elements, it is important (and relatively easy) to ensure correct alignment of floating-point values in your compiled code.

To ensure that floating-point values are aligned properly, add the GCC compiler option `-malign-natural` to your project’s build settings. This option causes the compiler to align floating-point values along their natural boundaries. Although there are other options for doing floating-point alignment, the `-malign-natural` option is preferred because it handles all of the important types, including `double` floating-point values. For more information about this option, see the `gcc` man page.

As processor speeds increase, so does the latency for accessing memory. To help alleviate this problem, the G5 processor includes a hardware prefetch engine to get data into the processor caches before it is needed. However, taking advantage of this prefetch engine requires you to do the following:

- Pack your data structures together to improve their locality.
- Walk through your data structures contiguously so that the hardware prefetch engine can stream data in just before you need it.

G5 cache lines are 128 bytes long. If your data structures are tightly packed, the prefetch engine can load the entire structure into the fewest number of cache lines. This improves both the latency in loading the cache and your cache usage, since more useful memory is in the cache at the same time.

You also need to be careful about accessing memory in a contiguous manner. For example, if you need to iterate over the entries in a two-dimensional array of data, there are two ways to do it. You can walk the columns of the first row, followed by the columns of the second row; or, you can walk the first element of each row, followed by the second element of each row. Because of the organization of memory, walking the columns of the first row, followed by the columns of the second row is much more efficient because the column data is contiguous. Walking an array in this order is often many times faster than walking down a single column of data.

The Velocity Engine (also known as AltiVec) is a 128-bit vector execution unit embedded in the G4 and G5 processors. This unit lets you perform highly parallel operations, such as high-bandwidth data processing (for streaming video) and algorithmically intensive computations used in graphics, audio, and mathematical operations. If you perform any operations of this nature, you should incorporate Velocity Engine support into your application.

In many cases, all you need to do to take advantage of Velocity Engine is link with the right frameworks and libraries. OS X uses Velocity Engine to implement accelerated support for the following types of operations:

- 

  Digital signal processing—Fast Fourier Transforms, convolutions, squares, and more
- 

  Vector Image Processing—resize, distort, convolution, morphing, alpha compositing, format conversion, and other operations on images
- 

  Basic Linear Algebra Subprograms—vector-scaling linear algebra, matrix-vector linear algebra, and matrix operations
- Linear Algebra operations—linear equation computations, find least-square solutions of linear systems of equations, solve eigenvalue problems, and perform many other operations from the LAPACK library
- 

  Vector Mathematics—computational functions such as divides, square roots, and exponential functions.
- Basic Algebraic operations—basic algebraic operations on operands up to 128 bits in size
- 

  Big Number operations—basic math, shift, and rotate operations on operands ranging in size from 256 bits to 1024 bits.

The Accelerate framework (introduced in OS X version 10.3) coalesces support for these operations in a single framework. If your software supports versions of OS X earlier than 10.3, you might need to include several separate libraries and frameworks instead.

If you choose to write your own custom code using Velocity Engine instructions, you should always check to make sure the feature is available on the current hardware. Although most newer computers support Velocity Engine, some older computers based on the G3 processor might not. If you execute Velocity Engine instructions on one of these older computers, your program will crash.

To check whether Velocity Engine is available, you can either use the Gestalt feature in Core Services or use the `sysctl` function. To use the Gestalt feature, query the system using the `gestaltPowerPCProcessorFeatures` selector, which is defined in `Gestalt.h`. To use the `sysctl` function, you would write a function similar to the one in Listing 3.

__Listing 3__  Checking for Velocity Engine availability

```
Boolean HasVelocityEngine(void)
{
    int mib[2], hasVE;
    size_t len;

    mib[0] = CTL_HW;
    mib[1] = HW_VECTORUNIT;
    len = sizeof(hasVE);
    sysctl(mib, 2, &hasVE, &len, NULL, 0);
    return (hasVE != 0);
}
```

Although checking for the availability of vector instructions is sufficient for most developers, if you do any data streaming in your application, you should also check to see if the `dcba` instruction is available as well. Gestalt and `sysctl` both offer ways to tell if this instruction is available. For more information, see the _[Gestalt Manager Reference](https://developer.apple.com/documentation/coreservices/carbon_core/gestalt_manager)_ or the `sysctlbyname` man page.

[Next](Tuning%20Your%20Java%20Code.md)[Previous](Notifications.md)

