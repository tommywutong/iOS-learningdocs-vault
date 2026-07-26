---
title: main()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/thread/main()
source_url: 'https://developer.apple.com/documentation/foundation/thread/main()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/thread/main%28%29.json'
content_hash: 'sha256:490c2f7324206a75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Thread](../thread.md)

# main()

<sub>Instance Method</sub>

The main entry point routine for the thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func main()
```

## Discussion

The default implementation of this method takes the target and selector used to initialize the receiver and invokes the selector on the specified target. If you subclass `NSThread`, you can override this method and use it to implement the main body of your thread instead. If you do so, you do not need to invoke `super`.

You should never invoke this method directly. You should always start your thread by invoking the [- start](<start().md>) method.

## See Also

### Starting a Thread

- [+ detachNewThreadSelector:toTarget:withObject:](<detachnewthreadselector(__totarget_with_).md>) — Detaches a new thread and uses the specified selector as the thread entry point.
- [- start](<start().md>) — Starts the receiver.
