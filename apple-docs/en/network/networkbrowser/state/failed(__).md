---
title: 'NetworkBrowser.State.failed(_:)'
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkbrowser/state/failed(_:)'
source_url: 'https://developer.apple.com/documentation/network/networkbrowser/state/failed(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkbrowser/state/failed%28_%3A%29.json'
content_hash: 'sha256:801aa26003e7862f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NetworkBrowser](../../networkbrowser.md) · [State](../state.md)

# NetworkBrowser.State.failed(_:)

<sub>Case</sub>

The browser has irrecoverably failed. Do not call `start()` on the browser to restart it. Instead, `cancel()` the browser and create a new browser.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case failed(NWError)
```
