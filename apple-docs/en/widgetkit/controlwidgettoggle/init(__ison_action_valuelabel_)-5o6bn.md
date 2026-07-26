---
title: 'init(_:isOn:action:valueLabel:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/controlwidgettoggle/init(_:ison:action:valuelabel:)-5o6bn'
source_url: 'https://developer.apple.com/documentation/widgetkit/controlwidgettoggle/init(_:ison:action:valuelabel:)-5o6bn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/controlwidgettoggle/init%28_%3Aison%3Aaction%3Avaluelabel%3A%29-5o6bn.json'
content_hash: 'sha256:4951a2fe1b8686ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [ControlWidgetToggle](../controlwidgettoggle.md)

# init(_:isOn:action:valueLabel:)

<sub>Initializer</sub>

Creates a toggle template for a control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(_ titleKey: LocalizedStringKey, isOn: Bool, action: Action, @ViewBuilder valueLabel: @escaping (Bool) -> ValueLabel) where Action : SetValueIntent, Action.ValueType == Bool
```

## Parameters

- `titleKey` — The key to a localized string to display as the title of the toggle.

- `isOn` — A boolean value that describes the current value of the toggle.

- `action` — The action the toggle performs when pressed.

- `valueLabel` — A view that renders the toggle’s value. The boolean parameter represents the value.

## See Also

### Initializers

- [init(isOn:action:label:)](<init(ison_action_label_).md>) — Creates a toggle template for a control.
- [init(isOn:action:label:valueLabel:)](<init(ison_action_label_valuelabel_).md>) — Creates a toggle template for a control.
- [init(_:isOn:action:valueLabel:)](<init(__ison_action_valuelabel_)-33wfq.md>) — Creates a toggle template for a control.
- [init(_:isOn:action:valueLabel:)](<init(__ison_action_valuelabel_)-4lk32.md>) — Creates a toggle template for a control.
