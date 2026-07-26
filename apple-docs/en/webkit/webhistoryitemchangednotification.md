---
title: WebHistoryItemChangedNotification
framework: WebKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.3+（10.14 起废弃）]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/webkit/webhistoryitemchangednotification
source_url: 'https://developer.apple.com/documentation/webkit/webhistoryitemchangednotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/webkit/webhistoryitemchangednotification.json'
content_hash: 'sha256:29caaf40cb73734e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WebKit](../webkit.md)

# WebHistoryItemChangedNotification

<sub>Global Variable</sub>

Posted by a WebHistoryItem object when the value of the history item’s title, alternate title, URL strings, or last visited interval changes.

<sub>macOS</sub>

```objc
extern NSString * WebHistoryItemChangedNotification;
```

## Discussion

This notification does not contain a `userInfo` dictionary.

## See Also

### Related Documentation

- [alternateTitle](webhistoryitem/alternatetitle.md) — An alternate title that may be used in place of the receiver’s page title. _(deprecated)_

### Notifications

- [WebHistoryAllItemsRemovedNotification](webhistoryallitemsremovednotification.md) — Posted when all history items have been removed from the web history. _(deprecated)_
- [WebHistoryItemsAddedNotification](webhistoryitemsaddednotification.md) — Posted when history items have been added to a web history. _(deprecated)_
- [WebHistoryItemsRemovedNotification](webhistoryitemsremovednotification.md) — Posted when items have been removed from the web history. _(deprecated)_
- [WebHistoryLoadedNotification](webhistoryloadednotification.md) — Posted when web history items have been loaded from a URL. _(deprecated)_
- [WebHistorySavedNotification](webhistorysavednotification.md) — Posted when web history items have been saved to a URL. _(deprecated)_
