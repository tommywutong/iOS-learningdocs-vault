---
title: AVAssetCache
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetcache
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetcache'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetcache.json'
content_hash: 'sha256:cf46196a7fe60038'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetCache

<sub>Class</sub>

An object that you use to inspect locally cached media data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVAssetCache
```

## Overview

You can download HTTP Live Streaming assets to an iOS device using the [AVAssetDownloadURLSession](avassetdownloadurlsession.md) and [AVAssetDownloadTask](avassetdownloadtask.md) classes.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Inspecting the cached media

- [playableOffline](avassetcache/isplayableoffline.md) — A Boolean value that indicates whether the asset is playable without an internet connection.
- [- mediaSelectionOptionsInMediaSelectionGroup:](<avassetcache/mediaselectionoptions(in_).md>) — Returns an array of locally cached media selection options that are available for offline use.
- [- mediaPresentationLanguagesForMediaSelectionGroup:](<avassetcache/mediapresentationlanguages(for_).md>) — Returns an array of extended language tags for languages that can be selected for offline operations via use of the AVMediaSelectionGroup’s AVCustomMediaSelectionScheme.
- [- mediaPresentationSettingsForMediaSelectionGroup:](<avassetcache/mediapresentationsettings(for_).md>) — For each AVMediaPresentationSelector defined by the AVCustomMediaSelectionScheme of an AVMediaSelectionGroup, returns the AVMediaPresentationSettings that can be satisfied for offline operations, e.g. playback.
