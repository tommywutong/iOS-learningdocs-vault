---
title: 'hash(into:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/hash(into:)'
source_url: 'https://developer.apple.com/documentation/swift/string/hash(into:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/hash%28into%3A%29.json'
content_hash: 'sha256:dfba05d928f9a677'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# hash(into:)

<sub>Instance Method</sub>

Hashes the essential components of this value by feeding them into the given hasher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hash(into hasher: inout Hasher)
```

## Parameters

- `hasher` — The hasher to use when combining the components of this instance.

## See Also

### Describing a String

- [description](description.md) — The value of this string.
- [debugDescription](debugdescription.md) — A representation of the string that is suitable for debugging.
- [customMirror](custommirror.md) — A mirror that reflects the `String` instance.
- [hashValue](hashvalue.md) — The hash value.
