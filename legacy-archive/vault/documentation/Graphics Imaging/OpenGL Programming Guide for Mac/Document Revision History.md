---
title: OpenGL Programming Guide for Mac
apple_id: TP40001987
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/opengl_rev_hx/opengl_rev_hx.html
archived_at: '2026-07-15T07:36:43.459587Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenGL Programming Guide for Mac](About%20OpenGL%20for%20OS%20X.md)


[Next](Glossary.md)[Previous](Setting%20Up%20Function%20Pointers%20to%20OpenGL%20Routines.md)

# Document Revision History

This table describes the changes to _OpenGL Programming Guide for Mac_.

| __Date__ | __Notes__ |
| 2018-06-04 | Updated with information on supporting high-resolution displays. |
| 2012-07-23 | Updated with information on supporting high-resolution displays. |
| 2011-06-06 | Added new context options. |
| 2010-11-15 | Fixed a few small errors in the texture chapter. |
|  | Updated the recommendations on when to use each texture uploading and downloading technique. |
|  | Updated the code for creating a texture from a view’s contents to use newer, better supported techniques. |
| 2010-06-14 | Corrected texture creation code snippets. |
| 2010-03-24 | Minor updates and clarifications. |
| 2010-02-24 | Substantial revisions to describe behaviors for OpenGL on OS X v10.5 and OS X v10.6. Removed information on obsolete and deprecated behaviors. |
| 2009-08-28 | Corrected errors in code listings. Pixel format attribute lists should be terminated with 0, not NULL. One call to glTexImage2D had an incorrect number of parameters. |
| 2008-06-09 | Updated the Cocoa OpenGL tutorial and made numerous other minor changes. |
|  | Fixed compilation errors in [Listing 8-1](Determining%20the%20OpenGL%20Capabilities%20Supported%20by%20the%20Renderer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqmrrgewvgvzs). |
|  | Added [Getting Decompressed Raw Pixel Data from a Source Image](Best%20Practices%20for%20Working%20with%20Texture%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqnbqg4wvgvztgq). |
|  | Updated links to OpenGL extensions. |
|  | Made several minor edits. |
| 2007-12-04 | Corrected minor typographical and technical errors. |
|  | Added [Ensuring That Back Buffer Contents Remain the Same](Choosing%20Renderer%20and%20Buffer%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqmrrgqwvgvzu). |
|  | Revised [Deprecated Attributes](Choosing%20Renderer%20and%20Buffer%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqmrrgqwvgvzv). |
| 2007-08-07 | Fixed several technical issues. |
| 2007-05-29 | Fixed a broken link. |
| 2007-05-17 | Fixed a few technical inaccuracies in the code listings. |
|  | Changed attribs to attributes in [Listing 6-2](Choosing%20Renderer%20and%20Buffer%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqmrrgqwvgvzs). |
|  | Fixed drawRect method implementation in [Drawing to a Window or View](Drawing%20to%20a%20Window%20or%20View.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqnbqgqwvgvzy). |
| 2006-12-20 | Fixed minor errors. |
|  | Added information concerning the Apple client storage extension. Fixed a typographical error. |
| 2006-11-07 | Added information about performance issues and processor queries. |
|  | See [Determining Whether Vertex and Fragment Processing Happens on the GPU](Working%20with%20Rendering%20Contexts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqmrrgywvgvzsgi). |
| 2006-10-03 | Added a section on checking for GPU processing. |
|  | Added [Determining Whether Vertex and Fragment Processing Happens on the GPU](Working%20with%20Rendering%20Contexts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqmrrgywvgvzsgi). |
|  | Fixed a number of minor typos in the code and in the text. |
| 2006-09-05 | Fixed minor technical problems. |
| 2006-07-24 | Made minor technical and typograhical changes throughout. |
|  | Added information to [Surface Drawing Order Specifies the Position of the OpenGL Surface Relative to the Window](Working%20with%20Rendering%20Contexts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqmrrgywvgvzsge). |
|  | Changed `glCopyTexSubImage` to `glCopyTexSubImage2D` in [Downloading Texture Data](Best%20Practices%20for%20Working%20with%20Texture%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqnbqg4wvgvzrgm). |
|  | Made minor improvements to [Listing 11-6](Best%20Practices%20for%20Working%20with%20Texture%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqnbqg4wvgvzy). |
|  | Removed information about 1-D textures. |
| 2006-06-28 | Made several minor technical corrections. |
|  | Redirected links to the [OpenGL specification for the framebuffer object extension](http://oss.sgi.com/projects/ogl-sample/registry/EXT/framebuffer_object.txt) so that they point to the SGI Open Source website, which hosts the most up-to-date version of this specification. |
|  | Removed the logic operation blending entry from [Table A-6](Legacy%20OpenGL%20Functionality%20by%20Version.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqmzqgewvgvzs) because this functionality is not available in OpenGL 2.0. |
| 2006-05-23 | First version. |
|  | This document replaces _Macintosh OpenGL Programming Guide_ and _AGL Programming Guide_. |
|  | This document incorporates information from the following Technical Notes: |
|  | TN2007 “The CGDirectDisplay API” |
|  | TN2014 “Insights on OpenGL” |
|  | TN2080 “Understanding and Detecting OpenGL Functionality” |
|  | TN2093 “OpenGL Performance Optimization: The Basics” |
|  | This document incorporates information from the following Technical Q&As: |
|  | Technical Q&A OGL01 “aglChoosePixelFormat, The Inside Scoop” |
|  | Technical Q&A OGL02 “Correct Setup of an AGLDrawable” |
|  | Technical Q&A QA1158 “glFlush() vs. glFinish()” |
|  | Technical Q&A QA1167 “Using Interface Builder's NSOpenGLView or Custom View objects for an OpenGL application” |
|  | Technical Q&A QA1188 “GetProcAdress and OpenGL Entry Points” |
|  | Technical Q&A QA1209 “Updating OpenGL Contexts” |
|  | Technical Q&A QA1248 “Context Sharing Tips” |
|  | Technical Q&A QA1268 “Sharpening Full Scene Anti-Aliasing Details” |
|  | Technical Q&A QA1269 “OS X OpenGL Interfaces” |
|  | Technical Q&A QA1325 “Creating an OpenGL texture from an NSView” |

[Next](Glossary.md)[Previous](Setting%20Up%20Function%20Pointers%20to%20OpenGL%20Routines.md)

