---
title: UIWebViewDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwebviewdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uiwebviewdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebviewdelegate.json'
content_hash: 'sha256:c4982a890182e62c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIWebViewDelegate

<sub>Protocol</sub>

The `UIWebViewDelegate` protocol defines methods that a delegate of a [UIWebView](uiwebview.md) object can optionally implement to intervene when web content is loaded.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor protocol UIWebViewDelegate : NSObjectProtocol
```

## Overview

> [!important] Important
> Before releasing an instance of `UIWebView` for which you have set a delegate, you must first set the `UIWebView` delegate property to `nil` before disposing of the `UIWebView` instance. This can be done, for example, in the dealloc method where you dispose of the `UIWebView`.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Loading Content

- [- webView:shouldStartLoadWithRequest:navigationType:](<uiwebviewdelegate/webview(__shouldstartloadwith_navigationtype_).md>) — Sent before a web view begins loading a frame. _(deprecated)_
- [- webViewDidStartLoad:](<uiwebviewdelegate/webviewdidstartload(__).md>) — Sent after a web view starts loading a frame. _(deprecated)_
- [- webViewDidFinishLoad:](<uiwebviewdelegate/webviewdidfinishload(__).md>) — Sent after a web view finishes loading a frame. _(deprecated)_
- [- webView:didFailLoadWithError:](<uiwebviewdelegate/webview(__didfailloadwitherror_).md>) — Sent if a web view failed to load a frame. _(deprecated)_

## See Also

### Responding to web view changes

- [delegate](uiwebview/delegate.md) — The receiver’s delegate. _(deprecated)_
