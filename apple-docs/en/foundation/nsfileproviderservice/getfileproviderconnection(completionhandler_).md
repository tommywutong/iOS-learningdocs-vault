---
title: 'getFileProviderConnection(completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfileproviderservice/getfileproviderconnection(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfileproviderservice/getfileproviderconnection(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileproviderservice/getfileproviderconnection%28completionhandler%3A%29.json'
content_hash: 'sha256:3031b01d6ba4d3ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileProviderService](../nsfileproviderservice.md)

# getFileProviderConnection(completionHandler:)

<sub>Instance Method</sub>

Asynchronously returns the service’s connection object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func getFileProviderConnection(completionHandler: @escaping @Sendable (NSXPCConnection?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func fileProviderConnection() async throws -> NSXPCConnection
```

## Parameters

- `completionHandler` — A block that is called on an anonymous background queue. The system passes this block the following parameters: - **`connection`** — An [NSXPCConnection](../nsxpcconnection.md) object for the service, or `nil` if an error occurs. - **`error`** — If an error occurs, this property contains an object that describes the error; otherwise, it is set to `nil`.

## See Also

### Accessing the Service

- [name](name.md) — The File Provider service’s name.
