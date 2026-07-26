---
title: localOnly
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/optionskey/localonly
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/optionskey/localonly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/optionskey/localonly.json'
content_hash: 'sha256:33ac73de98f0ebb6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIPasteboard](../../uipasteboard.md) · [OptionsKey](../optionskey.md)

# localOnly

<sub>Type Property</sub>

A Boolean value that specifies that the pasteboard items should not be available to other devices through the Handoff feature.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static let localOnly: UIPasteboard.OptionsKey
```

## Description

The value is expressed as an [NSNumber](../../../foundation/nsnumber.md) type.

## See Also

### Constants

- [UIPasteboardOptionExpirationDate](expirationdate.md) — The time and date that you want the system to remove the pasteboard items from the pasteboard.
