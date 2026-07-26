---
title: 'read(from:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocument/read(from:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/read(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/read%28from%3A%29.json'
content_hash: 'sha256:8b383cb973030cf7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# read(from:)

<sub>Instance Method</sub>

Reads the document data in a file at a specified location in the application sandbox.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func read(from url: URL) throws
```

## Parameters

- `url` — A file URL that identifies the location of the document file in the application sandbox. This file URL is typically the one returned by the [fileURL](fileurl.md) property.

## Discussion

Typical [UIDocument](../uidocument.md) subclasses shouldn’t need to call this method directly, especially if the entire file is read at once. The default implementation calls [- loadFromContents:ofType:error:](<load(fromcontents_oftype_).md>) on the queue on which [- openWithCompletionHandler:](<open(completionhandler_).md>) was called to provide the `UIDocument` subclass with the document data object.

Subclasses that want more control over the reading of the document file—for example, that want to read a large document file incrementally—can override this method. It isn’t necessary for these subclasses to call the superclass implementation (`super`).

> [!note] Handling Errors in Swift
> In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> When overriding this method, use the `throw` statement to throw an `NSError`, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Reading document data

- [- openWithCompletionHandler:](<open(completionhandler_).md>) — Opens a document asynchronously.
- [- loadFromContents:ofType:error:](<load(fromcontents_oftype_).md>) — Loads the document data into the app’s data model.
