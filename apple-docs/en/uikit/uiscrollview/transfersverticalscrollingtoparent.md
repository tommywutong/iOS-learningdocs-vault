---
title: transfersVerticalScrollingToParent
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, tvOS 17.4+, visionOS 1.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/transfersverticalscrollingtoparent
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/transfersverticalscrollingtoparent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/transfersverticalscrollingtoparent.json'
content_hash: 'sha256:aed02104b7c4a3f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# transfersVerticalScrollingToParent

<sub>Instance Property</sub>

A Boolean value that determines whether the scroll view passes vertical scroll events to a superview.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var transfersVerticalScrollingToParent: Bool { get set }
```

## Discussion

The default value is `true`, in which case when the scroll view reaches either end of its vertical scroll axis it transfers scroll events to a containing scroll view. To stop this behavior, set the property to `false`.

## See Also

### Nesting scroll views

- [transfersHorizontalScrollingToParent](transfershorizontalscrollingtoparent.md) — A Boolean value that determines whether the scroll view passes horizontal scroll events to a superview.
