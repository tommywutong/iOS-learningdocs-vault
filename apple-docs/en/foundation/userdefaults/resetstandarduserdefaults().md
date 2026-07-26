---
title: resetStandardUserDefaults()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/userdefaults/resetstandarduserdefaults()
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/resetstandarduserdefaults()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/resetstandarduserdefaults%28%29.json'
content_hash: 'sha256:e682c3f37bce04f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# resetStandardUserDefaults()

<sub>Type Method</sub>

This method has no effect and shouldn’t be used.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func resetStandardUserDefaults()
```

## See Also

### Deprecated

- [- initWithUser:](<init(user_).md>) — Creates a user defaults object initialized with the defaults for the specified user account. _(deprecated)_
- [- synchronize](<synchronize().md>) — Waits for any pending asynchronous updates to the defaults database and returns; this method is unnecessary and shouldn’t be used.
- [- persistentDomainNames](<persistentdomainnames().md>) — Returns an array of the current persistent domain names. _(deprecated)_
- [NSUbiquitousUserDefaultsCompletedInitialSyncNotification](completedinitialcloudsyncnotification.md) — Posted when ubiquitous defaults finish downloading data, either the first time a device is connected to an iCloud account or when a user switches their primary iCloud account. _(deprecated)_
- [NSUbiquitousUserDefaultsDidChangeAccountsNotification](didchangecloudaccountsnotification.md) — Posted when the user changes the primary iCloud account. _(deprecated)_
- [NSUbiquitousUserDefaultsNoCloudAccountNotification](nocloudaccountnotification.md) — Posted when a cloud default is set, but no iCloud user is logged in. _(deprecated)_
- [Language-Dependent Information Constants](../language-dependent-information-constants.md) — These constants are deprecated and shouldn’t be used.
