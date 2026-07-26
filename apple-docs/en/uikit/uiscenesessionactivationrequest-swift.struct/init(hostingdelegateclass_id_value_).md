---
title: 'init(hostingDelegateClass:id:value:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 27.0+ beta, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscenesessionactivationrequest-swift.struct/init(hostingdelegateclass:id:value:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-swift.struct/init(hostingdelegateclass:id:value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenesessionactivationrequest-swift.struct/init%28hostingdelegateclass%3Aid%3Avalue%3A%29.json'
content_hash: 'sha256:05bc5b2bba16d224'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneSessionActivationRequest](../uiscenesessionactivationrequest-swift.struct.md)

# init(hostingDelegateClass:id:value:)

<sub>Initializer</sub>

Creates a `UISceneSessionActivationRequest` customized to open a SwiftUI scene with the given identifier and presented value.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init?<H, D>(hostingDelegateClass: H.Type, id: String, value: D) where H : UIHostingSceneDelegate, D : Decodable, D : Encodable, D : Hashable
```

## Parameters

- `hostingDelegateClass` — A Class type that conforms to `UIHostingSceneDelegate`.

- `id` — A string matching the `id` of one of the scenes declared in the sceneRepresentation’s content.

- `value` — The data to be presented in the scene.

## Discussion

The specified scene must be declared in the `rootScene` property of your hosting delegate class. The initializer will fail if no scene with the specified identifier is defined.

```
class HostingSceneDelegate: UIHostingSceneDelegate {
    static var rootScene: some Scene {
        WindowGroup(id: "window", for: FavoriteNumber.self) { $value in
            ContentView(favoriteNumber: $value)
        }
    }
}

if let activationWithIDAndData = UISceneSessionActivationRequest(
    hostingDelegateClass: HostingSceneDelegate.self,
    id: "window", value: FavoriteNumber(13)
) {
    UIApplication.shared.activateSceneSession(for: activationWithIDAndData)
}
```

When a UIScene is activated using this request object, its configuration is managed by SwiftUI. You will not see a call to your app delegate’s `application(_:configurationForConnecting:)` method.

An instance of the provided hosting delegate class will be created by SwiftUI and receive lifecycle callbacks for the associated scene.
