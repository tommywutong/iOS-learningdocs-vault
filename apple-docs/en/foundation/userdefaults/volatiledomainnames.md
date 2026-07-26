---
title: volatileDomainNames
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/userdefaults/volatiledomainnames
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/volatiledomainnames'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/volatiledomainnames.json'
content_hash: 'sha256:a8a549b9547665bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# volatileDomainNames

<sub>Instance Property</sub>

An array of identifiers for the volatile domains associated with the current object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var volatileDomainNames: [String] { get }
```

## Discussion

Each string in the array corresponds to one of the volatile domains this `UserDefaults` object searches. To get the contents of one of these domains, call the [- volatileDomainForName:](<volatiledomain(forname_).md>) method.

## See Also

### Getting the domain names

- [NSArgumentDomain](argumentdomain.md) — The identifier for the domain that contains command-line settings.
- [NSGlobalDomain](globaldomain.md) — The identifier for the domain that contains system-specified settings for all apps.
- [NSRegistrationDomain](registrationdomain.md) — The identifier for the domain that contains your app’s registered default values.
