---
title: captureStreams()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionstreamtask/capturestreams()
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionstreamtask/capturestreams()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionstreamtask/capturestreams%28%29.json'
content_hash: 'sha256:98aeaffb2f30259e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionStreamTask](../urlsessionstreamtask.md)

# captureStreams()

<sub>Instance Method</sub>

Completes any already enqueued reads and writes, and then invokes the [- URLSession:streamTask:didBecomeInputStream:outputStream:](<../urlsessionstreamdelegate/urlsession(__streamtask_didbecome_outputstream_).md>) delegate message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func captureStreams()
```
