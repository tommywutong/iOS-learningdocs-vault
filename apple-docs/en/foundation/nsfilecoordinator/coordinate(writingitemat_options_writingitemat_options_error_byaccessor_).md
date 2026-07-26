---
title: 'coordinate(writingItemAt:options:writingItemAt:options:error:byAccessor:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilecoordinator/coordinate(writingitemat:options:writingitemat:options:error:byaccessor:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilecoordinator/coordinate(writingitemat:options:writingitemat:options:error:byaccessor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilecoordinator/coordinate%28writingitemat%3Aoptions%3Awritingitemat%3Aoptions%3Aerror%3Abyaccessor%3A%29.json'
content_hash: 'sha256:b949f4cffab12561'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileCoordinator](../nsfilecoordinator.md)

# coordinate(writingItemAt:options:writingItemAt:options:error:byAccessor:)

<sub>Instance Method</sub>

Initiates a write operation that involves a secondary write operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func coordinate(writingItemAt url1: URL, options options1: NSFileCoordinator.WritingOptions = [], writingItemAt url2: URL, options options2: NSFileCoordinator.WritingOptions = [], error outError: NSErrorPointer, byAccessor writer: (URL, URL) -> Void)
```

## Parameters

- `url1` — A URL identifying the first file or directory to write. If other objects or processes are acting on the item at the URL, the actual URL passed to the block in the `writer` parameter may be different from the one in this parameter.

- `options1` — One of the writing options described in [WritingOptions](writingoptions.md).

- `url2` — A URL identifying the other file or directory to write. If other objects or processes are acting on the item at the URL, the actual URL passed to the block in the `writer` parameter may be different from the one in this parameter.

- `options2` — One of the writing options described in [WritingOptions](writingoptions.md). The options you specify partially determine how file presenters are notified and how this file coordinator object waits to execute your block.

- `outError` — On input, a pointer to a pointer for an error object. If a file presenter encounters an error while preparing for this operation, that error is returned in this parameter and the block in the `writer` parameter is not executed. If you cancel this operation before the `writer` block is executed, this parameter contains an error object on output.

- `writer` — A [Block object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3) containing the write operations you want to perform in a coordinated manner. This block receives [NSURL](../nsurl.md) objects containing the URLs of the items to write and returns no value. Always use the URLs passed into the block instead of the values in the `url1` and `url2` parameters.

## Discussion

When invoking these methods, declare a `__block` variable before the accessor block and initialize it to a value that signals failure, and then inside the accessor block set it to a value that indicates success. If the coordinated operation fails, then the accessor block never runs. The sentinel variable still holds a value that indicates failure, and the [NSError](../nserror.md) out parameter contains a reference that describes the error.

You use this method to perform two write operations without the risk of those operations creating a deadlock. This method executes synchronously, blocking the current thread until the `writer` block finishes executing. You may call the [- coordinateWritingItemAtURL:options:error:byAccessor:](<coordinate(writingitemat_options_error_byaccessor_).md>) method from your `writer` block. This method does the canonical lock ordering that is required to prevent a potential deadlock of the file operations.

This method makes the same calls to file presenters, and has the same general wait behavior, as the [- coordinateWritingItemAtURL:options:error:byAccessor:](<coordinate(writingitemat_options_error_byaccessor_).md>) method.

## See Also

### Coordinating File Operations Synchronously

- [- coordinateReadingItemAtURL:options:error:byAccessor:](<coordinate(readingitemat_options_error_byaccessor_).md>) — Initiates a read operation on a single file or directory using the specified options.
- [- coordinateWritingItemAtURL:options:error:byAccessor:](<coordinate(writingitemat_options_error_byaccessor_).md>) — Initiates a write operation on a single file or directory using the specified options.
- [- coordinateReadingItemAtURL:options:writingItemAtURL:options:error:byAccessor:](<coordinate(readingitemat_options_writingitemat_options_error_byaccessor_).md>) — Initiates a read operation that contains a follow-up write operation.
- [- prepareForReadingItemsAtURLs:options:writingItemsAtURLs:options:error:byAccessor:](<prepare(forreadingitemsat_options_writingitemsat_options_error_byaccessor_).md>) — Prepare to read or write from multiple files in a single batch operation.
- [- itemAtURL:willMoveToURL:](<item(at_willmoveto_).md>) — Announces that your app is moving a file to a new URL.
- [- itemAtURL:didMoveToURL:](<item(at_didmoveto_).md>) — Notifies relevant file presenters that the location of a file or directory changed.
- [- cancel](<cancel().md>) — Cancels any active file coordination calls.
