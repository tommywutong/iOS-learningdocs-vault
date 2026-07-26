---
title: 'init(rawValue:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlblitoption/init(rawvalue:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlblitoption/init(rawvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitoption/init%28rawvalue%3A%29.json'
content_hash: 'sha256:e249b3ff00c109d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitOption](../mtlblitoption.md)

# init(rawValue:)

<sub>Initializer</sub>

Creates a blit option from a raw value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(rawValue: UInt)
```

## Parameters

- `rawValue` — The bitwise value of a blit option as an integer.

## Discussion

Use one of the [MTLBlitOption](../mtlblitoption.md) type’s static properties, such as [MTLBlitOptionDepthFromDepthStencil](depthfromdepthstencil.md), [MTLBlitOptionStencilFromDepthStencil](stencilfromdepthstencil.md), and [MTLBlitOptionRowLinearPVRTC](rowlinearpvrtc.md) instead of creating a blit option yourself with this initializer.
