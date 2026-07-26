---
title: 'subscript(dynamicMember:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/discontiguousattributedsubstring/subscript(dynamicmember:)-89pug'
source_url: 'https://developer.apple.com/documentation/foundation/discontiguousattributedsubstring/subscript(dynamicmember:)-89pug'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/discontiguousattributedsubstring/subscript%28dynamicmember%3A%29-89pug.json'
content_hash: 'sha256:5124f66020db92c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DiscontiguousAttributedSubstring](../discontiguousattributedsubstring.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

Returns a scoped attribute container that a key path indicates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<S>(dynamicMember keyPath: KeyPath<AttributeScopes, S.Type>) -> ScopedAttributeContainer<S> where S : AttributeScope { get set }
```
