---
title: 'writeContents(_:andAttributes:safelyTo:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocument/writecontents(_:andattributes:safelyto:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/writecontents(_:andattributes:safelyto:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/writecontents%28_%3Aandattributes%3Asafelyto%3Afor%3A%29.json'
content_hash: 'sha256:486e3e9d62db2e7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# writeContents(_:andAttributes:safelyTo:for:)

<sub>Instance Method</sub>

Ensures that document data is written safely to a specified location in the application sandbox.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func writeContents(_ contents: Any, andAttributes additionalFileAttributes: [AnyHashable : Any]? = nil, safelyTo url: URL, for saveOperation: UIDocument.SaveOperation) throws
```

## Parameters

- `contents` — The document data to write to disk. Typically, the data is encapsulated by an [NSData](../../foundation/nsdata.md) object (if a flat file) or an [FileWrapper](../../foundation/filewrapper.md) object (if a file package). If the object encapsulating the document data is of some other type, you should override this method or [- writeContents:toURL:forSaveOperation:originalContentsURL:error:](<writecontents(__to_for_originalcontentsurl_).md>) to perform the actual writing of the data.

- `additionalFileAttributes` — A dictionary of [FileManager](../../foundation/filemanager.md) file attributes to assign to the document file. The default implementation obtains these file attributes by calling [- fileAttributesToWriteToURL:forSaveOperation:error:](<fileattributestowrite(to_for_).md>).

- `url` — The file URL specifying the location of the document file in the application sandbox.

- `saveOperation` — A constant that indicates whether the document file is being written the first time or whether it is being overwritten. See [SaveOperation](saveoperation.md) for details.

## Discussion

This method is called by the [- saveToURL:forSaveOperation:completionHandler:](<save(to_for_completionhandler_).md>) method to save the file data (and associated attributes in the case of an [FileWrapper](../../foundation/filewrapper.md)). It creates temporary files and directories as necessary so that successful saves can be completed atomically and failed saves can be rolled back cleanly. This method calls [- writeContents:toURL:forSaveOperation:originalContentsURL:error:](<writecontents(__to_for_originalcontentsurl_).md>) to save the `contents` object, passing the location for the new saved file in the `toURL` parameter and the location of the previously existing file in the `originalContentsURL` parameter, if this is an overwrite operation.

If you want to change how file data is saved, you generally override the [- writeContents:toURL:forSaveOperation:originalContentsURL:error:](<writecontents(__to_for_originalcontentsurl_).md>) method instead of this method. Additionally, you don’t need to call this method directly unless you are overriding the [- saveToURL:forSaveOperation:completionHandler:](<save(to_for_completionhandler_).md>) method.

> [!note] Handling Errors in Swift
> In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> When overriding this method, use the `throw` statement to throw an `NSError`, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Writing document data

- [- closeWithCompletionHandler:](<close(completionhandler_).md>) — Asynchronously closes the document after saving any changes.
- [- contentsForType:error:](<contents(fortype_).md>) — Returns the document data to be saved.
- [- saveToURL:forSaveOperation:completionHandler:](<save(to_for_completionhandler_).md>) — Saves document data to the specified location in the application sandbox.
- [- writeContents:toURL:forSaveOperation:originalContentsURL:error:](<writecontents(__to_for_originalcontentsurl_).md>) — Writes the document data to disk at the sandbox location indicated by a file URL.
- [savingFileType](savingfiletype.md) — Returns the file type to use for saving a document.
- [- fileAttributesToWriteToURL:forSaveOperation:error:](<fileattributestowrite(to_for_).md>) — Returns a dictionary of file attributes to associate with the document file when writing or updating it.
- [- fileNameExtensionForType:saveOperation:](<filenameextension(fortype_saveoperation_).md>) — Returns a file extension to append to the file URL of the document file being written.
