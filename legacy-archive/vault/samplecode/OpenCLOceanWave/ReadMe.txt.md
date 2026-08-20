---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:17:44.054199Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_OceanWave](OpenCLOceanWave.md)


[Next](main.cpp.md)[Previous](OpenCLOceanWave.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# ReadMe.txt

```

### OpenCL FFT Based Ocean Demo ###

===========================================================================
DESCRIPTION:

This sdk sample shows how to animate ocean water waves using random 
fourier spectrum and FFT.

===========================================================================
BUILD REQUIREMENTS:

Mac OS X v10.6 or later
OpenCL 1.0 compliant hardware

===========================================================================
RUNTIME REQUIREMENTS:

. Mac OS X v10.6 or later with OpenCL 1.0
. For good performance, device should support local memory. 
  FFT performance critically depend on how efficiently local shuffles 
  (matrix transposes) using local memory to reduce external DRAM bandwidth
  requirement.

===========================================================================
PACKAGING LIST:


compute_kernels.cl
main.cpp
Makefile
ocean_renderer.cpp
ocean_renderer.h
ocean_simulator.cpp
ocean_simulator.h
ocean.frag
ocean.vert
ReadMe.txt
sky.frag
sky.vert
common/aabb.h
common/buffer_object.cpp
common/buffer_object.h
common/camera.cpp
common/camera.h
common/compute_engine.cpp
common/compute_engine.h
common/compute_math.cpp
common/compute_math.h
common/compute_types.h
common/csm.cpp
common/csm.h
common/data_loader.h
common/data_loader.m
common/fbo.cpp
common/fbo.h
common/frustum.cpp
common/frustum.h
common/grid_mesh.cpp
common/grid_mesh.h
common/Makefile
common/memory_buffer.cpp
common/memory_buffer.h
common/mesh_model.cpp
common/mesh_model.h
common/mesh_renderer.cpp
common/mesh_renderer.h
common/plane.cpp
common/plane.h
common/projected_grid.cpp
common/projected_grid.h
common/projector.cpp
common/projector.h
common/pssm.cpp
common/pssm.h
common/shader.cpp
common/shader.h
common/texture.cpp
common/texture.h
common/timing.h
fft/clFFT.h
fft/fft_base_kernels.h
fft/fft_execute.cpp
fft/fft_internal.h
fft/fft_kernelstring.cpp
fft/fft_setup.cpp
fft/Makefile

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 1.0
- First version.

===========================================================================
Copyright (C) 2008-2011 Apple Inc. All rights reserved.
```

[Next](main.cpp.md)[Previous](OpenCLOceanWave.md)

