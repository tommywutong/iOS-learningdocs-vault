---
title: behavior
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/behavior
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/behavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/behavior.json'
content_hash: 'sha256:06cfb032c4c32bb5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md)

# behavior

<sub>Instance Property</sub>

The actual level of Writing Tools support the system provides for your view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var behavior: UIWritingToolsBehavior { get }
```

## Discussion

The system chooses this value based on the device capabilities, and takes the value in the [preferredBehavior](preferredbehavior.md) property into consideration when making the choice. The value in this property is never the default option, and is instead one of the specific options such as [UIWritingToolsBehaviorNone](../uiwritingtoolsbehavior/none.md), [UIWritingToolsBehaviorLimited](../uiwritingtoolsbehavior/limited.md), or [UIWritingToolsBehaviorComplete](../uiwritingtoolsbehavior/complete.md).

## See Also

### Configuring the experience

- [preferredBehavior](preferredbehavior.md) — The level of Writing Tools support you want the system to provide for your view.
- [preferredResultOptions](preferredresultoptions.md) — The type of content you allow Writing Tools to generate for your custom text view.
- [resultOptions](resultoptions.md) — The type of content the system generates for your custom text view.
