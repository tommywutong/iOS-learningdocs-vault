---
title: 'accessibilityDropPoint(_:description:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilitydroppoint(_:description:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilitydroppoint(_:description:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilitydroppoint%28_%3Adescription%3Aisenabled%3A%29.json'
content_hash: 'sha256:93ac8c5d2210d7cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityDropPoint(_:description:isEnabled:)

<sub>Instance Method</sub>

The point an assistive technology should use to end a drag interaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated func accessibilityDropPoint(_ point: UnitPoint, description: LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

## Parameters

- `point` — The point the assistive technology will perform a drop interaction.

- `description` — The description of the drop interaction.

- `isEnabled` — If true the accessibility drop point is applied; otherwise the accessibility drop point is unchanged.

## Discussion

Use this modifier when you need to provide a description to users when prompted end a drag interaction.

```swift
struct FolderView: View {
    var folderName: String

    var body: some View {
        FolderIcon(folderName: folderName)
            .accessibilityDropPoint(
                .center, description: Text("Move to \(folderName)"))
    }
}
```

By default, if an accessible view or its subtree has drag and/or drop interactions, they will be automatically exposed by assistive technologies. However, if there is more than one such interaction, each drag or drop should have a description to disambiguate it and give a good user experience.

> [!note] Note
> An accessibility element can have multiple points for a drop, provided they have different descriptions.

## See Also

### Making gestures accessible

- [accessibilityActivationPoint(_:)](<accessibilityactivationpoint(__).md>) — The activation point for an element is the location assistive technologies use to initiate gestures.
- [accessibilityActivationPoint(_:isEnabled:)](<accessibilityactivationpoint(__isenabled_).md>) — The activation point for an element is the location assistive technologies use to initiate gestures.
- [accessibilityDragPoint(_:description:)](<accessibilitydragpoint(__description_).md>) — The point an assistive technology should use to begin a drag interaction.
- [accessibilityDragPoint(_:description:isEnabled:)](<accessibilitydragpoint(__description_isenabled_).md>) — The point an assistive technology should use to begin a drag interaction.
- [accessibilityDropPoint(_:description:)](<accessibilitydroppoint(__description_).md>) — The point an assistive technology should use to end a drag interaction.
- [accessibilityDirectTouch(_:options:)](<accessibilitydirecttouch(__options_).md>) — Explicitly set whether this accessibility element is a direct touch area. Direct touch areas passthrough touch events to the app rather than being handled through an assistive technology, such as VoiceOver. The modifier accepts an optional `AccessibilityDirectTouchOptions` option set to customize the functionality of the direct touch area.
- [accessibilityZoomAction(_:)](<accessibilityzoomaction(__).md>) — Adds an accessibility zoom action to the view. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action.
- [AccessibilityDirectTouchOptions](../accessibilitydirecttouchoptions.md) — An option set that defines the functionality of a view’s direct touch area.
- [AccessibilityZoomGestureAction](../accessibilityzoomgestureaction.md) — Position and direction information of a zoom gesture that someone performs with an assistive technology like VoiceOver.
