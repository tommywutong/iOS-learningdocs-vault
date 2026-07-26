---
title: 'removeLast(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/navigationpath/removelast(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/navigationpath/removelast(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationpath/removelast%28_%3A%29.json'
content_hash: 'sha256:51c44a49d9df1409'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationPath](../navigationpath.md)

# removeLast(_:)

<sub>Instance Method</sub>

Removes values from the end of this path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func removeLast(_ k: Int = 1)
```

## Parameters

- `k` — The number of values to remove. The default value is `1`.

## Discussion

> [!info] Precondition
> The input parameter `k` must be greater than or equal to zero, and must be less than or equal to the number of elements in the path.

## See Also

### Managing path contents

- [isEmpty](isempty.md) — A Boolean that indicates whether this path is empty.
- [count](count.md) — The number of elements in this path.
- [append(_:)](<append(__).md>) — Appends a new codable value to the end of this path.
