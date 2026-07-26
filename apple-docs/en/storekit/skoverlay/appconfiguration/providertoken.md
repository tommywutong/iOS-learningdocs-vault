---
title: providerToken
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skoverlay/appconfiguration/providertoken
source_url: 'https://developer.apple.com/documentation/storekit/skoverlay/appconfiguration/providertoken'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skoverlay/appconfiguration/providertoken.json'
content_hash: 'sha256:ea741222fa0f8959'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [SKOverlay](../../skoverlay.md) · [AppConfiguration](../appconfiguration.md)

# providerToken

<sub>Instance Property</sub>

A token that represents the provider of an app promotion campaign, and that you use to measure the campaign’s effectiveness.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var providerToken: String? { get set }
```

## Discussion

When you set a provider token, you must also set the [campaignToken](campaigntoken.md).

When promoting your own apps, set your own provider token using `providerToken`. This allows you to track a promotion’s effectiveness independently from any affiliate campaign that shares the same campaign token.

When promoting apps by other developers, set `providerToken` using their provider token. This allows those developers to track the effectiveness of your App Store Connect Analytics campaign.

## See Also

### Verifying Advertising Campaigns

- [campaignToken](campaigntoken.md) — A token you use to represent an ad campaign and measure its effectiveness.
- [- setAdditionalValue:forKey:](<setadditionalvalue(__forkey_).md>) — Sets an additional value for a key; for example, a value for measuring the effectiveness of an ad campaign.
- [- additionalValueForKey:](<additionalvalue(forkey_).md>) — Returns the object associated with the key.
