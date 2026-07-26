---
title: undoRedoItemGroup
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentviewcontroller/undoredoitemgroup
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentviewcontroller/undoredoitemgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentviewcontroller/undoredoitemgroup.json'
content_hash: 'sha256:0b16890c51eb3820'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentViewController](../uidocumentviewcontroller.md)

# undoRedoItemGroup

<sub>Instance Property</sub>

The group that contains the undo/redo buttons that this view controller adds to the navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var undoRedoItemGroup: UIBarButtonItemGroup { get }
```

## Discussion

If you want undo and redo buttons to appear in your `UIDocumentViewController`, add an `undoRedoItemGroup` to the navigation bar and ensure that your custom `UIDocument` has an undo manager assigned to it. `UIDocumentViewController` sets the hidden property of this group, depending on the availability of an undo manager. It automatically enables or disables the buttons inside the group, as necessary.
