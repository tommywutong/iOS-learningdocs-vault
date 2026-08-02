---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Objective-C/PassKit.html
archived_at: '2026-07-18T02:54:57.939087Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# PassKit Changes for Objective-C

### PassKit

#### PKAddPaymentPassViewController.h

Modified [PKAddPaymentPassRequestConfiguration.encryptionScheme](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/1615946-encryptionscheme)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy, readonly) NSString *encryptionScheme ``` |
| To | ``` @property(nonatomic, copy, readonly) PKEncryptionScheme encryptionScheme ``` |

Modified [-[PKAddPaymentPassRequestConfiguration initWithEncryptionScheme:]](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/1615930-initwithencryptionscheme)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithEncryptionScheme:(NSString *)encryptionScheme ``` |
| To | ``` - (instancetype)initWithEncryptionScheme:(PKEncryptionScheme)encryptionScheme ``` |

Modified [PKAddPaymentPassRequestConfiguration.paymentNetwork](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/1615948-paymentnetwork)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *paymentNetwork ``` |
| To | ``` @property(nonatomic, copy) PKPaymentNetwork paymentNetwork ``` |

#### PKConstants.h

Added [PKEncryptionScheme](https://developer.apple.com/documentation/passkit/pkencryptionscheme)Added [PKEncryptionSchemeRSA_V2](https://developer.apple.com/documentation/passkit/pkencryptionschemersa_v2)Added [PKPaymentNetwork](https://developer.apple.com/documentation/passkit/pkpaymentnetwork)Modified [PKPaymentAuthorizationStatus](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus)

|  | Header |
| --- | --- |
| From | PassKit/PKPaymentAuthorizationViewController.h |
| To | PassKit/PKConstants.h |

Modified [PKPaymentAuthorizationStatusFailure](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatusfailure)

|  | Header |
| --- | --- |
| From | PassKit/PKPaymentAuthorizationViewController.h |
| To | PassKit/PKConstants.h |

Modified [PKPaymentAuthorizationStatusInvalidBillingPostalAddress](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/invalidbillingpostaladdress)

|  | Header |
| --- | --- |
| From | PassKit/PKPaymentAuthorizationViewController.h |
| To | PassKit/PKConstants.h |

Modified [PKPaymentAuthorizationStatusInvalidShippingContact](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatusinvalidshippingcontact)

|  | Header |
| --- | --- |
| From | PassKit/PKPaymentAuthorizationViewController.h |
| To | PassKit/PKConstants.h |

Modified [PKPaymentAuthorizationStatusInvalidShippingPostalAddress](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatusinvalidshippingpostaladdress)

|  | Header |
| --- | --- |
| From | PassKit/PKPaymentAuthorizationViewController.h |
| To | PassKit/PKConstants.h |

Modified [PKPaymentAuthorizationStatusPINIncorrect](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pinincorrect)

|  | Header |
| --- | --- |
| From | PassKit/PKPaymentAuthorizationViewController.h |
| To | PassKit/PKConstants.h |

Modified [PKPaymentAuthorizationStatusPINLockout](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatuspinlockout)

|  | Header |
| --- | --- |
| From | PassKit/PKPaymentAuthorizationViewController.h |
| To | PassKit/PKConstants.h |

Modified [PKPaymentAuthorizationStatusPINRequired](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatuspinrequired)

|  | Header |
| --- | --- |
| From | PassKit/PKPaymentAuthorizationViewController.h |
| To | PassKit/PKConstants.h |

Modified [PKPaymentAuthorizationStatusSuccess](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatussuccess)

|  | Header |
| --- | --- |
| From | PassKit/PKPaymentAuthorizationViewController.h |
| To | PassKit/PKConstants.h |

#### PKContact.h

Modified [PKContact.emailAddress](https://developer.apple.com/documentation/passkit/pkcontact/1619273-emailaddress)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSString *emailAddress ``` |
| To | ``` @property(nonatomic, strong) NSString *emailAddress ``` |

Modified [PKContact.name](https://developer.apple.com/documentation/passkit/pkcontact/1619318-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSPersonNameComponents *name ``` |
| To | ``` @property(nonatomic, strong) NSPersonNameComponents *name ``` |

Modified [PKContact.phoneNumber](https://developer.apple.com/documentation/passkit/pkcontact/1619223-phonenumber)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) CNPhoneNumber *phoneNumber ``` |
| To | ``` @property(nonatomic, strong) CNPhoneNumber *phoneNumber ``` |

Modified [PKContact.postalAddress](https://developer.apple.com/documentation/passkit/pkcontact/1619283-postaladdress)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) CNPostalAddress *postalAddress ``` |
| To | ``` @property(nonatomic, strong) CNPostalAddress *postalAddress ``` |

#### PKPass.h

Modified [PKPass.paymentPass](https://developer.apple.com/documentation/passkit/pkpass/1618784-paymentpass)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign, readonly) PKPaymentPass *paymentPass ``` |
| To | ``` @property(nonatomic, readonly) PKPaymentPass *paymentPass ``` |

#### PKPassLibrary.h

Added [-[PKPassLibrary presentPaymentPass:]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1649554-present)Added [PKPassLibraryNotificationKey](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationkey)Added [PKPassLibraryNotificationName](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationname)

#### PKPayment.h

Modified [PKPayment.billingAddress](https://developer.apple.com/documentation/passkit/pkpayment/1619307-billingaddress)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) ABRecordRef billingAddress ``` |
| To | ``` @property(nonatomic, assign, readonly) ABRecordRef billingAddress ``` |

Modified [PKPayment.billingContact](https://developer.apple.com/documentation/passkit/pkpayment/1619320-billingcontact)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) PKContact *billingContact ``` |
| To | ``` @property(nonatomic, strong, readonly) PKContact *billingContact ``` |

Modified [PKPayment.shippingAddress](https://developer.apple.com/documentation/passkit/pkpayment/1619271-shippingaddress)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) ABRecordRef shippingAddress ``` |
| To | ``` @property(nonatomic, assign, readonly) ABRecordRef shippingAddress ``` |

Modified [PKPayment.shippingContact](https://developer.apple.com/documentation/passkit/pkpayment/1619250-shippingcontact)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) PKContact *shippingContact ``` |
| To | ``` @property(nonatomic, strong, readonly) PKContact *shippingContact ``` |

Modified [PKPayment.shippingMethod](https://developer.apple.com/documentation/passkit/pkpayment/1619268-shippingmethod)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) PKShippingMethod *shippingMethod ``` |
| To | ``` @property(nonatomic, strong, readonly) PKShippingMethod *shippingMethod ``` |

Modified [PKPayment.token](https://developer.apple.com/documentation/passkit/pkpayment/1619239-token)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) PKPaymentToken *token ``` |
| To | ``` @property(nonatomic, strong, readonly) PKPaymentToken *token ``` |

#### PKPaymentAuthorizationController.h (Added)

Added [PKPaymentAuthorizationController](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller)Added [+[PKPaymentAuthorizationController canMakePayments]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1649461-canmakepayments)Added [+[PKPaymentAuthorizationController canMakePaymentsUsingNetworks:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1649457-canmakepaymentsusingnetworks)Added [+[PKPaymentAuthorizationController canMakePaymentsUsingNetworks:capabilities:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1649455-canmakepaymentsusingnetworks)Added [PKPaymentAuthorizationController.delegate](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1649453-delegate)Added [-[PKPaymentAuthorizationController dismissWithCompletion:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1771696-dismiss)Added [-[PKPaymentAuthorizationController initWithPaymentRequest:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1649462-init)Added [-[PKPaymentAuthorizationController presentWithCompletion:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1649463-presentwithcompletion)Added [PKPaymentAuthorizationControllerDelegate](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate)Added [-[PKPaymentAuthorizationControllerDelegate paymentAuthorizationController:didAuthorizePayment:completion:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/1649454-paymentauthorizationcontroller)Added [-[PKPaymentAuthorizationControllerDelegate paymentAuthorizationController:didSelectPaymentMethod:completion:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/1649460-paymentauthorizationcontroller)Added [-[PKPaymentAuthorizationControllerDelegate paymentAuthorizationController:didSelectShippingContact:completion:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/1649458-paymentauthorizationcontroller)Added [-[PKPaymentAuthorizationControllerDelegate paymentAuthorizationController:didSelectShippingMethod:completion:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/1649465-paymentauthorizationcontroller)Added [-[PKPaymentAuthorizationControllerDelegate paymentAuthorizationControllerDidFinish:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/1649456-paymentauthorizationcontrollerdi)Added [-[PKPaymentAuthorizationControllerDelegate paymentAuthorizationControllerWillAuthorizePayment:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/1649464-paymentauthorizationcontrollerwi)

#### PKPaymentAuthorizationViewController.h

Modified [+[PKPaymentAuthorizationViewController canMakePaymentsUsingNetworks:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller/1616187-canmakepaymentsusingnetworks)

|  | Declaration |
| --- | --- |
| From | ``` + (BOOL)canMakePaymentsUsingNetworks:(NSArray<NSString *> *)supportedNetworks ``` |
| To | ``` + (BOOL)canMakePaymentsUsingNetworks:(NSArray<PKPaymentNetwork> *)supportedNetworks ``` |

Modified [+[PKPaymentAuthorizationViewController canMakePaymentsUsingNetworks:capabilities:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller/1616181-canmakepaymentsusingnetworks)

|  | Declaration |
| --- | --- |
| From | ``` + (BOOL)canMakePaymentsUsingNetworks:(NSArray<NSString *> *)supportedNetworks capabilities:(PKMerchantCapability)capabilties ``` |
| To | ``` + (BOOL)canMakePaymentsUsingNetworks:(NSArray<PKPaymentNetwork> *)supportedNetworks capabilities:(PKMerchantCapability)capabilties ``` |

Modified [PKPaymentAuthorizationStatus](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus)

|  | Header |
| --- | --- |
| From | PassKit/PKPaymentAuthorizationViewController.h |
| To | PassKit/PKConstants.h |

Modified [PKPaymentAuthorizationStatusFailure](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatusfailure)

|  | Header |
| --- | --- |
| From | PassKit/PKPaymentAuthorizationViewController.h |
| To | PassKit/PKConstants.h |

Modified [PKPaymentAuthorizationStatusInvalidBillingPostalAddress](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/invalidbillingpostaladdress)

|  | Header |
| --- | --- |
| From | PassKit/PKPaymentAuthorizationViewController.h |
| To | PassKit/PKConstants.h |

Modified [PKPaymentAuthorizationStatusInvalidShippingContact](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatusinvalidshippingcontact)

|  | Header |
| --- | --- |
| From | PassKit/PKPaymentAuthorizationViewController.h |
| To | PassKit/PKConstants.h |

Modified [PKPaymentAuthorizationStatusInvalidShippingPostalAddress](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatusinvalidshippingpostaladdress)

|  | Header |
| --- | --- |
| From | PassKit/PKPaymentAuthorizationViewController.h |
| To | PassKit/PKConstants.h |

Modified [PKPaymentAuthorizationStatusPINIncorrect](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pinincorrect)

|  | Header |
| --- | --- |
| From | PassKit/PKPaymentAuthorizationViewController.h |
| To | PassKit/PKConstants.h |

Modified [PKPaymentAuthorizationStatusPINLockout](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatuspinlockout)

|  | Header |
| --- | --- |
| From | PassKit/PKPaymentAuthorizationViewController.h |
| To | PassKit/PKConstants.h |

Modified [PKPaymentAuthorizationStatusPINRequired](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatuspinrequired)

|  | Header |
| --- | --- |
| From | PassKit/PKPaymentAuthorizationViewController.h |
| To | PassKit/PKConstants.h |

Modified [PKPaymentAuthorizationStatusSuccess](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatussuccess)

|  | Header |
| --- | --- |
| From | PassKit/PKPaymentAuthorizationViewController.h |
| To | PassKit/PKConstants.h |

#### PKPaymentButton.h

Added [PKPaymentButtonTypeInStore](https://developer.apple.com/documentation/passkit/pkpaymentbuttontype/pkpaymentbuttontypeinstore)

#### PKPaymentMethod.h

Modified [PKPaymentMethod.displayName](https://developer.apple.com/documentation/passkit/pkpaymentmethod/1619249-displayname)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *displayName ``` |
| To | ``` @property(nonatomic, copy, readonly) NSString *displayName ``` |

Modified [PKPaymentMethod.network](https://developer.apple.com/documentation/passkit/pkpaymentmethod/1619209-network)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *network ``` |
| To | ``` @property(nonatomic, copy, readonly) PKPaymentNetwork network ``` |

Modified [PKPaymentMethod.paymentPass](https://developer.apple.com/documentation/passkit/pkpaymentmethod/1619269-paymentpass)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) PKPaymentPass *paymentPass ``` |
| To | ``` @property(nonatomic, copy, readonly) PKPaymentPass *paymentPass ``` |

#### PKPaymentPass.h

Modified [PKPaymentPass.deviceAccountIdentifier](https://developer.apple.com/documentation/passkit/pkpaymentpass/1619074-deviceaccountidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *deviceAccountIdentifier ``` |
| To | ``` @property(weak, readonly) NSString *deviceAccountIdentifier ``` |

Modified [PKPaymentPass.deviceAccountNumberSuffix](https://developer.apple.com/documentation/passkit/pkpaymentpass/1619075-deviceaccountnumbersuffix)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *deviceAccountNumberSuffix ``` |
| To | ``` @property(weak, readonly) NSString *deviceAccountNumberSuffix ``` |

#### PKPaymentRequest.h

Added [+[PKPaymentRequest availableNetworks]](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1833288-availablenetworks)Modified [PKPaymentRequest.billingContact](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619221-billingcontact)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) PKContact *billingContact ``` |
| To | ``` @property(nonatomic, strong) PKContact *billingContact ``` |

Modified [PKPaymentRequest.shippingContact](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619245-shippingcontact)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) PKContact *shippingContact ``` |
| To | ``` @property(nonatomic, strong) PKContact *shippingContact ``` |

Modified [PKPaymentRequest.supportedNetworks](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619329-supportednetworks)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray<NSString *> *supportedNetworks ``` |
| To | ``` @property(nonatomic, copy) NSArray<PKPaymentNetwork> *supportedNetworks ``` |

#### PKPaymentToken.h

Modified [PKPaymentToken.paymentData](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1617000-paymentdata)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSData *paymentData ``` |
| To | ``` @property(nonatomic, copy, readonly) NSData *paymentData ``` |

Modified [PKPaymentToken.paymentInstrumentName](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1616998-paymentinstrumentname)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *paymentInstrumentName ``` |
| To | ``` @property(nonatomic, copy, readonly) NSString *paymentInstrumentName ``` |

Modified [PKPaymentToken.paymentMethod](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1617002-paymentmethod)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) PKPaymentMethod *paymentMethod ``` |
| To | ``` @property(nonatomic, strong, readonly) PKPaymentMethod *paymentMethod ``` |

Modified [PKPaymentToken.paymentNetwork](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1617001-paymentnetwork)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *paymentNetwork ``` |
| To | ``` @property(nonatomic, copy, readonly) NSString *paymentNetwork ``` |

Modified [PKPaymentToken.transactionIdentifier](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1617003-transactionidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *transactionIdentifier ``` |
| To | ``` @property(nonatomic, copy, readonly) NSString *transactionIdentifier ``` |

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
