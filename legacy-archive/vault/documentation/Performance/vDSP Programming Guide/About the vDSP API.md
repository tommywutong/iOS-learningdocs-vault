---
title: vDSP Programming Guide
apple_id: TP40005147
resource_type: Guide
platform: iOS|macOS
topic: Mathematical Computation
technology: Accelerate
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/vDSP_Programming_Guide/About_vDSP/About_vDSP.html
archived_at: '2026-07-18T01:50:33.375705Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [vDSP Programming Guide](Introduction.md)



# About the vDSP API

The vDSP API provides mathematical functions for applications such as speech, sound, audio, and video processing, diagnostic medical imaging, radar signal processing, seismic analysis, and scientific data processing.

The vDSP functions operate on real and complex data types. The functions include data type conversions, fast Fourier transforms (FFTs), and vector-to-vector and vector-to-scalar operations.

The vDSP functions have been implemented in two ways: as vectorized code, which uses vector instructions (SSE3, for example) in the processor, and as scalar code, which does not. The vDSP API uses the appropriate version depending on the arguments given and the vector capabilities of the processor.

The header file `vDSP.h` defines nonstandard data types used by the vDSP functions and symbols accepted as flag arguments to vDSP functions. The vDSP API itself is part of vecLib, which in turn is part of the Accelerate framework in OS X. Thus, when actually including the header in your code, you should always use the umbrella framework header (`#include <Accelerate/Accelerate.h>`).

This section describes the calling conventions used with the vDSP functions and discusses the use of address strides.

Most vDSP functions accept input data and produce output data. All such data arguments, whether vector or scalar, are passed by reference; that is, callers pass pointers to memory locations from which input data is read and to which output data is written.

Other argument types passed to vDSP functions include:

- Address strides, which tell a function how to step through input and output data. Stride examples include every element, every other element, every third element, and so forth.
- Flags, which influence a function's behavior in some way. Examples include forward versus inverse directional flags for discrete Fourier transforms.
- Element counts, which tell functions how many elements to process.

Address strides, flags, and element counts are integer values and, unlike input and output data, these values are passed to a function directly, not by reference. For example, the vector multiply command, [vDSP_vmul](https://developer.apple.com/documentation/accelerate/1450344-vdsp_vmul), uses vector pointers, address strides, and element counts:

```
void vDSP_vmul(
    float *__A,       /* input vector 1 */
    vDSP_Stride __IA, /* address stride for input vector 1 */
    float *__B,       /* input vector 2 */
    vDSP_Stride __IB, /* address stride for input vector 2 */
    float *__C,       /* output vector */
    vDSP_Stride __IC, /* address stride for output vector */
    vDSP_Length __N   /* real output count */
);
```

where `vDSP_Stride` is defined to be the type `long` and `vDSP_Length` is defined to be the type `unsigned long`.

A typical call to [vDSP_vmul](https://developer.apple.com/documentation/accelerate/1450344-vdsp_vmul) illustrates how the input and output data is passed by reference, whereas address strides, flags, and element counts pass directly:

```
/* Multiply sequential values of two 1,024-point vectors */
float a[1024], b[1024], c[1024];
vDSP_vmul( a, 1, b, 1, c, 1, 1024 );
```


As mentioned earlier, address strides tell functions how to step through input and output data: every element, every second element, every third element, and so on. Though usually positive, address strides can be specified as negative for most vDSP functions. Developers should be aware, however, that negative address strides can often change the arithmetic operation of a function, so experimentation with input values that produce known results is recommended.

When operating on real vectors, address strides of 1 address every element, address strides of 2 address every other element, and so forth. For some functions, address strides of 1 for real vectors result in superior performance over non-unit strides because longer strides require those functions to fall back to using scalar-mode CPU instructions. The use of split complex yields similar performance benefits for complex vectors.

When operating on complex vectors, there are two formats for storing each complex number in a vector element: split complex and interleaved complex.

With split complex vectors (the [DSPSplitComplex](https://developer.apple.com/documentation/kernel/dspsplitcomplex) and [DSPDoubleSplitComplex](https://developer.apple.com/documentation/accelerate/dspdoublesplitcomplex) types), the real parts of the elements in the vector are stored in one array, and the imaginary parts are stored in a separate array. Thus, as with real arrays, an address stride of 1 addresses every element. Most functions use split complex vectors.

With interleaved complex vectors (the [DSPComplex](https://developer.apple.com/documentation/accelerate/dspcomplex) and [DSPDoubleComplex](https://developer.apple.com/documentation/kernel/dspdoublecomplex) types), complex numbers are stored as ordered pairs of floating point or double values. Therefore, a stride of 2 is specified to process every vector element; a stride of 4 is specified to process every other element; and so forth.

Repeating the synopsis of [vDSP_vmul](https://developer.apple.com/documentation/accelerate/1450344-vdsp_vmul), the definition line shows `vDSP_vmul` to be of type `void`; that is, it provides no return value to the caller:

```
extern void vDSP_vmul(float *__A, vDSP_Stride __IA, float *__B, vDSP_Stride __IB, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

All data returned by these functions is done inline through overwriting the array arguments, in this case, argument `__C`.

Functions in the vDSP API begin with a `vDSP_` prefix. Within this namespace, the vDSP API contains multiple variants of functions depending on whether they use single-precision or double-precision numbers. These variants can be distinguished by their suffix.

| Suffix | Meaning |
| --- | --- |
| no suffix | Uses single-precision floating point numbers. |
| `D` | Uses double-precision floating point numbers |

For example, the [vDSP_fft2d_zip](https://developer.apple.com/documentation/accelerate/1450430-vdsp_fft2d_zip) and [vDSP_fft2d_zipD](https://developer.apple.com/documentation/accelerate/1450508-vdsp_fft2d_zipd) functions are equivalent except that the former works with single-precision values and the latter with double-precision values.

The vDSP API is based on standard C integer and floating-point data types. It defines four additional data types to represent vector elements:

- [DSPComplex](https://developer.apple.com/documentation/accelerate/dspcomplex)—An ordered pair of `float` values stored as a packed data structure. Functions with no suffix may take this type.
- [DSPDoubleComplex](https://developer.apple.com/documentation/kernel/dspdoublecomplex)—An ordered pair of `double` values stored as a packed data structure. Functions with a `D` suffix may take this type.
- [DSPSplitComplex](https://developer.apple.com/documentation/kernel/dspsplitcomplex)—An ordered pair of `float` values stored as a pair of pointers into an array of real parts and an array of imaginary parts. Functions with no suffix and a `z` at the beginning of the last part of the name typically take this type.
- [DSPDoubleSplitComplex](https://developer.apple.com/documentation/accelerate/dspdoublesplitcomplex)—An ordered pair of `double` values stored as a pair of pointers into an array of real parts and an array of imaginary parts. Functions with a `D` suffix and a `z` at the beginning of the last part of the name typically take this type.

