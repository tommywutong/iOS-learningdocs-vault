---
title: secondaryAction
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentviewcontroller/launchoptions-swift.class/secondaryaction
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentviewcontroller/launchoptions-swift.class/secondaryaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentviewcontroller/launchoptions-swift.class/secondaryaction.json'
content_hash: 'sha256:630762e9092449eb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIDocumentViewController](../../uidocumentviewcontroller.md) · [LaunchOptions](../launchoptions-swift.class.md)

# secondaryAction

<sub>Instance Property</sub>

The launch scene’s secondary action.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@NSCopying var secondaryAction: UIAction? { get set }
```

## Discussion

Set this property to add a secondary action to the document launch scene. If you set this property, the system adds a button for the secondary action to the title view.

## See Also

### Adding actions

- [primaryAction](primaryaction.md) — The launch scene’s primary action.
