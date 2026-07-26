---
title: UUID
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 6.0+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/uuid
source_url: 'https://developer.apple.com/documentation/foundation/uuid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/uuid.json'
content_hash: 'sha256:543cd126cb9ec486'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# UUID

<sub>Structure</sub>

A universally unique value to identify types, interfaces, and other items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct UUID
```

## Relationships

- **Conforms To**: [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md), [Comparable](../swift/comparable.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [EntityIdentifierConvertible](../appintents/entityidentifierconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [ReferenceConvertible](referenceconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating UUIDs

- [init()](<uuid/init().md>) — Creates a UUID with RFC 4122 version 4 random bytes.
- [init(uuid:)](<uuid/init(uuid_).md>) — Creates a UUID from the uuid C-language structure.
- [init(uuidString:)](<uuid/init(uuidstring_).md>) — Creates a UUID from a string representation.

### Getting UUID Values

- [uuid](uuid/uuid.md) — Returns the UUID as bytes.
- [uuidString](uuid/uuidstring.md) — Returns a string created from the UUID, such as “E621E1F8-C36C-495A-93FC-0C247A3E6E5F”

### Using Reference Types

- [NSUUID](nsuuid.md) — A universally unique value that can be used to identify types, interfaces, and other items.

### Type Methods

- [random(using:)](<uuid/random(using_).md>) — Generates a new random UUID.
