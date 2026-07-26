---
title: allowedWritingToolsResultOptions
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.4+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextview/allowedwritingtoolsresultoptions
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/allowedwritingtoolsresultoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/allowedwritingtoolsresultoptions.json'
content_hash: 'sha256:60d3965d3a797e4c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# allowedWritingToolsResultOptions

<sub>Instance Property</sub>

The type of content Writing Tools generates for your text view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var allowedWritingToolsResultOptions: UIWritingToolsResultOptions { get set }
```

## Discussion

Text views support most types of generated content. However, if you set this property to a value that includes the [UIWritingToolsResultTable](../uiwritingtoolsresultoptions/table.md) option, UIKit raises [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md).

## See Also

### Getting the Writing Tools configuration

- [writingToolsBehavior](writingtoolsbehavior.md) — The level of Writing Tools support to use in the text view.
- [writingToolsActive](iswritingtoolsactive.md) — A Boolean value that indicates whether the writing tools are currently interacting with the text view’s content.
- [writingToolsCoordinator](writingtoolscoordinator.md) — The object that coordinates interactions between Writing Tools and the text view.
- [subclassForWritingToolsCoordinator](subclassforwritingtoolscoordinator.md)
