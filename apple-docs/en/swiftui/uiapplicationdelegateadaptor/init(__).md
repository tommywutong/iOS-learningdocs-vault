---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uiapplicationdelegateadaptor/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uiapplicationdelegateadaptor/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uiapplicationdelegateadaptor/init%28_%3A%29.json'
content_hash: 'sha256:f51b170dddab2d5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIApplicationDelegateAdaptor](../uiapplicationdelegateadaptor.md)

# init(_:)

<sub>Initializer</sub>

Creates a UIKit app delegate adaptor using an observable delegate.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency init(_ delegateType: DelegateType.Type = DelegateType.self)
```

## Parameters

- `delegateType` — The type of application delegate that you define in your app, which conforms to the [UIApplicationDelegate](../../uikit/uiapplicationdelegate.md) and [Observable](../../observation/observable.md) protocols.

## Discussion

Call this initializer indirectly by creating a property with the [UIApplicationDelegateAdaptor](../uiapplicationdelegateadaptor.md) property wrapper from inside your [App](../app.md) declaration:

```swift
@main
struct MyApp: App {
    @UIApplicationDelegateAdaptor private var appDelegate: MyAppDelegate

    var body: some Scene { ... }
}
```

SwiftUI initializes the delegate and manages its lifetime, calling it as needed to handle application delegate callbacks.

SwiftUI invokes this method when your app delegate conforms to the [Observable](../../observation/observable.md) protocol. In this case, SwiftUI automatically places the delegate in the [Environment](../environment.md). You can access such a delegate from any scene or view in your app using the [Environment](../environment.md) property wrapper:

```swift
@Environment(MyAppDelegate.self) private var appDelegate
```

If your delegate isn’t observable, SwiftUI invokes the [init(_:)](<init(__)-59sfu.md>) initializer rather than this one, and doesn’t put the delegate instance in the environment.
