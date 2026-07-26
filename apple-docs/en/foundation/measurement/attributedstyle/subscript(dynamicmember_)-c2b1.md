---
title: 'subscript(dynamicMember:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/measurement/attributedstyle/subscript(dynamicmember:)-c2b1'
source_url: 'https://developer.apple.com/documentation/foundation/measurement/attributedstyle/subscript(dynamicmember:)-c2b1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/attributedstyle/subscript%28dynamicmember%3A%29-c2b1.json'
content_hash: 'sha256:c5f501294325ba28'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Measurement](../../measurement.md) · [AttributedStyle](../attributedstyle.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<T>(dynamicMember key: WritableKeyPath<Measurement<UnitType>.FormatStyle, T>) -> T { get set }
```
