---
title: 'contents(forType:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocument/contents(fortype:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/contents(fortype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/contents%28fortype%3A%29.json'
content_hash: 'sha256:d0e359316506dcbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# contents(forType:)

<sub>Instance Method</sub>

Returns the document data to be saved.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func contents(forType typeName: String) throws -> Any
```

## Parameters

- `typeName` — The file type of the document, a Uniform Type Identifier (UTI). This string typically derives from the [fileType](filetype.md) property. If you want to save the document under a different UTI, you can override the [savingFileType](savingfiletype.md) method.

## Return Value

The document data to be saved, or `nil` if you cannot return document data. The returned object is typically an instance of the [NSData](../../foundation/nsdata.md) class for flat files or the [FileWrapper](../../foundation/filewrapper.md) class for file packages. If you return `nil`, you should also return an error object in `outError`.

If you return an object other than an [NSData](../../foundation/nsdata.md) or [FileWrapper](../../foundation/filewrapper.md) object, you must override the [- writeContents:andAttributes:safelyToURL:forSaveOperation:error:](<writecontents(__andattributes_safelyto_for_).md>) or [- writeContents:toURL:forSaveOperation:originalContentsURL:error:](<writecontents(__to_for_originalcontentsurl_).md>) method to handle the writing of data.

## Discussion

When you subclass [UIDocument](../uidocument.md), override this method to provide UIKit with the document data for saving.

This method is called on the queue that the [- saveToURL:forSaveOperation:completionHandler:](<save(to_for_completionhandler_).md>) method was called on (typically, the main queue). Writing of data occurs on a background queue. The default implementation of this method returns `nil`.

When you return a non-`nil` value in the `outError` parameter, the completion handlers for the following methods don’t get called:

- [- saveToURL:forSaveOperation:completionHandler:](<save(to_for_completionhandler_).md>)
- [- autosaveWithCompletionHandler:](<autosave(completionhandler_).md>)
- [- closeWithCompletionHandler:](<close(completionhandler_).md>)

Instead, in this case, the error is available to your app in the [- handleError:userInteractionPermitted:](<handleerror(__userinteractionpermitted_).md>) method and in the [UIDocumentStateChangedNotification](statechangednotification.md) notification.

If you want more control over the saving operation than this method provides—for example, if you want to perform incremental writing of data — override, instead, one of the lower-level data-writing methods such as [- writeContents:andAttributes:safelyToURL:forSaveOperation:error:](<writecontents(__andattributes_safelyto_for_).md>) or [- writeContents:toURL:forSaveOperation:originalContentsURL:error:](<writecontents(__to_for_originalcontentsurl_).md>). These methods are called on a background thread.

> [!note] Handling Errors in Swift
> In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> When overriding this method, use the `throw` statement to throw an `NSError`, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Related Documentation

- [- openWithCompletionHandler:](<open(completionhandler_).md>) — Opens a document asynchronously.
- [- revertToContentsOfURL:completionHandler:](<revert(tocontentsof_completionhandler_).md>) — Reverts a document to the most recent document data stored on-disk.

### Writing document data

- [- closeWithCompletionHandler:](<close(completionhandler_).md>) — Asynchronously closes the document after saving any changes.
- [- saveToURL:forSaveOperation:completionHandler:](<save(to_for_completionhandler_).md>) — Saves document data to the specified location in the application sandbox.
- [- writeContents:andAttributes:safelyToURL:forSaveOperation:error:](<writecontents(__andattributes_safelyto_for_).md>) — Ensures that document data is written safely to a specified location in the application sandbox.
- [- writeContents:toURL:forSaveOperation:originalContentsURL:error:](<writecontents(__to_for_originalcontentsurl_).md>) — Writes the document data to disk at the sandbox location indicated by a file URL.
- [savingFileType](savingfiletype.md) — Returns the file type to use for saving a document.
- [- fileAttributesToWriteToURL:forSaveOperation:error:](<fileattributestowrite(to_for_).md>) — Returns a dictionary of file attributes to associate with the document file when writing or updating it.
- [- fileNameExtensionForType:saveOperation:](<filenameextension(fortype_saveoperation_).md>) — Returns a file extension to append to the file URL of the document file being written.
