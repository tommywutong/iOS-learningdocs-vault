---
title: 'controlWidgetStatus(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/controlwidgetstatus(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/controlwidgetstatus(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/controlwidgetstatus%28_%3A%29.json'
content_hash: 'sha256:373b45df9f3955e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# controlWidgetStatus(_:)

<sub>Instance Method</sub>

The status of the control described by the modified label.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@MainActor @preconcurrency func controlWidgetStatus(_ status: LocalizedStringResource) -> some View

```

## Parameters

- `status` — The localized string resource to display.

## Discussion

This text appears in Control Center when your control’s state changes. You can customize the text by applying this modifier to the control’s value label:

```swift
// Status Text: "Do Not Disturb Until This Evening" / "Do Not Disturb Disabled"
ControlWidgetToggle("Do Not Disturb", ...) { isOn in
    Image(systemName: "moon")
        .controlWidgetStatus(isOn ? "Do Not Disturb Until This Evening" : "Do Not Disturb Disabled")
}
```

## See Also

### Composing control widgets

- [ControlWidget](../controlwidget.md) — The configuration and content of a control widget to display in system spaces such as Control Center, the Lock Screen, and the Action Button.
- [ControlWidgetConfiguration](../controlwidgetconfiguration.md) — A type that describes a control widget’s content.
- [EmptyControlWidgetConfiguration](../emptycontrolwidgetconfiguration.md) — An empty control widget configuration.
- [ControlWidgetConfigurationBuilder](../controlwidgetconfigurationbuilder.md) — A custom attribute that constructs a control widget’s body.
- [ControlWidgetTemplate](../controlwidgettemplate.md) — A type that describes a control widget’s content.
- [EmptyControlWidgetTemplate](../emptycontrolwidgettemplate.md) — An empty control widget template.
- [ControlWidgetTemplateBuilder](../controlwidgettemplatebuilder.md) — A custom attribute that constructs a control widget template’s body.
- [controlWidgetActionHint(_:)](<controlwidgetactionhint(__).md>) — The action hint of the control described by the modified label.
