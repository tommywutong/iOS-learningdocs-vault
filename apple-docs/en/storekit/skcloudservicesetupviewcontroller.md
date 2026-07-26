---
title: SKCloudServiceSetupViewController
framework: StoreKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.1+（18.0 起废弃）, iPadOS 10.1+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skcloudservicesetupviewcontroller
source_url: 'https://developer.apple.com/documentation/storekit/skcloudservicesetupviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skcloudservicesetupviewcontroller.json'
content_hash: 'sha256:8b7e9da9a6242b1a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKCloudServiceSetupViewController

<sub>Class</sub>

A view controller that helps people perform setup for a cloud service, like an Apple Music subscription.

> [!warning] Deprecated
> Use [musicSubscriptionOffer(isPresented:options:onLoadCompletion:)](<../swiftui/view/musicsubscriptionoffer(ispresented_options_onloadcompletion_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor class SKCloudServiceSetupViewController
```

## Overview

Use the view that this view controller presents to allow customers to set up cloud services that are associated with their iTunes Store account, like an Apple Music subscription.

To enable the Apple Music subscriber setup flow in particular, you first request the current set of capabilities from [SKCloudServiceController](skcloudservicecontroller.md). Then, present the setup view controller only when the [SKCloudServiceCapabilityMusicCatalogSubscriptionEligible](skcloudservicecapability/musiccatalogsubscriptioneligible.md) capability is enabled and the [SKCloudServiceCapabilityMusicCatalogPlayback](skcloudservicecapability/musiccatalogplayback.md) capability is disabled.

For information about other capabilities that you can enable by using this view controller, see [SKCloudServiceCapability](skcloudservicecapability.md).

## Relationships

- **Inherits From**: [UIViewController](../uikit/uiviewcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md), [UIAppearanceContainer](../uikit/uiappearancecontainer.md), [UIContentContainer](../uikit/uicontentcontainer.md), [UIFocusEnvironment](../uikit/uifocusenvironment.md), [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md), [UIStateRestoring](../uikit/uistaterestoring.md), [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md), [UITraitEnvironment](../uikit/uitraitenvironment.md), [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## Topics

### Setting a delegate

- [delegate](skcloudservicesetupviewcontroller/delegate.md) — The cloud service view controller’s delegate. _(deprecated)_
- [SKCloudServiceSetupViewControllerDelegate](skcloudservicesetupviewcontrollerdelegate.md) — A protocol that defines the methods a cloud service setup view controller can use to get the status of the view, including when it is dismissed. _(deprecated)_

### Loading the setup view

- [Offering Apple Music Subscription in Your App](offering-apple-music-subscription-in-your-app.md) — Allow eligible customers to subscribe to Apple Music.
- [SKCloudServiceSetupOptionsKey](skcloudservicesetupoptionskey.md) — Keys to specify the types of setup options for a cloud service.
- [- loadWithOptions:completionHandler:](<skcloudservicesetupviewcontroller/load(options_completionhandler_).md>) — Loads the cloud service setup view with the specified options. _(deprecated)_
- [SKArcadeService](skarcadeservice.md)

## See Also

### Deprecated

- [SKCloudServiceController](skcloudservicecontroller.md) — An object that determines the current capabilities of a person’s Music library. _(deprecated)_
