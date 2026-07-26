---
title: 'init(isOn:action:label:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/controlwidgettoggle/init(ison:action:label:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/controlwidgettoggle/init(ison:action:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/controlwidgettoggle/init%28ison%3Aaction%3Alabel%3A%29.json'
content_hash: 'sha256:62a759371a54388a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [ControlWidgetToggle](../controlwidgettoggle.md)

# init(isOn:action:label:)

<sub>Initializer</sub>

Creates a toggle template for a control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(isOn: Bool, action: Action, @ViewBuilder label: @escaping () -> Label) where ValueLabel == ControlWidgetToggleDefaultLabel, Action : SetValueIntent, Action.ValueType == Bool
```

## Parameters

- `isOn` — A boolean value that describes the current value of the toggle.

- `action` — The action the toggle performs when pressed.

- `label` — A view that renders the toggle’s label.

## Discussion

The toggle will use “On” and “Off” as default value label.

## See Also

### Initializers

- [init(isOn:action:label:valueLabel:)](<init(ison_action_label_valuelabel_).md>) — Creates a toggle template for a control.
- [init(_:isOn:action:valueLabel:)](<init(__ison_action_valuelabel_)-33wfq.md>) — Creates a toggle template for a control.
- [init(_:isOn:action:valueLabel:)](<init(__ison_action_valuelabel_)-5o6bn.md>) — Creates a toggle template for a control.
- [init(_:isOn:action:valueLabel:)](<init(__ison_action_valuelabel_)-4lk32.md>) — Creates a toggle template for a control.
