---
title: presentedItemDidChange()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilepresenter/presenteditemdidchange()
source_url: 'https://developer.apple.com/documentation/foundation/nsfilepresenter/presenteditemdidchange()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilepresenter/presenteditemdidchange%28%29.json'
content_hash: 'sha256:824e3c40e2ea4764'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFilePresenter](../nsfilepresenter.md)

# presentedItemDidChange()

<sub>Instance Method</sub>

Tells your object that the presented item’s contents or attributes changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func presentedItemDidChange()
```

## Discussion

You can use this method to update your internal data structures to reflect the changes to the presented item. This method reports both changes to the file’s contents, such as the data in a file or the files in a directory, or the attributes of the item, such as whether the Hide extension checkbox of a file was toggled.

Because this method notifies you of both attribute and content changes, you might want to check the modification date before needlessly rereading the contents of a file. To do that, you must store the date when your object last made changes to the file and compare that date with the item’s current modification date. Use the [- coordinateReadingItemAtURL:options:error:byAccessor:](<../nsfilecoordinator/coordinate(readingitemat_options_error_byaccessor_).md>) method of a file coordinator to ensure exclusive access to the file when reading the current modification date.

## See Also

### Handling Changes to Files

- [- savePresentedItemChangesWithCompletionHandler:](<savepresenteditemchanges(completionhandler_).md>) — Tells your object to save any unsaved changes for the presented item.
- [- accommodatePresentedItemDeletionWithCompletionHandler:](<accommodatepresenteditemdeletion(completionhandler_).md>) — Tells your object that its presented item is about to be deleted.
- [- presentedItemDidMoveToURL:](<presenteditemdidmove(to_).md>) — Tells your object that the presented item moved or was renamed.
