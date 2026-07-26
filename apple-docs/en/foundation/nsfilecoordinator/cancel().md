---
title: cancel()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilecoordinator/cancel()
source_url: 'https://developer.apple.com/documentation/foundation/nsfilecoordinator/cancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilecoordinator/cancel%28%29.json'
content_hash: 'sha256:fd2807c5e620cf24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileCoordinator](../nsfilecoordinator.md)

# cancel()

<sub>Instance Method</sub>

Cancels any active file coordination calls.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancel()
```

## Discussion

Use this method to cancel any active calls to coordinate the reading or writing of a file. If the block passed to the file coordination call has not yet been executed—perhaps because the file coordinator is still waiting for a response from other file presenters—the file coordinator method stops waiting for a response, does not execute its block, and returns an error object with the error code [NSUserCancelledError](../nsusercancellederror-swift.var.md). However, if the block is already being executed, the file coordinator method does not return until the block finishes executing.

You can call this method from any thread of your application and it returns immediately without waiting for the file coordinator object to respond. Thus, when this method returns, you cannot assume that the read or write operation occurred or did not occur. (In fact, it is possible for this method to return while the file coordinator is in the middle of executing a block.) If you want to know whether the operation actually occurred, you must track it yourself by setting a flag when the block starts executing or by using some other means.

## See Also

### Coordinating File Operations Synchronously

- [- coordinateReadingItemAtURL:options:error:byAccessor:](<coordinate(readingitemat_options_error_byaccessor_).md>) — Initiates a read operation on a single file or directory using the specified options.
- [- coordinateWritingItemAtURL:options:error:byAccessor:](<coordinate(writingitemat_options_error_byaccessor_).md>) — Initiates a write operation on a single file or directory using the specified options.
- [- coordinateReadingItemAtURL:options:writingItemAtURL:options:error:byAccessor:](<coordinate(readingitemat_options_writingitemat_options_error_byaccessor_).md>) — Initiates a read operation that contains a follow-up write operation.
- [- coordinateWritingItemAtURL:options:writingItemAtURL:options:error:byAccessor:](<coordinate(writingitemat_options_writingitemat_options_error_byaccessor_).md>) — Initiates a write operation that involves a secondary write operation.
- [- prepareForReadingItemsAtURLs:options:writingItemsAtURLs:options:error:byAccessor:](<prepare(forreadingitemsat_options_writingitemsat_options_error_byaccessor_).md>) — Prepare to read or write from multiple files in a single batch operation.
- [- itemAtURL:willMoveToURL:](<item(at_willmoveto_).md>) — Announces that your app is moving a file to a new URL.
- [- itemAtURL:didMoveToURL:](<item(at_didmoveto_).md>) — Notifies relevant file presenters that the location of a file or directory changed.
