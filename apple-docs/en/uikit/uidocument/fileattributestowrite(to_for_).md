---
title: 'fileAttributesToWrite(to:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocument/fileattributestowrite(to:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/fileattributestowrite(to:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/fileattributestowrite%28to%3Afor%3A%29.json'
content_hash: 'sha256:ac9ab24d7c0e7277'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# fileAttributesToWrite(to:for:)

<sub>Instance Method</sub>

Returns a dictionary of file attributes to associate with the document file when writing or updating it.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func fileAttributesToWrite(to url: URL, for saveOperation: UIDocument.SaveOperation) throws -> [AnyHashable : Any]
```

## Parameters

- `url` — A file URL locating the document in the application sandbox.

- `saveOperation` — A constant that indicates whether the document file is being written the first time or whether it’s being overwritten. See [SaveOperation](saveoperation.md) for details.

## Return Value

A dictionary of file attributes — for example, level of file protection and creation date. See [FileManager](../../foundation/filemanager.md) for more information about file attributes.

## Discussion

The attributes are associated with a specific file type and save operation. You can override this method to return a dictionary of file attributes that are different than the default file attribute, which for new files is [extensionHidden](../../foundation/fileattributekey/extensionhidden.md).

The [- saveToURL:forSaveOperation:completionHandler:](<save(to_for_completionhandler_).md>) calls this method before executing asynchronous writing. It passes the dictionary into [- writeContents:andAttributes:safelyToURL:forSaveOperation:error:](<writecontents(__andattributes_safelyto_for_).md>) when it calls that method to write the document file.

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
- [- writeContents:toURL:forSaveOperation:originalContentsURL:error:](<writecontents(__to_for_originalcontentsurl_).md>) — Writes the document data to disk at the sandbox location indicated by a file URL.
- [savingFileType](savingfiletype.md) — Returns the file type to use for saving a document.
- [- fileNameExtensionForType:saveOperation:](<filenameextension(fortype_saveoperation_).md>) — Returns a file extension to append to the file URL of the document file being written.
