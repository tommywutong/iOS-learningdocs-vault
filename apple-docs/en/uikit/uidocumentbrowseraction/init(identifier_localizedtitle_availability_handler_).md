---
title: 'init(identifier:localizedTitle:availability:handler:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentbrowseraction/init(identifier:localizedtitle:availability:handler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowseraction/init(identifier:localizedtitle:availability:handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowseraction/init%28identifier%3Alocalizedtitle%3Aavailability%3Ahandler%3A%29.json'
content_hash: 'sha256:71d4b7b3440c3b2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserAction](../uidocumentbrowseraction.md)

# init(identifier:localizedTitle:availability:handler:)

<sub>Initializer</sub>

Instantiates and returns a new browser action item.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(identifier: String, localizedTitle: String, availability: UIDocumentBrowserAction.Availability, handler: @escaping ([URL]) -> Void)
```

## Parameters

- `identifier` — A unique identifier for the activity.

- `localizedTitle` — The title that appears in the Edit Menu or navigation bar. This title should be a [String](../../swift/string.md) returned by  [NSLocalizedString](../../foundation/nslocalizedstring.md).

- `availability` — A value that defines where the action can appear (in the menu, navigation bar, or both). For a list of valid values, see [Availability](availability-swift.struct.md).

- `handler` — A block that is called when the user triggers the action. The block takes the following parameter: - **urls** — An array of URLs for the documents that the user has selected. If the action’s [supportsMultipleItems](supportsmultipleitems.md)  property is [false](../../swift/false.md), this array contains one URL. Otherwise, it can contain one or more URLs.

## See Also

### Creating and configuring actions

- [image](image.md) — The action’s image displayed in the navigation bar.
- [supportedContentTypes](supportedcontenttypes.md) — An array of uniform type identifiers that define the types of documents that the action supports.
- [supportsMultipleItems](supportsmultipleitems.md) — A Boolean value that determines whether the action can be triggered on more than one document at a time.
