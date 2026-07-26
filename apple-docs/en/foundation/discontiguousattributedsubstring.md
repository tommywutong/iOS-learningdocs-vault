---
title: DiscontiguousAttributedSubstring
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/discontiguousattributedsubstring
source_url: 'https://developer.apple.com/documentation/foundation/discontiguousattributedsubstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/discontiguousattributedsubstring.json'
content_hash: 'sha256:90459f29fea06a08'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# DiscontiguousAttributedSubstring

<sub>Structure</sub>

A discontiguous portion of an attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@dynamicMemberLookup struct DiscontiguousAttributedSubstring
```

## Relationships

- **Conforms To**: [AttributedStringAttributeMutation](attributedstringattributemutation.md), [Copyable](../swift/copyable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [base](discontiguousattributedsubstring/base.md) — The underlying attributed string that the discontiguous attributed substring derives from.
- [characters](discontiguousattributedsubstring/characters.md) — The characters of the discontiguous attributed string, as a view into the underlying string.
- [runs](discontiguousattributedsubstring/runs.md) — The attributed runs of the discontiguous attributed string, as a view into the underlying string.
- [unicodeScalars](discontiguousattributedsubstring/unicodescalars.md) — The Unicode scalars of the discontiguous attributed string, as a view into the underlying string.

### Subscripts

- [subscript(_:)](<discontiguousattributedsubstring/subscript(__)-1bcls.md>) — Returns an attribute value that corresponds to an attributed string key.
- [subscript(_:)](<discontiguousattributedsubstring/subscript(__)-6j670.md>) — Returns a discontiguous substring of this discontiguous attributed string using a range to indicate the discontiguous substring bounds.
- [subscript(_:)](<discontiguousattributedsubstring/subscript(__)-6p2b.md>) — Returns a discontiguous substring of this discontiguous attributed string using a set of ranges to indicate the discontiguous substring bounds.
- [subscript(dynamicMember:)](<discontiguousattributedsubstring/subscript(dynamicmember_)-5i1c9.md>) — Returns an attribute value that a key path indicates.
- [subscript(dynamicMember:)](<discontiguousattributedsubstring/subscript(dynamicmember_)-89pug.md>) — Returns a scoped attribute container that a key path indicates.
