---
title: 'presentedSubitemDidChange(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilepresenter/presentedsubitemdidchange(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilepresenter/presentedsubitemdidchange(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilepresenter/presentedsubitemdidchange%28at%3A%29.json'
content_hash: 'sha256:2e2c9028e090a732'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFilePresenter](../nsfilepresenter.md)

# presentedSubitemDidChange(at:)

<sub>Instance Method</sub>

Tells the delegate that the contents or attributes of the specified item changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func presentedSubitemDidChange(at url: URL)
```

## Parameters

- `url` — The URL of the item in the presented directory that changed. The item need not be at the top level of the presented directory but may itself be inside a nested subdirectory.

## Discussion

This method is relevant for applications that present directories. This might occur if the delegate manages the contents of a directory or manages a file that is implemented as a file package. Your implementation of this method should take whatever actions necessary to handle the change in content or attributes of the specified item.

If the presented directory is a file package, the system calls the [- presentedItemDidChange](<presenteditemdidchange().md>) method if your delegate does not implement this method.

## See Also

### Handling Changes to a Presented Directory

- [- accommodatePresentedSubitemDeletionAtURL:completionHandler:](<accommodatepresentedsubitemdeletion(at_completionhandler_).md>) — Tells the delegate that some entity wants to delete an item that is inside of a presented directory.
- [- presentedSubitemDidAppearAtURL:](<presentedsubitemdidappear(at_).md>) — Tells the delegate that an item was added to the presented directory.
- [- presentedSubitemAtURL:didMoveToURL:](<presentedsubitem(at_didmoveto_).md>) — Tells the delegate that an item in the presented directory moved to a new location.
