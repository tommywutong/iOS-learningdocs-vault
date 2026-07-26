---
title: 'webView(_:didFailLoadWithError:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（12.0 起废弃）, iPadOS 2.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiwebviewdelegate/webview(_:didfailloadwitherror:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwebviewdelegate/webview(_:didfailloadwitherror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebviewdelegate/webview%28_%3Adidfailloadwitherror%3A%29.json'
content_hash: 'sha256:5d07b95d4332b282'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWebViewDelegate](../uiwebviewdelegate.md)

# webView(_:didFailLoadWithError:)

<sub>Instance Method</sub>

Sent if a web view failed to load a frame.

> [!warning] Deprecated
> For more information, see [UIWebView](../uiwebview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func webView(_ webView: UIWebView, didFailLoadWithError error: any Error)
```

## Parameters

- `webView` — The web view that failed to load a frame.

- `error` — The error that occurred during loading.

## See Also

### Loading Content

- [- webView:shouldStartLoadWithRequest:navigationType:](<webview(__shouldstartloadwith_navigationtype_).md>) — Sent before a web view begins loading a frame. _(deprecated)_
- [- webViewDidStartLoad:](<webviewdidstartload(__).md>) — Sent after a web view starts loading a frame. _(deprecated)_
- [- webViewDidFinishLoad:](<webviewdidfinishload(__).md>) — Sent after a web view finishes loading a frame. _(deprecated)_
