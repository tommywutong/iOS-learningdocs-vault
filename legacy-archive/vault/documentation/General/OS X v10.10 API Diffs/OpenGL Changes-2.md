---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/OpenGL.html
archived_at: '2026-07-15T07:34:56.341691Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# OpenGL Changes

## OpenGL (Added)

Added CGLChoosePixelFormat(UnsafePointer<CGLPixelFormatAttribute>, UnsafeMutablePointer<CGLPixelFormatObj>, UnsafeMutablePointer<GLint>) -> CGLErrorAdded CGLClearDrawable(CGLContextObj) -> CGLErrorAdded CGLContextEnableAdded CGLContextObjAdded CGLContextParameterAdded CGLCreateContext(CGLPixelFormatObj, CGLContextObj, UnsafeMutablePointer<CGLContextObj>) -> CGLErrorAdded CGLDescribePixelFormat(CGLPixelFormatObj, GLint, CGLPixelFormatAttribute, UnsafeMutablePointer<GLint>) -> CGLErrorAdded CGLDescribeRenderer(CGLRendererInfoObj, GLint, CGLRendererProperty, UnsafeMutablePointer<GLint>) -> CGLErrorAdded CGLDestroyContext(CGLContextObj) -> CGLErrorAdded CGLDestroyPixelFormat(CGLPixelFormatObj) -> CGLErrorAdded CGLDestroyRendererInfo(CGLRendererInfoObj) -> CGLErrorAdded CGLDisable(CGLContextObj, CGLContextEnable) -> CGLErrorAdded CGLEnable(CGLContextObj, CGLContextEnable) -> CGLErrorAdded CGLErrorAdded CGLErrorString(CGLError) -> UnsafePointer<Int8>Added CGLFlushDrawable(CGLContextObj) -> CGLErrorAdded CGLGPURestartStatusAdded CGLGetContextRetainCount(CGLContextObj) -> GLuintAdded CGLGetCurrentContext() -> CGLContextObjAdded CGLGetDeviceFromGLRenderer(GLint) -> cl_device_idAdded CGLGetGlobalOption(CGLGlobalOption, UnsafeMutablePointer<GLint>) -> CGLErrorAdded CGLGetOption(CGLGlobalOption, UnsafeMutablePointer<GLint>) -> CGLErrorAdded CGLGetParameter(CGLContextObj, CGLContextParameter, UnsafeMutablePointer<GLint>) -> CGLErrorAdded CGLGetPixelFormat(CGLContextObj) -> CGLPixelFormatObjAdded CGLGetPixelFormatRetainCount(CGLPixelFormatObj) -> GLuintAdded CGLGetShareGroup(CGLContextObj) -> CGLShareGroupObjAdded CGLGetVersion(UnsafeMutablePointer<GLint>, UnsafeMutablePointer<GLint>)Added CGLGetVirtualScreen(CGLContextObj, UnsafeMutablePointer<GLint>) -> CGLErrorAdded CGLGlobalOptionAdded CGLIsEnabled(CGLContextObj, CGLContextEnable, UnsafeMutablePointer<GLint>) -> CGLErrorAdded CGLLockContext(CGLContextObj) -> CGLErrorAdded CGLOpenGLProfileAdded CGLPixelFormatAttributeAdded CGLPixelFormatObjAdded CGLQueryRendererInfo(GLuint, UnsafeMutablePointer<CGLRendererInfoObj>, UnsafeMutablePointer<GLint>) -> CGLErrorAdded CGLReleaseContext(CGLContextObj)Added CGLReleasePixelFormat(CGLPixelFormatObj)Added CGLRendererInfoObjAdded CGLRendererPropertyAdded CGLRetainContext(CGLContextObj) -> CGLContextObjAdded CGLRetainPixelFormat(CGLPixelFormatObj) -> CGLPixelFormatObjAdded CGLSetCurrentContext(CGLContextObj) -> CGLErrorAdded CGLSetGlobalOption(CGLGlobalOption, UnsafePointer<GLint>) -> CGLErrorAdded CGLSetOption(CGLGlobalOption, GLint) -> CGLErrorAdded CGLSetParameter(CGLContextObj, CGLContextParameter, UnsafePointer<GLint>) -> CGLErrorAdded CGLSetVirtualScreen(CGLContextObj, GLint) -> CGLErrorAdded CGLShareGroupObjAdded CGLTexImageIOSurface2D(CGLContextObj, GLenum, GLenum, GLsizei, GLsizei, GLenum, GLenum, IOSurface!, GLuint) -> CGLErrorAdded CGLUnlockContext(CGLContextObj) -> CGLErrorAdded CGLUpdateContext(CGLContextObj) -> CGLErrorAdded CGL_VERSION_1_0Added CGL_VERSION_1_1Added CGL_VERSION_1_2Added CGL_VERSION_1_3Added GLbitfieldAdded GLbooleanAdded GLbyteAdded GLcharAdded GLcharARBAdded GLclampdAdded GLclampfAdded GLdoubleAdded GLenumAdded GLfixedAdded GLfloatAdded GLhalfAdded GLhalfARBAdded GLhandleARBAdded GLintAdded GLint64Added GLint64EXTAdded GLintptrAdded GLintptrARBAdded GLshortAdded GLsizeiAdded GLsizeiptrAdded GLsizeiptrARBAdded GLsyncAdded GLubyteAdded GLuintAdded GLuint64Added GLuint64EXTAdded GLushortAdded IOSurfaceRefAdded cl_device_idAdded kCGL0BitAdded kCGL10BitAdded kCGL128BitAdded kCGL12BitAdded kCGL16BitAdded kCGL1BitAdded kCGL24BitAdded kCGL2BitAdded kCGL32BitAdded kCGL3BitAdded kCGL48BitAdded kCGL4BitAdded kCGL5BitAdded kCGL64BitAdded kCGL6BitAdded kCGL8BitAdded kCGL96BitAdded kCGLARGB12121212BitAdded kCGLARGB1555BitAdded kCGLARGB16161616BitAdded kCGLARGB2101010BitAdded kCGLARGB4444BitAdded kCGLARGB8888BitAdded kCGLBadAddressAdded kCGLBadAllocAdded kCGLBadAttributeAdded kCGLBadCodeModuleAdded kCGLBadConnectionAdded kCGLBadContextAdded kCGLBadDisplayAdded kCGLBadDrawableAdded kCGLBadEnumerationAdded kCGLBadFullScreenAdded kCGLBadMatchAdded kCGLBadOffScreenAdded kCGLBadPixelFormatAdded kCGLBadPropertyAdded kCGLBadRendererInfoAdded kCGLBadStateAdded kCGLBadValueAdded kCGLBadWindowAdded kCGLCECrashOnRemovedFunctionsAdded kCGLCEDisplayListOptimizationAdded kCGLCEMPEngineAdded kCGLCERasterizationAdded kCGLCEStateValidationAdded kCGLCESurfaceBackingSizeAdded kCGLCESwapLimitAdded kCGLCESwapRectangleAdded kCGLCPAbortOnGPURestartStatusBlacklistedAdded kCGLCPClientStorageAdded kCGLCPCurrentRendererIDAdded kCGLCPDispatchTableSizeAdded kCGLCPGPUFragmentProcessingAdded kCGLCPGPURestartStatusAdded kCGLCPGPURestartStatusBlacklistedAdded kCGLCPGPURestartStatusCausedAdded kCGLCPGPURestartStatusNoneAdded kCGLCPGPUVertexProcessingAdded kCGLCPHasDrawableAdded kCGLCPMPSwapsInFlightAdded kCGLCPReclaimResourcesAdded kCGLCPSupportGPURestartAdded kCGLCPSupportSeparateAddressSpaceAdded kCGLCPSurfaceBackingSizeAdded kCGLCPSurfaceOpacityAdded kCGLCPSurfaceOrderAdded kCGLCPSurfaceSurfaceVolatileAdded kCGLCPSwapIntervalAdded kCGLCPSwapRectangleAdded kCGLDoubleBufferBitAdded kCGLGOClearFormatCacheAdded kCGLGOFormatCacheSizeAdded kCGLGORetainRenderersAdded kCGLGOUseBuildCacheAdded kCGLMonoscopicBitAdded kCGLMultisampleBitAdded kCGLNoErrorAdded kCGLOGLPVersion_3_2_CoreAdded kCGLOGLPVersion_GL3_CoreAdded kCGLOGLPVersion_GL4_CoreAdded kCGLOGLPVersion_LegacyAdded kCGLPFAAcceleratedAdded kCGLPFAAcceleratedComputeAdded kCGLPFAAccumSizeAdded kCGLPFAAllRenderersAdded kCGLPFAAllowOfflineRenderersAdded kCGLPFAAlphaSizeAdded kCGLPFAAuxBuffersAdded kCGLPFAAuxDepthStencilAdded kCGLPFABackingStoreAdded kCGLPFABackingVolatileAdded kCGLPFAClosestPolicyAdded kCGLPFAColorFloatAdded kCGLPFAColorSizeAdded kCGLPFADepthSizeAdded kCGLPFADisplayMaskAdded kCGLPFADoubleBufferAdded kCGLPFAMaximumPolicyAdded kCGLPFAMinimumPolicyAdded kCGLPFAMultisampleAdded kCGLPFANoRecoveryAdded kCGLPFAOpenGLProfileAdded kCGLPFARendererIDAdded kCGLPFASampleAlphaAdded kCGLPFASampleBuffersAdded kCGLPFASamplesAdded kCGLPFAStencilSizeAdded kCGLPFAStereoAdded kCGLPFASupersampleAdded kCGLPFASupportsAutomaticGraphicsSwitchingAdded kCGLPFATripleBufferAdded kCGLPFAVirtualScreenCountAdded kCGLRGB101010BitAdded kCGLRGB101010_A8BitAdded kCGLRGB121212BitAdded kCGLRGB161616BitAdded kCGLRGB444A8BitAdded kCGLRGB444BitAdded kCGLRGB555A8BitAdded kCGLRGB555BitAdded kCGLRGB565A8BitAdded kCGLRGB565BitAdded kCGLRGB888A8BitAdded kCGLRGB888BitAdded kCGLRGBA16161616BitAdded kCGLRGBAFloat128BitAdded kCGLRGBAFloat256BitAdded kCGLRGBAFloat64BitAdded kCGLRGBFloat128BitAdded kCGLRGBFloat256BitAdded kCGLRGBFloat64BitAdded kCGLRPAcceleratedAdded kCGLRPAcceleratedComputeAdded kCGLRPAccumModesAdded kCGLRPBackingStoreAdded kCGLRPBufferModesAdded kCGLRPColorModesAdded kCGLRPCompliantAdded kCGLRPDepthModesAdded kCGLRPDisplayMaskAdded kCGLRPGPUFragProcCapableAdded kCGLRPGPUVertProcCapableAdded kCGLRPMajorGLVersionAdded kCGLRPMaxAuxBuffersAdded kCGLRPMaxSampleBuffersAdded kCGLRPMaxSamplesAdded kCGLRPOffScreenAdded kCGLRPOnlineAdded kCGLRPRendererCountAdded kCGLRPRendererIDAdded kCGLRPSampleAlphaAdded kCGLRPSampleModesAdded kCGLRPStencilModesAdded kCGLRPTextureMemoryMegabytesAdded kCGLRPVideoMemoryMegabytesAdded kCGLRPWindowAdded kCGLRendererATIRadeonX2000IDAdded kCGLRendererATIRadeonX3000IDAdded kCGLRendererATIRadeonX4000IDAdded kCGLRendererAppleSWIDAdded kCGLRendererGeForce8xxxIDAdded kCGLRendererGeForceIDAdded kCGLRendererGenericFloatIDAdded kCGLRendererIDMatchingMaskAdded kCGLRendererIntelHD4000IDAdded kCGLRendererIntelHD5000IDAdded kCGLRendererIntelHDIDAdded kCGLSingleBufferBitAdded kCGLStereoscopicBitAdded kCGLSupersampleBitAdded kCGLTripleBufferBit

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
