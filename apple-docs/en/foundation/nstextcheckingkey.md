---
title: NSTextCheckingKey
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstextcheckingkey
source_url: 'https://developer.apple.com/documentation/foundation/nstextcheckingkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstextcheckingkey.json'
content_hash: 'sha256:87f7a45749623c92'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSTextCheckingKey

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NSTextCheckingKey
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(_:)](<nstextcheckingkey/init(__).md>)
- [init(rawValue:)](<nstextcheckingkey/init(rawvalue_).md>)

## See Also

### Constants

- [Keys for Transit Components](keys-for-transit-components.md) — The following constants identify the possible keys returned in the components dictionary.
- [Keys for Address Components](keys-for-address-components.md) — The following constants identify the possible keys returned in the [addressComponents](nstextcheckingresult/addresscomponents.md) dictionary.
- [CheckingType](nstextcheckingresult/checkingtype.md) — These constants specify the type of checking the methods should do. They are returned by [resultType](nstextcheckingresult/resulttype.md).
- [NSTextCheckingTypes](nstextcheckingtypes.md) — Defines the types of checking that are available. These values can be combined using the C-bitwise OR operator. The system supports its own internal types, and the user can extend those types by subclassing `NSTextCheckingResult` and adding their own custom types.
- [Anonymous](1476845-anonymous.md)
