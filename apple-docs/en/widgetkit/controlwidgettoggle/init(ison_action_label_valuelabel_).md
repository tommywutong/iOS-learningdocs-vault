---
title: 'init(isOn:action:label:valueLabel:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/controlwidgettoggle/init(ison:action:label:valuelabel:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/controlwidgettoggle/init(ison:action:label:valuelabel:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/controlwidgettoggle/init%28ison%3Aaction%3Alabel%3Avaluelabel%3A%29.json'
content_hash: 'sha256:b1689ebe06cd44e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [ControlWidgetToggle](../controlwidgettoggle.md)

# init(isOn:action:label:valueLabel:)

<sub>Initializer</sub>

Creates a toggle template for a control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(isOn: Bool, action: Action, @ViewBuilder label: @escaping () -> Label, @ViewBuilder valueLabel: @escaping (Bool) -> ValueLabel) where Action : SetValueIntent, Action.ValueType == Bool
```

## Parameters

- `isOn` — A boolean value that describes the current value of the toggle.

- `action` — The action the toggle performs when pressed.

- `label` — A view that renders the toggle’s label.

- `valueLabel` — A view that renders the toggle’s value. The boolean parameter represents the value.

## See Also

### Initializers

- [init(isOn:action:label:)](<init(ison_action_label_).md>) — Creates a toggle template for a control.
- [init(_:isOn:action:valueLabel:)](<init(__ison_action_valuelabel_)-33wfq.md>) — Creates a toggle template for a control.
- [init(_:isOn:action:valueLabel:)](<init(__ison_action_valuelabel_)-5o6bn.md>) — Creates a toggle template for a control.
- [init(_:isOn:action:valueLabel:)](<init(__ison_action_valuelabel_)-4lk32.md>) — Creates a toggle template for a control.
