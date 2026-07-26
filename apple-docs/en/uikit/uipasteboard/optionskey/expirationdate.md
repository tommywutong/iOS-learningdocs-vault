---
title: expirationDate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/optionskey/expirationdate
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/optionskey/expirationdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/optionskey/expirationdate.json'
content_hash: 'sha256:cb9de6bd01962f2d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIPasteboard](../../uipasteboard.md) · [OptionsKey](../optionskey.md)

# expirationDate

<sub>Type Property</sub>

The time and date that you want the system to remove the pasteboard items from the pasteboard.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static let expirationDate: UIPasteboard.OptionsKey
```

## Discussion

Specify the date and time as an [NSDate](../../../foundation/nsdate.md) value.

## See Also

### Constants

- [UIPasteboardOptionLocalOnly](localonly.md) — A Boolean value that specifies that the pasteboard items should not be available to other devices through the Handoff feature.
