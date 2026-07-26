---
title: preferredStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uialertcontroller/preferredstyle
source_url: 'https://developer.apple.com/documentation/uikit/uialertcontroller/preferredstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertcontroller/preferredstyle.json'
content_hash: 'sha256:f1eb3430d4bdd77d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertController](../uialertcontroller.md)

# preferredStyle

<sub>Instance Property</sub>

The style of the alert controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var preferredStyle: UIAlertController.Style { get }
```

## Discussion

The value of this property is set to the value you specified in the [+ alertControllerWithTitle:message:preferredStyle:](<init(title_message_preferredstyle_).md>) method. This value determines how the alert is displayed onscreen.

## See Also

### Configuring the alert

- [title](title.md) — The title of the alert.
- [message](message.md) — Descriptive text that provides more details about the reason for the alert.
- [Style](style.md) — Constants indicating the type of alert to display.
