---
title: 'load(fromContents:ofType:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocument/load(fromcontents:oftype:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/load(fromcontents:oftype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/load%28fromcontents%3Aoftype%3A%29.json'
content_hash: 'sha256:f60eb7169e6875e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# load(fromContents:ofType:)

<sub>Instance Method</sub>

Loads the document data into the app’s data model.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func load(fromContents contents: Any, ofType typeName: String?) throws
```

## Parameters

- `contents` — An object encapsulating the document data to load. This object is either an instance of the [NSData](../../foundation/nsdata.md) class (for flat files) or the [FileWrapper](../../foundation/filewrapper.md) class (for file packages).

- `typeName` — The file type of the document, a Uniform Type Identifier (UTI) based on the file extension of [fileURL](fileurl.md). You can obtain the default value of the file type from the [fileType](filetype.md) property.

## Discussion

Override this method to accept and load the data for a document. After `UIDocument` reads the document data from the file located at [fileURL](fileurl.md) it calls your subclass, passing the data to the subclass in this method. This method is called on the queue that the [- openWithCompletionHandler:](<open(completionhandler_).md>) method was called on (typically, the main queue).

> [!note] Handling Errors in Swift
> In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> When overriding this method, use the `throw` statement to throw an `NSError`, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Reading document data

- [- openWithCompletionHandler:](<open(completionhandler_).md>) — Opens a document asynchronously.
- [- readFromURL:error:](<read(from_).md>) — Reads the document data in a file at a specified location in the application sandbox.
