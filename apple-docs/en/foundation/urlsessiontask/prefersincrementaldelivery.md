---
title: prefersIncrementalDelivery
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, macOS 11.3+, tvOS 14.5+, visionOS 1.0+, watchOS 7.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/prefersincrementaldelivery
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/prefersincrementaldelivery'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/prefersincrementaldelivery.json'
content_hash: 'sha256:a18e9f0b80062dfd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTask](../urlsessiontask.md)

# prefersIncrementalDelivery

<sub>Instance Property</sub>

A Boolean value that determines whether to deliver a partial response body in increments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var prefersIncrementalDelivery: Bool { get set }
```

## Discussion

Set this property to `true` to tell the task that the app would benefit from receiving a partial response body in increments. If the app can’t process the response until it has all the data, set this property to `false`. Task performance may improve when this value is `false`, in which case the task only delivers data when complete.

This property defaults to `true`, except in the following cases which default to `false`:

- The task delivers results to a completion handler rather than to a delegate.
- The task is a download task.
