---
title: canGoBack
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（12.0 起废弃）, iPadOS 2.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwebview/cangoback
source_url: 'https://developer.apple.com/documentation/uikit/uiwebview/cangoback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebview/cangoback.json'
content_hash: 'sha256:1dbece4a607eaaa1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWebView](../uiwebview.md)

# canGoBack

<sub>Instance Property</sub>

A Boolean value indicating whether the receiver can move backward.

> [!warning] Deprecated
> For more information, see [UIWebView](../uiwebview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var canGoBack: Bool { get }
```

## Discussion

If [true](../../swift/true.md), able to move backward; otherwise, [false](../../swift/false.md).

## See Also

### Moving back and forward

- [canGoForward](cangoforward.md) — A Boolean value indicating whether the receiver can move forward. _(deprecated)_
- [- goBack](<goback().md>) — Loads the previous location in the back-forward list. _(deprecated)_
- [- goForward](<goforward().md>) — Loads the next location in the back-forward list. _(deprecated)_
