---
title: documentState
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocument/documentstate
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/documentstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/documentstate.json'
content_hash: 'sha256:286cae114092d392'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# documentState

<sub>Instance Property</sub>

The current state of the document.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var documentState: UIDocument.State { get }
```

## Discussion

When document state changes, the [UIDocument](../uidocument.md) object stores a constant identifying the new state in this property. See the [State](state.md) enum for descriptions of these constants. To receive notifications about changes in document state, observe the [UIDocumentStateChangedNotification](statechangednotification.md) notification.

## See Also

### Accessing document attributes

- [fileURL](fileurl.md) — The file URL you use to initialize the document.
- [localizedName](localizedname.md) — The localized name of the document.
- [fileType](filetype.md) — The file type of the document.
- [fileModificationDate](filemodificationdate.md) — The date and time your app last modified the document file.
- [progress](progress.md) — The upload or download progress of a document.
