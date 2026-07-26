---
title: 'init(hostingDelegateClass:id:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 27.0+ beta, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscenesessionactivationrequest-swift.struct/init(hostingdelegateclass:id:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-swift.struct/init(hostingdelegateclass:id:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenesessionactivationrequest-swift.struct/init%28hostingdelegateclass%3Aid%3A%29.json'
content_hash: 'sha256:9ac653505ee97c8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneSessionActivationRequest](../uiscenesessionactivationrequest-swift.struct.md)

# init(hostingDelegateClass:id:)

<sub>Initializer</sub>

Creates a `UISceneSessionActivationRequest` customized to open a SwiftUI scene with the given identifier.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init?<D>(hostingDelegateClass: D.Type, id: String) where D : UIHostingSceneDelegate
```

## Parameters

- `hostingDelegateClass` — A Class type that conforms to `UIHostingSceneDelegate`.

- `id` — A string matching the `id` of one of the scenes declared in the sceneRepresentation’s content.

## Discussion

The specified scene must be declared in the `rootScene` property of your hosting delegate class. The initializer will fail if no scene with the specified identifier is defined.

```
class HostingSceneDelegate: UIHostingSceneDelegate {
    static var rootScene: some Scene {
        WindowGroup(id: "swiftui-window") {
            ContentView()
        }
    }
}

if let requestWithID = UISceneSessionActivationRequest(
    hostingDelegateClass: HostingSceneDelegate.self,
    id: "swiftui-window"
) {
    UIApplication.shared.activateSceneSession(for: requestWithID)
}
```

When a UIScene is activated using this request object, its configuration is managed by SwiftUI. You will not see a call to your app delegate’s `application(_:configurationForConnecting:options:)` method.

An instance of the provided hosting delegate class will be created by SwiftUI and receive lifecycle callbacks for the associated scene.
