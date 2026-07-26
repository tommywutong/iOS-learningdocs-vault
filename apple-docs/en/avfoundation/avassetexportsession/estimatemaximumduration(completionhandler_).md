---
title: 'estimateMaximumDuration(completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetexportsession/estimatemaximumduration(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/estimatemaximumduration(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/estimatemaximumduration%28completionhandler%3A%29.json'
content_hash: 'sha256:cbd086e9ef3db793'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# estimateMaximumDuration(completionHandler:)

<sub>Instance Method</sub>

Starts estimating the maximum duration of the export while considering the asset, preset, and time range configuration of the export session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func estimateMaximumDuration(completionHandler handler: @escaping @Sendable (CMTime, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var estimatedMaximumDuration: CMTime { get async throws }
```

## Parameters

- `handler` — A callback the system invokes when it finishes its estimation. It passes the callback the following parameters: - **`estimatedMaximumDuration`** — The system’s estimation of the maximum duration. - **`error`** — An optional error object that indicates if an error occurred during processing.
