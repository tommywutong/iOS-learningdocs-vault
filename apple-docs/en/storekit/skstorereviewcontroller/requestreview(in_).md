---
title: 'requestReview(in:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+（18.0 起废弃）, iPadOS 14.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skstorereviewcontroller/requestreview(in:)'
source_url: 'https://developer.apple.com/documentation/storekit/skstorereviewcontroller/requestreview(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skstorereviewcontroller/requestreview%28in%3A%29.json'
content_hash: 'sha256:698800697c44e88e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKStoreReviewController](../skstorereviewcontroller.md)

# requestReview(in:)

<sub>Type Method</sub>

Tells StoreKit to ask the customer to rate or review the app, if appropriate, using the specified scene.

> [!warning] Deprecated
> Use AppStore.requestReview(in:).

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class func requestReview(in windowScene: UIWindowScene)
```

## Parameters

- `windowScene` — The window scene that StoreKit uses to present the rating and review request interface.

## Discussion

When you call this method in your shipping app and the system displays a rating and review request view, the system handles the entire process for you. Although you normally call this method when it makes sense in the user experience flow of your app, App Store policy governs the actual display of a rating and review request view. When your app calls this API, StoreKit uses the following criteria::

- If the person hasn’t rated or reviewed your app on this device, StoreKit displays the ratings and review request a maximum of three times within a 365-day period.
- If the person has rated or reviewed your app on this device, StoreKit displays the ratings and review request if the app version is new, and if more than 365 days have passed since the person’s previous review.

> [!note] Note
> Because this method may not present an alert, don’t call [+ requestReview](<requestreview().md>) or [+ requestReviewInScene:](<requestreview(in_).md>) in response to a button tap or other user action.

It’s up to your app to decide on the best timing for requesting reviews. For design guidance, see Human Interface Guidelines \> [Ratings and reviews](https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews).

### Test review requests

When your app calls this method while it’s in development mode, StoreKit always displays the rating and review request view, so you can test the user interface and experience. However, this method has no effect in apps that you distribute for beta testing using TestFlight.

### Provide a persistent link to your product page (optional)

Your customers can review your app at any time on the App Store. To make it easier for people to leave reviews, you may include a persistent link to your App Store product page in your app’s settings or configuration screens. Append the query parameter `action=write-review` to your product page URL to automatically open the App Store page where users can write a review.

## See Also

### Indicating an appropriate time for a review

- [+ requestReview](<requestreview().md>) — Tells StoreKit to ask the customer to rate or review your app, if appropriate. _(deprecated)_
