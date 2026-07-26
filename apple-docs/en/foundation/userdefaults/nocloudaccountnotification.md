---
title: noCloudAccountNotification
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.3+（9.3 起废弃）, iPadOS 9.3+（9.3 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/userdefaults/nocloudaccountnotification
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/nocloudaccountnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/nocloudaccountnotification.json'
content_hash: 'sha256:3d698894ccb60cb6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# noCloudAccountNotification

<sub>Type Property</sub>

Posted when a cloud default is set, but no iCloud user is logged in.

> [!warning] Deprecated
> Notification is never posted

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class let noCloudAccountNotification: NSNotification.Name
```

## Discussion

This notification is posted to the default notification center on the main queue.

This notification doesn’t necessarily indicate an error; ubiquitous defaults set when no iCloud user is logged in are uploaded the next time one is available if configured to do so.

## See Also

### Deprecated

- [- initWithUser:](<init(user_).md>) — Creates a user defaults object initialized with the defaults for the specified user account. _(deprecated)_
- [- synchronize](<synchronize().md>) — Waits for any pending asynchronous updates to the defaults database and returns; this method is unnecessary and shouldn’t be used.
- [+ resetStandardUserDefaults](<resetstandarduserdefaults().md>) — This method has no effect and shouldn’t be used.
- [- persistentDomainNames](<persistentdomainnames().md>) — Returns an array of the current persistent domain names. _(deprecated)_
- [NSUbiquitousUserDefaultsCompletedInitialSyncNotification](completedinitialcloudsyncnotification.md) — Posted when ubiquitous defaults finish downloading data, either the first time a device is connected to an iCloud account or when a user switches their primary iCloud account. _(deprecated)_
- [NSUbiquitousUserDefaultsDidChangeAccountsNotification](didchangecloudaccountsnotification.md) — Posted when the user changes the primary iCloud account. _(deprecated)_
- [Language-Dependent Information Constants](../language-dependent-information-constants.md) — These constants are deprecated and shouldn’t be used.
