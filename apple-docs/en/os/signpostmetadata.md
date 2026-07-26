---
title: SignpostMetadata
framework: os
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/signpostmetadata
source_url: 'https://developer.apple.com/documentation/os/signpostmetadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/signpostmetadata.json'
content_hash: 'sha256:2935065e7b34f4fb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# SignpostMetadata

<sub>Type Alias</sub>

The type that represents a message you attach to a signpost.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias SignpostMetadata = OSLogMessage
```

## See Also

### Starting a Signposted Interval

- [beginInterval(_:id:)](<ossignposter/begininterval(__id_).md>) — Begins a signposted interval.
- [beginInterval(_:id:_:)](<ossignposter/begininterval(__id___).md>) — Begins a signposted interval and attaches the specified message.
- [beginAnimationInterval(_:id:)](<ossignposter/beginanimationinterval(__id_).md>) — Begins a signposted interval for measuring an animation.
- [beginAnimationInterval(_:id:_:)](<ossignposter/beginanimationinterval(__id___).md>) — Begins a signposted interval for measuring an animation, and attaches a message.
- [OSSignpostIntervalState](ossignpostintervalstate.md) — An object that tracks the state of a signposted interval.
