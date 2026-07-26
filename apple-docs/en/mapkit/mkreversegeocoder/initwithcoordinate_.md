---
title: 'initWithCoordinate:'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（5.0 起废弃）, iPadOS 3.0+（5.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mkreversegeocoder/initwithcoordinate:'
source_url: 'https://developer.apple.com/documentation/mapkit/mkreversegeocoder/initwithcoordinate:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkreversegeocoder/initwithcoordinate%3A.json'
content_hash: 'sha256:61edf9e893190e99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKReverseGeocoder](../mkreversegeocoder.md)

# initWithCoordinate:

<sub>Instance Method</sub>

Initializes the reverse geocoder with the specified coordinate value.

> [!warning] Deprecated
> Use the [CLGeocoder](../../corelocation/clgeocoder.md) class instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithCoordinate:(CLLocationCoordinate2D) coordinate;
```

## Parameters

- `coordinate` — The map coordinate whose placemark information you want to retrieve.

## Return Value

An initialized `MKReverseGeocoder` object.

## See Also

### Related Documentation

- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
