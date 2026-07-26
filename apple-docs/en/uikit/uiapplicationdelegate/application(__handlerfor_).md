---
title: 'application(_:handlerFor:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:handlerfor:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:handlerfor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Ahandlerfor%3A%29.json'
content_hash: 'sha256:a876b0e0a7eb4228'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:handlerFor:)

<sub>Instance Method</sub>

Asks the delegate for an intent handler capable of handling the specified intent.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func application(_ application: UIApplication, handlerFor intent: INIntent) -> Any?
```

## Parameters

- `application` — The shared app object.

- `intent` — The intent object that represents the request coming from the system.

## Return Value

An instance of a type capable of handling the specified intent; otherwise, `nil` if your app doesn’t handle the intent. Return an instance of a type that conforms to the handling intents protocol for the same type as the provided intent.

## Discussion

> [!important] Important
> The system only invokes this method in apps that support multiple scenes. For more information, see [Specifying the scenes your app supports](../specifying-the-scenes-your-app-supports.md).

Siri invokes this method on the main queue when it wants to process one of your app’s supported intents. To indicate the intents that your app supports, populate the [INIntentsSupported](../../bundleresources/information-property-list/inintentssupported.md) array in your app target’s `Info.plist` file.

In your delegate’s implementation of this method, check the `intent` parameter’s type and return a custom object that adopts the corresponding handling protocol. For example, if `intent` is an instance of [INPlayMediaIntent](../../intents/inplaymediaintent.md), return an object that adopts [INPlayMediaIntentHandling](../../intents/inplaymediaintenthandling.md). Only use the provided intent to determine the handler to return; don’t use it to initialize the handler and don’t store a reference to it. SiriKit updates the intent throughout the request to incorporate information the requester provides. For more information, see [Dispatching intents to handlers](../../sirikit/dispatching-intents-to-handlers.md).

For information about handling intents, see [Resolving and Handling Intents](../../sirikit/resolving-and-handling-intents.md).
