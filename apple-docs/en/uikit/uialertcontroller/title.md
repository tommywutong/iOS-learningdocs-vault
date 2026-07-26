---
title: title
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uialertcontroller/title
source_url: 'https://developer.apple.com/documentation/uikit/uialertcontroller/title'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertcontroller/title.json'
content_hash: 'sha256:9d5a6374ad72ae27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertController](../uialertcontroller.md)

# title

<sub>Instance Property</sub>

The title of the alert.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var title: String? { get set }
```

## Discussion

The title string is displayed prominently in the alert or action sheet. You should use this string to get the user’s attention and communicate the reason for displaying the alert.

## See Also

### Configuring the alert

- [message](message.md) — Descriptive text that provides more details about the reason for the alert.
- [preferredStyle](preferredstyle.md) — The style of the alert controller.
- [Style](style.md) — Constants indicating the type of alert to display.
