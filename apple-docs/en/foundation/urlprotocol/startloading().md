---
title: startLoading()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlprotocol/startloading()
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocol/startloading()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocol/startloading%28%29.json'
content_hash: 'sha256:e5b38306dc7dcf50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtocol](../urlprotocol.md)

# startLoading()

<sub>Instance Method</sub>

Starts protocol-specific loading of the request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func startLoading()
```

## Discussion

When this method is called, the subclass implementation should start loading the request, providing feedback to the URL loading system via the [URLProtocolClient](../urlprotocolclient.md) protocol.

Subclasses must implement this method.

## See Also

### Starting and stopping downloads

- [- stopLoading](<stoploading().md>) — Stops protocol-specific loading of the request.
