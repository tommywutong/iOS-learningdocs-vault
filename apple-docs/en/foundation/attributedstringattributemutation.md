---
title: AttributedStringAttributeMutation
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstringattributemutation
source_url: 'https://developer.apple.com/documentation/foundation/attributedstringattributemutation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstringattributemutation.json'
content_hash: 'sha256:627d4390ab2ade84'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# AttributedStringAttributeMutation

<sub>Protocol</sub>

A protocol that defines in-place mutations for attributes in an attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol AttributedStringAttributeMutation
```

## Relationships

- **Inherited By**: [AttributedStringProtocol](attributedstringprotocol.md)

- **Conforming Types**: [AttributedString](attributedstring.md), [AttributedSubstring](attributedsubstring.md), [DiscontiguousAttributedSubstring](discontiguousattributedsubstring.md)

## Topics

### Mutating the String’s Attributes

- [setAttributes(_:)](<attributedstringattributemutation/setattributes(__).md>) — Sets the attributed string’s attributes to those in a specified attribute container.
- [mergeAttributes(_:mergePolicy:)](<attributedstringattributemutation/mergeattributes(__mergepolicy_).md>) — Merges the attributed string’s attributes with those in a specified attribute container.
- [replaceAttributes(_:with:)](<attributedstringattributemutation/replaceattributes(__with_).md>) — Replaces the attributed string’s attributes with those in a specified attribute container.

## See Also

### Applying and Modifying Attributes

- [setAttributes(_:)](<attributedstring/setattributes(__).md>) — Sets the attributed string’s attributes to those in a specified attribute container.
- [mergeAttributes(_:mergePolicy:)](<attributedstring/mergeattributes(__mergepolicy_).md>) — Merges the attributed string’s attributes with those in a specified attribute container.
- [AttributeMergePolicy](attributedstring/attributemergepolicy.md) — An enumeration of behaviors to apply when merging attributes.
- [replaceAttributes(_:with:)](<attributedstring/replaceattributes(__with_).md>) — Replaces occurrences of attributes in one attribute container with those in another attribute container.
