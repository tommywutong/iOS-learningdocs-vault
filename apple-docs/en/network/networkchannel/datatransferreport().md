---
title: dataTransferReport()
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networkchannel/datatransferreport()
source_url: 'https://developer.apple.com/documentation/network/networkchannel/datatransferreport()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/datatransferreport%28%29.json'
content_hash: 'sha256:421e8bed7d826aee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# dataTransferReport()

<sub>Instance Method</sub>

Start a data transfer report on a connection. The report begins capturing data when the connection moves to the .ready state, or when the report is created (whichever occurs last). This method will start the connection if it isn’t already started.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dataTransferReport() async throws -> NWConnection.DataTransferReport
```
