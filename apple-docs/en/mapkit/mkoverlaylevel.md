---
title: MKOverlayLevel
framework: MapKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkoverlaylevel
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlaylevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlaylevel.json'
content_hash: 'sha256:053d4ba37a50e97d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKOverlayLevel

<sub>Enumeration</sub>

Constants that indicate the position of overlays relative to other content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum MKOverlayLevel
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [MKOverlayLevelAboveRoads](mkoverlaylevel/aboveroads.md) — Place the overlay above roadways but below map labels, shields, or point-of-interest icons.
- [MKOverlayLevelAboveLabels](mkoverlaylevel/abovelabels.md) — Place the overlay above map labels, shields, or point-of-interest icons but below annotations and 3D projections of buildings.

### Initializers

- [init(rawValue:)](<mkoverlaylevel/init(rawvalue_).md>)

## See Also

### Accessing overlays

- [overlays](mkmapview/overlays.md) — The overlay objects associated with the map view.
- [- overlaysInLevel:](<mkmapview/overlays(in_).md>) — Returns overlay objects in the specified level of the map.
- [- rendererForOverlay:](<mkmapview/renderer(for_).md>) — Returns the renderer object for drawing the contents of the specified overlay object.
- [- viewForOverlay:](<mkmapview/view(for_)-38z60.md>) — Returns the view associated with the overlay object, if any. _(deprecated)_
