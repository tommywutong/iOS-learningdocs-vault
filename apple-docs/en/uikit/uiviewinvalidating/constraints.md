---
title: constraints
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS, Swift 5.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewinvalidating/constraints
source_url: 'https://developer.apple.com/documentation/uikit/uiviewinvalidating/constraints'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewinvalidating/constraints.json'
content_hash: 'sha256:f936f23112d65f53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewInvalidating](../uiviewinvalidating.md)

# constraints

<sub>Type Property</sub>

A change that invalidates a view’s constraints.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var constraints: UIView.Invalidations.Constraints { get }
```

## Discussion

Use this invalidation type to call [- setNeedsUpdateConstraints](<../uiview/setneedsupdateconstraints().md>) when a change in property value should cause the containing view to update constraints.

## See Also

### Specifying invalidation types

- [configuration](configuration.md) — A change that invalidates a view’s configuration.
- [display](display.md) — A change that requires the system to redraw a view’s content.
- [intrinsicContentSize](intrinsiccontentsize.md) — A change that invalidates a view’s intrinsic size.
- [layout](layout.md) — A change that invalidates the layout of the containing view’s subviews.
