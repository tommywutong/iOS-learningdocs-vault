---
title: 'save(to:for:completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocument/save(to:for:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/save(to:for:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/save%28to%3Afor%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:3ea7127767cf3578'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# save(to:for:completionHandler:)

<sub>Instance Method</sub>

Saves document data to the specified location in the application sandbox.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func save(to url: URL, for saveOperation: UIDocument.SaveOperation, completionHandler: (@Sendable (Bool) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func save(to url: URL, for saveOperation: UIDocument.SaveOperation) async -> Bool
```

## Parameters

- `url` — The file URL identifying the location in the application sandbox to write the document data to. Typically, this is the URL obtained from the [fileURL](fileurl.md) property.

- `saveOperation` — A constant that indicates whether the document file is being written the first time or whether it is being overwritten. See [SaveOperation](saveoperation.md) for details.

- `completionHandler` — A block with code that is executed when the save operation concludes. The block returns no value and has one parameter: - **`success`** — [true](../../swift/true.md) if the save operation succeeds, otherwise [false](../../swift/false.md). This block is invoked on the calling queue.

## Discussion

The default implementation of this method first calls the [- contentsForType:error:](<contents(fortype_).md>) method synchronously on the calling queue to get the document data to save. Then it calls the [- writeContents:andAttributes:safelyToURL:forSaveOperation:error:](<writecontents(__andattributes_safelyto_for_).md>) method on a background queue to perform the actual writing of the data to disk.

If you override this method, it’s recommended that you first call the superclass implementation of the method (`super`). If you do not call `super`, you must do two things:

- Call [- performAsynchronousFileAccessUsingBlock:](<performasynchronousfileaccess(__).md>) to put the save operation on a background queue.
- In the block parameter, implement coordinated writing by using the [NSFileCoordinator](../../foundation/nsfilecoordinator.md) class.
- From within the coordinated write, call [- writeContents:andAttributes:safelyToURL:forSaveOperation:error:](<writecontents(__andattributes_safelyto_for_).md>).

## See Also

### Writing document data

- [- closeWithCompletionHandler:](<close(completionhandler_).md>) — Asynchronously closes the document after saving any changes.
- [- contentsForType:error:](<contents(fortype_).md>) — Returns the document data to be saved.
- [- writeContents:andAttributes:safelyToURL:forSaveOperation:error:](<writecontents(__andattributes_safelyto_for_).md>) — Ensures that document data is written safely to a specified location in the application sandbox.
- [- writeContents:toURL:forSaveOperation:originalContentsURL:error:](<writecontents(__to_for_originalcontentsurl_).md>) — Writes the document data to disk at the sandbox location indicated by a file URL.
- [savingFileType](savingfiletype.md) — Returns the file type to use for saving a document.
- [- fileAttributesToWriteToURL:forSaveOperation:error:](<fileattributestowrite(to_for_).md>) — Returns a dictionary of file attributes to associate with the document file when writing or updating it.
- [- fileNameExtensionForType:saveOperation:](<filenameextension(fortype_saveoperation_).md>) — Returns a file extension to append to the file URL of the document file being written.
