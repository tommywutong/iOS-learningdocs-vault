---
title: newValue
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyvalueobservedchange/newvalue
source_url: 'https://developer.apple.com/documentation/foundation/nskeyvalueobservedchange/newvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyvalueobservedchange/newvalue.json'
content_hash: 'sha256:d1eeed1c5f8e94b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyValueObservedChange](../nskeyvalueobservedchange.md)

# newValue

<sub>Instance Property</sub>

newValue and oldValue will only be non-nil if .new/.old is passed to `observe()`. In general, get the most up to date value by accessing it directly on the observed object instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let newValue: Value?
```
