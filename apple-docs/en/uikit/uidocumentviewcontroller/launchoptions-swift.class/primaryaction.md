---
title: primaryAction
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentviewcontroller/launchoptions-swift.class/primaryaction
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentviewcontroller/launchoptions-swift.class/primaryaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentviewcontroller/launchoptions-swift.class/primaryaction.json'
content_hash: 'sha256:6e473ba6068f3e10'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIDocumentViewController](../../uidocumentviewcontroller.md) · [LaunchOptions](../launchoptions-swift.class.md)

# primaryAction

<sub>Instance Property</sub>

The launch scene’s primary action.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@NSCopying var primaryAction: UIAction? { get set }
```

## Discussion

Set this property to customize the primary action’s button in the document launch scene. If you don’t set this property, the system adds a default Create Document button to the title view.

## See Also

### Adding actions

- [secondaryAction](secondaryaction.md) — The launch scene’s secondary action.
