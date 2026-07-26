---
title: 'connectionTimeout(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/tcp/connectiontimeout(_:)'
source_url: 'https://developer.apple.com/documentation/network/tcp/connectiontimeout(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tcp/connectiontimeout%28_%3A%29.json'
content_hash: 'sha256:96a314aff78afa13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [TCP](../tcp.md)

# connectionTimeout(_:)

<sub>Instance Method</sub>

Set the timeout for TCP connection establishment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func connectionTimeout(_ timeout: UInt32) -> TCP
```

## Parameters

- `timeout` — The connection establishment timeout, in seconds.

## Discussion

A timeout for TCP connection establishment, in seconds. (`TCP_CONNECTIONTIMEOUT`).
