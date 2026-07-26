---
title: AttributedString.AttributeMergePolicy
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/attributemergepolicy
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/attributemergepolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/attributemergepolicy.json'
content_hash: 'sha256:eb2b5cab13419a0c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# AttributedString.AttributeMergePolicy

<sub>Enumeration</sub>

An enumeration of behaviors to apply when merging attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum AttributeMergePolicy
```

## Overview

Use an [AttributeMergePolicy](attributemergepolicy.md) when working with methods like [mergeAttributes(_:mergePolicy:)](<mergeattributes(__mergepolicy_).md>) to indicate how to resolve conflicts between multiple sets of attributes. When a source string and a merging attribute container both contain a given attribute with different values, the merge policy determines how to resolve the conflict.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Merge Policies

- [AttributedString.AttributeMergePolicy.keepCurrent](attributemergepolicy/keepcurrent.md) — A policy to keep the string’s current attribute value when merging multiple sets of attributes.
- [AttributedString.AttributeMergePolicy.keepNew](attributemergepolicy/keepnew.md) — A policy to keep the newly-merged attribute value when merging multiple sets of attributes.

## See Also

### Applying and Modifying Attributes

- [setAttributes(_:)](<setattributes(__).md>) — Sets the attributed string’s attributes to those in a specified attribute container.
- [mergeAttributes(_:mergePolicy:)](<mergeattributes(__mergepolicy_).md>) — Merges the attributed string’s attributes with those in a specified attribute container.
- [replaceAttributes(_:with:)](<replaceattributes(__with_).md>) — Replaces occurrences of attributes in one attribute container with those in another attribute container.
- [AttributedStringAttributeMutation](../attributedstringattributemutation.md) — A protocol that defines in-place mutations for attributes in an attributed string.
