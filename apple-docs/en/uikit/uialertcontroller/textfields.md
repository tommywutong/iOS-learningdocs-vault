---
title: textFields
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uialertcontroller/textfields
source_url: 'https://developer.apple.com/documentation/uikit/uialertcontroller/textfields'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertcontroller/textfields.json'
content_hash: 'sha256:73e1fcd7cef00f40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertController](../uialertcontroller.md)

# textFields

<sub>Instance Property</sub>

The array of text fields displayed by the alert.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var textFields: [UITextField]? { get }
```

## Discussion

Use this property to access the text fields displayed by the alert. The text fields are in the order in which you added them to the alert controller. This order also corresponds to the order in which they are displayed in the alert.

## See Also

### Configuring text fields

- [- addTextFieldWithConfigurationHandler:](<addtextfield(configurationhandler_).md>) — Adds a text field to an alert.
