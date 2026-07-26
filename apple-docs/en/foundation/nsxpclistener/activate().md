---
title: activate()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpclistener/activate()
source_url: 'https://developer.apple.com/documentation/foundation/nsxpclistener/activate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpclistener/activate%28%29.json'
content_hash: 'sha256:02c32e6586c96802'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCListener](../nsxpclistener.md)

# activate()

<sub>Instance Method</sub>

Activates the listener.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func activate()
```

## Discussion

Connections start in an inactive state. You must call [- activate](<activate().md>) on a connection before it can send or receive any messages.

Calling [- activate](<activate().md>) on an active connection has no effect.

For backward compatibility reasons, calling [- resume](<resume().md>) on an inactive and otherwise not suspended [NSXPCListener](../nsxpclistener.md) has the same effect as calling [- activate](<activate().md>). For new code, prefer [- activate](<activate().md>).

## See Also

### Managing connection state

- [- resume](<resume().md>) — Starts processing of incoming requests.
- [- invalidate](<invalidate().md>) — Invalidates the listener.
- [- suspend](<suspend().md>) — Suspends the listener.
