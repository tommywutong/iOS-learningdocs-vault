---
title: 'videoEditorController(_:didSaveEditedVideoToPath:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uivideoeditorcontrollerdelegate/videoeditorcontroller(_:didsaveeditedvideotopath:)'
source_url: 'https://developer.apple.com/documentation/uikit/uivideoeditorcontrollerdelegate/videoeditorcontroller(_:didsaveeditedvideotopath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uivideoeditorcontrollerdelegate/videoeditorcontroller%28_%3Adidsaveeditedvideotopath%3A%29.json'
content_hash: 'sha256:c3f5d10d74fc4b23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIVideoEditorControllerDelegate](../uivideoeditorcontrollerdelegate.md)

# videoEditorController(_:didSaveEditedVideoToPath:)

<sub>Instance Method</sub>

Notifies the delegate after the system finishes saving an edited movie.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func videoEditorController(_ editor: UIVideoEditorController, didSaveEditedVideoToPath editedVideoPath: String)
```

## Parameters

- `editor` — The video editor that has finished editing and saving a movie.

- `editedVideoPath` — The filesystem path to the edited movie.

## See Also

### Closing the video editor

- [- videoEditorControllerDidCancel:](<videoeditorcontrollerdidcancel(__).md>) — Notifies the delegate when the user cancels a movie editing operation.
