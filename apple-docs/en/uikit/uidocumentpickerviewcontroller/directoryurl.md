---
title: directoryURL
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentpickerviewcontroller/directoryurl
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/directoryurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentpickerviewcontroller/directoryurl.json'
content_hash: 'sha256:a01d89452b6b0b16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentPickerViewController](../uidocumentpickerviewcontroller.md)

# directoryURL

<sub>Instance Property</sub>

The initial directory that the document picker displays.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var directoryURL: URL? { get set }
```

## Discussion

Set this property to specify the starting directory for the document picker. This property defaults to `nil`. If you specify a value, the document picker tries to start at the specified directory. Otherwise, it starts with the last directory chosen by the user.

The [directoryURL](directoryurl.md) property only returns a value when you explicitly set it. For example, it doesn’t calculate the default URL presented to the user when the property isn’t set.

> [!note] Note
> This property has no effect in Mac apps built with Mac Catalyst.

## See Also

### Getting the user-selected document

- [delegate](delegate.md) — An object that acts as the delegate of the view controller.
- [UIDocumentPickerDelegate](../uidocumentpickerdelegate.md) — A set of methods for tracking when the user selects a document or destination, or cancels the operation.
- [allowsMultipleSelection](allowsmultipleselection.md) — A Boolean value that determines whether the user can select more than one document at a time.
