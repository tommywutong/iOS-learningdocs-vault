---
title: EnumeratedSequence.Index
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/enumeratedsequence/index
source_url: 'https://developer.apple.com/documentation/swift/enumeratedsequence/index'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/enumeratedsequence/index.json'
content_hash: 'sha256:8d09ba706ebca44f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [EnumeratedSequence](../enumeratedsequence.md)

# EnumeratedSequence.Index

<sub>Structure</sub>

A type that represents a position in the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Index
```

## Overview

Valid indices consist of the position of every element and a “past the end” position that’s not valid for use as a subscript argument.

## Relationships

- **Conforms To**: [Comparable](../comparable.md), [Equatable](../equatable.md)

## Topics

### Instance Properties

- [base](index/base.md) — The position in the underlying collection.

### Default Implementations

- [Comparable Implementations](index/comparable-implementations.md)
- [Equatable Implementations](index/equatable-implementations.md)
