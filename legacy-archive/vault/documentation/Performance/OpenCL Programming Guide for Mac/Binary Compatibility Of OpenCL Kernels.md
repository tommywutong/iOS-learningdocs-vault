---
title: OpenCL Programming Guide for Mac
apple_id: TP40008312
resource_type: Guide
platform: macOS
topic: Performance
technology: OpenCL
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/OpenCL_MacProgGuide/BinaryCompatibilityOfOpenCLKernels/BinaryCompatibilityOfOpenCLKernels.html
archived_at: '2026-07-18T01:48:58.417362Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenCL Programming Guide for Mac](About%20OpenCL%20for%20OS%20X.md)


[Next](Document%20Revision%20History.md)[Previous](Improving%20Performance%20On%20the%20CPU.md)

# Binary Compatibility Of OpenCL Kernels

Like other frameworks, OpenCL guarantees backwards binary compatibility for API calls. OpenCL, however, does not guarantee that OpenCL kernel binaries (binaries obtained by calling the `clGetProgramInfo(CL_PROGRAM_BINARIES)` function) will continue to work on future OpenCL revisions. In fact, these binaries are likely to break frequently, possibly with each new OpenCL minor and major release.

If you plan to get kernel binaries with `clGetProgramInfo(CL_PROGRAM_BINARIES)` and save them to disk or other long term storage device for later reuse, you must handle the possibility that the `clBuildProgram` function will fail with error `CL_INVALID_BINARY` when you try to reuse the saved binary later. If this happens, your application should:

1. Create a new OpenCL program by calling the `clCreateProgramWithSource` function, passing the OpenCL C source code in the `strings` parameter.
2. Recompile the program using the `clBuildProgram` function.
3. Extract the new binary using `clGetProgramInfo(CL_PROGRAM_BINARIES)` and replace the old one on disk.

Binary OpenCL kernel images saved to disk may also fail to build for the current machine if the image was created by another machine and saved to a network volume, if the user installs new hardware such as an additional GPU or replaces existing hardware, or changes some hardware settings (for example, turns on and off the discrete graphics card on MacBook Pro with both discrete and integrated GPUs).

The best way to avoid shipping binary OpenCL code is to use the offline OpenCL compiler to produce LLVM bitcode.

To generate LLVM IR (on OS X v10.8), compile a bitcode file for each of the architectures available: i368 32b, x86_64 bit, and 32b GPU. For each architecture, call the openclc compiler:

```
/System/Library/Frameworks/OpenCL.framework/Libraries/openclc -Os -arch i386 -emit-llvm-bc clFileName -o outputFileName
/System/Library/Frameworks/OpenCL.framework/Libraries/openclc -Os -arch x86_64 -emit-llvm-bc clFileName -o outputFileName
/System/Library/Frameworks/OpenCL.framework/Libraries/openclc -Os -arch gpu_32 -emit-llvm-bc clFileName -o outputFileName
```

The output file will be an LLVM bit-code object file, which can be used with the `clCreateProgramWithBinary` function.

[Next](Document%20Revision%20History.md)[Previous](Improving%20Performance%20On%20the%20CPU.md)

