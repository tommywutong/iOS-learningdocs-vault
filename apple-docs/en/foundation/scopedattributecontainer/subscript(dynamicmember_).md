---
title: 'subscript(dynamicMember:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/scopedattributecontainer/subscript(dynamicmember:)'
source_url: 'https://developer.apple.com/documentation/foundation/scopedattributecontainer/subscript(dynamicmember:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/scopedattributecontainer/subscript%28dynamicmember%3A%29.json'
content_hash: 'sha256:7ebcd1fc8cf10dae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ScopedAttributeContainer](../scopedattributecontainer.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

Returns the value of the attribute that the specified key path indicates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency subscript<T>(dynamicMember keyPath: KeyPath<S, T>) -> T.Value? where T : AttributedStringKey, T.Value : Sendable { get set }
```
