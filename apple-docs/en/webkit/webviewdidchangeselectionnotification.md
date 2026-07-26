---
title: WebViewDidChangeSelectionNotification
framework: WebKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.3+（10.14 起废弃）]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/webkit/webviewdidchangeselectionnotification
source_url: 'https://developer.apple.com/documentation/webkit/webviewdidchangeselectionnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/webkit/webviewdidchangeselectionnotification.json'
content_hash: 'sha256:830d8012675c32f0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WebKit](../webkit.md)

# WebViewDidChangeSelectionNotification

<sub>Global Variable</sub>

Posted when a web view changes its typing selection.

<sub>macOS</sub>

```objc
extern NSString * const WebViewDidChangeSelectionNotification;
```

## Discussion

The notification object is the WebView that changed its typing selection. This notification does not contain a `userInfo` dictionary.

## See Also

### Notifications

- [WebViewDidBeginEditingNotification](webviewdidbegineditingnotification.md) — Posted when a web view begins any operation that changes its contents in response to user editing. _(deprecated)_
- [WebViewDidChangeNotification](webviewdidchangenotification.md) — Posted when a web view performs any operation that changes its contents in response to user editing. _(deprecated)_
- [WebViewDidChangeTypingStyleNotification](webviewdidchangetypingstylenotification.md) — Posted when a web view changes its typing style. _(deprecated)_
- [WebViewDidEndEditingNotification](webviewdidendeditingnotification.md) — Posted when a web view ends any operation that changes its contents in response to user editing. _(deprecated)_
- [WebViewProgressEstimateChangedNotification](webviewprogressestimatechangednotification.md) — Posted by a WebView object when the estimated progress value of a load changes. _(deprecated)_
- [WebViewProgressFinishedNotification](webviewprogressfinishednotification.md) — Posted by a WebView object when the load has finished. _(deprecated)_
- [WebViewProgressStartedNotification](webviewprogressstartednotification.md) — Posted by a WebView object when a load begins, including a load that is initiated in a subframe. _(deprecated)_
