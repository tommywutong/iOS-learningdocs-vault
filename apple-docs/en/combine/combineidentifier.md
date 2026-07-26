---
title: CombineIdentifier
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/combineidentifier
source_url: 'https://developer.apple.com/documentation/combine/combineidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/combineidentifier.json'
content_hash: 'sha256:3240921b8d501a5e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# CombineIdentifier

<sub>Structure</sub>

A unique identifier for identifying publisher streams.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CombineIdentifier
```

## Overview

To conform to [CustomCombineIdentifierConvertible](customcombineidentifierconvertible.md) in a [Subscription](subscription.md) or [Subject](subject.md) that you implement as a structure, create an instance of [CombineIdentifier](combineidentifier.md) as follows:

```swift
let combineIdentifier = CombineIdentifier()
```

## Relationships

- **Conforms To**: [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a Combine identifier

- [init()](<combineidentifier/init().md>) — Creates a unique Combine identifier.
- [init(_:)](<combineidentifier/init(__).md>) — Creates a Combine identifier, using the bit pattern of the provided object.

### Providing a description

- [description](combineidentifier/description.md) — A textual representation of this instance.

## See Also

### Debugging Identifiers

- [CustomCombineIdentifierConvertible](customcombineidentifierconvertible.md) — A protocol for uniquely identifying publisher streams.
