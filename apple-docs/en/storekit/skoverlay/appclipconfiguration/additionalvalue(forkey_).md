---
title: 'additionalValue(forKey:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/storekit/skoverlay/appclipconfiguration/additionalvalue(forkey:)'
source_url: 'https://developer.apple.com/documentation/storekit/skoverlay/appclipconfiguration/additionalvalue(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skoverlay/appclipconfiguration/additionalvalue%28forkey%3A%29.json'
content_hash: 'sha256:6eb03b58e5c843c1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [SKOverlay](../../skoverlay.md) · [AppClipConfiguration](../appclipconfiguration.md)

# additionalValue(forKey:)

<sub>Instance Method</sub>

Returns the object associated with the key.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func additionalValue(forKey key: String) -> Any?
```

## Parameters

- `key` — The string that identifies an additional value.

## Return Value

The associated value of the key.

## Discussion

Additional values are values you use to verify and associate an app installation with an ad campaign. For more information, see [SKAdNetwork](../../skadnetwork.md).

## See Also

### Verifying Advertising Campaigns

- [campaignToken](campaigntoken.md) — A token you use to represent an ad campaign and measure its effectiveness.
- [providerToken](providertoken.md) — A token that represents the provider of an app promotion campaign, and that you use to measure the campaign’s effectiveness.
- [- setAdditionalValue:forKey:](<setadditionalvalue(__forkey_).md>) — Sets an additional value for a key, such as a value for measuring the effectiveness of an ad campaign.
