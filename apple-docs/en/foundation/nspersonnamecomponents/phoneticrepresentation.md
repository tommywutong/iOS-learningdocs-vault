---
title: phoneticRepresentation
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspersonnamecomponents/phoneticrepresentation
source_url: 'https://developer.apple.com/documentation/foundation/nspersonnamecomponents/phoneticrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspersonnamecomponents/phoneticrepresentation.json'
content_hash: 'sha256:bccd12ef5102494f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPersonNameComponents](../nspersonnamecomponents.md)

# phoneticRepresentation

<sub>Instance Property</sub>

The phonetic representation name components of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var phoneticRepresentation: PersonNameComponents? { get set }
```

## Discussion

Each component of the receiver with a value should have a corresponding value for any value set for this property. `nil` by default.

The `phoneticRepresentation` property value of this property value is ignored.

## See Also

### Accessing Person Name Components

- [namePrefix](nameprefix.md) — The portion of a name’s full form of address that precedes the name itself _(for example, “Dr.,” “Mr.,” “Ms.”)_.
- [givenName](givenname.md) — Name bestowed upon an individual to differentiate them from other members of a group that share a family name _(for example, “Johnathan”)_.
- [middleName](middlename.md) — Secondary name bestowed upon an individual to differentiate them from others that have the same given name _(for example, “Maple”)_.
- [familyName](familyname.md) — Name bestowed upon an individual to denote membership in a group or family. _(for example, “Appleseed”)_.
- [nameSuffix](namesuffix.md) — The portion of a name’s full form of address that follows the name itself _(for example, “Esq.,” “Jr.,” “Ph.D.”)_.
- [nickname](nickname.md) — Name substituted for the purposes of familiarity _(for example, “Johnny”)_.
