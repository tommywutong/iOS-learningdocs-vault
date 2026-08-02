---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/PassKit.html
archived_at: '2026-07-18T02:56:56.904643Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# PassKit Changes for Swift

### PassKit

Removed PKAddressField.init(_: UInt)Removed PKMerchantCapability.init(_: UInt)Added [PKAddPassButton](https://developer.apple.com/documentation/passkit/pkaddpassbutton)Added [PKAddPassButton.addPassButtonStyle](https://developer.apple.com/documentation/passkit/pkaddpassbutton/1618546-addpassbuttonstyle)Added [PKAddPassButton.init(addPassButtonStyle: PKAddPassButtonStyle)](https://developer.apple.com/documentation/passkit/pkaddpassbutton/1618547-initwithaddpassbuttonstyle)Added [PKAddPassButton.init(style: PKAddPassButtonStyle)](https://developer.apple.com/documentation/passkit/pkaddpassbutton/1618549-addpassbuttonwithstyle)Added [PKAddPassButtonStyle [enum]](https://developer.apple.com/documentation/passkit/pkaddpassbuttonstyle)Added [PKAddPassButtonStyle.Black](https://developer.apple.com/documentation/passkit/pkaddpassbuttonstyle/black)Added [PKAddPassButtonStyle.BlackOutline](https://developer.apple.com/documentation/passkit/pkaddpassbuttonstyle/pkaddpassbuttonstyleblackoutline)Added [PKAddPaymentPassError [enum]](https://developer.apple.com/documentation/passkit/pkaddpaymentpasserror)Added [PKAddPaymentPassError.SystemCancelled](https://developer.apple.com/documentation/passkit/pkaddpaymentpasserror/pkaddpaymentpasserrorsystemcancelled)Added [PKAddPaymentPassError.Unsupported](https://developer.apple.com/documentation/passkit/pkaddpaymentpasserror/unsupported)Added [PKAddPaymentPassError.UserCancelled](https://developer.apple.com/documentation/passkit/pkaddpaymentpasserror/usercancelled)Added [PKAddPaymentPassRequest](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest)Added [PKAddPaymentPassRequest.activationData](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest/1615914-activationdata)Added [PKAddPaymentPassRequest.encryptedPassData](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest/1615926-encryptedpassdata)Added [PKAddPaymentPassRequest.ephemeralPublicKey](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest/1615952-ephemeralpublickey)Added [PKAddPaymentPassRequest.init()](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest/1615919-init)Added [PKAddPaymentPassRequest.wrappedKey](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest/1615950-wrappedkey)Added [PKAddPaymentPassRequestConfiguration](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration)Added [PKAddPaymentPassRequestConfiguration.cardholderName](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/1615910-cardholdername)Added [PKAddPaymentPassRequestConfiguration.encryptionScheme](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/1615946-encryptionscheme)Added [PKAddPaymentPassRequestConfiguration.init(encryptionScheme: String)](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/1615930-initwithencryptionscheme)Added [PKAddPaymentPassRequestConfiguration.localizedDescription](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/1615932-localizeddescription)Added [PKAddPaymentPassRequestConfiguration.paymentNetwork](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/1615948-paymentnetwork)Added [PKAddPaymentPassRequestConfiguration.primaryAccountIdentifier](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/1615936-primaryaccountidentifier)Added [PKAddPaymentPassRequestConfiguration.primaryAccountSuffix](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/1615917-primaryaccountsuffix)Added [PKAddPaymentPassViewController](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontroller)Added [PKAddPaymentPassViewController.canAddPaymentPass() -> Bool [class]](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontroller/1615938-canaddpaymentpass)Added [PKAddPaymentPassViewController.delegate](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontroller/1615913-delegate)Added [PKAddPaymentPassViewController.init(requestConfiguration: PKAddPaymentPassRequestConfiguration, delegate: PKAddPaymentPassViewControllerDelegate?)](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontroller/1615922-initwithrequestconfiguration)Added [PKAddPaymentPassViewControllerDelegate](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontrollerdelegate)Added [PKAddPaymentPassViewControllerDelegate.addPaymentPassViewController(_: PKAddPaymentPassViewController, didFinishAddingPaymentPass: PKPaymentPass?, error: NSError?)](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontrollerdelegate/1615942-addpaymentpassviewcontroller)Added [PKAddPaymentPassViewControllerDelegate.addPaymentPassViewController(_: PKAddPaymentPassViewController, generateRequestWithCertificateChain: [NSData], nonce: NSData, nonceSignature: NSData, completionHandler: (PKAddPaymentPassRequest) -> Void)](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontrollerdelegate/1615915-addpaymentpassviewcontroller)Added [PKAutomaticPassPresentationSuppressionResult [enum]](https://developer.apple.com/documentation/passkit/pkautomaticpasspresentationsuppressionresult)Added [PKAutomaticPassPresentationSuppressionResult.AlreadyPresenting](https://developer.apple.com/documentation/passkit/pkautomaticpasspresentationsuppressionresult/alreadypresenting)Added [PKAutomaticPassPresentationSuppressionResult.Cancelled](https://developer.apple.com/documentation/passkit/pkautomaticpasspresentationsuppressionresult/cancelled)Added [PKAutomaticPassPresentationSuppressionResult.Denied](https://developer.apple.com/documentation/passkit/pkautomaticpasspresentationsuppressionresult/denied)Added [PKAutomaticPassPresentationSuppressionResult.NotSupported](https://developer.apple.com/documentation/passkit/pkautomaticpasspresentationsuppressionresult/pkautomaticpasspresentationsuppressionresultnotsupported)Added [PKAutomaticPassPresentationSuppressionResult.Success](https://developer.apple.com/documentation/passkit/pkautomaticpasspresentationsuppressionresult/success)Added [PKContact](https://developer.apple.com/documentation/passkit/pkcontact)Added [PKContact.emailAddress](https://developer.apple.com/documentation/passkit/pkcontact/1619273-emailaddress)Added [PKContact.name](https://developer.apple.com/documentation/passkit/pkcontact/1619318-name)Added [PKContact.phoneNumber](https://developer.apple.com/documentation/passkit/pkcontact/1619223-phonenumber)Added [PKContact.postalAddress](https://developer.apple.com/documentation/passkit/pkcontact/1619283-postaladdress)Added [PKMerchantCapability.CapabilityCredit](https://developer.apple.com/documentation/passkit/pkmerchantcapability/pkmerchantcapabilitycredit)Added [PKMerchantCapability.CapabilityDebit](https://developer.apple.com/documentation/passkit/pkmerchantcapability/pkmerchantcapabilitydebit)Added [PKPass.deviceName](https://developer.apple.com/documentation/passkit/pkpass/1618774-devicename)Added [PKPass.remotePass](https://developer.apple.com/documentation/passkit/pkpass/1618786-remotepass)Added [PKPassLibrary.canAddPaymentPassWithPrimaryAccountIdentifier(_: String) -> Bool](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617081-canaddpaymentpasswithprimaryacco)Added [PKPassLibrary.endAutomaticPassPresentationSuppressionWithRequestToken(_: PKSuppressionRequestToken) [class]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617097-endautomaticpasspresentationsupp)Added [PKPassLibrary.isPaymentPassActivationAvailable() -> Bool](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617107-ispaymentpassactivationavailable)Added [PKPassLibrary.isSuppressingAutomaticPassPresentation() -> Bool [class]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617092-issuppressingautomaticpasspresen)Added [PKPassLibrary.remotePaymentPasses() -> [PKPaymentPass]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617099-remotepaymentpasses)Added [PKPassLibrary.requestAutomaticPassPresentationSuppressionWithResponseHandler(_: (PKAutomaticPassPresentationSuppressionResult) -> Void) -> PKSuppressionRequestToken [class]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617078-requestautomaticpasspresentation)Added [PKPayment.billingContact](https://developer.apple.com/documentation/passkit/pkpayment/1619320-billingcontact)Added [PKPayment.shippingContact](https://developer.apple.com/documentation/passkit/pkpayment/1619250-shippingcontact)Added [PKPaymentAuthorizationViewController.canMakePaymentsUsingNetworks(_: [String], capabilities: PKMerchantCapability) -> Bool [class]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller/1616181-canmakepaymentsusingnetworks)Added [PKPaymentAuthorizationViewControllerDelegate.paymentAuthorizationViewController(_: PKPaymentAuthorizationViewController, didSelectPaymentMethod: PKPaymentMethod, completion: ([PKPaymentSummaryItem]) -> Void)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616184-paymentauthorizationviewcontroll)Added [PKPaymentAuthorizationViewControllerDelegate.paymentAuthorizationViewController(_: PKPaymentAuthorizationViewController, didSelectShippingContact: PKContact, completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616198-paymentauthorizationviewcontroll)Added [PKPaymentButton.init(paymentButtonType: PKPaymentButtonType, paymentButtonStyle: PKPaymentButtonStyle)](https://developer.apple.com/documentation/passkit/pkpaymentbutton/1617842-init)Added [PKPaymentButtonType.SetUp](https://developer.apple.com/documentation/passkit/pkpaymentbuttontype/setup)Added [PKPaymentMethod](https://developer.apple.com/documentation/passkit/pkpaymentmethod)Added [PKPaymentMethod.displayName](https://developer.apple.com/documentation/passkit/pkpaymentmethod/1619249-displayname)Added [PKPaymentMethod.network](https://developer.apple.com/documentation/passkit/pkpaymentmethod/1619209-network)Added [PKPaymentMethod.paymentPass](https://developer.apple.com/documentation/passkit/pkpaymentmethod/1619269-paymentpass)Added [PKPaymentMethod.type](https://developer.apple.com/documentation/passkit/pkpaymentmethod/1619279-type)Added [PKPaymentMethodType [struct]](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype)Added [PKPaymentMethodType.Credit](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/pkpaymentmethodtypecredit)Added [PKPaymentMethodType.Debit](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/debit)Added PKPaymentMethodType.init(rawValue: UInt)Added [PKPaymentMethodType.Prepaid](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/pkpaymentmethodtypeprepaid)Added [PKPaymentMethodType.Store](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/pkpaymentmethodtypestore)Added [PKPaymentMethodType.Unknown](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/unknown)Added [PKPaymentRequest.billingContact](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619221-billingcontact)Added [PKPaymentRequest.shippingContact](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619245-shippingcontact)Added [PKPaymentSummaryItem.init(label: String, amount: NSDecimalNumber, type: PKPaymentSummaryItemType)](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/1619262-summaryitemwithlabel)Added [PKPaymentSummaryItem.type](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/1619327-type)Added [PKPaymentSummaryItemType [enum]](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitemtype)Added [PKPaymentSummaryItemType.Final](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitemtype/pkpaymentsummaryitemtypefinal)Added [PKPaymentSummaryItemType.Pending](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitemtype/pkpaymentsummaryitemtypepending)Added [PKPaymentToken.paymentMethod](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1617002-paymentmethod)Added [PKEncryptionSchemeECC_V2](https://developer.apple.com/documentation/passkit/pkencryptionschemeecc_v2)Added [PKPassLibraryRemotePaymentPassesDidChangeNotification](https://developer.apple.com/documentation/passkit/pkpasslibraryremotepaymentpassesdidchangenotification)Added [PKPaymentNetworkDiscover](https://developer.apple.com/documentation/passkit/pkpaymentnetworkdiscover)Added [PKPaymentNetworkPrivateLabel](https://developer.apple.com/documentation/passkit/pkpaymentnetwork/1618639-privatelabel)Added [PKSuppressionRequestToken](https://developer.apple.com/documentation/passkit/pksuppressionrequesttoken)Modified [PKAddPassesViewController](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class PKAddPassesViewController : UIViewController {     init!(pass pass: AnyObject!)     init!(passes passes: [AnyObject]!)     class func canAddPasses() -> Bool     unowned(unsafe) var delegate: PKAddPassesViewControllerDelegate! } ``` |
| To | ``` class PKAddPassesViewController : UIViewController {     init(pass pass: PKPass)     init(passes passes: [PKPass])     class func canAddPasses() -> Bool     unowned(unsafe) var delegate: PKAddPassesViewControllerDelegate? } ``` |

Modified [PKAddPassesViewController.delegate](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller/1619220-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: PKAddPassesViewControllerDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: PKAddPassesViewControllerDelegate? ``` |

Modified [PKAddPassesViewController.init(pass: PKPass)](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller/1619251-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(pass pass: AnyObject!) ``` |
| To | ``` init(pass pass: PKPass) ``` |

Modified [PKAddPassesViewController.init(passes: [PKPass])](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller/1619217-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(passes passes: [AnyObject]!) ``` |
| To | ``` init(passes passes: [PKPass]) ``` |

Modified [PKAddPassesViewControllerDelegate](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol PKAddPassesViewControllerDelegate : NSObjectProtocol {     optional func addPassesViewControllerDidFinish(_ controller: PKAddPassesViewController!) } ``` |
| To | ``` protocol PKAddPassesViewControllerDelegate : NSObjectProtocol {     optional func addPassesViewControllerDidFinish(_ controller: PKAddPassesViewController) } ``` |

Modified [PKAddPassesViewControllerDelegate.addPassesViewControllerDidFinish(_: PKAddPassesViewController)](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontrollerdelegate/1619236-addpassesviewcontrollerdidfinish)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func addPassesViewControllerDidFinish(_ controller: PKAddPassesViewController!) ``` | iOS 8.0 |
| To | ``` optional func addPassesViewControllerDidFinish(_ controller: PKAddPassesViewController) ``` | iOS 6.0 |

Modified [PKAddressField [struct]](https://developer.apple.com/documentation/passkit/pkaddressfield)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct PKAddressField : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: PKAddressField { get }     static var PostalAddress: PKAddressField { get }     static var Phone: PKAddressField { get }     static var Email: PKAddressField { get }     static var Name: PKAddressField { get }     static var All: PKAddressField { get } } ``` | RawOptionSetType |
| To | ``` struct PKAddressField : OptionSetType {     init(rawValue rawValue: UInt)     static var None: PKAddressField { get }     static var PostalAddress: PKAddressField { get }     static var Phone: PKAddressField { get }     static var Email: PKAddressField { get }     static var Name: PKAddressField { get }     static var All: PKAddressField { get } } ``` | OptionSetType |

Modified [PKMerchantCapability [struct]](https://developer.apple.com/documentation/passkit/pkmerchantcapability)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct PKMerchantCapability : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Capability3DS: PKMerchantCapability { get }     static var CapabilityEMV: PKMerchantCapability { get } } ``` | RawOptionSetType |
| To | ``` struct PKMerchantCapability : OptionSetType {     init(rawValue rawValue: UInt)     static var Capability3DS: PKMerchantCapability { get }     static var CapabilityEMV: PKMerchantCapability { get }     static var CapabilityCredit: PKMerchantCapability { get }     static var CapabilityDebit: PKMerchantCapability { get } } ``` | OptionSetType |

Modified [PKPass](https://developer.apple.com/documentation/passkit/pkpass)

|  | Declaration |
| --- | --- |
| From | ``` class PKPass : PKObject {     init!(data data: NSData!, error error: NSErrorPointer)     var passType: PKPassType { get }     unowned(unsafe) var paymentPass: PKPaymentPass! { get }     var serialNumber: String! { get }     var passTypeIdentifier: String! { get }     @NSCopying var webServiceURL: NSURL! { get }     var authenticationToken: String! { get }     @NSCopying var icon: UIImage! { get }     var localizedName: String! { get }     var localizedDescription: String! { get }     var organizationName: String! { get }     @NSCopying var relevantDate: NSDate! { get }     var userInfo: [NSObject : AnyObject]! { get }     @NSCopying var passURL: NSURL! { get }     func localizedValueForFieldKey(_ key: String!) -> AnyObject! } ``` |
| To | ``` class PKPass : PKObject {     init(data data: NSData, error error: NSErrorPointer)     var passType: PKPassType { get }     unowned(unsafe) var paymentPass: PKPaymentPass? { get }     var serialNumber: String { get }     var passTypeIdentifier: String { get }     @NSCopying var webServiceURL: NSURL? { get }     var authenticationToken: String? { get }     @NSCopying var icon: UIImage { get }     var localizedName: String { get }     var localizedDescription: String { get }     var organizationName: String { get }     @NSCopying var relevantDate: NSDate? { get }     var userInfo: [NSObject : AnyObject]? { get }     @NSCopying var passURL: NSURL { get }     var remotePass: Bool { get }     var deviceName: String { get }     func localizedValueForFieldKey(_ key: String) -> AnyObject? } ``` |

Modified [PKPass.authenticationToken](https://developer.apple.com/documentation/passkit/pkpass/1618766-authenticationtoken)

|  | Declaration |
| --- | --- |
| From | ``` var authenticationToken: String! { get } ``` |
| To | ``` var authenticationToken: String? { get } ``` |

Modified [PKPass.icon](https://developer.apple.com/documentation/passkit/pkpass/1618762-icon)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var icon: UIImage! { get } ``` |
| To | ``` @NSCopying var icon: UIImage { get } ``` |

Modified [PKPass.init(data: NSData, error: NSErrorPointer)](https://developer.apple.com/documentation/passkit/pkpass/1618792-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(data data: NSData!, error error: NSErrorPointer) ``` |
| To | ``` init(data data: NSData, error error: NSErrorPointer) ``` |

Modified [PKPass.localizedDescription](https://developer.apple.com/documentation/passkit/pkpass/1618770-localizeddescription)

|  | Declaration |
| --- | --- |
| From | ``` var localizedDescription: String! { get } ``` |
| To | ``` var localizedDescription: String { get } ``` |

Modified [PKPass.localizedName](https://developer.apple.com/documentation/passkit/pkpass/1618768-localizedname)

|  | Declaration |
| --- | --- |
| From | ``` var localizedName: String! { get } ``` |
| To | ``` var localizedName: String { get } ``` |

Modified [PKPass.localizedValueForFieldKey(_: String) -> AnyObject?](https://developer.apple.com/documentation/passkit/pkpass/1618798-localizedvalueforfieldkey)

|  | Declaration |
| --- | --- |
| From | ``` func localizedValueForFieldKey(_ key: String!) -> AnyObject! ``` |
| To | ``` func localizedValueForFieldKey(_ key: String) -> AnyObject? ``` |

Modified [PKPass.organizationName](https://developer.apple.com/documentation/passkit/pkpass/1618778-organizationname)

|  | Declaration |
| --- | --- |
| From | ``` var organizationName: String! { get } ``` |
| To | ``` var organizationName: String { get } ``` |

Modified [PKPass.passTypeIdentifier](https://developer.apple.com/documentation/passkit/pkpass/1618783-passtypeidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var passTypeIdentifier: String! { get } ``` |
| To | ``` var passTypeIdentifier: String { get } ``` |

Modified [PKPass.passURL](https://developer.apple.com/documentation/passkit/pkpass/1618781-passurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var passURL: NSURL! { get } ``` |
| To | ``` @NSCopying var passURL: NSURL { get } ``` |

Modified [PKPass.paymentPass](https://developer.apple.com/documentation/passkit/pkpass/1618784-paymentpass)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var paymentPass: PKPaymentPass! { get } ``` |
| To | ``` unowned(unsafe) var paymentPass: PKPaymentPass? { get } ``` |

Modified [PKPass.relevantDate](https://developer.apple.com/documentation/passkit/pkpass/1618776-relevantdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var relevantDate: NSDate! { get } ``` |
| To | ``` @NSCopying var relevantDate: NSDate? { get } ``` |

Modified [PKPass.serialNumber](https://developer.apple.com/documentation/passkit/pkpass/1618788-serialnumber)

|  | Declaration |
| --- | --- |
| From | ``` var serialNumber: String! { get } ``` |
| To | ``` var serialNumber: String { get } ``` |

Modified [PKPass.userInfo](https://developer.apple.com/documentation/passkit/pkpass/1618794-userinfo)

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]! { get } ``` |
| To | ``` var userInfo: [NSObject : AnyObject]? { get } ``` |

Modified [PKPass.webServiceURL](https://developer.apple.com/documentation/passkit/pkpass/1618772-webserviceurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var webServiceURL: NSURL! { get } ``` |
| To | ``` @NSCopying var webServiceURL: NSURL? { get } ``` |

Modified [PKPassKitErrorCode [enum]](https://developer.apple.com/documentation/passkit/pkpasskiterrorcode)

|  | Declaration | Protocols | Raw Value Type |
| --- | --- | --- | --- |
| From | ``` enum PKPassKitErrorCode : Int {     case UnknownError     case InvalidDataError     case UnsupportedVersionError     case InvalidSignature     case NotEntitledError } ``` | Equatable, Hashable, RawRepresentable | -- |
| To | ``` enum PKPassKitErrorCode : Int {     case UnknownError     case InvalidDataError     case UnsupportedVersionError     case InvalidSignature     case NotEntitledError } extension PKPassKitErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension PKPassKitErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable | Int |

Modified [PKPassLibrary](https://developer.apple.com/documentation/passkit/pkpasslibrary)

|  | Declaration |
| --- | --- |
| From | ``` class PKPassLibrary : NSObject {     class func isPassLibraryAvailable() -> Bool     func passes() -> [AnyObject]!     func passWithPassTypeIdentifier(_ identifier: String!, serialNumber serialNumber: String!) -> PKPass!     func passesOfType(_ passType: PKPassType) -> [AnyObject]!     func removePass(_ pass: PKPass!)     func containsPass(_ pass: PKPass!) -> Bool     func replacePassWithPass(_ pass: PKPass!) -> Bool     func addPasses(_ passes: [AnyObject]!, withCompletionHandler completion: ((PKPassLibraryAddPassesStatus) -> Void)!)     class func isPaymentPassActivationAvailable() -> Bool     func openPaymentSetup()     func activatePaymentPass(_ paymentPass: PKPaymentPass!, withActivationData activationData: NSData!, completion completion: ((Bool, NSError!) -> Void)!)     func activatePaymentPass(_ paymentPass: PKPaymentPass!, withActivationCode activationCode: String!, completion completion: ((Bool, NSError!) -> Void)!) } ``` |
| To | ``` class PKPassLibrary : NSObject {     class func isPassLibraryAvailable() -> Bool     class func requestAutomaticPassPresentationSuppressionWithResponseHandler(_ responseHandler: (PKAutomaticPassPresentationSuppressionResult) -> Void) -> PKSuppressionRequestToken     class func endAutomaticPassPresentationSuppressionWithRequestToken(_ requestToken: PKSuppressionRequestToken)     class func isSuppressingAutomaticPassPresentation() -> Bool     class func isPaymentPassActivationAvailable() -> Bool     func isPaymentPassActivationAvailable() -> Bool     func passes() -> [PKPass]     func passWithPassTypeIdentifier(_ identifier: String, serialNumber serialNumber: String) -> PKPass?     func passesOfType(_ passType: PKPassType) -> [PKPass]     func remotePaymentPasses() -> [PKPaymentPass]     func removePass(_ pass: PKPass)     func containsPass(_ pass: PKPass) -> Bool     func replacePassWithPass(_ pass: PKPass) -> Bool     func addPasses(_ passes: [PKPass], withCompletionHandler completion: ((PKPassLibraryAddPassesStatus) -> Void)?)     func openPaymentSetup()     func canAddPaymentPassWithPrimaryAccountIdentifier(_ primaryAccountIdentifier: String) -> Bool     func activatePaymentPass(_ paymentPass: PKPaymentPass, withActivationData activationData: NSData, completion completion: ((Bool, NSError) -> Void)?)     func activatePaymentPass(_ paymentPass: PKPaymentPass, withActivationCode activationCode: String, completion completion: ((Bool, NSError) -> Void)?) } ``` |

Modified [PKPassLibrary.activatePaymentPass(_: PKPaymentPass, withActivationCode: String, completion: ((Bool, NSError) -> Void)?)](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617079-activate)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func activatePaymentPass(_ paymentPass: PKPaymentPass!, withActivationCode activationCode: String!, completion completion: ((Bool, NSError!) -> Void)!) ``` | -- |
| To | ``` func activatePaymentPass(_ paymentPass: PKPaymentPass, withActivationCode activationCode: String, completion completion: ((Bool, NSError) -> Void)?) ``` | iOS 9.0 |

Modified [PKPassLibrary.activatePaymentPass(_: PKPaymentPass, withActivationData: NSData, completion: ((Bool, NSError) -> Void)?)](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617088-activate)

|  | Declaration |
| --- | --- |
| From | ``` func activatePaymentPass(_ paymentPass: PKPaymentPass!, withActivationData activationData: NSData!, completion completion: ((Bool, NSError!) -> Void)!) ``` |
| To | ``` func activatePaymentPass(_ paymentPass: PKPaymentPass, withActivationData activationData: NSData, completion completion: ((Bool, NSError) -> Void)?) ``` |

Modified [PKPassLibrary.addPasses(_: [PKPass], withCompletionHandler: ((PKPassLibraryAddPassesStatus) -> Void)?)](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617093-addpasses)

|  | Declaration |
| --- | --- |
| From | ``` func addPasses(_ passes: [AnyObject]!, withCompletionHandler completion: ((PKPassLibraryAddPassesStatus) -> Void)!) ``` |
| To | ``` func addPasses(_ passes: [PKPass], withCompletionHandler completion: ((PKPassLibraryAddPassesStatus) -> Void)?) ``` |

Modified [PKPassLibrary.containsPass(_: PKPass) -> Bool](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617110-containspass)

|  | Declaration |
| --- | --- |
| From | ``` func containsPass(_ pass: PKPass!) -> Bool ``` |
| To | ``` func containsPass(_ pass: PKPass) -> Bool ``` |

Modified [PKPassLibrary.isPassLibraryAvailable() -> Bool [class]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617080-ispasslibraryavailable)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [PKPassLibrary.isPaymentPassActivationAvailable() -> Bool [class]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617108-ispaymentpassactivationavailable)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [PKPassLibrary.passes() -> [PKPass]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617109-passes)

|  | Declaration |
| --- | --- |
| From | ``` func passes() -> [AnyObject]! ``` |
| To | ``` func passes() -> [PKPass] ``` |

Modified [PKPassLibrary.passesOfType(_: PKPassType) -> [PKPass]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617074-passes)

|  | Declaration |
| --- | --- |
| From | ``` func passesOfType(_ passType: PKPassType) -> [AnyObject]! ``` |
| To | ``` func passesOfType(_ passType: PKPassType) -> [PKPass] ``` |

Modified [PKPassLibrary.passWithPassTypeIdentifier(_: String, serialNumber: String) -> PKPass?](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617104-passwithpasstypeidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func passWithPassTypeIdentifier(_ identifier: String!, serialNumber serialNumber: String!) -> PKPass! ``` |
| To | ``` func passWithPassTypeIdentifier(_ identifier: String, serialNumber serialNumber: String) -> PKPass? ``` |

Modified [PKPassLibrary.removePass(_: PKPass)](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617083-removepass)

|  | Declaration |
| --- | --- |
| From | ``` func removePass(_ pass: PKPass!) ``` |
| To | ``` func removePass(_ pass: PKPass) ``` |

Modified [PKPassLibrary.replacePassWithPass(_: PKPass) -> Bool](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617082-replacepasswithpass)

|  | Declaration |
| --- | --- |
| From | ``` func replacePassWithPass(_ pass: PKPass!) -> Bool ``` |
| To | ``` func replacePassWithPass(_ pass: PKPass) -> Bool ``` |

Modified [PKPassLibraryAddPassesStatus [enum]](https://developer.apple.com/documentation/passkit/pkpasslibraryaddpassesstatus)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [PKPassType [enum]](https://developer.apple.com/documentation/passkit/pkpasstype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [PKPayment](https://developer.apple.com/documentation/passkit/pkpayment)

|  | Declaration |
| --- | --- |
| From | ``` class PKPayment : NSObject {     var token: PKPaymentToken! { get }     var billingAddress: ABRecord! { get }     var shippingAddress: ABRecord! { get }     var shippingMethod: PKShippingMethod! { get } } ``` |
| To | ``` class PKPayment : NSObject {     var token: PKPaymentToken { get }     var billingAddress: ABRecord? { get }     var billingContact: PKContact? { get }     var shippingAddress: ABRecord? { get }     var shippingContact: PKContact? { get }     var shippingMethod: PKShippingMethod? { get } } ``` |

Modified [PKPayment.billingAddress](https://developer.apple.com/documentation/passkit/pkpayment/1619307-billingaddress)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var billingAddress: ABRecord! { get } ``` | -- |
| To | ``` var billingAddress: ABRecord? { get } ``` | iOS 9.0 |

Modified [PKPayment.shippingAddress](https://developer.apple.com/documentation/passkit/pkpayment/1619271-shippingaddress)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var shippingAddress: ABRecord! { get } ``` | -- |
| To | ``` var shippingAddress: ABRecord? { get } ``` | iOS 9.0 |

Modified [PKPayment.shippingMethod](https://developer.apple.com/documentation/passkit/pkpayment/1619268-shippingmethod)

|  | Declaration |
| --- | --- |
| From | ``` var shippingMethod: PKShippingMethod! { get } ``` |
| To | ``` var shippingMethod: PKShippingMethod? { get } ``` |

Modified [PKPayment.token](https://developer.apple.com/documentation/passkit/pkpayment/1619239-token)

|  | Declaration |
| --- | --- |
| From | ``` var token: PKPaymentToken! { get } ``` |
| To | ``` var token: PKPaymentToken { get } ``` |

Modified [PKPaymentAuthorizationStatus [enum]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [PKPaymentAuthorizationViewController](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class PKPaymentAuthorizationViewController : UIViewController {     class func canMakePayments() -> Bool     class func canMakePaymentsUsingNetworks(_ supportedNetworks: [AnyObject]!) -> Bool     unowned(unsafe) var delegate: PKPaymentAuthorizationViewControllerDelegate!     init!(paymentRequest request: PKPaymentRequest!) } ``` |
| To | ``` class PKPaymentAuthorizationViewController : UIViewController {     class func canMakePayments() -> Bool     class func canMakePaymentsUsingNetworks(_ supportedNetworks: [String]) -> Bool     class func canMakePaymentsUsingNetworks(_ supportedNetworks: [String], capabilities capabilties: PKMerchantCapability) -> Bool     unowned(unsafe) var delegate: PKPaymentAuthorizationViewControllerDelegate?     init(paymentRequest request: PKPaymentRequest) } ``` |

Modified [PKPaymentAuthorizationViewController.canMakePaymentsUsingNetworks(_: [String]) -> Bool [class]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller/1616187-canmakepaymentsusingnetworks)

|  | Declaration |
| --- | --- |
| From | ``` class func canMakePaymentsUsingNetworks(_ supportedNetworks: [AnyObject]!) -> Bool ``` |
| To | ``` class func canMakePaymentsUsingNetworks(_ supportedNetworks: [String]) -> Bool ``` |

Modified [PKPaymentAuthorizationViewController.delegate](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller/1616199-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: PKPaymentAuthorizationViewControllerDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: PKPaymentAuthorizationViewControllerDelegate? ``` |

Modified [PKPaymentAuthorizationViewController.init(paymentRequest: PKPaymentRequest)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller/1616178-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(paymentRequest request: PKPaymentRequest!) ``` |
| To | ``` init(paymentRequest request: PKPaymentRequest) ``` |

Modified [PKPaymentAuthorizationViewControllerDelegate](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol PKPaymentAuthorizationViewControllerDelegate : NSObjectProtocol {     func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController!, didAuthorizePayment payment: PKPayment!, completion completion: ((PKPaymentAuthorizationStatus) -> Void)!)     func paymentAuthorizationViewControllerDidFinish(_ controller: PKPaymentAuthorizationViewController!)     optional func paymentAuthorizationViewControllerWillAuthorizePayment(_ controller: PKPaymentAuthorizationViewController!)     optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController!, didSelectShippingMethod shippingMethod: PKShippingMethod!, completion completion: ((PKPaymentAuthorizationStatus, [AnyObject]!) -> Void)!)     optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController!, didSelectShippingAddress address: ABRecord!, completion completion: ((PKPaymentAuthorizationStatus, [AnyObject]!, [AnyObject]!) -> Void)!) } ``` |
| To | ``` protocol PKPaymentAuthorizationViewControllerDelegate : NSObjectProtocol {     func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didAuthorizePayment payment: PKPayment, completion completion: (PKPaymentAuthorizationStatus) -> Void)     func paymentAuthorizationViewControllerDidFinish(_ controller: PKPaymentAuthorizationViewController)     optional func paymentAuthorizationViewControllerWillAuthorizePayment(_ controller: PKPaymentAuthorizationViewController)     optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelectShippingMethod shippingMethod: PKShippingMethod, completion completion: (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem]) -> Void)     optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelectShippingAddress address: ABRecord, completion completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void)     optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelectShippingContact contact: PKContact, completion completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void)     optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelectPaymentMethod paymentMethod: PKPaymentMethod, completion completion: ([PKPaymentSummaryItem]) -> Void) } ``` |

Modified [PKPaymentAuthorizationViewControllerDelegate.paymentAuthorizationViewController(_: PKPaymentAuthorizationViewController, didAuthorizePayment: PKPayment, completion: (PKPaymentAuthorizationStatus) -> Void)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616195-paymentauthorizationviewcontroll)

|  | Declaration |
| --- | --- |
| From | ``` func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController!, didAuthorizePayment payment: PKPayment!, completion completion: ((PKPaymentAuthorizationStatus) -> Void)!) ``` |
| To | ``` func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didAuthorizePayment payment: PKPayment, completion completion: (PKPaymentAuthorizationStatus) -> Void) ``` |

Modified [PKPaymentAuthorizationViewControllerDelegate.paymentAuthorizationViewController(_: PKPaymentAuthorizationViewController, didSelectShippingAddress: ABRecord, completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616196-paymentauthorizationviewcontroll)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController!, didSelectShippingAddress address: ABRecord!, completion completion: ((PKPaymentAuthorizationStatus, [AnyObject]!, [AnyObject]!) -> Void)!) ``` | -- |
| To | ``` optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelectShippingAddress address: ABRecord, completion completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void) ``` | iOS 9.0 |

Modified [PKPaymentAuthorizationViewControllerDelegate.paymentAuthorizationViewController(_: PKPaymentAuthorizationViewController, didSelectShippingMethod: PKShippingMethod, completion: (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem]) -> Void)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616186-paymentauthorizationviewcontroll)

|  | Declaration |
| --- | --- |
| From | ``` optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController!, didSelectShippingMethod shippingMethod: PKShippingMethod!, completion completion: ((PKPaymentAuthorizationStatus, [AnyObject]!) -> Void)!) ``` |
| To | ``` optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelectShippingMethod shippingMethod: PKShippingMethod, completion completion: (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem]) -> Void) ``` |

Modified [PKPaymentAuthorizationViewControllerDelegate.paymentAuthorizationViewControllerDidFinish(_: PKPaymentAuthorizationViewController)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616180-paymentauthorizationviewcontroll)

|  | Declaration |
| --- | --- |
| From | ``` func paymentAuthorizationViewControllerDidFinish(_ controller: PKPaymentAuthorizationViewController!) ``` |
| To | ``` func paymentAuthorizationViewControllerDidFinish(_ controller: PKPaymentAuthorizationViewController) ``` |

Modified [PKPaymentAuthorizationViewControllerDelegate.paymentAuthorizationViewControllerWillAuthorizePayment(_: PKPaymentAuthorizationViewController)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616179-paymentauthorizationviewcontroll)

|  | Declaration |
| --- | --- |
| From | ``` optional func paymentAuthorizationViewControllerWillAuthorizePayment(_ controller: PKPaymentAuthorizationViewController!) ``` |
| To | ``` optional func paymentAuthorizationViewControllerWillAuthorizePayment(_ controller: PKPaymentAuthorizationViewController) ``` |

Modified [PKPaymentButton](https://developer.apple.com/documentation/passkit/pkpaymentbutton)

|  | Declaration |
| --- | --- |
| From | ``` class PKPaymentButton : UIButton {     convenience init!(type buttonType: PKPaymentButtonType, style buttonStyle: PKPaymentButtonStyle)     class func buttonWithType(_ buttonType: PKPaymentButtonType, style buttonStyle: PKPaymentButtonStyle) -> Self! } ``` |
| To | ``` class PKPaymentButton : UIButton {     convenience init(type buttonType: PKPaymentButtonType, style buttonStyle: PKPaymentButtonStyle)     class func buttonWithType(_ buttonType: PKPaymentButtonType, style buttonStyle: PKPaymentButtonStyle) -> Self     init(paymentButtonType type: PKPaymentButtonType, paymentButtonStyle style: PKPaymentButtonStyle) } ``` |

Modified [PKPaymentButton.init(type: PKPaymentButtonType, style: PKPaymentButtonStyle)](https://developer.apple.com/documentation/passkit/pkpaymentbutton/1617848-buttonwithtype)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(type buttonType: PKPaymentButtonType, style buttonStyle: PKPaymentButtonStyle) ``` |
| To | ``` convenience init(type buttonType: PKPaymentButtonType, style buttonStyle: PKPaymentButtonStyle) ``` |

Modified [PKPaymentButtonStyle [enum]](https://developer.apple.com/documentation/passkit/pkpaymentbuttonstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [PKPaymentButtonType [enum]](https://developer.apple.com/documentation/passkit/pkpaymentbuttontype)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum PKPaymentButtonType : Int {     case Plain     case Buy } ``` | -- |
| To | ``` enum PKPaymentButtonType : Int {     case Plain     case Buy     case SetUp } ``` | Int |

Modified [PKPaymentPass](https://developer.apple.com/documentation/passkit/pkpaymentpass)

|  | Declaration |
| --- | --- |
| From | ``` class PKPaymentPass : PKPass {     var primaryAccountIdentifier: String! { get }     var primaryAccountNumberSuffix: String! { get }     var deviceAccountIdentifier: String! { get }     var deviceAccountNumberSuffix: String! { get }     var activationState: PKPaymentPassActivationState { get } } ``` |
| To | ``` class PKPaymentPass : PKPass {     var primaryAccountIdentifier: String { get }     var primaryAccountNumberSuffix: String { get }     var deviceAccountIdentifier: String { get }     var deviceAccountNumberSuffix: String { get }     var activationState: PKPaymentPassActivationState { get } } ``` |

Modified [PKPaymentPass.deviceAccountIdentifier](https://developer.apple.com/documentation/passkit/pkpaymentpass/1619074-deviceaccountidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var deviceAccountIdentifier: String! { get } ``` |
| To | ``` var deviceAccountIdentifier: String { get } ``` |

Modified [PKPaymentPass.deviceAccountNumberSuffix](https://developer.apple.com/documentation/passkit/pkpaymentpass/1619075-deviceaccountnumbersuffix)

|  | Declaration |
| --- | --- |
| From | ``` var deviceAccountNumberSuffix: String! { get } ``` |
| To | ``` var deviceAccountNumberSuffix: String { get } ``` |

Modified [PKPaymentPass.primaryAccountIdentifier](https://developer.apple.com/documentation/passkit/pkpaymentpass/1619084-primaryaccountidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var primaryAccountIdentifier: String! { get } ``` |
| To | ``` var primaryAccountIdentifier: String { get } ``` |

Modified [PKPaymentPass.primaryAccountNumberSuffix](https://developer.apple.com/documentation/passkit/pkpaymentpass/1619081-primaryaccountnumbersuffix)

|  | Declaration |
| --- | --- |
| From | ``` var primaryAccountNumberSuffix: String! { get } ``` |
| To | ``` var primaryAccountNumberSuffix: String { get } ``` |

Modified [PKPaymentPassActivationState [enum]](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [PKPaymentRequest](https://developer.apple.com/documentation/passkit/pkpaymentrequest)

|  | Declaration |
| --- | --- |
| From | ``` class PKPaymentRequest : NSObject {     var merchantIdentifier: String!     var countryCode: String!     var supportedNetworks: [AnyObject]!     var merchantCapabilities: PKMerchantCapability     var paymentSummaryItems: [AnyObject]!     var currencyCode: String!     var requiredBillingAddressFields: PKAddressField     unowned(unsafe) var billingAddress: ABRecord!     var requiredShippingAddressFields: PKAddressField     unowned(unsafe) var shippingAddress: ABRecord!     var shippingMethods: [AnyObject]!     var shippingType: PKShippingType     @NSCopying var applicationData: NSData! } ``` |
| To | ``` class PKPaymentRequest : NSObject {     var merchantIdentifier: String     var countryCode: String     var supportedNetworks: [String]     var merchantCapabilities: PKMerchantCapability     var paymentSummaryItems: [PKPaymentSummaryItem]     var currencyCode: String     var requiredBillingAddressFields: PKAddressField     unowned(unsafe) var billingAddress: ABRecord?     var billingContact: PKContact?     var requiredShippingAddressFields: PKAddressField     unowned(unsafe) var shippingAddress: ABRecord?     var shippingContact: PKContact?     var shippingMethods: [PKShippingMethod]?     var shippingType: PKShippingType     @NSCopying var applicationData: NSData? } ``` |

Modified [PKPaymentRequest.applicationData](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619298-applicationdata)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var applicationData: NSData! ``` |
| To | ``` @NSCopying var applicationData: NSData? ``` |

Modified [PKPaymentRequest.billingAddress](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619229-billingaddress)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` unowned(unsafe) var billingAddress: ABRecord! ``` | -- |
| To | ``` unowned(unsafe) var billingAddress: ABRecord? ``` | iOS 9.0 |

Modified [PKPaymentRequest.countryCode](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619246-countrycode)

|  | Declaration |
| --- | --- |
| From | ``` var countryCode: String! ``` |
| To | ``` var countryCode: String ``` |

Modified [PKPaymentRequest.currencyCode](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619248-currencycode)

|  | Declaration |
| --- | --- |
| From | ``` var currencyCode: String! ``` |
| To | ``` var currencyCode: String ``` |

Modified [PKPaymentRequest.merchantIdentifier](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619305-merchantidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var merchantIdentifier: String! ``` |
| To | ``` var merchantIdentifier: String ``` |

Modified [PKPaymentRequest.paymentSummaryItems](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619231-paymentsummaryitems)

|  | Declaration |
| --- | --- |
| From | ``` var paymentSummaryItems: [AnyObject]! ``` |
| To | ``` var paymentSummaryItems: [PKPaymentSummaryItem] ``` |

Modified [PKPaymentRequest.shippingAddress](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619216-shippingaddress)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` unowned(unsafe) var shippingAddress: ABRecord! ``` | -- |
| To | ``` unowned(unsafe) var shippingAddress: ABRecord? ``` | iOS 9.0 |

Modified [PKPaymentRequest.shippingMethods](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619226-shippingmethods)

|  | Declaration |
| --- | --- |
| From | ``` var shippingMethods: [AnyObject]! ``` |
| To | ``` var shippingMethods: [PKShippingMethod]? ``` |

Modified [PKPaymentRequest.supportedNetworks](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619329-supportednetworks)

|  | Declaration |
| --- | --- |
| From | ``` var supportedNetworks: [AnyObject]! ``` |
| To | ``` var supportedNetworks: [String] ``` |

Modified [PKPaymentSummaryItem](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem)

|  | Declaration |
| --- | --- |
| From | ``` class PKPaymentSummaryItem : NSObject {     convenience init!(label label: String!, amount amount: NSDecimalNumber!)     class func summaryItemWithLabel(_ label: String!, amount amount: NSDecimalNumber!) -> Self!     var label: String!     @NSCopying var amount: NSDecimalNumber! } ``` |
| To | ``` class PKPaymentSummaryItem : NSObject {     convenience init(label label: String, amount amount: NSDecimalNumber)     class func summaryItemWithLabel(_ label: String, amount amount: NSDecimalNumber) -> Self     convenience init(label label: String, amount amount: NSDecimalNumber, type type: PKPaymentSummaryItemType)     class func summaryItemWithLabel(_ label: String, amount amount: NSDecimalNumber, type type: PKPaymentSummaryItemType) -> Self     var label: String     @NSCopying var amount: NSDecimalNumber     var type: PKPaymentSummaryItemType } ``` |

Modified [PKPaymentSummaryItem.amount](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/1619291-amount)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var amount: NSDecimalNumber! ``` |
| To | ``` @NSCopying var amount: NSDecimalNumber ``` |

Modified [PKPaymentSummaryItem.init(label: String, amount: NSDecimalNumber)](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/1619275-summaryitemwithlabel)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(label label: String!, amount amount: NSDecimalNumber!) ``` |
| To | ``` convenience init(label label: String, amount amount: NSDecimalNumber) ``` |

Modified [PKPaymentSummaryItem.label](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/1619260-label)

|  | Declaration |
| --- | --- |
| From | ``` var label: String! ``` |
| To | ``` var label: String ``` |

Modified [PKPaymentToken](https://developer.apple.com/documentation/passkit/pkpaymenttoken)

|  | Declaration |
| --- | --- |
| From | ``` class PKPaymentToken : NSObject {     var paymentInstrumentName: String! { get }     var paymentNetwork: String! { get }     var transactionIdentifier: String! { get }     var paymentData: NSData! { get } } ``` |
| To | ``` class PKPaymentToken : NSObject {     var paymentMethod: PKPaymentMethod { get }     var paymentInstrumentName: String { get }     var paymentNetwork: String { get }     var transactionIdentifier: String { get }     var paymentData: NSData { get } } ``` |

Modified [PKPaymentToken.paymentData](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1617000-paymentdata)

|  | Declaration |
| --- | --- |
| From | ``` var paymentData: NSData! { get } ``` |
| To | ``` var paymentData: NSData { get } ``` |

Modified [PKPaymentToken.paymentInstrumentName](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1616998-paymentinstrumentname)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var paymentInstrumentName: String! { get } ``` | -- |
| To | ``` var paymentInstrumentName: String { get } ``` | iOS 9.0 |

Modified [PKPaymentToken.paymentNetwork](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1617001-paymentnetwork)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var paymentNetwork: String! { get } ``` | -- |
| To | ``` var paymentNetwork: String { get } ``` | iOS 9.0 |

Modified [PKPaymentToken.transactionIdentifier](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1617003-transactionidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var transactionIdentifier: String! { get } ``` |
| To | ``` var transactionIdentifier: String { get } ``` |

Modified [PKShippingMethod](https://developer.apple.com/documentation/passkit/pkshippingmethod)

|  | Declaration |
| --- | --- |
| From | ``` class PKShippingMethod : PKPaymentSummaryItem {     var identifier: String!     var detail: String! } ``` |
| To | ``` class PKShippingMethod : PKPaymentSummaryItem {     var identifier: String?     var detail: String? } ``` |

Modified [PKShippingMethod.detail](https://developer.apple.com/documentation/passkit/pkshippingmethod/1619306-detail)

|  | Declaration |
| --- | --- |
| From | ``` var detail: String! ``` |
| To | ``` var detail: String? ``` |

Modified [PKShippingMethod.identifier](https://developer.apple.com/documentation/passkit/pkshippingmethod/1619232-identifier)

|  | Declaration |
| --- | --- |
| From | ``` var identifier: String! ``` |
| To | ``` var identifier: String? ``` |

Modified [PKShippingType [enum]](https://developer.apple.com/documentation/passkit/pkshippingtype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

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
