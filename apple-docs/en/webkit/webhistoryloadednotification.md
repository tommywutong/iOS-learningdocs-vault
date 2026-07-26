---
title: WebHistoryLoadedNotification
framework: WebKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.3+（10.14 起废弃）]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/webkit/webhistoryloadednotification
source_url: 'https://developer.apple.com/documentation/webkit/webhistoryloadednotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/webkit/webhistoryloadednotification.json'
content_hash: 'sha256:d40188726a3d54f6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WebKit](../webkit.md)

# WebHistoryLoadedNotification

<sub>Global Variable</sub>

Posted when web history items have been loaded from a URL.

<sub>macOS</sub>

```objc
extern NSString * WebHistoryLoadedNotification;
```

## Discussion

The notification object is the web history that loaded the history items. This notification does not contain a `userInfo` dictionary.

## See Also

### Related Documentation

- [- loadFromURL:error:](<webhistory/load(from_).md>) — Loads the contents of the specified web history file. _(deprecated)_

### Notifications

- [WebHistoryAllItemsRemovedNotification](webhistoryallitemsremovednotification.md) — Posted when all history items have been removed from the web history. _(deprecated)_
- [WebHistoryItemChangedNotification](webhistoryitemchangednotification.md) — Posted by a WebHistoryItem object when the value of the history item’s title, alternate title, URL strings, or last visited interval changes. _(deprecated)_
- [WebHistoryItemsAddedNotification](webhistoryitemsaddednotification.md) — Posted when history items have been added to a web history. _(deprecated)_
- [WebHistoryItemsRemovedNotification](webhistoryitemsremovednotification.md) — Posted when items have been removed from the web history. _(deprecated)_
- [WebHistorySavedNotification](webhistorysavednotification.md) — Posted when web history items have been saved to a URL. _(deprecated)_
