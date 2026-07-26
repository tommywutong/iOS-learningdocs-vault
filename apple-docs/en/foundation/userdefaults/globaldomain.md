---
title: globalDomain
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/userdefaults/globaldomain
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/globaldomain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/globaldomain.json'
content_hash: 'sha256:5c7090ebd1a06709'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# globalDomain

<sub>Type Property</sub>

The identifier for the domain that contains system-specified settings for all apps.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let globalDomain: String
```

## Discussion

The system populates this domain with information that’s relevant to all apps. For example, this domain contains the current language settings for the device. You can read values from this domain, but don’t write your own settings to it.

## See Also

### Getting the domain names

- [NSArgumentDomain](argumentdomain.md) — The identifier for the domain that contains command-line settings.
- [NSRegistrationDomain](registrationdomain.md) — The identifier for the domain that contains your app’s registered default values.
- [volatileDomainNames](volatiledomainnames.md) — An array of identifiers for the volatile domains associated with the current object.
