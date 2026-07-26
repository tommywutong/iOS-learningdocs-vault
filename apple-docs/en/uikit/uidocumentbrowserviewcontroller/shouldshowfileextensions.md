---
title: shouldShowFileExtensions
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentbrowserviewcontroller/shouldshowfileextensions
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/shouldshowfileextensions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontroller/shouldshowfileextensions.json'
content_hash: 'sha256:a243790a7fb648c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewController](../uidocumentbrowserviewcontroller.md)

# shouldShowFileExtensions

<sub>Instance Property</sub>

A Boolean value that determines whether the browser always shows file extensions.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var shouldShowFileExtensions: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md).

> [!note] Note
> This property has no effect in Mac apps built with Mac Catalyst.

## See Also

### Modifying the browser’s appearance

- [browserUserInterfaceStyle](browseruserinterfacestyle-swift.property.md) — The visual style for the document browser.
- [BrowserUserInterfaceStyle](browseruserinterfacestyle-swift.enum.md) — Styles that define the document browser’s appearance.
- [additionalLeadingNavigationBarButtonItems](additionalleadingnavigationbarbuttonitems.md) — Additional bar button items that the document browser displays on the leading side of its navigation bar.
- [additionalTrailingNavigationBarButtonItems](additionaltrailingnavigationbarbuttonitems.md) — Additional bar button items that the document browser displays on the trailing side of its navigation bar.
- [localizedCreateDocumentActionTitle](localizedcreatedocumentactiontitle.md) — The title for the Create Document button.
- [defaultDocumentAspectRatio](defaultdocumentaspectratio.md) — The aspect ratio for the Create Document button.
