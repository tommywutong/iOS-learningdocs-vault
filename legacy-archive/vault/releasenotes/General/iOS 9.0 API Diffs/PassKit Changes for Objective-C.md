---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/PassKit.html
archived_at: '2026-07-18T02:56:36.052350Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# PassKit Changes for Objective-C

### PassKit

#### PKAddPassButton.h (Added)

Added [PKAddPassButton](https://developer.apple.com/documentation/passkit/pkaddpassbutton)Added [PKAddPassButton.addPassButtonStyle](https://developer.apple.com/documentation/passkit/pkaddpassbutton/1618546-addpassbuttonstyle)Added [+[PKAddPassButton addPassButtonWithStyle:]](https://developer.apple.com/documentation/passkit/pkaddpassbutton/1618549-addpassbuttonwithstyle)Added [-[PKAddPassButton initWithAddPassButtonStyle:]](https://developer.apple.com/documentation/passkit/pkaddpassbutton/1618547-initwithaddpassbuttonstyle)Added [PKAddPassButtonStyle](https://developer.apple.com/documentation/passkit/pkaddpassbuttonstyle)Added [PKAddPassButtonStyleBlack](https://developer.apple.com/documentation/passkit/pkaddpassbuttonstyle/pkaddpassbuttonstyleblack)Added [PKAddPassButtonStyleBlackOutline](https://developer.apple.com/documentation/passkit/pkaddpassbuttonstyle/pkaddpassbuttonstyleblackoutline)

#### PKAddPassesViewController.h

Modified [-[PKAddPassesViewController initWithPass:]](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller/1619251-initwithpass)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithPass:(id)pass ``` |
| To | ``` - (instancetype _Nonnull)initWithPass:(PKPass * _Nonnull)pass ``` |

Modified [-[PKAddPassesViewController initWithPasses:]](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller/1619217-initwithpasses)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithPasses:(NSArray *)passes ``` |
| To | ``` - (instancetype _Nonnull)initWithPasses:(NSArray<PKPass *> * _Nonnull)passes ``` |

#### PKAddPaymentPassViewController.h (Added)

Added [PKAddPaymentPassRequest](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest)Added [PKAddPaymentPassRequest.activationData](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest/1615914-activationdata)Added [PKAddPaymentPassRequest.encryptedPassData](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest/1615926-encryptedpassdata)Added [PKAddPaymentPassRequest.ephemeralPublicKey](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest/1615952-ephemeralpublickey)Added [-[PKAddPaymentPassRequest init]](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest/1615919-init)Added [PKAddPaymentPassRequest.wrappedKey](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest/1615950-wrappedkey)Added [PKAddPaymentPassRequestConfiguration](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration)Added [PKAddPaymentPassRequestConfiguration.cardholderName](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/1615910-cardholdername)Added [PKAddPaymentPassRequestConfiguration.encryptionScheme](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/1615946-encryptionscheme)Added [-[PKAddPaymentPassRequestConfiguration initWithEncryptionScheme:]](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/1615930-initwithencryptionscheme)Added [PKAddPaymentPassRequestConfiguration.localizedDescription](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/1615932-localizeddescription)Added [PKAddPaymentPassRequestConfiguration.paymentNetwork](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/1615948-paymentnetwork)Added [PKAddPaymentPassRequestConfiguration.primaryAccountIdentifier](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/1615936-primaryaccountidentifier)Added [PKAddPaymentPassRequestConfiguration.primaryAccountSuffix](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/1615917-primaryaccountsuffix)Added [PKAddPaymentPassViewController](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontroller)Added [+[PKAddPaymentPassViewController canAddPaymentPass]](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontroller/1615938-canaddpaymentpass)Added [PKAddPaymentPassViewController.delegate](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontroller/1615913-delegate)Added [-[PKAddPaymentPassViewController initWithRequestConfiguration:delegate:]](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontroller/1615922-initwithrequestconfiguration)Added [PKAddPaymentPassViewControllerDelegate](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontrollerdelegate)Added [-[PKAddPaymentPassViewControllerDelegate addPaymentPassViewController:didFinishAddingPaymentPass:error:]](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontrollerdelegate/1615942-addpaymentpassviewcontroller)Added [-[PKAddPaymentPassViewControllerDelegate addPaymentPassViewController:generateRequestWithCertificateChain:nonce:nonceSignature:completionHandler:]](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontrollerdelegate/1615915-addpaymentpassviewcontroller)Added [PKAddPaymentPassError](https://developer.apple.com/documentation/passkit/pkaddpaymentpasserror)Added [PKAddPaymentPassErrorSystemCancelled](https://developer.apple.com/documentation/passkit/pkaddpaymentpasserror/pkaddpaymentpasserrorsystemcancelled)Added [PKAddPaymentPassErrorUnsupported](https://developer.apple.com/documentation/passkit/pkaddpaymentpasserror/unsupported)Added [PKAddPaymentPassErrorUserCancelled](https://developer.apple.com/documentation/passkit/pkaddpaymentpasserror/usercancelled)

#### PKConstants.h (Added)

Added [PKEncryptionSchemeECC_V2](https://developer.apple.com/documentation/passkit/pkencryptionschemeecc_v2)Added [PKPaymentNetworkDiscover](https://developer.apple.com/documentation/passkit/pkpaymentnetwork/1618641-discover)Added [PKPaymentNetworkPrivateLabel](https://developer.apple.com/documentation/passkit/pkpaymentnetworkprivatelabel)Modified [PKPaymentNetworkAmex](https://developer.apple.com/documentation/passkit/pkpaymentnetworkamex)

|  | Header |
| --- | --- |
| From | PassKit/PKPaymentRequest.h |
| To | PassKit/PKConstants.h |

Modified [PKPaymentNetworkMasterCard](https://developer.apple.com/documentation/passkit/pkpaymentnetwork/1618643-mastercard)

|  | Header |
| --- | --- |
| From | PassKit/PKPaymentRequest.h |
| To | PassKit/PKConstants.h |

Modified [PKPaymentNetworkVisa](https://developer.apple.com/documentation/passkit/pkpaymentnetworkvisa)

|  | Header |
| --- | --- |
| From | PassKit/PKPaymentRequest.h |
| To | PassKit/PKConstants.h |

#### PKContact.h (Added)

Added [PKContact](https://developer.apple.com/documentation/passkit/pkcontact)Added [PKContact.emailAddress](https://developer.apple.com/documentation/passkit/pkcontact/1619273-emailaddress)Added [PKContact.name](https://developer.apple.com/documentation/passkit/pkcontact/1619318-name)Added [PKContact.phoneNumber](https://developer.apple.com/documentation/passkit/pkcontact/1619223-phonenumber)Added [PKContact.postalAddress](https://developer.apple.com/documentation/passkit/pkcontact/1619283-postaladdress)

#### PKPass.h

Added [PKPass.deviceName](https://developer.apple.com/documentation/passkit/pkpass/1618774-devicename)Added [PKPass.remotePass](https://developer.apple.com/documentation/passkit/pkpass/1618786-isremotepass)

#### PKPassLibrary.h

Added [-[PKPassLibrary canAddPaymentPassWithPrimaryAccountIdentifier:]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617081-canaddpaymentpass)Added [+[PKPassLibrary endAutomaticPassPresentationSuppressionWithRequestToken:]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617097-endautomaticpasspresentationsupp)Added [-[PKPassLibrary isPaymentPassActivationAvailable]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617107-ispaymentpassactivationavailable)Added [+[PKPassLibrary isSuppressingAutomaticPassPresentation]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617092-issuppressingautomaticpasspresen)Added [-[PKPassLibrary remotePaymentPasses]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617099-remotepaymentpasses)Added [+[PKPassLibrary requestAutomaticPassPresentationSuppressionWithResponseHandler:]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617078-requestautomaticpasspresentation)Added [PKAutomaticPassPresentationSuppressionResult](https://developer.apple.com/documentation/passkit/pkautomaticpasspresentationsuppressionresult)Added [PKAutomaticPassPresentationSuppressionResultAlreadyPresenting](https://developer.apple.com/documentation/passkit/pkautomaticpasspresentationsuppressionresult/alreadypresenting)Added [PKAutomaticPassPresentationSuppressionResultCancelled](https://developer.apple.com/documentation/passkit/pkautomaticpasspresentationsuppressionresult/cancelled)Added [PKAutomaticPassPresentationSuppressionResultDenied](https://developer.apple.com/documentation/passkit/pkautomaticpasspresentationsuppressionresult/denied)Added [PKAutomaticPassPresentationSuppressionResultNotSupported](https://developer.apple.com/documentation/passkit/pkautomaticpasspresentationsuppressionresult/pkautomaticpasspresentationsuppressionresultnotsupported)Added [PKAutomaticPassPresentationSuppressionResultSuccess](https://developer.apple.com/documentation/passkit/pkautomaticpasspresentationsuppressionresult/success)Added [PKPassLibraryRemotePaymentPassesDidChangeNotification](https://developer.apple.com/documentation/passkit/pkpasslibraryremotepaymentpassesdidchangenotification)Added [PKSuppressionRequestToken](https://developer.apple.com/documentation/passkit/pksuppressionrequesttoken)Modified [-[PKPassLibrary activatePaymentPass:withActivationCode:completion:]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617079-activate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[PKPassLibrary addPasses:withCompletionHandler:]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617093-addpasses)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addPasses:(NSArray *)passes withCompletionHandler:(void (^)(PKPassLibraryAddPassesStatus status))completion ``` |
| To | ``` - (void)addPasses:(NSArray<PKPass *> * _Nonnull)passes withCompletionHandler:(void (^ _Nullable)(PKPassLibraryAddPassesStatus status))completion ``` |

Modified [+[PKPassLibrary isPaymentPassActivationAvailable]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617108-ispaymentpassactivationavailable)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[PKPassLibrary passes]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617109-passes)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)passes ``` |
| To | ``` - (NSArray<PKPass *> * _Nonnull)passes ``` |

Modified [-[PKPassLibrary passesOfType:]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617074-passes)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)passesOfType:(PKPassType)passType ``` |
| To | ``` - (NSArray<PKPass *> * _Nonnull)passesOfType:(PKPassType)passType ``` |

#### PKPayment.h

Added [PKPayment.billingContact](https://developer.apple.com/documentation/passkit/pkpayment/1619320-billingcontact)Added [PKPayment.shippingContact](https://developer.apple.com/documentation/passkit/pkpayment/1619250-shippingcontact)Modified [PKPayment.billingAddress](https://developer.apple.com/documentation/passkit/pkpayment/1619307-billingaddress)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [PKPayment.shippingAddress](https://developer.apple.com/documentation/passkit/pkpayment/1619271-shippingaddress)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### PKPaymentAuthorizationViewController.h

Added [+[PKPaymentAuthorizationViewController canMakePaymentsUsingNetworks:capabilities:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller/1616181-canmakepaymentsusingnetworks)Added [-[PKPaymentAuthorizationViewControllerDelegate paymentAuthorizationViewController:didSelectPaymentMethod:completion:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616184-paymentauthorizationviewcontroll)Added [-[PKPaymentAuthorizationViewControllerDelegate paymentAuthorizationViewController:didSelectShippingContact:completion:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616198-paymentauthorizationviewcontroll)Modified [+[PKPaymentAuthorizationViewController canMakePaymentsUsingNetworks:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller/1616187-canmakepaymentsusingnetworks)

|  | Declaration |
| --- | --- |
| From | ``` + (BOOL)canMakePaymentsUsingNetworks:(NSArray *)supportedNetworks ``` |
| To | ``` + (BOOL)canMakePaymentsUsingNetworks:(NSArray<NSString *> * _Nonnull)supportedNetworks ``` |

Modified [-[PKPaymentAuthorizationViewControllerDelegate paymentAuthorizationViewController:didSelectShippingAddress:completion:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616196-paymentauthorizationviewcontroll)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (void)paymentAuthorizationViewController:(PKPaymentAuthorizationViewController *)controller didSelectShippingAddress:(ABRecordRef)address completion:(void (^)(PKPaymentAuthorizationStatus status, NSArray *shippingMethods, NSArray *summaryItems))completion ``` | -- |
| To | ``` - (void)paymentAuthorizationViewController:(PKPaymentAuthorizationViewController * _Nonnull)controller didSelectShippingAddress:(ABRecordRef _Nonnull)address completion:(void (^ _Nonnull)(PKPaymentAuthorizationStatus status, NSArray<PKShippingMethod *> * _Nonnull shippingMethods, NSArray<PKPaymentSummaryItem *> * _Nonnull summaryItems))completion ``` | iOS 9.0 |

Modified [-[PKPaymentAuthorizationViewControllerDelegate paymentAuthorizationViewController:didSelectShippingMethod:completion:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616186-paymentauthorizationviewcontroll)

|  | Declaration |
| --- | --- |
| From | ``` - (void)paymentAuthorizationViewController:(PKPaymentAuthorizationViewController *)controller didSelectShippingMethod:(PKShippingMethod *)shippingMethod completion:(void (^)(PKPaymentAuthorizationStatus status, NSArray *summaryItems))completion ``` |
| To | ``` - (void)paymentAuthorizationViewController:(PKPaymentAuthorizationViewController * _Nonnull)controller didSelectShippingMethod:(PKShippingMethod * _Nonnull)shippingMethod completion:(void (^ _Nonnull)(PKPaymentAuthorizationStatus status, NSArray<PKPaymentSummaryItem *> * _Nonnull summaryItems))completion ``` |

#### PKPaymentButton.h

Added [-[PKPaymentButton initWithPaymentButtonType:paymentButtonStyle:]](https://developer.apple.com/documentation/passkit/pkpaymentbutton/1617842-init)Added [PKPaymentButtonTypeSetUp](https://developer.apple.com/documentation/passkit/pkpaymentbuttontype/pkpaymentbuttontypesetup)

#### PKPaymentMethod.h (Added)

Added [PKPaymentMethod](https://developer.apple.com/documentation/passkit/pkpaymentmethod)Added [PKPaymentMethod.displayName](https://developer.apple.com/documentation/passkit/pkpaymentmethod/1619249-displayname)Added [PKPaymentMethod.network](https://developer.apple.com/documentation/passkit/pkpaymentmethod/1619209-network)Added [PKPaymentMethod.paymentPass](https://developer.apple.com/documentation/passkit/pkpaymentmethod/1619269-paymentpass)Added [PKPaymentMethod.type](https://developer.apple.com/documentation/passkit/pkpaymentmethod/1619279-type)Added [PKPaymentMethodType](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype)Added [PKPaymentMethodTypeCredit](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/credit)Added [PKPaymentMethodTypeDebit](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/pkpaymentmethodtypedebit)Added [PKPaymentMethodTypePrepaid](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/pkpaymentmethodtypeprepaid)Added [PKPaymentMethodTypeStore](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/pkpaymentmethodtypestore)Added [PKPaymentMethodTypeUnknown](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/pkpaymentmethodtypeunknown)

#### PKPaymentRequest.h

Added [PKPaymentRequest.billingContact](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619221-billingcontact)Added [PKPaymentRequest.shippingContact](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619245-shippingcontact)Added [+[PKPaymentSummaryItem summaryItemWithLabel:amount:type:]](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/1619262-summaryitemwithlabel)Added [PKPaymentSummaryItem.type](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/1619327-type)Added [PKMerchantCapabilityCredit](https://developer.apple.com/documentation/passkit/pkmerchantcapability/1619253-capabilitycredit)Added [PKMerchantCapabilityDebit](https://developer.apple.com/documentation/passkit/pkmerchantcapability/pkmerchantcapabilitydebit)Added [PKPaymentSummaryItemType](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitemtype)Added [PKPaymentSummaryItemTypeFinal](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitemtype/final)Added [PKPaymentSummaryItemTypePending](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitemtype/pkpaymentsummaryitemtypepending)Modified [PKPaymentRequest.billingAddress](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619229-billingaddress)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [PKPaymentRequest.paymentSummaryItems](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619231-paymentsummaryitems)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *paymentSummaryItems ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSArray<PKPaymentSummaryItem *> *paymentSummaryItems ``` |

Modified [PKPaymentRequest.shippingAddress](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619216-shippingaddress)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [PKPaymentRequest.shippingMethods](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619226-shippingmethods)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *shippingMethods ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<PKShippingMethod *> *shippingMethods ``` |

Modified [PKPaymentRequest.supportedNetworks](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619329-supportednetworks)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *supportedNetworks ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSArray<NSString *> *supportedNetworks ``` |

Modified [PKPaymentNetworkAmex](https://developer.apple.com/documentation/passkit/pkpaymentnetworkamex)

|  | Header |
| --- | --- |
| From | PassKit/PKPaymentRequest.h |
| To | PassKit/PKConstants.h |

Modified [PKPaymentNetworkMasterCard](https://developer.apple.com/documentation/passkit/pkpaymentnetwork/1618643-mastercard)

|  | Header |
| --- | --- |
| From | PassKit/PKPaymentRequest.h |
| To | PassKit/PKConstants.h |

Modified [PKPaymentNetworkVisa](https://developer.apple.com/documentation/passkit/pkpaymentnetworkvisa)

|  | Header |
| --- | --- |
| From | PassKit/PKPaymentRequest.h |
| To | PassKit/PKConstants.h |

#### PKPaymentToken.h

Added [PKPaymentToken.paymentMethod](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1617002-paymentmethod)Modified [PKPaymentToken.paymentInstrumentName](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1616998-paymentinstrumentname)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [PKPaymentToken.paymentNetwork](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1617001-paymentnetwork)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

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
