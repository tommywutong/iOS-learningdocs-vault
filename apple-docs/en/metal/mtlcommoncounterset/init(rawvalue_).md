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
doc_path: '/documentation/metal/mtlcommoncounterset/init(rawvalue:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommoncounterset/init(rawvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommoncounterset/init%28rawvalue%3A%29.json'
content_hash: 'sha256:61e4b381ae00a9c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommonCounterSet](../mtlcommoncounterset.md)

# init(rawValue:)

<sub>Initializer</sub>

Creates a common counter set name from a raw value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(rawValue: String)
```

## Parameters

- `rawValue` — The name of a counter set as a string.

## Discussion

Use one of the [MTLCommonCounterSet](../mtlcommoncounterset.md) type’s static properties, such as [MTLCommonCounterSetTimestamp](timestamp.md), [MTLCommonCounterSetStageUtilization](stageutilization.md), and [MTLCommonCounterSetStatistic](statistic.md) instead of creating a common counter set instance yourself with this initializer.
