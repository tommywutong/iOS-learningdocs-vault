---
title: critical
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 13.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dialogseverity/critical
source_url: 'https://developer.apple.com/documentation/swiftui/dialogseverity/critical'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dialogseverity/critical.json'
content_hash: 'sha256:041cb67db992d678'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DialogSeverity](../dialogseverity.md)

# critical

<sub>Type Property</sub>

A severity that indicates extra attention should be given to the dialog, for example when unexpected data loss may occur as a result of the action taken.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let critical: DialogSeverity
```

## Discussion

On macOS, a dialog with critical severity will display a large caution symbol with the app icon as an overlay.

## See Also

### Getting severities

- [automatic](automatic.md) — The default dialog severity. Alerts that present an error will use `.critical` and all others will use `.standard`.
- [standard](standard.md) — A severity that indicates the dialog is being displayed for the purpose of presenting information to the user.
