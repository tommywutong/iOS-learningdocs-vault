---
title: messageIdentifier
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+（18.0 起废弃）, iPadOS 11.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, tvOS 11.0+（18.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skcloudservicesetupoptionskey/messageidentifier
source_url: 'https://developer.apple.com/documentation/storekit/skcloudservicesetupoptionskey/messageidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skcloudservicesetupoptionskey/messageidentifier.json'
content_hash: 'sha256:74dd643ff57445dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKCloudServiceSetupOptionsKey](../skcloudservicesetupoptionskey.md)

# messageIdentifier

<sub>Type Property</sub>

A key that is used to select the main message presented to the user for this setup view.

> [!warning] Deprecated
> Use the messageIdentifier property of MusicSubscriptionOffer.Options from MusicKit.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
static let messageIdentifier: SKCloudServiceSetupOptionsKey
```

## Discussion

If this key is missing, the setup view is configured as if it is using the [SKCloudServiceSetupMessageIdentifierJoin](../skcloudservicesetupmessageidentifier/join.md) key by default.

## See Also

### Indicating Setup Options

- [SKCloudServiceSetupOptionsActionKey](action.md) — A key that specifies the action for a setup entry point. _(deprecated)_
- [SKCloudServiceSetupAction](../skcloudservicesetupaction.md) — A string used to specify the type of setup action to offer for a cloud service.
- [SKCloudServiceSetupOptionsITunesItemIdentifierKey](itunesitemidentifier.md) — A key that specifies the iTunes Store item that the user is trying to access through the service. _(deprecated)_
- [SKCloudServiceSetupOptionsAffiliateTokenKey](affiliatetoken.md) — A key that specifies the iTunes Store affiliate token. _(deprecated)_
- [SKCloudServiceSetupOptionsCampaignTokenKey](campaigntoken.md) — A key that specifies the iTunes Store affiliate campaign token. _(deprecated)_
- [SKCloudServiceSetupMessageIdentifier](../skcloudservicesetupmessageidentifier.md) — Identifiers for the available messages the setup view can present to the user.
