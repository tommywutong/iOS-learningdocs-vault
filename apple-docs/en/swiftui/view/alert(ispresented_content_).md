---
title: 'alert(isPresented:content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/alert(ispresented:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/alert(ispresented:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/alert%28ispresented%3Acontent%3A%29.json'
content_hash: 'sha256:5690427ddee850e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# alert(isPresented:content:)

<sub>Instance Method</sub>

Presents an alert to the user.

> [!warning] Deprecated
> Use [alert(_:isPresented:actions:message:)](<alert(__ispresented_actions_message_)-6awwp.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func alert(isPresented: Binding<Bool>, content: () -> Alert) -> some View

```

## Parameters

- `isPresented` — A binding to a Boolean value that determines whether to present the alert that you create in the modifier’s `content` closure. When the user presses or taps OK the system sets `isPresented` to `false` which dismisses the alert.

- `content` — A closure returning the alert to present.

## Discussion

Use this method when you need to show an alert to the user. The example below displays an alert that is shown when the user toggles a Boolean value that controls the presentation of the alert:

```swift
struct OrderCompleteAlert: View {
    @State private var isPresented = false
    var body: some View {
        Button("Show Alert", action: {
            isPresented = true
        })
        .alert(isPresented: $isPresented) {
            Alert(title: Text("Order Complete"),
                  message: Text("Thank you for shopping with us."),
                  dismissButton: .default(Text("OK")))
        }
    }
}
```

![](../../../../attachments/484648a41f7dabaa507054457b090206/SwiftUI-View-AlertIsPresentedContent@2x.png)

<sub>An alert whose title reads Order Complete, with the message, Thank you for shopping with us placed underneath. The alert also includes an OK button for dismissing the alert.</sub>

## See Also

### View presentation modifiers

- [actionSheet(isPresented:content:)](<actionsheet(ispresented_content_).md>) — Presents an action sheet when a given condition is true. _(deprecated)_
- [actionSheet(item:content:)](<actionsheet(item_content_).md>) — Presents an action sheet using the given item as a data source for the sheet’s content. _(deprecated)_
- [alert(item:content:)](<alert(item_content_).md>) — Presents an alert to the user. _(deprecated)_
