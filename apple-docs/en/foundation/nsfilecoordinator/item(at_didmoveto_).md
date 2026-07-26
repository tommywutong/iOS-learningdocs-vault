---
title: 'item(at:didMoveTo:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilecoordinator/item(at:didmoveto:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilecoordinator/item(at:didmoveto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilecoordinator/item%28at%3Adidmoveto%3A%29.json'
content_hash: 'sha256:1eb8d5690eb01cd1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileCoordinator](../nsfilecoordinator.md)

# item(at:didMoveTo:)

<sub>Instance Method</sub>

Notifies relevant file presenters that the location of a file or directory changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func item(at oldURL: URL, didMoveTo newURL: URL)
```

## Parameters

- `oldURL` — The old location of the file or directory.

- `newURL` — The new location of the file or directory.

## Discussion

If you move or rename a file or directory as part of a write operation, call this method to notify relevant file presenters that the change occurred. This method calls the [- presentedItemDidMoveToURL:](<../nsfilepresenter/presenteditemdidmove(to_).md>) method for any of the item’s file presenters.  If the item is a directory, this method calls [- presentedItemDidMoveToURL:](<../nsfilepresenter/presenteditemdidmove(to_).md>) on the file presenters for the item’s contents. Finally, it calls [- presentedSubitemAtURL:didMoveToURL:](<../nsfilepresenter/presentedsubitem(at_didmoveto_).md>) on the file presenter of any directory containing the item.

You must call this method from a coordinated write block. Calling this method with the same URL in the `oldURL` and `newURL` parameters is harmless. This call must balance a call to [- itemAtURL:willMoveToURL:](<item(at_willmoveto_).md>).

## See Also

### Coordinating File Operations Synchronously

- [- coordinateReadingItemAtURL:options:error:byAccessor:](<coordinate(readingitemat_options_error_byaccessor_).md>) — Initiates a read operation on a single file or directory using the specified options.
- [- coordinateWritingItemAtURL:options:error:byAccessor:](<coordinate(writingitemat_options_error_byaccessor_).md>) — Initiates a write operation on a single file or directory using the specified options.
- [- coordinateReadingItemAtURL:options:writingItemAtURL:options:error:byAccessor:](<coordinate(readingitemat_options_writingitemat_options_error_byaccessor_).md>) — Initiates a read operation that contains a follow-up write operation.
- [- coordinateWritingItemAtURL:options:writingItemAtURL:options:error:byAccessor:](<coordinate(writingitemat_options_writingitemat_options_error_byaccessor_).md>) — Initiates a write operation that involves a secondary write operation.
- [- prepareForReadingItemsAtURLs:options:writingItemsAtURLs:options:error:byAccessor:](<prepare(forreadingitemsat_options_writingitemsat_options_error_byaccessor_).md>) — Prepare to read or write from multiple files in a single batch operation.
- [- itemAtURL:willMoveToURL:](<item(at_willmoveto_).md>) — Announces that your app is moving a file to a new URL.
- [- cancel](<cancel().md>) — Cancels any active file coordination calls.
