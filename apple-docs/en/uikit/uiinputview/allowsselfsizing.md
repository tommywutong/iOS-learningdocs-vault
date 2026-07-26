---
title: allowsSelfSizing
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiinputview/allowsselfsizing
source_url: 'https://developer.apple.com/documentation/uikit/uiinputview/allowsselfsizing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinputview/allowsselfsizing.json'
content_hash: 'sha256:e75734e1356749d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIInputView](../uiinputview.md)

# allowsSelfSizing

<sub>Instance Property</sub>

A Boolean value that indicates whether the input view is responsible for its own size.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var allowsSelfSizing: Bool { get set }
```

## Discussion

When the value of this property is [false](../../swift/false.md) (the default), UIKit determines an appropriate size of the input view based on its current layout. When the value of this property is [true](../../swift/true.md), UIKit honors the value returned by the [- systemLayoutSizeFittingSize:](<../uiview/systemlayoutsizefitting(__).md>) method of the input view.
