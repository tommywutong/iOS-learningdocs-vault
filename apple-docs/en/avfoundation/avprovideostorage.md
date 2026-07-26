---
title: AVProVideoStorage
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avprovideostorage
source_url: 'https://developer.apple.com/documentation/avfoundation/avprovideostorage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avprovideostorage.json'
content_hash: 'sha256:bae0a8cc492fcc3c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVProVideoStorage

<sub>Class</sub>

A class to track and manage pre-allocated storage for high data rate video capture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVProVideoStorage
```

## Overview

`AVProVideoStorage` is a singleton that manages system-wide pre-allocated storage used during high data rate video capture to ensure I/O determinism and sustain high bandwidth captures (e.g. ProRes).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the shared storage

- [sharedStorage](avprovideostorage/shared.md) — Returns the singleton instance for Pro Video Storage. _(beta)_
- [supported](avprovideostorage/issupported.md) — Whether Pro Video Storage is supported in its current configuration. _(beta)_

### Inspecting capacity

- [initialCapacity](avprovideostorage/initialcapacity.md) — Initial size of Pro Video Storage in bytes. _(beta)_
- [remainingCapacity](avprovideostorage/remainingcapacity.md) — Current size of Pro Video Storage in bytes. _(beta)_
- [- replenishCapacityWithCompletionHandler:](<avprovideostorage/replenishcapacity(completionhandler_).md>) — Performs a best-effort attempt to restore Pro Video Storage to the initial capacity specified by the user in Settings app. _(beta)_

### Determining whether storage is busy

- [busyReasons](avprovideostorage/busyreasons.md) — Whether Pro Video Storage is busy and the associated reasons. _(beta)_
- [BusyReason](avprovideostorage/busyreason.md) — A reason that Pro Video Storage may be busy. _(beta)_

### Presenting the settings interface

- [- openSettings](<avprovideostorage/opensettings().md>) — Opens the Pro Video Storage UI in Settings app. _(beta)_
