---
title: savingFileType
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocument/savingfiletype
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/savingfiletype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/savingfiletype.json'
content_hash: 'sha256:dbf535a86e822d54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# savingFileType

<sub>Instance Property</sub>

Returns the file type to use for saving a document.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var savingFileType: String? { get }
```

## Return Value

A Uniform Type Identifier (UTI) identifying a document type (for example, PDF or HTML).

## Discussion

The default implementation returns the current file type obtained from the [fileType](filetype.md) property. The default implementation of the [- saveToURL:forSaveOperation:completionHandler:](<save(to_for_completionhandler_).md>) method appends an extension to the file URL that’s based on the file type. So if you want to move the document to a new type and extension, you can override this method to supply that file type.

## See Also

### Writing document data

- [- closeWithCompletionHandler:](<close(completionhandler_).md>) — Asynchronously closes the document after saving any changes.
- [- contentsForType:error:](<contents(fortype_).md>) — Returns the document data to be saved.
- [- saveToURL:forSaveOperation:completionHandler:](<save(to_for_completionhandler_).md>) — Saves document data to the specified location in the application sandbox.
- [- writeContents:andAttributes:safelyToURL:forSaveOperation:error:](<writecontents(__andattributes_safelyto_for_).md>) — Ensures that document data is written safely to a specified location in the application sandbox.
- [- writeContents:toURL:forSaveOperation:originalContentsURL:error:](<writecontents(__to_for_originalcontentsurl_).md>) — Writes the document data to disk at the sandbox location indicated by a file URL.
- [- fileAttributesToWriteToURL:forSaveOperation:error:](<fileattributestowrite(to_for_).md>) — Returns a dictionary of file attributes to associate with the document file when writing or updating it.
- [- fileNameExtensionForType:saveOperation:](<filenameextension(fortype_saveoperation_).md>) — Returns a file extension to append to the file URL of the document file being written.
