---
title: 'init(user:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+（7.0 起废弃）, iPadOS 2.0+（7.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/userdefaults/init(user:)'
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/init(user:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/init%28user%3A%29.json'
content_hash: 'sha256:7aaafe1c4fb12dca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# init(user:)

<sub>Initializer</sub>

Creates a user defaults object initialized with the defaults for the specified user account.

> [!warning] Deprecated
> This method was never implemented to return anything but the defaults for the current user. Use [standardUserDefaults](standard.md) instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
convenience init?(user username: String)
```

## Parameters

- `username` — The name of the user account.

## Return Value

An initialized [UserDefaults](../userdefaults.md) object whose argument and registration domains are already set up. If the current user does not have access to the specified user account, this method returns `nil`.

## Discussion

This method doesn’t put anything in the search list. Invoke it only if you’ve allocated your own [UserDefaults](../userdefaults.md) instance instead of using the shared one.

You do not normally use this method to initialize an instance of [UserDefaults](../userdefaults.md). Applications used by a superuser might use this method to update the defaults databases for a number of users. The user who started the application must have appropriate access (read, write, or both) to the defaults database of the new user, or this method returns `nil`.

### Special Considerations

This method was never implemented to do anything except return the defaults for the current user.

## See Also

### Related Documentation

- [standardUserDefaults](standard.md) — The shared defaults object for the current app.

### Deprecated

- [- synchronize](<synchronize().md>) — Waits for any pending asynchronous updates to the defaults database and returns; this method is unnecessary and shouldn’t be used.
- [+ resetStandardUserDefaults](<resetstandarduserdefaults().md>) — This method has no effect and shouldn’t be used.
- [- persistentDomainNames](<persistentdomainnames().md>) — Returns an array of the current persistent domain names. _(deprecated)_
- [NSUbiquitousUserDefaultsCompletedInitialSyncNotification](completedinitialcloudsyncnotification.md) — Posted when ubiquitous defaults finish downloading data, either the first time a device is connected to an iCloud account or when a user switches their primary iCloud account. _(deprecated)_
- [NSUbiquitousUserDefaultsDidChangeAccountsNotification](didchangecloudaccountsnotification.md) — Posted when the user changes the primary iCloud account. _(deprecated)_
- [NSUbiquitousUserDefaultsNoCloudAccountNotification](nocloudaccountnotification.md) — Posted when a cloud default is set, but no iCloud user is logged in. _(deprecated)_
- [Language-Dependent Information Constants](../language-dependent-information-constants.md) — These constants are deprecated and shouldn’t be used.
