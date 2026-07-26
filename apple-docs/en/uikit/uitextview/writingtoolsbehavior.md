---
title: writingToolsBehavior
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.4+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextview/writingtoolsbehavior
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/writingtoolsbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/writingtoolsbehavior.json'
content_hash: 'sha256:bbad8b0aa5baaa21'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# writingToolsBehavior

<sub>Instance Property</sub>

The level of Writing Tools support to use in the text view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var writingToolsBehavior: UIWritingToolsBehavior { get set }
```

## Discussion

The system chooses an initial value based on the device’s capabilities. The value in this property is never the default option, and is instead one of the specific options such as [UIWritingToolsBehaviorNone](../uiwritingtoolsbehavior/none.md), [UIWritingToolsBehaviorLimited](../uiwritingtoolsbehavior/limited.md), or [UIWritingToolsBehaviorComplete](../uiwritingtoolsbehavior/complete.md). Change the initial value to customize your text view’s Writing Tools support.

## See Also

### Getting the Writing Tools configuration

- [allowedWritingToolsResultOptions](allowedwritingtoolsresultoptions.md) — The type of content Writing Tools generates for your text view.
- [writingToolsActive](iswritingtoolsactive.md) — A Boolean value that indicates whether the writing tools are currently interacting with the text view’s content.
- [writingToolsCoordinator](writingtoolscoordinator.md) — The object that coordinates interactions between Writing Tools and the text view.
- [subclassForWritingToolsCoordinator](subclassforwritingtoolscoordinator.md)
