---
title: 'cuttable(for:action:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 13.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/cuttable(for:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/cuttable(for:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/cuttable%28for%3Aaction%3A%29.json'
content_hash: 'sha256:3e0410ad30285e2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# cuttable(for:action:)

<sub>Instance Method</sub>

Specifies an action that moves items to the Clipboard in response to the system’s Cut command.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
nonisolated func cuttable<T>(for payloadType: T.Type = T.self, action: @escaping () -> [T]) -> some View where T : Transferable

```

## Parameters

- `payloadType` — The type of items to cut.

- `action` — A closure that you implement to delete the selected items from the collection, and return them for addition to the Clipboard. The items must conform to the [Transferable](../../coretransferable/transferable.md) protocol.

## Return Value

A view that sends one or more items to the Clipboard in response to a Cut command.

## Discussion

Use this modifier to remove one or more items from a collection of items and then move the items to the Clipboard when someone issues a Cut command. People issue a Cut command by choosing Edit \> Cut from the app’s menu, or by using the Command-X keyboard shortcut. The system enables the Cut command for your app when it detects cuttable content.

For example, the following code enables people to remove bird names from a list of birds:

```swift
struct CuttableExample: View {
    @State private var birds = ["owl", "parrot", "swift"]
    @State private var selection: Set<String> = []

    var body: some View {
        List(birds, id: \.self, selection: $selection) {
            Text($0)
        }
        .cuttable(for: String.self) {
            for bird in selection {
                birds.removeAll(where: { $0 == bird })
            }
            return Array(selection)
        }
    }
}
```

When someone selects “owl” and issues a Cut command, the `action` closure removes the selected item from the list and returns it. In response, SwiftUI moves it to the Clipboard. If you want to copy the item without removing it, use the [copyable(_:)](<copyable(__).md>) modifier instead.

> [!note] Note
> To enable people to cut using a custom action — like from a context menu item — rather than using the system Cut command, update the Clipboard directly using an [NSPasteboard](../../appkit/nspasteboard.md) or a [UIPasteboard](../../uikit/uipasteboard.md) instance.

## See Also

### Copying transferable items

- [copyable(_:)](<copyable(__).md>) — Specifies a list of items to copy in response to the system’s Copy command.
- [pasteDestination(for:action:validator:)](<pastedestination(for_action_validator_).md>) — Specifies an action that adds validated items to a view in response to the system’s Paste command.
