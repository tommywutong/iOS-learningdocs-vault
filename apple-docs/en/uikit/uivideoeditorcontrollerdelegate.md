---
title: UIVideoEditorControllerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uivideoeditorcontrollerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uivideoeditorcontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uivideoeditorcontrollerdelegate.json'
content_hash: 'sha256:466f431ba60d8af3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIVideoEditorControllerDelegate

<sub>Protocol</sub>

A set of methods that your delegate object must implement to respond to the video editor.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIVideoEditorControllerDelegate : NSObjectProtocol
```

## Overview

The methods of this protocol notify your delegate when the system has saved an edited movie or the user has canceled editing to discard any changes. There’s also a method for responding to errors encountered by the video editor.

The delegate methods are responsible for dismissing the video editor when the operation completes. To dismiss the editor, call the [- dismissViewControllerAnimated:completion:](<uiviewcontroller/dismiss(animated_completion_).md>) method of the parent controller responsible for displaying the video editor. The video editor is described in [UIVideoEditorController](uivideoeditorcontroller.md).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Closing the video editor

- [- videoEditorController:didSaveEditedVideoToPath:](<uivideoeditorcontrollerdelegate/videoeditorcontroller(__didsaveeditedvideotopath_).md>) — Notifies the delegate after the system finishes saving an edited movie.
- [- videoEditorControllerDidCancel:](<uivideoeditorcontrollerdelegate/videoeditorcontrollerdidcancel(__).md>) — Notifies the delegate when the user cancels a movie editing operation.

### Handling errors

- [- videoEditorController:didFailWithError:](<uivideoeditorcontrollerdelegate/videoeditorcontroller(__didfailwitherror_).md>) — Notifies the delegate when the video editor is unable to load or save a movie.

## See Also

### Managing changes to the video

- [delegate](uivideoeditorcontroller/delegate.md) — The video editor’s delegate object.
