---
title: 'init(copying:newPort:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, tvOS 26.4+, visionOS 26.4+, watchOS 26.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwendpoint/init(copying:newport:)'
source_url: 'https://developer.apple.com/documentation/network/nwendpoint/init(copying:newport:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwendpoint/init%28copying%3Anewport%3A%29.json'
content_hash: 'sha256:094577735bfbc2f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWEndpoint](../nwendpoint.md)

# init(copying:newPort:)

<sub>Initializer</sub>

Creates a new `NWEndpoint` by copying an existing endpoint and specifying a new port.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(copying endpoint: NWEndpoint, newPort: NWEndpoint.Port)
```

## Parameters

- `endpoint` — The source endpoint to copy.

- `newPort` — The new port to use.

## Return Value

A new `NWEndpoint` instance copied from the source endpoint with a new port, or `nil` if the original endpoint is invalid or if modifying the port for the copy results in an invalid endpoint. Examples of invalid endpoints are malformed IP addresses or port numbers greater than 65535.
