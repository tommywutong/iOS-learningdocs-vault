---
title: 'initWithCenter:radius:'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/clcirculargeographiccondition/initwithcenter:radius:'
source_url: 'https://developer.apple.com/documentation/corelocation/clcirculargeographiccondition/initwithcenter:radius:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clcirculargeographiccondition/initwithcenter%3Aradius%3A.json'
content_hash: 'sha256:abf8d6e2e4335d75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLCircularGeographicCondition](../clcirculargeographiccondition.md)

# initWithCenter:radius:

<sub>Instance Method</sub>

Creates a new circular geographic condition with the center point and radius you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithCenter:(CLLocationCoordinate2D) center radius:(CLLocationDistance) radius;
```

## Parameters

- `center` — The center of the circular geographic condition.

- `radius` — The radius of the circular geographic condition.

## Return Value

Returns an instance of `CLCircularGeographicCondition` with the specified center coordinate and radius.
