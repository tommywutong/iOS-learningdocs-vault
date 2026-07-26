---
title: presentedItemOperationQueue
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilepresenter/presenteditemoperationqueue
source_url: 'https://developer.apple.com/documentation/foundation/nsfilepresenter/presenteditemoperationqueue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilepresenter/presenteditemoperationqueue.json'
content_hash: 'sha256:eca8b7acc2789077'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFilePresenter](../nsfilepresenter.md)

# presentedItemOperationQueue

<sub>Instance Property</sub>

The operation queue in which to execute presenter-related messages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var presentedItemOperationQueue: OperationQueue { get }
```

## Discussion

As other objects and processes interact with the presented item, the system queues relevant messages for this presenter object on the operation queue in this property. For example, when another process attempts to read a file presented by this object, the system places an invocation of this object’s [- relinquishPresentedItemToReader:](<relinquishpresenteditem(toreader_).md>) method on the queue for execution. The other process must wait to read the file until that method is dequeued and executed. Requests for an object’s presented URL are not processed on this queue.

## See Also

### Accessing File Presenter Attributes

- [presentedItemURL](presenteditemurl.md) — The URL of the presented file or directory.
- [primaryPresentedItemURL](primarypresenteditemurl.md) — The URL of a secondary item’s primary presented file or directory.
