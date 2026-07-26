---
title: display
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS, Swift 5.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewinvalidating/display
source_url: 'https://developer.apple.com/documentation/uikit/uiviewinvalidating/display'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewinvalidating/display.json'
content_hash: 'sha256:345a4773548d918d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewInvalidating](../uiviewinvalidating.md)

# display

<sub>Type Property</sub>

A change that requires the system to redraw a view’s content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var display: UIView.Invalidations.Display { get }
```

## Discussion

Use this invalidation type to call [- setNeedsDisplay](<../uiview/setneedsdisplay().md>) when a change in property value should cause the system to redraw the containing view’s content.

## See Also

### Specifying invalidation types

- [configuration](configuration.md) — A change that invalidates a view’s configuration.
- [constraints](constraints.md) — A change that invalidates a view’s constraints.
- [intrinsicContentSize](intrinsiccontentsize.md) — A change that invalidates a view’s intrinsic size.
- [layout](layout.md) — A change that invalidates the layout of the containing view’s subviews.
