---
title: fire()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/timer/fire()
source_url: 'https://developer.apple.com/documentation/foundation/timer/fire()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timer/fire%28%29.json'
content_hash: 'sha256:9c812aa9a8b74dda'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Timer](../timer.md)

# fire()

<sub>Instance Method</sub>

Causes the timer’s message to be sent to its target.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func fire()
```

## Discussion

You can use this method to fire a repeating timer without interrupting its regular firing schedule. If the timer is non-repeating, it is automatically invalidated after firing, even if its scheduled fire date has not arrived.

## See Also

### Related Documentation

- [- invalidate](<invalidate().md>) — Stops the timer from ever firing again and requests its removal from its run loop.
