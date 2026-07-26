---
title: transfersHorizontalScrollingToParent
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, tvOS 17.4+, visionOS 1.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/transfershorizontalscrollingtoparent
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/transfershorizontalscrollingtoparent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/transfershorizontalscrollingtoparent.json'
content_hash: 'sha256:cc19ef311e627554'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# transfersHorizontalScrollingToParent

<sub>Instance Property</sub>

A Boolean value that determines whether the scroll view passes horizontal scroll events to a superview.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var transfersHorizontalScrollingToParent: Bool { get set }
```

## Discussion

The default value is `true`, in which case when the scroll view reaches either end of its horizontal scroll axis it transfers scroll events to a containing scroll view. To stop this behavior, set the property to `false`.

## See Also

### Nesting scroll views

- [transfersVerticalScrollingToParent](transfersverticalscrollingtoparent.md) — A Boolean value that determines whether the scroll view passes vertical scroll events to a superview.
