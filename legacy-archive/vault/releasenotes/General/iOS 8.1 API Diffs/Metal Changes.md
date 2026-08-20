---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/Metal.html
archived_at: '2026-07-18T02:56:14.786193Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# Metal Changes

## Metal

Removed MTLColorWriteMask.valueRemoved MTLPipelineOption.valueRemoved MTLRenderPassColorAttachmentDescriptorArray.objectAtIndexedSubscript(Int) -> MTLRenderPassColorAttachmentDescriptorRemoved MTLRenderPassColorAttachmentDescriptorArray.setObject(MTLRenderPassColorAttachmentDescriptor?, atIndexedSubscript: Int)Removed MTLRenderPipelineColorAttachmentDescriptorArray.objectAtIndexedSubscript(Int) -> MTLRenderPipelineColorAttachmentDescriptorRemoved MTLRenderPipelineColorAttachmentDescriptorArray.setObject(MTLRenderPipelineColorAttachmentDescriptor?, atIndexedSubscript: Int)Removed MTLResourceOptions.valueRemoved MTLVertexAttributeDescriptorArray.objectAtIndexedSubscript(Int) -> MTLVertexAttributeDescriptorRemoved MTLVertexAttributeDescriptorArray.setObject(MTLVertexAttributeDescriptor?, atIndexedSubscript: Int)Removed MTLVertexBufferLayoutDescriptorArray.objectAtIndexedSubscript(Int) -> MTLVertexBufferLayoutDescriptorRemoved MTLVertexBufferLayoutDescriptorArray.setObject(MTLVertexBufferLayoutDescriptor!, atIndexedSubscript: Int)Added MTLColorWriteMask.init(rawValue: UInt)Added MTLPipelineOption.init(rawValue: UInt)Added MTLResourceOptions.init(rawValue: UInt)Modified MTLColorWriteMask [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MTLColorWriteMask : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var None: MTLColorWriteMask { get }     static var Red: MTLColorWriteMask { get }     static var Green: MTLColorWriteMask { get }     static var Blue: MTLColorWriteMask { get }     static var Alpha: MTLColorWriteMask { get }     static var All: MTLColorWriteMask { get } } ``` |
| To | ``` struct MTLColorWriteMask : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: MTLColorWriteMask { get }     static var Red: MTLColorWriteMask { get }     static var Green: MTLColorWriteMask { get }     static var Blue: MTLColorWriteMask { get }     static var Alpha: MTLColorWriteMask { get }     static var All: MTLColorWriteMask { get } } ``` |

Modified MTLColorWriteMask.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified MTLPipelineOption [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MTLPipelineOption : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var None: MTLPipelineOption { get }     static var ArgumentInfo: MTLPipelineOption { get }     static var BufferTypeInfo: MTLPipelineOption { get } } ``` |
| To | ``` struct MTLPipelineOption : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: MTLPipelineOption { get }     static var ArgumentInfo: MTLPipelineOption { get }     static var BufferTypeInfo: MTLPipelineOption { get } } ``` |

Modified MTLPipelineOption.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified MTLResourceOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MTLResourceOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var OptionCPUCacheModeDefault: MTLResourceOptions { get }     static var OptionCPUCacheModeWriteCombined: MTLResourceOptions { get } } ``` |
| To | ``` struct MTLResourceOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var OptionCPUCacheModeDefault: MTLResourceOptions { get }     static var OptionCPUCacheModeWriteCombined: MTLResourceOptions { get } } ``` |

Modified MTLResourceOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

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
