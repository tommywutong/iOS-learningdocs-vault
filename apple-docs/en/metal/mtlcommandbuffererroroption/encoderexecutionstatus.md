---
title: encoderExecutionStatus
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffererroroption/encoderexecutionstatus
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffererroroption/encoderexecutionstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffererroroption/encoderexecutionstatus.json'
content_hash: 'sha256:3252d92f128373ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBufferErrorOption](../mtlcommandbuffererroroption.md)

# encoderExecutionStatus

<sub>Type Property</sub>

An option that instructs a command buffer to save additional details about a GPU runtime error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var encoderExecutionStatus: MTLCommandBufferErrorOption { get }
```

## Discussion

You can set this option to a command buffer descriptor’s [errorOptions](../mtlcommandbufferdescriptor/erroroptions.md) property.

> [!note] Note
> Enabling this option can slightly reduce your app’s CPU runtime performance.
