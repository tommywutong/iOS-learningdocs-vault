---
title: isWritingToolsActive
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.4+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextview/iswritingtoolsactive
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/iswritingtoolsactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/iswritingtoolsactive.json'
content_hash: 'sha256:a75f2a6238e0ea68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# isWritingToolsActive

<sub>Instance Property</sub>

A Boolean value that indicates whether the writing tools are currently interacting with the text view’s content.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isWritingToolsActive: Bool { get }
```

## Discussion

Use this property to determine when someone is using the writing tools to rewrite text in the current text view. When writing tools are active, the system can change significant portions of the text view’s content. You might use this property to prevent your app from performing actions that interfere with those changes. For example, you might stop synchronizing text to iCloud while the UI is active.

To receive notifications when writing tools interactions start and stop, implement the  [- textViewWritingToolsWillBegin:](<../uitextviewdelegate/textviewwritingtoolswillbegin(__).md>) and [- textViewWritingToolsDidEnd:](<../uitextviewdelegate/textviewwritingtoolsdidend(__).md>) delegate methods.

## See Also

### Getting the Writing Tools configuration

- [writingToolsBehavior](writingtoolsbehavior.md) — The level of Writing Tools support to use in the text view.
- [allowedWritingToolsResultOptions](allowedwritingtoolsresultoptions.md) — The type of content Writing Tools generates for your text view.
- [writingToolsCoordinator](writingtoolscoordinator.md) — The object that coordinates interactions between Writing Tools and the text view.
- [subclassForWritingToolsCoordinator](subclassforwritingtoolscoordinator.md)
