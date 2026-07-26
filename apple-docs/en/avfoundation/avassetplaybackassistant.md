---
title: AVAssetPlaybackAssistant
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetplaybackassistant
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetplaybackassistant'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetplaybackassistant.json'
content_hash: 'sha256:8e14d87386c72c27'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetPlaybackAssistant

<sub>Class</sub>

An object that provides playback information for an asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVAssetPlaybackAssistant
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a playback assistant

- [+ assetPlaybackAssistantWithAsset:](<avassetplaybackassistant/init(asset_).md>) — Creates a playback assistant to inspect the specified asset.

### Loading playback configuration options

- [- loadPlaybackConfigurationOptionsWithCompletionHandler:](<avassetplaybackassistant/loadplaybackconfigurationoptions(completionhandler_).md>) — Loads playback configuration options for an asset.

## See Also

### Utilities

- [AVAssetPlaybackConfigurationOption](avassetplaybackconfigurationoption.md) — A structure that defines playback configuration options for an asset.
