---
title: NSExtensionRequestHandling
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsextensionrequesthandling
source_url: 'https://developer.apple.com/documentation/foundation/nsextensionrequesthandling'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensionrequesthandling.json'
content_hash: 'sha256:ab3418344fc70827'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSExtensionRequestHandling

<sub>Protocol</sub>

The interface an app extension uses to respond to a request from a host app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NSExtensionRequestHandling : NSObjectProtocol
```

## Overview

The [NSExtensionRequestHandling](nsextensionrequesthandling.md) protocol provides a life cycle hook into an app extension. An extension’s principal object can implement this protocol and use [- beginRequestWithExtensionContext:](<nsextensionrequesthandling/beginrequest(with_).md>) to keep track of the request from a host app.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Preparing for a request

- [- beginRequestWithExtensionContext:](<nsextensionrequesthandling/beginrequest(with_).md>) — Tells the extension to prepare for a host app’s request.

## See Also

### Extension Support

- [NSExtensionContext](nsextensioncontext.md) — The host app context from which an app extension is invoked.
