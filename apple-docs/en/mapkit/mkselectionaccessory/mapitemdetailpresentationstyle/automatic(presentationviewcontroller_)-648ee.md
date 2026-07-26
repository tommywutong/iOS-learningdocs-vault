---
title: 'automatic(presentationViewController:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkselectionaccessory/mapitemdetailpresentationstyle/automatic(presentationviewcontroller:)-648ee'
source_url: 'https://developer.apple.com/documentation/mapkit/mkselectionaccessory/mapitemdetailpresentationstyle/automatic(presentationviewcontroller:)-648ee'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkselectionaccessory/mapitemdetailpresentationstyle/automatic%28presentationviewcontroller%3A%29-648ee.json'
content_hash: 'sha256:65901d7972b04878'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKSelectionAccessory](../../mkselectionaccessory.md) · [MapItemDetailPresentationStyle](../mapitemdetailpresentationstyle.md)

# automatic(presentationViewController:)

<sub>Type Method</sub>

An appropriate presentation style will be chosen automatically.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static func automatic(presentationViewController: UIViewController? = nil) -> MKSelectionAccessory.MapItemDetailPresentationStyle
```

## Parameters

- `presentationViewController` — Supplying a non-nil presentationViewController will enable sheet presentation, if appropriate.

## See Also

### Creating a presentation style

- [automatic(presentationViewController:)](<automatic(presentationviewcontroller_)-9t9vt.md>) — An appropriate presentation style will be chosen automatically.
- [callout](callout.md) — Show map item detail as an annotation callout on the map.
- [callout(_:)](<callout(__).md>) — Show map item detail as an annotation callout on the map
- [openInMaps](openinmaps.md) — Display a small “Open in Apple Maps” link.
- [+ sheetPresentedFromViewController:](<sheet(presentedfrom_).md>) — Show map item detail by presenting a sheet.
