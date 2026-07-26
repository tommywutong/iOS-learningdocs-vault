---
title: DigitalCrownRotationalSensitivity
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/digitalcrownrotationalsensitivity
source_url: 'https://developer.apple.com/documentation/swiftui/digitalcrownrotationalsensitivity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/digitalcrownrotationalsensitivity.json'
content_hash: 'sha256:0e3da7b0bef3c0af'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DigitalCrownRotationalSensitivity

<sub>Enumeration</sub>

The amount of Digital Crown rotation needed to move between two integer numbers.

<sub>watchOS</sub>

```swift
enum DigitalCrownRotationalSensitivity
```

## Overview

You may need to experiment to find the level of sensitivity that works for your use case.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting sensitivity options

- [DigitalCrownRotationalSensitivity.low](digitalcrownrotationalsensitivity/low.md) — Low sensitivity.
- [DigitalCrownRotationalSensitivity.medium](digitalcrownrotationalsensitivity/medium.md) — Medium sensitivity.
- [DigitalCrownRotationalSensitivity.high](digitalcrownrotationalsensitivity/high.md) — High sensitivity.

## See Also

### Interacting with the Digital Crown

- [digitalCrownAccessory(_:)](<view/digitalcrownaccessory(__).md>) — Specifies the visibility of Digital Crown accessory Views on Apple Watch.
- [digitalCrownAccessory(content:)](<view/digitalcrownaccessory(content_).md>) — Places an accessory View next to the Digital Crown on Apple Watch.
- [digitalCrownRotation(_:from:through:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)](<view/digitalcrownrotation(__from_through_sensitivity_iscontinuous_ishapticfeedbackenabled_onchange_onidle_).md>) — Tracks Digital Crown rotations by updating the specified binding.
- [digitalCrownRotation(_:onChange:onIdle:)](<view/digitalcrownrotation(__onchange_onidle_).md>) — Tracks Digital Crown rotations by updating the specified binding.
- [digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)](<view/digitalcrownrotation(detent_from_through_by_sensitivity_iscontinuous_ishapticfeedbackenabled_onchange_onidle_).md>) — Tracks Digital Crown rotations by updating the specified binding.
- [digitalCrownRotation(_:)](<view/digitalcrownrotation(__).md>) — Tracks Digital Crown rotations by updating the specified binding.
- [digitalCrownRotation(_:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:)](<view/digitalcrownrotation(__from_through_by_sensitivity_iscontinuous_ishapticfeedbackenabled_).md>) — Tracks Digital Crown rotations by updating the specified binding.
- [DigitalCrownEvent](digitalcrownevent.md) — An event emitted when the user rotates the Digital Crown.
