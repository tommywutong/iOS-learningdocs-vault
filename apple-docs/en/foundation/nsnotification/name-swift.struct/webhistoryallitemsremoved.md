---
title: WebHistoryAllItemsRemoved
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.3+（10.14 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsnotification/name-swift.struct/webhistoryallitemsremoved
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/webhistoryallitemsremoved'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/webhistoryallitemsremoved.json'
content_hash: 'sha256:63d8f97782cc110f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# WebHistoryAllItemsRemoved

<sub>Type Property</sub>

Posted when all history items have been removed from the web history.

<sub>macOS</sub>

```swift
static let WebHistoryAllItemsRemoved: NSNotification.Name
```

## Discussion

The notification object is the web history from which the history items were removed. The `userInfo` dictionary contains the following information:

| Key | Value |
|---|---|
| @“WebHistoryItemsKey” | An [NSArray](../../nsarray.md) object containing the removed items. |

## See Also

### Related Documentation

- [removeAllItems()](<../../../webkit/webhistory/removeallitems().md>) — Removes all items from the web history. _(deprecated)_

### WebKit

- [WebHistoryItemChanged](webhistoryitemchanged.md) — Posted by a WebHistoryItem object when the value of the history item’s title, alternate title, URL strings, or last visited interval changes. _(deprecated)_
- [WebHistoryItemsAdded](webhistoryitemsadded.md) — Posted when history items have been added to a web history. _(deprecated)_
- [WebHistoryItemsRemoved](webhistoryitemsremoved.md) — Posted when items have been removed from the web history. _(deprecated)_
- [WebHistoryLoaded](webhistoryloaded.md) — Posted when web history items have been loaded from a URL. _(deprecated)_
- [WebHistorySaved](webhistorysaved.md) — Posted when web history items have been saved to a URL. _(deprecated)_
- [WebPreferencesChanged](webpreferenceschanged.md) — Posted when the web preference settings are changed. _(deprecated)_
- [WebViewDidBeginEditing](webviewdidbeginediting.md) — Posted when a web view begins any operation that changes its contents in response to user editing. _(deprecated)_
- [WebViewDidChange](webviewdidchange.md) — Posted when a web view performs any operation that changes its contents in response to user editing. _(deprecated)_
- [WebViewDidChangeSelection](webviewdidchangeselection.md) — Posted when a web view changes its typing selection. _(deprecated)_
- [WebViewDidChangeTypingStyle](webviewdidchangetypingstyle.md) — Posted when a web view changes its typing style. _(deprecated)_
- [WebViewDidEndEditing](webviewdidendediting.md) — Posted when a web view ends any operation that changes its contents in response to user editing. _(deprecated)_
- [WebViewProgressEstimateChanged](webviewprogressestimatechanged.md) — Posted by a WebView object when the estimated progress value of a load changes. _(deprecated)_
- [WebViewProgressFinished](webviewprogressfinished.md) — Posted by a WebView object when the load has finished. _(deprecated)_
- [WebViewProgressStarted](webviewprogressstarted.md) — Posted by a WebView object when a load begins, including a load that is initiated in a subframe. _(deprecated)_
