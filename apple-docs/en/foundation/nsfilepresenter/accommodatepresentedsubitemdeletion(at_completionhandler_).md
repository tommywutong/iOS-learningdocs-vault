---
title: 'accommodatePresentedSubitemDeletion(at:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilepresenter/accommodatepresentedsubitemdeletion(at:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilepresenter/accommodatepresentedsubitemdeletion(at:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilepresenter/accommodatepresentedsubitemdeletion%28at%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:30b7232f6b4950e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFilePresenter](../nsfilepresenter.md)

# accommodatePresentedSubitemDeletion(at:completionHandler:)

<sub>Instance Method</sub>

Tells the delegate that some entity wants to delete an item that is inside of a presented directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func accommodatePresentedSubitemDeletion(at url: URL, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func accommodatePresentedSubitemDeletion(at url: URL) async throws
```

## Parameters

- `url` — The URL of the item being deleted from the presented directory. The item need not be at the top level of the presented directory but may itself be inside a nested subdirectory.

- `completionHandler` — The [Block object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3) to call after updating your data structures. Pass `nil` to the block’s `errorOrNil` parameter if you were able to successfully prepare for the deletion of the item. Pass an error object if your object could not prepare itself properly.

## Discussion

This method is relevant for applications that present directories. This might occur if the delegate manages the contents of a directory or manages a file that is implemented as a file package. When called, your implementation of this method should take whatever actions needed to update your application to handle the deletion of the specified file.

> [!important] Important
> If you implement this method, you must execute the block in the `completionHandler` parameter at the end of your implementation. The system waits for you to execute that block before allowing the other object to delete the item at the specified URL. Therefore, failure to execute the block could stall threads in your application or in other processes.

## See Also

### Handling Changes to a Presented Directory

- [- presentedSubitemDidAppearAtURL:](<presentedsubitemdidappear(at_).md>) — Tells the delegate that an item was added to the presented directory.
- [- presentedSubitemAtURL:didMoveToURL:](<presentedsubitem(at_didmoveto_).md>) — Tells the delegate that an item in the presented directory moved to a new location.
- [- presentedSubitemDidChangeAtURL:](<presentedsubitemdidchange(at_).md>) — Tells the delegate that the contents or attributes of the specified item changed.
