---
title: defaultValue
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/foundation/progressmanager/property/defaultvalue
source_url: 'https://developer.apple.com/documentation/foundation/progressmanager/property/defaultvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressmanager/property/defaultvalue.json'
content_hash: 'sha256:3f67365316def7bf'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [ProgressManager](../../progressmanager.md) · [Property](../property.md)

# defaultValue

<sub>Type Property</sub>

The default value to return when property is not set to a specific value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var defaultValue: Self.Value { get }
```

## Return Value

The default value for this property type.

## Discussion

This value is used when a progress manager doesn’t have an explicit value set for this property type.
