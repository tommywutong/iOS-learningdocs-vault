---
title: 'persistentDomain(forName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/userdefaults/persistentdomain(forname:)'
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/persistentdomain(forname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/persistentdomain%28forname%3A%29.json'
content_hash: 'sha256:c90ce61949bd1409'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# persistentDomain(forName:)

<sub>Instance Method</sub>

Retrieves the settings from the specified persistent domain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func persistentDomain(forName domainName: String) -> [String : Any]?
```

## Parameters

- `domainName` — The name of the persistent domain. Specify your app’s bundle identifier to retrieve any app-specific keys. Specify the [NSGlobalDomain](globaldomain.md) identifier to retrieve keys in the global domain.

## Return Value

A dictionary containing the keys and values from the specified domain. If the domain doesn’t contain any keys, or is a volatile domain, the method returns `nil`.

## Discussion

This method retrieves only the keys and values from the specified domain. It doesn’t retrieve keys from other persistent or volatile domains.

## See Also

### Managing domain-specific values

- [- setPersistentDomain:forName:](<setpersistentdomain(__forname_).md>) — Replaces the keys and values in the specified domain with the new keys and values you supply.
- [- volatileDomainForName:](<volatiledomain(forname_).md>) — Retrieves the settings from the specified volatile domain.
- [- setVolatileDomain:forName:](<setvolatiledomain(__forname_).md>) — Replaces the keys and values in the specified domain with the new keys and values you supply.
- [- removePersistentDomainForName:](<removepersistentdomain(forname_).md>) — Removes the keys and values from the specified persistent domain.
- [- removeVolatileDomainForName:](<removevolatiledomain(forname_).md>) — Removes the keys and values from the specified volatile domain.
