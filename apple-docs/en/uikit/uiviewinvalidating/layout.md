---
title: layout
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS, Swift 5.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewinvalidating/layout
source_url: 'https://developer.apple.com/documentation/uikit/uiviewinvalidating/layout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewinvalidating/layout.json'
content_hash: 'sha256:7852d79de80ee75e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewInvalidating](../uiviewinvalidating.md)

# layout

<sub>Type Property</sub>

A change that invalidates the layout of the containing view’s subviews.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var layout: UIView.Invalidations.Layout { get }
```

## Discussion

Use this invalidation type to call [- setNeedsLayout](<../uiview/setneedslayout().md>) when a change in property value should cause an update to the layout of the containing view’s subviews.

## See Also

### Specifying invalidation types

- [configuration](configuration.md) — A change that invalidates a view’s configuration.
- [constraints](constraints.md) — A change that invalidates a view’s constraints.
- [display](display.md) — A change that requires the system to redraw a view’s content.
- [intrinsicContentSize](intrinsiccontentsize.md) — A change that invalidates a view’s intrinsic size.
