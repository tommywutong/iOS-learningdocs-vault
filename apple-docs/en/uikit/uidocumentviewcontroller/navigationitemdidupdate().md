---
title: navigationItemDidUpdate()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentviewcontroller/navigationitemdidupdate()
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentviewcontroller/navigationitemdidupdate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentviewcontroller/navigationitemdidupdate%28%29.json'
content_hash: 'sha256:6693cee54912ee37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentViewController](../uidocumentviewcontroller.md)

# navigationItemDidUpdate()

<sub>Instance Method</sub>

Provides an opportunity to customize the navigation items after the navigation bar updates.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func navigationItemDidUpdate()
```

## Discussion

The system calls `navigationItemDidUpdate()` every time `UIDocumentViewController` makes changes to the navigation item. Customize the navigation items in this method.

This example adds buttons to the navigation bar and customizes the toolbar:

```swift
class EditorViewController:
        UIDocumentViewController,
        UINavigationItemRenameDelegate {

    override func navigationItemDidUpdate() {
        navigationItem.customizationIdentifier = "editorViewCustomization"
        configureCenterItemGroups()
        navigationItem.rightBarButtonItem = splitView.previewVisibilityBarButton
    }

}
```
