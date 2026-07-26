---
title: 'init(asset:title:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetdownloadconfiguration/init(asset:title:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadconfiguration/init(asset:title:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadconfiguration/init%28asset%3Atitle%3A%29.json'
content_hash: 'sha256:f44db71ea60dfb80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetDownloadConfiguration](../avassetdownloadconfiguration.md)

# init(asset:title:)

<sub>Initializer</sub>

Creates a download configuration for a media asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(asset: AVURLAsset, title: String)
```

## Parameters

- `asset` — The asset the task downloads.

- `title` — A human-readable title for this asset. The system displays this value in the usage pane of the Settings app; choose a title suitable for display in the user’s preferred language.
