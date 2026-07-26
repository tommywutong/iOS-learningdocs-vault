---
title: 'pasteDestination(for:action:validator:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 13.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/pastedestination(for:action:validator:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/pastedestination(for:action:validator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/pastedestination%28for%3Aaction%3Avalidator%3A%29.json'
content_hash: 'sha256:6e7ffbd3a9186c1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# pasteDestination(for:action:validator:)

<sub>Instance Method</sub>

Specifies an action that adds validated items to a view in response to the system’s Paste command.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
nonisolated func pasteDestination<T>(for payloadType: T.Type = T.self, action: @escaping ([T]) -> Void, validator: @escaping ([T]) -> [T] = { $0 }) -> some View where T : Transferable

```

## Parameters

- `payloadType` — The type of data that the paste destination accepts. The type must conform to the [Transferable](../../coretransferable/transferable.md) protocol.

- `action` — The action to perform when someone uses the system’s Paste command to paste one or more items of the payload type. The closure takes one parameter, which is the array of items to paste.

- `validator` — A closure that you implement to validate the data to paste. SwiftUI calls this before it calls the `action` closure, and passes in an array of items to validate. Inspect the items, and return an array that includes only those from the input array that you consider valid. The array that you return from this closure becomes the input to the `action` closure. If you return an empty array, SwiftUI doesn’t call the `action` closure.

## Return Value

A view that people can paste into using the system Paste command.

## Discussion

Use this modifier to paste one or more items into a view from the Clipboard when someone issues a Paste command. People issue a Paste command by choosing Edit \> Paste from the app’s menu, or by using the Command-V keyboard shortcut. The system enables the Paste command for your app when the view in focus provides a paste destination.

For example, the following code enables people to paste bird names into a list:

```swift
struct PasteDestinationExample: View {
    @State private var birds: [String] = []
    @State private var selection: Set<String> = []

    let knownBirds = ["owl", "parrot", "swift",
                      "sparrow", "robin", "bluebird"]

    var body: some View {
        List(birds, id: \.self, selection: $selection) {
            Text($0)
        }
        .pasteDestination(for: String.self) { values in
            birds.append(contentsOf: values)
        } validator: { values in
            values.filter { knownBirds.contains($0) }
        }
    }
}
```

The paste destination handles only pasted content with a type that matches the `payloadType` that you specify. The list in the above example only accepts strings.

Use the `validator` closure to restrict the pasted content to items that make sense in the context of the view. The above example allows people to paste only strings that match one of a known list of bird names because the list is meant to contain only birds. You can omit the final closure if you don’t need to perform any validation.

> [!note] Note
> To enable people to paste using a custom action — like from a context menu item — rather than using the system Paste command, access the Clipboard directly using an [NSPasteboard](../../appkit/nspasteboard.md) or a [UIPasteboard](../../uikit/uipasteboard.md) instance.

## See Also

### Copying transferable items

- [copyable(_:)](<copyable(__).md>) — Specifies a list of items to copy in response to the system’s Copy command.
- [cuttable(for:action:)](<cuttable(for_action_).md>) — Specifies an action that moves items to the Clipboard in response to the system’s Cut command.
