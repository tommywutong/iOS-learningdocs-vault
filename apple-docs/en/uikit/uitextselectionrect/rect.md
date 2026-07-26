---
title: rect
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextselectionrect/rect
source_url: 'https://developer.apple.com/documentation/uikit/uitextselectionrect/rect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextselectionrect/rect.json'
content_hash: 'sha256:99bfe6eb6f96b974'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSelectionRect](../uitextselectionrect.md)

# rect

<sub>Instance Property</sub>

The rectangle that encloses the text selection rectangle’s text range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var rect: CGRect { get }
```

## Discussion

The returned rectangle is in the coordinate system of the text input view that created the receiver.
