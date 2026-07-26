---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/defaultfocusevaluationpriority/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/defaultfocusevaluationpriority/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/defaultfocusevaluationpriority/automatic.json'
content_hash: 'sha256:1becb81dab34109d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DefaultFocusEvaluationPriority](../defaultfocusevaluationpriority.md)

# automatic

<sub>Type Property</sub>

Use the default focus preference when focus moves into the affected branch automatically, but ignore it when the movement is driven by a user-initiated navigation command.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let automatic: DefaultFocusEvaluationPriority
```

## See Also

### Getting the priorities

- [userInitiated](userinitiated.md) — Always use the default focus preference when focus moves into the affected branch.
