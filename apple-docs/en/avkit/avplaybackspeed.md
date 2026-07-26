---
title: AVPlaybackSpeed
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplaybackspeed
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackspeed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackspeed.json'
content_hash: 'sha256:ec3d29cb0c56e92f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlaybackSpeed

<sub>Class</sub>

An object that represents a user-selectable playback speed in a playback user interface.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVPlaybackSpeed
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Retrieving Default Speeds

- [systemDefaultSpeeds](avplaybackspeed/systemdefaultspeeds.md) — A list of playback speeds the system uses by default.

### Creating a Playback Speed

- [- initWithRate:localizedName:](<avplaybackspeed/init(rate_localizedname_).md>) — Creates a playback speed with a rate and localized name.

### Inspecting Speed Details

- [rate](avplaybackspeed/rate.md) — The playback rate to use when you select this speed.
- [localizedName](avplaybackspeed/localizedname.md) — A localized name for a speed that’s suitable for display in a user interface.
- [localizedNumericName](avplaybackspeed/localizednumericname.md) — A localized numeric name for a speed that’s suitable for display in a user interface.

## See Also

### Configuring the playback speed

- [speeds](avplayerview/speeds.md) — A list of user-selectable playback speeds to show in the playback speed control.
- [selectedSpeed](avplayerview/selectedspeed.md) — The currently selected playback speed.
- [- selectSpeed:](<avplayerview/selectspeed(__).md>) — Selects a specified playback speed.
