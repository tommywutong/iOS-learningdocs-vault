---
title: action
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.1+（18.0 起废弃）, iPadOS 10.1+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, tvOS 10.0+（18.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skcloudservicesetupoptionskey/action
source_url: 'https://developer.apple.com/documentation/storekit/skcloudservicesetupoptionskey/action'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skcloudservicesetupoptionskey/action.json'
content_hash: 'sha256:d5bb9057359e2cf0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKCloudServiceSetupOptionsKey](../skcloudservicesetupoptionskey.md)

# action

<sub>Type Property</sub>

A key that specifies the action for a setup entry point.

> [!warning] Deprecated
> Use the action property of MusicSubscriptionOffer.Options from MusicKit.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
static let action: SKCloudServiceSetupOptionsKey
```

## See Also

### Indicating Setup Options

- [SKCloudServiceSetupAction](../skcloudservicesetupaction.md) — A string used to specify the type of setup action to offer for a cloud service.
- [SKCloudServiceSetupOptionsITunesItemIdentifierKey](itunesitemidentifier.md) — A key that specifies the iTunes Store item that the user is trying to access through the service. _(deprecated)_
- [SKCloudServiceSetupOptionsAffiliateTokenKey](affiliatetoken.md) — A key that specifies the iTunes Store affiliate token. _(deprecated)_
- [SKCloudServiceSetupOptionsCampaignTokenKey](campaigntoken.md) — A key that specifies the iTunes Store affiliate campaign token. _(deprecated)_
- [SKCloudServiceSetupOptionsMessageIdentifierKey](messageidentifier.md) — A key that is used to select the main message presented to the user for this setup view. _(deprecated)_
- [SKCloudServiceSetupMessageIdentifier](../skcloudservicesetupmessageidentifier.md) — Identifiers for the available messages the setup view can present to the user.
