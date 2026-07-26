---
title: defaultDocumentAspectRatio
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentbrowserviewcontroller/defaultdocumentaspectratio
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/defaultdocumentaspectratio'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontroller/defaultdocumentaspectratio.json'
content_hash: 'sha256:237d9cacda4ff532'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewController](../uidocumentbrowserviewcontroller.md)

# defaultDocumentAspectRatio

<sub>Instance Property</sub>

The aspect ratio for the Create Document button.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var defaultDocumentAspectRatio: CGFloat { get set }
```

## Discussion

The aspect ratio is defined as the button’s width divided by its height. The default is `2.0/3.0`.

## See Also

### Modifying the browser’s appearance

- [browserUserInterfaceStyle](browseruserinterfacestyle-swift.property.md) — The visual style for the document browser.
- [BrowserUserInterfaceStyle](browseruserinterfacestyle-swift.enum.md) — Styles that define the document browser’s appearance.
- [additionalLeadingNavigationBarButtonItems](additionalleadingnavigationbarbuttonitems.md) — Additional bar button items that the document browser displays on the leading side of its navigation bar.
- [additionalTrailingNavigationBarButtonItems](additionaltrailingnavigationbarbuttonitems.md) — Additional bar button items that the document browser displays on the trailing side of its navigation bar.
- [shouldShowFileExtensions](shouldshowfileextensions.md) — A Boolean value that determines whether the browser always shows file extensions.
- [localizedCreateDocumentActionTitle](localizedcreatedocumentactiontitle.md) — The title for the Create Document button.
