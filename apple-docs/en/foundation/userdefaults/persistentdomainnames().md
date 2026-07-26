---
title: persistentDomainNames()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（7.0 起废弃）, iPadOS 2.0+（7.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/userdefaults/persistentdomainnames()
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/persistentdomainnames()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/persistentdomainnames%28%29.json'
content_hash: 'sha256:72dd2672d123b370'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# persistentDomainNames()

<sub>Instance Method</sub>

Returns an array of the current persistent domain names.

> [!warning] Deprecated
> Instead of using this method, you should track the domains you add if you want to later retrieve them with [- persistentDomainForName:](<persistentdomain(forname_).md>).

<sub>tvOS, visionOS, watchOS</sub>

```swift
func persistentDomainNames() -> [Any]
```

## Return Value

An array of `NSString` objects containing the domain names.

## Discussion

You can get the keys and values for each domain by passing the returned domain names to the  [- persistentDomainForName:](<persistentdomain(forname_).md>) method.

## See Also

### Deprecated

- [- initWithUser:](<init(user_).md>) — Creates a user defaults object initialized with the defaults for the specified user account. _(deprecated)_
- [- synchronize](<synchronize().md>) — Waits for any pending asynchronous updates to the defaults database and returns; this method is unnecessary and shouldn’t be used.
- [+ resetStandardUserDefaults](<resetstandarduserdefaults().md>) — This method has no effect and shouldn’t be used.
- [NSUbiquitousUserDefaultsCompletedInitialSyncNotification](completedinitialcloudsyncnotification.md) — Posted when ubiquitous defaults finish downloading data, either the first time a device is connected to an iCloud account or when a user switches their primary iCloud account. _(deprecated)_
- [NSUbiquitousUserDefaultsDidChangeAccountsNotification](didchangecloudaccountsnotification.md) — Posted when the user changes the primary iCloud account. _(deprecated)_
- [NSUbiquitousUserDefaultsNoCloudAccountNotification](nocloudaccountnotification.md) — Posted when a cloud default is set, but no iCloud user is logged in. _(deprecated)_
- [Language-Dependent Information Constants](../language-dependent-information-constants.md) — These constants are deprecated and shouldn’t be used.
