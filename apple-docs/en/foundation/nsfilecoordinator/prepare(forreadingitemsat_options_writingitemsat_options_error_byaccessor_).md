---
title: 'prepare(forReadingItemsAt:options:writingItemsAt:options:error:byAccessor:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilecoordinator/prepare(forreadingitemsat:options:writingitemsat:options:error:byaccessor:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilecoordinator/prepare(forreadingitemsat:options:writingitemsat:options:error:byaccessor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilecoordinator/prepare%28forreadingitemsat%3Aoptions%3Awritingitemsat%3Aoptions%3Aerror%3Abyaccessor%3A%29.json'
content_hash: 'sha256:ee7362882eacc1f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileCoordinator](../nsfilecoordinator.md)

# prepare(forReadingItemsAt:options:writingItemsAt:options:error:byAccessor:)

<sub>Instance Method</sub>

Prepare to read or write from multiple files in a single batch operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func prepare(forReadingItemsAt readingURLs: [URL], options readingOptions: NSFileCoordinator.ReadingOptions = [], writingItemsAt writingURLs: [URL], options writingOptions: NSFileCoordinator.WritingOptions = [], error outError: NSErrorPointer, byAccessor batchAccessor: (@escaping @Sendable () -> Void) -> Void)
```

## Parameters

- `readingURLs` — An array of [NSURL](../nsurl.md) objects identifying the items you want to read.

- `readingOptions` — One of the reading options described in [ReadingOptions](readingoptions.md). If you pass `0` for this parameter, the [- savePresentedItemChangesWithCompletionHandler:](<../nsfilepresenter/savepresenteditemchanges(completionhandler_).md>) method of relevant file presenters is called before your block executes.

- `writingURLs` — An array of [NSURL](../nsurl.md) objects identifying the items you want to write.

- `writingOptions` — One of the writing options described in [WritingOptions](writingoptions.md). The options you specify partially determine how file presenters are notified and how this file coordinator object waits to execute your block.

- `outError` — On input, a pointer to a pointer for an error object. If a file presenter encounters an error while preparing for this operation, that error is returned in this parameter and the block in the `writer` parameter is not executed. If you cancel this operation before the `batchAccessor` block is executed, this parameter contains an error object on output.

- `batchAccessor` — A [Block object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3) containing additional calls to methods of this class. The block takes the following parameter: - **completionHandler** — A completion handler block. The batch accessor must call the completion handler when it has finished its read and write calls.

## Discussion

Use this method to prepare the file coordinator for multiple read and write operations. Because file coordination requires interprocess communication, it is much more efficient to batch changes to large numbers of files and directories than to change each item individually. The file coordinator uses the values in the `readingURLs` and `writingURLs` parameters, together with reading and writing options, to prepare any relevant file presenters for the upcoming operations. Specifically, it uses these parameters in the same way as the [- coordinateReadingItemAtURL:options:error:byAccessor:](<coordinate(readingitemat_options_error_byaccessor_).md>) and [- coordinateWritingItemAtURL:options:error:byAccessor:](<coordinate(writingitemat_options_error_byaccessor_).md>) methods to determine which file presenter methods to call.

This method executes synchronously, blocking the current thread until the `batchAccessor` block finishes executing. The block you provide for the `batchAccessor` parameter does not perform the actual operations itself. Instead, you must call the individual coordinated read and write methods from inside the `batchAccessor` block. You must then call the completion handler after all the coordinated reads and writes have completed. You can call the completion handler from any thread.

Don’t simply pass this method all the URLs that are passed into the nested coordinate methods. Instead pass only the top-level files and directories involved in the operation. This method triggers messages to the file presenters of those items and to the file presenters of any items contained by those items.

In most cases, passing the same reading and writing options to both this method and the contained coordination operations is redundant. For example, it is often appropriate to pass [NSFileCoordinatorReadingWithoutChanges](readingoptions/withoutchanges.md) to nested read operations. This method has already triggered a call to [- savePresentedItemChangesWithCompletionHandler:](<../nsfilepresenter/savepresenteditemchanges(completionhandler_).md>). The individual read operations do not need to trigger additional calls.

## See Also

### Related Documentation

- [- coordinateAccessWithIntents:queue:byAccessor:](<coordinate(with_queue_byaccessor_).md>) — Performs a number of coordinated-read or -write operations asynchronously.

### Coordinating File Operations Synchronously

- [- coordinateReadingItemAtURL:options:error:byAccessor:](<coordinate(readingitemat_options_error_byaccessor_).md>) — Initiates a read operation on a single file or directory using the specified options.
- [- coordinateWritingItemAtURL:options:error:byAccessor:](<coordinate(writingitemat_options_error_byaccessor_).md>) — Initiates a write operation on a single file or directory using the specified options.
- [- coordinateReadingItemAtURL:options:writingItemAtURL:options:error:byAccessor:](<coordinate(readingitemat_options_writingitemat_options_error_byaccessor_).md>) — Initiates a read operation that contains a follow-up write operation.
- [- coordinateWritingItemAtURL:options:writingItemAtURL:options:error:byAccessor:](<coordinate(writingitemat_options_writingitemat_options_error_byaccessor_).md>) — Initiates a write operation that involves a secondary write operation.
- [- itemAtURL:willMoveToURL:](<item(at_willmoveto_).md>) — Announces that your app is moving a file to a new URL.
- [- itemAtURL:didMoveToURL:](<item(at_didmoveto_).md>) — Notifies relevant file presenters that the location of a file or directory changed.
- [- cancel](<cancel().md>) — Cancels any active file coordination calls.
