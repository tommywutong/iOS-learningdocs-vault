---
title: displayName
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprinterdestination/displayname
source_url: 'https://developer.apple.com/documentation/uikit/uiprinterdestination/displayname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinterdestination/displayname.json'
content_hash: 'sha256:54ab737a99422a57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrinterDestination](../uiprinterdestination.md)

# displayName

<sub>Instance Property</sub>

A human-readable string that displays the name of a printer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var displayName: String? { get set }
```

## Discussion

This property contains a name that describes the printer’s manufacturer and model number to display in the app’s user interface. If `nil`, the [txtRecord](txtrecord.md) property can produce the display name.

## See Also

### Describing the printer

- [txtRecord](txtrecord.md) — A DNS TXT record to identify the printer.
- [URL](url.md) — The address of the printer.
