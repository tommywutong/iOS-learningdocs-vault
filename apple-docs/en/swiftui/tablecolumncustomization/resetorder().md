---
title: resetOrder()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tablecolumncustomization/resetorder()
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumncustomization/resetorder()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumncustomization/resetorder%28%29.json'
content_hash: 'sha256:0348351311571a13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableColumnCustomization](../tablecolumncustomization.md)

# resetOrder()

<sub>Instance Method</sub>

Resets the column order back to the default, preserving the customized visibility and size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
mutating func resetOrder()
```

## Discussion

Tables that are bound to this state will order their columns as described by their column builder.

## See Also

### Managing the customization

- [subscript(visibility:)](<subscript(visibility_).md>) — The visibility of the column identified by its identifier.
