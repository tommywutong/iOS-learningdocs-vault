---
title: dispatchMain()
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchmain()
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchmain()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchmain%28%29.json'
content_hash: 'sha256:c6ff6c964503fea5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatchMain()

<sub>Function</sub>

Executes blocks submitted to the main queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dispatchMain() -> Never
```

## Discussion

This function “parks” the main thread and waits for blocks to be submitted to the main queue. Applications that call [UIApplicationMain(_:_:_:_:)](<../uikit/uiapplicationmain(________)-1yub7.md>) (iOS), [NSApplicationMain(_:_:)](<../appkit/nsapplicationmain(____).md>) (macOS), or [CFRunLoopRun()](<../corefoundation/cfrunlooprun().md>) on the main thread must not call [dispatch_main](<dispatchmain().md>).

This function never returns.
