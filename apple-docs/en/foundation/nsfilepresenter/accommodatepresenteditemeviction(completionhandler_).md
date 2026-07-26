---
title: 'accommodatePresentedItemEviction(completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, visionOS 1.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilepresenter/accommodatepresenteditemeviction(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilepresenter/accommodatepresenteditemeviction(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilepresenter/accommodatepresenteditemeviction%28completionhandler%3A%29.json'
content_hash: 'sha256:6bf671284d88ab31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFilePresenter](../nsfilepresenter.md)

# accommodatePresentedItemEviction(completionHandler:)

<sub>Instance Method</sub>

Given that something in the system is waiting to evict the presented file or directory, do whatever it takes to ensure that the eviction will succeed and that the receiver’s application will behave properly when the eviction has happened, and then invoke the completion handler. This must include calling +[NSFileCoordinator removeFilePresenter:]. You may instead prevent eviction by passing the completion handler a meaningful error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
optional func accommodatePresentedItemEviction(completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
optional func accommodatePresentedItemEviction() async throws
```

## Discussion

If this method is not implemented, eviction will fail.
