---
title: 'synchronizeToBackingStore(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextelementprovider/synchronizetobackingstore(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextelementprovider/synchronizetobackingstore(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextelementprovider/synchronizetobackingstore%28_%3A%29.json'
content_hash: 'sha256:2d146bf1dd616285'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextElementProvider](../nstextelementprovider.md)

# synchronizeToBackingStore(_:)

<sub>Instance Method</sub>

Synchronizes changes to the backing store.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func synchronizeToBackingStore(_ completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func synchronizeToBackingStore() async throws
```

## Parameters

- `completionHandler` — A completion handler to run upon successful completion, or to process an error upon failure.

## Discussion

If `completionHandler` is `nil`, performs the operation synchronously. The `completionHandler` gets passed `error` if the synchronization fails. It should block (or fails if synchronous) when there’s an active transaction.
