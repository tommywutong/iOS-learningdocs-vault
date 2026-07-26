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
doc_path: '/documentation/swiftui/modifiedcontent/accessibilityscrollstatus(_:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibilityscrollstatus(_:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modifiedcontent/accessibilityscrollstatus%28_%3Aisenabled%3A%29.json'
content_hash: 'sha256:81eccec2f714f27b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ModifiedContent](../modifiedcontent.md)

# accessibilityScrollStatus(_:isEnabled:)

<sub>Instance Method</sub>

Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func accessibilityScrollStatus(_ status: LocalizedStringResource, isEnabled: Bool = true) -> ModifiedContent<Content, Modifier>
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
