---
title: getCFRunLoop()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/runloop/getcfrunloop()
source_url: 'https://developer.apple.com/documentation/foundation/runloop/getcfrunloop()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/getcfrunloop%28%29.json'
content_hash: 'sha256:6b136888a5ced382'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RunLoop](../runloop.md)

# getCFRunLoop()

<sub>Instance Method</sub>

Returns the receiver’s underlying run loop object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getCFRunLoop() -> CFRunLoop
```

## Return Value

The receiver’s underlying [CFRunLoop](../../corefoundation/cfrunloop.md) object.

## Discussion

You can use the returned run loop to configure the current run loop using Core Foundation function calls. For example, you might use this function to set up a run loop observer.

## See Also

### Accessing Run Loops and Modes

- [currentRunLoop](current.md) — Returns the run loop for the current thread.
- [currentMode](currentmode.md) — The receiver’s current input mode.
- [- limitDateForMode:](<limitdate(formode_).md>) — Performs one pass through the run loop in the specified mode and returns the date at which the next timer is scheduled to fire.
- [mainRunLoop](main.md) — Returns the run loop of the main thread.
- [Mode](mode.md) — Modes that a run loop operates in.
