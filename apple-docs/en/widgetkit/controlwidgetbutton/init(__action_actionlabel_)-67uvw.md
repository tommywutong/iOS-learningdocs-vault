---
title: 'init(_:action:actionLabel:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/controlwidgetbutton/init(_:action:actionlabel:)-67uvw'
source_url: 'https://developer.apple.com/documentation/widgetkit/controlwidgetbutton/init(_:action:actionlabel:)-67uvw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/controlwidgetbutton/init%28_%3Aaction%3Aactionlabel%3A%29-67uvw.json'
content_hash: 'sha256:814748a7d9010ddd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [ControlWidgetButton](../controlwidgetbutton.md)

# init(_:action:actionLabel:)

<sub>Initializer</sub>

Creates a button template for a control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(_ titleKey: LocalizedStringKey, action: Action, @ViewBuilder actionLabel: @escaping (Bool) -> ActionLabel) where Action : AppIntent
```

## Parameters

- `titleKey` — The key to a localized string to display as the title of the button.

- `action` — The action your button performs when pressed.

- `actionLabel` — A view that is rendered when the button’s action is performed.

## Discussion

Use the action label to additionally customize the appearance of this control button while its action is performed

```swift
ControlWidgetButton(
    "Open Trunk",
    action: OpenTrunkIntent()
) { isActive in
    Image(systemName: "car.side.rear.open.crop")
    if isActive {
        Text("Opening...")
    }
}
```

The example above produces a control button that appears in Control Center with “Open Trunk” as its title and the provided SF symbol. While the control is performing its action, it shows the “Opening…” subtitle.

## See Also

### Initializers

- [init(action:label:)](<init(action_label_)-77p8j.md>) — Creates a button template for a control.
- [init(action:label:)](<init(action_label_)-8oxxp.md>) — Creates a button template for a control that launches an app.
- [init(action:label:actionLabel:)](<init(action_label_actionlabel_).md>) — Creates a button template for a control.
- [init(action:label:actionLabel:)](<init(action_label_actionlabel_).md>) — Creates a button template for a control.
- [init(_:action:actionLabel:)](<init(__action_actionlabel_)-4sgji.md>) — Creates a button template for a control.
