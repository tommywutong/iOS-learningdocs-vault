---
title: UIPress.Phase
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipress/phase-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uipress/phase-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipress/phase-swift.enum.json'
content_hash: 'sha256:0a1e80614689cde1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPress](../uipress.md)

# UIPress.Phase

<sub>Enumeration</sub>

Constants that represent the phases of a button press.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Phase
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIPressPhaseBegan](phase-swift.enum/began.md) — A physical button was pressed.
- [UIPressPhaseChanged](phase-swift.enum/changed.md) — A button moved, or the force property changed.
- [UIPressPhaseStationary](phase-swift.enum/stationary.md) — A button was pressed but hasn’t moved since the previous event.
- [UIPressPhaseEnded](phase-swift.enum/ended.md) — A button was released.
- [UIPressPhaseCancelled](phase-swift.enum/cancelled.md) — The system canceled tracking for the button.

### Initializers

- [init(rawValue:)](<phase-swift.enum/init(rawvalue_).md>)

## See Also

### Constants

- [PressType](presstype.md) — Constants that represent buttons that a person can press.
