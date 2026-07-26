---
title: valueExpression
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspropertymapping/valueexpression
source_url: 'https://developer.apple.com/documentation/coredata/nspropertymapping/valueexpression'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspropertymapping/valueexpression.json'
content_hash: 'sha256:fbbb145c3a99de64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPropertyMapping](../nspropertymapping.md)

# valueExpression

<sub>Instance Property</sub>

The value expression for the property mapping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var valueExpression: NSExpression? { get set }
```

## Discussion

The expression is used to create the value for the destination property.

## See Also

### Managing Mapping Attributes

- [name](name.md) — The name of the property in the destination entity for the property mapping.
- [userInfo](userinfo.md) — The user info for the property mapping.
