---
title: OpenGL ES Programming Guide
apple_id: TP40008793
resource_type: Guide
platform: tvOS|iOS
topic: Graphics & Animation
technology: OpenGLES
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/3DDrawing/Conceptual/OpenGLES_ProgrammingGuide/Glossary/Glossary.html
archived_at: '2026-07-15T04:56:18.212944Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenGL ES Programming Guide](About%20OpenGL%20ES.md)


[Previous](Document%20Revision%20History.md)

# Glossary

This glossary contains terms that are used specifically for the Apple implementation of OpenGL ES as well as terms that are common in OpenGL ES graphics programming.

- __aliased__

  Said of graphics whose edges appear jagged; can be remedied by performing antialiasing operations.

- __antialiasing__

  In graphics, a technique used to smooth and soften the jagged (or aliased) edges that are sometimes apparent when graphical objects such as text, line art, and images are drawn.

- __attach__

  To establish a connection between two existing objects. Compare [bind](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doojtfvbuqnjqgiwvgvzv).

- __bind__

  To create a new object and then establish a connection between that object and a rendering context. Compare [attach](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doojtfvbuqnjqgiwvgvzu).

- __bitmap__

  A rectangular array of bits.

- __buffer__

  A block of memory managed by OpenGL ES dedicated to storing a specific kind of data, such as vertex attributes, color data or indices.

- __clipping__

  An operation that identifies the area of drawing. Anything not in the clipping region is not drawn.

- __clip coordinates__

  The coordinate system used for view-volume clipping. Clip coordinates are applied after applying the projection matrix and prior to perspective division.

- __completeness__

  A state that indicates whether a framebuffer object meets all the requirements for drawing.

- __context__

  A set of OpenGL ES state variables that affect how drawing is performed to a drawable object attached to that context. Also called a _rendering context_.

- __culling__

  Eliminating parts of a scene that can’t be seen by the observer.

- __current context__

  The rendering context to which OpenGL ES routes commands issued by your app.

- __current matrix__

  A matrix used by OpenGL ES 1.1 to transform coordinates in one system to those of another system, such as the modelview matrix, the perspective matrix, and the texture matrix. GLSL ES uses user-defined matrices instead.

- __depth__

  In OpenGL, the _z_ coordinate that specifies how far a pixel lies from the observer.

- __depth buffer__

  A block of memory used to store a depth value for each pixel. The depth buffer is used to determine whether or not a pixel can be seen by the observer. All fragments rasterized by OpenGL ES must pass a depth test that compares the incoming depth value to the value stored in the depth buffer; only fragments that pass the depth test are stored to framebuffer.

- __double buffering__

  The practice of using two buffers to avoid resource conflicts between two different parts of the graphic subsystem. The front buffer is used by one participant and the back buffer is modified by the other. When a swap occurs, the front and back buffer change places.

- __drawable object__

  An object allocated outside of OpenGL ES that can be used as part of an OpenGL ES framebuffer object. On iOS, the only type of drawable object is the [CAEAGLLayer](https://developer.apple.com/documentation/quartzcore/caeagllayer) class that integrates OpenGL ES rendering into Core Animation.

- __extension__

  A feature of OpenGL ES that’s not part of the OpenGL ES core API and therefore not guaranteed to be supported by every implementation of OpenGL ES. The naming conventions used for extensions indicate how widely accepted the extension is. The name of an extension supported only by a specific company includes an abbreviation of the company name. If more then one company adopts the extension, the extension name is changed to include `EXT` instead of a company abbreviation. If the Khronos OpenGL Working Group approves an extension, the extension name changes to include `OES` instead of `EXT` or a company abbreviation.

- __eye coordinates__

  The coordinate system with the observer at the origin. Eye coordinates are produced by the modelview matrix and passed to the projection matrix.

- __filtering__

  A process that modifies an image by combining pixels or texels.

- __fog__

  An effect achieved by fading colors to a background color based on the distance from the observer. Fog provides depth cues to the observer.

- __fragment__

  The color and depth values calculated when rasterizing a primitive. Each fragment must past a series of tests before being blended with the pixel stored in the framebuffer.

- __system framebuffer__

  A framebuffer provided by an operating system. This type of framebuffer supports integrating OpenGL ES into an operating system’s windowing system. iOS does not use system framebuffers. Instead, it provides framebuffer objects that are associated with a Core Animation layer.

- __framebuffer attachable image__

  The rendering destination for a framebuffer object.

- __framebuffer object__

  A framebuffer that is managed entirely by OpenGL ES. A framebuffer object contains state information for an OpenGL ES framebuffer and its set of images, called _renderbuffers_. Framebuffers are built into OpenGL ES 2.0 and later, and all iOS implementations of OpenGL ES 1.1 are guaranteed to support framebuffer objects (through the `OES_framebuffer_object` extension).

- __frustum__

  The region of space that is seen by the observer and that is warped by perspective division.

- __image__

  A rectangular array of pixels.

- __interleaved data__

  Arrays of dissimilar data that are grouped together, such as vertex data and texture coordinates. Interleaving can speed data retrieval.

- __mipmaps__

  A set of texture maps, provided at various resolutions, whose purpose is to minimize artifacts that can occur when a texture is applied to a geometric primitive whose onscreen resolution doesn’t match the source texture map. Mipmapping derives from the latin phrase _multum in parvo_, which means “many things in a small place.”

- __modelview matrix__

  A 4 x 4 matrix used by OpenGL to transform points, lines, polygons, and positions from object coordinates to eye coordinates.

- __multisampling__

  A technique that takes multiple samples at a pixel and combines them with coverage values to arrive at a final fragment.

- __mutex__

  A mutual exclusion object in a multithreaded app.

- __packing__

  Converting pixel color components from a buffer into the format needed by an app.

- __pixel__

  A picture element—the smallest element that the graphics hardware can display on the screen. A pixel is made up of all the bits at the location _x_, _y_, in all the bitplanes in the framebuffer.

- __pixel depth__

  In a pixel image, the number of bits per pixel.

- __pixel format__

  A format used to store pixel data in memory. The format describes the pixel components (red, green, blue, alpha), the number and order of components, and other relevant information, such as whether a pixel contains stencil and depth values.

- __premultiplied alpha__

  A pixel whose other components have been multiplied by the alpha value. For example, a pixel whose RGBA values start as (1.0, 0.5, 0.0, 0.5) would, when premultiplied, be (0.5, 0.25, 0.0, 0.5).

- __primitives__

  The simplest elements in OpenGL—points, lines, polygons, bitmaps, and images.

- __projection matrix__

  A matrix that OpenGL uses to transform points, lines, polygons, and positions from eye coordinates to clip coordinates.

- __rasterization__

  The process of converting vertex and pixel data to fragments, each of which corresponds to a pixel in the framebuffer.

- __renderbuffer__

  A rendering destination for a 2D pixel image, used for generalized offscreen rendering, as defined in the OpenGL specification for the `OES_framebuffer_object` extension.

- __renderer__

  A combination of hardware and software that OpenGL ES uses to create an image from a view and a model.

- __rendering context__

  A container for state information.

- __rendering pipeline__

  The order of operations used by OpenGL ES to transform pixel and vertex data to an image in the framebuffer.

- __render-to-texture__

  An operation that draws content directly to a texture target.

- __RGBA__

  Red, green, blue, and alpha color components.

- __shader__

  A program that computes surface properties.

- __shading language__

  A high-level language, accessible in C, used to produce advanced imaging effects.

- __stencil buffer__

  Memory used specifically for stencil testing. A stencil test is typically used to identify masking regions, to identify solid geometry that needs to be capped, and to overlap translucent polygons.

- __tearing__

  A visual anomaly caused when part of the current frame overwrites previous frame data in the framebuffer before the current frame is fully rendered on the screen. iOS avoids tearing by processing all visible OpenGL ES content through Core Animation.

- __tessellation__

  An operation that reduces a surface to a mesh of polygons, or a curve to a sequence of lines.

- __texel__

  A texture element used to specify the color to apply to a fragment.

- __texture__

  Image data used to modify the color of rasterized fragments. The data can be one-, two-, or three- dimensional or it can be a cube map.

- __texture mapping__

  The process of applying a texture to a primitive.

- __texture matrix__

  A 4 x 4 matrix that OpenGL ES 1.1 uses to transform texture coordinates to the coordinates that are used for interpolation and texture lookup.

- __texture object__

  An opaque data structure used to store all data related to a texture. A texture object can include such things as an image, a mipmap, and texture parameters (width, height, internal format, resolution, wrapping modes, and so forth).

- __vertex__

  A three-dimensional point. A set of vertices specify the geometry of a shape. Vertices can have a number of additional attributes, such as color and texture coordinates. See [vertex array](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doojtfvbuqnjqgiwvgvzsgy).

- __vertex array__

  A data structure that stores a block of data that specifies such things as vertex coordinates, texture coordinates, surface normals, RGBA colors, color indices, and edge flags.

- __vertex array object__

  An OpenGL ES object that records a list of active vertex attributes, the format each attribute is stored in, and the location of the data describing vertices and attributes. Vertex array objects simplify the effort of reconfiguring the graphics pipeline.

[Previous](Document%20Revision%20History.md)

