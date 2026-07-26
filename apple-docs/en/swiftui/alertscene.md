---
title: AlertScene
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/alertscene
source_url: 'https://developer.apple.com/documentation/swiftui/alertscene'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/alertscene.json'
content_hash: 'sha256:7f172f74a2410f94'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AlertScene

<sub>Structure</sub>

A scene that renders itself as a standalone alert dialog.

<sub>macOS</sub>

```swift
nonisolated struct AlertScene<Actions, Message> where Actions : View, Message : View
```

## Overview

Alert scenes present themselves in the center of the current display, and don’t attach to any particular window. The system prevents interaction with the app until someone dismisses the alert scene.

```swift
@main
struct MyApp: App {
    @State var showLoginAlert = true
    @State var loggedIn = false

    var body: some Scene {
        Window("Welcome User Window", id:"WelcomeWindow") {
            ...
        }
        .defaultLaunchBehavior(loggedIn ? .presented : .suppressed)

        AlertScene("Login Required", isPresented: $showLoginAlert) {
            Button("OK") {
                ...
            }
        }
    }
}
```

All the actions you provide in the [ContentBuilder](contentbuilder.md) dismiss the alert when someone invokes them. Like the alert modifier, specify the role of the buttons with [cancel](buttonrole/cancel.md) or [destructive](buttonrole/destructive.md). If you don’t provide any actions, the system automatically includes a button with the title “OK” that dismisses the alert scene.

## Relationships

- **Conforms To**: [Scene](scene.md)

## Topics

### Initializers

- [init(_:isPresented:actions:)](<alertscene/init(__ispresented_actions_).md>) — Creates an alert scene with a title and a set of actions. Note that this creates a text view on your behalf.
- [init(_:isPresented:actions:message:)](<alertscene/init(__ispresented_actions_message_).md>) — Creates an alert scene with a title, a set of actions, and a message. Note that this creates a text view on your behalf.
- [init(_:isPresented:presenting:actions:)](<alertscene/init(__ispresented_presenting_actions_).md>) — Creates an alert scene, using the given data to produce the alert’s content with a title, and a set of actions. Note that this creates a text view on your behalf.
- [init(_:isPresented:presenting:actions:message:)](<alertscene/init(__ispresented_presenting_actions_message_).md>) — Creates an alert scene, using the given data to produce the alert’s content with a title, a set of actions, and a message. Note that this creates a text view on your behalf.
- [init(_:item:actions:)](<alertscene/init(__item_actions_).md>) — Creates an alert scene, using the given data to produce the alert’s content with a title, and a set of actions. Note that this creates a text view on your behalf.
- [init(_:item:actions:message:)](<alertscene/init(__item_actions_message_).md>) — Creates an alert scene, using the given data to produce the alert’s content with a title, a set of actions, and a message. Note that this creates a text view on your behalf.

## See Also

### Presenting an alert

- [alert(_:isPresented:actions:)](<view/alert(__ispresented_actions_).md>) — Presents an alert when a given condition is true, using a localized string resource for the title.
- [alert(_:isPresented:presenting:actions:)](<view/alert(__ispresented_presenting_actions_).md>) — Presents an alert using the given data to produce the alert’s content and a localized string resource for a title.
- [alert(_:item:actions:)](<view/alert(__item_actions_).md>) — Presents an alert using the given data to produce the alert’s content and a text view as a title.
- [alert(error:actions:)](<view/alert(error_actions_).md>) — Presents an alert when an error is present.
- [alert(isPresented:error:actions:)](<view/alert(ispresented_error_actions_).md>) — Presents an alert when an error is present.
- [alert(_:isPresented:actions:message:)](<view/alert(__ispresented_actions_message_).md>) — Presents an alert with a message when a given condition is true, using a localized string resource for a title.
- [alert(_:isPresented:presenting:actions:message:)](<view/alert(__ispresented_presenting_actions_message_).md>) — Presents an alert with a message using the given data to produce the alert’s content and a localized string resource for a title.
- [alert(_:item:actions:message:)](<view/alert(__item_actions_message_).md>) — Presents an alert with a message using the given data to produce the alert’s content and a localized string key for a title.
- [alert(error:actions:message:)](<view/alert(error_actions_message_).md>) — Presents an alert with a message when an error is present.
- [alert(isPresented:error:actions:message:)](<view/alert(ispresented_error_actions_message_).md>) — Presents an alert with a message when an error is present.
