---
title: OpenGL Programming Guide for Mac
apple_id: TP40001987
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/opengl_general/opengl_gen_tasks.html
archived_at: '2026-07-15T07:36:35.485262Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenGL Programming Guide for Mac](About%20OpenGL%20for%20OS%20X.md)


[Next](OpenGL%20Application%20Design%20Strategies.md)[Previous](Working%20with%20Rendering%20Contexts.md)

# Determining the OpenGL Capabilities Supported by the Renderer

One of the benefits of using OpenGL is that it is extensible. An extension is typically introduced by one or more vendors and then later is accepted by the OpenGL Working Group. Some extensions are promoted from a vendor-specific extension to one shared by more than one vendor, sometimes even being incorporated into the core OpenGL API. Extensions allow OpenGL to embrace innovation, but require you to verify that the OpenGL functionality you want to use is available.

Because extensions can be introduced at the vendor level, more than one extension can provide the same basic functionality. There might also be an ARB-approved extension that has functionality similar to that of a vendor-specific extension. Your application should prefer core functionality or ARB-approved extensions over those specific to a particular vendor, when both are offered by the same renderer. This makes it easier to transparently support new renderers from other vendors.

As particular functionality becomes widely adopted, it can be moved into the core OpenGL API by the ARB. As a result, functionality that you want to use could be included as an extension, as part of the core API, or both. For example, the ability to combine texture environments is supported through the `GL_ARB_texture_env_combine` and the `GL_EXT_texture_env_combine` extensions. It's also part of the core OpenGL version 1.3 API. Although each has similar functionality, they use a different syntax. You may need to check in several places (core OpenGL API and extension strings) to determine whether a specific renderer supports functionality that you want to use.

OpenGL has two types of commands—those that are part of the core API and those that are part of an extension to OpenGL. Your application first needs to check for the version of the core OpenGL API and then check for the available extensions. Keep in mind that OpenGL functionality is available on a per-renderer basis. For example, a software renderer might not support fog effects even though fog effects are available in an OpenGL extension implemented by a hardware vendor on the same system. For this reason, it's important that you check for functionality on a per-renderer basis.

Regardless of what functionality you are checking for, the approach is the same. You need to call the OpenGL function `glGetString` twice. The first time pass the `GL_VERSION` constant. The function returns a string that specifies the version of OpenGL. The second time, pass the `GL_EXTENSIONS` constant. The function returns a pointer to an extension name string. The _extension name string_ is a space-delimited list of the OpenGL extensions that are supported by the current renderer. This string can be rather long, so do not allocate a fixed-length string for the return value of the `glGetString` function. Use a pointer and evaluate the string in place.

Pass the extension name string to the function `gluCheckExtension` along with the name of the extension you want to check for. The `gluCheckExtension` function returns a Boolean value that indicates whether or not the extension is available for the current renderer.

If an extension becomes part of the core OpenGL API, OpenGL continues to export the name strings of the promoted extensions. It also continues to support the previous versions of any extension that has been exported in earlier versions of OS X. Because extensions are not typically removed, the methodology you use today to check for a feature works in future versions of OS X.

Checking for functionality, although fairly straightforward, involves writing a large chunk of code. The best way to check for OpenGL functionality is to implement a capability-checking function that you call when your program starts up, and then any time the renderer changes. Listing 8-1 shows a code excerpt that checks for a few extensions. A detailed explanation for each line of code appears following the listing.

__Listing 8-1__  Checking for OpenGL functionality

```
GLint maxRectTextureSize;
GLint myMaxTextureUnits;
GLint myMaxTextureSize;
const GLubyte * strVersion;
const GLubyte * strExt;
float myGLVersion;
GLboolean isVAO, isTexLOD, isColorTable, isFence, isShade,
          isTextureRectangle;
strVersion = glGetString (GL_VERSION); // 1
sscanf((char *)strVersion, "%f", &myGLVersion);
strExt = glGetString (GL_EXTENSIONS); // 2
glGetIntegerv(GL_MAX_TEXTURE_UNITS, &myMaxTextureUnits); // 3
glGetIntegerv(GL_MAX_TEXTURE_SIZE, &myMaxTextureSize); // 4
isVAO =
    gluCheckExtension ((const GLubyte*)"GL_APPLE_vertex_array_object",strExt); // 5
isFence = gluCheckExtension ((const GLubyte*)"GL_APPLE_fence", strExt); // 6
isShade =
     gluCheckExtension ((const GLubyte*)"GL_ARB_shading_language_100", strExt); // 7
isColorTable =
     gluCheckExtension ((const GLubyte*)"GL_SGI_color_table", strExt) ||
             gluCheckExtension ((const GLubyte*)"GL_ARB_imaging", strExt); // 8
isTexLOD =
     gluCheckExtension ((const GLubyte*)"GL_SGIS_texture_lod", strExt) ||
                                  (myGLVersion >= 1.2); // 9
isTextureRectangle = gluCheckExtension ((const GLubyte*)
                                 "GL_EXT_texture_rectangle", strExt);
if (isTextureRectangle)
      glGetIntegerv (GL_MAX_RECTANGLE_TEXTURE_SIZE_EXT, &maxRectTextureSize);
else
     maxRectTextureSize = 0; // 10
```

Here is what the code does:

1. Gets a string that specifies the version of OpenGL.
2. Gets the extension name string.
3. Calls the OpenGL function `glGetIntegerv` to get the value of the attribute passed to it which, in this case, is the maximum number of texture units.
4. Gets the maximum texture size.
5. Checks whether vertex array objects are supported.
6. Checks for the Apple fence extension.
7. Checks for support for version 1.0 of the OpenGL shading language.
8. Checks for RGBA-format color lookup table support. In this case, the code needs to check for the vendor-specific string and for the ARB string. If either is present, the functionality is supported.
9. Checks for an extension related to the texture level of detail parameter (LOD). In this case, the code needs to check for the vendor-specific string and for the OpenGL version. If the vendor string is present or the OpenGL version is greater than or equal to 1.2, the functionality is supported.
10. Gets the OpenGL limit for rectangle textures. For some extensions, such as the rectangle texture extension, it may not be enough to check whether the functionality is supported. You may also need to check the limits. You can use `glGetIntegerv` and related functions (`glGetBooleanv`, `glGetDoublev`, `glGetFloatv`) to obtain a variety of parameter values.

You can extend this example to make a comprehensive functionality-checking routine for your application. For more details, see the `GLCheck.c` file in the _[Cocoa OpenGL](../../../samplecode/Cocoa%20OpenGL/Cocoa%20OpenGL.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinjqge)_ sample application.

The code in Listing 8-2 shows one way to query the current renderer. It uses the CGL API, which can be called from Cocoa applications. In reality, you need to iterate over all displays and all renderers for each display to get a true picture of the OpenGL functionality available on a particular system. You also need to update your functionality snapshot each time the list of displays or display configuration changes.

__Listing 8-2__  Setting up a valid rendering context to get renderer functionality information

```c
#include <OpenGL/OpenGL.h>
#include <ApplicationServices/ApplicationServices.h>
CGDirectDisplayID display = CGMainDisplayID (); // 1
CGOpenGLDisplayMask myDisplayMask =
                CGDisplayIDToOpenGLDisplayMask (display); // 2

{ // Check capabilities of display represented by display mask
    CGLPixelFormatAttribute attribs[] = {kCGLPFADisplayMask,
                             myDisplayMask,
                             0}; // 3
    CGLPixelFormatObj pixelFormat = NULL;
    GLint numPixelFormats = 0;
    CGLContextObj myCGLContext = 0;
    CGLContextObj curr_ctx = CGLGetCurrentContext (); // 4
    CGLChoosePixelFormat (attribs, &pixelFormat, &numPixelFormats); // 5
    if (pixelFormat) {
        CGLCreateContext (pixelFormat, NULL, &myCGLContext); // 6
        CGLDestroyPixelFormat (pixelFormat); // 7
        CGLSetCurrentContext (myCGLContext); // 8
        if (myCGLContext) {
            // Check for capabilities and functionality here
        }
    }
    CGLDestroyContext (myCGLContext); // 9
    CGLSetCurrentContext (curr_ctx); // 10
}
```

Here's what the code does:

1. Gets the display ID of the main display.
2. Maps a display ID to an OpenGL mask.
3. Fills a pixel format attributes array with the display mask attribute and the mask value.
4. Saves the current context so that it can be restored later.
5. Gets the pixel format object for the display. The `numPixelFormats` parameter specifies how many pixel formats are listed in the pixel format object.
6. Creates a context based on the first pixel format in the list supplied by the pixel format object. Only one renderer will be associated with this context.

   In your application, you would need to iterate through all pixel formats for this display.
7. Destroys the pixel format object when it is no longer needed.
8. Sets the current context to the newly created, single-renderer context. Now you are ready to check for the functionality supported by the current renderer. See [Listing 8-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqmrrgewvgvzs) for an example of functionality-checking code.
9. Destroys the context because it is no longer needed.
10. Restores the previously saved context as the current context, thus ensuring no intrusion upon the user.

The guidelines in this section ensure that your functionality-checking code is thorough yet efficient.

- Don't rely on what's in a header file. A function declaration in a header file does not ensure that a feature is supported by the current renderer. Neither does linking against a stub library that exports a function.
- Make sure that a renderer is attached to a valid rendering context before you check the functionality of that renderer.
- Check the API version or the extension name string for the current renderer before you issue OpenGL commands.
- Check only once per renderer. After you've determined that the current renderer supports an OpenGL command, you don't need to check for that functionality again for that renderer.
- Make sure that you are aware of whether a feature is being used as part of the Core OpenGL API or as an extension. When a feature is implemented both as part of the core OpenGL API and as an extension, it uses different constants and function names.

The OpenGL specification defines implementation-dependent values that define the limits of what an OpenGL implementation is capable of. For example, the maximum size of a texture and the number of texture units are both common implementation-dependent values that an application is expected to check. Each of these values provides a minimum value that all conforming OpenGL implementations are expected to support. If your application’s usage exceeds these minimums, it must check the limit first, and fail gracefully if the implementation cannot provide the limit desired. Your application may need to load smaller textures, disable a rendering feature, or choose a different implementation.

Although the specification provides a comprehensive list of these limitations, a few stand out in most OpenGL applications. Table 8-1 lists values that applications should test if they require more than the minimum values in the specification.

__Table 8-1__  Common OpenGL renderer limitations

| Maximum size of the texture | GL_MAX_TEXTURE_SIZE |
| Number of depth buffer planes | GL_DEPTH_BITS |
| Number of stencil buffer planes | GL_STENCIL_BITS |

The limit on the size and complexity of your shaders is a key area you need to test. All graphics hardware supports limited memory to pass attributes into the vertex and fragment shaders. Your application must either keep its usage below the minimums as defined in the specification, or it must check the shader limitations documented in Table 8-2 and choose shaders that are within those limits.

__Table 8-2__  OpenGL shader limitations

| Maximum number of vertex attributes | GL_MAX_VERTEX_ATTRIBS |
| Maximum number of uniform vertex vectors | GL_MAX_VERTEX_UNIFORM_COMPONENTS |
| Maximum number of uniform fragment vectors | GL_MAX_FRAGMENT_UNIFORM_COMPONENTS |
| Maximum number of varying vectors | GL_MAX_VARYING_FLOATS |
| Maximum number of texture units usable in a vertex shader | GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS |
| Maximum number of texture units usable in a fragment shader | GL_MAX_TEXTURE_IMAGE_UNITS |

[Next](OpenGL%20Application%20Design%20Strategies.md)[Previous](Working%20with%20Rendering%20Contexts.md)

