---
title: OpenGL Programming Guide for Mac
apple_id: TP40001987
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/opengl_glossary/opengl_glossary.html
archived_at: '2026-07-15T07:36:35.498688Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenGL Programming Guide for Mac](About%20OpenGL%20for%20OS%20X.md)


[Previous](Document%20Revision%20History.md)

# Glossary

This glossary contains terms that are used specifically for the Apple implementation of OpenGL and a few terms that are common in graphics programming. For definitions of additional OpenGL terms, see [OpenGL Programming Guide](http://www.opengl.org/documentation/red_book/), by the Khronos OpenGL Working Group

- __aliased__

  Said of graphics whose edges appear jagged; can be remedied by performing antialiasing operations.

- __antialiasing__

  In graphics, a technique used to smooth and soften the jagged (or aliased) edges that are sometimes apparent when graphical objects such as text, line art, and images are drawn.

- __ARB__

  The Khronos OpenGL Working Group, which is the group that oversees the OpenGL specification and extensions to it.

- __attach__

  To establish a connection between two existing objects. Compare [bind](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqnjqgiwvgvzt).

- __bind__

  To create a new object and then establish a connection between that object and a rendering context. Compare [attach](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqnjqgiwvgvzrge).

- __bitmap__

  A rectangular array of bits.

- __bitplane__

  A rectangular array of pixels.

- __buffer__

  A block of memory dedicated to storing a specific kind of data, such as depth values, green color values, stencil index values, and color index values.

- __CGL (Core OpenGL) framework__

  The Apple framework for using OpenGL graphics in OS X applications that need low-level access to OpenGL.

- __clipping__

  An operation that identifies the area of drawing. Anything not in the clipping region is not drawn.

- __clip coordinates__

  The coordinate system used for view-volume clipping. Clip coordinates are applied after applying the projection matrix and prior to perspective division.

- __color lookup table__

  A table of values used to map color indexes into actual color values.

- __completeness__

  A state that indicates whether a framebuffer object meets all the requirements for drawing.

- __context__

  A set of OpenGL state variables that affect how drawing is performed for a drawable object attached to that context. Also called a _rendering context_.

- __culling__

  Eliminating parts of a scene that can't be seen by the observer.

- __current context__

  The rendering context to which OpenGL routes commands issued by your application.

- __current matrix__

  A matrix used by OpenGL to transform coordinates in one system to those of another system, such as the modelview matrix, the perspective matrix, and the texture matrix. GL shading language allows user-defined matrices.

- __depth__

  In OpenGL, refers to the _z_ coordinate and specifies how far a pixel lies from the observer.

- __depth buffer__

  A block of memory used to store a depth value for each pixel. The depth buffer is used to determine whether or not a pixel can be seen by the observer. Those that are hidden are typically removed.

- __display list__

  A list of OpenGL commands that have an associated name and that are uploaded to the GPU, preprocessed, and then executed at a later time. Display lists are often used for computing-intensive commands.

- __double buffering__

  The practice of using a front and back color buffer to achieve smooth animation. The back buffer is not displayed, but swapped with the front buffer.

- __drawable object__

  In OS X, an object allocated outside of OpenGL that can serve as an OpenGL framebuffer. A drawable object can be any of the following: a window, a view, a pixel buffer, offscreen memory, or a full-screen graphics device. See also [framebuffer object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqnjqgiwvgvzv)

- __extension__

  A feature of OpenGL that's not part of the OpenGL core API and therefore not guaranteed to be supported by every implementation of OpenGL. The naming conventions used for extensions indicate how widely accepted the extension is. The name of an extension supported only by a specific company includes an abbreviation of the company name. If more then one company adopts the extension, the extension name is changed to include `EXT` instead of a company abbreviation. If the Khronos OpenGL Working Group approves an extension, the extension name changes to include `ARB` instead of `EXT` or a company abbreviation.

- __eye coordinates__

  The coordinate system with the observer at the origin. Eye coordinates are produced by the modelview matrix and passed to the projection matrix.

- __fence__

  A token used by the `GL_APPLE_fence` extension to determine whether a given command has completed or not.

- __filtering__

  A process that modifies an image by combining pixels or texels.

- __fog__

  An effect achieved by fading colors to a background color based on the distance from the observer. Fog provides depth cues to the observer.

- __fragment__

  The color and depth values for a single pixel; can also include texture coordinate values. A fragment is the result of rasterizing primitives.

- __framebuffer__

  The collection of buffers associated with a window or a rendering context.

- __framebuffer attachable image__

  The rendering destination for a framebuffer object.

- __framebuffer object__

  An OpenGL extension that allows rendering to a destination other than the usual OpenGL buffers or destinations provided by the windowing system. A framebuffer object (FBO) contains state information for the OpenGL framebuffer and its set of images. A framebuffer object is similar to a drawable object, except that a drawable object is a window-system specific object whereas a framebuffer object is a window-agnostic object. The context that's bound to a framebuffer object can be bound to a window-system-provided drawable object for the purpose of displaying the content associated with the framebuffer object.

- __frustum__

  The region of space that is seen by the observer and that is warped by perspective division.

- __FSAA (full scene antialiasing)__

  A technique that takes multiple samples at a pixel and combines them with coverage values to arrive at a final fragment.

- __gamma correction__

  A function that changes color intensity values to correct for the nonlinear response of the eye or of a display.

- __GLU__

  Graphics library utilities.

- __GL__

  Graphics library.

- __GLUT__

  Graphics Library Utilities Toolkit, which is independent of the window system. In OS X, GLUT is implemented on top of Cocoa.

- __GLX__

  An OpenGL extension that supports using OpenGL within a window provided by the X Window system.

- __image__

  A rectangular array of pixels.

- __immediate mode__

  The practice of OpenGL executing commands at the time an application issues them. To prevent commands from being issued immediately, an application can use a [display list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqnjqgiwvgvzs).

- __interleaved data__

  Arrays of dissimilar data that are grouped together, such as vertex data and texture coordinates. Interleaving can speed data retrieval.

- __mipmaps__

  A set of texture maps, provided at various resolutions, whose purpose is to minimize artifacts that can occur when a texture is applied to a geometric primitive whose onscreen resolution doesn't match the source texture map. Mipmapping derives from the latin phrase _multum in parvo_, which means "many things in a small place."

- __modelview matrix__

  A 4 X 4 matrix used by OpenGL to transforms points, lines, polygons, and positions from object coordinates to eye coordinates.

- __mutex__

  A mutual exclusion object in a multithreaded application.

- __NURBS (nonuniform rational basis spline)__

  A methodology use to specify parametric curves and surfaces.

- __packing__

  Converting pixel color components from a buffer into the format needed by an application.

- __pbuffer__

  See [pixel buffer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqnjqgiwvgvzu).

- __pixel__

  A picture element; the smallest element that the graphics hardware can display on the screen. A pixel is made up of all the bits at the location _x_, _y_, in all the bitplanes in the framebuffer.

- __pixel buffer__

  A type of drawable object that allows the use of offscreen buffers as sources for OpenGL texturing. Pixel buffers allow hardware-accelerated rendering to a texture.

- __pixel depth__

  The number of bits per pixel in a pixel image.

- __pixel format__

  A format used to store pixel data in memory. The format describes the pixel components (that is, red, blue, green, alpha), the number and order of components, and other relevant information, such as whether a pixel contains stencil and depth values.

- __primitives__

  The simplest elements in OpenGL—points, lines, polygons, bitmaps, and images.

- __projection matrix__

  A matrix that OpenGL uses to transform points, lines, polygons, and positions from eye coordinates to clip coordinates.

- __rasterization__

  The process of converting vertex and pixel data to fragments, each of which corresponds to a pixel in the framebuffer.

- __renderbuffer__

  A rendering destination for a 2D pixel image, used for generalized offscreen rendering, as defined in the OpenGL specification for the `GL_EXT_framebuffer_object` extension.

- __renderer__

  A combination of hardware and software that OpenGL uses to create an image from a view and a model. The hardware portion of a renderer is associated with a particular display device and supports specific capabilities, such as the ability to support a certain color depth or buffering mode. A renderer that uses only software is called a _software renderer_ and is typically used as a fallback.

- __rendering context__

  A container for state information.

- __rendering pipeline__

  The order of operations used by OpenGL to transform pixel and vertex data to an image in the framebuffer.

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

- __surface__

  The internal representation of a single buffer that OpenGL actually draws to and reads from. For windowed drawable objects, this surface is what the OS X window server uses to composite OpenGL content on the desktop.

- __tearing__

  A visual anomaly caused when part of the current frame overwrites previous frame data in the framebuffer before the current frame is fully rendered on the screen.

- __tessellation__

  An operation that reduces a surface to a mesh of polygons, or a curve to a sequence of lines.

- __texel__

  A texture element used to specify the color to apply to a fragment.

- __texture__

  Image data used to modify the color of rasterized fragments; can be one-, two-, or three- dimensional or be a cube map.

- __texture mapping__

  The process of applying a texture to a primitive.

- __texture matrix__

  A 4 x 4 matrix that OpenGL uses to transform texture coordinates to the coordinates that are used for interpolation and texture lookup.

- __texture object__

  An opaque data structure used to store all data related to a texture. A texture object can include such things as an image, a mipmap, and texture parameters (width, height, internal format, resolution, wrapping modes, and so forth).

- __vertex__

  A three-dimensional point. A set of vertices specify the geometry of a shape. Vertices can have a number of additional attributes such as color and texture coordinates. See [vertex array](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqnjqgiwvgvzw).

- __vertex array__

  A data structure that stores a block of data that specifies such things as vertex coordinates, texture coordinates, surface normals, RGBA colors, color indices, and edge flags.

- __virtual screen__

  A combination of hardware, renderer, and pixel format that OpenGL selects as suitable for an imaging task. When the current virtual screen changes, the current renderer typically changes.

[Previous](Document%20Revision%20History.md)

