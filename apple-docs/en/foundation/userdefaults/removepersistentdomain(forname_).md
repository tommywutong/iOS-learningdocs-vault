---
title: 'removePersistentDomain(forName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/userdefaults/removepersistentdomain(forname:)'
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/removepersistentdomain(forname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/removepersistentdomain%28forname%3A%29.json'
content_hash: 'sha256:5b2310a84010a7cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# removePersistentDomain(forName:)

<sub>Instance Method</sub>

Removes the keys and values from the specified persistent domain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removePersistentDomain(forName domainName: String)
```

## Parameters

- `domainName` — The name of the domain to clear. If you specify the identifier for the argument or registration domain, this method throws an exception.

## Discussion

This method removes all of the keys and values from the specified domain. After clearing the domain’s contents, this method generates a [NSUserDefaultsDidChangeNotification](didchangenotification.md) for registered observers.

## See Also

### Managing domain-specific values

- [- persistentDomainForName:](<persistentdomain(forname_).md>) — Retrieves the settings from the specified persistent domain.
- [- setPersistentDomain:forName:](<setpersistentdomain(__forname_).md>) — Replaces the keys and values in the specified domain with the new keys and values you supply.
- [- volatileDomainForName:](<volatiledomain(forname_).md>) — Retrieves the settings from the specified volatile domain.
- [- setVolatileDomain:forName:](<setvolatiledomain(__forname_).md>) — Replaces the keys and values in the specified domain with the new keys and values you supply.
- [- removeVolatileDomainForName:](<removevolatiledomain(forname_).md>) — Removes the keys and values from the specified volatile domain.
