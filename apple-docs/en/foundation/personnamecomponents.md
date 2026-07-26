---
title: PersonNameComponents
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 9.0+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/personnamecomponents
source_url: 'https://developer.apple.com/documentation/foundation/personnamecomponents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/personnamecomponents.json'
content_hash: 'sha256:13ad4ee0c4017436'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# PersonNameComponents

<sub>Structure</sub>

The separate parts of a person’s name, allowing locale-aware formatting.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PersonNameComponents
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomLocalizedStringResourceConvertible](customlocalizedstringresourceconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Decodable](../swift/decodable.md), [DisplayRepresentable](../appintents/displayrepresentable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [InstanceDisplayRepresentable](../appintents/instancedisplayrepresentable.md), [IntentValueConvertible](../appintents/intentvalueconvertible.md), [IntentValueExpressing](../appintents/intentvalueexpressing.md), [ReferenceConvertible](referenceconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [TypeDisplayRepresentable](../appintents/typedisplayrepresentable.md)

## Topics

### Creating Person Name Components

- [init()](<personnamecomponents/init().md>) — Initializes a new person name components structure.

### Accessing Person Name Components

- [namePrefix](personnamecomponents/nameprefix.md) — The portion of a name’s full form of address that precedes the name itself.
- [givenName](personnamecomponents/givenname.md) — Name bestowed upon an individual to differentiate them from other members of a group that share a family name.
- [middleName](personnamecomponents/middlename.md) — Secondary name bestowed upon an individual to differentiate them from others that have the same given name.
- [familyName](personnamecomponents/familyname.md) — Name bestowed upon an individual to denote membership in a group or family.
- [nameSuffix](personnamecomponents/namesuffix.md) — The portion of a name’s full form of address that follows the name itself.
- [nickname](personnamecomponents/nickname.md) — Name substituted for the purposes of familiarity.
- [phoneticRepresentation](personnamecomponents/phoneticrepresentation.md) — The phonetic representation name components of the receiver.

### Formatting Person Name Components

- [formatted()](<personnamecomponents/formatted().md>) — Generates a locale-aware string representation of an instance of person name components using the default format style.
- [formatted(_:)](<personnamecomponents/formatted(__).md>) — Generates a locale-aware string representation of an instance of person name components using the provided format style.
- [FormatStyle](personnamecomponents/formatstyle.md) — A type used to format a person’s name with a style appropriate for the given locale.

### Using Reference Types

- [NSPersonNameComponents](nspersonnamecomponents.md) — An object that manages the separate parts of a person’s name to allow locale-aware formatting.

### Structures

- [AttributedStyle](personnamecomponents/attributedstyle.md)
- [ParseStrategy](personnamecomponents/parsestrategy.md)

### Initializers

- [init(_:)](<personnamecomponents/init(__).md>) — Creates a person name components object from a given string.
- [init(_:strategy:)](<personnamecomponents/init(__strategy_).md>) — Creates a person name components object from a given string by applying the provided parsing strategy.
- [init(namePrefix:givenName:middleName:familyName:nameSuffix:nickname:phoneticRepresentation:)](<personnamecomponents/init(nameprefix_givenname_middlename_familyname_namesuffix_nickname_phoneticrepresentation_).md>)

### Type Aliases

- [Specification](personnamecomponents/specification.md)
- [UnwrappedType](personnamecomponents/unwrappedtype.md)
- [ValueType](personnamecomponents/valuetype.md)

### Type Properties

- [defaultResolverSpecification](personnamecomponents/defaultresolverspecification.md)

## See Also

### Names

- [PersonNameComponentsFormatter](personnamecomponentsformatter.md) — A formatter that provides localized representations of the components of a person’s name.
