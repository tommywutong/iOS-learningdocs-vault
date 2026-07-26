---
title: invalidate()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/timer/invalidate()
source_url: 'https://developer.apple.com/documentation/foundation/timer/invalidate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timer/invalidate%28%29.json'
content_hash: 'sha256:808c23ca77d2f555'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Timer](../timer.md)

# invalidate()

<sub>Instance Method</sub>

Stops the timer from ever firing again and requests its removal from its run loop.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func invalidate()
```

## Discussion

This method is the only way to remove a timer from an [RunLoop](../runloop.md) object. The [RunLoop](../runloop.md) object removes its strong reference to the timer, either just before the [- invalidate](<invalidate().md>) method returns or at some later point.

If it was configured with target and user info objects, the receiver removes its strong references to those objects as well.

### Special Considerations

You must send this message from the thread on which the timer was installed. If you send this message from another thread, the input source associated with the timer may not be removed from its run loop, which could prevent the thread from exiting properly.

## See Also

### Related Documentation

- [- fire](<fire().md>) — Causes the timer’s message to be sent to its target.
