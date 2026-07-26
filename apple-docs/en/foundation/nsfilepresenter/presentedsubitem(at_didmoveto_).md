---
title: 'presentedSubitem(at:didMoveTo:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilepresenter/presentedsubitem(at:didmoveto:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilepresenter/presentedsubitem(at:didmoveto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilepresenter/presentedsubitem%28at%3Adidmoveto%3A%29.json'
content_hash: 'sha256:f282391c8ceb9573'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFilePresenter](../nsfilepresenter.md)

# presentedSubitem(at:didMoveTo:)

<sub>Instance Method</sub>

Tells the delegate that an item in the presented directory moved to a new location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func presentedSubitem(at oldURL: URL, didMoveTo newURL: URL)
```

## Parameters

- `oldURL` — The original URL of the item inside the presented directory. The item need not be at the top level of the presented directory but may itself be inside a nested subdirectory.

- `newURL` — The new URL for the item. This URL may or may not be located inside the presented directory.

## Discussion

This method is relevant for applications that present directories. This might occur if the delegate manages the contents of a directory or manages a file that is implemented as a file package. Your implementation of this method should take whatever actions necessary to handle the change in location of the specified item. For example, you might update references to the item in your application’s data structures and refresh your user interface.

If the presented directory is a file package, the system calls the [- presentedItemDidChange](<presenteditemdidchange().md>) method if your delegate does not implement this method.

## See Also

### Handling Changes to a Presented Directory

- [- accommodatePresentedSubitemDeletionAtURL:completionHandler:](<accommodatepresentedsubitemdeletion(at_completionhandler_).md>) — Tells the delegate that some entity wants to delete an item that is inside of a presented directory.
- [- presentedSubitemDidAppearAtURL:](<presentedsubitemdidappear(at_).md>) — Tells the delegate that an item was added to the presented directory.
- [- presentedSubitemDidChangeAtURL:](<presentedsubitemdidchange(at_).md>) — Tells the delegate that the contents or attributes of the specified item changed.
