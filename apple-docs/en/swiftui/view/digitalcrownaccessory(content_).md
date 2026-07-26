---
title: 'digitalCrownAccessory(content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/digitalcrownaccessory(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/digitalcrownaccessory(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/digitalcrownaccessory%28content%3A%29.json'
content_hash: 'sha256:182eb3fb797aaa45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# digitalCrownAccessory(content:)

<sub>Instance Method</sub>

Places an accessory View next to the Digital Crown on Apple Watch.

<sub>watchOS</sub>

```swift
nonisolated func digitalCrownAccessory<Content>(@ContentBuilder content: @escaping () -> Content) -> some View where Content : View

```

## Parameters

- `content` — The view to be used as a Digital Crown Accessory.

## Discussion

Use this method to place a custom `View` next to the Digital Crown on Apple Watch. Use [digitalCrownAccessory(_:)](<digitalcrownaccessory(__).md>) to specify the visibility of your custom view.

```swift
struct ZoomingMapView: View {
    // Width of the map displayed on screen in miles
    @State private var zoomLevel: Int = 1.0

    var body: some View {
        CustomMap(width: .miles(zoomLevel))
            .focusable()
            .digitalCrownRotation(value: $zoomLevel)
            .digitalCrownAccessory {
                Text("\(zoomLevel, specifier: "%.2f")MI")
                .background {
                    RoundedRectangle(cornerRadius: 5)
                        .fill(Color.gray)
                }
            }
    }
}
```

## See Also

### Interacting with the Digital Crown

- [digitalCrownAccessory(_:)](<digitalcrownaccessory(__).md>) — Specifies the visibility of Digital Crown accessory Views on Apple Watch.
- [digitalCrownRotation(_:from:through:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)](<digitalcrownrotation(__from_through_sensitivity_iscontinuous_ishapticfeedbackenabled_onchange_onidle_).md>) — Tracks Digital Crown rotations by updating the specified binding.
- [digitalCrownRotation(_:onChange:onIdle:)](<digitalcrownrotation(__onchange_onidle_).md>) — Tracks Digital Crown rotations by updating the specified binding.
- [digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)](<digitalcrownrotation(detent_from_through_by_sensitivity_iscontinuous_ishapticfeedbackenabled_onchange_onidle_).md>) — Tracks Digital Crown rotations by updating the specified binding.
- [digitalCrownRotation(_:)](<digitalcrownrotation(__).md>) — Tracks Digital Crown rotations by updating the specified binding.
- [digitalCrownRotation(_:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:)](<digitalcrownrotation(__from_through_by_sensitivity_iscontinuous_ishapticfeedbackenabled_).md>) — Tracks Digital Crown rotations by updating the specified binding.
- [DigitalCrownEvent](../digitalcrownevent.md) — An event emitted when the user rotates the Digital Crown.
- [DigitalCrownRotationalSensitivity](../digitalcrownrotationalsensitivity.md) — The amount of Digital Crown rotation needed to move between two integer numbers.
