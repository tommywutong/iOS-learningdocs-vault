---
title: 'fileNameExtension(forType:saveOperation:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocument/filenameextension(fortype:saveoperation:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/filenameextension(fortype:saveoperation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/filenameextension%28fortype%3Asaveoperation%3A%29.json'
content_hash: 'sha256:5ce3c6ebe7d3be2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# fileNameExtension(forType:saveOperation:)

<sub>Instance Method</sub>

Returns a file extension to append to the file URL of the document file being written.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func fileNameExtension(forType typeName: String?, saveOperation: UIDocument.SaveOperation) -> String
```

## Parameters

- `typeName` — A Uniform Type Identifier (UTI) that indicates the type of document (for example, PDF or HTML).

- `saveOperation` — A constant that indicates whether the document file is being written the first time or whether it’s being overwritten. See [SaveOperation](saveoperation.md) for details.

## Return Value

A string to use as the file extension of the document file.

## Discussion

The default implementation queries Launch Services to obtain the file extension matching the file (document) type. You can override this method to return a file extension that’s different from the default extension. The default implementation of the [- saveToURL:forSaveOperation:completionHandler:](<save(to_for_completionhandler_).md>) method calls this method before it gets the document content and writes the document file to disk.

## See Also

### Writing document data

- [- closeWithCompletionHandler:](<close(completionhandler_).md>) — Asynchronously closes the document after saving any changes.
- [- contentsForType:error:](<contents(fortype_).md>) — Returns the document data to be saved.
- [- saveToURL:forSaveOperation:completionHandler:](<save(to_for_completionhandler_).md>) — Saves document data to the specified location in the application sandbox.
- [- writeContents:andAttributes:safelyToURL:forSaveOperation:error:](<writecontents(__andattributes_safelyto_for_).md>) — Ensures that document data is written safely to a specified location in the application sandbox.
- [- writeContents:toURL:forSaveOperation:originalContentsURL:error:](<writecontents(__to_for_originalcontentsurl_).md>) — Writes the document data to disk at the sandbox location indicated by a file URL.
- [savingFileType](savingfiletype.md) — Returns the file type to use for saving a document.
- [- fileAttributesToWriteToURL:forSaveOperation:error:](<fileattributestowrite(to_for_).md>) — Returns a dictionary of file attributes to associate with the document file when writing or updating it.
