---
title: loopingPlayerItems
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerlooper/loopingplayeritems
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerlooper/loopingplayeritems'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerlooper/loopingplayeritems.json'
content_hash: 'sha256:1c7bc7f8277979ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerLooper](../avplayerlooper.md)

# loopingPlayerItems

<sub>Instance Property</sub>

An array containing replicas of the template player item used to accomplish the looping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var loopingPlayerItems: [AVPlayerItem] { get }
```

## Discussion

`AVPlayerLooper` creates replicas of the template [AVPlayerItem](../avplayeritem.md) using the [copyWithZone:](../../objectivec/nsobject-swift.class/copywithzone_.md) method and inserts them in the queue player’s queue to accomplish the looping. You can determine the number of replicas created and can listen for notifications and property changes from the replicas if desired.

Access to the [AVPlayerItem](../avplayeritem.md) replicas are for informational purposes and to allow you to apply any configuration that is not transferred from the template player item to the replicas. For instance, any instances of [AVPlayerItemOutput](../avplayeritemoutput.md) and [AVPlayerItemMediaDataCollector](../avplayeritemmediadatacollector.md) attached to the template player item are not transferred to the replicas so you should add them to each replica item if needed.

> [!important] Important
> You should not modify any properties of the replicas that would disrupt looping playback. This includes properties such as the playhead time/date, selected media option, and forward playback end time.

## See Also

### Configuring looping

- [- disableLooping](<disablelooping().md>) — Disables looping for the player queue.
