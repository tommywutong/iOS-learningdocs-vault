---
title: WebViewDidChangeNotification
framework: WebKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.3+（10.14 起废弃）]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/webkit/webviewdidchangenotification
source_url: 'https://developer.apple.com/documentation/webkit/webviewdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/webkit/webviewdidchangenotification.json'
content_hash: 'sha256:0fdf4ea004c13a71'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WebKit](../webkit.md)

# WebViewDidChangeNotification

<sub>Global Variable</sub>

Posted when a web view performs any operation that changes its contents in response to user editing.

<sub>macOS</sub>

```objc
extern NSString * const WebViewDidChangeNotification;
```

## Discussion

The notification object is the WebView object that the user is editing. This notification does not contain a `userInfo` dictionary.

## See Also

### Notifications

- [WebViewDidBeginEditingNotification](webviewdidbegineditingnotification.md) — Posted when a web view begins any operation that changes its contents in response to user editing. _(deprecated)_
- [WebViewDidChangeSelectionNotification](webviewdidchangeselectionnotification.md) — Posted when a web view changes its typing selection. _(deprecated)_
- [WebViewDidChangeTypingStyleNotification](webviewdidchangetypingstylenotification.md) — Posted when a web view changes its typing style. _(deprecated)_
- [WebViewDidEndEditingNotification](webviewdidendeditingnotification.md) — Posted when a web view ends any operation that changes its contents in response to user editing. _(deprecated)_
- [WebViewProgressEstimateChangedNotification](webviewprogressestimatechangednotification.md) — Posted by a WebView object when the estimated progress value of a load changes. _(deprecated)_
- [WebViewProgressFinishedNotification](webviewprogressfinishednotification.md) — Posted by a WebView object when the load has finished. _(deprecated)_
- [WebViewProgressStartedNotification](webviewprogressstartednotification.md) — Posted by a WebView object when a load begins, including a load that is initiated in a subframe. _(deprecated)_
