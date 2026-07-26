---
title: 'setVolatileDomain(_:forName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/userdefaults/setvolatiledomain(_:forname:)'
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/setvolatiledomain(_:forname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/setvolatiledomain%28_%3Aforname%3A%29.json'
content_hash: 'sha256:3072d7790a0c7981'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# setVolatileDomain(_:forName:)

<sub>Instance Method</sub>

Replaces the keys and values in the specified domain with the new keys and values you supply.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setVolatileDomain(_ domain: [String : Any], forName domainName: String)
```

## Parameters

- `domain` — A dictionary of keys and values to assign to the domain.

- `domainName` — The name of the domain to update.

## Discussion

This method removes the existing keys from the specified domain and then adds the new keys you provide. After updating the keys, this method generates a [NSUserDefaultsDidChangeNotification](didchangenotification.md) for registered observers.

## See Also

### Managing domain-specific values

- [- persistentDomainForName:](<persistentdomain(forname_).md>) — Retrieves the settings from the specified persistent domain.
- [- setPersistentDomain:forName:](<setpersistentdomain(__forname_).md>) — Replaces the keys and values in the specified domain with the new keys and values you supply.
- [- volatileDomainForName:](<volatiledomain(forname_).md>) — Retrieves the settings from the specified volatile domain.
- [- removePersistentDomainForName:](<removepersistentdomain(forname_).md>) — Removes the keys and values from the specified persistent domain.
- [- removeVolatileDomainForName:](<removevolatiledomain(forname_).md>) — Removes the keys and values from the specified volatile domain.
