---
title: 'states(updateInterval:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetexportsession/states(updateinterval:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/states(updateinterval:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/states%28updateinterval%3A%29.json'
content_hash: 'sha256:46fb00d0bc4692a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# states(updateInterval:)

<sub>Instance Method</sub>

Monitors the progress state of an export operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func states(updateInterval: TimeInterval = .infinity) -> some Sendable & AsyncSequence<AVAssetExportSession.State, Never>

```

## Parameters

- `updateInterval` — The time interval between updates. The value must be greater than `0`.

## Return Value

An asynchronous sequence of states.

## See Also

### Monitoring export progress

- [State](state.md) — Constants that indicate the state of an export operation.
- [Status](status-swift.enum.md) — Values that indicate the state of an export session.
