---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/OpenGL.html
archived_at: '2026-07-18T02:52:35.535141Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# OpenGL Changes

## OpenGL

Added CGLCPContextPriorityRequest [struct]Added CGLCPContextPriorityRequest.init(_: UInt32)Added CGLCPContextPriorityRequest.valueAdded kCGLCPContextPriorityRequestAdded kCGLCPContextPriorityRequestHighAdded kCGLCPContextPriorityRequestLowAdded kCGLCPContextPriorityRequestNormalModified CGLChoosePixelFormat(UnsafePointer<CGLPixelFormatAttribute>, UnsafeMutablePointer<CGLPixelFormatObj>, UnsafeMutablePointer<GLint>) -> CGLError

|  | Declaration |
| --- | --- |
| From | ``` func CGLChoosePixelFormat(_ attribs: ConstUnsafePointer<CGLPixelFormatAttribute>, _ pix: UnsafePointer<CGLPixelFormatObj>, _ npix: UnsafePointer<GLint>) -> CGLError ``` |
| To | ``` func CGLChoosePixelFormat(_ attribs: UnsafePointer<CGLPixelFormatAttribute>, _ pix: UnsafeMutablePointer<CGLPixelFormatObj>, _ npix: UnsafeMutablePointer<GLint>) -> CGLError ``` |

Modified CGLContextObj

|  | Declaration |
| --- | --- |
| From | ``` typealias CGLContextObj = UnsafePointer<_CGLContextObject> ``` |
| To | ``` typealias CGLContextObj = UnsafeMutablePointer<_CGLContextObject> ``` |

Modified CGLCreateContext(CGLPixelFormatObj, CGLContextObj, UnsafeMutablePointer<CGLContextObj>) -> CGLError

|  | Declaration |
| --- | --- |
| From | ``` func CGLCreateContext(_ pix: CGLPixelFormatObj, _ share: CGLContextObj, _ ctx: UnsafePointer<CGLContextObj>) -> CGLError ``` |
| To | ``` func CGLCreateContext(_ pix: CGLPixelFormatObj, _ share: CGLContextObj, _ ctx: UnsafeMutablePointer<CGLContextObj>) -> CGLError ``` |

Modified CGLDescribePixelFormat(CGLPixelFormatObj, GLint, CGLPixelFormatAttribute, UnsafeMutablePointer<GLint>) -> CGLError

|  | Declaration |
| --- | --- |
| From | ``` func CGLDescribePixelFormat(_ pix: CGLPixelFormatObj, _ pix_num: GLint, _ attrib: CGLPixelFormatAttribute, _ value: UnsafePointer<GLint>) -> CGLError ``` |
| To | ``` func CGLDescribePixelFormat(_ pix: CGLPixelFormatObj, _ pix_num: GLint, _ attrib: CGLPixelFormatAttribute, _ value: UnsafeMutablePointer<GLint>) -> CGLError ``` |

Modified CGLDescribeRenderer(CGLRendererInfoObj, GLint, CGLRendererProperty, UnsafeMutablePointer<GLint>) -> CGLError

|  | Declaration |
| --- | --- |
| From | ``` func CGLDescribeRenderer(_ rend: CGLRendererInfoObj, _ rend_num: GLint, _ prop: CGLRendererProperty, _ value: UnsafePointer<GLint>) -> CGLError ``` |
| To | ``` func CGLDescribeRenderer(_ rend: CGLRendererInfoObj, _ rend_num: GLint, _ prop: CGLRendererProperty, _ value: UnsafeMutablePointer<GLint>) -> CGLError ``` |

Modified CGLErrorString(CGLError) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func CGLErrorString(_ error: CGLError) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func CGLErrorString(_ error: CGLError) -> UnsafePointer<Int8> ``` |

Modified CGLGetContextRetainCount(CGLContextObj) -> GLuint

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGLGetGlobalOption(CGLGlobalOption, UnsafeMutablePointer<GLint>) -> CGLError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGLGetGlobalOption(_ pname: CGLGlobalOption, _ params: UnsafePointer<GLint>) -> CGLError ``` | OS X 10.10 |
| To | ``` func CGLGetGlobalOption(_ pname: CGLGlobalOption, _ params: UnsafeMutablePointer<GLint>) -> CGLError ``` | OS X 10.6 |

Modified CGLGetOption(CGLGlobalOption, UnsafeMutablePointer<GLint>) -> CGLError

|  | Declaration |
| --- | --- |
| From | ``` func CGLGetOption(_ pname: CGLGlobalOption, _ param: UnsafePointer<GLint>) -> CGLError ``` |
| To | ``` func CGLGetOption(_ pname: CGLGlobalOption, _ param: UnsafeMutablePointer<GLint>) -> CGLError ``` |

Modified CGLGetParameter(CGLContextObj, CGLContextParameter, UnsafeMutablePointer<GLint>) -> CGLError

|  | Declaration |
| --- | --- |
| From | ``` func CGLGetParameter(_ ctx: CGLContextObj, _ pname: CGLContextParameter, _ params: UnsafePointer<GLint>) -> CGLError ``` |
| To | ``` func CGLGetParameter(_ ctx: CGLContextObj, _ pname: CGLContextParameter, _ params: UnsafeMutablePointer<GLint>) -> CGLError ``` |

Modified CGLGetPixelFormat(CGLContextObj) -> CGLPixelFormatObj

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGLGetPixelFormatRetainCount(CGLPixelFormatObj) -> GLuint

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGLGetShareGroup(CGLContextObj) -> CGLShareGroupObj

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CGLGetVersion(UnsafeMutablePointer<GLint>, UnsafeMutablePointer<GLint>)

|  | Declaration |
| --- | --- |
| From | ``` func CGLGetVersion(_ majorvers: UnsafePointer<GLint>, _ minorvers: UnsafePointer<GLint>) ``` |
| To | ``` func CGLGetVersion(_ majorvers: UnsafeMutablePointer<GLint>, _ minorvers: UnsafeMutablePointer<GLint>) ``` |

Modified CGLGetVirtualScreen(CGLContextObj, UnsafeMutablePointer<GLint>) -> CGLError

|  | Declaration |
| --- | --- |
| From | ``` func CGLGetVirtualScreen(_ ctx: CGLContextObj, _ screen: UnsafePointer<GLint>) -> CGLError ``` |
| To | ``` func CGLGetVirtualScreen(_ ctx: CGLContextObj, _ screen: UnsafeMutablePointer<GLint>) -> CGLError ``` |

Modified CGLIsEnabled(CGLContextObj, CGLContextEnable, UnsafeMutablePointer<GLint>) -> CGLError

|  | Declaration |
| --- | --- |
| From | ``` func CGLIsEnabled(_ ctx: CGLContextObj, _ pname: CGLContextEnable, _ enable: UnsafePointer<GLint>) -> CGLError ``` |
| To | ``` func CGLIsEnabled(_ ctx: CGLContextObj, _ pname: CGLContextEnable, _ enable: UnsafeMutablePointer<GLint>) -> CGLError ``` |

Modified CGLLockContext(CGLContextObj) -> CGLError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGLOpenGLProfile

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CGLQueryRendererInfo(GLuint, UnsafeMutablePointer<CGLRendererInfoObj>, UnsafeMutablePointer<GLint>) -> CGLError

|  | Declaration |
| --- | --- |
| From | ``` func CGLQueryRendererInfo(_ display_mask: GLuint, _ rend: UnsafePointer<CGLRendererInfoObj>, _ nrend: UnsafePointer<GLint>) -> CGLError ``` |
| To | ``` func CGLQueryRendererInfo(_ display_mask: GLuint, _ rend: UnsafeMutablePointer<CGLRendererInfoObj>, _ nrend: UnsafeMutablePointer<GLint>) -> CGLError ``` |

Modified CGLReleaseContext(CGLContextObj)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGLReleasePixelFormat(CGLPixelFormatObj)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGLRetainContext(CGLContextObj) -> CGLContextObj

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGLRetainPixelFormat(CGLPixelFormatObj) -> CGLPixelFormatObj

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGLSetGlobalOption(CGLGlobalOption, UnsafePointer<GLint>) -> CGLError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGLSetGlobalOption(_ pname: CGLGlobalOption, _ params: ConstUnsafePointer<GLint>) -> CGLError ``` | OS X 10.10 |
| To | ``` func CGLSetGlobalOption(_ pname: CGLGlobalOption, _ params: UnsafePointer<GLint>) -> CGLError ``` | OS X 10.6 |

Modified CGLSetParameter(CGLContextObj, CGLContextParameter, UnsafePointer<GLint>) -> CGLError

|  | Declaration |
| --- | --- |
| From | ``` func CGLSetParameter(_ ctx: CGLContextObj, _ pname: CGLContextParameter, _ params: ConstUnsafePointer<GLint>) -> CGLError ``` |
| To | ``` func CGLSetParameter(_ ctx: CGLContextObj, _ pname: CGLContextParameter, _ params: UnsafePointer<GLint>) -> CGLError ``` |

Modified CGLShareGroupObj

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CGLTexImageIOSurface2D(CGLContextObj, GLenum, GLenum, GLsizei, GLsizei, GLenum, GLenum, IOSurface!, GLuint) -> CGLError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CGLUnlockContext(CGLContextObj) -> CGLError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGLUpdateContext(CGLContextObj) -> CGLError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified GLhandleARB

|  | Declaration |
| --- | --- |
| From | ``` typealias GLhandleARB = UnsafePointer<()> ``` |
| To | ``` typealias GLhandleARB = UnsafeMutablePointer<Void> ``` |

Modified kCGLCECrashOnRemovedFunctions

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCGLCEDisplayListOptimization

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCGLCEMPEngine

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGLCESurfaceBackingSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCGLCESwapLimit

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCGLCPCurrentRendererID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGLCPDispatchTableSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCGLCPGPUFragmentProcessing

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGLCPGPUVertexProcessing

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGLCPHasDrawable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGLCPMPSwapsInFlight

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGLCPReclaimResources

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGLCPSurfaceBackingSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCGLCPSurfaceOpacity

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCGLCPSurfaceOrder

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCGLCPSurfaceSurfaceVolatile

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCGLGOUseBuildCache

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGLOGLPVersion_3_2_Core

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCGLOGLPVersion_GL3_Core

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCGLOGLPVersion_GL4_Core

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCGLOGLPVersion_Legacy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCGLPFAAcceleratedCompute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCGLPFAAllowOfflineRenderers

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGLPFAAuxDepthStencil

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCGLPFABackingVolatile

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCGLPFAColorFloat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCGLPFAMultisample

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCGLPFAOpenGLProfile

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCGLPFASampleAlpha

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCGLPFASampleBuffers

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCGLPFASamples

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCGLPFASupersample

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCGLPFASupportsAutomaticGraphicsSwitching

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGLPFATripleBuffer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCGLRPAcceleratedCompute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCGLRPGPUFragProcCapable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGLRPGPUVertProcCapable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGLRPMajorGLVersion

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCGLRPMaxSampleBuffers

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCGLRPMaxSamples

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCGLRPOnline

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGLRPSampleAlpha

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCGLRPSampleModes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCGLRPTextureMemoryMegabytes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCGLRPVideoMemoryMegabytes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCGLRendererATIRadeonX2000ID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGLRendererATIRadeonX3000ID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCGLRendererATIRadeonX4000ID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGLRendererGeForce8xxxID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGLRendererGeForceID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCGLRendererGenericFloatID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCGLRendererIntelHD4000ID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCGLRendererIntelHD5000ID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGLRendererIntelHDID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
