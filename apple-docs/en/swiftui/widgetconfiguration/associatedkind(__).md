---
title: 'associatedKind(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/widgetconfiguration/associatedkind(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/widgetconfiguration/associatedkind(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widgetconfiguration/associatedkind%28_%3A%29.json'
content_hash: 'sha256:770c7265626a86ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WidgetConfiguration](../widgetconfiguration.md)

# associatedKind(_:)

<sub>Instance Method</sub>

Tells the system that a relevance-based widget can replace a timeline-based widget.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency func associatedKind(_ associatedKind: String?) -> some WidgetConfiguration

```

## Discussion

If you offer a timeline-based widget and a widget that uses relevance clues, a person could pin the timeline widget to the Smart Stack, and several instances of the relevance-based widget could appear in the Smart Stack, causing the stack to run out of space. To allow the Smart Stack to display the most relevant widgets by replacing the timeline-based widget with your widgets that use relevance clues, associate your timeline-based widget with relevance widget configuration using `associatedKind(_:)`.

> [!note] Note
> Use this modifier for a widget you configure with a `RelevanceConfiguration` and provide an associated timeline-based widget. The system ignores associations with other relevance-based widgets and if your configuration doesn’t conform to `RelevanceConfiguration`.

For more information about widgets that appear in the Smart Stack on Apple Watch, refer to doc:Widget-Suggestions-In-Smart-Stacks.

- parameter: associatedKind: The string that identifies the associated timeline-based widget.
