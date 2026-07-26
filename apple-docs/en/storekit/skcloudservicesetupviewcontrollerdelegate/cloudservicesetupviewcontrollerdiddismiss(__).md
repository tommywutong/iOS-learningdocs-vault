---
title: 'cloudServiceSetupViewControllerDidDismiss(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.1+（18.0 起废弃）, iPadOS 10.1+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skcloudservicesetupviewcontrollerdelegate/cloudservicesetupviewcontrollerdiddismiss(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/skcloudservicesetupviewcontrollerdelegate/cloudservicesetupviewcontrollerdiddismiss(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skcloudservicesetupviewcontrollerdelegate/cloudservicesetupviewcontrollerdiddismiss%28_%3A%29.json'
content_hash: 'sha256:5b48f7d8d93fd809'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKCloudServiceSetupViewControllerDelegate](../skcloudservicesetupviewcontrollerdelegate.md)

# cloudServiceSetupViewControllerDidDismiss(_:)

<sub>Instance Method</sub>

Tells the delegate that the cloud service setup view controller was dismissed.

> [!warning] Deprecated
> Use the musicSubscriptionOffer(isPresented:options:onLoadCompletion:) SwiftUI View Modifier from MusicKit.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func cloudServiceSetupViewControllerDidDismiss(_ cloudServiceSetupViewController: SKCloudServiceSetupViewController)
```

## Parameters

- `cloudServiceSetupViewController` — The cloud service view controller that was dismissed.
