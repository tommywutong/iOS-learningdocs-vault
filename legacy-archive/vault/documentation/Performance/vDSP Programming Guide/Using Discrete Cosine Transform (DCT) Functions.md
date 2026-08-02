---
title: vDSP Programming Guide
apple_id: TP40005147
resource_type: Guide
platform: iOS|macOS
topic: Mathematical Computation
technology: Accelerate
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/vDSP_Programming_Guide/UsingDCTFunctions/UsingDCTFunctions.html
archived_at: '2026-07-18T01:50:33.722119Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [vDSP Programming Guide](Introduction.md)



# Using Discrete Cosine Transform (DCT) Functions

The vDSP API provides the [vDSP_DCT_CreateSetup](https://developer.apple.com/documentation/accelerate/1449930-vdsp_dct_createsetup) and [vDSP_DCT_Execute](https://developer.apple.com/documentation/accelerate/1450016-vdsp_dct_execute) functions. They implement DCT capabilities using the following model:

- Set up all the parameters of a DCT operation using [vDSP_DCT_CreateSetup](https://developer.apple.com/documentation/accelerate/1449930-vdsp_dct_createsetup), which creates an opaque "setup" object of type `vDSP_DFT_Setup`.
- Call [vDSP_DCT_Execute](https://developer.apple.com/documentation/accelerate/1450016-vdsp_dct_execute), passing in the setup object, to execute the DCT operation.
- When the setup object is no longer needed, call the [vDSP_DFT_DestroySetup](https://developer.apple.com/documentation/accelerate/1450791-vdsp_dft_destroysetup) function to deallocate memory that has been allocated by vDSP in connection with this setup.

For an example of DCT functions in use, see _[vDSP Examples](https://developer.apple.com/library/archive/samplecode/vDSPExamples/Introduction/Intro.html#//apple_ref/doc/uid/DTS10004300)_.

Note the integration with the DFT family of functions – single-precision DCT setups have the same type as a DFT setup, and can be shared with DFT setups; and the DestroySetup function from the DFT family is used to destroy DCT setups.

A DCT setup contains all the information needed to perform a single-precision DCT operation, except the pointers to input and output data vectors. It may include information about memory allocations made by previously created setups.

This is a preparation step to be done when a program is starting, or is starting some new phase (e.g., when a communication channel is opened). It should never be done during real-time processing. The setup routine is slow and is called only once to prepare data that can be used many times.

DCT setups can be shared with other DCT setups (as well as single-precision DFT setups). This occurs when you pass a previously created setup in the `Previous` parameter of a `CreateSetup` call that creates another setup. When setups are shared, vDSP may be able to share memory amongst them, leading to better efficiency. Sharing any setup of a group of setups that share data will result in a new setup sharing data with all of the group.

1. Use the [vDSP_DCT_CreateSetup](https://developer.apple.com/documentation/accelerate/1449930-vdsp_dct_createsetup) function.
2. Pass in any existing setup that you want the new setup to share with, or pass `NULL` to create a new setup independent of any previous setups.
3. Specify the length of the transform, i.e. the number of elements to process. Only certain lengths are implemented: they are given by

   _f_ \* 2_n_, where _f_ is 1, 3, 5, or 15 and _n_ >= 4
4. Specify the type of the transform. At present, the supported DCT types are II and III (which are mutual inverses, up to scaling) and IV (which is its own inverse). These are specified with symbol names `vDSP_DCT_II`, `vDSP_DCT_III`, and `vDSP_DCT_IV`.

Once you have created all the setups needed for a particular phase of your program, you can execute them in any desired order.

A DCT setup does its work when it is passed into the [vDSP_DCT_Execute](https://developer.apple.com/documentation/accelerate/1450016-vdsp_dct_execute) function. It fully specifies the desired transform, leaving only the data pointers to be provided to [vDSP_DCT_Execute](https://developer.apple.com/documentation/accelerate/1450016-vdsp_dct_execute). The setup can be used repeatedly as many times as desired, changing the data pointers each time.

When [vDSP_DCT_Execute](https://developer.apple.com/documentation/accelerate/1450016-vdsp_dct_execute) is called with a setup returned from [vDSP_DCT_CreateSetup](https://developer.apple.com/documentation/accelerate/1449930-vdsp_dct_createsetup), it performs one of the following calculations:

```
If Type is vDSP_DCT_II:
  For 0 <= k < N,
    Or[k] = sum(Ir[j] * cos(k * (j+1/2) * pi / N, 0 <= j < N)

If Type is vDSP_DCT_III:
  For 0 <= k < N,
    Or[k] = Ir[0]/2 + sum(Ir[j] * cos((k+1/2) * j * pi / N), 1 <= j < N)

If Type is vDSP_DCT_IV:
  For 0 <= k < N,
    Or[k] = sum(Ir[j] * cos((k+1/2) * (j+1/2) * pi / N, 0 <= j < N)
```

Where

- `N` is the length given in the setup
- `h` is the array of real numbers passed to [vDSP_DCT_Execute](https://developer.apple.com/documentation/accelerate/1450016-vdsp_dct_execute) in `Input`
- `H` is the array of real numbers stored by [vDSP_DCT_Execute](https://developer.apple.com/documentation/accelerate/1450016-vdsp_dct_execute) in the array passed to it in `Output`.

When a DCT setup is no longer needed, it should be destroyed with the [vDSP_DFT_DestroySetup](https://developer.apple.com/documentation/accelerate/1450791-vdsp_dft_destroysetup) function. This allows vDSP to release memory associated with the setup (and not needed by other setups or for other purposes).

