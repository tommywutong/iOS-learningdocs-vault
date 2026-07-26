---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/delegate.json'
content_hash: 'sha256:e409666bae07c76a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# delegate

<sub>Instance Property</sub>

The delegate of the scroll view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var delegate: (any UIScrollViewDelegate)? { get set }
```

## Discussion

The delegate must adopt the [UIScrollViewDelegate](../uiscrollviewdelegate.md) protocol. The [UIScrollView](../uiscrollview.md) class, which doesn’t retain the delegate, invokes each protocol method the delegate implements.

## See Also

### Responding to scroll view interactions

- [UIScrollViewDelegate](../uiscrollviewdelegate.md) — The interface for the delegate of a scroll view.
