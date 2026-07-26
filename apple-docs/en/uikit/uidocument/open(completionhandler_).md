---
title: 'open(completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocument/open(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/open(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/open%28completionhandler%3A%29.json'
content_hash: 'sha256:3bc9a49deb56677e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# open(completionHandler:)

<sub>Instance Method</sub>

Opens a document asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func open(completionHandler: (@Sendable (Bool) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func open() async -> Bool
```

## Parameters

- `completionHandler` — A block with code to execute after the open operation concludes. The block returns no value and has one parameter: - **`success`** — [true](../../swift/true.md) if the open operation succeeds, otherwise [false](../../swift/false.md). The block is invoked on the main queue.

## Discussion

Call this method to begin the sequence of method calls that opens and reads a document asynchronously. The method obtains the file-system location of the document from the [fileURL](fileurl.md) property. After the open operation concludes, the code in `completionHandler` is executed.

You can override this method if you want custom document-opening behavior, but if you do it’s recommended that you call the superclass implementation first (`super`). If you don’t call `super`, you should use the [NSFileCoordinator](../../foundation/nsfilecoordinator.md) class to implement coordinated reading. The default implementation calls [- performAsynchronousFileAccessUsingBlock:](<performasynchronousfileaccess(__).md>) to schedule the document-reading work for execution on a background queue and then, from the dispatched block, performs file coordination. The queued task then calls [- readFromURL:error:](<read(from_).md>).

## See Also

### Reading document data

- [- loadFromContents:ofType:error:](<load(fromcontents_oftype_).md>) — Loads the document data into the app’s data model.
- [- readFromURL:error:](<read(from_).md>) — Reads the document data in a file at a specified location in the application sandbox.
