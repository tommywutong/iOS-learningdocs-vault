---
title: 'subscript(_:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/discontiguousattributedsubstring/subscript(_:)-1bcls'
source_url: 'https://developer.apple.com/documentation/foundation/discontiguousattributedsubstring/subscript(_:)-1bcls'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/discontiguousattributedsubstring/subscript%28_%3A%29-1bcls.json'
content_hash: 'sha256:2a9059a36dd4173e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DiscontiguousAttributedSubstring](../discontiguousattributedsubstring.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns an attribute value that corresponds to an attributed string key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<K>(_: K.Type) -> K.Value? where K : AttributedStringKey, K.Value : Sendable { get set }
```

## Overview

This subscript returns `nil` unless the specified attribute exists, and is present and identical for the entire discontiguous attributed substring. To find portions of an attributed string with consistent attributes, use the `runs` property. Getting or setting stringwide attributes with this subscript has `O(n)` behavior in the worst case, where n is the number of runs.
