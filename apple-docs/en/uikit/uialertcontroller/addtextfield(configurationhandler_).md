---
title: 'addTextField(configurationHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uialertcontroller/addtextfield(configurationhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uialertcontroller/addtextfield(configurationhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertcontroller/addtextfield%28configurationhandler%3A%29.json'
content_hash: 'sha256:092ea259dbe7586f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertController](../uialertcontroller.md)

# addTextField(configurationHandler:)

<sub>Instance Method</sub>

Adds a text field to an alert.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addTextField(configurationHandler: ((UITextField) -> Void)? = nil)
```

## Parameters

- `configurationHandler` — A block for configuring the text field prior to displaying the alert. This block has no return value and takes a single parameter corresponding to the text field object. Use that parameter to change the text field properties.

## Discussion

Calling this method adds an editable text field to the alert. You can call this method more than once to add additional text fields. The text fields are stacked in the resulting alert.

You can add a text field only if the [preferredStyle](preferredstyle.md) property is set to [UIAlertControllerStyleAlert](style/alert.md).

## See Also

### Configuring text fields

- [textFields](textfields.md) — The array of text fields displayed by the alert.
