---
title: ToggleStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/togglestyle
source_url: 'https://developer.apple.com/documentation/swiftui/togglestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/togglestyle.json'
content_hash: 'sha256:b6977c959b9f004c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ToggleStyle

<sub>Protocol</sub>

The appearance and behavior of a toggle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency protocol ToggleStyle
```

## Overview

To configure the style for a single [Toggle](toggle.md) or for all toggle instances in a view hierarchy, use the [toggleStyle(_:)](<view/togglestyle(__).md>) modifier. You can specify one of the built-in toggle styles, like [switch](togglestyle/switch.md) or [button](togglestyle/button.md):

```swift
Toggle(isOn: $isFlagged) {
    Label("Flag", systemImage: "flag.fill")
}
.toggleStyle(.button)
```

Alternatively, you can create and apply a custom style.

### Custom styles

To create a custom style, declare a type that conforms to the `ToggleStyle` protocol and implement the required [makeBody(configuration:)](<togglestyle/makebody(configuration_).md>) method. For example, you can define a checklist toggle style:

```swift
struct ChecklistToggleStyle: ToggleStyle {
    func makeBody(configuration: Configuration) -> some View {
        // Return a view that has checklist appearance and behavior.
    }
}
```

Inside the method, use the `configuration` parameter, which is an instance of the [ToggleStyleConfiguration](togglestyleconfiguration.md) structure, to get the label and a binding to the toggle state. To see examples of how to use these items to construct a view that has the appearance and behavior of a toggle, see [makeBody(configuration:)](<togglestyle/makebody(configuration_).md>).

To provide easy access to the new style, declare a corresponding static variable in an extension to `ToggleStyle`:

```swift
extension ToggleStyle where Self == ChecklistToggleStyle {
    static var checklist: ChecklistToggleStyle { .init() }
}
```

You can then use your custom style:

```swift
Toggle(activity.name, isOn: $activity.isComplete)
    .toggleStyle(.checklist)
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

- **Conforming Types**: [ButtonToggleStyle](buttontogglestyle.md), [CheckboxToggleStyle](checkboxtogglestyle.md), [DefaultToggleStyle](defaulttogglestyle.md), [SwitchToggleStyle](switchtogglestyle.md)

## Topics

### Getting built-in toggle styles

- [automatic](togglestyle/automatic.md) — The default toggle style.
- [button](togglestyle/button.md) — A toggle style that displays as a button with its label as the title.
- [checkbox](togglestyle/checkbox.md) — A toggle style that displays a checkbox followed by its label.
- [switch](togglestyle/switch.md) — A toggle style that displays a leading label and a trailing switch.

### Creating custom toggle styles

- [makeBody(configuration:)](<togglestyle/makebody(configuration_).md>) — Creates a view that represents the body of a toggle.
- [ToggleStyleConfiguration](togglestyleconfiguration.md) — The properties of a toggle instance.
- [Configuration](togglestyle/configuration.md) — The properties of a toggle instance.
- [Body](togglestyle/body.md) — A view that represents the appearance and interaction of a toggle.

### Supporting types

- [DefaultToggleStyle](defaulttogglestyle.md) — The default toggle style.
- [ButtonToggleStyle](buttontogglestyle.md) — A toggle style that displays as a button with its label as the title.
- [CheckboxToggleStyle](checkboxtogglestyle.md) — A toggle style that displays a checkbox followed by its label.
- [SwitchToggleStyle](switchtogglestyle.md) — A toggle style that displays a leading label and a trailing switch.

## See Also

### Styling toggles

- [toggleStyle(_:)](<view/togglestyle(__).md>) — Sets the style for toggles in a view hierarchy.
- [ToggleStyleConfiguration](togglestyleconfiguration.md) — The properties of a toggle instance.
