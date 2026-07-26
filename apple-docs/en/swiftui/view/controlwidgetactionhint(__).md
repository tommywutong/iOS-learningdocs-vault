---
title: 'controlWidgetActionHint(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/controlwidgetactionhint(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/controlwidgetactionhint(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/controlwidgetactionhint%28_%3A%29.json'
content_hash: 'sha256:52775597f6dca81d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# controlWidgetActionHint(_:)

<sub>Instance Method</sub>

The action hint of the control described by the modified label.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@MainActor @preconcurrency func controlWidgetActionHint(_ hint: LocalizedStringResource) -> some View

```

## Parameters

- `hint` — The localized string resource to display.

## Discussion

This text will appear next to the Action Button to describe what your control will do when activated. By default, a control’s action hint is derived from its display name, the type of control, and value text, if any:

// Action Hint: “Hold for ‘Ping My Watch’” struct PingMyWatchButton: Control { static let displayName: LocalizedStringResource = “Ping My Watch” … }

// When this button’s action conforms to `OpenIntent`: // Action Hint: “Hold to Open Notes” struct NotesLauncher: Control { static let displayName: LocalizedStringResource = “Notes” … }

// Action Hint: “Hold to Turn On ‘Silent Mode’” / “Hold to Turn Off ‘Silent Mode’” struct SilentModeToggle: Control { static let displayName: LocalizedStringResource = “Silent Mode” … }

// Action Hint: “Hold for Silent” / “Hold for Ring” ControlWidgetToggle(…) { isOn in Label( isOn ? “Silent” : “Ring”, systemImage: isOn ? “bell.slash” : “bell” ) }

When the default action hint is insufficiently descriptive, you can customize the hint by applying this modifier to the control’s label. For instance, we can describe what the user will use our `NotesLauncher` control to do, “Compose a Note”, instead of the default “Hold to Open Notes” hint, like this:

ControlWidgetButton(…) { Image(systemName: “note.text”) .controlWidgetActionHint(“Compose a Note”) }

## See Also

### Composing control widgets

- [ControlWidget](../controlwidget.md) — The configuration and content of a control widget to display in system spaces such as Control Center, the Lock Screen, and the Action Button.
- [ControlWidgetConfiguration](../controlwidgetconfiguration.md) — A type that describes a control widget’s content.
- [EmptyControlWidgetConfiguration](../emptycontrolwidgetconfiguration.md) — An empty control widget configuration.
- [ControlWidgetConfigurationBuilder](../controlwidgetconfigurationbuilder.md) — A custom attribute that constructs a control widget’s body.
- [ControlWidgetTemplate](../controlwidgettemplate.md) — A type that describes a control widget’s content.
- [EmptyControlWidgetTemplate](../emptycontrolwidgettemplate.md) — An empty control widget template.
- [ControlWidgetTemplateBuilder](../controlwidgettemplatebuilder.md) — A custom attribute that constructs a control widget template’s body.
- [controlWidgetStatus(_:)](<controlwidgetstatus(__).md>) — The status of the control described by the modified label.
