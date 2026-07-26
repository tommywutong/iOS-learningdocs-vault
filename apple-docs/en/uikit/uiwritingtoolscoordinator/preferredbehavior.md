---
title: preferredBehavior
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/preferredbehavior
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/preferredbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/preferredbehavior.json'
content_hash: 'sha256:3976d2db2306ddc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md)

# preferredBehavior

<sub>Instance Property</sub>

The level of Writing Tools support you want the system to provide for your view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var preferredBehavior: UIWritingToolsBehavior { get set }
```

## Discussion

Use this property to request an inline or panel-based experience, or to disable Writing Tools for your view altogether. The default value of this property is [UIWritingToolsBehaviorDefault](../uiwritingtoolsbehavior/default.md).

## See Also

### Configuring the experience

- [behavior](behavior.md) — The actual level of Writing Tools support the system provides for your view.
- [preferredResultOptions](preferredresultoptions.md) — The type of content you allow Writing Tools to generate for your custom text view.
- [resultOptions](resultoptions.md) — The type of content the system generates for your custom text view.
