---
title: 'chartYAxisLabel(position:alignment:spacing:content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartyaxislabel(position:alignment:spacing:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartyaxislabel(position:alignment:spacing:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartyaxislabel%28position%3Aalignment%3Aspacing%3Acontent%3A%29.json'
content_hash: 'sha256:009b6c34493e913a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartYAxisLabel(position:alignment:spacing:content:)

<sub>Instance Method</sub>

Adds y axis label for charts in the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func chartYAxisLabel<C>(position: AnnotationPosition = .automatic, alignment: Alignment? = nil, spacing: CGFloat? = nil, @ViewBuilder content: () -> C) -> some View where C : View

```

## Parameters

- `position` — The position of the label.

- `alignment` — The alignment of the label.

- `spacing` — The spacing of the label from the axis markers.

- `content` — The label content.

## See Also

### Axis Labels

- [chartXAxisLabel(_:position:alignment:spacing:)](<chartxaxislabel(__position_alignment_spacing_).md>) — Adds x axis label for charts in the view.
- [chartXAxisLabel(position:alignment:spacing:content:)](<chartxaxislabel(position_alignment_spacing_content_).md>) — Adds x axis label for charts in the view.
- [chartYAxisLabel(_:position:alignment:spacing:)](<chartyaxislabel(__position_alignment_spacing_).md>) — Adds y axis label for charts in the view.
- [chartZAxisLabel(_:position:alignment:spacing:)](<chartzaxislabel(__position_alignment_spacing_).md>) — Adds z axis label for charts in the view. It effects 3D charts only.
