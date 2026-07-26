---
title: accessInstanceVariablesDirectly
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessinstancevariablesdirectly
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessinstancevariablesdirectly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessinstancevariablesdirectly.json'
content_hash: 'sha256:0a0387d7bcd5671b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessInstanceVariablesDirectly

<sub>Type Property</sub>

Returns a Boolean value that indicates whether the key-value coding methods should access the corresponding instance variable directly on finding no accessor method for a property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var accessInstanceVariablesDirectly: Bool { get }
```

## Return Value

[YES](../yes.md) if the key-value coding methods should access the corresponding instance variable directly on finding no accessor method for a property, otherwise [NO](../no.md).

## Discussion

The default returns [YES](../yes.md). Subclasses can override it to return [NO](../no.md), in which case the key-value coding methods won’t access instance variables.
