---
title: ACAccountStoreDidChangeNotification
framework: Accounts
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+（14.0 起废弃）, iPadOS 5.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, macOS 10.8+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/accounts/acaccountstoredidchangenotification
source_url: 'https://developer.apple.com/documentation/accounts/acaccountstoredidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/accounts/acaccountstoredidchangenotification.json'
content_hash: 'sha256:90733926fcdc6dc3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Accounts](../accounts.md)

# ACAccountStoreDidChangeNotification

<sub>Global Variable</sub>

Posted when the accounts managed by this account store changed in the database.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```objc
extern NSString * const ACAccountStoreDidChangeNotification;
```

## Discussion

The notification sent if an account is saved or removed locally or externally. If you receive this notification, you should refetch all account objects.

There’s no `userInfo` dictionary associated with this notification.
