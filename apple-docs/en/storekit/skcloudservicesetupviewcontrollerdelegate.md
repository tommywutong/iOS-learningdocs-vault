---
title: SKCloudServiceSetupViewControllerDelegate
framework: StoreKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 10.1+（18.0 起废弃）, iPadOS 10.1+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skcloudservicesetupviewcontrollerdelegate
source_url: 'https://developer.apple.com/documentation/storekit/skcloudservicesetupviewcontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skcloudservicesetupviewcontrollerdelegate.json'
content_hash: 'sha256:71c6659475a1ed12'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKCloudServiceSetupViewControllerDelegate

<sub>Protocol</sub>

A protocol that defines the methods a cloud service setup view controller can use to get the status of the view, including when it is dismissed.

> [!warning] Deprecated
> Use the musicSubscriptionOffer(isPresented:options:onLoadCompletion:) SwiftUI View Modifier from MusicKit.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
protocol SKCloudServiceSetupViewControllerDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Receiving Notification of Dismissal

- [- cloudServiceSetupViewControllerDidDismiss:](<skcloudservicesetupviewcontrollerdelegate/cloudservicesetupviewcontrollerdiddismiss(__).md>) — Tells the delegate that the cloud service setup view controller was dismissed. _(deprecated)_

## See Also

### Setting a delegate

- [delegate](skcloudservicesetupviewcontroller/delegate.md) — The cloud service view controller’s delegate. _(deprecated)_
