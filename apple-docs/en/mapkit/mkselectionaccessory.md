---
title: MKSelectionAccessory
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkselectionaccessory
source_url: 'https://developer.apple.com/documentation/mapkit/mkselectionaccessory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkselectionaccessory.json'
content_hash: 'sha256:8bc2637d1aa93087'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKSelectionAccessory

<sub>Class</sub>

The type of accessory to display for a selected annotation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class MKSelectionAccessory
```

## Overview

Implement [- mapView:selectionAccessoryForAnnotation:](<mkmapviewdelegate/mapview(__selectionaccessoryfor_).md>) in your map view delegate to specify a selection accessory for annotation content.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a selection accessory

- [+ mapItemDetailWithPresentationStyle:](<mkselectionaccessory/mapitemdetail(__).md>) — Detailed information about a place

## See Also

### Place information

- [MKMapItemDetailViewControllerDelegate](mkmapitemdetailviewcontrollerdelegate.md) — The methods that you use to receive events from an associated map view controller.
- [MKMapItemDetailViewController](mkmapitemdetailviewcontroller.md) — An object that displays detailed information about a map item.
- [MapItemDetailPresentationStyle](mkselectionaccessory/mapitemdetailpresentationstyle.md) — The type of map item detail accessory presentation to use.
- [CalloutStyle](mkselectionaccessory/mapitemdetailpresentationstyle/calloutstyle.md) — The style to use for a map item detail callout presentation.
