---
title: OpenGL Programming Guide for Mac
apple_id: TP40001987
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/opengl_offscreen/opengl_offscreen.html
archived_at: '2026-07-15T07:36:35.527599Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenGL Programming Guide for Mac](About%20OpenGL%20for%20OS%20X.md)


[Next](Choosing%20Renderer%20and%20Buffer%20Attributes.md)[Previous](Drawing%20to%20the%20Full%20Screen.md)

# Drawing Offscreen

OpenGL applications may want to use OpenGL to render images without actually displaying them to the user. For example, an image processing application might render the image, then copy that image back to the application and save it to disk. Another useful strategy is to create intermediate images that are used later to render additional content. For example, your application might want to render an image and use it as a texture in a future rendering pass. For best performance, offscreen targets should be managed by OpenGL. Having OpenGL manage offscreen targets allows you to avoid copying pixel data back to your application, except when this is absolutely necessary.

OS X offers two useful options for creating offscreen rendering targets:

- __Framebuffer objects__. The OpenGL framebuffer extension allows your application to create fully supported offscreen OpenGL framebuffers. Framebuffer objects are fully supported as a cross-platform extension, so they are the preferred way to create offscreen rendering targets. See [Rendering to a Framebuffer Object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqnbqgmwvgvzx).
- __Pixel buffer drawable objects__. Pixel buffer drawable objects are an Apple-specific technology for creating an offscreen target. Each of the Apple-specific OpenGL APIs provides routines to create an offscreen hardware accelerated pixel buffer. Pixel buffers are recommended for use only when framebuffer objects are not available. See [Rendering to a Pixel Buffer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqnbqgmwvgvzt).

The OpenGL framebuffer extension (`GL_EXT_framebuffer_object`) allows applications to create offscreen rendering targets from within OpenGL. OpenGL manages the memory for these framebuffers.

A _framebuffer object_ (FBO) is similar to a drawable object, except a drawable object is a window-system-specific object, whereas a framebuffer object is a window-agnostic object that's defined in the OpenGL standard. After drawing to a framebuffer object, it is straightforward to read the pixel data to the application, or to use it as source data for other OpenGL commands.

Framebuffer objects offer a number of benefits:

- They are window-system independent, which makes porting code easier.
- They are easy to set up and save memory. There is no need to set up attributes and obtain a pixel format object.
- They are associated with a single OpenGL context, whereas each pixel buffer must be bound to a context.
- You can switch between them faster since there is no context switch as with pixel buffers. Because all commands are rendered by a single context, no additional serialization is required.
- They can share depth buffers; pixel buffers cannot.
- You can use them for 2D pixel images and texture images.

Completeness is a key concept to understanding framebuffer objects. _Completeness_ is a state that indicates whether a framebuffer object meets all the requirements for drawing. You test for this state after performing all the necessary setup work. If a framebuffer object is not complete, it cannot be used as the destination for rendering operations and as a source for read operations.

Completeness is dependent on many factors that are not possible to condense into one or two statements, but these factors are thoroughly defined in the [OpenGL specification for the framebuffer object extension](http://www.opengl.org/registry/specs/EXT/framebuffer_object.txt). The specification describes the requirements for internal formats of images attached to the framebuffer, how to determine if a format is color-, depth-, and stencil-renderable, as well as other requirements.

Prior to using framebuffer objects, read the OpenGL specification, which not only defines the framebuffer object API, but provides detailed definitions of all the terms necessary to understand their use and shows several code examples.

The remainder of this section provides an overview of how to use a framebuffer as either a texture or an image. The functions used to set up textures and images are slightly different. The API for images uses the renderbuffer terminology defined in the OpenGL specification. A _renderbuffer image_ is simply a 2D pixel image. The API for textures uses texture terminology, as you might expect. For example, one of the calls for setting up a framebuffer object for a texture is `glFramebufferTexture2DEXT`, whereas the call for setting up a framebuffer object for an image is `glFramebufferRenderbufferEXT`. You'll see how to set up a simple framebuffer object for each type of drawing, starting first with textures.

These are the basic steps needed to set up a framebuffer object for drawing a texture offscreen:

1. Make sure the framebuffer extension (`GL_EXT_framebuffer_object`) is supported on the system that your code runs on. See [Determining the OpenGL Capabilities Supported by the Renderer](Determining%20the%20OpenGL%20Capabilities%20Supported%20by%20the%20Renderer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqmrrgewvgvzx).
2. Check the renderer limits. For example, you might want to call the OpenGL function `glGetIntegerv` to check the maximum texture size (`GL_MAX_TEXTURE_SIZE`) or find out the maximum number of color buffers you can attach to the framebuffer object(`GL_MAX_COLOR_ATTACHMENTS_EXT`).
3. Generate a framebuffer object name by calling the following function:

```
void glGenFramebuffersEXT (GLsizei n, GLuint *ids);
```

   `n` is the number of framebuffer object names that you want to create.

   On return, `*ids` points to the generated names.
4. Bind the framebuffer object name to a framebuffer target by calling the following function:

```
void glBindFramebufferEXT(GLenum target, GLuint framebuffer);
```

   `target` should be the constant `GL_FRAMEBUFFER_EXT`.

   `framebuffer` is set to an unused framebuffer object name.

   On return, the framebuffer object is initialized to the state values described in the [OpenGL specification for the framebuffer object extension](http://www.opengl.org/registry/specs/EXT/framebuffer_object.txt). Each attachment point of the framebuffer is initialized to the attachment point state values described in the specification. The number of attachment points is equal to `GL_MAX_COLOR_ATTACHMENTS_EXT` plus 2 (for depth and stencil attachment points).

   Whenever a framebuffer object is bound, drawing commands are directed to it instead of being directed to the drawable associated with the rendering context.
5. Generate a texture name.

```
void glGenTextures(GLsizei n, GLuint *textures);
```

   `n` is the number of texture object names that you want to create.

   On return, `*textures` points to the generated names.
6. Bind the texture name to a texture target.

```
void glBindTexture(GLenum target, GLuint texture);
```

   `target` is the type of texture to bind.

   `texture` is the texture name you just created.
7. Set up the texture environment and parameters.
8. Define the texture by calling the appropriate OpenGL function to specify the target, level of detail, internal format, dimensions, border, pixel data format, and texture data storage.
9. Attach the texture to the framebuffer by calling the following function:

```
void glFramebufferTexture2DEXT (GLenum target, GLenum attachment,
                                 GLenum textarget, GLuint texture,
                                 GLint level);
```

   `target` must be `GL_FRAMEBUFFER_EXT`.

   `attachment` must be one of the attachment points of the framebuffer: `GL_STENCIL_ATTACHMENT_EXT`, `GL_DEPTH_ATTACHMENT_EXT`, or `GL_COLOR_ATTACHMENTn_EXT`, where `n` is a number from `0` to `GL_MAX_COLOR_ATTACHMENTS_EXT-1`.

   `textarget` is the texture target.

   `texture` is an existing texture object.

   `level` is the mipmap level of the texture image to attach to the framebuffer.
10. Check to make sure that the framebuffer is complete by calling the following function:

```
GLenum glCheckFramebufferStatusEXT(GLenum target);
```

    `target` must be the constant `GL_FRAMEBUFFER_EXT`.

    This function returns a status constant. You must test to make sure that the constant is `GL_FRAMEBUFFER_COMPLETE_EXT`. If it isn't, see the [OpenGL specification for the framebuffer object extension](http://www.opengl.org/registry/specs/EXT/framebuffer_object.txt) for a description of the other constants in the status enumeration.
11. Render content to the texture. You must make sure to bind a different texture to the framebuffer object or disable texturing before you render content. If you render to a framebuffer object texture attachment with that same texture currently bound and enabled, the result is undefined.
12. To draw the contents of the texture to a window, make the window the target of all rendering commands by calling the function `glBindFramebufferEXT` and passing the constant `GL_FRAMEBUFFER_EXT` and `0`. The window is always specified as `0`.
13. Use the texture attachment as a normal texture by binding it, enabling texturing, and drawing.
14. Delete the texture.
15. Delete the framebuffer object by calling the following function:

```
void  glDeleteFramebuffersEXT (GLsizei n, const GLuint *framebuffers);
```

    `n` is the number of framebuffer objects to delete.

    `*framebuffers` points to an array that contains the framebuffer object names.

Listing 5-1 shows code that performs these tasks. This example creates and draws to a single framebuffer object.

__Listing 5-1__  Setting up a framebuffer for texturing

```
GLuint framebuffer, texture;
GLenum status;
glGenFramebuffersEXT(1, &framebuffer);
// Set up the FBO with one texture attachment
glBindFramebufferEXT(GL_FRAMEBUFFER_EXT, framebuffer);
glGenTextures(1, &texture);
glBindTexture(GL_TEXTURE_2D, texture);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA8, TEXWIDE, TEXHIGH, 0,
                GL_RGBA, GL_UNSIGNED_BYTE, NULL);
glFramebufferTexture2DEXT(GL_FRAMEBUFFER_EXT, GL_COLOR_ATTACHMENT0_EXT,
                GL_TEXTURE_2D, texture, 0);
status = glCheckFramebufferStatusEXT(GL_FRAMEBUFFER_EXT);
if (status != GL_FRAMEBUFFER_COMPLETE_EXT)
                // Handle error here
// Your code to draw content to the FBO
// ...
// Make the window the target
glBindFramebufferEXT(GL_FRAMEBUFFER_EXT, 0);
//Your code to use the contents of the FBO
// ...
//Tear down the FBO and texture attachment
glDeleteTextures(1, &texture);
glDeleteFramebuffersEXT(1, &framebuffer);
```


There is a lot of similarity between setting up a framebuffer object for drawing images and setting one up to draw textures. These are the basic steps needed to set up a framebuffer object for drawing a 2D pixel image (a renderbuffer image) offscreen:

1. Make sure the framebuffer extension (`EXT_framebuffer_object`) is supported on the renderer that your code runs on.
2. Check the renderer limits. For example, you might want to call the OpenGL function `glGetIntegerv` to find out the maximum number of color buffers (`GL_MAX_COLOR_ATTACHMENTS_EXT`).
3. Generate a framebuffer object name by calling the function `glGenFramebuffersEXT`.
4. Bind the framebuffer object name to a framebuffer target by calling the function `glBindFramebufferEXT`.
5. Generate a renderbuffer object name by calling the following function:

```
void  glGenRenderbuffersEXT (GLsizei n, GLuint *renderbuffers );
```

   `n` is the number of renderbuffer object names to create.

   `*renderbuffers` points to storage for the generated names.
6. Bind the renderbuffer object name to a renderbuffer target by calling the following function:

```
void glBindRenderbufferEXT (GLenum target, GLuint renderbuffer);
```

   `target` must be the constant `GL_RENDERBUFFER_EXT`.

   `renderbuffer` is the renderbuffer object name generated previously.
7. Create data storage and establish the pixel format and dimensions of the renderbuffer image by calling the following function:

```
void glRenderbufferStorageEXT (GLenum target, GLenum internalformat,
                                GLsizei width, GLsizei height);
```

   `target` must be the constant `GL_RENDERBUFFER_EXT`.

   `internalformat` is the pixel format of the image. The value must be `RGB`, `RGBA`, `DEPTH_COMPONENT`, `STENCIL_INDEX`, or one of the other formats listed in the OpenGL specification.

   `width` is the width of the image, in pixels.

   `height` is the height of the image, in pixels.
8. Attach the renderbuffer to a framebuffer target by calling the function `glFramebufferRenderbufferEXT`.

```
void glFramebufferRenderbufferEXT(GLenum target, GLenum attachment,
                             GLenum renderbuffertarget, GLuint renderbuffer);
```

   `target` must be the constant `GL_FRAMEBUFFER_EXT`.

   `attachment` should be one of the attachment points of the framebuffer: `GL_STENCIL_ATTACHMENT_EXT`, `GL_DEPTH_ATTACHMENT_EXT`, or GL_`COLOR_ATTACHMENTn_EXT`, where n is a number from `0` to `GL_MAX_COLOR_ATTACHMENTS_EXT–1`.

   `renderbuffertarget` must be the constant `GL_RENDERBUFFER_EXT`.

   `renderbuffer` should be set to the name of the renderbuffer object that you want to attach to the framebuffer.
9. Check to make sure that the framebuffer is complete by calling the following function:

```
enum  glCheckFramebufferStatusEXT(GLenum target);
```

   `target` must be the constant `GL_FRAMEBUFFER_EXT`.

   This function returns a status constant. You must test to make sure that the constant is `GL_FRAMEBUFFER_COMPLETE_EXT`. If it isn't, see the [OpenGL specification for the framebuffer object extension](http://www.opengl.org/registry/specs/EXT/framebuffer_object.txt) for a description of the other constants in the status enumeration.
10. Render content to the renderbuffer.
11. To access the contents of the renderbuffer object, bind the framebuffer object and then use OpenGL functions such as `glReadPixels` or `glCopyTexImage2D`.
12. Delete the framebuffer object with its renderbuffer attachment.

Listing 5-2 shows code that sets up and draws to a single renderbuffer object. Your application can set up more than one renderbuffer object if it requires them.

__Listing 5-2__  Setting up a renderbuffer for drawing images

```
GLuint framebuffer, renderbuffer;
GLenum status;
// Set the width and height appropriately for your image
GLuint imageWidth = 1024,
       imageHeight = 1024;
//Set up a FBO with one renderbuffer attachment
glGenFramebuffersEXT(1, &framebuffer);
glBindFramebufferEXT(GL_FRAMEBUFFER_EXT, framebuffer);
glGenRenderbuffersEXT(1, &renderbuffer);
glBindRenderbufferEXT(GL_RENDERBUFFER_EXT, renderbuffer);
glRenderbufferStorageEXT(GL_RENDERBUFFER_EXT, GL_RGBA8, imageWidth, imageHeight);
glFramebufferRenderbufferEXT(GL_FRAMEBUFFER_EXT, GL_COLOR_ATTACHMENT0_EXT,
                 GL_RENDERBUFFER_EXT, renderbuffer);
status = glCheckFramebufferStatusEXT(GL_FRAMEBUFFER_EXT);
if (status != GL_FRAMEBUFFER_COMPLETE_EXT)
                // Handle errors
//Your code to draw content to the renderbuffer
// ...
//Your code to use the contents
// ...
// Make the window the target
glBindFramebufferEXT(GL_FRAMEBUFFER_EXT, 0);
// Delete the renderbuffer attachment
glDeleteRenderbuffersEXT(1, &renderbuffer);
```


The OpenGL extension string `GL_APPLE_pixel_buffer` provides hardware-accelerated offscreen rendering to a pixel buffer. A pixel buffer is typically used as a texture source. It can also be used for remote rendering.

You must create a rendering context for each pixel buffer. For example, if you want to use a pixel buffer as a texture source, you create one rendering context attached to the pixel buffer and a second context attached to a window or view.

The first step in using a pixel buffer is to create it. The Apple-specific OpenGL APIs each provide a routine for this purpose:

- The `NSOpenGLPixelBuffer` method `initWithTextureTarget:textureInternalFormat:textureMaxMipMapLevel:pixelsWide:pixelsHigh:`
- The CGL function `CGLCreatePBuffer`

Each of these routines requires that you provide a texture target, an internal format, a maximum mipmap level, and the width and height of the texture.

The texture target must be one of these OpenGL texture constants: `GL_TEXTURE_2D` for a 2D texture, `GL_TEXTURE_RECTANGLE_ARB` for a rectangular (not power-of-two) texture, or `GL_TEXTURE_CUBE_MAP` for a cube map texture.

The internal format specifies how to interpret the data for texturing operations. You can supply any of these options: `GL_RGB` (each pixel is a three-component group), `GL_RGBA` (each pixel is a four-component group), or `GL_DEPTH_COMPONENT` (each pixel is a single depth component).

The maximum mipmap level should be `0` for a pixel buffer that does not have a mipmap. The value that you supply should not exceed the actual maximum number of mipmap levels that can be represented with the given width and height.

Note that none of the routines that create a pixel buffer allocate the storage needed. The storage is allocated by the system at the time that you attach the pixel buffer to a rendering context.

After you create a pixel buffer, the general procedure for using a pixel buffer for drawing is similar to the way you set up windows and views for drawing:

1. Specify renderer and buffer attributes.
2. Obtain a pixel format object.
3. Create a rendering context and make it current.
4. Attach a pixel buffer to the context using the appropriate Apple OpenGL attachment function:

   - The `setPixelBuffer:cubeMapFace:mipMapLevel:currentVirtualScreen:` method of the `NSOpenGLContext` class instructs the receiver to render into a pixel buffer.
   - The CGL function `CGLSetPBuffer` attaches a CGL rendering context to a pixel buffer.
5. Draw, as you normally would, using OpenGL.

Pixel buffers let you perform direct texturing without incurring the cost of extra copies. After drawing to a pixel buffer, you can create a texture by following these steps:

1. Generate a texture name by calling the OpenGL function `glGenTextures`.
2. Bind the named texture to a target by calling the OpenGL function `glBindTexture`.
3. Set the texture parameters by calling OpenGL function `glTexEnvParameter`.
4. Set up the pixel buffer as the source for the texture by calling one of the following Apple OpenGL functions:

   - The `setTextureImageToPixelBuffer:colorBuffer:` method of the `NSOpenGLContext` class attaches the image data in the pixel buffer to the texture object currently bound by the receiver.
   - The CGL function `CGLTexImagePBuffer` binds the contents of a CGL pixel buffer as the data source for a texture object.

   The context that you attach to the pixel buffer is the target rendering context: the context that uses the pixel buffer as the source of the texture data. Each of these routines requires a `source` parameter, which is an OpenGL constant that specifies the source buffer to texture from. The source parameter must be a valid OpenGL buffer, such as `GL_FRONT`, `GL_BACK`, or `GL_AUX0`, and should be compatible with the buffer attributes used to create the OpenGL context associated with the pixel buffer. This means that the pixel buffer must possess the buffer in question for texturing to succeed. For example, if the buffer attribute used with the pixel buffer is only single buffered, then texturing from the `GL_BACK` buffer will fail.

   If you modify content of any pixel buffer that contains mipmap levels, you must call the appropriate Apple OpenGL function again (`setTextureImageToPixelBuffer:colorBuffer:` or `CGLTexImagePBuffer`) before drawing with the pixel buffer to ensure that the content is synchronized with OpenGL. To synchronize the content of pixel buffers without mipmaps, simply rebind to the texture object using `glBind`.
5. Draw primitives using the appropriate texture coordinates. (See "The Red book"—_OpenGL Programming Guide_—for details.)
6. Call `glFlush` to cause all drawing commands to be executed.
7. When you no longer need the texture object, call the OpenGL function `glDeleteTextures`.
8. Set the current context to `NULL` using one of the Apple OpenGL routines:

   - The `makeCurrentContext` method of the `NSOpenGLContext` class
   - The CGL function `CGLSetCurrentContext`
9. Destroy the pixel buffer by calling `CGLDestroyPBuffer`.
10. Destroy the context by calling `CGLDestroyContext`.
11. Destroy the pixel format by calling `CGLDestroyPixelFormat`.

You might find these guidelines useful when using pixel buffers for texturing:

- You cannot make OpenGL texturing calls that modify pixel buffer content (such as `glTexSubImage2D` or `glCopyTexImage2D`) with the pixel buffer as the destination. You can use texturing commands to read data from a pixel buffer, such as `glCopyTexImage2D`, with the pixel buffer texture as the source. You can also use OpenGL functions such as `glReadPixels` to read the contents of a pixel buffer directly from the pixel buffer context.
- Texturing can fail to produce the intended results without reporting an error. You must make sure that you enable the proper texture target, set a compatible filter mode, and adhere to other requirements described in the OpenGL specification.
- You are not required to set up context sharing when you texture from a pixel buffer. You can have different pixel format objects and rendering contexts for both the pixel buffer and the target drawable object, without sharing resources, and still texture using a pixel buffer in the target context.

Follow these steps to render to a pixel buffer on a remote system. The remote system does not need to have a display attached to it.

1. When you set the renderer and buffer attributes, include the remote pixel buffer attribute `kCGLPFARemotePBuffer`.
2. Log in to the remote machine using the `ssh` command to ensure security.
3. Run the application on the target system.
4. Retrieve the content.

[Next](Choosing%20Renderer%20and%20Buffer%20Attributes.md)[Previous](Drawing%20to%20the%20Full%20Screen.md)

