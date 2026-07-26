---
title: PersistentIdentifier
framework: SwiftData
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/persistentidentifier
source_url: 'https://developer.apple.com/documentation/swiftdata/persistentidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/persistentidentifier.json'
content_hash: 'sha256:a7010c7b254673ad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# PersistentIdentifier

<sub>Structure</sub>

A type that describes the aggregate identity of a SwiftData model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PersistentIdentifier
```

## Overview

> [!note] Note
> Decoded [PersistentIdentifier](persistentidentifier.md) and identifiers created by the [DefaultStore](defaultstore.md) are not considered equivalent.

## Relationships

- **Conforms To**: [Comparable](../swift/comparable.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Identifiable](../swift/identifiable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing identity information

- [id](persistentidentifier/id-swift.property.md) — The value that uniquely identifies the associated model within the containing store.
- [ID](persistentidentifier/id-swift.struct.md) — A type that represents the stable identity of a SwiftData model.
- [storeIdentifier](persistentidentifier/storeidentifier.md) — The identifier of the store that contains the associated model.
- [entityName](persistentidentifier/entityname.md) — The entity name for the associated model.

### Instance Properties

- [isTemporary](persistentidentifier/istemporary.md) — A Boolean value that indicates whether the identifier is temporary. _(beta)_

### Type Methods

- [identifier(for:entityName:primaryKey:)](<persistentidentifier/identifier(for_entityname_primarykey_).md>)

## See Also

### Identifying the model instance

- [persistentModelID](persistentmodel/persistentmodelid.md)
- [modelContext](persistentmodel/modelcontext.md)
