---
title: 'subscript(_:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/layoutsubview/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/layoutsubview/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layoutsubview/subscript%28_%3A%29.json'
content_hash: 'sha256:b06b4d3dee3cfad9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LayoutSubview](../layoutsubview.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Gets the value for the subview that’s associated with the specified key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<K>(key: K.Type) -> K.Value where K : LayoutValueKey { get }
```

## Overview

If you define a custom layout value using [LayoutValueKey](../layoutvaluekey.md), you can read the key’s associated value for a given subview in a layout container by indexing the container’s subviews with the key type. For example, if you define a `Flexibility` key type, you can put the associated values of all the layout’s subviews into an array:

```swift
let flexibilities = subviews.map { subview in
    subview[Flexibility.self]
}
```

For more information about creating a custom layout, see [Layout](../layout.md).
