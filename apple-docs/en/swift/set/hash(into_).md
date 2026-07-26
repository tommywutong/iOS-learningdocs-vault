---
title: 'hash(into:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/set/hash(into:)'
source_url: 'https://developer.apple.com/documentation/swift/set/hash(into:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/hash%28into%3A%29.json'
content_hash: 'sha256:5ee27db1cd63a4e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

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

### Describing a Set

- [description](description.md) — A string that represents the contents of the set.
- [debugDescription](debugdescription.md) — A string that represents the contents of the set, suitable for debugging.
- [customMirror](custommirror.md) — A mirror that reflects the set.
