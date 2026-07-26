---
title: intrinsicContentSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS, Swift 5.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewinvalidating/intrinsiccontentsize
source_url: 'https://developer.apple.com/documentation/uikit/uiviewinvalidating/intrinsiccontentsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewinvalidating/intrinsiccontentsize.json'
content_hash: 'sha256:3fec23ede0b8ee19'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewInvalidating](../uiviewinvalidating.md)

# intrinsicContentSize

<sub>Type Property</sub>

A change that invalidates a view’s intrinsic size.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var intrinsicContentSize: UIView.Invalidations.IntrinsicContentSize { get }
```

## Discussion

Use this type of invalidation type to call [- invalidateIntrinsicContentSize](<../uiview/invalidateintrinsiccontentsize().md>) when a change in property value invalidates the containing view’s intrinsic content size. When you use this type, the constraint-based layout system accounts for the change the next time it updates the layout.

## See Also

### Specifying invalidation types

- [configuration](configuration.md) — A change that invalidates a view’s configuration.
- [constraints](constraints.md) — A change that invalidates a view’s constraints.
- [display](display.md) — A change that requires the system to redraw a view’s content.
- [layout](layout.md) — A change that invalidates the layout of the containing view’s subviews.
