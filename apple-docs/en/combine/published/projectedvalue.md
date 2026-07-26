---
title: projectedValue
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/published/projectedvalue
source_url: 'https://developer.apple.com/documentation/combine/published/projectedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/published/projectedvalue.json'
content_hash: 'sha256:2fc621653e87e0e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Published](../published.md)

# projectedValue

<sub>Instance Property</sub>

The property for which this instance exposes a publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var projectedValue: Published<Value>.Publisher { mutating get set }
```

## Discussion

The [projectedValue](projectedvalue.md) is the property accessed with the `$` operator.

## See Also

### Publishing the value

- [Publisher](publisher.md) — A publisher for properties marked with the `@Published` attribute.
