---
title: 'estimateOutputFileLength(completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetexportsession/estimateoutputfilelength(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/estimateoutputfilelength(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/estimateoutputfilelength%28completionhandler%3A%29.json'
content_hash: 'sha256:439491cf7b6fe6b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# estimateOutputFileLength(completionHandler:)

<sub>Instance Method</sub>

Starts estimating the output file length of the export while considering the asset, preset, and time range configuration of the export session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func estimateOutputFileLength(completionHandler handler: @escaping @Sendable (Int64, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var estimatedOutputFileLengthInBytes: Int64 { get async throws }
```

## Parameters

- `handler` — A callback the system invokes when it finishes its estimation. It passes the callback the following parameters: - **`estimatedOutputFileLength`** — The system’s estimation of the output file length. - **`error`** — An error object if the request fails; otherwise, `nil`.
