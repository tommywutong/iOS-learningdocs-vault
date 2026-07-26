---
title: 'init(url:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+（18.0 起废弃）, iPadOS 4.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 1.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avasset/init(url:)-42gl8'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/init(url:)-42gl8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/init%28url%3A%29-42gl8.json'
content_hash: 'sha256:d6a8d4b205074234'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# init(url:)

<sub>Initializer</sub>

Creates an asset that models the media at the specified URL.

> [!warning] Deprecated
> Use AVURLAsset(url:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(url URL: URL)
```

## Parameters

- `URL` — A URL to a local, remote, or HTTP Live Streaming media resource.
