---
title: keyboard
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbaritemplacement/keyboard
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritemplacement/keyboard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritemplacement/keyboard.json'
content_hash: 'sha256:957232bae53fe90b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarItemPlacement](../toolbaritemplacement.md)

# keyboard

<sub>Type Property</sub>

A placement for items in the keyboard section.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
static let keyboard: ToolbarItemPlacement
```

## Discussion

On iOS, keyboard items are above the software keyboard when present, or at the bottom of the screen when a hardware keyboard is attached.

On macOS, keyboard items will be placed inside the Touch Bar.

A `FocusedValue` can be used to adjust the content of the keyboard bar based on the currently focused view. In the example below, the keyboard bar gains additional buttons only when the appropriate `TextField` is focused.

```swift
enum Field {
    case suit
    case rank
}

struct KeyboardBarDemo : View {
    @FocusedValue(\.field) var field: Field?

    var body: some View {
        HStack {
            TextField("Suit", text: $suitText)
                .focusedValue(\.field, .suit)
            TextField("Rank", text: $rankText)
                .focusedValue(\.field, .rank)
        }
        .toolbar {
            ToolbarItemGroup(placement: .keyboard) {
                if field == .suit {
                    Button("♣️", action: {})
                    Button("♥️", action: {})
                    Button("♠️", action: {})
                    Button("♦️", action: {})
                }
                DoneButton()
            }
        }
    }
}
```

## See Also

### Getting explicit placement

- [topBarLeading](topbarleading.md) — A placement for items in the leading edge of the top bar.
- [topBarTrailing](topbartrailing.md) — A placement for items in the trailing edge of the top bar.
- [topBarPinnedTrailing](topbarpinnedtrailing.md) — A placement that pins the item to the trailing edge of the toolbar. _(beta)_
- [bottomBar](bottombar.md) — A placement for items in the bottom toolbar.
- [bottomOrnament](bottomornament.md) — A placement for items in an ornament under the window.
- [accessoryBar(id:)](<accessorybar(id_).md>) — Creates a unique accessory bar placement.
