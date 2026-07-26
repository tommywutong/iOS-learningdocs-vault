---
title: WebViewDidChangeTypingStyleNotification
framework: WebKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.3+（10.14 起废弃）]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/webkit/webviewdidchangetypingstylenotification
source_url: 'https://developer.apple.com/documentation/webkit/webviewdidchangetypingstylenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/webkit/webviewdidchangetypingstylenotification.json'
content_hash: 'sha256:287daa1ee667a7fc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WebKit](../webkit.md)

# WebViewDidChangeTypingStyleNotification

<sub>Global Variable</sub>

Posted when a web view changes its typing style.

<sub>macOS</sub>

```objc
extern NSString * const WebViewDidChangeTypingStyleNotification;
```

## Discussion

The notification object is the WebView that changed its typing style. This notification does not contain a `userInfo` dictionary.

## See Also

### Related Documentation

- [typingStyle](webview-swift.class/typingstyle.md) — The receiver’s CSS typing style.

### Notifications

- [WebViewDidBeginEditingNotification](webviewdidbegineditingnotification.md) — Posted when a web view begins any operation that changes its contents in response to user editing. _(deprecated)_
- [WebViewDidChangeNotification](webviewdidchangenotification.md) — Posted when a web view performs any operation that changes its contents in response to user editing. _(deprecated)_
- [WebViewDidChangeSelectionNotification](webviewdidchangeselectionnotification.md) — Posted when a web view changes its typing selection. _(deprecated)_
- [WebViewDidEndEditingNotification](webviewdidendeditingnotification.md) — Posted when a web view ends any operation that changes its contents in response to user editing. _(deprecated)_
- [WebViewProgressEstimateChangedNotification](webviewprogressestimatechangednotification.md) — Posted by a WebView object when the estimated progress value of a load changes. _(deprecated)_
- [WebViewProgressFinishedNotification](webviewprogressfinishednotification.md) — Posted by a WebView object when the load has finished. _(deprecated)_
- [WebViewProgressStartedNotification](webviewprogressstartednotification.md) — Posted by a WebView object when a load begins, including a load that is initiated in a subframe. _(deprecated)_
