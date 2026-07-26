---
title: 'automaticWithPresentationViewController:'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapitemdetailselectionaccessorypresentationstyle/automaticwithpresentationviewcontroller:'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapitemdetailselectionaccessorypresentationstyle/automaticwithpresentationviewcontroller:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapitemdetailselectionaccessorypresentationstyle/automaticwithpresentationviewcontroller%3A.json'
content_hash: 'sha256:ba91ea53d8cb34e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapItemDetailPresentationStyle](../mkselectionaccessory/mapitemdetailpresentationstyle.md)

# automaticWithPresentationViewController:

<sub>Type Method</sub>

An appropriate presentation style will be chosen automatically.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
+ (MKMapItemDetailSelectionAccessoryPresentationStyle *) automaticWithPresentationViewController:(UIViewController *) presentationViewController;
```

<sub>macOS</sub>

```objc
+ (MKMapItemDetailSelectionAccessoryPresentationStyle *) automaticWithPresentationViewController:(NSViewController *) presentationViewController;
```

## Parameters

- `presentationViewController` — Supplying a non-nil presentationViewController will enable sheet presentation, if appropriate.

## See Also

### Creating a presentation style

- [callout](../mkselectionaccessory/mapitemdetailpresentationstyle/callout.md) — Show map item detail as an annotation callout on the map.
- [calloutWithCalloutStyle:](calloutwithcalloutstyle_.md) — Show map item detail as an annotation callout on the map
- [openInMaps](../mkselectionaccessory/mapitemdetailpresentationstyle/openinmaps.md) — Display a small “Open in Apple Maps” link.
- [+ sheetPresentedFromViewController:](<../mkselectionaccessory/mapitemdetailpresentationstyle/sheet(presentedfrom_).md>) — Show map item detail by presenting a sheet.
