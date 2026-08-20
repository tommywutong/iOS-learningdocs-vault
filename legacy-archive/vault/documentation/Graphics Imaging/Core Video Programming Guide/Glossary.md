---
title: Core Video Programming Guide
apple_id: TP40001536
resource_type: Guide
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QuartzCore
published: '2007-04-03'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreVideo/CVProg_Gloss/CVProg_Gloss.html
archived_at: '2026-07-15T07:35:40.006207Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Video Programming Guide](Introduction%20to%20Core%20Video%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Core%20Video%20Tasks.md)

# Glossary

- __attachment__

  A Core Foundation object associated with a video frame. This attachment, specified by a key-value pair, can hold any sort of information relevant to the frame, such as timestamp.

- __buffer pool__

  A collection of preallocated buffers that can be used over and over. Keeping a pool of buffers available requires less overhead than allocating and deallocating a buffer each time it is needed.

- __display link__

  A high-priority thread that, based on a specified hardware display, makes intelligent guesses as to how often frames must be output to synchronize with the display’s refresh rate.

- __image buffer__

  An abstract buffer type that holds Core Video images. Pixel buffers, Core Video OpenGL buffers, and OpenGL textures derive from the CVImageBuffer type.

- __OpenGL buffer__

  A buffer that holds image information in graphics card memory. In Core Video, you manipulate OpenGL buffers using the `CVOpenGLBufferRef` type, which is a wrapper around the standard OpenGL buffer type.

- __OpenGL texture__

  An immutable image that OpenGL uses to wrap onto primitives. In Core Video, you manipulate OpenGL textures using the `CVOpenGLTextureRef` type, which is a wrapper around the standard OpenGL texture type.

- __pixel buffer__

  A buffer that holds image information in main memory.

- __pool__

  See [buffer pool](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmzwfvbuqmrqgqwugskiirfekskf).

- __texture__

  See [OpenGL texture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmzwfvbuqmrqgqwugskiinfeqsse).

- __texture cache__

  A pool of OpenGL textures.

- __visual context__

  An abstract space that indicates where drawing should occur. For example, an OpenGL context specifies where OpenGL drawing should occur. A visual context is typically associated with an NSView or HIView object.

[Next](Document%20Revision%20History.md)[Previous](Core%20Video%20Tasks.md)

