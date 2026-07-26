---
title: debugDescription
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float/debugdescription
source_url: 'https://developer.apple.com/documentation/swift/float/debugdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/debugdescription.json'
content_hash: 'sha256:d39058f7efb3fed3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# debugDescription

<sub>Instance Property</sub>

A textual representation of the value, suitable for debugging.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var debugDescription: String { get }
```

## Discussion

This property has the same value as the `description` property, except that NaN values are printed in an extended format.

## See Also

### Describing a Float

- [hash(into:)](<hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.
- [description](description.md) — A textual representation of the value.
- [customMirror](custommirror.md) — A mirror that reflects the `Float` instance.
- [hashValue](hashvalue.md) — The hash value.
