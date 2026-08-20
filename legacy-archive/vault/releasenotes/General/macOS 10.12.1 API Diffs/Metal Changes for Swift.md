---
title: macOS 10.12.1 API Diffs
apple_id: TP40017565
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12_1/Swift/Metal.html
archived_at: '2026-07-18T02:51:46.695017Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12.1 API Diffs](macOS%2010.12%20to%20macOS%2010.12.1%20API%20Differences.md)


# Metal Changes for Swift

### Metal

Added [MTLCommandBufferError [struct]](https://developer.apple.com/documentation/metal/mtlcommandbuffererror)Added [MTLCommandBufferError.blacklisted](https://developer.apple.com/documentation/metal/mtlcommandbuffererror/2630714-blacklisted)Added MTLCommandBufferError.init(_nsError: NSError)Added [MTLCommandBufferError.internal](https://developer.apple.com/documentation/metal/mtlcommandbuffererror/2630699-internal)Added [MTLCommandBufferError.invalidResource](https://developer.apple.com/documentation/metal/mtlcommandbuffererror/2630705-invalidresource)Added [MTLCommandBufferError.none](https://developer.apple.com/documentation/metal/mtlcommandbuffererror/2630706-none)Added [MTLCommandBufferError.notPermitted](https://developer.apple.com/documentation/metal/mtlcommandbuffererror/2630708-notpermitted)Added [MTLCommandBufferError.outOfMemory](https://developer.apple.com/documentation/metal/mtlcommandbuffererror/2630710-outofmemory)Added [MTLCommandBufferError.pageFault](https://developer.apple.com/documentation/metal/mtlcommandbuffererror/2630694-pagefault)Added [MTLCommandBufferError.timeout](https://developer.apple.com/documentation/metal/mtlcommandbuffererror/2630698-timeout)Added [MTLLibraryError [struct]](https://developer.apple.com/documentation/metal/mtllibraryerror)Added [MTLLibraryError.compileFailure](https://developer.apple.com/documentation/metal/mtllibraryerror/2630707-compilefailure)Added [MTLLibraryError.compileWarning](https://developer.apple.com/documentation/metal/mtllibraryerror/2630700-compilewarning)Added [MTLLibraryError.fileNotFound](https://developer.apple.com/documentation/metal/mtllibraryerror/2630716-filenotfound)Added [MTLLibraryError.functionNotFound](https://developer.apple.com/documentation/metal/mtllibraryerror/2630703-functionnotfound)Added MTLLibraryError.init(_nsError: NSError)Added [MTLLibraryError.internal](https://developer.apple.com/documentation/metal/mtllibraryerror/2630693-internal)Added [MTLLibraryError.unsupported](https://developer.apple.com/documentation/metal/mtllibraryerror/2630702-unsupported)Added MTLRenderPipelineError [struct]Added MTLRenderPipelineError.init(_nsError: NSError)Added MTLRenderPipelineError.internalAdded MTLRenderPipelineError.invalidInputAdded MTLRenderPipelineError.unsupportedModified [MTLCommandBuffer](https://developer.apple.com/documentation/metal/mtlcommandbuffer)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLCommandBuffer : NSObjectProtocol {     var device: MTLDevice { get }     var commandQueue: MTLCommandQueue { get }     var retainedReferences: Bool { get }     var label: String? { get set }     func enqueue()     func commit()     func addScheduledHandler(_ block: Metal.MTLCommandBufferHandler)     func present(_ drawable: MTLDrawable)     func present(_ drawable: MTLDrawable, atTime presentationTime: CFTimeInterval)     func waitUntilScheduled()     func addCompletedHandler(_ block: Metal.MTLCommandBufferHandler)     func waitUntilCompleted()     var status: MTLCommandBufferStatus { get }     var error: Error? { get }     func makeBlitCommandEncoder() -> MTLBlitCommandEncoder     func makeRenderCommandEncoder(descriptor renderPassDescriptor: MTLRenderPassDescriptor) -> MTLRenderCommandEncoder     func makeComputeCommandEncoder() -> MTLComputeCommandEncoder     func makeParallelRenderCommandEncoder(descriptor renderPassDescriptor: MTLRenderPassDescriptor) -> MTLParallelRenderCommandEncoder } ``` |
| To | ``` protocol MTLCommandBuffer : NSObjectProtocol {     var device: MTLDevice { get }     var commandQueue: MTLCommandQueue { get }     var retainedReferences: Bool { get }     var label: String? { get set }     func enqueue()     func commit()     func addScheduledHandler(_ block: @escaping Metal.MTLCommandBufferHandler)     func present(_ drawable: MTLDrawable)     func present(_ drawable: MTLDrawable, atTime presentationTime: CFTimeInterval)     func waitUntilScheduled()     func addCompletedHandler(_ block: @escaping Metal.MTLCommandBufferHandler)     func waitUntilCompleted()     var status: MTLCommandBufferStatus { get }     var error: Error? { get }     func makeBlitCommandEncoder() -> MTLBlitCommandEncoder     func makeRenderCommandEncoder(descriptor renderPassDescriptor: MTLRenderPassDescriptor) -> MTLRenderCommandEncoder     func makeComputeCommandEncoder() -> MTLComputeCommandEncoder     func makeParallelRenderCommandEncoder(descriptor renderPassDescriptor: MTLRenderPassDescriptor) -> MTLParallelRenderCommandEncoder } ``` |

Modified [MTLCommandBuffer.addCompletedHandler(_: Metal.MTLCommandBufferHandler)](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1442997-addcompletedhandler)

|  | Declaration |
| --- | --- |
| From | ``` func addCompletedHandler(_ block: Metal.MTLCommandBufferHandler) ``` |
| To | ``` func addCompletedHandler(_ block: @escaping Metal.MTLCommandBufferHandler) ``` |

Modified [MTLCommandBuffer.addScheduledHandler(_: Metal.MTLCommandBufferHandler)](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1442991-addscheduledhandler)

|  | Declaration |
| --- | --- |
| From | ``` func addScheduledHandler(_ block: Metal.MTLCommandBufferHandler) ``` |
| To | ``` func addScheduledHandler(_ block: @escaping Metal.MTLCommandBufferHandler) ``` |

Modified [MTLCommandBufferError.Code [enum]](https://developer.apple.com/documentation/metal/mtlcommandbuffererror/code)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLCommandBufferErrorDomain : UInt {     case none     case `internal`     case timeout     case pageFault     case blacklisted     case notPermitted     case outOfMemory     case invalidResource     case memoryless } ``` |
| To | ``` enum Code : UInt {         typealias _ErrorType = MTLCommandBufferError         case none         case `internal`         case timeout         case pageFault         case blacklisted         case notPermitted         case outOfMemory         case invalidResource         case memoryless     } ``` |

Modified [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLDevice : NSObjectProtocol {     var name: String? { get }     var maxThreadsPerThreadgroup: MTLSize { get }     var isLowPower: Bool { get }     var isHeadless: Bool { get }     var recommendedMaxWorkingSetSize: UInt64 { get }     var isDepth24Stencil8PixelFormatSupported: Bool { get }     func makeCommandQueue() -> MTLCommandQueue     func makeCommandQueue(maxCommandBufferCount maxCommandBufferCount: Int) -> MTLCommandQueue     func heapTextureSizeAndAlign(descriptor desc: MTLTextureDescriptor) -> MTLSizeAndAlign     func heapBufferSizeAndAlign(length length: Int, options options: MTLResourceOptions = []) -> MTLSizeAndAlign     func makeHeap(descriptor descriptor: MTLHeapDescriptor) -> MTLHeap     func makeBuffer(length length: Int, options options: MTLResourceOptions = []) -> MTLBuffer     func makeBuffer(bytes pointer: UnsafeRawPointer, length length: Int, options options: MTLResourceOptions = []) -> MTLBuffer     func makeBuffer(bytesNoCopy pointer: UnsafeMutableRawPointer, length length: Int, options options: MTLResourceOptions = [], deallocator deallocator: (@escaping (UnsafeMutableRawPointer, Int) -> Swift.Void)? = nil) -> MTLBuffer     func makeDepthStencilState(descriptor descriptor: MTLDepthStencilDescriptor) -> MTLDepthStencilState     func makeTexture(descriptor descriptor: MTLTextureDescriptor) -> MTLTexture     func makeTexture(descriptor descriptor: MTLTextureDescriptor, iosurface iosurface: IOSurfaceRef, plane plane: Int) -> MTLTexture     func makeSamplerState(descriptor descriptor: MTLSamplerDescriptor) -> MTLSamplerState     func newDefaultLibrary() -> MTLLibrary?     func makeDefaultLibrary(bundle bundle: Bundle) throws -> MTLLibrary     func makeLibrary(filepath filepath: String) throws -> MTLLibrary     func makeLibrary(data data: __DispatchData) throws -> MTLLibrary     func makeLibrary(source source: String, options options: MTLCompileOptions?) throws -> MTLLibrary     func makeLibrary(source source: String, options options: MTLCompileOptions?, completionHandler completionHandler: Metal.MTLNewLibraryCompletionHandler)     func makeRenderPipelineState(descriptor descriptor: MTLRenderPipelineDescriptor) throws -> MTLRenderPipelineState     func makeRenderPipelineState(descriptor descriptor: MTLRenderPipelineDescriptor, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedRenderPipelineReflection?>?) throws -> MTLRenderPipelineState     func makeRenderPipelineState(descriptor descriptor: MTLRenderPipelineDescriptor, completionHandler completionHandler: Metal.MTLNewRenderPipelineStateCompletionHandler)     func makeRenderPipelineState(descriptor descriptor: MTLRenderPipelineDescriptor, options options: MTLPipelineOption, completionHandler completionHandler: Metal.MTLNewRenderPipelineStateWithReflectionCompletionHandler)     func makeComputePipelineState(function computeFunction: MTLFunction) throws -> MTLComputePipelineState     func makeComputePipelineState(function computeFunction: MTLFunction, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>?) throws -> MTLComputePipelineState     func makeComputePipelineState(function computeFunction: MTLFunction, completionHandler completionHandler: Metal.MTLNewComputePipelineStateCompletionHandler)     func makeComputePipelineState(function computeFunction: MTLFunction, options options: MTLPipelineOption, completionHandler completionHandler: Metal.MTLNewComputePipelineStateWithReflectionCompletionHandler)     func makeComputePipelineState(descriptor descriptor: MTLComputePipelineDescriptor, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>?) throws -> MTLComputePipelineState     func makeComputePipelineState(descriptor descriptor: MTLComputePipelineDescriptor, options options: MTLPipelineOption, completionHandler completionHandler: Metal.MTLNewComputePipelineStateWithReflectionCompletionHandler)     func makeFence() -> MTLFence     func supportsFeatureSet(_ featureSet: MTLFeatureSet) -> Bool     func supportsTextureSampleCount(_ sampleCount: Int) -> Bool } ``` |
| To | ``` protocol MTLDevice : NSObjectProtocol {     var name: String? { get }     var maxThreadsPerThreadgroup: MTLSize { get }     var isLowPower: Bool { get }     var isHeadless: Bool { get }     var recommendedMaxWorkingSetSize: UInt64 { get }     var isDepth24Stencil8PixelFormatSupported: Bool { get }     func makeCommandQueue() -> MTLCommandQueue     func makeCommandQueue(maxCommandBufferCount maxCommandBufferCount: Int) -> MTLCommandQueue     func heapTextureSizeAndAlign(descriptor desc: MTLTextureDescriptor) -> MTLSizeAndAlign     func heapBufferSizeAndAlign(length length: Int, options options: MTLResourceOptions = []) -> MTLSizeAndAlign     func makeHeap(descriptor descriptor: MTLHeapDescriptor) -> MTLHeap     func makeBuffer(length length: Int, options options: MTLResourceOptions = []) -> MTLBuffer     func makeBuffer(bytes pointer: UnsafeRawPointer, length length: Int, options options: MTLResourceOptions = []) -> MTLBuffer     func makeBuffer(bytesNoCopy pointer: UnsafeMutableRawPointer, length length: Int, options options: MTLResourceOptions = [], deallocator deallocator: ((UnsafeMutableRawPointer, Int) -> Swift.Void)? = nil) -> MTLBuffer     func makeDepthStencilState(descriptor descriptor: MTLDepthStencilDescriptor) -> MTLDepthStencilState     func makeTexture(descriptor descriptor: MTLTextureDescriptor) -> MTLTexture     func makeTexture(descriptor descriptor: MTLTextureDescriptor, iosurface iosurface: IOSurfaceRef, plane plane: Int) -> MTLTexture     func makeSamplerState(descriptor descriptor: MTLSamplerDescriptor) -> MTLSamplerState     func newDefaultLibrary() -> MTLLibrary?     func makeDefaultLibrary(bundle bundle: Bundle) throws -> MTLLibrary     func makeLibrary(filepath filepath: String) throws -> MTLLibrary     func makeLibrary(data data: __DispatchData) throws -> MTLLibrary     func makeLibrary(source source: String, options options: MTLCompileOptions?) throws -> MTLLibrary     func makeLibrary(source source: String, options options: MTLCompileOptions?, completionHandler completionHandler: @escaping Metal.MTLNewLibraryCompletionHandler)     func makeRenderPipelineState(descriptor descriptor: MTLRenderPipelineDescriptor) throws -> MTLRenderPipelineState     func makeRenderPipelineState(descriptor descriptor: MTLRenderPipelineDescriptor, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedRenderPipelineReflection?>?) throws -> MTLRenderPipelineState     func makeRenderPipelineState(descriptor descriptor: MTLRenderPipelineDescriptor, completionHandler completionHandler: @escaping Metal.MTLNewRenderPipelineStateCompletionHandler)     func makeRenderPipelineState(descriptor descriptor: MTLRenderPipelineDescriptor, options options: MTLPipelineOption, completionHandler completionHandler: @escaping Metal.MTLNewRenderPipelineStateWithReflectionCompletionHandler)     func makeComputePipelineState(function computeFunction: MTLFunction) throws -> MTLComputePipelineState     func makeComputePipelineState(function computeFunction: MTLFunction, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>?) throws -> MTLComputePipelineState     func makeComputePipelineState(function computeFunction: MTLFunction, completionHandler completionHandler: @escaping Metal.MTLNewComputePipelineStateCompletionHandler)     func makeComputePipelineState(function computeFunction: MTLFunction, options options: MTLPipelineOption, completionHandler completionHandler: @escaping Metal.MTLNewComputePipelineStateWithReflectionCompletionHandler)     func makeComputePipelineState(descriptor descriptor: MTLComputePipelineDescriptor, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>?) throws -> MTLComputePipelineState     func makeComputePipelineState(descriptor descriptor: MTLComputePipelineDescriptor, options options: MTLPipelineOption, completionHandler completionHandler: @escaping Metal.MTLNewComputePipelineStateWithReflectionCompletionHandler)     func makeFence() -> MTLFence     func supportsFeatureSet(_ featureSet: MTLFeatureSet) -> Bool     func supportsTextureSampleCount(_ sampleCount: Int) -> Bool } ``` |

Modified [MTLDevice.makeBuffer() -> Swift.Void)? = nil) -> MTLBuffer](https://developer.apple.com/documentation/metal/mtldevice/1433382-newbufferwithbytesnocopy)

|  | Declaration |
| --- | --- |
| From | ``` func makeBuffer(bytesNoCopy pointer: UnsafeMutableRawPointer, length length: Int, options options: MTLResourceOptions = [], deallocator deallocator: (@escaping (UnsafeMutableRawPointer, Int) -> Swift.Void)? = nil) -> MTLBuffer ``` |
| To | ``` func makeBuffer(bytesNoCopy pointer: UnsafeMutableRawPointer, length length: Int, options options: MTLResourceOptions = [], deallocator deallocator: ((UnsafeMutableRawPointer, Int) -> Swift.Void)? = nil) -> MTLBuffer ``` |

Modified [MTLDevice.makeComputePipelineState(descriptor: MTLComputePipelineDescriptor, options: MTLPipelineOption, completionHandler: Metal.MTLNewComputePipelineStateWithReflectionCompletionHandler)](https://developer.apple.com/documentation/metal/mtldevice/1433403-makecomputepipelinestate)

|  | Declaration |
| --- | --- |
| From | ``` func makeComputePipelineState(descriptor descriptor: MTLComputePipelineDescriptor, options options: MTLPipelineOption, completionHandler completionHandler: Metal.MTLNewComputePipelineStateWithReflectionCompletionHandler) ``` |
| To | ``` func makeComputePipelineState(descriptor descriptor: MTLComputePipelineDescriptor, options options: MTLPipelineOption, completionHandler completionHandler: @escaping Metal.MTLNewComputePipelineStateWithReflectionCompletionHandler) ``` |

Modified [MTLDevice.makeComputePipelineState(function: MTLFunction, completionHandler: Metal.MTLNewComputePipelineStateCompletionHandler)](https://developer.apple.com/documentation/metal/mtldevice/1433427-newcomputepipelinestatewithfunct)

|  | Declaration |
| --- | --- |
| From | ``` func makeComputePipelineState(function computeFunction: MTLFunction, completionHandler completionHandler: Metal.MTLNewComputePipelineStateCompletionHandler) ``` |
| To | ``` func makeComputePipelineState(function computeFunction: MTLFunction, completionHandler completionHandler: @escaping Metal.MTLNewComputePipelineStateCompletionHandler) ``` |

Modified [MTLDevice.makeComputePipelineState(function: MTLFunction, options: MTLPipelineOption, completionHandler: Metal.MTLNewComputePipelineStateWithReflectionCompletionHandler)](https://developer.apple.com/documentation/metal/mtldevice/1433410-makecomputepipelinestate)

|  | Declaration |
| --- | --- |
| From | ``` func makeComputePipelineState(function computeFunction: MTLFunction, options options: MTLPipelineOption, completionHandler completionHandler: Metal.MTLNewComputePipelineStateWithReflectionCompletionHandler) ``` |
| To | ``` func makeComputePipelineState(function computeFunction: MTLFunction, options options: MTLPipelineOption, completionHandler completionHandler: @escaping Metal.MTLNewComputePipelineStateWithReflectionCompletionHandler) ``` |

Modified [MTLDevice.makeLibrary(source: String, options: MTLCompileOptions?, completionHandler: Metal.MTLNewLibraryCompletionHandler)](https://developer.apple.com/documentation/metal/mtldevice/1433351-newlibrarywithsource)

|  | Declaration |
| --- | --- |
| From | ``` func makeLibrary(source source: String, options options: MTLCompileOptions?, completionHandler completionHandler: Metal.MTLNewLibraryCompletionHandler) ``` |
| To | ``` func makeLibrary(source source: String, options options: MTLCompileOptions?, completionHandler completionHandler: @escaping Metal.MTLNewLibraryCompletionHandler) ``` |

Modified [MTLDevice.makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, completionHandler: Metal.MTLNewRenderPipelineStateCompletionHandler)](https://developer.apple.com/documentation/metal/mtldevice/1433363-makerenderpipelinestate)

|  | Declaration |
| --- | --- |
| From | ``` func makeRenderPipelineState(descriptor descriptor: MTLRenderPipelineDescriptor, completionHandler completionHandler: Metal.MTLNewRenderPipelineStateCompletionHandler) ``` |
| To | ``` func makeRenderPipelineState(descriptor descriptor: MTLRenderPipelineDescriptor, completionHandler completionHandler: @escaping Metal.MTLNewRenderPipelineStateCompletionHandler) ``` |

Modified [MTLDevice.makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, options: MTLPipelineOption, completionHandler: Metal.MTLNewRenderPipelineStateWithReflectionCompletionHandler)](https://developer.apple.com/documentation/metal/mtldevice/1433365-newrenderpipelinestatewithdescri)

|  | Declaration |
| --- | --- |
| From | ``` func makeRenderPipelineState(descriptor descriptor: MTLRenderPipelineDescriptor, options options: MTLPipelineOption, completionHandler completionHandler: Metal.MTLNewRenderPipelineStateWithReflectionCompletionHandler) ``` |
| To | ``` func makeRenderPipelineState(descriptor descriptor: MTLRenderPipelineDescriptor, options options: MTLPipelineOption, completionHandler completionHandler: @escaping Metal.MTLNewRenderPipelineStateWithReflectionCompletionHandler) ``` |

Modified [MTLLibraryError.Code [enum]](https://developer.apple.com/documentation/metal/mtllibraryerror/code)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLLibraryErrorDomain : UInt {     case unsupported     case `internal`     case compileFailure     case compileWarning     case functionNotFound     case fileNotFound } ``` |
| To | ``` enum Code : UInt {         typealias _ErrorType = MTLLibraryError         case unsupported         case `internal`         case compileFailure         case compileWarning         case functionNotFound         case fileNotFound     } ``` |

Modified MTLRenderPipelineError.Code [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum MTLRenderPipelineErrorDomain : UInt {     case `internal`     case unsupported     case invalidInput } ``` |
| To | ``` enum Code : UInt {         typealias _ErrorType = MTLRenderPipelineError         case `internal`         case unsupported         case invalidInput     } ``` |

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
