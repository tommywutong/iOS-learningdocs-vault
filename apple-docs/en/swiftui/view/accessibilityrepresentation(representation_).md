---
title: 'accessibilityRepresentation(representation:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityrepresentation(representation:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityrepresentation(representation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityrepresentation%28representation%3A%29.json'
content_hash: 'sha256:bbb88f8cb651affe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityRepresentation(representation:)

<sub>Instance Method</sub>

Replaces one or more accessibility elements for this view with new accessibility elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityRepresentation<V>(@ContentBuilder representation: () -> V) -> some View where V : View

```

## Parameters

- `representation` — A hidden view that the accessibility system uses to generate accessibility elements.

## Discussion

You can make controls accessible by using a custom style. For example, a custom [ToggleStyle](../togglestyle.md) that you create inherits the accessibility features of [Toggle](../toggle.md) automatically. When you can’t use the parent view’s accessibility elements, use the `accessibilityRepresentation(representation:)` modifier instead. This modifier replaces default accessibility elements with different accessibility elements that you provide. You use synthetic, non-visual accessibility elements to represent what the view displays.

The example below makes a custom adjustable control accessible by explicitly defining the representation of its step increments using a [Slider](../slider.md):

```swift
var body: some View {
    VStack {
        SliderTrack(...) // Custom slider implementation.
    }
    .accessibilityRepresentation {
        Slider(value: $value, in: 0...100) {
            Text("Label")
        }
    }
}
```

SwiftUI hides the view that you provide in the `representation` closure and makes it non-interactive. The framework uses it only to generate accessibility elements.

## See Also

### Creating accessible elements

- [accessibilityElement(children:)](<accessibilityelement(children_).md>) — Creates a new accessibility element, or modifies the [AccessibilityChildBehavior](../accessibilitychildbehavior.md) of the existing accessibility element.
- [accessibilityChildren(children:)](<accessibilitychildren(children_).md>) — Replaces the existing accessibility element’s children with one or more new synthetic accessibility elements.
- [AccessibilityChildBehavior](../accessibilitychildbehavior.md) — Defines the behavior for the child elements of the new parent element.
