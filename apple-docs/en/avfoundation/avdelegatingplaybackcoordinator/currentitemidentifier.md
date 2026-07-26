---
title: currentItemIdentifier
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avdelegatingplaybackcoordinator/currentitemidentifier
source_url: 'https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinator/currentitemidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdelegatingplaybackcoordinator/currentitemidentifier.json'
content_hash: 'sha256:c4c40a44b4d1f3c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDelegatingPlaybackCoordinator](../avdelegatingplaybackcoordinator.md)

# currentItemIdentifier

<sub>Instance Property</sub>

An identifier of the current item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var currentItemIdentifier: String? { get }
```

## Discussion

The coordinator sets this value in a previous call to [- transitionToItemWithIdentifier:proposingInitialTimingBasedOnTimebase:](<transitiontoitem(withidentifier_proposinginitialtimingbasedon_).md>).
