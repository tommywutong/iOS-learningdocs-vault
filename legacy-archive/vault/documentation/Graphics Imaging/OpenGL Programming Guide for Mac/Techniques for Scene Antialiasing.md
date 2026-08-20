---
title: OpenGL Programming Guide for Mac
apple_id: TP40001987
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/opengl_fsaa/opengl_fsaa.html
archived_at: '2026-07-15T07:36:34.830465Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenGL Programming Guide for Mac](About%20OpenGL%20for%20OS%20X.md)


[Next](Concurrency%20and%20OpenGL.md)[Previous](Customizing%20the%20OpenGL%20Pipeline%20with%20Shaders.md)

# Techniques for Scene Antialiasing

Aliasing is the bane of the digital domain. In the early days of the personal computer, jagged edges and blocky graphics were accepted by the user simply because not much could be done to correct them. Now with faster hardware and higher-resolution displays, there are several antialiasing techniques that can smooth edges to achieve a more realistic scene.

OpenGL supports antialiasing that operates at the level of lines and polygons as well as at the level of the full scene. This chapter discusses techniques for full scene antialiasing (FSAA). If your application needs point or line antialiasing instead of full scene antialiasing, use the built in OpenGL point and line antialiasing functions. These are described in Section 3.4.2 in the OpenGL Specification.

The three antialiasing techniques in use today are multisampling, supersampling, and alpha channel blending:

- _Multisampling_ defines a technique for sampling pixel content at multiple locations for each pixel. This is a good technique to use if you want to smooth polygon edges.
- _Supersampling_ renders at a much higher resolution than what's needed for the display. Prior to drawing the content to the display, OpenGL scales and filters the content to the appropriate resolution. This is a good technique to use when you want to smooth texture interiors in addition to polygon edges.
- _Alpha channel blending_ uses the alpha value of a fragment to control how to blend the fragment with the pixel values that are already in the framebuffer. It's a good technique to use when you want to ensure that foreground and background images are composited smoothly.

The [ARB_multisample](http://www.opengl.org/registry/specs/ARB/multisample.txt) extension defines a specification for full scene antialiasing. It describes multisampling and alpha channel sampling. The specification does not specifically mention supersampling but its wording doesn't preclude supersampling. The antialiasing methods that are available depend on the hardware and the actual implementation depends on the vendor. Some graphics cards support antialiasing using a mixture of multisampling and supersampling. The methodology used to select the samples can vary as well. Your best approach is to query the renderer to find out exactly what is supported. OpenGL lets you provide a hint to the renderer as to which antialiasing technique you prefer. Hints are available as renderer attributes that you supply when you create a pixel format object.

A smaller subset of renderers support the [EXT_framebuffer_blit](http://www.opengl.org/registry/specs/EXT/framebuffer_blit.txt) and [EXT_framebuffer_multisample](http://www.opengl.org/registry/specs/EXT/framebuffer_multisample.txt) extensions. These extensions allow your application to create multisampled offscreen frame buffer objects, render detailed scenes to them, with precise control over when the multisampled renderbuffer is resolved to a single displayable color per pixel.

Keep the following in mind when you set up full scene antialiasing:

- Although a system may have enough VRAM to accommodate a multisample buffer, a large buffer can affect the ability of OpenGL to maintain a properly working texture set. Keep in mind that the buffers associated with the rendering context—depth and stencil—increase in size by a factor equal to number of samples per pixel.
- The OpenGL driver allocates the memory needed for the multisample buffer; your application should not allocate this memory.
- Any antialiasing algorithm that operates on the full scene requires additional computing resources. There is a tradeoff between performance and quality. For that reason, you may want to provide a user interface that allows the user to enable and disable FSAA, or to choose the level of quality for antialiasing.
- The commands `glEnable(GL_MULTISAMPLE)` and `glDisable(GL_MULTISAMPLE)` are ignored on some hardware because some graphics cards have the feature enabled all the time. That doesn't mean that you should not call these commands because you'll certainly need them on hardware that doesn't ignore them.
- A hint as to the variant of sampling you want is a suggestion, not a command. Not all hardware supports all types of antialiasing. Other hardware mixes multisampling with supersampling techniques. The driver dictates the type of antialiasing that's actually used in your application.
- The best way to find out which sample modes are supported is to call the CGL function `CGLDescribeRenderer` with the renderer property `kCGLRPSampleModes` or `kCGLRPSampleAlpha`. You can also determine how many samples the renderer supports by calling `CGLDescribeRenderer` with the renderer property `kCGLRPMaxSamples`.

The general approach to setting up full scene antialiasing is as follows:

1. Check to see what's supported. Not all renderers support the ARB multisample extension, so you need to check for this functionality (see [Detecting Functionality](Determining%20the%20OpenGL%20Capabilities%20Supported%20by%20the%20Renderer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqmrrgewvgvzr)).

   To find out what type of antialiasing a specific renderer supports, call the function `CGLDescribeRenderer`. Supply the renderer property `kCGLRPSampleModes` to find out whether the renderer supports multisampling and supersampling. Supply `kCGLRPSampleAlpha` to see whether the renderer supports alpha sampling.

   You can choose to exclude unsupported hardware from the pixel format search by specifying only the hardware that supports multisample antialiasing. Keep in mind that if you exclude unsupported hardware, the unsupported displays will not render anything. If you include unsupported hardware, OpenGL uses normal aliased rendering to the unsupported displays and multisampled rendering to supported displays.
2. Include these buffer attributes in the attributes array:

   - The appropriate sample buffer attribute constant (`NSOpenGLPFASampleBuffers` or `kCGLPFASampleBuffers`) along with the number of multisample buffers. At this time the specification allows only one multisample buffer.
   - The appropriate samples constant (`NSOpenGLPFASamples` or `kCGLPFASamples`) along with the number of samples per pixel. You can supply 2, 4, 6, or more depending on what the renderer supports and the amount of VRAM available. The value that you supply affects the quality, memory use, and speed of the multisampling operation. For fastest performance, and to use the least amount of video memory, specify 2 samples. When you need more quality, specify 4 or more.
   - The no recovery attribute ( `NSOpenGLPFANoRecovery` or `kCGLPFANoRecovery`). Although enabling this attribute is not mandatory, it's recommended to prevent OpenGL from using software fallback as a renderer. Multisampled antialiasing performance is slow in the software renderer.
3. Optionally provide a hint for the type of antialiasing you want—multisampling, supersampling, or alpha sampling. See [Hinting for a Specific Antialiasing Technique](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqnbqguwvgvzt).
4. Enable multisampling with the following command:

   `glEnable(GL_MULTISAMPLE)`;

   Regardless of the enabled state, OpenGL always uses the multisample buffer if you supply the appropriate buffer attributes when you set up the pixel format object. If you haven't supplied the appropriate attributes, enabling multisampling has no effect.

   When multisampling is disabled, all coverage values are set to `1`, which gives the appearance of rendering without multisampling.

   Some graphics hardware leaves multisampling enabled all the time. However, don't rely on hardware to have multisampling enabled; use `glEnable` to programmatically turn on this feature.
5. Optionally provide hints for the rendering algorithm. You perform this optional step only if you want OpenGL to compute coverage values by a method other than uniformly weighting samples and averaging them.

   Some hardware supports a multisample filter hint through an OpenGL extension—`GL_NV_multisample_filter_hint`. This hint allows an OpenGL implementation to use an alternative method of resolving the color of multisampled pixels.

   You can specify that OpenGL uses faster or nicer rendering by calling the OpenGL function `glHint`, passing the constant `GL_MULTISAMPLE_FILTER_HINT_NV` as the target parameter and `GL_FASTEST` or `GL_NICEST` as the mode parameter. Hints allow the hardware to optimize the output if it can. There is no performance penalty or returned error for issuing a hint that's not supported.

   For more information, see the [OpenGL extension registry for NV_multisample_filter_hint](http://oss.sgi.com/projects/ogl-sample/registry/NV/multisample_filter_hint.txt).

When you set up your renderer and buffer attributes for full scene antialiasing, you can specify a hint to prefer one antialiasing technique over the others. If the underlying renderer does not have sufficient resources to support what you request, OpenGL ignores the hint. If you do not supply the appropriate buffer attributes when you create a pixel format object, then the hint does nothing. Table 13-1 lists the hinting constants available for the `NSOpenGLPixelFormat` class and CGL.

__Table 13-1__  Antialiasing hints

| Multisampling | Supersampling | Alpha blending |
| `NSOpenGLPFAMultisample` | `NSOpenGLPFASupersample` | `NSOpenGLPFASampleAlpha` |
| `kCGLPFAMultisample` | `kCGLPFASupersample` | `kCGLPFASampleAlpha` |

[Next](Concurrency%20and%20OpenGL.md)[Previous](Customizing%20the%20OpenGL%20Pipeline%20with%20Shaders.md)

