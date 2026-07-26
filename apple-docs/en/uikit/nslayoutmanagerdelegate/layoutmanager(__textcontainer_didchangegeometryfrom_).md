---
title: 'layoutManager(_:textContainer:didChangeGeometryFrom:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanagerdelegate/layoutmanager(_:textcontainer:didchangegeometryfrom:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/layoutmanager(_:textcontainer:didchangegeometryfrom:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanagerdelegate/layoutmanager%28_%3Atextcontainer%3Adidchangegeometryfrom%3A%29.json'
content_hash: 'sha256:b6d87b49d42849d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManagerDelegate](../nslayoutmanagerdelegate.md)

# layoutManager(_:textContainer:didChangeGeometryFrom:)

<sub>Instance Method</sub>

Informs the delegate when the layout manager invalidates layout due to a change in the geometry of the specified text container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func layoutManager(_ layoutManager: NSLayoutManager, textContainer: NSTextContainer, didChangeGeometryFrom oldSize: CGSize)
```

## Parameters

- `layoutManager` — The layout manager invalidating layout.

- `textContainer` — The text container that changed geometry.

- `oldSize` — The size of the text container before it changed geometry.

## Discussion

The delegate can react to the geometry change and perform adjustments such as recreating an exclusion path.

## See Also

### Responding to text container layout

- [- layoutManager:didCompleteLayoutForTextContainer:atEnd:](<layoutmanager(__didcompletelayoutfor_atend_).md>) — Informs the delegate when the layout manager finishes laying out text in the specified text container.
