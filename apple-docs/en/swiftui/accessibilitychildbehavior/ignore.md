---
title: ignore
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessibilitychildbehavior/ignore
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilitychildbehavior/ignore'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilitychildbehavior/ignore.json'
content_hash: 'sha256:b61dcf341ff53a7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AccessibilityChildBehavior](../accessibilitychildbehavior.md)

# ignore

<sub>Type Property</sub>

Any child accessibility elements become hidden.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let ignore: AccessibilityChildBehavior
```

## Discussion

Use this behavior when you want a view represented by a single accessibility element. The new accessibility element has no initial properties. So you will need to use other accessibility modifiers, such as [accessibilityLabel(_:)](<../view/accessibilitylabel(__).md>), to begin making it accessible.

```swift
var body: some View {
    VStack {
        Button("Previous Page", action: goBack)
        Text("\(pageNumber)")
        Button("Next Page", action: goForward)
    }
    .accessibilityElement(children: .ignore)
    .accessibilityValue("Page \(pageNumber) of \(pages.count)")
    .accessibilityAdjustableAction { action in
        if action == .increment {
            goForward()
        } else {
            goBack()
        }
    }
}
```

Before using the  [ignore](ignore.md)behavior, consider using the [combine](combine.md) behavior.

> [!note] Note
> A new accessibility element is always created.

## See Also

### Getting behaviors

- [combine](combine.md) — Any child accessibility element’s properties are merged into the new accessibility element.
- [contain](contain.md) — Any child accessibility elements become children of the new accessibility element.
