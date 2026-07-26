---
title: 'savePresentedItemChanges(completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilepresenter/savepresenteditemchanges(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilepresenter/savepresenteditemchanges(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilepresenter/savepresenteditemchanges%28completionhandler%3A%29.json'
content_hash: 'sha256:942a4b364c5bb87f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFilePresenter](../nsfilepresenter.md)

# savePresentedItemChanges(completionHandler:)

<sub>Instance Method</sub>

Tells your object to save any unsaved changes for the presented item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func savePresentedItemChanges(completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func savePresentedItemChanges() async throws
```

## Parameters

- `completionHandler` — The [Block object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3) to call after you save your changes. If you saved your changes successfully, pass `nil` for the block’s `errorOrNil` parameter; otherwise, pass an error object indicating why the changes could not be saved.

## Discussion

The file coordinator calls this method to ensure that all objects trying to access the file or directory see the same contents. Implement this method if your object can change the presented item in a way that requires you to write those changes back to disk. If your presenter object does not make changes that need to be saved, you do not need to implement this method.

> [!important] Important
> If you implement this method, you must execute the block in the `completionHandler` parameter at the end of your implementation. The system waits for you to execute that block before allowing other objects to operate on the file. Therefore, failure to execute the block could stall threads in your application or other processes.

## See Also

### Handling Changes to Files

- [- accommodatePresentedItemDeletionWithCompletionHandler:](<accommodatepresenteditemdeletion(completionhandler_).md>) — Tells your object that its presented item is about to be deleted.
- [- presentedItemDidMoveToURL:](<presenteditemdidmove(to_).md>) — Tells your object that the presented item moved or was renamed.
- [- presentedItemDidChange](<presenteditemdidchange().md>) — Tells your object that the presented item’s contents or attributes changed.
