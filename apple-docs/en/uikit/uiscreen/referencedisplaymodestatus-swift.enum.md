---
title: UIScreen.ReferenceDisplayModeStatus
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/referencedisplaymodestatus-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/referencedisplaymodestatus-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/referencedisplaymodestatus-swift.enum.json'
content_hash: 'sha256:c1f08e7d66e536b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# UIScreen.ReferenceDisplayModeStatus

<sub>Enumeration</sub>

Describes a screen’s reference display mode status.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
enum ReferenceDisplayModeStatus
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Statuses

- [UIScreenReferenceDisplayModeStatusNotSupported](referencedisplaymodestatus-swift.enum/notsupported.md) — A status that indicates the screen doesn’t provide a reference display mode.
- [UIScreenReferenceDisplayModeStatusNotEnabled](referencedisplaymodestatus-swift.enum/notenabled.md) — A status that indicates the screen provides a reference display mode but it’s in a disabled state.
- [UIScreenReferenceDisplayModeStatusLimited](referencedisplaymodestatus-swift.enum/limited.md) — A status that indicates the screen’s in a limited reference display mode.
- [UIScreenReferenceDisplayModeStatusEnabled](referencedisplaymodestatus-swift.enum/enabled.md) — A status that indicates the screen’s in an accurate reference display mode.

### Initializers

- [init(rawValue:)](<referencedisplaymodestatus-swift.enum/init(rawvalue_).md>)

## See Also

### Getting the reference display mode status

- [referenceDisplayModeStatus](referencedisplaymodestatus-swift.property.md) — The status of the screen’s reference display mode.
- [currentEDRHeadroom](currentedrheadroom.md) — The screen’s current headroom when displaying extended dynamic range content.
- [potentialEDRHeadroom](potentialedrheadroom.md) — The screen’s maximum headroom when displaying extended dynamic range content.
