---
title: 'loadPlaybackConfigurationOptions(completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetplaybackassistant/loadplaybackconfigurationoptions(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetplaybackassistant/loadplaybackconfigurationoptions(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetplaybackassistant/loadplaybackconfigurationoptions%28completionhandler%3A%29.json'
content_hash: 'sha256:db50b77064773e02'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetPlaybackAssistant](../avassetplaybackassistant.md)

# loadPlaybackConfigurationOptions(completionHandler:)

<sub>Instance Method</sub>

Loads playback configuration options for an asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadPlaybackConfigurationOptions(completionHandler: @escaping @Sendable ([AVAssetPlaybackConfigurationOption]) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var playbackConfigurationOptions: [AVAssetPlaybackConfigurationOption] { get async }
```

## Parameters

- `completionHandler` — A callback the system invokes with an array of [AVAssetPlaybackConfigurationOption](../avassetplaybackconfigurationoption.md) values that describe capabilities of the asset.
