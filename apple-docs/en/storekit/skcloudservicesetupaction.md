---
title: SKCloudServiceSetupAction
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skcloudservicesetupaction
source_url: 'https://developer.apple.com/documentation/storekit/skcloudservicesetupaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skcloudservicesetupaction.json'
content_hash: 'sha256:72ba750fd710b358'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKCloudServiceSetupAction

<sub>Structure</sub>

A string used to specify the type of setup action to offer for a cloud service.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct SKCloudServiceSetupAction
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(rawValue:)](<skcloudservicesetupaction/init(rawvalue_).md>) — Initializes a setup action to offer for a cloud service using the specified value.

### Type Properties

- [SKCloudServiceSetupActionSubscribe](skcloudservicesetupaction/subscribe.md) — A subscribe action in a cloud service setup view, such as an offer to subscribe to Apple Music. _(deprecated)_

## See Also

### Indicating Setup Options

- [SKCloudServiceSetupOptionsActionKey](skcloudservicesetupoptionskey/action.md) — A key that specifies the action for a setup entry point. _(deprecated)_
- [SKCloudServiceSetupOptionsITunesItemIdentifierKey](skcloudservicesetupoptionskey/itunesitemidentifier.md) — A key that specifies the iTunes Store item that the user is trying to access through the service. _(deprecated)_
- [SKCloudServiceSetupOptionsAffiliateTokenKey](skcloudservicesetupoptionskey/affiliatetoken.md) — A key that specifies the iTunes Store affiliate token. _(deprecated)_
- [SKCloudServiceSetupOptionsCampaignTokenKey](skcloudservicesetupoptionskey/campaigntoken.md) — A key that specifies the iTunes Store affiliate campaign token. _(deprecated)_
- [SKCloudServiceSetupOptionsMessageIdentifierKey](skcloudservicesetupoptionskey/messageidentifier.md) — A key that is used to select the main message presented to the user for this setup view. _(deprecated)_
- [SKCloudServiceSetupMessageIdentifier](skcloudservicesetupmessageidentifier.md) — Identifiers for the available messages the setup view can present to the user.
