---
title: AttributedString.Index
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/index
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/index'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/index.json'
content_hash: 'sha256:2205c1ab00f91ac8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# AttributedString.Index

<sub>Structure</sub>

A type that represents the position of a character or code unit within an attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Index
```

## Relationships

- **Conforms To**: [Comparable](../../swift/comparable.md), [Equatable](../../swift/equatable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(_:within:)](<index/init(__within_).md>)

### Instance Methods

- [isValid(within:)](<index/isvalid(within_)-6wjr6.md>) — Indicates whether the index is valid for use with the provided discontiguous attributed string.
- [isValid(within:)](<index/isvalid(within_)-8fw50.md>) — Indicates whether the index is valid for use with the provided attributed string.

## See Also

### Modifying an Attributed String

- [insert(_:at:)](<insert(__at_).md>) — Inserts the specified string at a specific index in the attributed string.
- [removeSubrange(_:)](<removesubrange(__).md>) — Removes a range of characters from the attributed string.
- [replaceSubrange(_:with:)](<replacesubrange(__with_).md>) — Replaces the contents in a range of the attributed string.
