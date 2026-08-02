---
title: OpenCL Parallel Reduction Example
apple_id: DTS40008188
resource_type: Sample Code
platform: macOS
topic: Performance
technology: OpenCL
published: '2009-09-30'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_Parallel_Reduction_Example/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:17:51.207093Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL Parallel Reduction Example](OpenCL%20Parallel%20Reduction%20Example.md)


[Next](reduce.c.md)[Previous](OpenCL%20Parallel%20Reduction%20Example.md)

# ReadMe.txt

```
### OpenCL Parallel Reduction Example ###

===========================================================================
DESCRIPTION:

This example shows how to perform an efficient parallel reduction using OpenCL.
Reduce is a common data parallel primitive which can be used for variety
of different operations -- this example computes the global sum for a large
number of values, and includes kernels for integer and floating point vector
types.

Note that the .cl compute kernel file(s) are loaded and compiled at
runtime.  The example source assumes that these files are in the same 
path as the built executable.

For simplicity, this example is intended to be run from the command line.
If run from within XCode, open the Run Log (Command-Shift-R) to see the 
output.  Alternatively, run the applications from within a Terminal.app 
session to launch from the command line.

===========================================================================
BUILD REQUIREMENTS:

Mac OS X v10.6 or later

===========================================================================
RUNTIME REQUIREMENTS:

Mac OS X v10.6 or later

To use the GPU as a compute device, use one of the following devices:
- MacBook Pro w/NVidia GeForce 8600M 
- Mac Pro w/NVidia GeForce 8800GT

===========================================================================
PACKAGING LIST:

ReadMe.txt
reduce.c
reduce.xcodeproj
reduce_float2_kernel.cl
reduce_float4_kernel.cl
reduce_float_kernel.cl
reduce_int2_kernel.cl
reduce_int4_kernel.cl
reduce_int_kernel.cl

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 1.0
- First version.

===========================================================================
Copyright (C) 2008 Apple Inc. All rights reserved.
```

[Next](reduce.c.md)[Previous](OpenCL%20Parallel%20Reduction%20Example.md)

