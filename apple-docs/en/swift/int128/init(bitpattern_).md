---
title: 'init(bitPattern:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int128/init(bitpattern:)'
source_url: 'https://developer.apple.com/documentation/swift/int128/init(bitpattern:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int128/init%28bitpattern%3A%29.json'
content_hash: 'sha256:dbbbfd49ea05285f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int128](../int128.md)

# init(bitPattern:)

<sub>Initializer</sub>

Creates a new instance with the same memory representation as the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(bitPattern: UInt128)
```

## Parameters

- `bitPattern` — A value to use as the source of the new instance’s binary representation.

## Discussion

This initializer does not perform any range or overflow checking. The resulting instance may not have the same numeric value as `bitPattern`—it is only guaranteed to use the same pattern of bits in its binary representation.
