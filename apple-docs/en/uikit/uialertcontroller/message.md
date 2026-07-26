---
title: message
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uialertcontroller/message
source_url: 'https://developer.apple.com/documentation/uikit/uialertcontroller/message'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertcontroller/message.json'
content_hash: 'sha256:97c7a07b1622b804'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertController](../uialertcontroller.md)

# message

<sub>Instance Property</sub>

Descriptive text that provides more details about the reason for the alert.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var message: String? { get set }
```

## Discussion

The message string is displayed below the title string and is less prominent. Use this string to provide additional context about the reason for the alert or about the actions that the user might take.

## See Also

### Configuring the alert

- [title](title.md) — The title of the alert.
- [preferredStyle](preferredstyle.md) — The style of the alert controller.
- [Style](style.md) — Constants indicating the type of alert to display.
