---
title: invalidate()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpclistener/invalidate()
source_url: 'https://developer.apple.com/documentation/foundation/nsxpclistener/invalidate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpclistener/invalidate%28%29.json'
content_hash: 'sha256:20eeb12185770f80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCListener](../nsxpclistener.md)

# invalidate()

<sub>Instance Method</sub>

Invalidates the listener.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func invalidate()
```

## Discussion

After calling this method, no more connections are created. Once a listener is invalidated it may not be resumed or suspended.

## See Also

### Managing connection state

- [- activate](<activate().md>) — Activates the listener.
- [- resume](<resume().md>) — Starts processing of incoming requests.
- [- suspend](<suspend().md>) — Suspends the listener.
