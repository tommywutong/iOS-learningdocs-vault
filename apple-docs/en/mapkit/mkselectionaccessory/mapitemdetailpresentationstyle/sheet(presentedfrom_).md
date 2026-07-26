---
title: 'sheet(presentedFrom:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkselectionaccessory/mapitemdetailpresentationstyle/sheet(presentedfrom:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkselectionaccessory/mapitemdetailpresentationstyle/sheet(presentedfrom:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkselectionaccessory/mapitemdetailpresentationstyle/sheet%28presentedfrom%3A%29.json'
content_hash: 'sha256:5b0ec6b8660ca346'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKSelectionAccessory](../../mkselectionaccessory.md) · [MapItemDetailPresentationStyle](../mapitemdetailpresentationstyle.md)

# sheet(presentedFrom:)

<sub>Type Method</sub>

Show map item detail by presenting a sheet.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class func sheet(presentedFrom viewController: UIViewController) -> MKSelectionAccessory.MapItemDetailPresentationStyle
```

<sub>macOS</sub>

```swift
class func sheet(presentedFrom viewController: NSViewController) -> MKSelectionAccessory.MapItemDetailPresentationStyle
```

## Parameters

- `viewController` — The view controller that will present the sheet.

## See Also

### Creating a presentation style

- [automatic(presentationViewController:)](<automatic(presentationviewcontroller_)-648ee.md>) — An appropriate presentation style will be chosen automatically.
- [automatic(presentationViewController:)](<automatic(presentationviewcontroller_)-9t9vt.md>) — An appropriate presentation style will be chosen automatically.
- [callout](callout.md) — Show map item detail as an annotation callout on the map.
- [callout(_:)](<callout(__).md>) — Show map item detail as an annotation callout on the map
- [openInMaps](openinmaps.md) — Display a small “Open in Apple Maps” link.
