---
title: 'CFRunLoopPerformBlock(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopperformblock(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopperformblock(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopperformblock%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:cbf6e6d500e8af66'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopPerformBlock(_:_:_:)

<sub>Function</sub>

Enqueues a block object on a given runloop to be executed as the runloop cycles in specified modes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopPerformBlock(_ rl: CFRunLoop!, _ mode: CFTypeRef!, _ block: (() -> Void)!)
```

## Parameters

- `rl` — A run loop.

- `mode` — A CFString that identifies a runloop mode, or a CFArray of CFStrings that each identify a runloop mode.

- `block` — The block object to execute. The block is copied by the function before the function returns.

## Discussion

When the runloop runs in the specified `mode`, the block object is executed. You can use this function as a means to offload work to another thread similar to Cocoa’s [perform(_:on:with:waitUntilDone:)](<../objectivec/nsobject-swift.class/perform(__on_with_waituntildone_).md>) and related methods. You can also use it as an alternative to mechanisms such as putting a CFRunLoopTimer in the other thread’s run loop, or using CFMessagePort to pass information between threads.

This method enqueues the block only and does not automatically wake up the specified run loop. Therefore, execution of the block occurs the next time the run loop wakes up to handle another input source. If you want the work performed right away, you must explicitly wake up that thread using the [CFRunLoopWakeUp](<cfrunloopwakeup(__).md>) function.
