---
title: Context Sharing Tips
apple_id: DTS10002302
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2005-02-07'
source_url: https://developer.apple.com/library/archive/qa/qa1248/_index.html
archived_at: '2026-07-18T02:30:17.771140Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1248

# Context Sharing Tips

## Q:  How do I share resources between OpenGL contexts?

A: Contexts can share object resources and their associated object state by indicating a shared context at context creation time. Shared contexts will share all texture objects, vertex array objects, display lists, vertex programs, and fragment programs created before and after sharing is initiated. These objects' state are also shared but other context state is not. Not every context can be shared with every other context. Much depends on ensuring the same set of renderers support both contexts. Overall, shared contexts allow less resource duplication, set up costs and coding for the developer.

## Q:  What are the basics?

A: When OpenGL contexts are created one can designate a second context to share object resources. All sharing is peer to peer and developers can assume that shared resources are reference counted and thus will be maintained until explicitly released or when the last context sharing resources is itself released. It is helpful to think of this in the simplest terms possible and not to assume excess complication.

## Q:  What is and is not shared?

A: Context share "object resources", which include textures, vertex array objects, display lists, vertex programs and fragment programs. Object state is also shared, such as texture parameters or program environment parameters. Non-object state is not shared, such as texture target enables, or the current fragment/vertex program. Clients will need to duplicate context state changes as required while individual object setup will only need to be done one time.

## Q:  Which contexts can be shared?

A: Context sharing is limited to those contexts which have duplicate virtual screen mappings. This means pixels formats, which are set up with the exact same set of renderers, can create contexts which can be shared. There are two simple ways to achieve this goal. First, use the exact same pixel format for all contexts the client wishes to share. This guarantees the same virtual screen mapping and thus the ability to share contexts. In some cases, due to required pixel format differences it may not be simple to ensure the set of renderers is consistent. The easiest solution is to choose a single renderer for all pixel formats.

## Q:  Exactly how are contexts shared?

A: Sharing contexts is very simple. The exact form of the function calls depends on which API is in use. Examples of CGL, AGL and NSOpenGL are presented in Listing 1, Listing 2 and Listing 3, respectively..

__Listing 1__  CGL Context Setup for Sharing

```c
#include <OpenGL/OpenGL.h>

// Note: for demonstration purposes, normally one would create a CGL pixel
//format for a single full screen, see Listing 2 for an example of this
CGLPixelFormatAttribute attrib[] = {kCGLPFADoubleBuffer, 0};
CGLPixelFormatObj pixelFormat = NULL;
long numPixelFormats = 0;
CGLContextObj cglContext1 = NULL;
CGLContextObj cglContext2 = NULL;

CGLChoosePixelFormat (attribs, &pixelFormat, &numPixelFormats);
CGLCreateContext(pixelFormat, NULL, &cglContext1);

// create a second context sharing with the first
CGLCreateContext(pixelFormat, cglContext1, &cglContext2);
```


__Listing 2__  AGL Context Setup for Sharing

```c
#include <AGL/agl.h>

GLint attrib[] = {AGL_RGBA, AGL_DOUBLEBUFFER, AGL_NONE};

AGLPixelFormat aglPixFmt = aglChoosePixelFormat (NULL, 0, attrib);
AGLContext aglContext1 = aglCreateContext (aglPixFmt, NULL);

// create a second context sharing with the first
AGLContext aglContext2 = aglCreateContext (aglPixFmt, aglContext1);
```


__Listing 3__  Changes to NSOpenGLContext Setup for Sharing

```objc
#import <Cocoa/Cocoa.h>

+ (NSOpenGLPixelFormat*)defaultPixelFormat
{
  NSOpenGLPixelFormatAttribute attributes [] = {
                               NSOpenGLPFADoubleBuffer,  // double buffered
                               (NSOpenGLPixelFormatAttribute)nil };

  return [[(NSOpenGLPixelFormat *)[NSOpenGLPixelFormat alloc]
                                  initWithAttributes:attribs] autorelease];
}

- (NSOpenGLContext*)openGLContextWithShareContext:(NSOpenGLContext*)context
{ // create a context the first time through
   if (_openGLContext == NULL) {
    _openGLContext = [[NSOpenGLContext alloc]
                      initWithFormat:[[self class] defaultPixelFormat]
                      shareContext:context];
    [_openGLContext makeCurrentContext];
    [self prepareOpenGL]; // call to initialize OpenGL state here
  }
  return _openGLContext;
}

- (void)prepareOpenGL
{
  // for overriding to initialize OpenGL state,
  // occurs after context creation
}
```

Setting contexts to use a single renderer for a specific display screen is reasonably straight forward also. Since the OpenGL framework will normally provide a software fall back renderer, one should explicitly prevent this by specifying no recovery in the pixel format attributes if not already specifying full screen (since full screen implies no recovery). Listing 4, Listing 5 and Listing 6 show examples of how to set up pixel formats that are single display only.

__Listing 4__  CGL Single Screen Pixel Format

```c
#include <OpenGL/OpenGL.h>

// a full screen single drawable set of pixel attributes
CGLPixelFormatAttribute attribs[] = { kCGLPFADisplayMask, 0,
                                      kCGLPFAFullScreen,
                                      kCGLPFADoubleBuffer,
                                      0 };
CGLPixelFormatObj pixelFormat = NULL;
long numPixelFormats = 0;
CGLContextObj cglContext = NULL;

// fill in display mask attrib for selected display
CGDirectDisplayID display = CGMainDisplayID ();
attribs[1] = CGDisplayIDToOpenGLDisplayMask (display);
CGLChoosePixelFormat (attribs, &pixelFormat, &numPixelFormats);
```


__Listing 5__  AGL Single Screen Pixel Format

```c
#include <AGL/agl.h>

GLint attrib[] = {AGL_RGBA, GL_DOUBLEBUFFER, AGL_NO_RECOVERY, AGL_NONE};

GDHandle display = GetMainDevice ();
AGLPixelFormat aglPixFmt = aglChoosePixelFormat (&display, 1, attrib);
```


__Listing 6__  NSOpenGL Single Screen Pixel Format

```objc
#import <Cocoa/Cocoa.h>

+ (NSOpenGLPixelFormat*)defaultPixelFormat
{
  NSOpenGLPixelFormatAttribute attributes [] = {
                               NSOpenGLPFAScreenMask,
                               0,
                               NSOpenGLPFANoRecovery,
                               NSOpenGLPFADoubleBuffer,  // double buffered
                               (NSOpenGLPixelFormatAttribute)nil };

// fill in display mask attrib for selected display
CGDirectDisplayID display = CGMainDisplayID ();
attributes[1] = (NSOpenGLPixelFormatAttribute)
                                  CGDisplayIDToOpenGLDisplayMask (display);
return [[(NSOpenGLPixelFormat *)[NSOpenGLPixelFormat alloc]
                                  initWithAttributes:attribs] autorelease];
}
```

## Q:  Any additional notes?

A: If your pixel format is specified to support a single display, thus a single renderer, understand that dragging a windowed drawable to another screen or attaching a full screen context to another display will likely result in failed rendering or rendering on the specified renderer with a copy across to the newly resident display. Neither of which are likely desirable. Developers should code defensively to detect and handle renderer changes.

## Q:  How about windowed drawables with full screen pixel formats?

A: To further simplify the sharing of windowed and full screen contexts, the ability to use full screen pixel formats to create windowed drawables has been added to Mac OS X v10.3 Panther. This means a client can create one pixel format with full screen specified and use it to support both windowed and full screen contexts. However, the requirements for a full screen pixel format to explicitly support a single display and for shared pixel formats to support the exact same screen configuration have not been relaxed and must still be satisfied.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-02-07 | Updated and reformatted text. Changed information in the last paragraph according to radr://problem/3968679 |
| 2003-06-24 | New document that how to correctly share OpenGL contexts and what the limits on this sharing are. |

