---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uivideoeditorcontroller/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uivideoeditorcontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uivideoeditorcontroller/delegate.json'
content_hash: 'sha256:c698e73aef6c3df0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIVideoEditorController](../uivideoeditorcontroller.md)

# delegate

<sub>Instance Property</sub>

The video editor’s delegate object.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
unowned(unsafe) var delegate: (any UINavigationControllerDelegate & UIVideoEditorControllerDelegate)? { get set }
```

## Discussion

The delegate receives a notification when the system has finished saving an edited movie or when the user cancels the video editor. The delegate also decides when to dismiss the editor interface, so you must provide a delegate to use a video editor. If this property is `nil`, the editor is dismissed immediately if you try to show it. The delegate protocol is described in [UIVideoEditorControllerDelegate](../uivideoeditorcontrollerdelegate.md).

## See Also

### Managing changes to the video

- [UIVideoEditorControllerDelegate](../uivideoeditorcontrollerdelegate.md) — A set of methods that your delegate object must implement to respond to the video editor.
