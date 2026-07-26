---
title: redPinColor()
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+（16.0 起废弃）, iPadOS 9.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkpinannotationview/redpincolor()
source_url: 'https://developer.apple.com/documentation/mapkit/mkpinannotationview/redpincolor()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpinannotationview/redpincolor%28%29.json'
content_hash: 'sha256:1107428699185252'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKPinAnnotationView](../mkpinannotationview.md)

# redPinColor()

<sub>Type Method</sub>

Returns the standard color for red pins.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func redPinColor() -> UIColor
```

<sub>macOS</sub>

```swift
class func redPinColor() -> NSColor
```

## Return Value

The red pin color.

## Discussion

The system uses red pins to indicate destination points on the map.

## See Also

### Getting Standard Pin Colors

- [+ greenPinColor](<greenpincolor().md>) — Returns the standard color for green pins. _(deprecated)_
- [+ purplePinColor](<purplepincolor().md>) — Returns the standard color for purple pins. _(deprecated)_
- [MKPinAnnotationColor](../mkpinannotationcolor.md) — The supported colors for pin annotations. _(deprecated)_
