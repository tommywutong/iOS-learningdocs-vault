---
title: disableLooping()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerlooper/disablelooping()
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerlooper/disablelooping()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerlooper/disablelooping%28%29.json'
content_hash: 'sha256:901485ceec420a71'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerLooper](../avplayerlooper.md)

# disableLooping()

<sub>Instance Method</sub>

Disables looping for the player queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func disableLooping()
```

## Discussion

The player looper will stop performing player queue operations for looping and let the current looping item replica play to the end. The player’s original [actionAtItemEnd](../avplayer/actionatitemend-swift.property.md) property will be restored afterwards.

## See Also

### Configuring looping

- [loopingPlayerItems](loopingplayeritems.md) — An array containing replicas of the template player item used to accomplish the looping.
