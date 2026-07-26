---
title: 'removeFilePresenter(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilecoordinator/removefilepresenter(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilecoordinator/removefilepresenter(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilecoordinator/removefilepresenter%28_%3A%29.json'
content_hash: 'sha256:0878fe4be4878cb2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileCoordinator](../nsfilecoordinator.md)

# removeFilePresenter(_:)

<sub>Type Method</sub>

Unregisters the specified file presenter object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func removeFilePresenter(_ filePresenter: any NSFilePresenter)
```

## Parameters

- `filePresenter` — The file presenter object to unregister. If the object is not currently registered, this method does nothing.

## Discussion

Call this method to unregister file presenters before those objects are deallocated, even in a garbage-collected application.

## See Also

### Managing File Presenters

- [+ addFilePresenter:](<addfilepresenter(__).md>) — Registers the specified file presenter object so that it can receive notifications.
- [filePresenters](filepresenters.md) — Returns an array containing the currently registered file presenter objects.
- [purposeIdentifier](purposeidentifier.md) — A string that uniquely identifies the file access that was performed by this file coordinator.
