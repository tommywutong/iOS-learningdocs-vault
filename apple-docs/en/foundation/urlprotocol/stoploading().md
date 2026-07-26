---
title: stopLoading()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlprotocol/stoploading()
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocol/stoploading()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocol/stoploading%28%29.json'
content_hash: 'sha256:e628d1cd1f53ba35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtocol](../urlprotocol.md)

# stopLoading()

<sub>Instance Method</sub>

Stops protocol-specific loading of the request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func stopLoading()
```

## Discussion

When this method is called, the subclass implementation should stop loading a request. This could be in response to a cancel operation, so protocol implementations must be able to handle this call while a load is in progress. When your protocol receives a call to this method, it should also stop sending notifications to the client.

Subclasses must implement this method.

## See Also

### Starting and stopping downloads

- [- startLoading](<startloading().md>) — Starts protocol-specific loading of the request.
