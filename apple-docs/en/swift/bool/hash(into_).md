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
doc_path: '/documentation/swift/bool/hash(into:)'
source_url: 'https://developer.apple.com/documentation/swift/bool/hash(into:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bool/hash%28into%3A%29.json'
content_hash: 'sha256:d0e20e2c4c12adb5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Bool](../bool.md)

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

### Inspecting a Boolean

- [customMirror](custommirror.md) — A mirror that reflects the `Bool` instance.
- [customPlaygroundQuickLook](customplaygroundquicklook.md) — A custom playground Quick Look for the `Bool` instance. _(deprecated)_
- [hashValue](hashvalue.md) — The hash value.
