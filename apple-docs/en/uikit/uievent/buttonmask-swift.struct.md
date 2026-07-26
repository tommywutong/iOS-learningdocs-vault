---
title: UIEvent.ButtonMask
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uievent/buttonmask-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uievent/buttonmask-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uievent/buttonmask-swift.struct.json'
content_hash: 'sha256:8f481ba56213926d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEvent](../uievent.md)

# UIEvent.ButtonMask

<sub>Structure</sub>

Constants that indicate which input-device buttons are pressed.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct ButtonMask
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Creating button masks

- [init(rawValue:)](<buttonmask-swift.struct/init(rawvalue_).md>) — Creates a button mask with the specified raw value.
- [UIEventButtonMaskForButtonNumber](<buttonmask-swift.struct/button(__).md>) — Creates a button mask from the specified button index.

### Accessing button masks

- [UIEventButtonMaskPrimary](buttonmask-swift.struct/primary.md) — A constant that represents the primary button on the input device.
- [UIEventButtonMaskSecondary](buttonmask-swift.struct/secondary.md) — A constant that represents the secondary button on the input device.

## See Also

### Getting the button mask

- [buttonMask](buttonmask-swift.property.md) — A bit mask that represents which input-device buttons are pressed for the current event.
