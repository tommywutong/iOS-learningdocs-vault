---
title: 'beginRefundRequest(for:in:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/transaction/beginrefundrequest(for:in:)-65tph'
source_url: 'https://developer.apple.com/documentation/storekit/transaction/beginrefundrequest(for:in:)-65tph'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/beginrefundrequest%28for%3Ain%3A%29-65tph.json'
content_hash: 'sha256:7644a97208443516'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# beginRefundRequest(for:in:)

<sub>Type Method</sub>

Presents the refund request sheet for the specified transaction in a window scene.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor static func beginRefundRequest(for transactionID: UInt64, in scene: UIWindowScene) async throws -> Transaction.RefundRequestStatus
```

## Parameters

- `transactionID` — The identifier of the transaction the user is requesting a refund for.

- `scene` — The [UIWindowScene](../../uikit/uiwindowscene.md) that the system displays the sheet on.

## Return Value

[RefundRequestStatus](refundrequeststatus.md)

## Discussion

Call this function from account settings or a help menu to enable customers to request a refund for an in-app purchase within your app. When you call this function, the system displays a refund sheet with the customer’s purchase details and a list of reason codes for the customer to choose from. For design guidance, see [Human Interface Guidelines \> In-app purchase \> Providing help with in-app purchases](https://developer.apple.com/design/human-interface-guidelines/in-app-purchase/overview/introduction/#providing-help-with-in-app-purchases).

When a customer requests a refund for consumable in-app purchases through your app, the App Stores sends a `CONSUMPTION_REQUEST` [notificationType](../../appstoreservernotifications/notificationtype.md) to your server. If the customer provided consent, respond by sending consumption data to the App Store using the [Send Consumption Information](../../appstoreserverapi/send-consumption-information.md) endpoint. If not, don’t respond to the `CONSUMPTION_REQUEST` notification.

The App Store takes up to 48 hours to either approve or deny a refund.

For information about setting up your server to receive notifications, see [Enabling App Store Server Notifications](../enabling-app-store-server-notifications.md).

> [!note] Note
> If your app uses SwiftUI, use [refundRequestSheet(for:isPresented:onDismiss:)](<../../swiftui/view/refundrequestsheet(for_ispresented_ondismiss_).md>) instead. For example usage, see [Food Truck: Building a SwiftUI multiplatform app](../../swiftui/food-truck-building-a-swiftui-multiplatform-app.md).

### Test refund requests

The sandbox environment and StoreKit Testing in Xcode both support testing refund requests. For more information, see [Testing refund requests](../testing-refund-requests.md).

## See Also

### Requesting refunds

- [Testing refund requests](../testing-refund-requests.md) — Test your app’s implementation of refund requests, and your app’s and server’s handling of approved and declined refunds.
- [beginRefundRequest(in:)](<beginrefundrequest(in_)-9k0pj.md>) — Presents the refund request sheet for the transaction in a window scene.
- [beginRefundRequest(in:)](<beginrefundrequest(in_)-63bvd.md>) — Presents the refund request sheet for the transaction in a view controller.
- [beginRefundRequest(for:in:)](<beginrefundrequest(for_in_)-9mscy.md>) — Presents the refund request sheet for the specified transaction in a view controller.
- [RefundRequestError](refundrequesterror.md) — The error codes for refund requests.
- [RefundRequestStatus](refundrequeststatus.md) — The status codes for refund requests.
