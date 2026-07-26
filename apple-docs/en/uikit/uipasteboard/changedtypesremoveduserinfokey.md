---
title: changedTypesRemovedUserInfoKey
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/changedtypesremoveduserinfokey
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/changedtypesremoveduserinfokey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/changedtypesremoveduserinfokey.json'
content_hash: 'sha256:4fbdd2d0521acbf0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# changedTypesRemovedUserInfoKey

<sub>Type Property</sub>

With the notification named [UIPasteboardChangedNotification](changednotification.md), use this key to access the removed representation types. These types are stored as an array in the notification’s `userInfo` dictionary.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated class let changedTypesRemovedUserInfoKey: String
```

## See Also

### Constants

- [UIPasteboardChangedTypesAddedKey](changedtypesaddeduserinfokey.md) — With the notification named [UIPasteboardChangedNotification](changednotification.md), use this key to access the added representation types. These types are stored as an array in the notification’s `userInfo` dictionary.
