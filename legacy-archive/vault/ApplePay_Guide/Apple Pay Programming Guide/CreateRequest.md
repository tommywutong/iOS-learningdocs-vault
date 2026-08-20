---
title: Apple Pay Programming Guide
apple_id: TP40014764
resource_type: Guide
platform: watchOS|iOS
topic: null
technology: PassKit
published: '2017-03-16'
source_url: https://developer.apple.com/library/archive/ApplePay_Guide/CreateRequest.html
archived_at: '2026-07-15T03:48:35.957213Z'
---
> 导航：[总目录](../../README.md) · [ApplePay_Guide](../../_indexes/ApplePay_Guide.md) · [Apple Pay Programming Guide](index.md)



## Creating Payment Requests

Payment requests are instances of the [PKPaymentRequest](https://developer.apple.com/documentation/passkit/pkpaymentrequest) class. A payment request consists of a list of summary items that describe to the user what is being paid for, a list of available shipping methods, a description of what shipping information the user needs to provide, and information about the merchant and the payment processor.

### Decide Whether the User Can Make Payments

Before creating a payment request, determine whether the user will be able to make payments using a network that you support by calling the [canMakePaymentsUsingNetworks:](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller/1616187-canmakepaymentsusingnetworks) method of the [PKPaymentAuthorizationViewController](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller) class. To check whether Apple Pay is supported by this device’s hardware and parental controls, use the [canMakePayments](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller/1616192-canmakepayments) method.

> [!NOTE]
> 

If `canMakePayments` returns `NO``false`, the device does not support Apple Pay. Do not display the Apple Pay button. Instead, fall back to another method of payment.

If `canMakePayments` returns `YES``true` but `canMakePaymentsUsingNetworks:` returns `NO``false`, the device supports Apple Pay, but the user has not added a card for any of the requested networks. You can, optionally, display a payment setup button, prompting the user to set up his or her card. As soon as the user taps this button, initiate the process of setting up a new card (for example, by calling the [openPaymentSetup](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617100-openpaymentsetup) method).

Otherwise, as soon as the user presses the Apple Pay button, you must begin the payment authorization process. Do not ask the user to perform any other tasks before presenting the payment request. For example, if the user needs to enter a discount code, you must ask for the code before he or she presses the Apple Pay button.

To create an Apple Pay–branded button for initiating payment request on iOS 8.3 or later, use the [PKPaymentButton](https://developer.apple.com/documentation/passkit/pkpaymentbutton) class. For additional guidelines on using Apple Pay buttons and payment marks, see [Apple Pay](https://developer.apple.com/ios/human-interface-guidelines/technologies/apple-pay/) in [iOS Human Interface Guidelines](https://developer.apple.com/ios/human-interface-guidelines/).

### Bridging from Web-Based Interfaces

If your app uses a web-based interface for purchasing goods and services, you must move the request from the web interface to native iOS code before processing an Apple Pay transaction. Listing 3-1 shows the steps needed to process requests from a web view.

__Listing 3-1__Buying items from a web view

1. `// Called when the web view tries to load "myShoppingApp:buyItem"`
2. `-(void)webView:(nonnull WKWebView *)webView`
3. `decidePolicyForNavigationAction:(nonnull WKNavigationAction *)navigationAction`
4. `decisionHandler:(nonnull void (^)(WKNavigationActionPolicy))decisionHandler {`
6. `// Get the URL for the selected link.`
7. `NSURL *URL = navigationAction.request.URL;`
9. `// If the scheme and resource specifier match those defined by your app,`
10. `// handle the payment in native iOS code.`
11. `if ([URL.scheme isEqualToString:@"myShoppingApp"] &&`
12. `[URL.resourceSpecifier isEqualToString:@"buyItem"]) {`
14. `// Create and present the payment request here.`
16. `// The web view ignores the link.`
17. `decisionHandler(WKNavigationActionPolicyCancel);`
18. `}`
20. `// Otherwise the web view loads the link.`
21. `decisionHandler(WKNavigationActionPolicyAllow);`
22. `}`

### Payment Requests Include Currency and Region Information

All of the summary amounts in a payment request use the same currency, which is specified using the [currencyCode](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619248-currencycode) property of `PKPaymentRequest`. Use a three-character ISO currency code, such as `USD`.

The payment request’s country code indicates the country where the purchase took place or where the purchase will be processed. Use a two-character ISO country code, such as `US`.

The merchant ID you set in a payment request must match one of the merchant IDs in your app’s entitlement.

1. `request.currencyCode = @"USD";`
2. `request.countryCode = @"US";`
3. `request.merchantIdentifier = @"merchant.com.example";`

### Payment Requests Have a List of Payment Summary Items

Payment summary items, represented by the [PKPaymentSummaryItem](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem) class, describe the different parts of the payment request to the user. Use a small number of summary items—typically the subtotal, any discount, the shipping, the tax, and the grand total. If you do not have any additional fees (for example, shipping or tax), just use the purchase’s total. Provide granular details of the item-by-item costs elsewhere in your app.

Each summary item has a label and an amount, as shown in Listing 3-2. The label is a user-readable description of what the item summarizes. The amount is the corresponding payment amount. All of the amounts in a payment request use the currency specified in the payment request. For a discount or a coupon, set the amount to a negative number.

__Listing 3-2__Creating a payment summary item

1. `// 12.75 subtotal`
2. `NSDecimalNumber *subtotalAmount = [NSDecimalNumber decimalNumberWithMantissa:1275 exponent:-2 isNegative:NO];`
3. `self.subtotal = [PKPaymentSummaryItem summaryItemWithLabel:@"Subtotal" amount:subtotalAmount];`
5. `// 2.00 discount`
6. `NSDecimalNumber *discountAmount = [NSDecimalNumber decimalNumberWithMantissa:200 exponent:-2 isNegative:YES];`
7. `self.discount = [PKPaymentSummaryItem summaryItemWithLabel:@"Discount" amount:discountAmount];`

> [!NOTE]
> 

The last payment summary item in the list is the grand total. Calculate the grand total amount by adding the amounts of all the other summary items. The grand total is displayed differently from the other summary items: Use your company’s name as its label, and use the total of all the other summary items’ amounts as its amount. Add the payment summary items to the payment request using the [paymentSummaryItems](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619231-paymentsummaryitems) property.

If you do not know the actual cost when the payment is authorized (for example, a taxi fare), make a subtotal summary item using the [PKPaymentSummaryItemTypePending](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitemtype/pkpaymentsummaryitemtypepending) type and a `0.0` amount. For the grand total, use a positive non-zero amount and the [PKPaymentSummaryItemTypePending](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitemtype/pkpaymentsummaryitemtypepending) type. The system then shows the cost as pending without a numeric amount.

> [!NOTE]
> 

1. `// 10.75 grand total`
2. `NSDecimalNumber *totalAmount = [NSDecimalNumber zero];`
3. `totalAmount = [totalAmount decimalNumberByAdding:subtotalAmount];`
4. `totalAmount = [totalAmount decimalNumberByAdding:discountAmount];`
5. `self.total = [PKPaymentSummaryItem summaryItemWithLabel:@"My Company Name" amount:totalAmount];`
7. `self.summaryItems = @[self.subtotal, self.discount, self.total];`
8. `request.paymentSummaryItems = self.summaryItems;`

### A Shipping Method Is a Special Payment Summary Item

Create an instance of [PKShippingMethod](https://developer.apple.com/documentation/passkit/pkshippingmethod) for each available shipping method. Just like other payment summary items, shipping methods have a user-readable label such as Standard Shipping or Next Day Shipping, and an amount that is the shipping cost. Unlike other summary items, shipping methods also have a [detail](https://developer.apple.com/documentation/passkit/pkshippingmethod/1619306-detail) property—such as “Arrives by July 29” or “Ships in 24 hours”—that explains the difference between shipping methods.

To distinguish shipping methods in your delegate methods, use the [identifier](https://developer.apple.com/documentation/passkit/pkshippingmethod/1619232-identifier) property. This property is used only by your app—the framework treats it as an opaque value and it doesn’t appear in the UI. Assign a unique identifier for each shipping method when you create it. For ease of debugging, use a brief or abbreviated string, such as “discount,” “standard,” or “next-day.”

Some shipping methods aren’t available in all areas or have different costs for different addresses. You can update this information when the user selects a shipping address or method, as described in [Your Delegate Updates Shipping Methods and Costs](Authorization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2donrufvbuqnbnknlte).

### Indicating Your Supported Payment Processing Mechanisms

Indicate which payment networks you support by populating the [supportedNetworks](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619329-supportednetworks) property with an array of string constants. Indicate which payment processing protocols you support by setting a value for the [merchantCapabilities](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619257-merchantcapabilities) property. You must support 3DS; specify EMV only if you support Apple Pay in China.

The merchant capabilities are bit masks and are combined as follows:

1. `request.supportedNetworks = @[PKPaymentNetworkAmex, PKPaymentNetworkDiscover, PKPaymentNetworkMasterCard, PKPaymentNetworkVisa];`
3. `// Supports 3DS only`
4. `request.merchantCapabilities = PKMerchantCapability3DS;`
6. `// Supports both 3DS and EMV (add EMV only if you support Apple Pay in China)`
7. `request.merchantCapabilities = PKMerchantCapability3DS | PKMerchantCapabilityEMV;`

### Indicating What Shipping and Billing Information Is Needed

Populate the [requiredBillingAddressFields](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619265-requiredbillingaddressfields) and [requiredShippingAddressFields](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619228-requiredshippingaddressfields) properties of the payment authorization view controller to indicate what billing and shipping information is needed. When you present this view controller, it prompts the users to supply the requested billing and shipping information. The field constants are combined as follows to set values for these properties:

1. `request.requiredBillingAddressFields = PKAddressFieldEmail;`
2. `request.requiredBillingAddressFields = PKAddressFieldEmail | PKAddressFieldPostalAddress;`

> [!NOTE]
> 

If you have up-to-date billing and shipping contact information, you can set those on the payment request. Apple Pay uses this information by default; however, the user can still choose other contact information as part of the payment authorization process.

1. `PKContact *contact = [[PKContact alloc] init];`
3. `NSPersonNameComponents *name = [[NSPersonNameComponents alloc] init];`
4. `name.givenName = @"John";`
5. `name.familyName = @"Appleseed";`
7. `contact.name = name;`
9. `CNMutablePostalAddress *address = [[CNMutablePostalAddress alloc] init];`
10. `address.street = @"1234 Laurel Street";`
11. `address.city = @"Atlanta";`
12. `address.state = @"GA";`
13. `address.postalCode = @"30303";`
15. `contact.postalAddress = address;`
17. `request.shippingContact = contact;`

> [!NOTE]
> 

### Storing Additional Information

To store information about the payment request that is specific to your app, such as in a shopping cart identifier, use the [applicationData](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619298-applicationdata) property. This property is treated as an opaque value by the system. A hash of the application data appears in the payment token after the user authorizes the payment request.

[Configuring Your Environment](Configuration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2donrufvbuqmrnknltc)

[Authorizing Payments](Authorization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2donrufvbuqnbnknltg)
