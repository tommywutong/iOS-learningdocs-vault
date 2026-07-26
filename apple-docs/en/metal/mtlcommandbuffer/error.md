---
title: error
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffer/error
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/error.json'
content_hash: 'sha256:195f9c935e314f40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# error

<sub>Instance Property</sub>

A description of an error when the GPU encounters an issue as it runs the command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var error: (any Error)? { get }
```

## Discussion

You typically check this property during development to get more information about a runtime issue. The property remains `nil` unless the GPU can’t successfully run the command buffer.

An error’s [userInfo](../../foundation/nserror/userinfo.md) dictionary property contains additional information if the command buffer’s [errorOptions](erroroptions.md) property includes [MTLCommandBufferErrorOptionEncoderExecutionStatus](../mtlcommandbuffererroroption/encoderexecutionstatus.md). You can retrieve an [MTLCommandBufferEncoderInfo](../mtlcommandbufferencoderinfo.md) instance from the dictionary by accessing it with [MTLCommandBufferEncoderInfoErrorKey](../mtlcommandbufferencoderinfoerrorkey.md).

## See Also

### Getting error details

- [errorOptions](erroroptions.md) — Settings that determine which information the command buffer records about execution errors, and how it does it.
- [MTLCommandBufferEncoderInfo](../mtlcommandbufferencoderinfo.md) — A container that provides additional information about a runtime failure a GPU encounters as it runs the commands in a command buffer.
- [MTLCommandBufferEncoderInfoErrorKey](../mtlcommandbufferencoderinfoerrorkey.md) — A key to a command buffer error’s user information dictionary that retrieves additional information about a GPU’s runtime error.
