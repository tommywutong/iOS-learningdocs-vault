---
title: 'init(rawValue:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldatatype/init(rawvalue:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldatatype/init(rawvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldatatype/init%28rawvalue%3A%29.json'
content_hash: 'sha256:363f98564b1707ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDataType](../mtldatatype.md)

# init(rawValue:)

<sub>Initializer</sub>

Creates a data type instance from a raw integer value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init?(rawValue: UInt)
```

## Parameters

- `rawValue` — The underlying integer value that represents a data type.

## Discussion

Use the [MTLDataType](../mtldatatype.md) structure’s type properties, such as [MTLDataTypeInt](int.md), instead of this initializer.
