---
title: establishmentReport()
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networkchannel/establishmentreport()
source_url: 'https://developer.apple.com/documentation/network/networkchannel/establishmentreport()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/establishmentreport%28%29.json'
content_hash: 'sha256:668dd30db7f1e6a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# establishmentReport()

<sub>Instance Method</sub>

Asynchronously request the establishment report for this connection. If called prior to the connection being in the .ready state, this method will wait until the connection becomes ready and then deliver the report. This method will start the connection if it isn’t already started.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func establishmentReport() async throws -> NWConnection.EstablishmentReport
```
