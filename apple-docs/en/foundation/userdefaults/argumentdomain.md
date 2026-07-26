---
title: argumentDomain
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/userdefaults/argumentdomain
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/argumentdomain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/argumentdomain.json'
content_hash: 'sha256:1c2ad804b57feead'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# argumentDomain

<sub>Type Property</sub>

The identifier for the domain that contains command-line settings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let argumentDomain: String
```

## Discussion

When someone launches your app from Xcode or the command-line, they can override setting values using command-line arguments. The defaults system stores those overrides in this domain, which is volatile and resets with each app launch. Values in this domain override most other domains, including your app-specific settings.

To specify custom settings from the command line, add the `-default` parameter to your command-line invocation followed by a _key=value_ string with the key and value you want to set.

## See Also

### Getting the domain names

- [NSGlobalDomain](globaldomain.md) — The identifier for the domain that contains system-specified settings for all apps.
- [NSRegistrationDomain](registrationdomain.md) — The identifier for the domain that contains your app’s registered default values.
- [volatileDomainNames](volatiledomainnames.md) — An array of identifiers for the volatile domains associated with the current object.
