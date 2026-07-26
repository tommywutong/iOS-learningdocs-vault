---
title: 'videoEditorControllerDidCancel(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uivideoeditorcontrollerdelegate/videoeditorcontrollerdidcancel(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uivideoeditorcontrollerdelegate/videoeditorcontrollerdidcancel(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uivideoeditorcontrollerdelegate/videoeditorcontrollerdidcancel%28_%3A%29.json'
content_hash: 'sha256:102b456a11a43864'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIVideoEditorControllerDelegate](../uivideoeditorcontrollerdelegate.md)

# videoEditorControllerDidCancel(_:)

<sub>Instance Method</sub>

Notifies the delegate when the user cancels a movie editing operation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func videoEditorControllerDidCancel(_ editor: UIVideoEditorController)
```

## Parameters

- `editor` — The video editor that the user canceled, not wanting to save changes.

## See Also

### Closing the video editor

- [- videoEditorController:didSaveEditedVideoToPath:](<videoeditorcontroller(__didsaveeditedvideotopath_).md>) — Notifies the delegate after the system finishes saving an edited movie.
