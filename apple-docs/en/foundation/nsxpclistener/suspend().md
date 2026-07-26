---
title: suspend()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpclistener/suspend()
source_url: 'https://developer.apple.com/documentation/foundation/nsxpclistener/suspend()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpclistener/suspend%28%29.json'
content_hash: 'sha256:1dfd7d5709852090'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCListener](../nsxpclistener.md)

# suspend()

<sub>Instance Method</sub>

Suspends the listener.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func suspend()
```

## Discussion

As you cannot invalidate a suspended listener, every call to [- suspend](<suspend().md>) that you make must be balanced by a call to [- resume](<resume().md>).

## See Also

### Managing connection state

- [- activate](<activate().md>) — Activates the listener.
- [- resume](<resume().md>) — Starts processing of incoming requests.
- [- invalidate](<invalidate().md>) — Invalidates the listener.
