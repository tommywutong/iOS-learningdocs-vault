---
title: watchOS 3.0 API Diffs
apple_id: TP40017328
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS30APIDiffs/Objective-C/PassKit.html
archived_at: '2026-07-18T02:58:14.909902Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 3.0 API Diffs](watchOS%202.2%20to%20watchOS%203.0%20API%20Differences.md)


# PassKit Changes for Objective-C

### PassKit

#### PKConstants.h

Added [PKEncryptionScheme](https://developer.apple.com/documentation/passkit/pkencryptionscheme)Added [PKEncryptionSchemeRSA_V2](https://developer.apple.com/documentation/passkit/pkencryptionschemersa_v2)Added [PKPaymentAuthorizationStatus](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus)Added [PKPaymentAuthorizationStatusFailure](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatusfailure)Added [PKPaymentAuthorizationStatusInvalidBillingPostalAddress](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/invalidbillingpostaladdress)Added [PKPaymentAuthorizationStatusInvalidShippingContact](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatusinvalidshippingcontact)Added [PKPaymentAuthorizationStatusInvalidShippingPostalAddress](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatusinvalidshippingpostaladdress)Added [PKPaymentAuthorizationStatusPINIncorrect](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pinincorrect)Added [PKPaymentAuthorizationStatusPINLockout](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatuspinlockout)Added [PKPaymentAuthorizationStatusPINRequired](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatuspinrequired)Added [PKPaymentAuthorizationStatusSuccess](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatussuccess)Added [PKPaymentNetwork](https://developer.apple.com/documentation/passkit/pkpaymentnetwork)Modified [PKPaymentNetworkAmex](https://developer.apple.com/documentation/passkit/pkpaymentnetworkamex)

|  | Introduction |
| --- | --- |
| From | watchOS 2.0 |
| To | watchOS 3.0 |

Modified [PKPaymentNetworkChinaUnionPay](https://developer.apple.com/documentation/passkit/pkpaymentnetwork/1618644-chinaunionpay)

|  | Introduction |
| --- | --- |
| From | watchOS 2.2 |
| To | watchOS 3.0 |

Modified [PKPaymentNetworkDiscover](https://developer.apple.com/documentation/passkit/pkpaymentnetwork/1618641-discover)

|  | Introduction |
| --- | --- |
| From | watchOS 2.0 |
| To | watchOS 3.0 |

Modified [PKPaymentNetworkInterac](https://developer.apple.com/documentation/passkit/pkpaymentnetworkinterac)

|  | Introduction |
| --- | --- |
| From | watchOS 2.2 |
| To | watchOS 3.0 |

Modified [PKPaymentNetworkMasterCard](https://developer.apple.com/documentation/passkit/pkpaymentnetwork/1618643-mastercard)

|  | Introduction |
| --- | --- |
| From | watchOS 2.0 |
| To | watchOS 3.0 |

Modified [PKPaymentNetworkPrivateLabel](https://developer.apple.com/documentation/passkit/pkpaymentnetworkprivatelabel)

|  | Introduction |
| --- | --- |
| From | watchOS 2.0 |
| To | watchOS 3.0 |

Modified [PKPaymentNetworkVisa](https://developer.apple.com/documentation/passkit/pkpaymentnetworkvisa)

|  | Introduction |
| --- | --- |
| From | watchOS 2.0 |
| To | watchOS 3.0 |

#### PKContact.h

Modified [PKContact](https://developer.apple.com/documentation/passkit/pkcontact)

|  | Introduction |
| --- | --- |
| From | watchOS 2.0 |
| To | watchOS 3.0 |

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

Added [PKPassLibraryNotificationKey](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationkey)Added [PKPassLibraryNotificationName](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationname)

#### PKPayment.h (Added)

Added [PKPayment](https://developer.apple.com/documentation/passkit/pkpayment)Added [PKPayment.billingContact](https://developer.apple.com/documentation/passkit/pkpayment/1619320-billingcontact)Added [PKPayment.shippingContact](https://developer.apple.com/documentation/passkit/pkpayment/1619250-shippingcontact)Added [PKPayment.shippingMethod](https://developer.apple.com/documentation/passkit/pkpayment/1619268-shippingmethod)Added [PKPayment.token](https://developer.apple.com/documentation/passkit/pkpayment/1619239-token)

#### PKPaymentAuthorizationController.h (Added)

Added [PKPaymentAuthorizationController](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller)Added [+[PKPaymentAuthorizationController canMakePayments]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1649461-canmakepayments)Added [+[PKPaymentAuthorizationController canMakePaymentsUsingNetworks:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1649457-canmakepaymentsusingnetworks)Added [+[PKPaymentAuthorizationController canMakePaymentsUsingNetworks:capabilities:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1649455-canmakepaymentsusingnetworks)Added [PKPaymentAuthorizationController.delegate](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1649453-delegate)Added [-[PKPaymentAuthorizationController dismissWithCompletion:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1771696-dismiss)Added [-[PKPaymentAuthorizationController initWithPaymentRequest:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1649462-init)Added [-[PKPaymentAuthorizationController presentWithCompletion:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1649463-presentwithcompletion)Added [PKPaymentAuthorizationControllerDelegate](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate)Added [-[PKPaymentAuthorizationControllerDelegate paymentAuthorizationController:didAuthorizePayment:completion:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/1649454-paymentauthorizationcontroller)Added [-[PKPaymentAuthorizationControllerDelegate paymentAuthorizationController:didSelectPaymentMethod:completion:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/1649460-paymentauthorizationcontroller)Added [-[PKPaymentAuthorizationControllerDelegate paymentAuthorizationController:didSelectShippingContact:completion:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/1649458-paymentauthorizationcontroller)Added [-[PKPaymentAuthorizationControllerDelegate paymentAuthorizationController:didSelectShippingMethod:completion:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/1649465-paymentauthorizationcontroller)Added [-[PKPaymentAuthorizationControllerDelegate paymentAuthorizationControllerDidFinish:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/1649456-paymentauthorizationcontrollerdi)Added [-[PKPaymentAuthorizationControllerDelegate paymentAuthorizationControllerWillAuthorizePayment:]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/1649464-paymentauthorizationcontrollerwi)

#### PKPaymentMethod.h (Added)

Added [PKPaymentMethod](https://developer.apple.com/documentation/passkit/pkpaymentmethod)Added [PKPaymentMethod.displayName](https://developer.apple.com/documentation/passkit/pkpaymentmethod/1619249-displayname)Added [PKPaymentMethod.network](https://developer.apple.com/documentation/passkit/pkpaymentmethod/1619209-network)Added [PKPaymentMethod.paymentPass](https://developer.apple.com/documentation/passkit/pkpaymentmethod/1619269-paymentpass)Added [PKPaymentMethod.type](https://developer.apple.com/documentation/passkit/pkpaymentmethod/1619279-type)Added [PKPaymentMethodType](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype)Added [PKPaymentMethodTypeCredit](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/credit)Added [PKPaymentMethodTypeDebit](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/pkpaymentmethodtypedebit)Added [PKPaymentMethodTypePrepaid](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/pkpaymentmethodtypeprepaid)Added [PKPaymentMethodTypeStore](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/pkpaymentmethodtypestore)Added [PKPaymentMethodTypeUnknown](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/pkpaymentmethodtypeunknown)

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

#### PKPaymentRequest.h (Added)

Added [PKPaymentRequest](https://developer.apple.com/documentation/passkit/pkpaymentrequest)Added [PKPaymentRequest.applicationData](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619298-applicationdata)Added [+[PKPaymentRequest availableNetworks]](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1833288-availablenetworks)Added [PKPaymentRequest.billingContact](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619221-billingcontact)Added [PKPaymentRequest.countryCode](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619246-countrycode)Added [PKPaymentRequest.currencyCode](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619248-currencycode)Added [PKPaymentRequest.merchantCapabilities](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619257-merchantcapabilities)Added [PKPaymentRequest.merchantIdentifier](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619305-merchantidentifier)Added [PKPaymentRequest.paymentSummaryItems](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619231-paymentsummaryitems)Added [PKPaymentRequest.requiredBillingAddressFields](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619265-requiredbillingaddressfields)Added [PKPaymentRequest.requiredShippingAddressFields](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619228-requiredshippingaddressfields)Added [PKPaymentRequest.shippingContact](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619245-shippingcontact)Added [PKPaymentRequest.shippingMethods](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619226-shippingmethods)Added [PKPaymentRequest.shippingType](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619330-shippingtype)Added [PKPaymentRequest.supportedNetworks](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619329-supportednetworks)Added [PKPaymentSummaryItem](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem)Added [PKPaymentSummaryItem.amount](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/1619291-amount)Added [PKPaymentSummaryItem.label](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/1619260-label)Added [+[PKPaymentSummaryItem summaryItemWithLabel:amount:]](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/1619275-init)Added [+[PKPaymentSummaryItem summaryItemWithLabel:amount:type:]](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/1619262-summaryitemwithlabel)Added [PKPaymentSummaryItem.type](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/1619327-type)Added [PKShippingMethod](https://developer.apple.com/documentation/passkit/pkshippingmethod)Added [PKShippingMethod.detail](https://developer.apple.com/documentation/passkit/pkshippingmethod/1619306-detail)Added [PKShippingMethod.identifier](https://developer.apple.com/documentation/passkit/pkshippingmethod/1619232-identifier)Added [PKAddressField](https://developer.apple.com/documentation/passkit/pkaddressfield)Added [PKAddressFieldAll](https://developer.apple.com/documentation/passkit/pkaddressfield/pkaddressfieldall)Added [PKAddressFieldEmail](https://developer.apple.com/documentation/passkit/pkaddressfield/pkaddressfieldemail)Added [PKAddressFieldName](https://developer.apple.com/documentation/passkit/pkaddressfield/1619276-name)Added [PKAddressFieldNone](https://developer.apple.com/documentation/passkit/pkaddressfield/pkaddressfieldnone)Added [PKAddressFieldPhone](https://developer.apple.com/documentation/passkit/pkaddressfield/1619308-phone)Added [PKAddressFieldPostalAddress](https://developer.apple.com/documentation/passkit/pkaddressfield/pkaddressfieldpostaladdress)Added [PKMerchantCapability](https://developer.apple.com/documentation/passkit/pkmerchantcapability)Added [PKMerchantCapability3DS](https://developer.apple.com/documentation/passkit/pkmerchantcapability/1619261-capability3ds)Added [PKMerchantCapabilityCredit](https://developer.apple.com/documentation/passkit/pkmerchantcapability/1619253-capabilitycredit)Added [PKMerchantCapabilityDebit](https://developer.apple.com/documentation/passkit/pkmerchantcapability/pkmerchantcapabilitydebit)Added [PKMerchantCapabilityEMV](https://developer.apple.com/documentation/passkit/pkmerchantcapability/pkmerchantcapabilityemv)Added [PKPaymentSummaryItemType](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitemtype)Added [PKPaymentSummaryItemTypeFinal](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitemtype/final)Added [PKPaymentSummaryItemTypePending](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitemtype/pkpaymentsummaryitemtypepending)Added [PKShippingType](https://developer.apple.com/documentation/passkit/pkshippingtype)Added [PKShippingTypeDelivery](https://developer.apple.com/documentation/passkit/pkshippingtype/delivery)Added [PKShippingTypeServicePickup](https://developer.apple.com/documentation/passkit/pkshippingtype/servicepickup)Added [PKShippingTypeShipping](https://developer.apple.com/documentation/passkit/pkshippingtype/shipping)Added [PKShippingTypeStorePickup](https://developer.apple.com/documentation/passkit/pkshippingtype/storepickup)

#### PKPaymentToken.h (Added)

Added [PKPaymentToken](https://developer.apple.com/documentation/passkit/pkpaymenttoken)Added [PKPaymentToken.paymentData](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1617000-paymentdata)Added [PKPaymentToken.paymentMethod](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1617002-paymentmethod)Added [PKPaymentToken.transactionIdentifier](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1617003-transactionidentifier)

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
