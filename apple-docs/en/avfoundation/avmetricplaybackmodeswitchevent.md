---
title: AVMetricPlaybackModeSwitchEvent
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avmetricplaybackmodeswitchevent
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetricplaybackmodeswitchevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetricplaybackmodeswitchevent.json'
content_hash: 'sha256:d416ca5517739528'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMetricPlaybackModeSwitchEvent

<sub>Class</sub>

Represents a change in playback state, entering one of AVMetricPlaybackMode

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVMetricPlaybackModeSwitchEvent
```

## Overview

Subclasses of this type that are used from Swift must fulfill the requirements of a Sendable type.

## Relationships

- **Inherits From**: [AVMetricEvent](avmetricevent.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Identifying the playback mode

- [mode](avmetricplaybackmodeswitchevent/mode.md) — Returns the mode into which playback entered. _(beta)_

## See Also

### Playback mode

- [AVMetricPlaybackMode](avmetricplaybackmode.md) — These constants are the possible playback modes returned by the property “mode” on AVMetricPlaybackModeSwitchEvent
