---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 13.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dialogseverity/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/dialogseverity/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dialogseverity/automatic.json'
content_hash: 'sha256:8cfb94f14ceccbce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DialogSeverity](../dialogseverity.md)

# automatic

<sub>Type Property</sub>

The default dialog severity. Alerts that present an error will use `.critical` and all others will use `.standard`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let automatic: DialogSeverity
```

## See Also

### Getting severities

- [standard](standard.md) — A severity that indicates the dialog is being displayed for the purpose of presenting information to the user.
- [critical](critical.md) — A severity that indicates extra attention should be given to the dialog, for example when unexpected data loss may occur as a result of the action taken.
