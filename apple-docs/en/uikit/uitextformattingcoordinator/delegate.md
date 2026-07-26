---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextformattingcoordinator/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uitextformattingcoordinator/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextformattingcoordinator/delegate.json'
content_hash: 'sha256:67844fdb641ff99d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextFormattingCoordinator](../uitextformattingcoordinator.md)

# delegate

<sub>Instance Property</sub>

The delegate of the text-formatting coordinator.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var delegate: (any UITextFormattingCoordinatorDelegate)? { get set }
```

## See Also

### Applying Updated Text Attributes

- [UITextFormattingCoordinatorDelegate](../uitextformattingcoordinatordelegate.md) — The methods that delegates of text-formatting coordinators implement to apply font panel settings to the currently selected text.
