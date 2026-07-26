---
title: description
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/description
source_url: 'https://developer.apple.com/documentation/swift/string/description'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/description.json'
content_hash: 'sha256:8e39e35b7c521457'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# description

<sub>Instance Property</sub>

The value of this string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var description: String { get }
```

## Discussion

Using this property directly is discouraged. Instead, use simple assignment to create a new constant or variable equal to this string.

## See Also

### Describing a String

- [debugDescription](debugdescription.md) — A representation of the string that is suitable for debugging.
- [customMirror](custommirror.md) — A mirror that reflects the `String` instance.
- [hashValue](hashvalue.md) — The hash value.
- [hash(into:)](<hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.
