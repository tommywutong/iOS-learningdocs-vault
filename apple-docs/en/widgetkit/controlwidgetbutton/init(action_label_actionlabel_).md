---
title: 'init(action:label:actionLabel:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/controlwidgetbutton/init(action:label:actionlabel:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/controlwidgetbutton/init(action:label:actionlabel:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/controlwidgetbutton/init%28action%3Alabel%3Aactionlabel%3A%29.json'
content_hash: 'sha256:bc714ebc34eac5a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [ControlWidgetButton](../controlwidgetbutton.md)

# init(action:label:actionLabel:)

<sub>Initializer</sub>

Creates a button template for a control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(action: Action, @ViewBuilder label: @escaping () -> Label, @ViewBuilder actionLabel: @escaping (Bool) -> ActionLabel) where Action : AppIntent
```

## Parameters

- `action` — The action your button performs when pressed.

- `label` — A view that renders the button.

- `actionLabel` — A view that is rendered when the button’s action is performed

## Discussion

Use the action label to additionally customize the appearance of this control button while its action is performed

```swift
ControlWidgetButton(action: OpenTrunkIntent()) {
    Label("Open Trunk", systemImage: "car.side.rear.open.crop")
} actionLabel: { isActive in
    if isActive {
        Text("Opening…")
    }
}
```

The example above produces a control button that appears in Control Center with “Open Trunk” as its title and the provided SF symbol. While the control is performing its action, it shows the “Opening…” subtitle.

## See Also

### Initializers

- [init(action:label:)](<init(action_label_)-77p8j.md>) — Creates a button template for a control.
- [init(action:label:)](<init(action_label_)-8oxxp.md>) — Creates a button template for a control that launches an app.
- [init(_:action:actionLabel:)](<init(__action_actionlabel_)-4sgji.md>) — Creates a button template for a control.
- [init(_:action:actionLabel:)](<init(__action_actionlabel_)-67uvw.md>) — Creates a button template for a control.
