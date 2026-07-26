---
title: browserUserInterfaceStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentbrowserviewcontroller/browseruserinterfacestyle-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/browseruserinterfacestyle-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontroller/browseruserinterfacestyle-swift.property.json'
content_hash: 'sha256:e06d9d88e4afd8d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewController](../uidocumentbrowserviewcontroller.md)

# browserUserInterfaceStyle

<sub>Instance Property</sub>

The visual style for the document browser.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var browserUserInterfaceStyle: UIDocumentBrowserViewController.BrowserUserInterfaceStyle { get set }
```

## Discussion

For a list of possible styles, see [BrowserUserInterfaceStyle](browseruserinterfacestyle-swift.enum.md).

> [!note] Note
> This property has no effect in Mac apps built with Mac Catalyst.

## See Also

### Modifying the browser’s appearance

- [BrowserUserInterfaceStyle](browseruserinterfacestyle-swift.enum.md) — Styles that define the document browser’s appearance.
- [additionalLeadingNavigationBarButtonItems](additionalleadingnavigationbarbuttonitems.md) — Additional bar button items that the document browser displays on the leading side of its navigation bar.
- [additionalTrailingNavigationBarButtonItems](additionaltrailingnavigationbarbuttonitems.md) — Additional bar button items that the document browser displays on the trailing side of its navigation bar.
- [shouldShowFileExtensions](shouldshowfileextensions.md) — A Boolean value that determines whether the browser always shows file extensions.
- [localizedCreateDocumentActionTitle](localizedcreatedocumentactiontitle.md) — The title for the Create Document button.
- [defaultDocumentAspectRatio](defaultdocumentaspectratio.md) — The aspect ratio for the Create Document button.
