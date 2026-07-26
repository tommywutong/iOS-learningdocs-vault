---
title: 'init(hostingDelegateClass:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 27.0+ beta, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscenesessionactivationrequest-swift.struct/init(hostingdelegateclass:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-swift.struct/init(hostingdelegateclass:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenesessionactivationrequest-swift.struct/init%28hostingdelegateclass%3A%29.json'
content_hash: 'sha256:ca58391967843865'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneSessionActivationRequest](../uiscenesessionactivationrequest-swift.struct.md)

# init(hostingDelegateClass:)

<sub>Initializer</sub>

Creates a `UISceneSessionActivationRequest` customized to open a SwiftUI scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init?<D>(hostingDelegateClass: D.Type) where D : UIHostingSceneDelegate
```

## Parameters

- `hostingDelegateClass` — A Class type that conforms to `UIHostingSceneDelegate`.

## Discussion

The first scene declared in the `rootScene` property of your hosting delegate class will be activated by this request.

```
class HostingSceneDelegate: UIHostingSceneDelegate {
    static var rootScene: some Scene {
        WindowGroup() {
            ContentView()
        }
    }
}

let request = UISceneSessionActivationRequest(
    hostingDelegateClass: HostingSceneDelegate.self
)
UIApplication.shared.activateSceneSession(for: request)
```

When a UIScene is activated using this request object, its configuration is managed by SwiftUI. You will not see a call to your app delegate’s `application(_:configurationForConnecting:options:)` method.

An instance of the provided hosting delegate class will be created by SwiftUI and receive lifecycle callbacks for the associated scene.
