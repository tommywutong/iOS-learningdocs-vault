---
title: 'propertyList(_:isValidFor:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/propertylistserialization/propertylist(_:isvalidfor:)'
source_url: 'https://developer.apple.com/documentation/foundation/propertylistserialization/propertylist(_:isvalidfor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/propertylistserialization/propertylist%28_%3Aisvalidfor%3A%29.json'
content_hash: 'sha256:802767867e63795e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PropertyListSerialization](../propertylistserialization.md)

# propertyList(_:isValidFor:)

<sub>Type Method</sub>

Returns a Boolean value that indicates whether a given property list is valid for a given format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func propertyList(_ plist: Any, isValidFor format: PropertyListSerialization.PropertyListFormat) -> Bool
```

## Parameters

- `plist` — A property list object.

- `format` — A property list format. For possible values, see [PropertyListFormat](propertylistformat.md).

## Return Value

[true](../../swift/true.md) if `plist` is a valid property list in format `format`, otherwise [false](../../swift/false.md).
