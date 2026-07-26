---
title: WebHistoryItemsAddedNotification
framework: WebKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.3+（10.14 起废弃）]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/webkit/webhistoryitemsaddednotification
source_url: 'https://developer.apple.com/documentation/webkit/webhistoryitemsaddednotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/webkit/webhistoryitemsaddednotification.json'
content_hash: 'sha256:341d08effef292c4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WebKit](../webkit.md)

# WebHistoryItemsAddedNotification

<sub>Global Variable</sub>

Posted when history items have been added to a web history.

<sub>macOS</sub>

```objc
extern NSString * WebHistoryItemsAddedNotification;
```

## Discussion

The notification object is the web history to which the items were added. The `userInfo` dictionary contains the following information:

| Key | Value |
|---|---|
| @“WebHistoryItemsKey” | An [NSArray](../foundation/nsarray.md) object containing the added items. |

## See Also

### Related Documentation

- [- addItems:](<webhistory/additems(__).md>) — Inserts or updates the specified items in the web history. _(deprecated)_

### Notifications

- [WebHistoryAllItemsRemovedNotification](webhistoryallitemsremovednotification.md) — Posted when all history items have been removed from the web history. _(deprecated)_
- [WebHistoryItemChangedNotification](webhistoryitemchangednotification.md) — Posted by a WebHistoryItem object when the value of the history item’s title, alternate title, URL strings, or last visited interval changes. _(deprecated)_
- [WebHistoryItemsRemovedNotification](webhistoryitemsremovednotification.md) — Posted when items have been removed from the web history. _(deprecated)_
- [WebHistoryLoadedNotification](webhistoryloadednotification.md) — Posted when web history items have been loaded from a URL. _(deprecated)_
- [WebHistorySavedNotification](webhistorysavednotification.md) — Posted when web history items have been saved to a URL. _(deprecated)_
