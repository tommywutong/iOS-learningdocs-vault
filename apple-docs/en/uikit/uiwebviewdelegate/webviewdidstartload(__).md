---
title: 'webViewDidStartLoad(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（12.0 起废弃）, iPadOS 2.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiwebviewdelegate/webviewdidstartload(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwebviewdelegate/webviewdidstartload(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebviewdelegate/webviewdidstartload%28_%3A%29.json'
content_hash: 'sha256:de2cd0b53410b1c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWebViewDelegate](../uiwebviewdelegate.md)

# webViewDidStartLoad(_:)

<sub>Instance Method</sub>

Sent after a web view starts loading a frame.

> [!warning] Deprecated
> For more information, see [UIWebView](../uiwebview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func webViewDidStartLoad(_ webView: UIWebView)
```

## Parameters

- `webView` — The web view that has begun loading a new frame.

## See Also

### Loading Content

- [- webView:shouldStartLoadWithRequest:navigationType:](<webview(__shouldstartloadwith_navigationtype_).md>) — Sent before a web view begins loading a frame. _(deprecated)_
- [- webViewDidFinishLoad:](<webviewdidfinishload(__).md>) — Sent after a web view finishes loading a frame. _(deprecated)_
- [- webView:didFailLoadWithError:](<webview(__didfailloadwitherror_).md>) — Sent if a web view failed to load a frame. _(deprecated)_
