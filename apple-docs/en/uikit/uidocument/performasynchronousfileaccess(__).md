---
title: 'performAsynchronousFileAccess(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocument/performasynchronousfileaccess(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/performasynchronousfileaccess(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/performasynchronousfileaccess%28_%3A%29.json'
content_hash: 'sha256:c9be9e0bc5b50948'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# performAsynchronousFileAccess(_:)

<sub>Instance Method</sub>

Schedules a document-reading or document-writing operation on a concurrent background queue.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func performAsynchronousFileAccess(_ block: @escaping () -> Void)
```

## Parameters

- `block` — A block that’s invoked as the task to execute on the background queue. The block returns no value and takes no parameters.

## Discussion

A typical [UIDocument](../uidocument.md) subclass — one that overrides [- contentsForType:error:](<contents(fortype_).md>) and [- loadFromContents:ofType:error:](<load(fromcontents_oftype_).md>) — doesn’t need to call this method.

The default implementations of [- saveToURL:forSaveOperation:completionHandler:](<save(to_for_completionhandler_).md>) and [- openWithCompletionHandler:](<open(completionhandler_).md>) call this method to serialize file access. If you override these methods and don’t call `super`, you should call this method to serialize file access on a background queue. If you directly call the [- readFromURL:error:](<read(from_).md>) method, you should wrap that call in the block passed into [- performAsynchronousFileAccessUsingBlock:](<performasynchronousfileaccess(__).md>).
