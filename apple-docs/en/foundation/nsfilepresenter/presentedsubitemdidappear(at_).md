---
title: 'presentedSubitemDidAppear(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilepresenter/presentedsubitemdidappear(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilepresenter/presentedsubitemdidappear(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilepresenter/presentedsubitemdidappear%28at%3A%29.json'
content_hash: 'sha256:0cedc2a135ee81e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFilePresenter](../nsfilepresenter.md)

# presentedSubitemDidAppear(at:)

<sub>Instance Method</sub>

Tells the delegate that an item was added to the presented directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func presentedSubitemDidAppear(at url: URL)
```

## Parameters

- `url` — The URL of the item being added to the presented directory. The item need not be at the top level of the presented directory but may itself be inside a nested subdirectory.

## Discussion

This method is relevant for applications that present directories. This might occur if the delegate manages the contents of a directory or manages a file that is implemented as a file package. Your implementation of this method should take whatever actions necessary to incorporate the new file or directory into the presented content. For example, you might add the new item to your application’s data structures and refresh your user interface.

If the presented directory is a file package, the system calls the [- presentedItemDidChange](<presenteditemdidchange().md>) method if your delegate does not implement this method.

## See Also

### Handling Changes to a Presented Directory

- [- accommodatePresentedSubitemDeletionAtURL:completionHandler:](<accommodatepresentedsubitemdeletion(at_completionhandler_).md>) — Tells the delegate that some entity wants to delete an item that is inside of a presented directory.
- [- presentedSubitemAtURL:didMoveToURL:](<presentedsubitem(at_didmoveto_).md>) — Tells the delegate that an item in the presented directory moved to a new location.
- [- presentedSubitemDidChangeAtURL:](<presentedsubitemdidchange(at_).md>) — Tells the delegate that the contents or attributes of the specified item changed.
