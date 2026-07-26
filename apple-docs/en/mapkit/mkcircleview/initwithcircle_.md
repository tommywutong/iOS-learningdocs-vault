---
title: 'initWithCircle:'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（7.0 起废弃）, iPadOS 4.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mkcircleview/initwithcircle:'
source_url: 'https://developer.apple.com/documentation/mapkit/mkcircleview/initwithcircle:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkcircleview/initwithcircle%3A.json'
content_hash: 'sha256:237dc4ed7e7b99c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKCircleView](../mkcircleview.md)

# initWithCircle:

<sub>Instance Method</sub>

Initializes and returns a new overlay view using the specified circle overlay object.

> [!warning] Deprecated
> Use the [MKCircleRenderer](../mkcirclerenderer.md) class instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithCircle:(MKCircle *) circle;
```

## Parameters

- `circle` — The circle overlay containing the information about the circular area to be drawn.

## Return Value

A new circle overlay view.

## See Also

### Related Documentation

- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
