---
title: Universal Binary Programming Guidelines, Second Edition
apple_id: TP40002217
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2009-02-04'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/universal_binary/universal_binary_vector/universal_binary_vector.html
archived_at: '2026-07-15T08:16:38.822317Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Universal Binary Programming Guidelines, Second Edition](Introduction.md)


[Next](Rosetta.md)[Previous](Guidelines%20for%20Specific%20Scenarios.md)

# Preparing Vector-Based Code

This chapter is relevant only for those developers who want to start writing vector-based code or whose applications already directly use the AltiVec extension to the PowerPC instruction set. AltiVec instructions, because they are processor specific, must be replaced on Intel-based Macintosh computers. You can choose from these two options:

- Use the Accelerate framework. This is the recommended option because the framework provides a layer of abstraction that lets you perform vector-based operations without needing to use low-level vector instructions yourself. See [Accelerate Framework](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrqhawtenjtgm4te).
- Port AltiVec code to the Intel instruction set architecture (ISA). This solution is available for developers who have performance needs that can’t be met by using the Accelerate framework. See [Rewriting AltiVec Instructions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrqhawtenjtgy2dq).

The Accelerate framework, introduced in Mac OS X v10.3 and expanded in v10.4, is a set of high-performance vector-accelerated libraries. You don’t need to be concerned with the architecture of the target machine because the routines in this framework abstract the low-level details. The system automatically invokes the appropriate instruction set for the architecture that your code runs on.

This framework contains the following libraries:

- vImage is the Apple image processing framework that includes high-level functions for image manipulation—convolutions, geometric transformations, histogram operations, morphological transformations, and alpha compositing—as well as utility functions that convert formats and perform other operations. See _[vImage Programming Guide](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/vImage/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001001)_.
- vDSP provides mathematical functions that perform digital signal processing (DSP) for applications such as speech, sound, audio, and video processing, diagnostic medical imaging, radar signal processing, seismic analysis, and scientific data processing. The vDSP functions operate on real and complex data types and include data type conversions, fast Fourier transforms (FFTs), and vector-to-vector and vector-to-scalar operations.
- vMathLib contains vector-accelerated versions of all routines in the standard math library. See _[vecLib Framework Reference](https://developer.apple.com/documentation/accelerate/veclib)_.
- LAPACK is a linear algebra package that solves simultaneous sets of linear equations, tackles eigenvalue and singular solution problems, and determines least-squares solutions for linear systems.
- BLAS (Basic Linear Algebra Subroutines) performs basic vector and matrix computations.
- vForce contains routines that take matrices as input and output arguments, rather than single variables.

Most of the tasks required to vectorize for AltiVec—restructuring data structures, designing parallel algorithms, eliminating branches, and so forth— are the same as those you’d need to perform for the Intel architecture. If you already have AltiVec code, you’ve already completed the fundamental vectorization work needed to rewrite your application for the Intel architecture. In many cases the translation process will be smooth, involving direct or nearly direct substitution of AltiVec intrinsics with Intel equivalents.

The MMX, SSE, SSE2, and SSE3 extensions provide analogous functionality to AltiVec. Like the AltiVec unit, these extensions are fixed-sized SIMD (Single Instruction Multiple Data) vector units, capable of a high degree of parallelism. Just as for AltiVec, code that is written to use the Intel ISA typically performs many times faster than scalar code.

Before you start rewriting AltiVec instructions for the Intel instruction set architecture, read _[AltiVec/SSE Migration Guide](../../Performance/AltiVec-SSE%20Migration%20Guide/Introduction%20to%20AltiVec-SSE%20Migration%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdomrz)_. It outlines the key differences between architectures in terms of vector-based programming, gives an overview of the SIMD extensions on x86, lists what you need to do to build your code, and provides an in-depth discussion on alignment and other relevant issues.

The following resources are relevant for rewriting AltiVec instructions for the Intel architecture:

- [Architecture-Independent Vector-Based Code](Architecture-Independent%20Vector-Based%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrrgmwviucykjcummjqge) shows how to write a fast matrix-multiplication function with a minimum of architecture-specific coding.
- Intel software manuals describe the x86 vector extensions:

  [http://developer.intel.com/design/Pentium4/documentation.htm](http://developer.intel.com/design/Pentium4/documentation.htm)
- [Perf-Optimization-dev](http://lists.apple.com/mailman/listinfo/perfoptimization-dev) is a list for discussions on analyzing and optimizing performance in Mac OS X. You can subscribe at:

  [http://lists.apple.com/mailman/listinfo/perfoptimization-devlists.apple.com](http://lists.apple.com/mailman/listinfo/perfoptimization-devlists.apple.com)

[Next](Rosetta.md)[Previous](Guidelines%20for%20Specific%20Scenarios.md)

