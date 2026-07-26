---
title: SKCloudServiceSetupOptionsKey
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skcloudservicesetupoptionskey
source_url: 'https://developer.apple.com/documentation/storekit/skcloudservicesetupoptionskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skcloudservicesetupoptionskey.json'
content_hash: 'sha256:e4e6d718ae3bfd21'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKCloudServiceSetupOptionsKey

<sub>Structure</sub>

Keys to specify the types of setup options for a cloud service.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct SKCloudServiceSetupOptionsKey
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing

- [init(rawValue:)](<skcloudservicesetupoptionskey/init(rawvalue_).md>) — Initializes a cloud service setup options key based on the provided raw value.

### Indicating Setup Options

- [SKCloudServiceSetupOptionsActionKey](skcloudservicesetupoptionskey/action.md) — A key that specifies the action for a setup entry point. _(deprecated)_
- [SKCloudServiceSetupAction](skcloudservicesetupaction.md) — A string used to specify the type of setup action to offer for a cloud service.
- [SKCloudServiceSetupOptionsITunesItemIdentifierKey](skcloudservicesetupoptionskey/itunesitemidentifier.md) — A key that specifies the iTunes Store item that the user is trying to access through the service. _(deprecated)_
- [SKCloudServiceSetupOptionsAffiliateTokenKey](skcloudservicesetupoptionskey/affiliatetoken.md) — A key that specifies the iTunes Store affiliate token. _(deprecated)_
- [SKCloudServiceSetupOptionsCampaignTokenKey](skcloudservicesetupoptionskey/campaigntoken.md) — A key that specifies the iTunes Store affiliate campaign token. _(deprecated)_
- [SKCloudServiceSetupOptionsMessageIdentifierKey](skcloudservicesetupoptionskey/messageidentifier.md) — A key that is used to select the main message presented to the user for this setup view. _(deprecated)_
- [SKCloudServiceSetupMessageIdentifier](skcloudservicesetupmessageidentifier.md) — Identifiers for the available messages the setup view can present to the user.

## See Also

### Loading the setup view

- [Offering Apple Music Subscription in Your App](offering-apple-music-subscription-in-your-app.md) — Allow eligible customers to subscribe to Apple Music.
- [- loadWithOptions:completionHandler:](<skcloudservicesetupviewcontroller/load(options_completionhandler_).md>) — Loads the cloud service setup view with the specified options. _(deprecated)_
- [SKArcadeService](skarcadeservice.md)
