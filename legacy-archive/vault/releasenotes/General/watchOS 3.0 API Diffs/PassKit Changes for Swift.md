---
title: watchOS 3.0 API Diffs
apple_id: TP40017328
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS30APIDiffs/Swift/PassKit.html
archived_at: '2026-07-18T02:58:31.964016Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 3.0 API Diffs](watchOS%202.2%20to%20watchOS%203.0%20API%20Differences.md)


# PassKit Changes for Swift

### PassKit

Added [PKAddressField [struct]](https://developer.apple.com/documentation/passkit/pkaddressfield)Added [PKAddressField.all](https://developer.apple.com/documentation/passkit/pkaddressfield/pkaddressfieldall)Added [PKAddressField.email](https://developer.apple.com/documentation/passkit/pkaddressfield/pkaddressfieldemail)Added [PKAddressField.init(rawValue: UInt)](https://developer.apple.com/documentation/passkit/pkaddressfield/1619324-init)Added [PKAddressField.name](https://developer.apple.com/documentation/passkit/pkaddressfield/pkaddressfieldname)Added [PKAddressField.phone](https://developer.apple.com/documentation/passkit/pkaddressfield/pkaddressfieldphone)Added [PKAddressField.postalAddress](https://developer.apple.com/documentation/passkit/pkaddressfield/pkaddressfieldpostaladdress)Added [PKEncryptionScheme [struct]](https://developer.apple.com/documentation/passkit/pkencryptionscheme)Added [PKEncryptionScheme.init(rawValue: String)](https://developer.apple.com/documentation/passkit/pkencryptionscheme/2092172-init)Added [PKEncryptionScheme.RSA_V2](https://developer.apple.com/documentation/passkit/pkencryptionschemersa_v2)Added [PKMerchantCapability [struct]](https://developer.apple.com/documentation/passkit/pkmerchantcapability)Added [PKMerchantCapability.capability3DS](https://developer.apple.com/documentation/passkit/pkmerchantcapability/pkmerchantcapability3ds)Added [PKMerchantCapability.capabilityCredit](https://developer.apple.com/documentation/passkit/pkmerchantcapability/pkmerchantcapabilitycredit)Added [PKMerchantCapability.capabilityDebit](https://developer.apple.com/documentation/passkit/pkmerchantcapability/pkmerchantcapabilitydebit)Added [PKMerchantCapability.capabilityEMV](https://developer.apple.com/documentation/passkit/pkmerchantcapability/1619224-capabilityemv)Added [PKMerchantCapability.init(rawValue: UInt)](https://developer.apple.com/documentation/passkit/pkmerchantcapability/1619316-init)Added [PKPassKitError [struct]](https://developer.apple.com/documentation/passkit/pkpasskiterror)Added PKPassKitError.init(_nsError: NSError)Added [PKPassKitError.invalidDataError](https://developer.apple.com/documentation/passkit/pkpasskiterror/2320681-invaliddataerror)Added [PKPassKitError.invalidSignature](https://developer.apple.com/documentation/passkit/pkpasskiterror/2320680-invalidsignature)Added [PKPassKitError.notEntitledError](https://developer.apple.com/documentation/passkit/pkpasskiterror/2320679-notentitlederror)Added [PKPassKitError.unknownError](https://developer.apple.com/documentation/passkit/pkpasskiterror/2320682-unknownerror)Added [PKPassKitError.unsupportedVersionError](https://developer.apple.com/documentation/passkit/pkpasskiterror/2320678-unsupportedversionerror)Added [PKPassLibraryNotificationKey [struct]](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationkey)Added [PKPassLibraryNotificationKey.init(rawValue: String)](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationkey/2092173-init)Added [PKPassLibraryNotificationName [struct]](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationname)Added [PKPassLibraryNotificationName.init(_: String)](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationname/2092171-init)Added [PKPassLibraryNotificationName.init(rawValue: String)](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationname/2092170-init)Added [PKPayment](https://developer.apple.com/documentation/passkit/pkpayment)Added [PKPayment.billingContact](https://developer.apple.com/documentation/passkit/pkpayment/1619320-billingcontact)Added [PKPayment.shippingContact](https://developer.apple.com/documentation/passkit/pkpayment/1619250-shippingcontact)Added [PKPayment.shippingMethod](https://developer.apple.com/documentation/passkit/pkpayment/1619268-shippingmethod)Added [PKPayment.token](https://developer.apple.com/documentation/passkit/pkpayment/1619239-token)Added [PKPaymentAuthorizationController](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller)Added [PKPaymentAuthorizationController.canMakePayments() -> Bool [class]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1649461-canmakepayments)Added [PKPaymentAuthorizationController.canMakePayments(usingNetworks: [PKPaymentNetwork]) -> Bool [class]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1649457-canmakepaymentsusingnetworks)Added [PKPaymentAuthorizationController.canMakePayments(usingNetworks: [PKPaymentNetwork], capabilities: PKMerchantCapability) -> Bool [class]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1649455-canmakepaymentsusingnetworks)Added [PKPaymentAuthorizationController.delegate](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1649453-delegate)Added [PKPaymentAuthorizationController.dismiss(completion: ( () -> Swift.Void)?)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1771696-dismiss)Added [PKPaymentAuthorizationController.init(paymentRequest: PKPaymentRequest)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1649462-init)Added [PKPaymentAuthorizationController.present(completion: ( (Bool) -> Swift.Void)?)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1649463-presentwithcompletion)Added [PKPaymentAuthorizationControllerDelegate](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate)Added [PKPaymentAuthorizationControllerDelegate.paymentAuthorizationController(_: PKPaymentAuthorizationController, didAuthorizePayment: PKPayment, completion: (PKPaymentAuthorizationStatus) -> Swift.Void)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/1649454-paymentauthorizationcontroller)Added [PKPaymentAuthorizationControllerDelegate.paymentAuthorizationController(_: PKPaymentAuthorizationController, didSelectPaymentMethod: PKPaymentMethod, completion: ([PKPaymentSummaryItem]) -> Swift.Void)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/1649460-paymentauthorizationcontroller)Added [PKPaymentAuthorizationControllerDelegate.paymentAuthorizationController(_: PKPaymentAuthorizationController, didSelectShippingContact: PKContact, completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Swift.Void)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/1649458-paymentauthorizationcontroller)Added [PKPaymentAuthorizationControllerDelegate.paymentAuthorizationController(_: PKPaymentAuthorizationController, didSelectShippingMethod: PKShippingMethod, completion: (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem]) -> Swift.Void)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/1649465-paymentauthorizationcontroller)Added [PKPaymentAuthorizationControllerDelegate.paymentAuthorizationControllerDidFinish(_: PKPaymentAuthorizationController)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/1649456-paymentauthorizationcontrollerdi)Added [PKPaymentAuthorizationControllerDelegate.paymentAuthorizationControllerWillAuthorizePayment(_: PKPaymentAuthorizationController)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/1649464-paymentauthorizationcontrollerwi)Added [PKPaymentAuthorizationStatus [enum]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus)Added [PKPaymentAuthorizationStatus.failure](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/failure)Added [PKPaymentAuthorizationStatus.invalidBillingPostalAddress](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatusinvalidbillingpostaladdress)Added [PKPaymentAuthorizationStatus.invalidShippingContact](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/invalidshippingcontact)Added [PKPaymentAuthorizationStatus.invalidShippingPostalAddress](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatusinvalidshippingpostaladdress)Added [PKPaymentAuthorizationStatus.pinIncorrect](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatuspinincorrect)Added [PKPaymentAuthorizationStatus.pinLockout](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatuspinlockout)Added [PKPaymentAuthorizationStatus.pinRequired](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatuspinrequired)Added [PKPaymentAuthorizationStatus.success](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/success)Added [PKPaymentMethod](https://developer.apple.com/documentation/passkit/pkpaymentmethod)Added [PKPaymentMethod.displayName](https://developer.apple.com/documentation/passkit/pkpaymentmethod/1619249-displayname)Added [PKPaymentMethod.network](https://developer.apple.com/documentation/passkit/pkpaymentmethod/1619209-network)Added [PKPaymentMethod.paymentPass](https://developer.apple.com/documentation/passkit/pkpaymentmethod/1619269-paymentpass)Added [PKPaymentMethod.type](https://developer.apple.com/documentation/passkit/pkpaymentmethod/1619279-type)Added [PKPaymentMethodType [enum]](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype)Added [PKPaymentMethodType.credit](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/credit)Added [PKPaymentMethodType.debit](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/debit)Added [PKPaymentMethodType.prepaid](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/prepaid)Added [PKPaymentMethodType.store](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/pkpaymentmethodtypestore)Added [PKPaymentMethodType.unknown](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/pkpaymentmethodtypeunknown)Added [PKPaymentNetwork [struct]](https://developer.apple.com/documentation/passkit/pkpaymentnetwork)Added [PKPaymentNetwork.init(_: String)](https://developer.apple.com/documentation/passkit/pkpaymentnetwork/2092169-init)Added [PKPaymentNetwork.init(rawValue: String)](https://developer.apple.com/documentation/passkit/pkpaymentnetwork/2092174-init)Added [PKPaymentRequest](https://developer.apple.com/documentation/passkit/pkpaymentrequest)Added [PKPaymentRequest.applicationData](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619298-applicationdata)Added [PKPaymentRequest.availableNetworks() -> [PKPaymentNetwork] [class]](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1833288-availablenetworks)Added [PKPaymentRequest.billingContact](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619221-billingcontact)Added [PKPaymentRequest.countryCode](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619246-countrycode)Added [PKPaymentRequest.currencyCode](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619248-currencycode)Added [PKPaymentRequest.merchantCapabilities](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619257-merchantcapabilities)Added [PKPaymentRequest.merchantIdentifier](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619305-merchantidentifier)Added [PKPaymentRequest.paymentSummaryItems](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619231-paymentsummaryitems)Added [PKPaymentRequest.requiredBillingAddressFields](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619265-requiredbillingaddressfields)Added [PKPaymentRequest.requiredShippingAddressFields](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619228-requiredshippingaddressfields)Added [PKPaymentRequest.shippingContact](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619245-shippingcontact)Added [PKPaymentRequest.shippingMethods](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619226-shippingmethods)Added [PKPaymentRequest.shippingType](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619330-shippingtype)Added [PKPaymentRequest.supportedNetworks](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619329-supportednetworks)Added [PKPaymentSummaryItem](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem)Added [PKPaymentSummaryItem.amount](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/1619291-amount)Added [PKPaymentSummaryItem.init(label: String, amount: NSDecimalNumber)](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/1619275-summaryitemwithlabel)Added [PKPaymentSummaryItem.init(label: String, amount: NSDecimalNumber, type: PKPaymentSummaryItemType)](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/1619262-summaryitemwithlabel)Added [PKPaymentSummaryItem.label](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/1619260-label)Added [PKPaymentSummaryItem.type](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/1619327-type)Added [PKPaymentSummaryItemType [enum]](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitemtype)Added [PKPaymentSummaryItemType.final](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitemtype/pkpaymentsummaryitemtypefinal)Added [PKPaymentSummaryItemType.pending](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitemtype/pkpaymentsummaryitemtypepending)Added [PKPaymentToken](https://developer.apple.com/documentation/passkit/pkpaymenttoken)Added [PKPaymentToken.paymentData](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1617000-paymentdata)Added [PKPaymentToken.paymentMethod](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1617002-paymentmethod)Added [PKPaymentToken.transactionIdentifier](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1617003-transactionidentifier)Added [PKShippingMethod](https://developer.apple.com/documentation/passkit/pkshippingmethod)Added [PKShippingMethod.detail](https://developer.apple.com/documentation/passkit/pkshippingmethod/1619306-detail)Added [PKShippingMethod.identifier](https://developer.apple.com/documentation/passkit/pkshippingmethod/1619232-identifier)Added [PKShippingType [enum]](https://developer.apple.com/documentation/passkit/pkshippingtype)Added [PKShippingType.delivery](https://developer.apple.com/documentation/passkit/pkshippingtype/pkshippingtypedelivery)Added [PKShippingType.servicePickup](https://developer.apple.com/documentation/passkit/pkshippingtype/servicepickup)Added [PKShippingType.shipping](https://developer.apple.com/documentation/passkit/pkshippingtype/shipping)Added [PKShippingType.storePickup](https://developer.apple.com/documentation/passkit/pkshippingtype/storepickup)Modified [PKContact](https://developer.apple.com/documentation/passkit/pkcontact)

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` class PKContact : NSObject {     var name: NSPersonNameComponents?     var postalAddress: CNPostalAddress?     var emailAddress: String?     var phoneNumber: CNPhoneNumber?     var supplementarySubLocality: String? } ``` | -- | watchOS 2.0 |
| To | ``` class PKContact : NSObject {     var name: PersonNameComponents?     var postalAddress: CNPostalAddress?     var emailAddress: String?     var phoneNumber: CNPhoneNumber?     var supplementarySubLocality: String?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension PKContact : CVarArg { } extension PKContact : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable | watchOS 3.0 |

Modified [PKContact.name](https://developer.apple.com/documentation/passkit/pkcontact/1619318-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: NSPersonNameComponents? ``` |
| To | ``` var name: PersonNameComponents? ``` |

Modified [PKEncryptionScheme.ECC_V2](https://developer.apple.com/documentation/passkit/pkencryptionscheme/1618637-ecc_v2)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKEncryptionSchemeECC_V2 | ``` let PKEncryptionSchemeECC_V2: String ``` |
| To | ECC_V2 | ``` static let ECC_V2: PKEncryptionScheme ``` |

Modified [PKObject](https://developer.apple.com/documentation/passkit/pkobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PKObject : NSObject { } ``` | -- |
| To | ``` class PKObject : NSObject {     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension PKObject : CVarArg { } extension PKObject : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PKPass](https://developer.apple.com/documentation/passkit/pkpass)

|  | Declaration |
| --- | --- |
| From | ``` class PKPass : PKObject {     init(data data: NSData, error error: NSErrorPointer)     var passType: PKPassType { get }     unowned(unsafe) var paymentPass: PKPaymentPass? { get }     var serialNumber: String { get }     var passTypeIdentifier: String { get }     @NSCopying var webServiceURL: NSURL? { get }     var authenticationToken: String? { get }     @NSCopying var icon: UIImage { get }     var localizedName: String { get }     var localizedDescription: String { get }     var organizationName: String { get }     @NSCopying var relevantDate: NSDate? { get }     var userInfo: [NSObject : AnyObject]? { get }     @NSCopying var passURL: NSURL { get }     var remotePass: Bool { get }     var deviceName: String { get }     func localizedValueForFieldKey(_ key: String) -> AnyObject? } ``` |
| To | ``` class PKPass : PKObject {     init(data data: Data, error error: NSErrorPointer)     var passType: PKPassType { get }     var paymentPass: PKPaymentPass? { get }     var serialNumber: String { get }     var passTypeIdentifier: String { get }     var webServiceURL: URL? { get }     var authenticationToken: String? { get }     @NSCopying var icon: UIImage { get }     var localizedName: String { get }     var localizedDescription: String { get }     var organizationName: String { get }     var relevantDate: Date? { get }     var userInfo: [AnyHashable : Any]? { get }     var passURL: URL? { get }     var isRemotePass: Bool { get }     var deviceName: String { get }     func localizedValue(forFieldKey key: String) -> Any? } ``` |

Modified [PKPass.init(data: Data, error: NSErrorPointer)](https://developer.apple.com/documentation/passkit/pkpass/1618792-init)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: NSData, error error: NSErrorPointer) ``` |
| To | ``` init(data data: Data, error error: NSErrorPointer) ``` |

Modified [PKPass.isRemotePass](https://developer.apple.com/documentation/passkit/pkpass/1618786-remotepass)

|  | Declaration |
| --- | --- |
| From | ``` var remotePass: Bool { get } ``` |
| To | ``` var isRemotePass: Bool { get } ``` |

Modified [PKPass.localizedValue(forFieldKey: String) -> Any?](https://developer.apple.com/documentation/passkit/pkpass/1618798-localizedvalueforfieldkey)

|  | Declaration |
| --- | --- |
| From | ``` func localizedValueForFieldKey(_ key: String) -> AnyObject? ``` |
| To | ``` func localizedValue(forFieldKey key: String) -> Any? ``` |

Modified [PKPass.passURL](https://developer.apple.com/documentation/passkit/pkpass/1618781-passurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var passURL: NSURL { get } ``` |
| To | ``` var passURL: URL? { get } ``` |

Modified [PKPass.paymentPass](https://developer.apple.com/documentation/passkit/pkpass/1618784-paymentpass)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var paymentPass: PKPaymentPass? { get } ``` |
| To | ``` var paymentPass: PKPaymentPass? { get } ``` |

Modified [PKPass.relevantDate](https://developer.apple.com/documentation/passkit/pkpass/1618776-relevantdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var relevantDate: NSDate? { get } ``` |
| To | ``` var relevantDate: Date? { get } ``` |

Modified [PKPass.userInfo](https://developer.apple.com/documentation/passkit/pkpass/1618794-userinfo)

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]? { get } ``` |
| To | ``` var userInfo: [AnyHashable : Any]? { get } ``` |

Modified [PKPass.webServiceURL](https://developer.apple.com/documentation/passkit/pkpass/1618772-webserviceurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var webServiceURL: NSURL? { get } ``` |
| To | ``` var webServiceURL: URL? { get } ``` |

Modified [PKPassKitError.Code [enum]](https://developer.apple.com/documentation/passkit/pkpasskiterrorcode)

|  | Declaration |
| --- | --- |
| From | ``` enum PKPassKitErrorCode : Int {     case UnknownError     case InvalidDataError     case UnsupportedVersionError     case InvalidSignature     case NotEntitledError } extension PKPassKitErrorCode : _BridgedNSError { } extension PKPassKitErrorCode : _BridgedNSError { } ``` |
| To | ``` enum Code : Int {         typealias _ErrorType = PKPassKitError         case unknownError         case invalidDataError         case unsupportedVersionError         case invalidSignature         case notEntitledError     } ``` |

Modified [PKPassKitError.Code.invalidDataError](https://developer.apple.com/documentation/passkit/pkpasskiterror/code/invaliddataerror)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidDataError ``` |
| To | ``` case invalidDataError ``` |

Modified [PKPassKitError.Code.invalidSignature](https://developer.apple.com/documentation/passkit/pkpasskiterror/code/invalidsignature)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidSignature ``` |
| To | ``` case invalidSignature ``` |

Modified [PKPassKitError.Code.notEntitledError](https://developer.apple.com/documentation/passkit/pkpasskiterror/code/notentitlederror)

|  | Declaration |
| --- | --- |
| From | ``` case NotEntitledError ``` |
| To | ``` case notEntitledError ``` |

Modified [PKPassKitError.Code.unknownError](https://developer.apple.com/documentation/passkit/pkpasskiterrorcode/pkunknownerror)

|  | Declaration |
| --- | --- |
| From | ``` case UnknownError ``` |
| To | ``` case unknownError ``` |

Modified [PKPassKitError.Code.unsupportedVersionError](https://developer.apple.com/documentation/passkit/pkpasskiterrorcode/pkunsupportedversionerror)

|  | Declaration |
| --- | --- |
| From | ``` case UnsupportedVersionError ``` |
| To | ``` case unsupportedVersionError ``` |

Modified [PKPassLibrary](https://developer.apple.com/documentation/passkit/pkpasslibrary)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PKPassLibrary : NSObject {     class func isPassLibraryAvailable() -> Bool     class func requestAutomaticPassPresentationSuppressionWithResponseHandler(_ responseHandler: (PKAutomaticPassPresentationSuppressionResult) -> Void) -> PKSuppressionRequestToken     class func endAutomaticPassPresentationSuppressionWithRequestToken(_ requestToken: PKSuppressionRequestToken)     class func isSuppressingAutomaticPassPresentation() -> Bool     class func isPaymentPassActivationAvailable() -> Bool     func isPaymentPassActivationAvailable() -> Bool     func passes() -> [PKPass]     func passWithPassTypeIdentifier(_ identifier: String, serialNumber serialNumber: String) -> PKPass?     func passesOfType(_ passType: PKPassType) -> [PKPass]     func remotePaymentPasses() -> [PKPaymentPass]     func removePass(_ pass: PKPass)     func containsPass(_ pass: PKPass) -> Bool     func replacePassWithPass(_ pass: PKPass) -> Bool     func addPasses(_ passes: [PKPass], withCompletionHandler completion: ((PKPassLibraryAddPassesStatus) -> Void)?)     func openPaymentSetup()     func canAddPaymentPassWithPrimaryAccountIdentifier(_ primaryAccountIdentifier: String) -> Bool     func activatePaymentPass(_ paymentPass: PKPaymentPass, withActivationData activationData: NSData, completion completion: ((Bool, NSError) -> Void)?)     func activatePaymentPass(_ paymentPass: PKPaymentPass, withActivationCode activationCode: String, completion completion: ((Bool, NSError) -> Void)?) } ``` | -- |
| To | ``` class PKPassLibrary : NSObject {     class func isPassLibraryAvailable() -> Bool     class func requestAutomaticPassPresentationSuppression(responseHandler responseHandler: @escaping (PKAutomaticPassPresentationSuppressionResult) -> Swift.Void) -> PKSuppressionRequestToken     class func endAutomaticPassPresentationSuppression(withRequestToken requestToken: PKSuppressionRequestToken)     class func isSuppressingAutomaticPassPresentation() -> Bool     class func isPaymentPassActivationAvailable() -> Bool     func isPaymentPassActivationAvailable() -> Bool     func passes() -> [PKPass]     func pass(withPassTypeIdentifier identifier: String, serialNumber serialNumber: String) -> PKPass?     func passes(of passType: PKPassType) -> [PKPass]     func remotePaymentPasses() -> [PKPaymentPass]     func removePass(_ pass: PKPass)     func containsPass(_ pass: PKPass) -> Bool     func replacePass(with pass: PKPass) -> Bool     func addPasses(_ passes: [PKPass], withCompletionHandler completion: (@escaping (PKPassLibraryAddPassesStatus) -> Swift.Void)? = nil)     func openPaymentSetup()     func present(_ pass: PKPaymentPass)     func canAddPaymentPass(withPrimaryAccountIdentifier primaryAccountIdentifier: String) -> Bool     func activate(_ paymentPass: PKPaymentPass, withActivationData activationData: Data, completion completion: (@escaping (Bool, Error) -> Swift.Void)? = nil)     func activate(_ paymentPass: PKPaymentPass, withActivationCode activationCode: String, completion completion: (@escaping (Bool, Error) -> Swift.Void)? = nil)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension PKPassLibrary : CVarArg { } extension PKPassLibrary : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PKPassLibrary.addPasses(_: [PKPass], withCompletionHandler: ( (PKPassLibraryAddPassesStatus) -> Swift.Void)?)](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617093-addpasses)

|  | Declaration |
| --- | --- |
| From | ``` func addPasses(_ passes: [PKPass], withCompletionHandler completion: ((PKPassLibraryAddPassesStatus) -> Void)?) ``` |
| To | ``` func addPasses(_ passes: [PKPass], withCompletionHandler completion: (@escaping (PKPassLibraryAddPassesStatus) -> Swift.Void)? = nil) ``` |

Modified [PKPassLibrary.canAddPaymentPass(withPrimaryAccountIdentifier: String) -> Bool](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617081-canaddpaymentpasswithprimaryacco)

|  | Declaration |
| --- | --- |
| From | ``` func canAddPaymentPassWithPrimaryAccountIdentifier(_ primaryAccountIdentifier: String) -> Bool ``` |
| To | ``` func canAddPaymentPass(withPrimaryAccountIdentifier primaryAccountIdentifier: String) -> Bool ``` |

Modified [PKPassLibrary.pass(withPassTypeIdentifier: String, serialNumber: String) -> PKPass?](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617104-passwithpasstypeidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func passWithPassTypeIdentifier(_ identifier: String, serialNumber serialNumber: String) -> PKPass? ``` |
| To | ``` func pass(withPassTypeIdentifier identifier: String, serialNumber serialNumber: String) -> PKPass? ``` |

Modified [PKPassLibrary.passes(of: PKPassType) -> [PKPass]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617074-passes)

|  | Declaration |
| --- | --- |
| From | ``` func passesOfType(_ passType: PKPassType) -> [PKPass] ``` |
| To | ``` func passes(of passType: PKPassType) -> [PKPass] ``` |

Modified [PKPassLibrary.replacePass(with: PKPass) -> Bool](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617082-replacepasswithpass)

|  | Declaration |
| --- | --- |
| From | ``` func replacePassWithPass(_ pass: PKPass) -> Bool ``` |
| To | ``` func replacePass(with pass: PKPass) -> Bool ``` |

Modified [PKPassLibraryAddPassesStatus [enum]](https://developer.apple.com/documentation/passkit/pkpasslibraryaddpassesstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum PKPassLibraryAddPassesStatus : Int {     case DidAddPasses     case ShouldReviewPasses     case DidCancelAddPasses } ``` |
| To | ``` enum PKPassLibraryAddPassesStatus : Int {     case didAddPasses     case shouldReviewPasses     case didCancelAddPasses } ``` |

Modified [PKPassLibraryAddPassesStatus.didAddPasses](https://developer.apple.com/documentation/passkit/pkpasslibraryaddpassesstatus/pkpasslibrarydidaddpasses)

|  | Declaration |
| --- | --- |
| From | ``` case DidAddPasses ``` |
| To | ``` case didAddPasses ``` |

Modified [PKPassLibraryAddPassesStatus.didCancelAddPasses](https://developer.apple.com/documentation/passkit/pkpasslibraryaddpassesstatus/pkpasslibrarydidcanceladdpasses)

|  | Declaration |
| --- | --- |
| From | ``` case DidCancelAddPasses ``` |
| To | ``` case didCancelAddPasses ``` |

Modified [PKPassLibraryAddPassesStatus.shouldReviewPasses](https://developer.apple.com/documentation/passkit/pkpasslibraryaddpassesstatus/shouldreviewpasses)

|  | Declaration |
| --- | --- |
| From | ``` case ShouldReviewPasses ``` |
| To | ``` case shouldReviewPasses ``` |

Modified [PKPassLibraryNotificationKey.addedPassesUserInfoKey](https://developer.apple.com/documentation/passkit/pkpasslibraryaddedpassesuserinfokey)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKPassLibraryAddedPassesUserInfoKey | ``` let PKPassLibraryAddedPassesUserInfoKey: String ``` |
| To | addedPassesUserInfoKey | ``` static let addedPassesUserInfoKey: PKPassLibraryNotificationKey ``` |

Modified [PKPassLibraryNotificationKey.passTypeIdentifierUserInfoKey](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationkey/1617094-passtypeidentifieruserinfokey)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKPassLibraryPassTypeIdentifierUserInfoKey | ``` let PKPassLibraryPassTypeIdentifierUserInfoKey: String ``` |
| To | passTypeIdentifierUserInfoKey | ``` static let passTypeIdentifierUserInfoKey: PKPassLibraryNotificationKey ``` |

Modified [PKPassLibraryNotificationKey.removedPassInfosUserInfoKey](https://developer.apple.com/documentation/passkit/pkpasslibraryremovedpassinfosuserinfokey)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKPassLibraryRemovedPassInfosUserInfoKey | ``` let PKPassLibraryRemovedPassInfosUserInfoKey: String ``` |
| To | removedPassInfosUserInfoKey | ``` static let removedPassInfosUserInfoKey: PKPassLibraryNotificationKey ``` |

Modified [PKPassLibraryNotificationKey.replacementPassesUserInfoKey](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationkey/1617077-replacementpassesuserinfokey)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKPassLibraryReplacementPassesUserInfoKey | ``` let PKPassLibraryReplacementPassesUserInfoKey: String ``` |
| To | replacementPassesUserInfoKey | ``` static let replacementPassesUserInfoKey: PKPassLibraryNotificationKey ``` |

Modified [PKPassLibraryNotificationKey.serialNumberUserInfoKey](https://developer.apple.com/documentation/passkit/pkpasslibraryserialnumberuserinfokey)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKPassLibrarySerialNumberUserInfoKey | ``` let PKPassLibrarySerialNumberUserInfoKey: String ``` |
| To | serialNumberUserInfoKey | ``` static let serialNumberUserInfoKey: PKPassLibraryNotificationKey ``` |

Modified [PKPassLibraryNotificationName.PKPassLibraryDidChange](https://developer.apple.com/documentation/passkit/pkpasslibrarydidchangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKPassLibraryDidChangeNotification | ``` let PKPassLibraryDidChangeNotification: String ``` |
| To | PKPassLibraryDidChange | ``` static let PKPassLibraryDidChange: PKPassLibraryNotificationName ``` |

Modified [PKPassLibraryNotificationName.PKPassLibraryRemotePaymentPassesDidChange](https://developer.apple.com/documentation/passkit/pkpasslibraryremotepaymentpassesdidchangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKPassLibraryRemotePaymentPassesDidChangeNotification | ``` let PKPassLibraryRemotePaymentPassesDidChangeNotification: String ``` |
| To | PKPassLibraryRemotePaymentPassesDidChange | ``` static let PKPassLibraryRemotePaymentPassesDidChange: PKPassLibraryNotificationName ``` |

Modified [PKPassType [enum]](https://developer.apple.com/documentation/passkit/pkpasstype)

|  | Declaration |
| --- | --- |
| From | ``` enum PKPassType : UInt {     case Barcode     case Payment     case Any } ``` |
| To | ``` enum PKPassType : UInt {     case barcode     case payment     case any } ``` |

Modified [PKPassType.any](https://developer.apple.com/documentation/passkit/pkpasstype/pkpasstypeany)

|  | Declaration |
| --- | --- |
| From | ``` case Any ``` |
| To | ``` case any ``` |

Modified [PKPassType.barcode](https://developer.apple.com/documentation/passkit/pkpasstype/barcode)

|  | Declaration |
| --- | --- |
| From | ``` case Barcode ``` |
| To | ``` case barcode ``` |

Modified [PKPassType.payment](https://developer.apple.com/documentation/passkit/pkpasstype/pkpasstypepayment)

|  | Declaration |
| --- | --- |
| From | ``` case Payment ``` |
| To | ``` case payment ``` |

Modified [PKPaymentNetwork.amex](https://developer.apple.com/documentation/passkit/pkpaymentnetworkamex)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | PKPaymentNetworkAmex | ``` let PKPaymentNetworkAmex: String ``` | watchOS 2.0 |
| To | amex | ``` static let amex: PKPaymentNetwork ``` | watchOS 3.0 |

Modified [PKPaymentNetwork.chinaUnionPay](https://developer.apple.com/documentation/passkit/pkpaymentnetwork/1618644-chinaunionpay)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | PKPaymentNetworkChinaUnionPay | ``` let PKPaymentNetworkChinaUnionPay: String ``` | watchOS 2.2 |
| To | chinaUnionPay | ``` static let chinaUnionPay: PKPaymentNetwork ``` | watchOS 3.0 |

Modified [PKPaymentNetwork.discover](https://developer.apple.com/documentation/passkit/pkpaymentnetwork/1618641-discover)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | PKPaymentNetworkDiscover | ``` let PKPaymentNetworkDiscover: String ``` | watchOS 2.0 |
| To | discover | ``` static let discover: PKPaymentNetwork ``` | watchOS 3.0 |

Modified [PKPaymentNetwork.interac](https://developer.apple.com/documentation/passkit/pkpaymentnetworkinterac)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | PKPaymentNetworkInterac | ``` let PKPaymentNetworkInterac: String ``` | watchOS 2.2 |
| To | interac | ``` static let interac: PKPaymentNetwork ``` | watchOS 3.0 |

Modified [PKPaymentNetwork.masterCard](https://developer.apple.com/documentation/passkit/pkpaymentnetwork/1618643-mastercard)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | PKPaymentNetworkMasterCard | ``` let PKPaymentNetworkMasterCard: String ``` | watchOS 2.0 |
| To | masterCard | ``` static let masterCard: PKPaymentNetwork ``` | watchOS 3.0 |

Modified [PKPaymentNetwork.privateLabel](https://developer.apple.com/documentation/passkit/pkpaymentnetworkprivatelabel)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | PKPaymentNetworkPrivateLabel | ``` let PKPaymentNetworkPrivateLabel: String ``` | watchOS 2.0 |
| To | privateLabel | ``` static let privateLabel: PKPaymentNetwork ``` | watchOS 3.0 |

Modified [PKPaymentNetwork.visa](https://developer.apple.com/documentation/passkit/pkpaymentnetworkvisa)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | PKPaymentNetworkVisa | ``` let PKPaymentNetworkVisa: String ``` | watchOS 2.0 |
| To | visa | ``` static let visa: PKPaymentNetwork ``` | watchOS 3.0 |

Modified [PKPaymentPass](https://developer.apple.com/documentation/passkit/pkpaymentpass)

|  | Declaration |
| --- | --- |
| From | ``` class PKPaymentPass : PKPass {     var primaryAccountIdentifier: String { get }     var primaryAccountNumberSuffix: String { get }     var deviceAccountIdentifier: String { get }     var deviceAccountNumberSuffix: String { get }     var activationState: PKPaymentPassActivationState { get } } ``` |
| To | ``` class PKPaymentPass : PKPass {     var primaryAccountIdentifier: String { get }     var primaryAccountNumberSuffix: String { get }     weak var deviceAccountIdentifier: NSString? { get }     weak var deviceAccountNumberSuffix: NSString? { get }     var activationState: PKPaymentPassActivationState { get } } ``` |

Modified [PKPaymentPass.deviceAccountIdentifier](https://developer.apple.com/documentation/passkit/pkpaymentpass/1619074-deviceaccountidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var deviceAccountIdentifier: String { get } ``` |
| To | ``` weak var deviceAccountIdentifier: NSString? { get } ``` |

Modified [PKPaymentPass.deviceAccountNumberSuffix](https://developer.apple.com/documentation/passkit/pkpaymentpass/1619075-deviceaccountnumbersuffix)

|  | Declaration |
| --- | --- |
| From | ``` var deviceAccountNumberSuffix: String { get } ``` |
| To | ``` weak var deviceAccountNumberSuffix: NSString? { get } ``` |

Modified [PKPaymentPassActivationState [enum]](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate)

|  | Declaration |
| --- | --- |
| From | ``` enum PKPaymentPassActivationState : UInt {     case Activated     case RequiresActivation     case Activating     case Suspended     case Deactivated } ``` |
| To | ``` enum PKPaymentPassActivationState : UInt {     case activated     case requiresActivation     case activating     case suspended     case deactivated } ``` |

Modified [PKPaymentPassActivationState.activated](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate/pkpaymentpassactivationstateactivated)

|  | Declaration |
| --- | --- |
| From | ``` case Activated ``` |
| To | ``` case activated ``` |

Modified [PKPaymentPassActivationState.activating](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate/pkpaymentpassactivationstateactivating)

|  | Declaration |
| --- | --- |
| From | ``` case Activating ``` |
| To | ``` case activating ``` |

Modified [PKPaymentPassActivationState.deactivated](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate/deactivated)

|  | Declaration |
| --- | --- |
| From | ``` case Deactivated ``` |
| To | ``` case deactivated ``` |

Modified [PKPaymentPassActivationState.requiresActivation](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate/pkpaymentpassactivationstaterequiresactivation)

|  | Declaration |
| --- | --- |
| From | ``` case RequiresActivation ``` |
| To | ``` case requiresActivation ``` |

Modified [PKPaymentPassActivationState.suspended](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate/suspended)

|  | Declaration |
| --- | --- |
| From | ``` case Suspended ``` |
| To | ``` case suspended ``` |

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
