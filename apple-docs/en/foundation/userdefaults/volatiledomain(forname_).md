---
title: 'volatileDomain(forName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/userdefaults/volatiledomain(forname:)'
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/volatiledomain(forname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/volatiledomain%28forname%3A%29.json'
content_hash: 'sha256:71b4cd29d4f98994'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# volatileDomain(forName:)

<sub>Instance Method</sub>

Retrieves the settings from the specified volatile domain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func volatileDomain(forName domainName: String) -> [String : Any]
```

## Parameters

- `domainName` — The name of the volatile domain. For example, specify the [NSArgumentDomain](argumentdomain.md) identifier to retrieve the command-line settings.

## Return Value

A dictionary containing the keys and values from the specified domain. If the domain doesn’t contain any keys, or is a persistent domain, this method returns `nil`.

## Discussion

This method retrieves only the keys and values from the specified domain. It doesn’t retrieve keys from other persistent or volatile domains.

## See Also

### Managing domain-specific values

- [- persistentDomainForName:](<persistentdomain(forname_).md>) — Retrieves the settings from the specified persistent domain.
- [- setPersistentDomain:forName:](<setpersistentdomain(__forname_).md>) — Replaces the keys and values in the specified domain with the new keys and values you supply.
- [- setVolatileDomain:forName:](<setvolatiledomain(__forname_).md>) — Replaces the keys and values in the specified domain with the new keys and values you supply.
- [- removePersistentDomainForName:](<removepersistentdomain(forname_).md>) — Removes the keys and values from the specified persistent domain.
- [- removeVolatileDomainForName:](<removevolatiledomain(forname_).md>) — Removes the keys and values from the specified volatile domain.
