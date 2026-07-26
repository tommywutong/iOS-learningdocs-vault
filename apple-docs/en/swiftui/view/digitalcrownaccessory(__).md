---
title: 'digitalCrownAccessory(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/digitalcrownaccessory(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/digitalcrownaccessory(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/digitalcrownaccessory%28_%3A%29.json'
content_hash: 'sha256:20703ae533e9acb2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# digitalCrownAccessory(_:)

<sub>Instance Method</sub>

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

<sub>watchOS</sub>

```swift
nonisolated func digitalCrownAccessory(_ visibility: Visibility) -> some View

```

## Parameters

- `visibility` — The visibility of the digital crown accessory.

## Discussion

Use this method to customize the visibility of a Digital Crown accessory `View` created with the `View/digitalCrownAccessory(_ content:)` modifier. You may want to keep an accessory visible even when the Digital Crown Indicator is not visible to indicate what scrolling the crown will do.

## See Also

### Interacting with the Digital Crown

- [digitalCrownAccessory(content:)](<digitalcrownaccessory(content_).md>) — Places an accessory View next to the Digital Crown on Apple Watch.
- [digitalCrownRotation(_:from:through:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)](<digitalcrownrotation(__from_through_sensitivity_iscontinuous_ishapticfeedbackenabled_onchange_onidle_).md>) — Tracks Digital Crown rotations by updating the specified binding.
- [digitalCrownRotation(_:onChange:onIdle:)](<digitalcrownrotation(__onchange_onidle_).md>) — Tracks Digital Crown rotations by updating the specified binding.
- [digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)](<digitalcrownrotation(detent_from_through_by_sensitivity_iscontinuous_ishapticfeedbackenabled_onchange_onidle_).md>) — Tracks Digital Crown rotations by updating the specified binding.
- [digitalCrownRotation(_:)](<digitalcrownrotation(__).md>) — Tracks Digital Crown rotations by updating the specified binding.
- [digitalCrownRotation(_:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:)](<digitalcrownrotation(__from_through_by_sensitivity_iscontinuous_ishapticfeedbackenabled_).md>) — Tracks Digital Crown rotations by updating the specified binding.
- [DigitalCrownEvent](../digitalcrownevent.md) — An event emitted when the user rotates the Digital Crown.
- [DigitalCrownRotationalSensitivity](../digitalcrownrotationalsensitivity.md) — The amount of Digital Crown rotation needed to move between two integer numbers.
