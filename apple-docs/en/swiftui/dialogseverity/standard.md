---
title: standard
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dialogseverity/standard
source_url: 'https://developer.apple.com/documentation/swiftui/dialogseverity/standard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dialogseverity/standard.json'
content_hash: 'sha256:5e8f47047f8220b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DialogSeverity](../dialogseverity.md)

# standard

<sub>Type Property</sub>

A severity that indicates the dialog is being displayed for the purpose of presenting information to the user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let standard: DialogSeverity
```

## See Also

### Getting severities

- [automatic](automatic.md) — The default dialog severity. Alerts that present an error will use `.critical` and all others will use `.standard`.
- [critical](critical.md) — A severity that indicates extra attention should be given to the dialog, for example when unexpected data loss may occur as a result of the action taken.
