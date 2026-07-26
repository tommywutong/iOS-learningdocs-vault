---
title: requestReview()
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.3+（14.0 起废弃）, iPadOS 10.3+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, macOS 10.14+（15.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skstorereviewcontroller/requestreview()
source_url: 'https://developer.apple.com/documentation/storekit/skstorereviewcontroller/requestreview()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skstorereviewcontroller/requestreview%28%29.json'
content_hash: 'sha256:d234421562f8353d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKStoreReviewController](../skstorereviewcontroller.md)

# requestReview()

<sub>Type Method</sub>

Tells StoreKit to ask the customer to rate or review your app, if appropriate.

> [!warning] Deprecated
> For iOS, iPadOS, and apps built with Mac Catalyst, use [+ requestReviewInScene:](<requestreview(in_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class func requestReview()
```

## Discussion

Although you normally call this method when it makes sense in the user experience flow of your app, App Store policy governs the actual display of a rating and review request view. Because this method may not present an alert, it isn’t appropriate to call [+ requestReview](<requestreview().md>) or [+ requestReviewInScene:](<requestreview(in_).md>) in response to a button tap or other user action.

> [!note] Note
> When you call this method while your app is in development mode, a rating and review request view is always displayed so you can test the user interface and experience. However, this method has no effect when you call it in an app that you distribute using TestFlight.

When you call this method in your shipping app and the system displays a rating and review request view, the system handles the entire process for you. In addition, you can continue to include a persistent link in the settings or configuration screens of your app that links to your App Store product page. To automatically open a page on which users can write a review in the App Store, append the query parameter `action=write-review` to your product URL.

## See Also

### Indicating an appropriate time for a review

- [+ requestReviewInScene:](<requestreview(in_).md>) — Tells StoreKit to ask the customer to rate or review the app, if appropriate, using the specified scene. _(deprecated)_
