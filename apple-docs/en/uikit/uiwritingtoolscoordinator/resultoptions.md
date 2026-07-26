---
title: resultOptions
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/resultoptions
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/resultoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/resultoptions.json'
content_hash: 'sha256:aa589c02d3912f42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md)

# resultOptions

<sub>Instance Property</sub>

The type of content the system generates for your custom text view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var resultOptions: UIWritingToolsResultOptions { get }
```

## Discussion

This property contains the set of options that Writing Tools outputs for your view. Writing Tools takes the value in the [preferredResultOptions](preferredresultoptions.md) property into consideration when determining this value.

## See Also

### Configuring the experience

- [preferredBehavior](preferredbehavior.md) — The level of Writing Tools support you want the system to provide for your view.
- [behavior](behavior.md) — The actual level of Writing Tools support the system provides for your view.
- [preferredResultOptions](preferredresultoptions.md) — The type of content you allow Writing Tools to generate for your custom text view.
