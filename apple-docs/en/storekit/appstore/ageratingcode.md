---
title: ageRatingCode
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.2+, iPadOS 26.2+, macOS 26.2+, tvOS 26.2+, visionOS 26.2+, watchOS 26.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/appstore/ageratingcode
source_url: 'https://developer.apple.com/documentation/storekit/appstore/ageratingcode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/appstore/ageratingcode.json'
content_hash: 'sha256:4254f5d6d4c78172'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppStore](../appstore.md)

# ageRatingCode

<sub>Type Property</sub>

The current age rating code for your app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var ageRatingCode: Int? { get async }
```

## Return Value

An integer representing the current age rating code, or `nil` if the age rating is unavailable.

## Discussion

Use this property to fetch the age rating for your app and compare it with the last known age rating to check if it has changed.

The following is an example of getting the age rating for an app:

```swift
func getAgeRatingCode() async -> Int? {
    guard let ageRatingCode = await AppStore.ageRatingCode else {
        print("Age rating code unavailable")
        return nil
    }
    return ageRatingCode
}
```

If your app’s age rating has changed, consider informing parents or guardians by using the [Significant Change API](https://developer.apple.com/documentation/PermissionKit/SignificantAppUpdateTopic).
