---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（12.0 起废弃）, iPadOS 2.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwebview/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uiwebview/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebview/delegate.json'
content_hash: 'sha256:ae552f1df8a0620c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWebView](../uiwebview.md)

# delegate

<sub>Instance Property</sub>

The receiver’s delegate.

> [!warning] Deprecated
> For more information, see [UIWebView](../uiwebview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
unowned(unsafe) var delegate: (any UIWebViewDelegate)? { get set }
```

## Discussion

The delegate is sent messages when content is loading. See [UIWebViewDelegate](../uiwebviewdelegate.md) for the optional methods this delegate may implement.

> [!important] Important
> Before releasing an instance of `UIWebView` for which you have set a delegate, you must first set its delegate property to `nil`. This can be done, for example, in your dealloc method.

## See Also

### Responding to web view changes

- [UIWebViewDelegate](../uiwebviewdelegate.md) — The `UIWebViewDelegate` protocol defines methods that a delegate of a [UIWebView](../uiwebview.md) object can optionally implement to intervene when web content is loaded.
