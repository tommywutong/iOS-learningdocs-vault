---
title: 'close(completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocument/close(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/close(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/close%28completionhandler%3A%29.json'
content_hash: 'sha256:a3dfbd9c6aa1e117'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# close(completionHandler:)

<sub>Instance Method</sub>

Asynchronously closes the document after saving any changes.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func close(completionHandler: (@Sendable (Bool) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func close() async -> Bool
```

## Parameters

- `completionHandler` — A block with code to execute after the save-and-close operation concludes. The block returns no value and has one parameter: - **`success`** — [true](../../swift/true.md) if any save operation succeeds, otherwise [false](../../swift/false.md). The block is invoked on the main queue.

## Discussion

You call this method to begin the sequence of method calls that saves a document safely and asynchronously. The file-system location of the document derives from the [fileURL](fileurl.md) property. After the save operation concludes, the code in `completionHandler` is executed. In this code, you can close the document — for example, by removing the document’s view from the screen. Additionally, if the save operation didn’t succeed (`success` is [false](../../swift/false.md)), you can respond in an appropriate manner.

You typically wouldn’t override this method. The default implementation calls the [- autosaveWithCompletionHandler:](<autosave(completionhandler_).md>) method.

## See Also

### Writing document data

- [- contentsForType:error:](<contents(fortype_).md>) — Returns the document data to be saved.
- [- saveToURL:forSaveOperation:completionHandler:](<save(to_for_completionhandler_).md>) — Saves document data to the specified location in the application sandbox.
- [- writeContents:andAttributes:safelyToURL:forSaveOperation:error:](<writecontents(__andattributes_safelyto_for_).md>) — Ensures that document data is written safely to a specified location in the application sandbox.
- [- writeContents:toURL:forSaveOperation:originalContentsURL:error:](<writecontents(__to_for_originalcontentsurl_).md>) — Writes the document data to disk at the sandbox location indicated by a file URL.
- [savingFileType](savingfiletype.md) — Returns the file type to use for saving a document.
- [- fileAttributesToWriteToURL:forSaveOperation:error:](<fileattributestowrite(to_for_).md>) — Returns a dictionary of file attributes to associate with the document file when writing or updating it.
- [- fileNameExtensionForType:saveOperation:](<filenameextension(fortype_saveoperation_).md>) — Returns a file extension to append to the file URL of the document file being written.
