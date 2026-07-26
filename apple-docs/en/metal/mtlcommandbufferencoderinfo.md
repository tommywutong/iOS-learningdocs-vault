---
title: MTLCommandBufferEncoderInfo
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbufferencoderinfo
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbufferencoderinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbufferencoderinfo.json'
content_hash: 'sha256:80f36f71587c7ad5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCommandBufferEncoderInfo

<sub>Protocol</sub>

A container that provides additional information about a runtime failure a GPU encounters as it runs the commands in a command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLCommandBufferEncoderInfo : NSObjectProtocol
```

## Overview

To create a command buffer that generates additional information (when a GPU encounters an error running it), configure an [MTLCommandBufferDescriptor](mtlcommandbufferdescriptor.md) instance’s [errorOptions](mtlcommandbufferdescriptor/erroroptions.md) property. For information about how to retrieve the information from an [MTLCommandBuffer](mtlcommandbuffer.md) instance, see its [error](mtlcommandbuffer/error.md) property.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Inspecting execution information

- [label](mtlcommandbufferencoderinfo/label.md) — The name of the encoder that generates the error information.
- [debugSignposts](mtlcommandbufferencoderinfo/debugsignposts.md) — An array of debug signposts that Metal records as the GPU executes the commands of the encoder’s pass.
- [errorState](mtlcommandbufferencoderinfo/errorstate.md) — The execution status of the command encoder.
- [MTLCommandEncoderErrorState](mtlcommandencodererrorstate.md) — Possible error conditions for the command encoder’s commands.

## See Also

### Getting error details

- [error](mtlcommandbuffer/error.md) — A description of an error when the GPU encounters an issue as it runs the command buffer.
- [errorOptions](mtlcommandbuffer/erroroptions.md) — Settings that determine which information the command buffer records about execution errors, and how it does it.
- [MTLCommandBufferEncoderInfoErrorKey](mtlcommandbufferencoderinfoerrorkey.md) — A key to a command buffer error’s user information dictionary that retrieves additional information about a GPU’s runtime error.
