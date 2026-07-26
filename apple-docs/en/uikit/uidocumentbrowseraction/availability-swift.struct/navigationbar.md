---
title: navigationBar
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentbrowseraction/availability-swift.struct/navigationbar
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowseraction/availability-swift.struct/navigationbar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowseraction/availability-swift.struct/navigationbar.json'
content_hash: 'sha256:3eca46ebde9eb8ce'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIDocumentBrowserAction](../../uidocumentbrowseraction.md) · [Availability](../availability-swift.struct.md)

# navigationBar

<sub>Type Property</sub>

An action that appears in the navigation bar when the user puts the document browser in Select mode.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static var navigationBar: UIDocumentBrowserAction.Availability { get }
```

## Discussion

The system enables this action as soon as the user makes a valid selection, as determined by the [supportedContentTypes](../supportedcontenttypes.md) and [supportsMultipleItems](../supportsmultipleitems.md) properties.

> [!note] Note
> In Mac apps built with Mac Catalyst, the system shows [UIDocumentBrowserActionAvailabilityNavigationBar](navigationbar.md) actions as [UIDocumentBrowserActionAvailabilityMenu](menu.md) actions.

## See Also

### Constants

- [UIDocumentBrowserActionAvailabilityMenu](menu.md) — An action that appears in the Edit Menu when the user long presses a supported document.
