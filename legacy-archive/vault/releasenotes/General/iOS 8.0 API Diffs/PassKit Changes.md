---
title: iOS 8.0 API Diffs
apple_id: TP40014455
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS80APIDiffs/frameworks/PassKit.html
archived_at: '2026-07-18T02:55:59.850617Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.0 API Diffs](iOS%207.1%20to%20iOS%208.0%20API%20Differences.md)


# PassKit Changes

## PassKit

PKAddPassesViewController.hAdded [+[PKAddPassesViewController canAddPasses]](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller/1619212-canaddpasses)Modified [-[PKAddPassesViewController initWithPass:]](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller/1619251-initwithpass)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithPass:(id)pass ``` |
| To | ``` - (instancetype)initWithPass:(id)pass ``` |

Modified [-[PKAddPassesViewController initWithPasses:]](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller/1619217-initwithpasses)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithPasses:(NSArray *)passes ``` |
| To | ``` - (instancetype)initWithPasses:(NSArray *)passes ``` |

Modified [-[PKAddPassesViewControllerDelegate addPassesViewControllerDidFinish:]](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontrollerdelegate/1619236-addpassesviewcontrollerdidfinish)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

PKError.hRemoved PKErrorCodeRemoved PKErrorDomainRemoved PKErrorNotEntitledRemoved PKErrorPassSignatureInvalidRemoved PKErrorPermissionDeniedRemoved PKErrorUnknownAdded [PKNotEntitledError](https://developer.apple.com/documentation/passkit/pkpasskiterrorcode/pknotentitlederror)Modified [PKInvalidDataError](https://developer.apple.com/documentation/passkit/pkpasskiterrorcode/pkinvaliddataerror)

|  | Header |
| --- | --- |
| From | PassKit/PKPass.h |
| To | PassKit/PKError.h |

Modified [PKInvalidSignature](https://developer.apple.com/documentation/passkit/pkpasskiterror/code/invalidsignature)

|  | Header |
| --- | --- |
| From | PassKit/PKPass.h |
| To | PassKit/PKError.h |

Modified [PKPassKitErrorCode](https://developer.apple.com/documentation/passkit/pkpasskiterror/code)

|  | Header |
| --- | --- |
| From | PassKit/PKPass.h |
| To | PassKit/PKError.h |

Modified [PKPassKitErrorDomain](https://developer.apple.com/documentation/passkit/pkpasskiterrordomain)

|  | Header |
| --- | --- |
| From | PassKit/PKPass.h |
| To | PassKit/PKError.h |

Modified [PKUnknownError](https://developer.apple.com/documentation/passkit/pkpasskiterror/code/unknownerror)

|  | Header |
| --- | --- |
| From | PassKit/PKPass.h |
| To | PassKit/PKError.h |

Modified [PKUnsupportedVersionError](https://developer.apple.com/documentation/passkit/pkpasskiterror/code/unsupportedversionerror)

|  | Header |
| --- | --- |
| From | PassKit/PKPass.h |
| To | PassKit/PKError.h |

PKObject.h (Added)Added [PKObject](https://developer.apple.com/documentation/passkit/pkobject)PKPass.hAdded [PKPass.passType](https://developer.apple.com/documentation/passkit/pkpass/1618760-passtype)Added [PKPass.paymentPass](https://developer.apple.com/documentation/passkit/pkpass/1618784-paymentpass)Added [PKPassType](https://developer.apple.com/documentation/passkit/pkpasstype)Added [PKPassTypeAny](https://developer.apple.com/documentation/passkit/pkpasstype/any)Added [PKPassTypeBarcode](https://developer.apple.com/documentation/passkit/pkpasstype/barcode)Added [PKPassTypePayment](https://developer.apple.com/documentation/passkit/pkpasstype/payment)Modified [PKPass](https://developer.apple.com/documentation/passkit/pkpass)

|  | Superclasses |
| --- | --- |
| From | NSObject |
| To | PKObject |

Modified [-[PKPass initWithData:error:]](https://developer.apple.com/documentation/passkit/pkpass/1618792-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithData:(NSData *)data error:(NSError **)error ``` |
| To | ``` - (instancetype)initWithData:(NSData *)data error:(NSError **)error ``` |

Modified [PKInvalidDataError](https://developer.apple.com/documentation/passkit/pkpasskiterrorcode/pkinvaliddataerror)

|  | Header |
| --- | --- |
| From | PassKit/PKPass.h |
| To | PassKit/PKError.h |

Modified [PKInvalidSignature](https://developer.apple.com/documentation/passkit/pkpasskiterror/code/invalidsignature)

|  | Header |
| --- | --- |
| From | PassKit/PKPass.h |
| To | PassKit/PKError.h |

Modified [PKPassKitErrorCode](https://developer.apple.com/documentation/passkit/pkpasskiterror/code)

|  | Header |
| --- | --- |
| From | PassKit/PKPass.h |
| To | PassKit/PKError.h |

Modified [PKPassKitErrorDomain](https://developer.apple.com/documentation/passkit/pkpasskiterrordomain)

|  | Header |
| --- | --- |
| From | PassKit/PKPass.h |
| To | PassKit/PKError.h |

Modified [PKUnknownError](https://developer.apple.com/documentation/passkit/pkpasskiterror/code/unknownerror)

|  | Header |
| --- | --- |
| From | PassKit/PKPass.h |
| To | PassKit/PKError.h |

Modified [PKUnsupportedVersionError](https://developer.apple.com/documentation/passkit/pkpasskiterror/code/unsupportedversionerror)

|  | Header |
| --- | --- |
| From | PassKit/PKPass.h |
| To | PassKit/PKError.h |

PKPassLibrary.hAdded [-[PKPassLibrary activatePaymentPass:withActivationCode:completion:]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617079-activate)Added [-[PKPassLibrary activatePaymentPass:withActivationData:completion:]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617088-activate)Added [+[PKPassLibrary isPaymentPassActivationAvailable]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617108-ispaymentpassactivationavailable)Added [-[PKPassLibrary passesOfType:]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617074-passes)PKPayment.h (Added)Added [PKPayment](https://developer.apple.com/documentation/passkit/pkpayment)Added [PKPayment.billingAddress](https://developer.apple.com/documentation/passkit/pkpayment/1619307-billingaddress)Added [PKPayment.shippingAddress](https://developer.apple.com/documentation/passkit/pkpayment/1619271-shippingaddress)Added [PKPayment.shippingMethod](https://developer.apple.com/documentation/passkit/pkpayment/1619268-shippingmethod)Added [PKPayment.token](https://developer.apple.com/documentation/passkit/pkpayment/1619239-token)PKPaymentAuthorizationViewController.h (Added)Added [PKPaymentAuthorizationViewController](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller)Added [+[PKPaymentAuthorizationViewController canMakePayments]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller/1616192-canmakepayments)Added [+[PKPaymentAuthorizationViewController canMakePaymentsUsingNetworks:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller/1616187-canmakepaymentsusingnetworks)Added [PKPaymentAuthorizationViewController.delegate](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller/1616199-delegate)Added [-[PKPaymentAuthorizationViewController initWithPaymentRequest:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller/1616178-init)Added [PKPaymentAuthorizationViewControllerDelegate](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate)Added [-[PKPaymentAuthorizationViewControllerDelegate paymentAuthorizationViewController:didAuthorizePayment:completion:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616195-paymentauthorizationviewcontroll)Added [-[PKPaymentAuthorizationViewControllerDelegate paymentAuthorizationViewController:didSelectShippingAddress:completion:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616196-paymentauthorizationviewcontroll)Added [-[PKPaymentAuthorizationViewControllerDelegate paymentAuthorizationViewController:didSelectShippingMethod:completion:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616186-paymentauthorizationviewcontroll)Added [-[PKPaymentAuthorizationViewControllerDelegate paymentAuthorizationViewControllerDidFinish:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616180-paymentauthorizationviewcontroll)Added [PKPaymentAuthorizationStatus](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus)Added [PKPaymentAuthorizationStatusFailure](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatusfailure)Added [PKPaymentAuthorizationStatusInvalidBillingPostalAddress](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/invalidbillingpostaladdress)Added [PKPaymentAuthorizationStatusInvalidShippingContact](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatusinvalidshippingcontact)Added [PKPaymentAuthorizationStatusInvalidShippingPostalAddress](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatusinvalidshippingpostaladdress)Added [PKPaymentAuthorizationStatusSuccess](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatussuccess)PKPaymentPass.h (Added)Added [PKPaymentPass](https://developer.apple.com/documentation/passkit/pkpaymentpass)Added [PKPaymentPass.activationState](https://developer.apple.com/documentation/passkit/pkpaymentpass/1619080-activationstate)Added [PKPaymentPass.deviceAccountIdentifier](https://developer.apple.com/documentation/passkit/pkpaymentpass/1619074-deviceaccountidentifier)Added [PKPaymentPass.deviceAccountNumberSuffix](https://developer.apple.com/documentation/passkit/pkpaymentpass/1619075-deviceaccountnumbersuffix)Added [PKPaymentPass.primaryAccountIdentifier](https://developer.apple.com/documentation/passkit/pkpaymentpass/1619084-primaryaccountidentifier)Added [PKPaymentPass.primaryAccountNumberSuffix](https://developer.apple.com/documentation/passkit/pkpaymentpass/1619081-primaryaccountnumbersuffix)Added [PKPaymentPassActivationState](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate)Added [PKPaymentPassActivationStateActivated](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate/pkpaymentpassactivationstateactivated)Added [PKPaymentPassActivationStateActivating](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate/pkpaymentpassactivationstateactivating)Added [PKPaymentPassActivationStateDeactivated](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate/pkpaymentpassactivationstatedeactivated)Added [PKPaymentPassActivationStateRequiresActivation](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate/requiresactivation)Added [PKPaymentPassActivationStateSuspended](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate/pkpaymentpassactivationstatesuspended)PKPaymentRequest.h (Added)Added [PKPaymentRequest](https://developer.apple.com/documentation/passkit/pkpaymentrequest)Added [PKPaymentRequest.applicationData](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619298-applicationdata)Added [PKPaymentRequest.billingAddress](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619229-billingaddress)Added [PKPaymentRequest.countryCode](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619246-countrycode)Added [PKPaymentRequest.currencyCode](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619248-currencycode)Added [PKPaymentRequest.merchantCapabilities](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619257-merchantcapabilities)Added [PKPaymentRequest.merchantIdentifier](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619305-merchantidentifier)Added [PKPaymentRequest.paymentSummaryItems](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619231-paymentsummaryitems)Added [PKPaymentRequest.requiredBillingAddressFields](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619265-requiredbillingaddressfields)Added [PKPaymentRequest.requiredShippingAddressFields](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619228-requiredshippingaddressfields)Added [PKPaymentRequest.shippingAddress](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619216-shippingaddress)Added [PKPaymentRequest.shippingMethods](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619226-shippingmethods)Added [PKPaymentRequest.supportedNetworks](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619329-supportednetworks)Added [PKPaymentSummaryItem](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem)Added [PKPaymentSummaryItem.amount](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/1619291-amount)Added [PKPaymentSummaryItem.label](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/1619260-label)Added [+[PKPaymentSummaryItem summaryItemWithLabel:amount:]](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/1619275-init)Added [PKShippingMethod](https://developer.apple.com/documentation/passkit/pkshippingmethod)Added [PKShippingMethod.detail](https://developer.apple.com/documentation/passkit/pkshippingmethod/1619306-detail)Added [PKShippingMethod.identifier](https://developer.apple.com/documentation/passkit/pkshippingmethod/1619232-identifier)Added [PKAddressField](https://developer.apple.com/documentation/passkit/pkaddressfield)Added [PKAddressFieldAll](https://developer.apple.com/documentation/passkit/pkaddressfield/pkaddressfieldall)Added [PKAddressFieldEmail](https://developer.apple.com/documentation/passkit/pkaddressfield/pkaddressfieldemail)Added [PKAddressFieldNone](https://developer.apple.com/documentation/passkit/pkaddressfield/pkaddressfieldnone)Added [PKAddressFieldPhone](https://developer.apple.com/documentation/passkit/pkaddressfield/1619308-phone)Added [PKAddressFieldPostalAddress](https://developer.apple.com/documentation/passkit/pkaddressfield/pkaddressfieldpostaladdress)Added [PKMerchantCapability](https://developer.apple.com/documentation/passkit/pkmerchantcapability)Added [PKMerchantCapability3DS](https://developer.apple.com/documentation/passkit/pkmerchantcapability/1619261-capability3ds)Added [PKMerchantCapabilityEMV](https://developer.apple.com/documentation/passkit/pkmerchantcapability/pkmerchantcapabilityemv)Added [PKPaymentNetworkAmex](https://developer.apple.com/documentation/passkit/pkpaymentnetworkamex)Added [PKPaymentNetworkMasterCard](https://developer.apple.com/documentation/passkit/pkpaymentnetwork/1618643-mastercard)Added [PKPaymentNetworkVisa](https://developer.apple.com/documentation/passkit/pkpaymentnetworkvisa)PKPaymentToken.h (Added)Added [PKPaymentToken](https://developer.apple.com/documentation/passkit/pkpaymenttoken)Added [PKPaymentToken.paymentData](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1617000-paymentdata)Added [PKPaymentToken.paymentInstrumentName](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1616998-paymentinstrumentname)Added [PKPaymentToken.paymentNetwork](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1617001-paymentnetwork)Added [PKPaymentToken.transactionIdentifier](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1617003-transactionidentifier)

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
