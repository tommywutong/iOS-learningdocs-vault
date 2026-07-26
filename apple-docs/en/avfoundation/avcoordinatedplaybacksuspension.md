---
title: AVCoordinatedPlaybackSuspension
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcoordinatedplaybacksuspension
source_url: 'https://developer.apple.com/documentation/avfoundation/avcoordinatedplaybacksuspension'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcoordinatedplaybacksuspension.json'
content_hash: 'sha256:da773525fad308a4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCoordinatedPlaybackSuspension

<sub>Class</sub>

An object that represents a temporary suspension of coordinated playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVCoordinatedPlaybackSuspension
```

## Overview

See the playback coordinator’s [- beginSuspensionForReason:](<avplaybackcoordinator/beginsuspension(for_).md>) method for details about suspending playback.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Inspecting a suspension

- [beginDate](avcoordinatedplaybacksuspension/begindate.md) — The time the suspension begins.
- [reason](avcoordinatedplaybacksuspension/reason-swift.property.md) — The reason for the suspension.
- [Reason](avcoordinatedplaybacksuspension/reason-swift.struct.md) — Constants that identify playback suspension reasons.

### Ending a suspension

- [- end](<avcoordinatedplaybacksuspension/end().md>) — Ends a suspension.
- [- endProposingNewTime:](<avcoordinatedplaybacksuspension/end(proposingnewtime_).md>) — Ends a suspension and proposes a new playback time to the group.

### Initializers

- [init(_:)](<avcoordinatedplaybacksuspension/reason-swift.struct/init(__).md>) — Creates a suspension with a string.
- [init(rawValue:)](<avcoordinatedplaybacksuspension/reason-swift.struct/init(rawvalue_).md>) — Creates a suspension with a raw string value.

## See Also

### Suspending state coordination

- [- beginSuspensionForReason:](<avplaybackcoordinator/beginsuspension(for_).md>) — Tells the coordinator to stop sending playback commands temporarily when the playback object disconnects from the group activity.
- [- expectedItemTimeAtHostTime:](<avplaybackcoordinator/expecteditemtime(athosttime_).md>) — Returns a time in the current item’s timeline that the coordinator expects to play at the specified host time.
