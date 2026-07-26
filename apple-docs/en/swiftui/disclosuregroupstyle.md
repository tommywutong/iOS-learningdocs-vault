---
title: DisclosureGroupStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/disclosuregroupstyle
source_url: 'https://developer.apple.com/documentation/swiftui/disclosuregroupstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/disclosuregroupstyle.json'
content_hash: 'sha256:9608b2fde92fc314'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DisclosureGroupStyle

<sub>Protocol</sub>

A type that specifies the appearance and interaction of disclosure groups within a view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency protocol DisclosureGroupStyle
```

## Overview

To configure the disclosure group style for a view hierarchy, use the [disclosureGroupStyle(_:)](<view/disclosuregroupstyle(__).md>) modifier.

To create a custom disclosure group style, declare a type that conforms to `DisclosureGroupStyle`. Implement the [makeBody(configuration:)](<disclosuregroupstyle/makebody(configuration_).md>) method to return a view that composes the elements of the `configuration` that SwiftUI provides to your method.

```swift
struct MyDisclosureStyle: DisclosureGroupStyle {
    func makeBody(configuration: Configuration) -> some View {
        VStack {
            Button {
                withAnimation {
                    configuration.isExpanded.toggle()
                }
            } label: {
                HStack(alignment: .firstTextBaseline) {
                    configuration.label
                    Spacer()
                    Text(configuration.isExpanded ? "hide" : "show")
                        .foregroundColor(.accentColor)
                        .font(.caption.lowercaseSmallCaps())
                        .animation(nil, value: configuration.isExpanded)
                }
                .contentShape(Rectangle())
            }
            .buttonStyle(.plain)
            if configuration.isExpanded {
                configuration.content
            }
        }
    }
}
```

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Relationships

- **Conforming Types**: [AutomaticDisclosureGroupStyle](automaticdisclosuregroupstyle.md)

## Topics

### Getting the styles

- [automatic](disclosuregroupstyle/automatic.md) — A disclosure group style that resolves its appearance automatically based on the current context.

### Creating custom disclosure group styles

- [makeBody(configuration:)](<disclosuregroupstyle/makebody(configuration_).md>) — Creates a view that represents the body of a disclosure group.
- [DisclosureGroupStyleConfiguration](disclosuregroupstyleconfiguration.md) — The properties of a disclosure group instance.
- [Configuration](disclosuregroupstyle/configuration.md) — The properties of a disclosure group instance.
- [Body](disclosuregroupstyle/body.md) — A view that represents the body of a disclosure group.

### Supporting types

- [AutomaticDisclosureGroupStyle](automaticdisclosuregroupstyle.md) — A disclosure group style that resolves its appearance automatically based on the current context.

## See Also

### Styling collection views

- [listStyle(_:)](<view/liststyle(__).md>) — Sets the style for lists within this view.
- [ListStyle](liststyle.md) — A protocol that describes the behavior and appearance of a list.
- [tableStyle(_:)](<view/tablestyle(__).md>) — Sets the style for tables within this view.
- [TableStyle](tablestyle.md) — A type that applies a custom appearance to all tables within a view.
- [TableStyleConfiguration](tablestyleconfiguration.md) — The properties of a table.
- [disclosureGroupStyle(_:)](<view/disclosuregroupstyle(__).md>) — Sets the style for disclosure groups within this view.
