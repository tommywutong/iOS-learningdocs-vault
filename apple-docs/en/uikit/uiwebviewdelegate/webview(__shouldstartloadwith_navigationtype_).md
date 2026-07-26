---
title: 'webView(_:shouldStartLoadWith:navigationType:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（12.0 起废弃）, iPadOS 2.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiwebviewdelegate/webview(_:shouldstartloadwith:navigationtype:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwebviewdelegate/webview(_:shouldstartloadwith:navigationtype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebviewdelegate/webview%28_%3Ashouldstartloadwith%3Anavigationtype%3A%29.json'
content_hash: 'sha256:94fa9d3113680184'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWebViewDelegate](../uiwebviewdelegate.md)

# webView(_:shouldStartLoadWith:navigationType:)

<sub>Instance Method</sub>

Sent before a web view begins loading a frame.

> [!warning] Deprecated
> For more information, see [UIWebView](../uiwebview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func webView(_ webView: UIWebView, shouldStartLoadWith request: URLRequest, navigationType: UIWebView.NavigationType) -> Bool
```

## Parameters

- `webView` — The web view that is about to load a new frame.

- `request` — The content location.

- `navigationType` — The type of user action that started the load request.

## Return Value

[true](../../swift/true.md) if the web view should begin loading content; otherwise, [false](../../swift/false.md) .

## See Also

### Loading Content

- [- webViewDidStartLoad:](<webviewdidstartload(__).md>) — Sent after a web view starts loading a frame. _(deprecated)_
- [- webViewDidFinishLoad:](<webviewdidfinishload(__).md>) — Sent after a web view finishes loading a frame. _(deprecated)_
- [- webView:didFailLoadWithError:](<webview(__didfailloadwitherror_).md>) — Sent if a web view failed to load a frame. _(deprecated)_
