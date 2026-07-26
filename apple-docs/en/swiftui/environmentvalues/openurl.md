---
title: openURL
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/openurl
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/openurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/openurl.json'
content_hash: 'sha256:a156abf367cf918d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# openURL

<sub>Instance Property</sub>

An action that opens a URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency var openURL: OpenURLAction { get set }
```

## Discussion

Read this environment value to get an [OpenURLAction](../openurlaction.md) instance for a given [Environment](../environment.md). Call the instance to open a URL. You call the instance directly because it defines a [callAsFunction(_:)](<../openurlaction/callasfunction(__).md>) method that Swift calls when you call the instance.

For example, you can open a web site when the user taps a button:

```swift
struct OpenURLExample: View {
    @Environment(\.openURL) private var openURL

    var body: some View {
        Button {
            if let url = URL(string: "https://www.example.com") {
                openURL(url)
            }
        } label: {
            Label("Get Help", systemImage: "person.fill.questionmark")
        }
    }
}
```

If you want to know whether the action succeeds, add a completion handler that takes a Boolean value. In this case, Swift implicitly calls the [callAsFunction(_:completion:)](<../openurlaction/callasfunction(__completion_).md>) method instead. That method calls your completion handler after it determines whether it can open the URL, but possibly before it finishes opening the URL. You can add a handler to the example above so that it prints the outcome to the console:

```swift
openURL(url) { accepted in
    print(accepted ? "Success" : "Failure")
}
```

The system provides a default open URL action with behavior that depends on the contents of the URL. For example, the default action opens a Universal Link in the associated app if possible, or in the user’s default web browser if not.

You can also set a custom action using the [environment(_:_:)](<../view/environment(____).md>) view modifier. Any views that read the action from the environment, including the built-in [Link](../link.md) view and [Text](../text.md) views with markdown links, or links in attributed strings, use your action. Initialize an action by calling the [init(handler:)](<../openurlaction/init(handler_).md>) initializer with a handler that takes a URL and returns an [Result](../openurlaction/result.md):

```swift
Text("Visit [Example Company](https://www.example.com) for details.")
    .environment(\.openURL, OpenURLAction { url in
        handleURL(url) // Define this method to take appropriate action.
        return .handled
    })
```

SwiftUI translates the value that your custom action’s handler returns into an appropriate Boolean result for the action call. For example, a view that uses the action declared above receives `true` when calling the action, because the handler always returns [handled](../openurlaction/result/handled.md).

## See Also

### Sending and receiving URLs

- [OpenURLAction](../openurlaction.md) — An action that opens a URL.
- [onOpenURL(perform:)](<../view/onopenurl(perform_).md>) — Registers a handler to invoke in response to a URL that your app receives.
