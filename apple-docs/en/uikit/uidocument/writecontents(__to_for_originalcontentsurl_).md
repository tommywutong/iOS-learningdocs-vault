---
title: 'writeContents(_:to:for:originalContentsURL:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocument/writecontents(_:to:for:originalcontentsurl:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/writecontents(_:to:for:originalcontentsurl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/writecontents%28_%3Ato%3Afor%3Aoriginalcontentsurl%3A%29.json'
content_hash: 'sha256:632f90119658df64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# writeContents(_:to:for:originalContentsURL:)

<sub>Instance Method</sub>

Writes the document data to disk at the sandbox location indicated by a file URL.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func writeContents(_ contents: Any, to url: URL, for saveOperation: UIDocument.SaveOperation, originalContentsURL: URL?) throws
```

## Parameters

- `contents` — The document data to write to disk. Typically, the data is encapsulated by an [NSData](../../foundation/nsdata.md) object (if a flat file) or an [FileWrapper](../../foundation/filewrapper.md) object (if a file package). If the object encapsulating the document data is of some other type, you should override this method or [- writeContents:andAttributes:safelyToURL:forSaveOperation:error:](<writecontents(__andattributes_safelyto_for_).md>) to perform the actual writing of the data.

- `url` — A file URL specifying the location of the document file in the application sandbox.

- `saveOperation` — A constant that indicates whether the document file is being written the first time or whether it is being overwritten. See [SaveOperation](saveoperation.md) for details.

- `originalContentsURL` — A file URL specifying the previous location of the document file (if not `nil`).

## Discussion

This method is called by the [- writeContents:andAttributes:safelyToURL:forSaveOperation:error:](<writecontents(__andattributes_safelyto_for_).md>) to write the actual file data. It is passed the contents object returned from your [- contentsForType:error:](<contents(fortype_).md>) implementation. The default implementation of this method supports [NSData](../../foundation/nsdata.md) or [FileWrapper](../../foundation/filewrapper.md) contents by asking the contents object to save itself to the corresponding URL.

If you override this method, you may choose to return a different type of data from [- contentsForType:error:](<contents(fortype_).md>) or you may choose to not override [- contentsForType:error:](<contents(fortype_).md>) and generate the writable data directly within this method. If you override this method, you should not invoke the superclass implementation.

> [!note] Handling Errors in Swift
> In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> When overriding this method, use the `throw` statement to throw an `NSError`, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Writing document data

- [- closeWithCompletionHandler:](<close(completionhandler_).md>) — Asynchronously closes the document after saving any changes.
- [- contentsForType:error:](<contents(fortype_).md>) — Returns the document data to be saved.
- [- saveToURL:forSaveOperation:completionHandler:](<save(to_for_completionhandler_).md>) — Saves document data to the specified location in the application sandbox.
- [- writeContents:andAttributes:safelyToURL:forSaveOperation:error:](<writecontents(__andattributes_safelyto_for_).md>) — Ensures that document data is written safely to a specified location in the application sandbox.
- [savingFileType](savingfiletype.md) — Returns the file type to use for saving a document.
- [- fileAttributesToWriteToURL:forSaveOperation:error:](<fileattributestowrite(to_for_).md>) — Returns a dictionary of file attributes to associate with the document file when writing or updating it.
- [- fileNameExtensionForType:saveOperation:](<filenameextension(fortype_saveoperation_).md>) — Returns a file extension to append to the file URL of the document file being written.
