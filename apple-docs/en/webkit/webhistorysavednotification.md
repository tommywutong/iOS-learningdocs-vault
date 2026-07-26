---
title: WebHistorySavedNotification
framework: WebKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.3+（10.14 起废弃）]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/webkit/webhistorysavednotification
source_url: 'https://developer.apple.com/documentation/webkit/webhistorysavednotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/webkit/webhistorysavednotification.json'
content_hash: 'sha256:4dac8929be9da68a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WebKit](../webkit.md)

# WebHistorySavedNotification

<sub>Global Variable</sub>

Posted when web history items have been saved to a URL.

<sub>macOS</sub>

```objc
extern NSString * WebHistorySavedNotification;
```

## Discussion

The notification object is the web history that saved the history items. This notification does not contain a `userInfo` dictionary.

## See Also

### Related Documentation

- [- saveToURL:error:](<webhistory/save(to_).md>) — Saves the web history to the specified file. _(deprecated)_

### Notifications

- [WebHistoryAllItemsRemovedNotification](webhistoryallitemsremovednotification.md) — Posted when all history items have been removed from the web history. _(deprecated)_
- [WebHistoryItemChangedNotification](webhistoryitemchangednotification.md) — Posted by a WebHistoryItem object when the value of the history item’s title, alternate title, URL strings, or last visited interval changes. _(deprecated)_
- [WebHistoryItemsAddedNotification](webhistoryitemsaddednotification.md) — Posted when history items have been added to a web history. _(deprecated)_
- [WebHistoryItemsRemovedNotification](webhistoryitemsremovednotification.md) — Posted when items have been removed from the web history. _(deprecated)_
- [WebHistoryLoadedNotification](webhistoryloadednotification.md) — Posted when web history items have been loaded from a URL. _(deprecated)_
