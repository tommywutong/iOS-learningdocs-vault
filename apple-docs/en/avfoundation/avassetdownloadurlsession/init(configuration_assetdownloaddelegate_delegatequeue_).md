---
title: 'init(configuration:assetDownloadDelegate:delegateQueue:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetdownloadurlsession/init(configuration:assetdownloaddelegate:delegatequeue:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadurlsession/init(configuration:assetdownloaddelegate:delegatequeue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadurlsession/init%28configuration%3Aassetdownloaddelegate%3Adelegatequeue%3A%29.json'
content_hash: 'sha256:4448e6ffe2afd91d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetDownloadURLSession](../avassetdownloadurlsession.md)

# init(configuration:assetDownloadDelegate:delegateQueue:)

<sub>Initializer</sub>

Creates a URL session to download assets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
init(configuration: URLSessionConfiguration, assetDownloadDelegate delegate: (any AVAssetDownloadDelegate)?, delegateQueue: OperationQueue?)
```

## Parameters

- `configuration` — The configuration for this download session. The configuration you provide must be a _background_ configuration or the system raises an exception.

- `delegate` — The delegate object to handle asset download progress updates and other session related events.

- `delegateQueue` — The queue to receive delegate callbacks on. If you specify `nil`, the system provides a serial queue.

## Return Value

A new download session.

## See Also

### Creating a download session

- [AVAssetDownloadDelegate](../avassetdownloaddelegate.md) — A protocol that defines the methods to implement to respond to asset-download events.
