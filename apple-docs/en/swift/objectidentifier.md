---
title: ObjectIdentifier
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/objectidentifier
source_url: 'https://developer.apple.com/documentation/swift/objectidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/objectidentifier.json'
content_hash: 'sha256:059474c78e75a15c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# ObjectIdentifier

<sub>Structure</sub>

A unique identifier for a class instance, actor instance, or metatype.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct ObjectIdentifier
```

## Overview

This unique identifier is valid for comparisons only during the lifetime of the instance.

In Swift, only instances of classes, instances of actors, and metatypes have unique identities. There’s no notion of identity for structures, enumerations, functions, or tuples.

## Relationships

- **Conforms To**: [AtomicOptionalRepresentable](../synchronization/atomicoptionalrepresentable.md), [AtomicRepresentable](../synchronization/atomicrepresentable.md), [BitwiseCopyable](bitwisecopyable.md), [Comparable](comparable.md), [ConvertibleToBytes](convertibletobytes.md), [Copyable](copyable.md), [CustomDebugStringConvertible](customdebugstringconvertible.md), [Equatable](equatable.md), [Escapable](escapable.md), [Hashable](hashable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Initializers

- [init(_:)](<objectidentifier/init(__)-223xw.md>) — Creates an instance that uniquely identifies the given class instance.
- [init(_:)](<objectidentifier/init(__)-52bz1.md>) — Creates an instance that uniquely identifies the given metatype.
- [init(_:)](<objectidentifier/init(__)-86u7l.md>)

### Default Implementations

- [AtomicOptionalRepresentable Implementations](objectidentifier/atomicoptionalrepresentable-implementations.md)
- [AtomicRepresentable Implementations](objectidentifier/atomicrepresentable-implementations.md)
- [Comparable Implementations](objectidentifier/comparable-implementations.md)
- [CustomDebugStringConvertible Implementations](objectidentifier/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](objectidentifier/equatable-implementations.md)
- [Hashable Implementations](objectidentifier/hashable-implementations.md)

## See Also

### Querying Runtime Values

- [Mirror](mirror.md) — A representation of the substructure and display style of an instance of any type.
- [type(of:)](<type(of_).md>) — Returns the dynamic type of a value.
