---
title: 'load(options:completionHandler:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.1+（18.0 起废弃）, iPadOS 10.1+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skcloudservicesetupviewcontroller/load(options:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/storekit/skcloudservicesetupviewcontroller/load(options:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skcloudservicesetupviewcontroller/load%28options%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:1ac942e591f609fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKCloudServiceSetupViewController](../skcloudservicesetupviewcontroller.md)

# load(options:completionHandler:)

<sub>Instance Method</sub>

Loads the cloud service setup view with the specified options.

> [!warning] Deprecated
> Use the musicSubscriptionOffer(isPresented:options:onLoadCompletion:) SwiftUI View Modifier from MusicKit.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func load(options: [SKCloudServiceSetupOptionsKey : Any] = [:], completionHandler: ((Bool, (any Error)?) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func load(options: [SKCloudServiceSetupOptionsKey : Any] = [:]) async throws -> Bool
```

## Parameters

- `options` — A key that identifies the type of setup the user needs to do. See [SKCloudServiceSetupOptionsKey](../skcloudservicesetupoptionskey.md) for possible values.

- `completionHandler` — A block that is called when the setup view has loaded. The block takes the following parameters: `result` A Boolean value that indicates whether the view controller has loaded the view and can be presented. `error` An error value that indicates the reason for failure. Possible values are [SKErrorUnknown](../skerror/code/unknown.md), [SKErrorCloudServicePermissionDenied](../skerror/code/cloudservicepermissiondenied.md), and [SKErrorCloudServiceNetworkConnectionFailed](../skerror/code/cloudservicenetworkconnectionfailed.md).

## Discussion

## See Also

### Loading the setup view

- [Offering Apple Music Subscription in Your App](../offering-apple-music-subscription-in-your-app.md) — Allow eligible customers to subscribe to Apple Music.
- [SKCloudServiceSetupOptionsKey](../skcloudservicesetupoptionskey.md) — Keys to specify the types of setup options for a cloud service.
- [SKArcadeService](../skarcadeservice.md)
