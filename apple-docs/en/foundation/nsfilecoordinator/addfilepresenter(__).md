---
title: 'addFilePresenter(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilecoordinator/addfilepresenter(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilecoordinator/addfilepresenter(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilecoordinator/addfilepresenter%28_%3A%29.json'
content_hash: 'sha256:d8fd5a995b289938'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileCoordinator](../nsfilecoordinator.md)

# addFilePresenter(_:)

<sub>Type Method</sub>

Registers the specified file presenter object so that it can receive notifications.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func addFilePresenter(_ filePresenter: any NSFilePresenter)
```

## Parameters

- `filePresenter` — The file presenter object to register.

## Discussion

This method registers the file presenter object process wide. Thus, any file coordinator objects you create later automatically know about the file presenter object and know to message it when its file or directory is affected.

Be sure to balance calls to this method with a corresponding call to the [+ removeFilePresenter:](<removefilepresenter(__).md>) method. You must remove file presenters from the process wide registry before the object is deallocated, even in a garbage-collected application.

If you call this method while coordinated file operations are already under way in another process, your file presenter may not receive notifications for that operation. To prevent missing such notifications, create a file coordinator, call its  [- coordinateReadingItemAtURL:options:error:byAccessor:](<coordinate(readingitemat_options_error_byaccessor_).md>) method, and register your file presenter object there. If you are going to read a file and then create a file presenter for that file, both actions should occur in the same coordinated read block. Synchronizing on the presented file or directory guarantees that when your block executes, all other objects have completed any tasks and you have sole access to the item.

## See Also

### Managing File Presenters

- [+ removeFilePresenter:](<removefilepresenter(__).md>) — Unregisters the specified file presenter object.
- [filePresenters](filepresenters.md) — Returns an array containing the currently registered file presenter objects.
- [purposeIdentifier](purposeidentifier.md) — A string that uniquely identifies the file access that was performed by this file coordinator.
