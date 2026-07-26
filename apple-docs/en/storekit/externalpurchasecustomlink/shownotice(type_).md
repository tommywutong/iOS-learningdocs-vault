---
title: 'showNotice(type:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.1+, iPadOS 18.1+, macOS 15.1+, tvOS 18.1+, visionOS 2.1+, watchOS 11.1+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/externalpurchasecustomlink/shownotice(type:)'
source_url: 'https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/shownotice(type:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/externalpurchasecustomlink/shownotice%28type%3A%29.json'
content_hash: 'sha256:a4be8e3109d1fab6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ExternalPurchaseCustomLink](../externalpurchasecustomlink.md)

# showNotice(type:)

<sub>Type Method</sub>

Displays the system disclosure notice sheet and asks the customer whether to continue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func showNotice(type: ExternalPurchaseCustomLink.NoticeType) async throws -> ExternalPurchaseCustomLink.NoticeResult
```

## Parameters

- `type` — An [NoticeType](noticetype.md) value you select that determines the disclosure sheet the system displays.

## Return Value

Returns [ExternalPurchaseCustomLink.NoticeResult.continued](noticeresult/continued.md) to indicate the customer chooses to continue, or [ExternalPurchaseCustomLink.NoticeResult.cancelled](noticeresult/cancelled.md) to indicate the customer chooses not to continue to view external purchases. This method throws an error if your app isn’t eligible, at runtime, to use this API.

## Discussion

Use this method if your app configures the [SKExternalPurchaseCustomLinkRegions](../../bundleresources/information-property-list/skexternalpurchasecustomlinkregions.md) or [SKExternalPurchaseLinkStreamingRegions](../../bundleresources/information-property-list/skexternalpurchaselinkstreamingregions.md) property list keys.

Call this method to display the system disclosure sheet before your app continues to communicate and promote offers for purchase in a distribution channel of your choice. Call this method in response to a deliberate customer action, such as tapping a button.

Select the notice type based on how your app communicates the offers if the customer chooses to continue:

- Use [ExternalPurchaseCustomLink.NoticeType.browser](noticetype/browser.md) if the app goes to the background, and promotes offers in a destination outside of the app.
- Use [ExternalPurchaseCustomLink.NoticeType.withinApp](noticetype/withinapp.md) if the app promotes offers in a web view or native experience within the app.

Continue to communicate and promote offers if [showNotice(type:)](<shownotice(type_).md>) returns [ExternalPurchaseCustomLink.NoticeResult.continued](noticeresult/continued.md); otherwise don’t continue.

For example code that calls this method, see [ExternalPurchaseCustomLink](../externalpurchasecustomlink.md).

## See Also

### Displaying the disclosure sheet

- [NoticeType](noticetype.md) — The custom link out style that informs the type of disclosure notice to display.
- [NoticeResult](noticeresult.md) — The result of showing the disclosure notice.
