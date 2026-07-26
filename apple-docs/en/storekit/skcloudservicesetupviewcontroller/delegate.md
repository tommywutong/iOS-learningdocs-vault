---
title: delegate
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.1+（18.0 起废弃）, iPadOS 10.1+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skcloudservicesetupviewcontroller/delegate
source_url: 'https://developer.apple.com/documentation/storekit/skcloudservicesetupviewcontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skcloudservicesetupviewcontroller/delegate.json'
content_hash: 'sha256:4a7d2cb1597a553c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKCloudServiceSetupViewController](../skcloudservicesetupviewcontroller.md)

# delegate

<sub>Instance Property</sub>

The cloud service view controller’s delegate.

> [!warning] Deprecated
> Use the musicSubscriptionOffer(isPresented:options:onLoadCompletion:) SwiftUI View Modifier from MusicKit.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
weak var delegate: (any SKCloudServiceSetupViewControllerDelegate)? { get set }
```

## Discussion

You can identify a delegate to get informed when the cloud service setup view controller is dismissed.

## See Also

### Setting a delegate

- [SKCloudServiceSetupViewControllerDelegate](../skcloudservicesetupviewcontrollerdelegate.md) — A protocol that defines the methods a cloud service setup view controller can use to get the status of the view, including when it is dismissed. _(deprecated)_
