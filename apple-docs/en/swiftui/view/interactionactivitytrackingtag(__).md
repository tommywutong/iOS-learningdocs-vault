---
title: 'interactionActivityTrackingTag(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/interactionactivitytrackingtag(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/interactionactivitytrackingtag(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/interactionactivitytrackingtag%28_%3A%29.json'
content_hash: 'sha256:65339f35ad43de28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# interactionActivityTrackingTag(_:)

<sub>Instance Method</sub>

Sets a tag that you use for tracking interactivity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func interactionActivityTrackingTag(_ tag: String) -> some View

```

## Parameters

- `tag` — The tag used to track user interactions hosted by this view as activities.

## Return Value

A view that uses a tracking tag.

## Discussion

The following example tracks the scrolling activity of a [List](../list.md):

```swift
List {
    Section("Today") {
        ForEach(messageStore.today) { message in
            Text(message.title)
        }
    }
}
.interactionActivityTrackingTag("MessagesList")
```

The resolved activity tracking tag is additive, so using the modifier across the view hierarchy builds the tag from top to bottom. The example below shows a hierarchical usage of this modifier with the resulting tag `Home-Feed`:

```swift
var body: some View {
    Home()
        .interactionActivityTrackingTag("Home")
}

struct Home: View {
    var body: some View {
        List {
            Text("A List Item")
            Text("A Second List Item")
            Text("A Third List Item")
        }
        .interactionActivityTrackingTag("Feed")
    }
}
```

## See Also

### Managing view interaction

- [disabled(_:)](<disabled(__).md>) — Adds a condition that controls whether users can interact with this view.
- [isEnabled](../environmentvalues/isenabled.md) — A Boolean value that indicates whether the view associated with this environment allows user interaction.
- [invalidatableContent(_:)](<invalidatablecontent(__).md>) — Mark the receiver as their content might be invalidated.
