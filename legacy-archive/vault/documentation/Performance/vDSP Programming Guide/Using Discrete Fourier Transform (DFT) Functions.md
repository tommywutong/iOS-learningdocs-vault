---
title: vDSP Programming Guide
apple_id: TP40005147
resource_type: Guide
platform: iOS|macOS
topic: Mathematical Computation
technology: Accelerate
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/vDSP_Programming_Guide/USingDFTFunctions/USingDFTFunctions.html
archived_at: '2026-07-18T01:50:33.583745Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [vDSP Programming Guide](Introduction.md)



# Using Discrete Fourier Transform (DFT) Functions

The vDSP API provides a small set of functions called the Discrete Fourier Transform (DFT) functions. They package some of the FFT capabilities of vDSP into a convenient, modern API that supports the following model:

- Set up all the parameters of an FFT operation using a `CreateSetup` function, which creates an opaque "setup" object of type `vDSP_DFT_Setup`.
- Call the `Execute` function , passing in the setup object, to execute the FFT operation.
- When the setup object is no longer needed, call the `DestroySetup` function to deallocate all memory that has been allocated by vDSP in connection with this setup.

For an example of DFT functions in use, see _[vDSP Examples](https://developer.apple.com/library/archive/samplecode/vDSPExamples/Introduction/Intro.html#//apple_ref/doc/uid/DTS10004300)_.

There are four flavors of `CreateSetup`, two flavors of `DestroySetup`, and two flavors of `Execute`.

The two flavors of `DestroySetup` and `Execute` simply distinguish between single- and double-precision data:

- [vDSP_DFT_DestroySetup](https://developer.apple.com/documentation/accelerate/1450791-vdsp_dft_destroysetup) // single precision
- [vDSP_DFT_DestroySetupD](https://developer.apple.com/documentation/accelerate/1450367-vdsp_dft_destroysetupd) // double precision
- [vDSP_DFT_Execute](https://developer.apple.com/documentation/accelerate/1450538-vdsp_dft_execute) // single precision
- [vDSP_DFT_ExecuteD](https://developer.apple.com/documentation/accelerate/1449812-vdsp_dft_executed) // double precision

The four flavors of `CreateSetup` allow for single- or double-precision data, and for either complex-to-complex or real-to-complex/complex-to-real operations:

- [vDSP_DFT_zop_CreateSetup](https://developer.apple.com/documentation/accelerate/1450061-vdsp_dft_zop_createsetup) // single precision, complex-to-complex
- [vDSP_DFT_zop_CreateSetupD](https://developer.apple.com/documentation/accelerate/1450730-vdsp_dft_zop_createsetupd) // double precision, complex-to-complex
- [vDSP_DFT_zrop_CreateSetup](https://developer.apple.com/documentation/accelerate/1449739-vdsp_dft_zrop_createsetup) // single precision, real-to-complex or complex-to-real
- [vDSP_DFT_zrop_CreateSetupD](https://developer.apple.com/documentation/accelerate/1449790-vdsp_dft_zrop_createsetupd) // double precision, real-to-complex or complex-to-real

[vDSP_DFT_zrop_CreateSetup](https://developer.apple.com/documentation/accelerate/1449739-vdsp_dft_zrop_createsetup) and [vDSP_DFT_zrop_CreateSetupD](https://developer.apple.com/documentation/accelerate/1449790-vdsp_dft_zrop_createsetupd) create setups for an FFT operation that is real-to-complex in the forward direction, or complex-to-real in the reverse direction.

A setup contains all the information needed to perform an FFT operation, except the pointers to input and output data vectors. It may include information about memory allocations made by previously created setups.

This is a preparation step to be done when a program is starting, or is starting some new phase (e.g., when a communication channel is opened). It should never be done during real-time processing. The setup routine is slow and is called only once to prepare data that can be used many times.

DFT setups can be shared with other DFT setups of any type (as well as DCT setups; see note below) with the same precision. This occurs when you pass a previously created setup in the `Previous` parameter of a `CreateSetup` call that creates another setup. When setups are shared, vDSP may be able to share memory amongst them, leading to better efficiency. Sharing any setup of a group of setups that share data will result in a new setup sharing data with all of the group.

1. Use one of the CreateSetup functions listed above.
2. Pass in any existing setup that you want the new setup to share with, or pass `NULL` if you don’t have one.
3. Specify the length of the transform, i.e. the number of real or complex elements to process. Only certain lengths are implemented: see notes below.

- Length is the number of real elements to be transformed (forward direction) or produced (reverse direction). Implemented lengths are given by

  - 2_n_
  - _f_ \* 2_n_, where _f_ is 3, 5, or 15 and _n_ >= 4.

- Length is the number of complex elements to be transformed (forward direction) or produced (reverse direction). Implemented lengths are given by

  - 2_n_
  - _f_ \* 2_n_, where _f_ is 3, 5, or 15 and _n_ >= 3.

Once you have created all the setups needed for a particular phase of your program, you can execute them in any desired order. Each type of setup can only be executed by an `Execute` function with matching data types, as described in the following sections.

A setup does its work when it is passed into an `Execute` function. It provides the complete definition of the desired transform, leaving only the data pointers to be provided to the `Execute` function. The setup can be executed repeatedly as many times as desired, changing the data pointers each time.

When a setup is no longer needed, it should be destroyed with the appropriate `DestroySetup` function. This releases any memory or other assets that may have been allocated in creating and using the setup.

The Discrete Cosine Transforms (DCT) API is integrated with the DFT API. Although it has its own `CreateSetup` and `Execute` functions, DCT setups can be freely shared with DFT setups of the same precision, and the same `DestroySetup` functions are used for both DFT and DCT.

The Discrete Cosine Transforms API is described in the next chapter of this document.

1. Create the setup with [vDSP_DFT_zop_CreateSetup](https://developer.apple.com/documentation/accelerate/1450061-vdsp_dft_zop_createsetup), passing in parameters as described above.
2. Use the [vDSP_DFT_Execute](https://developer.apple.com/documentation/accelerate/1450538-vdsp_dft_execute) function to execute the transform.
3. Pass the setup in the `Setup` parameter.
4. Pass pointers to two single-precision input vectors in the `Ir` and `Ii` parameters. `Ir` should contain the real parts and `Ii` the imaginary parts.
5. Pass pointers to two single-precision output vectors in the `Or` and `Oi` parameters. After execution,`Or` will contain the real data and `Oi` the imaginary data.
6. Call the [vDSP_DFT_Execute](https://developer.apple.com/documentation/accelerate/1450538-vdsp_dft_execute) function as many times as desired with the same setup and different input data.

- All four data vectors must be at least as long as the length specified in the setup. If this is not the case, or if the length is not one of the implemented values, [vDSP_DFT_Execute](https://developer.apple.com/documentation/accelerate/1450538-vdsp_dft_execute) will return 0.

- `Or` may equal `Ir` and `Oi` may equal `Ii`. Otherwise, no overlap of `Or`, `Oi`, `Ir`, and `Ii` is supported.

- Performance is good when the data vector addresses are 16-byte aligned. Other alignments are supported, but performance may be significantly worse in some cases, depending on the processor model or the transform length (because different algorithms are used for different forms of transform length).

- In the forward direction, the scale is 1: CFimp = CFmath.
- In the reverse direction, the scale is N, the number of elements processed: CFimp = CFmath\*N.
- For a more detailed discusssion, see Scaling Fourier Transforms

For an example of DFT functions in use, see _[vDSP Examples](https://developer.apple.com/library/archive/samplecode/vDSPExamples/Introduction/Intro.html#//apple_ref/doc/uid/DTS10004300)_.

This is exactly the same as the single-precision complex-to-complex case described above, with appropriate type changes. Use [vDSP_DFT_zop_CreateSetupD](https://developer.apple.com/documentation/accelerate/1450730-vdsp_dft_zop_createsetupd) to create the setup, remembering that only double-precision setups can be shared. Use [vDSP_DFT_ExecuteD](https://developer.apple.com/documentation/accelerate/1449812-vdsp_dft_executed) to execute the transform, passing double precision data vectors in `Ir`, `Ii`, `Or` and `Oi` parameters.

The real-to-complex transform is in the forward direction; the complex-to-real transform is in the reverse direction.

1. Create the setup with [vDSP_DFT_zrop_CreateSetupD](https://developer.apple.com/documentation/accelerate/1449790-vdsp_dft_zrop_createsetupd), passing in parameters as described above.
2. Pass the setup in the `Setup` parameter.
3. Pass pointers to two single-precision input vectors (type `float[]`) in the `Ir` and `Ii` parameters. See note on data layout below.
4. Pass pointers to two single-precision output vectors (type `float[]`) in the `Or` and `Oi` parameters. See note on data layout below.
5. Call the [vDSP_DFT_Execute](https://developer.apple.com/documentation/accelerate/1450538-vdsp_dft_execute) function as many times as desired with the same setup and different input data.

- All four data vectors must be at least as long as the length specified in the setup. If this is not the case, arrays will be overrun and results are unspecified.

- Let h stand for the input array of real numbers. Its even-index elements are stored in `Ir` and its odd-index elements are stored in `Ii`:
- |  |
```
for 0 <= j < N/2
  h[2*j+0] = Ir[j], and
  h[2*j+1] = Ii[j].
```
- Let H stand for the output array of complex numbers. H[0] and H[N/2] are the DC and Nyquist values, respectively, and are both real. Therefore their imaginary parts are implied (==0), and `Or`[0] contains the DC value H[0] while `Oi`[0] contains the Nyquist value H[N/2].
- |  |
```
H[0  ] = Or[0].  (H[0  ] is pure real.)
H[N/2] = Oi[0].  (H[N/2] is pure real.)
```
- Because of inherent symmetry in H, the first half of the elements of H are the complex conjugates of the second half, so only the first half needs to be represented in `Or` and `Oi`:
- |  |
```
for 1 < k < N/2,
  H[k] = Or[k] + i * Oi[k].
```
- The packing of complex data for real FFTs is explained in greater depth in Data Packing for Real FFTs.

- In the reverse direction, the layouts of the input and output arrays are swapped. `Ir` and `Ii` describe an input array with complex elements laid out as described above for `Or` and `Oi`. When vDSP_DFT_Execute returns, `Or` and `Oi` contain a pure real array, with its even-index elements stored in `Or` and its odd-index elements in `Oi`.

- `Or` may equal `Ir` and `Oi` may equal `Ii`. Otherwise, no overlap of `Or`, `Oi`, `Ir`, and `Ii` is supported.

- Performance is good when the data vector addresses are 16-byte aligned. Other alignments are supported, but performance may be significantly worse in some cases, depending on the processor model or the transform length (because different algorithms are used for different forms of transform length).

- In the forward direction, the scale is 2: CFimp = CFmath\*2.
- In the reverse dirrection, the scale is N, the number of elements processed: CFimp = CFmath\*N.
- For a more detailed discusssion, see Scaling Fourier Transforms.

For an example of DFT functions in use, see _[vDSP Examples](https://developer.apple.com/library/archive/samplecode/vDSPExamples/Introduction/Intro.html#//apple_ref/doc/uid/DTS10004300)_.

This is exactly the same as the single-precision real-to-complex or complex-to-real case described above, with appropriate type changes. Use [vDSP_DFT_zrop_CreateSetupD](https://developer.apple.com/documentation/accelerate/1449790-vdsp_dft_zrop_createsetupd) to create the setup, remembering that only double-precision setups can be shared. Use [vDSP_DFT_ExecuteD](https://developer.apple.com/documentation/accelerate/1449812-vdsp_dft_executed) to execute the transform, passing double-precision data vectors (type `double[]`) in `Ir`, `Ii`, `Or` and `Oi` parameters.

