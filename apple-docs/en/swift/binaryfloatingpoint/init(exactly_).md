---
title: 'init(exactly:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/binaryfloatingpoint/init(exactly:)'
source_url: 'https://developer.apple.com/documentation/swift/binaryfloatingpoint/init(exactly:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binaryfloatingpoint/init%28exactly%3A%29.json'
content_hash: 'sha256:feae9c4e9200bf1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BinaryFloatingPoint](../binaryfloatingpoint.md)

# init(exactly:)

<sub>Initializer</sub>

Creates a new instance from the given value, if it can be represented exactly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?<Source>(exactly value: Source) where Source : BinaryFloatingPoint
```

## Parameters

- `value` — A floating-point value to be converted.

## Discussion

If the given floating-point value cannot be represented exactly, the result is `nil`. A value that is NaN (“not a number”) cannot be represented exactly if its payload cannot be encoded exactly.

## Default Implementations

### BinaryFloatingPoint Implementations

- [init(exactly:)](<init(exactly_)-6fobm.md>) — Creates a new instance from the given value, if it can be represented exactly.
- [init(exactly:)](<init(exactly_)-9lyid.md>) — Creates a new value, if the given integer can be represented exactly.
