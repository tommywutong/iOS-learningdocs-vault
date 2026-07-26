---
title: MKSelectionAccessory.MapItemDetailPresentationStyle
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkselectionaccessory/mapitemdetailpresentationstyle
source_url: 'https://developer.apple.com/documentation/mapkit/mkselectionaccessory/mapitemdetailpresentationstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkselectionaccessory/mapitemdetailpresentationstyle.json'
content_hash: 'sha256:2db5cd19ed91c49e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKSelectionAccessory](../mkselectionaccessory.md)

# MKSelectionAccessory.MapItemDetailPresentationStyle

<sub>Class</sub>

The type of map item detail accessory presentation to use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class MapItemDetailPresentationStyle
```

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Creating a presentation style

- [automatic(presentationViewController:)](<mapitemdetailpresentationstyle/automatic(presentationviewcontroller_)-648ee.md>) — An appropriate presentation style will be chosen automatically.
- [automatic(presentationViewController:)](<mapitemdetailpresentationstyle/automatic(presentationviewcontroller_)-9t9vt.md>) — An appropriate presentation style will be chosen automatically.
- [callout](mapitemdetailpresentationstyle/callout.md) — Show map item detail as an annotation callout on the map.
- [callout(_:)](<mapitemdetailpresentationstyle/callout(__).md>) — Show map item detail as an annotation callout on the map
- [openInMaps](mapitemdetailpresentationstyle/openinmaps.md) — Display a small “Open in Apple Maps” link.
- [+ sheetPresentedFromViewController:](<mapitemdetailpresentationstyle/sheet(presentedfrom_).md>) — Show map item detail by presenting a sheet.

## See Also

### Place information

- [MKMapItemDetailViewControllerDelegate](../mkmapitemdetailviewcontrollerdelegate.md) — The methods that you use to receive events from an associated map view controller.
- [MKMapItemDetailViewController](../mkmapitemdetailviewcontroller.md) — An object that displays detailed information about a map item.
- [MKSelectionAccessory](../mkselectionaccessory.md) — The type of accessory to display for a selected annotation.
- [CalloutStyle](mapitemdetailpresentationstyle/calloutstyle.md) — The style to use for a map item detail callout presentation.
