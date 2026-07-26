---
title: 'menuActionDismissBehavior(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/menuactiondismissbehavior(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/menuactiondismissbehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/menuactiondismissbehavior%28_%3A%29.json'
content_hash: 'sha256:60d7ed46574c0a25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# menuActionDismissBehavior(_:)

<sub>Instance Method</sub>

Tells a menu whether to dismiss after performing an action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func menuActionDismissBehavior(_ behavior: MenuActionDismissBehavior) -> some View

```

## Parameters

- `behavior` — The menu action dismissal behavior to apply.

## Return Value

A view that has the specified menu dismissal behavior.

## Discussion

Use this modifier to control the dismissal behavior of a menu. In the example below, the menu doesn’t dismiss after someone chooses either the increase or decrease action:

```swift
Menu("Font size") {
    Button(action: increase) {
        Label("Increase", systemImage: "plus.magnifyingglass")
    }
    .menuActionDismissBehavior(.disabled)

    Button("Reset", action: reset)

    Button(action: decrease) {
        Label("Decrease", systemImage: "minus.magnifyingglass")
    }
    .menuActionDismissBehavior(.disabled)
}
```

You can use this modifier on any controls that present a menu, like a [Picker](../picker.md) that uses the [menu](../pickerstyle/menu.md) style or a [ControlGroup](../controlgroup.md). For example, the code below creates a picker that disables dismissal when someone selects one of the options:

```swift
Picker("Flavor", selection: $selectedFlavor) {
    ForEach(Flavor.allCases) { flavor in
        Text(flavor.rawValue.capitalized)
            .tag(flavor)
    }
}
.pickerStyle(.menu)
.menuActionDismissBehavior(.disabled)
```

You can also use this modifier on context menus. The example below creates a context menu that stays presented after someone selects an action to run:

```swift
Text("Favorite Card Suit")
    .padding()
    .contextMenu {
        Button("♥️ - Hearts", action: increaseHeartsCount)
        Button("♣️ - Clubs", action: increaseClubsCount)
        Button("♠️ - Spades", action: increaseSpadesCount)
        Button("♦️ - Diamonds", action: increaseDiamondsCount)
    }
    .menuActionDismissBehavior(.disabled)
```

## See Also

### Configuring menu dismissal

- [MenuActionDismissBehavior](../menuactiondismissbehavior.md) — The set of menu dismissal behavior options.
