---
title: 'hash(into:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/color/hash(into:)'
source_url: 'https://developer.apple.com/documentation/swiftui/color/hash(into:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/color/hash%28into%3A%29.json'
content_hash: 'sha256:74e58db43e494070'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Color](../color.md)

# hash(into:)

<sub>Instance Method</sub>

Hashes the essential components of the color by feeding them into the given hash function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hash(into hasher: inout Hasher)
```

## Parameters

- `hasher` — The hash function to use when combining the components of the color.

## See Also

### Comparing colors

- [==(_:_:)](<==(____).md>) — Indicates whether two colors are equal.
