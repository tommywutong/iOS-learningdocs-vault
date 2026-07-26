---
title: additionalTrailingNavigationBarButtonItems
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentbrowserviewcontroller/additionaltrailingnavigationbarbuttonitems
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/additionaltrailingnavigationbarbuttonitems'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontroller/additionaltrailingnavigationbarbuttonitems.json'
content_hash: 'sha256:85a0f4b5545acb28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewController](../uidocumentbrowserviewcontroller.md)

# additionalTrailingNavigationBarButtonItems

<sub>Instance Property</sub>

Additional bar button items that the document browser displays on the trailing side of its navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var additionalTrailingNavigationBarButtonItems: [UIBarButtonItem] { get set }
```

## Discussion

Actions triggered by these items don’t have any access to the browser’s content or to the URLs of selected items. Use these bar button items for global actions only (actions that don’t affect a specific document or folder).

> [!note] Note
> Bar button items added using this property don’t appear in Mac apps built with Mac Catalyst. You must find another way to display these actions (for example, using [UIMenuBuilder](../uimenubuilder.md) to add the actions to your app’s menu).

## See Also

### Modifying the browser’s appearance

- [browserUserInterfaceStyle](browseruserinterfacestyle-swift.property.md) — The visual style for the document browser.
- [BrowserUserInterfaceStyle](browseruserinterfacestyle-swift.enum.md) — Styles that define the document browser’s appearance.
- [additionalLeadingNavigationBarButtonItems](additionalleadingnavigationbarbuttonitems.md) — Additional bar button items that the document browser displays on the leading side of its navigation bar.
- [shouldShowFileExtensions](shouldshowfileextensions.md) — A Boolean value that determines whether the browser always shows file extensions.
- [localizedCreateDocumentActionTitle](localizedcreatedocumentactiontitle.md) — The title for the Create Document button.
- [defaultDocumentAspectRatio](defaultdocumentaspectratio.md) — The aspect ratio for the Create Document button.
