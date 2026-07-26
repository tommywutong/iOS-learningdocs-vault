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
doc_path: '/documentation/swift/character/hash(into:)'
source_url: 'https://developer.apple.com/documentation/swift/character/hash(into:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/character/hash%28into%3A%29.json'
content_hash: 'sha256:181b8f3fec7d8999'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Character](../character.md)

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

### Describing a Character

- [description](description.md) — A textual representation of this instance.
- [debugDescription](debugdescription.md) — A textual representation of the character, suitable for debugging.
- [customMirror](custommirror.md) — A mirror that reflects the `Character` instance.
- [customPlaygroundQuickLook](customplaygroundquicklook.md) — A custom playground Quick Look for the `Character` instance. _(deprecated)_
