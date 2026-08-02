---
title: DeferredShading
apple_id: DTS40010088
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2015-07-08'
source_url: https://developer.apple.com/library/archive/samplecode/DeferredShading/Listings/Readme_md.html
archived_at: '2026-07-18T03:06:11.569477Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DeferredShading](DeferredShading.md)


[Next](deferredLighting.fs.md)[Previous](GeoUtils.h.md)

# Readme.md

```
# DeferredShading #

This sample provides an example of deferred shading. It stores lighting attributes to various geometry buffers for performing lighting calculations in screen space.

### BACKGROUND ###

This example demonstrates deferred shading. In deferred shading, no shading is performed in the first pass of the vertex and pixel shaders. Shading is deferred until a second pass. On the first pass, information needed for shading (position, normal, depth, albedo) are rendered into the geometry buffer (G-buffer) as a series of textures. After this, a pixel shader computes the direct and indirect lighting at each pixel using the information of the texture buffers in screen space.

### USAGE ###

Press <1> to show the final image;  
Press <2> to show the position buffer;  
Press <3> to show the albedo buffer;  
Press <4> to show the normal buffer;  

Press <space> to toggle the model animation.


REQUIREMENTS
----------------------------------

### BUILD ###
OS X 10.10 SDK or later

### RUNTIME ###
OS X 10.8 or later


CHANGES FROM PREVIOUS VERSIONS:
----------------------------------

+ Version 2.0 
  - Updated to use OpenGL Core Profile
  - Updated to 10.10 SDK.

+ Version 1.1 
  - Moved shader setup to -prepareOpenGL to ensure that the OpenGL framebuffer is currently valid and thus avoid validation failure. . 
  - Replaced the NSTimer with a CVDisplayLink to drive the rendering loop.  
  - Added comments and cleaned up code.

+ Version 1.0 
  - First release


================================================================================
Copyright (C) 2008-2015 Apple Inc. All rights reserved.
```

[Next](deferredLighting.fs.md)[Previous](GeoUtils.h.md)

