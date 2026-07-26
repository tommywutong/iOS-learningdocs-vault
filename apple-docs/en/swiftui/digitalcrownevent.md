---
title: DigitalCrownEvent
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/digitalcrownevent
source_url: 'https://developer.apple.com/documentation/swiftui/digitalcrownevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/digitalcrownevent.json'
content_hash: 'sha256:8476752a19fe4f6d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DigitalCrownEvent

<sub>Structure</sub>

An event emitted when the user rotates the Digital Crown.

<sub>watchOS</sub>

```swift
struct DigitalCrownEvent
```

## Overview

Use the [digitalCrownRotation(_:)](<view/digitalcrownrotation(__).md>) modifier to receive these events.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting events

- [offset](digitalcrownevent/offset.md) — The offset of the digital crown when this event was sent.
- [velocity](digitalcrownevent/velocity.md) — The velocity at which the offset was changing when this event was sent.

## See Also

### Interacting with the Digital Crown

- [digitalCrownAccessory(_:)](<view/digitalcrownaccessory(__).md>) — Specifies the visibility of Digital Crown accessory Views on Apple Watch.
- [digitalCrownAccessory(content:)](<view/digitalcrownaccessory(content_).md>) — Places an accessory View next to the Digital Crown on Apple Watch.
- [digitalCrownRotation(_:from:through:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)](<view/digitalcrownrotation(__from_through_sensitivity_iscontinuous_ishapticfeedbackenabled_onchange_onidle_).md>) — Tracks Digital Crown rotations by updating the specified binding.
- [digitalCrownRotation(_:onChange:onIdle:)](<view/digitalcrownrotation(__onchange_onidle_).md>) — Tracks Digital Crown rotations by updating the specified binding.
- [digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)](<view/digitalcrownrotation(detent_from_through_by_sensitivity_iscontinuous_ishapticfeedbackenabled_onchange_onidle_).md>) — Tracks Digital Crown rotations by updating the specified binding.
- [digitalCrownRotation(_:)](<view/digitalcrownrotation(__).md>) — Tracks Digital Crown rotations by updating the specified binding.
- [digitalCrownRotation(_:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:)](<view/digitalcrownrotation(__from_through_by_sensitivity_iscontinuous_ishapticfeedbackenabled_).md>) — Tracks Digital Crown rotations by updating the specified binding.
- [DigitalCrownRotationalSensitivity](digitalcrownrotationalsensitivity.md) — The amount of Digital Crown rotation needed to move between two integer numbers.
