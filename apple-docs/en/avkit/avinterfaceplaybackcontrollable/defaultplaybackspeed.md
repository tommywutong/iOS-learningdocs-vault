---
title: defaultPlaybackSpeed
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avinterfaceplaybackcontrollable/defaultplaybackspeed
source_url: 'https://developer.apple.com/documentation/avkit/avinterfaceplaybackcontrollable/defaultplaybackspeed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinterfaceplaybackcontrollable/defaultplaybackspeed.json'
content_hash: 'sha256:2d498ebbb7388e6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVInterfacePlaybackControllable](../avinterfaceplaybackcontrollable.md)

# defaultPlaybackSpeed

<sub>Instance Property</sub>

The default playback speed to use when playback begins. This value is used to set the initial playback rate when starting playback. A value of 1.0 represents normal speed. Must be key-value observable.

<sub>tvOS</sub>

```objc
@property (nonatomic, readwrite) float defaultPlaybackSpeed;
```

## See Also

### Controlling playback speed

- [playbackSpeed](playbackspeed.md) — The current playback speed multiplier. A value of 1.0 represents normal speed, values greater than 1.0 represent faster playback, and values between 0.0 and 1.0 represent slower playback. Must be key-value observable.
- [scanSpeed](scanspeed.md) — The scanning speed multiplier used during fast-forward or rewind operations. A positive value indicates forward scanning, negative indicates backward scanning. Must be key-value observable.
- [supportedSeekCapabilities](supportedseekcapabilities.md) — An option set indicating which timeline navigation operations are supported by this media source. This property defines the available navigation capabilities, including precise seeking to specific time positions and accelerated scanning for fast-forward/rewind operations. The supported modes may vary based on content type, licensing restrictions, or technical limitations of the underlying media format. Must be key-value observable.
