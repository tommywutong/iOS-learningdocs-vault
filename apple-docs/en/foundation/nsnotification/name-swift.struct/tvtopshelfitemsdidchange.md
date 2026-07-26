---
title: TVTopShelfItemsDidChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [tvOS 9.0+（13.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsnotification/name-swift.struct/tvtopshelfitemsdidchange
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/tvtopshelfitemsdidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/tvtopshelfitemsdidchange.json'
content_hash: 'sha256:58390b2a2de5d1ea'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# TVTopShelfItemsDidChange

<sub>Type Property</sub>

A notification to post when your app’s Top Shelf content has changed.

> [!warning] Deprecated
> TVTopShelfItemsDidChangeNotification has been replaced by [TVTopShelfContentProvider topShelfContentDidChange]

<sub>tvOS</sub>

```swift
static let TVTopShelfItemsDidChange: NSNotification.Name
```

## Discussion

When the content has changed, post a new notification using the default notification center (`[NSNotificationCenter defaultCenter]`). At some point in the future, the system will fetch the new data from your extension. The notification’s parameters are ignored and should be `nil`.
