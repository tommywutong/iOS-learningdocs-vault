---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [watchOS 10.0+（10.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/wkextensiondelegateadaptor/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/wkextensiondelegateadaptor/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/wkextensiondelegateadaptor/init%28_%3A%29.json'
content_hash: 'sha256:9fb8ef1bb9b734a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WKExtensionDelegateAdaptor](../wkextensiondelegateadaptor.md)

# init(_:)

<sub>Initializer</sub>

Creates a WatchKit extension delegate adaptor using an observable delegate.

> [!warning] Deprecated
> Use WKApplicationDelegateAdaptor with a WKApplicationDelegate instead.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency init(_ delegateType: DelegateType.Type = DelegateType.self)
```

## Parameters

- `delegateType` — The type of extension delegate that you define in your app, which conforms to the [WKExtensionDelegate](../../watchkit/wkextensiondelegate.md) and [Observable](../../observation/observable.md) protocols.

## Discussion

Call this initializer indirectly by creating a property with the [WKExtensionDelegateAdaptor](../wkextensiondelegateadaptor.md) property wrapper from inside your [App](../app.md) declaration:

```swift
@main
struct MyApp: App {
    @WKExtensionDelegateAdaptor private var extensionDelegate: MyExtensionDelegate

    var body: some Scene { ... }
}
```

SwiftUI initializes the delegate and manages its lifetime, calling it as needed to handle extension delegate callbacks.

SwiftUI invokes this method when your app delegate conforms to the [Observable](../../observation/observable.md) protocol. In this case, SwiftUI automatically places the delegate in the [Environment](../environment.md). You can access such a delegate from any scene or view in your app using the [Environment](../environment.md) property wrapper:

```swift
@Environment(MyAppDelegate.self) private var appDelegate
```

If your delegate isn’t observable, SwiftUI invokes the [init(_:)](<init(__)-2556.md>) initializer rather than this one, and doesn’t put the delegate instance in the environment.
