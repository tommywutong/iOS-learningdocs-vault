---
title: registrationDomain
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/userdefaults/registrationdomain
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/registrationdomain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/registrationdomain.json'
content_hash: 'sha256:3b217e77e2628f18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# registrationDomain

<sub>Type Property</sub>

The identifier for the domain that contains your app’s registered default values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let registrationDomain: String
```

## Discussion

The settings in this domain represent default values you want to use for its settings. To register your app’s default settings, call the [- registerDefaults:](<register(defaults_).md>) method shortly after launch.

## See Also

### Getting the domain names

- [NSArgumentDomain](argumentdomain.md) — The identifier for the domain that contains command-line settings.
- [NSGlobalDomain](globaldomain.md) — The identifier for the domain that contains system-specified settings for all apps.
- [volatileDomainNames](volatiledomainnames.md) — An array of identifiers for the volatile domains associated with the current object.
