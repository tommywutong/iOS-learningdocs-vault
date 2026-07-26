---
title: 'inset(by:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uishape-swift.struct/resolved/inset(by:)-1r5gp'
source_url: 'https://developer.apple.com/documentation/uikit/uishape-swift.struct/resolved/inset(by:)-1r5gp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uishape-swift.struct/resolved/inset%28by%3A%29-1r5gp.json'
content_hash: 'sha256:1badbff6cf720c62'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIShape](../../uishape-swift.struct.md) · [Resolved](../resolved.md)

# inset(by:)

<sub>Instance Method</sub>

Creates a new modified shape by applying the provided inset to this shape.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func inset(by amount: CGFloat) -> UIShape.Resolved
```

## Discussion

You can use negative values to add inner padding to a shape.

If it isn’t possible to inset this shape (for example, if it’s a custom path), this method doesn’t have any effect. For some shapes like rounded rectangles, this method can also modify the corner radii of the shape to ensure the resulting corners are concentric.

## See Also

### Creating a resolved shape by applying insets

- [inset(by:)](<inset(by_)-9sjcg.md>) — Creates a new modified shape by applying the provided insets to this shape.
