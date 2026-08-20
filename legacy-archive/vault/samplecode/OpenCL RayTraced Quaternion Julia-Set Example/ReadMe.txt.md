---
title: OpenCL RayTraced Quaternion Julia-Set Example
apple_id: DTS40008190
resource_type: Sample Code
platform: macOS
topic: Performance
technology: OpenCL
published: '2011-10-03'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_RayTraced_Quaternion_Julia-Set_Example/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:17:57.818699Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL RayTraced Quaternion Julia-Set Example](OpenCL%20RayTraced%20Quaternion%20Julia-Set%20Example.md)


[Next](qjulia.c.md)[Previous](OpenCL%20RayTraced%20Quaternion%20Julia-Set%20Example.md)

# ReadMe.txt

```
### OpenCL RayTraced Quaternion Julia-Set Example ###

===========================================================================
DESCRIPTION:

This example shows how to use OpenCL to raytrace a 4d quaternion Julia-Set 
fractal and intermix the results of a compute kernel with OpenGL for rendering.

For theory and information regarding 4d quaternion julia-sets consult the following:

http://local.wasp.uwa.edu.au/~pbourke/fractals/quatjulia/
http://www.omegafield.net/library/dynamical/quaternion_julia_sets.pdf
http://www.evl.uic.edu/files/pdf/Sandin.RayTracerJuliaSetsbw.pdf
http://www.cs.caltech.edu/~keenan/project_qjulia.html

Note that the .cl compute kernel file(s) are loaded and compiled at
runtime.  The example source assumes that these files are in the same 
path as the built executable.

For simplicity, this example is intended to be run from the command line.
If run from within XCode, open the Run Log (Command-Shift-R) to see the 
output.  Alternatively, run the applications from within a Terminal.app 
session to launch from the command line.

===========================================================================
BUILD REQUIREMENTS:

Mac OS X v10.7 or later
This demo uses float3 vector datatype which is only supported 10.7 and later.

===========================================================================
RUNTIME REQUIREMENTS:

Mac OS X v10.7 or later with OpenCL 1.1

===========================================================================
PACKAGING LIST:

qjulia.c
qjulia.xcodeproj
qjulia_kernel.cl

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 1.0
- First version.

===========================================================================
Copyright (C) 2008 Apple Inc. All rights reserved.
```

[Next](qjulia.c.md)[Previous](OpenCL%20RayTraced%20Quaternion%20Julia-Set%20Example.md)

