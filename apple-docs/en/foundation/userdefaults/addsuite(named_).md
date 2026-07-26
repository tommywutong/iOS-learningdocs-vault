---
title: 'addSuite(named:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/userdefaults/addsuite(named:)'
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/addsuite(named:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/addsuite%28named%3A%29.json'
content_hash: 'sha256:40a6a35c82ceea11'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# addSuite(named:)

<sub>Instance Method</sub>

Inserts settings for the specified domain into the search list of the current object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addSuite(named suiteName: String)
```

## Parameters

- `suiteName` — The bundle identifier for the domain you want to add. You don’t need to specify a bundle identifier for another app. Instead, you might specify the app group identifier you use to share data between multiple apps or between your app and an app extension. Don’t specify your app’s bundle identifier or the [NSGlobalDomain](globaldomain.md) identifier in this parameter.

## Discussion

This method inserts the domain for your custom suite of settings after the app domain and before the global domain. This arrangement causes the `UserDefaults` object to return your app-specific settings first, followed by settings from the specified suite. If you call this method multiple times, the `UserDefaults` object searches your suites in the order you added them.

This method doesn’t affect the destination for write operations. If you want to write settings to a custom suite, use the [- initWithSuiteName:](<init(suitename_).md>) initializer to construct a `UserDefaults` object specifically for that suite.

> [!important] Important
> An app that accesses settings in a suite must also have the [App Groups entitlement](../../bundleresources/entitlements/com.apple.security.application-groups.md).

## See Also

### Adding and removing search domains

- [- removeSuiteNamed:](<removesuite(named_).md>) — Removes the specified domain from the search list of the current object.
