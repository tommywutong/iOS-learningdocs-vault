---
title: tertiary
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/shapestyle/tertiary-swift.type.property
source_url: 'https://developer.apple.com/documentation/swiftui/shapestyle/tertiary-swift.type.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapestyle/tertiary-swift.type.property.json'
content_hash: 'sha256:bccd08c7b7c9ac7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeStyle](../shapestyle.md)

# tertiary

<sub>Type Property</sub>

A shape style that maps to the third level of the current content style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static var tertiary: HierarchicalShapeStyle { get }
```

## Discussion

This hierarchical style maps to the third level of the current foreground style, or to the third level of the default foreground style if you haven’t set a foreground style in the view’s environment. You typically set a foreground style by supplying a non-hierarchical style to the [foregroundStyle(_:)](<../view/foregroundstyle(__).md>) modifier.

For information about how to use shape styles, see [ShapeStyle](../shapestyle.md).

## See Also

### Hierarchical styles

- [secondary](secondary-swift.property.md) — Returns the second level of this shape style.
- [tertiary](tertiary-swift.property.md) — Returns the third level of this shape style.
- [quaternary](quaternary-swift.property.md) — Returns the fourth level of this shape style.
- [quinary](quinary-swift.property.md) — Returns the fifth level of this shape style.
- [primary](primary.md) — A shape style that maps to the first level of the current content style.
- [secondary](secondary-swift.type.property.md) — A shape style that maps to the second level of the current content style.
- [quaternary](quaternary-swift.type.property.md) — A shape style that maps to the fourth level of the current content style.
- [quinary](quinary-swift.type.property.md) — A shape style that maps to the fifth level of the current content style.
