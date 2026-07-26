---
title: animatesDrop
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（16.0 起废弃）, iPadOS 3.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.9+（13.0 起废弃）, tvOS 9.2+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkpinannotationview/animatesdrop
source_url: 'https://developer.apple.com/documentation/mapkit/mkpinannotationview/animatesdrop'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpinannotationview/animatesdrop.json'
content_hash: 'sha256:8261578cafea5de9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKPinAnnotationView](../mkpinannotationview.md)

# animatesDrop

<sub>Instance Property</sub>

A Boolean value indicating whether the annotation view is animated onto the screen.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var animatesDrop: Bool { get set }
```

## Discussion

When this property is [true](../../swift/true.md), the map view animates the appearance of pin annotation views by making them appear to drop onto the map at the target point. This animation occurs whenever the view transitions from offscreen to onscreen.

## See Also

### Getting and Setting Attributes

- [pinTintColor](pintintcolor.md) — The color of the pin head. _(deprecated)_
- [pinColor](pincolor.md) — The color of the pin head. _(deprecated)_
