---
title: MKMapItemDetailViewControllerDelegate
framework: MapKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapitemdetailviewcontrollerdelegate
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapitemdetailviewcontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapitemdetailviewcontrollerdelegate.json'
content_hash: 'sha256:1c4fd5507e512e71'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMapItemDetailViewControllerDelegate

<sub>Protocol</sub>

The methods that you use to receive events from an associated map view controller.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor protocol MKMapItemDetailViewControllerDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Methods

- [- mapItemDetailViewControllerDidFinish:](<mkmapitemdetailviewcontrollerdelegate/mapitemdetailviewcontrollerdidfinish(__).md>) — Informs the delegate when a person dismissed the view controller.

## See Also

### Place information

- [MKMapItemDetailViewController](mkmapitemdetailviewcontroller.md) — An object that displays detailed information about a map item.
- [MapItemDetailPresentationStyle](mkselectionaccessory/mapitemdetailpresentationstyle.md) — The type of map item detail accessory presentation to use.
- [MKSelectionAccessory](mkselectionaccessory.md) — The type of accessory to display for a selected annotation.
- [CalloutStyle](mkselectionaccessory/mapitemdetailpresentationstyle/calloutstyle.md) — The style to use for a map item detail callout presentation.
