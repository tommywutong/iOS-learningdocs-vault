---
title: 'accommodatePresentedItemDeletion(completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilepresenter/accommodatepresenteditemdeletion(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilepresenter/accommodatepresenteditemdeletion(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilepresenter/accommodatepresenteditemdeletion%28completionhandler%3A%29.json'
content_hash: 'sha256:fae0921fc666eb63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFilePresenter](../nsfilepresenter.md)

# accommodatePresentedItemDeletion(completionHandler:)

<sub>Instance Method</sub>

Tells your object that its presented item is about to be deleted.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func accommodatePresentedItemDeletion(completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func accommodatePresentedItemDeletion() async throws
```

## Parameters

- `completionHandler` — The [Block object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3) to call after updating your data structures. Pass `nil` to the block’s `errorOrNil` parameter if you were able to successfully prepare for the deletion of the item. Pass an error object if your object could not prepare itself properly.

## Discussion

A file coordinator calls this method when your object’s presented item is about to be deleted. You can use this method to perform any actions that are needed to prepare for the deletion. For example, document objects typically use this method to close the document.

> [!important] Important
> If you implement this method, you must execute the block in the `completionHandler` parameter at the end of your implementation. The system waits for you to execute that block before allowing the other object to delete the file or directory. Therefore, failure to execute the block could stall threads in your application or other processes.

## See Also

### Handling Changes to Files

- [- savePresentedItemChangesWithCompletionHandler:](<savepresenteditemchanges(completionhandler_).md>) — Tells your object to save any unsaved changes for the presented item.
- [- presentedItemDidMoveToURL:](<presenteditemdidmove(to_).md>) — Tells your object that the presented item moved or was renamed.
- [- presentedItemDidChange](<presenteditemdidchange().md>) — Tells your object that the presented item’s contents or attributes changed.
