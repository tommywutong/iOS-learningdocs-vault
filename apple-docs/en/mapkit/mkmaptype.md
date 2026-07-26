---
title: MKMapType
framework: MapKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkmaptype
source_url: 'https://developer.apple.com/documentation/mapkit/mkmaptype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmaptype.json'
content_hash: 'sha256:7d0f3ce05fe95abe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMapType

<sub>Enumeration</sub>

The type of map to display.

> [!warning] Deprecated
> Use the map view’s [preferredConfiguration](mkmapview/preferredconfiguration.md) property with one of the [MKMapConfiguration](mkmapconfiguration.md) subclasses to select a specific map style instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MKMapType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [MKMapTypeStandard](mkmaptype/standard.md) — A street map that shows the position of all roads and some road names.
- [MKMapTypeSatellite](mkmaptype/satellite.md) — Satellite imagery of the area.
- [MKMapTypeHybrid](mkmaptype/hybrid.md) — A satellite image of the area with road and road name information layered on top.
- [MKMapTypeSatelliteFlyover](mkmaptype/satelliteflyover.md) — A satellite image of the area with flyover data where available.
- [MKMapTypeHybridFlyover](mkmaptype/hybridflyover.md) — A hybrid satellite image with flyover data where available.
- [MKMapTypeMutedStandard](mkmaptype/mutedstandard.md) — A street map where MapKit emphasizes your data over the underlying map details.

### Initializers

- [init(rawValue:)](<mkmaptype/init(rawvalue_).md>)

## See Also

### Enumerations

- [FilterType](mklocalsearchcompleter/filtertype-swift.enum.md) — Constants indicating the types of search completions to return. _(deprecated)_
- [MKPinAnnotationColor](mkpinannotationcolor.md) — The supported colors for pin annotations. _(deprecated)_
