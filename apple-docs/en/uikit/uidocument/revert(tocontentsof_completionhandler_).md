---
title: 'revert(toContentsOf:completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocument/revert(tocontentsof:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/revert(tocontentsof:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/revert%28tocontentsof%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:92bbc7eac28873de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# revert(toContentsOf:completionHandler:)

<sub>Instance Method</sub>

Reverts a document to the most recent document data stored on-disk.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func revert(toContentsOf url: URL, completionHandler: (@Sendable (Bool) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func revert(toContentsOf url: URL) async -> Bool
```

## Parameters

- `url` — A file URL locating the most recent version of the document file in the application’s sandbox.

- `completionHandler` — A block with code to execute after the reversion operation concludes. The block returns no value and has one parameter: - **`success`** — [true](../../swift/true.md) if the reversion operation succeeds, otherwise [false](../../swift/false.md). The block is invoked on the main queue.

## Discussion

You call this method to discard all unsaved document modifications and replace the document’s contents by reading the file or file package located by `url`. The default implementation brackets the reversion operation between [- disableEditing](<disableediting().md>) and [- enableEditing](<enableediting().md>)because the document shouldn’t accept user changes during this period. Subclasses that override this method must call the superclass implementation (`super`) or use the [NSFileCoordinator](../../foundation/nsfilecoordinator.md) class to initiate a coordinated read.
