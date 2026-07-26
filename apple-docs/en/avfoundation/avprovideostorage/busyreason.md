---
title: AVProVideoStorage.BusyReason
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avprovideostorage/busyreason
source_url: 'https://developer.apple.com/documentation/avfoundation/avprovideostorage/busyreason'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avprovideostorage/busyreason.json'
content_hash: 'sha256:59b9b4de1f370847'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVProVideoStorage](../avprovideostorage.md)

# AVProVideoStorage.BusyReason

<sub>Structure</sub>

A reason that Pro Video Storage may be busy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
struct BusyReason
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(rawValue:)](<busyreason/init(rawvalue_).md>) _(beta)_

### Type Properties

- [AVProVideoStorageBusyReasonAdjustingCapacity](busyreason/adjustingcapacity.md) — Pro Video Storage is being created or resized. _(beta)_
- [AVProVideoStorageBusyReasonCapturing](busyreason/capturing.md) — A capture to Pro Video Storage is in progress. _(beta)_
- [AVProVideoStorageBusyReasonReplenishing](busyreason/replenishing.md) — Pro Video Storage capacity is being replenished. _(beta)_

## See Also

### Determining whether storage is busy

- [busyReasons](busyreasons.md) — Whether Pro Video Storage is busy and the associated reasons. _(beta)_
