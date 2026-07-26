---
title: 'append(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/navigationpath/append(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/navigationpath/append(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationpath/append%28_%3A%29.json'
content_hash: 'sha256:6d40208f62508560'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationPath](../navigationpath.md)

# append(_:)

<sub>Instance Method</sub>

Appends a new codable value to the end of this path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func append<V>(_ value: V) where V : Decodable, V : Encodable, V : Hashable
```

## See Also

### Managing path contents

- [isEmpty](isempty.md) — A Boolean that indicates whether this path is empty.
- [count](count.md) — The number of elements in this path.
- [removeLast(_:)](<removelast(__).md>) — Removes values from the end of this path.
