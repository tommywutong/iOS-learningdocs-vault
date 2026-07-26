---
title: 'textSelection(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/textselection(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/textselection(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/textselection%28_%3A%29.json'
content_hash: 'sha256:3ec8e5732a8744d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# textSelection(_:)

<sub>Instance Method</sub>

Controls whether people can select text within this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func textSelection<S>(_ selectability: S) -> some View where S : TextSelectability

```

## Discussion

People sometimes need to copy useful information from [Text](../text.md) views — including error messages, serial numbers, or IP addresses — so they can then paste the text into another context. Enable text selection to let people select text in a platform-appropriate way.

You can apply this method to an individual text view, or to a container to make each contained text view selectable. In the following example, the person using the app can select text that shows the date of an event or the name or email of any of the event participants:

```swift
var body: some View {
    VStack {
        Text("Event Invite")
            .font(.title)
        Text(invite.date.formatted(date: .long, time: .shortened))
            .textSelection(.enabled)

        List(invite.recipients) { recipient in
            VStack (alignment: .leading) {
                Text(recipient.name)
                Text(recipient.email)
                    .foregroundStyle(.secondary)
            }
        }
        .textSelection(.enabled)
    }
    .navigationTitle("New Invitation")
}
```

On macOS, people use the mouse or trackpad to select a range of text, which they can quickly copy by choosing Edit \> Copy, or with the standard keyboard shortcut.

![A macOS window titled New Invitation, with header Event Invite and](../../../../attachments/b0a31c41cedda6a8e3d773bf2eb5d53c/View-textSelection-1@2x.png)

On iOS, the person using the app touches and holds on a selectable `Text` view to begin selecting text. In iOS 27 or later, this brings up the system text selection handles and highlight which supports selecting a range of text. In iOS 26 or earlier, this brings up a system menu with menu items appropriate for the current context. These menu items operate on the entire contents of the `Text` view.

![A portion of an iOS view, with header Event Invite and the date](../../../../attachments/a45efabe4bfbfa27b3f63847fbecbacc/View-textSelection-2@2x.png)

> [!note] Note
> [Button](../button.md) views don’t support text selection.

## See Also

### Selecting text

- [TextSelectability](../textselectability.md) — A type that describes the ability to select text.
- [TextSelection](../textselection.md) — Represents a selection of text.
- [textSelectionAffinity(_:)](<textselectionaffinity(__).md>) — Sets the direction of a selection or cursor relative to a text character.
- [textSelectionAffinity](../environmentvalues/textselectionaffinity.md) — A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
- [TextSelectionAffinity](../textselectionaffinity.md) — A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
- [AttributedTextSelection](../attributedtextselection.md) — Represents a selection of attributed text.
