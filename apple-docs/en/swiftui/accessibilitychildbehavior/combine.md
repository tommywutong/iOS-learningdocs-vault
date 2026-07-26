---
title: combine
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessibilitychildbehavior/combine
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilitychildbehavior/combine'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilitychildbehavior/combine.json'
content_hash: 'sha256:52f101fe86f92873'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AccessibilityChildBehavior](../accessibilitychildbehavior.md)

# combine

<sub>Type Property</sub>

Any child accessibility element’s properties are merged into the new accessibility element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let combine: AccessibilityChildBehavior
```

## Discussion

Use this behavior when you want a view represented by a single accessibility element. The new accessibility element merges properties from all non-hidden children. Some properties may be transformed or ignored to achieve the ideal combined result. For example, not all of [AccessibilityTraits](../accessibilitytraits.md) are merged and a [default](../accessibilityactionkind/default.md) action may become a named action ([init(named:)](<../accessibilityactionkind/init(named_).md>)).

```swift
struct UserCell: View {
    var user: User

    var body: some View {
        VStack {
            Image(user.image)
            Text(user.name)
            Button("Options", action: showOptions)
        }
        .accessibilityElement(children: .combine)
    }
}
```

A new accessibility element is created when:

- The view contains multiple or zero accessibility elements.
- The view wraps a [UIViewRepresentable](../uiviewrepresentable.md)/[NSViewRepresentable](../nsviewrepresentable.md).

> [!note] Note
> If an accessibility element is not created, the [AccessibilityChildBehavior](../accessibilitychildbehavior.md) of the existing accessibility element is modified.

## See Also

### Getting behaviors

- [contain](contain.md) — Any child accessibility elements become children of the new accessibility element.
- [ignore](ignore.md) — Any child accessibility elements become hidden.
