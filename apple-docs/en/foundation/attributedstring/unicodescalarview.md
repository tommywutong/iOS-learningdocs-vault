---
title: AttributedString.UnicodeScalarView
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/unicodescalarview
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/unicodescalarview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/unicodescalarview.json'
content_hash: 'sha256:68bae1e8d06509ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# AttributedString.UnicodeScalarView

<sub>Structure</sub>

A view into the underlying storage of the attributed string, as Unicode scalars.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct UnicodeScalarView
```

## Relationships

- **Conforms To**: [BidirectionalCollection](../../swift/bidirectionalcollection.md), [Collection](../../swift/collection.md), [Copyable](../../swift/copyable.md), [Escapable](../../swift/escapable.md), [RangeReplaceableCollection](../../swift/rangereplaceablecollection.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [Sequence](../../swift/sequence.md)

## Topics

### Default Implementations

- [Collection Implementations](unicodescalarview/collection-implementations.md)

## See Also

### Accessing Views into the Attributed String

- [characters](characters.md) — The characters of the attributed string, as a view into the underlying string.
- [CharacterView](characterview.md) — A view into the underlying storage of the attributed string, as Unicode characters.
- [unicodeScalars](unicodescalars.md) — The Unicode scalars of the attributed string, as a view into the underlying string.
- [runs](runs-swift.property.md) — The attributed runs of the attributed string, as a view into the underlying string.
- [Runs](runs-swift.struct.md) — An iterable view into segments of the attributed string, each of which indicates where a run of identical attributes begins or ends.
