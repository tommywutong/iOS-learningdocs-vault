---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextfield/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/delegate.json'
content_hash: 'sha256:80c557cc2e403c9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# delegate

<sub>Instance Property</sub>

The text field’s delegate.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var delegate: (any UITextFieldDelegate)? { get set }
```

## Discussion

A text field delegate responds to editing-related messages from the text field. You can use the delegate to respond to the text entered by the user and to some special commands, such as when the user taps Return.

> [!note] Note
> If the text field is a [UISearchTextField](../uisearchtextfield.md), set its delegate to an object that also conforms to the [UISearchTextFieldDelegate](../uisearchtextfielddelegate.md) protocol.

## See Also

### Validating and handling edits

- [UITextFieldDelegate](../uitextfielddelegate.md) — A set of optional methods to manage editing and validating text in a text field object.
