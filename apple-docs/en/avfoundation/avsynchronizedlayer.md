---
title: AVSynchronizedLayer
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsynchronizedlayer
source_url: 'https://developer.apple.com/documentation/avfoundation/avsynchronizedlayer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsynchronizedlayer.json'
content_hash: 'sha256:0d33f64208a0d42d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVSynchronizedLayer

<sub>Class</sub>

A Core Animation layer that derives its timing from a player item so that you can synchronize layer animations with media playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVSynchronizedLayer
```

## Overview

You can create an arbitrary number of synchronized layers from the same `AVPlayerItem` object.

A synchronized layer is similar to a [CATransformLayer](../quartzcore/catransformlayer.md) object in that it doesn’t display anything itself, it just confers state upon its layer subtree. `AVSynchronizedLayer` confers its timing state, synchronizing the timing of layers in its subtree with that of a player item.

Any `CoreAnimation` layer with animation property set that is added as a sublayer of `AVSynchronizedLayer` should set the animation’s [beginTime](../quartzcore/camediatiming/begintime.md) property to a non-zero positive value so animations will be interpreted on the player item’s timeline. `CoreAnimation` replaces the default `beginTime` of 0.0 with [CACurrentMediaTime()](<../quartzcore/cacurrentmediatime().md>). To start the animation from time 0, use a small positive value like [AVCoreAnimationBeginTimeAtZero](avcoreanimationbegintimeatzero.md).

You might use a layer as shown in the following example:

```objc
AVPlayerItem *playerItem = <#Get a player item#>;
CALayer *superLayer =  <#Get a layer#>;
// Set up a synchronized layer to sync the layer timing of its subtree
// with the playback of the playerItem/
AVSynchronizedLayer *syncLayer = [AVSynchronizedLayer synchronizedLayerWithPlayerItem:playerItem];
[syncLayer addSublayer:<#Another layer#>];    // These sublayers will be synchronized.
[superLayer addSublayer:syncLayer];
```

## Relationships

- **Inherits From**: [CALayer](../quartzcore/calayer.md)

- **Conforms To**: [CAMediaTiming](../quartzcore/camediatiming.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a synchronized layer

- [+ synchronizedLayerWithPlayerItem:](<avsynchronizedlayer/init(playeritem_).md>) — Creates a new synchronized layer with timing synchronized with a given player item.

### Managing the player item

- [playerItem](avsynchronizedlayer/playeritem.md) — The player item to which the timing of the layer is synchronized.

### Supporting types

- [AVCoreAnimationBeginTimeAtZero](avcoreanimationbegintimeatzero.md) — A value that sets an animation begin time to `0`.

## See Also

### Presentation

- [Monitoring playback progress in your app](monitoring-playback-progress-in-your-app.md) — Observe the playback of a media asset to update your app’s user-interface state.
- [Using HEVC video with alpha](using-hevc-video-with-alpha.md) — Play, write, and export HEVC video with an alpha channel to add overlay effects to your video processing.
- [AVPlayerLayer](avplayerlayer.md) — An object that presents the visual contents of a player object.
