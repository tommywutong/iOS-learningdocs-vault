---
title: 'accessibilityScrollStatus(_:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityscrollstatus(_:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityscrollstatus(_:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityscrollstatus%28_%3Aisenabled%3A%29.json'
content_hash: 'sha256:43765c42b503a9c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityScrollStatus(_:isEnabled:)

<sub>Instance Method</sub>

Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func accessibilityScrollStatus(_ status: LocalizedStringResource, isEnabled: Bool = true) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

## Parameters

- `status` — The current status of the scroll view.

- `isEnabled` — If true the accessibility scroll status is applied; otherwise the accessibility scroll status is unchanged.

## Discussion

Use this modifier to provide a description of the content at the current position in the scroll view. For example, you could use this modifier to announce the current month being scrolled to in a view that contains a calendar.

```swift
@State private var position = ScrollPosition(idType: Month.ID.self)

ScrollView {
    LazyVStack {
        ForEach(months) { months in
            MonthView(month: months)
        }
    }
    .scrollTargetLayout()
}
.scrollPosition($position)
.accessibilityScrollStatus("\(months.name(position.viewID)) \(year)")
```

By default, VoiceOver announces “Page X of Y” while scrolling.

## See Also

### Actions

- [accessibilityAction(_:_:)](<accessibilityaction(____).md>) — Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityActions(_:)](<accessibilityactions(__).md>) — Adds multiple accessibility actions to the view.
- [accessibilityActions(category:_:)](<accessibilityactions(category___).md>) — Adds multiple accessibility actions to the view with a specific category. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action and are grouped by their category. When multiple action modifiers with an equal category are applied to the view, the actions are combined together.
- [accessibilityAction(named:_:)](<accessibilityaction(named___).md>) — Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityAction(action:label:)](<accessibilityaction(action_label_).md>) — Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityAction(intent:label:)](<accessibilityaction(intent_label_).md>) — Adds an accessibility action labeled by the contents of `label` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [accessibilityAction(_:intent:)](<accessibilityaction(__intent_).md>) — Adds an accessibility action representing `actionKind` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [accessibilityAction(named:intent:)](<accessibilityaction(named_intent_).md>) — Adds an accessibility action labeled `name` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [accessibilityAdjustableAction(_:)](<accessibilityadjustableaction(__).md>) — Adds an accessibility adjustable action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [accessibilityScrollAction(_:)](<accessibilityscrollaction(__).md>) — Adds an accessibility scroll action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
