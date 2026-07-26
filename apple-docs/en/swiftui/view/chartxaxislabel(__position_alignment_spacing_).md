---
title: 'chartXAxisLabel(_:position:alignment:spacing:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartxaxislabel(_:position:alignment:spacing:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartxaxislabel(_:position:alignment:spacing:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartxaxislabel%28_%3Aposition%3Aalignment%3Aspacing%3A%29.json'
content_hash: 'sha256:38d2ffe5b830ebcb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartXAxisLabel(_:position:alignment:spacing:)

<sub>Instance Method</sub>

Adds x axis label for charts in the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func chartXAxisLabel(_ labelKey: LocalizedStringKey, position: AnnotationPosition = .automatic, alignment: Alignment? = nil, spacing: CGFloat? = nil) -> some View

```

## Parameters

- `labelKey` — The key for the localized label string.

- `position` — The position of the label.

- `alignment` — The alignment of the label.

- `spacing` — The spacing of the label from the axis markers.

## See Also

### Axis Labels

- [chartXAxisLabel(position:alignment:spacing:content:)](<chartxaxislabel(position_alignment_spacing_content_).md>) — Adds x axis label for charts in the view.
- [chartYAxisLabel(_:position:alignment:spacing:)](<chartyaxislabel(__position_alignment_spacing_).md>) — Adds y axis label for charts in the view.
- [chartYAxisLabel(position:alignment:spacing:content:)](<chartyaxislabel(position_alignment_spacing_content_).md>) — Adds y axis label for charts in the view.
- [chartZAxisLabel(_:position:alignment:spacing:)](<chartzaxislabel(__position_alignment_spacing_).md>) — Adds z axis label for charts in the view. It effects 3D charts only.
