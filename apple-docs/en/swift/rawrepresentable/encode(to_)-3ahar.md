---
title: 'encode(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rawrepresentable/encode(to:)-3ahar'
source_url: 'https://developer.apple.com/documentation/swift/rawrepresentable/encode(to:)-3ahar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rawrepresentable/encode%28to%3A%29-3ahar.json'
content_hash: 'sha256:92ff1bdf50990c52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RawRepresentable](../rawrepresentable.md)

# encode(to:)

<sub>Instance Method</sub>

Encodes this value into the given encoder, when the type’s `RawValue` is `UInt128`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encode(to encoder: any Encoder) throws
```

## Parameters

- `encoder` — The encoder to write data to.

## Discussion

This function throws an error if any values are invalid for the given encoder’s format.
