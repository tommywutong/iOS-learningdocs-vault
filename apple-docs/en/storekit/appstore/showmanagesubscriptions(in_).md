---
title: 'showManageSubscriptions(in:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/appstore/showmanagesubscriptions(in:)'
source_url: 'https://developer.apple.com/documentation/storekit/appstore/showmanagesubscriptions(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/appstore/showmanagesubscriptions%28in%3A%29.json'
content_hash: 'sha256:e88e014661437b61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppStore](../appstore.md)

# showManageSubscriptions(in:)

<sub>Type Method</sub>

Presents the App Store sheet for managing subscriptions.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor static func showManageSubscriptions(in scene: UIWindowScene) async throws
```

## Parameters

- `scene` — The [UIWindowScene](../../uikit/uiwindowscene.md) that the system displays the sheet on.

## Discussion

Use this function to display the manage subscriptions sheet within your app. Consider adding a manage subscriptions option to your app. For design guidance on supporting this functionality, see [Human Interface Guidelines \> In-App Purchase \> Helping People Manage Their Subscriptions](https://developer.apple.com/design/human-interface-guidelines/in-app-purchase/overview/auto-renewable-subscriptions/#helping-people-manage-their-subscriptions).

The [showManageSubscriptions(in:)](<showmanagesubscriptions(in_).md>) function presents a manage subscription sheet that’s the same as what customers can view in their account settings in the App Store app or by choosing Settings \> Apple Account \> Subscriptions on an iOS or iPadOS device. The sheet displays the customer’s currently active subscription for your app and the options to view, upgrade, downgrade, or cancel their subscription.

If you’re using SwiftUI, call the [manageSubscriptionsSheet(isPresented:)](<../../swiftui/view/managesubscriptionssheet(ispresented_).md>)view modifier.

Avoid showing the user interface for this feature in Mac apps built with Mac Catalyst and on iOS apps running on Mac computers with Apple silicon because this sheet isn’t supported in macOS.

- In Mac apps built with Mac Catalyst, enclose the code in a compilation conditional block that uses the `targetEnvironment():` platform condition. For more information on Mac Catalyst, see [Creating a Mac version of your iPad app](../../uikit/creating-a-mac-version-of-your-ipad-app.md).
- For iOS apps running on Apple silicon, if [isiOSAppOnMac](../../foundation/processinfo/isiosapponmac.md) is `true,` avoid showing the user interface for this feature.

### Test managing subscriptions

Test the managing subscriptions functionality in the sandbox environment and StoreKit testing in Xcode. For more information about testing, see [Testing at all stages of development with Xcode and the sandbox](../testing-at-all-stages-of-development-with-xcode-and-the-sandbox.md) and [Setting up StoreKit Testing in Xcode](../../xcode/setting-up-storekit-testing-in-xcode.md).

## See Also

### Managing subscriptions

- [showManageSubscriptions(in:subscriptionGroupID:)](<showmanagesubscriptions(in_subscriptiongroupid_).md>) — Presents the App Store sheet for managing subscriptions for a subscription group.
