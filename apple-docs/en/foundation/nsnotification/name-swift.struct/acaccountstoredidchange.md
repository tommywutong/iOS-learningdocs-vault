---
title: ACAccountStoreDidChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+（14.0 起废弃）, iPadOS 5.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, macOS 10.8+（11.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsnotification/name-swift.struct/acaccountstoredidchange
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/acaccountstoredidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/acaccountstoredidchange.json'
content_hash: 'sha256:0075495a49ebe550'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# ACAccountStoreDidChange

<sub>Type Property</sub>

Posted when the accounts managed by this account store changed in the database.

> [!warning] Deprecated
> Public notification deprecated. Internal clients, see private header for replacement

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
static let ACAccountStoreDidChange: NSNotification.Name
```

## Discussion

The notification sent if an account is saved or removed locally or externally. If you receive this notification, you should refetch all account objects.

There’s no `userInfo` dictionary associated with this notification.
