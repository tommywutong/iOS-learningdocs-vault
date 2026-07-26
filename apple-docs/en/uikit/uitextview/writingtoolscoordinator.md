---
title: writingToolsCoordinator
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextview/writingtoolscoordinator
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/writingtoolscoordinator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/writingtoolscoordinator.json'
content_hash: 'sha256:ff04e42ee2101150'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# writingToolsCoordinator

<sub>Instance Property</sub>

The object that coordinates interactions between Writing Tools and the text view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var writingToolsCoordinator: UIWritingToolsCoordinator { get }
```

## Discussion

When you get the value of this property, the system creates a Writing Tools coordinator object if one doesn’t already exist for this view.

## See Also

### Getting the Writing Tools configuration

- [writingToolsBehavior](writingtoolsbehavior.md) — The level of Writing Tools support to use in the text view.
- [allowedWritingToolsResultOptions](allowedwritingtoolsresultoptions.md) — The type of content Writing Tools generates for your text view.
- [writingToolsActive](iswritingtoolsactive.md) — A Boolean value that indicates whether the writing tools are currently interacting with the text view’s content.
- [subclassForWritingToolsCoordinator](subclassforwritingtoolscoordinator.md)
