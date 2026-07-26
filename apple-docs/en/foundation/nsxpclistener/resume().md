---
title: resume()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpclistener/resume()
source_url: 'https://developer.apple.com/documentation/foundation/nsxpclistener/resume()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpclistener/resume%28%29.json'
content_hash: 'sha256:48ce303a4a77f26c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCListener](../nsxpclistener.md)

# resume()

<sub>Instance Method</sub>

Starts processing of incoming requests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func resume()
```

## Discussion

All listeners start suspended and must be resumed before they begin processing incoming requests.

If called on the [+ serviceListener](<service().md>) object, this method never returns. Therefore, you should call it as the last step inside the XPC service’s `main` function after setting up any desired initial state and configuring the listener itself.

If called on any other [NSXPCListener](../nsxpclistener.md), the connection is resumed, and the method returns immediately.

## See Also

### Managing connection state

- [- activate](<activate().md>) — Activates the listener.
- [- invalidate](<invalidate().md>) — Invalidates the listener.
- [- suspend](<suspend().md>) — Suspends the listener.
