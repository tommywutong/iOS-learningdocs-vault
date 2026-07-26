---
title: MTLCommandBufferEncoderInfoErrorKey
framework: Metal
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbufferencoderinfoerrorkey
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbufferencoderinfoerrorkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbufferencoderinfoerrorkey.json'
content_hash: 'sha256:c7cf1bed9b89ec26'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCommandBufferEncoderInfoErrorKey

<sub>Global Variable</sub>

A key to a command buffer error’s user information dictionary that retrieves additional information about a GPU’s runtime error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let MTLCommandBufferEncoderInfoErrorKey: String
```

## Discussion

You can retrieve an [MTLCommandBufferEncoderInfo](mtlcommandbufferencoderinfo.md) instance from the [userInfo](../foundation/nserror/userinfo.md) dictionary of a command buffer’s [error](mtlcommandbuffer/error.md) property.

## See Also

### Getting error details

- [error](mtlcommandbuffer/error.md) — A description of an error when the GPU encounters an issue as it runs the command buffer.
- [errorOptions](mtlcommandbuffer/erroroptions.md) — Settings that determine which information the command buffer records about execution errors, and how it does it.
- [MTLCommandBufferEncoderInfo](mtlcommandbufferencoderinfo.md) — A container that provides additional information about a runtime failure a GPU encounters as it runs the commands in a command buffer.
