---
title: WebHistoryItemsRemovedNotification
framework: WebKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.3+（10.14 起废弃）]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/webkit/webhistoryitemsremovednotification
source_url: 'https://developer.apple.com/documentation/webkit/webhistoryitemsremovednotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/webkit/webhistoryitemsremovednotification.json'
content_hash: 'sha256:30ec7f6096fff2bb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WebKit](../webkit.md)

# WebHistoryItemsRemovedNotification

<sub>Global Variable</sub>

Posted when items have been removed from the web history.

<sub>macOS</sub>

```objc
extern NSString * WebHistoryItemsRemovedNotification;
```

## Discussion

The notification object is the web history from which the history items were removed. The `userInfo` dictionary contains the following information:

| Key | Value |
|---|---|
| @“WebHistoryItemsKey” | An [NSArray](../foundation/nsarray.md) object containing the removed items. |

## See Also

### Related Documentation

- [- removeItems:](<webhistory/removeitems(__).md>) — Removes the specified items from the web history. _(deprecated)_

### Notifications

- [WebHistoryAllItemsRemovedNotification](webhistoryallitemsremovednotification.md) — Posted when all history items have been removed from the web history. _(deprecated)_
- [WebHistoryItemChangedNotification](webhistoryitemchangednotification.md) — Posted by a WebHistoryItem object when the value of the history item’s title, alternate title, URL strings, or last visited interval changes. _(deprecated)_
- [WebHistoryItemsAddedNotification](webhistoryitemsaddednotification.md) — Posted when history items have been added to a web history. _(deprecated)_
- [WebHistoryLoadedNotification](webhistoryloadednotification.md) — Posted when web history items have been loaded from a URL. _(deprecated)_
- [WebHistorySavedNotification](webhistorysavednotification.md) — Posted when web history items have been saved to a URL. _(deprecated)_
