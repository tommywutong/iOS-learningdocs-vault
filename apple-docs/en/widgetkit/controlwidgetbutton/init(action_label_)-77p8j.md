---
title: 'init(action:label:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/controlwidgetbutton/init(action:label:)-77p8j'
source_url: 'https://developer.apple.com/documentation/widgetkit/controlwidgetbutton/init(action:label:)-77p8j'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/controlwidgetbutton/init%28action%3Alabel%3A%29-77p8j.json'
content_hash: 'sha256:db412db70a6e109d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [ControlWidgetButton](../controlwidgetbutton.md)

# init(action:label:)

<sub>Initializer</sub>

Creates a button template for a control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(action: Action, @ViewBuilder label: @escaping () -> Label) where ActionLabel == ControlWidgetButtonDefaultActionLabel, Action : AppIntent
```

## Parameters

- `action` — The action your button performs when pressed.

- `label` — A view that renders the button.

## See Also

### Initializers

- [init(action:label:)](<init(action_label_)-8oxxp.md>) — Creates a button template for a control that launches an app.
- [init(action:label:actionLabel:)](<init(action_label_actionlabel_).md>) — Creates a button template for a control.
- [init(action:label:actionLabel:)](<init(action_label_actionlabel_).md>) — Creates a button template for a control.
- [init(_:action:actionLabel:)](<init(__action_actionlabel_)-4sgji.md>) — Creates a button template for a control.
- [init(_:action:actionLabel:)](<init(__action_actionlabel_)-67uvw.md>) — Creates a button template for a control.
