---
title: TVTopShelfItemsDidChangeNotification
framework: TV Services
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [tvOS 9.0+（13.0 起废弃）]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/tvservices/tvtopshelfitemsdidchangenotification
source_url: 'https://developer.apple.com/documentation/tvservices/tvtopshelfitemsdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/tvservices/tvtopshelfitemsdidchangenotification.json'
content_hash: 'sha256:8d5201632998773f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [TV Services](../tvservices.md)

# TVTopShelfItemsDidChangeNotification

<sub>Global Variable</sub>

A notification to post when your app’s Top Shelf content has changed.

<sub>tvOS</sub>

```objc
extern NSString * const TVTopShelfItemsDidChangeNotification;
```

## Discussion

When the content has changed, post a new notification using the default notification center (`[NSNotificationCenter defaultCenter]`). At some point in the future, the system will fetch the new data from your extension. The notification’s parameters are ignored and should be `nil`.
