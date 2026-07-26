---
title: 'init(rawValue:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommoncounter/init(rawvalue:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommoncounter/init(rawvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommoncounter/init%28rawvalue%3A%29.json'
content_hash: 'sha256:f74056bec73bb266'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommonCounter](../mtlcommoncounter.md)

# init(rawValue:)

<sub>Initializer</sub>

Creates a common counter name from a raw value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(rawValue: String)
```

## Parameters

- `rawValue` — The name of a common counter as a string.

## Discussion

Use of the [MTLCommonCounter](../mtlcommoncounter.md) type’s static properties, such as [MTLCommonCounterTimestamp](timestamp.md), [MTLCommonCounterComputeKernelInvocations](computekernelinvocations.md), or [MTLCommonCounterTotalCycles](totalcycles.md) instead of creating a common counter instance yourself with this initializer.
