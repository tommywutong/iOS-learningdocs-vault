---
title: 'automatic(presentationViewController:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkselectionaccessory/mapitemdetailpresentationstyle/automatic(presentationviewcontroller:)-9t9vt'
source_url: 'https://developer.apple.com/documentation/mapkit/mkselectionaccessory/mapitemdetailpresentationstyle/automatic(presentationviewcontroller:)-9t9vt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkselectionaccessory/mapitemdetailpresentationstyle/automatic%28presentationviewcontroller%3A%29-9t9vt.json'
content_hash: 'sha256:80bff79c201c1f5a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKSelectionAccessory](../../mkselectionaccessory.md) · [MapItemDetailPresentationStyle](../mapitemdetailpresentationstyle.md)

# automatic(presentationViewController:)

<sub>Type Method</sub>

An appropriate presentation style will be chosen automatically.

<sub>macOS</sub>

```swift
static func automatic(presentationViewController: NSViewController? = nil) -> MKSelectionAccessory.MapItemDetailPresentationStyle
```

## Parameters

- `presentationViewController` — Supplying a non-nil presentationViewController will enable sheet presentation, if appropriate.

## See Also

### Creating a presentation style

- [automatic(presentationViewController:)](<automatic(presentationviewcontroller_)-648ee.md>) — An appropriate presentation style will be chosen automatically.
- [callout](callout.md) — Show map item detail as an annotation callout on the map.
- [callout(_:)](<callout(__).md>) — Show map item detail as an annotation callout on the map
- [openInMaps](openinmaps.md) — Display a small “Open in Apple Maps” link.
- [+ sheetPresentedFromViewController:](<sheet(presentedfrom_).md>) — Show map item detail by presenting a sheet.
