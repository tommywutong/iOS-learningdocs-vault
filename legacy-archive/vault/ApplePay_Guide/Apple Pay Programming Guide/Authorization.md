---
title: Apple Pay Programming Guide
apple_id: TP40014764
resource_type: Guide
platform: watchOS|iOS
topic: null
technology: PassKit
published: '2017-03-16'
source_url: https://developer.apple.com/library/archive/ApplePay_Guide/Authorization.html
archived_at: '2026-07-15T03:48:34.071830Z'
---
> 导航：[总目录](../../README.md) · [ApplePay_Guide](../../_indexes/ApplePay_Guide.md) · [Apple Pay Programming Guide](index.md)



## Authorizing Payments

The payment authorization process is a cooperative effort between the payment authorization view controller and its delegate. A payment authorization view controller does two things: It lets the user select the billing and shipping information that is needed by a payment request, and it lets the user authorize the payment to be made. The delegate methods are called when the user interacts with the view controller so that your app can update the information shown—for example, to update the shipping price when a shipping address is selected. The delegate is also called after the user authorizes the payment request.

> [!NOTE]
> 

All of the delegate methods called during the authorization process are passed a completion block as one of their arguments. The payment authorization view controller waits for its delegate to finish responding to one method (by calling the completion block) before it calls any other delegate methods. The [paymentAuthorizationViewControllerDidFinish:](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616180-paymentauthorizationviewcontroll) method is the only exception: It doesn’t take a completion block, and it can be called at any time.

The completion blocks take an argument that lets you specify the current status of the transaction based on the information that’s available. If there are no problems with the transaction, you pass the value `PKPaymentAuthorizationStatusSuccess`; otherwise, you pass a value that identifies the problem.

To create an instance of the [PKPaymentAuthorizationViewController](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller) class, pass the payment request to the view controller’s initializer. Set a delegate for the view controller, and then present it.

> [!NOTE]
> 

1. `PKPaymentAuthorizationViewController *viewController = [[PKPaymentAuthorizationViewController alloc] initWithPaymentRequest:request];`
2. `if (!viewController) { /* ... Handle error ... */ }`
3. `viewController.delegate = self;`
4. `[self presentViewController:viewController animated:YES completion:nil];`

As the user interacts with the view controller, the view controller calls its delegate methods.

> [!NOTE]
> 

### Your Delegate Updates Shipping Methods and Costs

When the user provides shipping information, the authorization view controller calls your delegate’s [paymentAuthorizationViewController:didSelectShippingContact:completion:](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616198-paymentauthorizationviewcontroll) and [paymentAuthorizationViewController:didSelectShippingMethod:completion:](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616186-paymentauthorizationviewcontroll) methods. Use these methods to update the payment request based on the new information.

1. `- (void) paymentAuthorizationViewController:(PKPaymentAuthorizationViewController *)controller`
2. `didSelectShippingContact:(CNContact *)contact`
3. `completion:(void (^)(PKPaymentAuthorizationStatus, NSArray *, NSArray *))completion`
4. `{`
5. `self.selectedContact = contact;`
6. `[self updateShippingCost];`
7. `NSArray *shippingMethods = [self shippingMethodsForContact:contact];`
8. `completion(PKPaymentAuthorizationStatusSuccess, shippingMethods, self.summaryItems);`
9. `}`
11. `- (void) paymentAuthorizationViewController:(PKPaymentAuthorizationViewController *)controller`
12. `didSelectShippingMethod:(PKShippingMethod *)shippingMethod`
13. `completion:(void (^)(PKPaymentAuthorizationStatus, NSArray *))completion`
14. `{`
15. `self.selectedShippingMethod = shippingMethod;`
16. `[self updateShippingCost];`
17. `completion(PKPaymentAuthorizationStatusSuccess, self.summaryItems);`
18. `}`

> [!NOTE]
> 

### A Payment Token Is Created When a Payment Is Authorized

When the user authorizes a payment request, the framework creates a payment token by coordinating with Apple’s server and the Secure Element. You send this payment token to your server in the [paymentAuthorizationViewController:didAuthorizePayment:completion:](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616195-paymentauthorizationviewcontroll) delegate method, along with any other information you need to process the purchase—for example, the shipping address and a shopping cart identifier. The process happens as follows:

- The framework sends the payment request to the Secure Element. Only the Secure Element has access to the tokenized device-specific payment card numbers.
- The Secure Element puts together payment data for the specified card and merchant, encrypts it so that only Apple can read it, and sends it to the framework. The framework then sends the payment data to Apple’s server.
- Apple’s server reencrypts the payment data using your Payment Processing certificate. The token can only be read by you and the people with whom you have shared your Payment Processing certificate. The server then signs the payment token, and returns it to the device.
- The framework passes the token to your delegate by calling its [paymentAuthorizationViewController:didAuthorizePayment:completion:](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616195-paymentauthorizationviewcontroll) method. Your delegate sends the token to your server.

The actions on your server vary depending on whether you process your own payments or work with a payment platform. In both cases, your server handles the order and sends a status back to the device, which your delegate passes to its completion handler, as described in [Processing Payments](ProcessPayment.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2donrufvbuqnjnknlti).

1. `- (void) paymentAuthorizationViewController:(PKPaymentAuthorizationViewController *)controller`
2. `didAuthorizePayment:(PKPayment *)payment`
3. `completion:(void (^)(PKPaymentAuthorizationStatus))completion`
4. `{`
5. `NSError *error;`
6. `ABMultiValueRef addressMultiValue = ABRecordCopyValue(payment.billingAddress, kABPersonAddressProperty);`
7. `NSDictionary *addressDictionary = (__bridge_transfer NSDictionary *) ABMultiValueCopyValueAtIndex(addressMultiValue, 0);`
8. `NSData *json = [NSJSONSerialization dataWithJSONObject:addressDictionary options:NSJSONWritingPrettyPrinted error: &error];`
10. `// ... Send payment token, shipping and billing address, and order information to your server ...`
12. `PKPaymentAuthorizationStatus status; // From your server`
13. `completion(status);`
14. `}`

### Your Delegate Dismisses the Payment Authorization View Controller

After the framework displays the transaction’s status, the authorization view controller calls your delegate’s [paymentAuthorizationViewControllerDidFinish:](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616180-paymentauthorizationviewcontroll) method. In your implementation, dismiss the authorization view controller and then display your own app-specific order-confirmation page.

1. `- (void) paymentAuthorizationViewControllerDidFinish:(PKPaymentAuthorizationViewController *)controller`
2. `{`
3. `[controller dismissViewControllerAnimated:YES completion:nil];`
4. `}`

[Creating Payment Requests](CreateRequest.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2donrufvbuqmznknlte)

[Processing Payments](ProcessPayment.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2donrufvbuqnjnknlti)
