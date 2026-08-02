---
title: Ensuring hardware accelerated rendering for your OpenGL application
apple_id: DTS10004199
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2007-07-18'
source_url: https://developer.apple.com/library/archive/qa/qa1502/_index.html
archived_at: '2026-07-18T02:31:39.648735Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1502

# Ensuring hardware accelerated rendering for your OpenGL application

## Q:  How do I select a hardware accelerated renderer and prevent it from falling into the software renderer?

A: The Mac OS X implementation of OpenGL allows an application to gracefully switch to a software renderer as a failure recovery system when the hardware resources are not sufficient for a given operation. While most applications will benefit from this recovery there are certain applications that might want to disable this feature.

Performance driven applications, like games, need to stay in hardware accelerated renderers to achieve and maintain an acceptable frame rate.

A simple way to select a hardware accelerated renderer without the choice of software fallback is by selecting the following pixel format attributes:

For CGL:

`kCGLPFAAccelerated` and `kCGLPFANoRecovery`

For AGL:

`AGL_ACCELERATED` and `AGL_NO_RECOVERY`

For NSOpenGL:

`NSOpenGLPFAAccelerated` and `NSOpenGLPFANoRecovery`

Using the \*`noRecovery` pixel format attribute will not prevent use of software vertex processing in such cases where the drawing request exceeds the hardware resources.

__Listing 1__  Creating a Pixel Format Object with Accelerated and NoRecovery attributes.

```
- initWithFrame:(NSRect)frameRect
{

    NSOpenGLPixelFormatAttribute attrs[] = {
          NSOpenGLPFANoRecovery,
          NSOpenGLPFAColorSize, 24,
            NSOpenGLPFADepthSize, 16,
            NSOpenGLPFADoubleBuffer,
            NSOpenGLPFAAccelerated,
            0
    };

    long rendererID;

    NSOpenGLPixelFormat* pixelFormat = [[NSOpenGLPixelFormat alloc] initWithAttributes:attrs];

    // Report the renderer ID that this pixel format binds to
    // CGLRenderers.h contains a list of known renderers and their corresponding RendererID codes.
    // Also at http://developer.apple.com/documentation/GraphicsImaging/Reference/CGL_OpenGL/

    [pixelFormat getValues:&rendererID forAttribute:NSOpenGLPFARendererID forVirtualScreen:0];

    NSLog(@"NSOpenGLView pixelFormat RendererID = %08x", (unsigned)rendererID);

    self = [super initWithFrame:frameRect pixelFormat:pixelFormat];

    return self;
}
```

The Techniques for Choosing Attributes section of the [OpenGL Programming Guide for Mac OS X](https://developer.apple.com/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/) provides additional information on this subject.

CGL provides two parameters for checking whether the system is using the GPU for processing: `kCGLCPGPUVertexProcessing` and `kCGLCPGPUFragmentProcessing`. To check vertex processing, pass the vertex constant to the [CGLGetParameter](https://developer.apple.com/documentation/GraphicsImaging/Reference/CGL_OpenGL/Reference/reference.html#//apple_ref/c/func/CGLGetParameter) function. To check fragment processing, pass the fragment constant to [CGLGetParameter](https://developer.apple.com/documentation/GraphicsImaging/Reference/CGL_OpenGL/Reference/reference.html#//apple_ref/c/func/CGLGetParameter).

__Listing 2__  Using CGL to check whether the GPU is processing vertices and fragments.

```
BOOL gpuProcessing;
GLint fragmentGPUProcessing, vertexGPUProcessing;
CGLGetParameter (CGLGetCurrentContext(), kCGLCPGPUFragmentProcessing,
                                         &fragmentGPUProcessing);
CGLGetParameter(CGLGetCurrentContext(), kCGLCPGPUVertexProcessing,
                                         &vertexGPUProcessing);
gpuProcessing = (fragmentGPUProcessing && vertexGPUProcessing) ? YES : NO;
```

The above listing will set `gpuProcessing` to `YES` for the currently bound shader if it will execute in the GPU.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-07-18 | New document that using the NoRecovery pixel format attribute and how to check whether vertex and fragment processing is executed on the GPU or CPU |

