---
title: 'init(rawValue:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandbuffererroroption/init(rawvalue:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffererroroption/init(rawvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffererroroption/init%28rawvalue%3A%29.json'
content_hash: 'sha256:6b5047740429742f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBufferErrorOption](../mtlcommandbuffererroroption.md)

# init(rawValue:)

<sub>Initializer</sub>

Creates a set of error options from a raw integer value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(rawValue: UInt)
```

## Parameters

- `rawValue` — The set of flags to use.

## Discussion

Use the [MTLCommandBufferErrorOption](../mtlcommandbuffererroroption.md) structure’s type properties, such as [MTLCommandBufferErrorOptionEncoderExecutionStatus](encoderexecutionstatus.md), instead of this initializer.
