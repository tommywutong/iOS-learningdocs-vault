---
title: 'mapItemDetailSelectionAccessory(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapcontent/mapitemdetailselectionaccessory(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapcontent/mapitemdetailselectionaccessory(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcontent/mapitemdetailselectionaccessory%28_%3A%29.json'
content_hash: 'sha256:a2176e4aeb995d42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapContent](../mapcontent.md)

# mapItemDetailSelectionAccessory(_:)

<sub>Instance Method</sub>

Specifies the selection accessory to display for the selected map item content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func mapItemDetailSelectionAccessory(_ style: MapItemDetailSelectionAccessoryStyle? = .automatic) -> some MapContent

```

## Parameters

- `style` — The map item detail selection accessory style. If `nil`, no selection accessory appears.

## See Also

### Place information

- [MapItemDetailSelectionAccessoryStyle](../mapitemdetailselectionaccessorystyle.md) — The map item detail selection accessory style.
- [callout(_:)](<../mapitemdetailselectionaccessorystyle/callout(__).md>) — Presents the accessory as an annotation callout on the map.
