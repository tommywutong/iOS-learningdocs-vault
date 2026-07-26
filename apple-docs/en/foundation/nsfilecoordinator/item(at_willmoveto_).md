---
title: 'item(at:willMoveTo:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilecoordinator/item(at:willmoveto:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilecoordinator/item(at:willmoveto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilecoordinator/item%28at%3Awillmoveto%3A%29.json'
content_hash: 'sha256:227cee859211f63c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileCoordinator](../nsfilecoordinator.md)

# item(at:willMoveTo:)

<sub>Instance Method</sub>

Announces that your app is moving a file to a new URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func item(at oldURL: URL, willMoveTo newURL: URL)
```

## Parameters

- `oldURL` — The old location of the file or directory.

- `newURL` — The new location of the file or directory.

## Discussion

This method is intended for apps that adopt App Sandbox.

Some apps need to rename files while saving them. For example, when a user adds an attachment to a rich text document, TextEdit changes the document’s filename extension from `.rtf` to `.rtfd`. In such a case, in a sandboxed app, you must call this method to declare your intent to rename a file without user approval.

After the renaming process succeeds, call the [- itemAtURL:didMoveToURL:](<item(at_didmoveto_).md>) method, with the same arguments, to provide your app with continued access to the file under its new name, while also giving up access to any file that appears with the old name.

If your macOS app is not sandboxed, this method serves no purpose. This method is nonfunctional in iOS.

## See Also

### Coordinating File Operations Synchronously

- [- coordinateReadingItemAtURL:options:error:byAccessor:](<coordinate(readingitemat_options_error_byaccessor_).md>) — Initiates a read operation on a single file or directory using the specified options.
- [- coordinateWritingItemAtURL:options:error:byAccessor:](<coordinate(writingitemat_options_error_byaccessor_).md>) — Initiates a write operation on a single file or directory using the specified options.
- [- coordinateReadingItemAtURL:options:writingItemAtURL:options:error:byAccessor:](<coordinate(readingitemat_options_writingitemat_options_error_byaccessor_).md>) — Initiates a read operation that contains a follow-up write operation.
- [- coordinateWritingItemAtURL:options:writingItemAtURL:options:error:byAccessor:](<coordinate(writingitemat_options_writingitemat_options_error_byaccessor_).md>) — Initiates a write operation that involves a secondary write operation.
- [- prepareForReadingItemsAtURLs:options:writingItemsAtURLs:options:error:byAccessor:](<prepare(forreadingitemsat_options_writingitemsat_options_error_byaccessor_).md>) — Prepare to read or write from multiple files in a single batch operation.
- [- itemAtURL:didMoveToURL:](<item(at_didmoveto_).md>) — Notifies relevant file presenters that the location of a file or directory changed.
- [- cancel](<cancel().md>) — Cancels any active file coordination calls.
