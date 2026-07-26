---
title: NSEnumerationOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsenumerationoptions
source_url: 'https://developer.apple.com/documentation/foundation/nsenumerationoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsenumerationoptions.json'
content_hash: 'sha256:ae50f14c46abfc85'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSEnumerationOptions

<sub>Structure</sub>

Options for block enumeration operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NSEnumerationOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [NSEnumerationConcurrent](nsenumerationoptions/concurrent.md) — Specifies that the Block enumeration should be concurrent.
- [NSEnumerationReverse](nsenumerationoptions/reverse.md) — Specifies that the enumeration should be performed in reverse.

### Initializers

- [init(rawValue:)](<nsenumerationoptions/init(rawvalue_).md>)

## See Also

### Iteration

- [NSEnumerator](nsenumerator.md) — An abstract class whose subclasses enumerate collections of objects, such as arrays and dictionaries.
- [NSFastEnumeration](nsfastenumeration.md) — A protocol that objects adopt to support fast enumeration.
- [NSFastEnumerationIterator](nsfastenumerationiterator.md)
- [NSIndexSetIterator](nsindexsetiterator.md) — An iterator suitable for enumerating the elements of an index set.
- [NSSortOptions](nssortoptions.md) — Options for block sorting operations.
