---
title: 'setAdditionalValue(_:forKey:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/storekit/skoverlay/appconfiguration/setadditionalvalue(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/storekit/skoverlay/appconfiguration/setadditionalvalue(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skoverlay/appconfiguration/setadditionalvalue%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:07f5ecf3deea3689'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [SKOverlay](../../skoverlay.md) · [AppConfiguration](../appconfiguration.md)

# setAdditionalValue(_:forKey:)

<sub>Instance Method</sub>

Sets an additional value for a key; for example, a value for measuring the effectiveness of an ad campaign.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setAdditionalValue(_ value: Any?, forKey key: String)
```

## Parameters

- `value` — The value to associate with the `key`.

- `key` — The string that identifies an additional value.

## Discussion

Set additional values to verify and associate an app installation with an ad campaign. For more information, see [SKAdNetwork](../../skadnetwork.md).

## See Also

### Verifying Advertising Campaigns

- [campaignToken](campaigntoken.md) — A token you use to represent an ad campaign and measure its effectiveness.
- [providerToken](providertoken.md) — A token that represents the provider of an app promotion campaign, and that you use to measure the campaign’s effectiveness.
- [- additionalValueForKey:](<additionalvalue(forkey_).md>) — Returns the object associated with the key.
