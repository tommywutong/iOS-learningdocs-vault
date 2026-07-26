---
title: NSTextCheckingTypes
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstextcheckingtypes
source_url: 'https://developer.apple.com/documentation/foundation/nstextcheckingtypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstextcheckingtypes.json'
content_hash: 'sha256:ed21c92990a172ef'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSTextCheckingTypes

<sub>Type Alias</sub>

Defines the types of checking that are available. These values can be combined using the C-bitwise OR operator. The system supports its own internal types, and the user can extend those types by subclassing `NSTextCheckingResult` and adding their own custom types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias NSTextCheckingTypes = UInt64
```

## Topics

### Constants

- [NSTextCheckingAllSystemTypes](nstextcheckingallsystemtypes.md) — Checking types supported by the system. The first 32 types are reserved.
- [NSTextCheckingAllCustomTypes](nstextcheckingallcustomtypes.md) — Checking types that can be used by clients.
- [NSTextCheckingAllTypes](nstextcheckingalltypes.md) — All possible checking types, both system- and user-supported.

## See Also

### Constants

- [Keys for Transit Components](keys-for-transit-components.md) — The following constants identify the possible keys returned in the components dictionary.
- [Keys for Address Components](keys-for-address-components.md) — The following constants identify the possible keys returned in the [addressComponents](nstextcheckingresult/addresscomponents.md) dictionary.
- [CheckingType](nstextcheckingresult/checkingtype.md) — These constants specify the type of checking the methods should do. They are returned by [resultType](nstextcheckingresult/resulttype.md).
- [NSTextCheckingKey](nstextcheckingkey.md)
- [Anonymous](1476845-anonymous.md)
