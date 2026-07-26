---
title: SKCloudServiceSetupMessageIdentifier
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skcloudservicesetupmessageidentifier
source_url: 'https://developer.apple.com/documentation/storekit/skcloudservicesetupmessageidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skcloudservicesetupmessageidentifier.json'
content_hash: 'sha256:eea1d12516c37e9f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKCloudServiceSetupMessageIdentifier

<sub>Structure</sub>

Identifiers for the available messages the setup view can present to the user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct SKCloudServiceSetupMessageIdentifier
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing Identifiers

- [init(rawValue:)](<skcloudservicesetupmessageidentifier/init(rawvalue_).md>) — Initializes a cloud service setup message identifier based on the provided raw value.

### Message Identifiers

- [SKCloudServiceSetupMessageIdentifierAddMusic](skcloudservicesetupmessageidentifier/addmusic.md) — Message identifier for adding music. _(deprecated)_
- [SKCloudServiceSetupMessageIdentifierConnect](skcloudservicesetupmessageidentifier/connect.md) — Message identifier for connecting. _(deprecated)_
- [SKCloudServiceSetupMessageIdentifierJoin](skcloudservicesetupmessageidentifier/join.md) — Message identifier for joining. _(deprecated)_
- [SKCloudServiceSetupMessageIdentifierPlayMusic](skcloudservicesetupmessageidentifier/playmusic.md) — Message identifier for playing music. _(deprecated)_

## See Also

### Indicating Setup Options

- [SKCloudServiceSetupOptionsActionKey](skcloudservicesetupoptionskey/action.md) — A key that specifies the action for a setup entry point. _(deprecated)_
- [SKCloudServiceSetupAction](skcloudservicesetupaction.md) — A string used to specify the type of setup action to offer for a cloud service.
- [SKCloudServiceSetupOptionsITunesItemIdentifierKey](skcloudservicesetupoptionskey/itunesitemidentifier.md) — A key that specifies the iTunes Store item that the user is trying to access through the service. _(deprecated)_
- [SKCloudServiceSetupOptionsAffiliateTokenKey](skcloudservicesetupoptionskey/affiliatetoken.md) — A key that specifies the iTunes Store affiliate token. _(deprecated)_
- [SKCloudServiceSetupOptionsCampaignTokenKey](skcloudservicesetupoptionskey/campaigntoken.md) — A key that specifies the iTunes Store affiliate campaign token. _(deprecated)_
- [SKCloudServiceSetupOptionsMessageIdentifierKey](skcloudservicesetupoptionskey/messageidentifier.md) — A key that is used to select the main message presented to the user for this setup view. _(deprecated)_
