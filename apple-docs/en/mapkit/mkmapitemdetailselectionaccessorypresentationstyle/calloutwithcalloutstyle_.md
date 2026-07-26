---
title: 'calloutWithCalloutStyle:'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapitemdetailselectionaccessorypresentationstyle/calloutwithcalloutstyle:'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapitemdetailselectionaccessorypresentationstyle/calloutwithcalloutstyle:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapitemdetailselectionaccessorypresentationstyle/calloutwithcalloutstyle%3A.json'
content_hash: 'sha256:31f20b332e2d81ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapItemDetailPresentationStyle](../mkselectionaccessory/mapitemdetailpresentationstyle.md)

# calloutWithCalloutStyle:

<sub>Type Method</sub>

Show map item detail as an annotation callout on the map

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (MKMapItemDetailSelectionAccessoryPresentationStyle *) calloutWithCalloutStyle:(MKMapItemDetailSelectionAccessoryCalloutStyle) style;
```

## Parameters

- `style` — The callout style to use.

## See Also

### Creating a presentation style

- [automaticWithPresentationViewController:](automaticwithpresentationviewcontroller_.md) — An appropriate presentation style will be chosen automatically.
- [callout](../mkselectionaccessory/mapitemdetailpresentationstyle/callout.md) — Show map item detail as an annotation callout on the map.
- [openInMaps](../mkselectionaccessory/mapitemdetailpresentationstyle/openinmaps.md) — Display a small “Open in Apple Maps” link.
- [+ sheetPresentedFromViewController:](<../mkselectionaccessory/mapitemdetailpresentationstyle/sheet(presentedfrom_).md>) — Show map item detail by presenting a sheet.
