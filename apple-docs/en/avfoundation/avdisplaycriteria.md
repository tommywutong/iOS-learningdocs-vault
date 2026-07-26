---
title: AVDisplayCriteria
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [tvOS 11.2+, visionOS 1.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avdisplaycriteria
source_url: 'https://developer.apple.com/documentation/avfoundation/avdisplaycriteria'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdisplaycriteria.json'
content_hash: 'sha256:3075b36668af7c42'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVDisplayCriteria

<sub>Class</sub>

An object the system uses to guide the selection of a display mode in tvOS.

<sub>tvOS, visionOS</sub>

```swift
class AVDisplayCriteria
```

## Overview

In tvOS, this object provides the display criteria that an [AVDisplayManager](../avkit/avdisplaymanager.md) uses to set an appropriate display mode, such as switching to HDR, when presenting a video asset. If your app uses [AVPlayerViewController](../avkit/avplayerviewcontroller.md) for its player user interface, the system automatically applies the display critera when it presents the asset. If you use a custom player interface, load the value of an asset’s [preferredDisplayCriteria](avpartialasyncproperty/preferreddisplaycriteria.md) property and set it on the window’s [avDisplayManager](../uikit/uiwindow/avdisplaymanager.md) object.

> [!important] Important
> Most apps don’t create instances of this class, and instead retrieve the preferred display criteria from a media asset. If your app doesn’t use [AVAsset](avasset.md), such as a streaming app that renders sample buffers using [AVSampleBufferDisplayLayer](avsamplebufferdisplaylayer.md), you can manually create an instance using the [- initWithRefreshRate:formatDescription:](<avdisplaycriteria/init(refreshrate_formatdescription_).md>) initializer.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Create a display criteria

- [- initWithRefreshRate:formatDescription:](<avdisplaycriteria/init(refreshrate_formatdescription_).md>) — Creates a display criteria object with the specified refresh rate and format description.

## See Also

### Loading asset preferences

- [preferredRate](avpartialasyncproperty/preferredrate.md) — The asset’s rate preference for playing its media.
- [preferredVolume](avpartialasyncproperty/preferredvolume-20mb3.md) — The asset’s volume preference for playing its audible media.
- [preferredTransform](avpartialasyncproperty/preferredtransform-80d13.md) — The asset’s transform preference to apply to its visual content during presentation or processing.
- [preferredDisplayCriteria](avpartialasyncproperty/preferreddisplaycriteria.md) — The asset’s display mode preference for optimal playback of its content.
