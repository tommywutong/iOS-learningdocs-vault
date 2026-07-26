---
title: preferredResultOptions
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/preferredresultoptions
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/preferredresultoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/preferredresultoptions.json'
content_hash: 'sha256:fd354787555c01ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md)

# preferredResultOptions

<sub>Instance Property</sub>

The type of content you allow Writing Tools to generate for your custom text view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var preferredResultOptions: UIWritingToolsResultOptions { get set }
```

## Discussion

Writing Tools can create plain text or rich text, and it can format text using lists or tables as needed. If your view doesn’t support specific types of content, specify the types you do support in this property. The default value of this property is `UIWritingToolsResultOptions/default`, which lets the system determine the type of content to generate.

## See Also

### Configuring the experience

- [preferredBehavior](preferredbehavior.md) — The level of Writing Tools support you want the system to provide for your view.
- [behavior](behavior.md) — The actual level of Writing Tools support the system provides for your view.
- [resultOptions](resultoptions.md) — The type of content the system generates for your custom text view.
