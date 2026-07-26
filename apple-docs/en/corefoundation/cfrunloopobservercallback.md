---
title: CFRunLoopObserverCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunloopobservercallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopobservercallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopobservercallback.json'
content_hash: 'sha256:b34cc428dae5a7d4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopObserverCallBack

<sub>Type Alias</sub>

Callback invoked when a CFRunLoopObserver object is fired.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFRunLoopObserverCallBack = (CFRunLoopObserver?, CFRunLoopActivity, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `observer` — The run loop observer that is firing.

- `activity` — The current activity stage of the run loop.

- `info` — The `info` member of the [CFRunLoopObserverContext](cfrunloopobservercontext.md) structure that was used when creating the run loop observer.

## Discussion

You specify this callback when you create the run loop observer with [CFRunLoopObserverCreate](<cfrunloopobservercreate(____________).md>).
