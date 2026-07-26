---
title: ToggleStyleConfiguration
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/togglestyleconfiguration
source_url: 'https://developer.apple.com/documentation/swiftui/togglestyleconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/togglestyleconfiguration.json'
content_hash: 'sha256:fe27406df59b83a8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ToggleStyleConfiguration

<sub>Structure</sub>

The properties of a toggle instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ToggleStyleConfiguration
```

## Overview

When you define a custom toggle style by creating a type that conforms to the [ToggleStyle](togglestyle.md) protocol, you implement the [makeBody(configuration:)](<togglestyle/makebody(configuration_).md>) method. That method takes a `ToggleStyleConfiguration` input that has the information you need to define the behavior and appearance of a [Toggle](toggle.md).

The configuration structure’s [label](togglestyleconfiguration/label-swift.property.md) reflects the toggle’s content, which might be the value that you supply to the `label` parameter of the [init(isOn:label:)](<toggle/init(ison_label_).md>) initializer. Alternatively, it could be another view that SwiftUI builds from an initializer that takes a string input, like [init(_:isOn:)](<toggle/init(__ison_).md>). In either case, incorporate the label into the toggle’s view to help the user understand what the toggle does. For example, the built-in [switch](togglestyle/switch.md) style horizontally stacks the label with the control element.

The structure’s [isOn](togglestyleconfiguration/ison.md) property provides a [Binding](binding.md) to the state of the toggle. Adjust the appearance of the toggle based on this value. For example, the built-in [button](togglestyle/button.md) style fills the button’s background when the property is `true`, but leaves the background empty when the property is `false`. Change the value when the user performs an action that’s meant to change the toggle, like the button does when tapped or clicked by the user.

## Topics

### Getting the label view

- [label](togglestyleconfiguration/label-swift.property.md) — A view that describes the effect of switching the toggle between states.
- [Label](togglestyleconfiguration/label-swift.struct.md) — A type-erased label of a toggle.

### Managing the toggle state

- [isMixed](togglestyleconfiguration/ismixed.md) — Whether the [Toggle](toggle.md) is currently in a mixed state.
- [isOn](togglestyleconfiguration/ison.md) — A binding to a state property that indicates whether the toggle is on.
- [$isOn](togglestyleconfiguration/$ison.md)

## See Also

### Styling toggles

- [toggleStyle(_:)](<view/togglestyle(__).md>) — Sets the style for toggles in a view hierarchy.
- [ToggleStyle](togglestyle.md) — The appearance and behavior of a toggle.
