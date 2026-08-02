---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/Contacts.html
archived_at: '2026-07-18T02:57:06.329620Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# Contacts Changes for Swift

### Contacts

Modified [CNAuthorizationStatus [enum]](https://developer.apple.com/documentation/contacts/cnauthorizationstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CNContact](https://developer.apple.com/documentation/contacts/cncontact)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CNContact : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     var identifier: String { get }     var contactType: CNContactType { get }     var namePrefix: String { get }     var givenName: String { get }     var middleName: String { get }     var familyName: String { get }     var previousFamilyName: String { get }     var nameSuffix: String { get }     var nickname: String { get }     var phoneticGivenName: String { get }     var phoneticMiddleName: String { get }     var phoneticFamilyName: String { get }     var organizationName: String { get }     var departmentName: String { get }     var jobTitle: String { get }     var note: String { get }     @NSCopying var imageData: NSData? { get }     @NSCopying var thumbnailImageData: NSData? { get }     var imageDataAvailable: Bool { get }     var phoneNumbers: [CNLabeledValue] { get }     var emailAddresses: [CNLabeledValue] { get }     var postalAddresses: [CNLabeledValue] { get }     var urlAddresses: [CNLabeledValue] { get }     var contactRelations: [CNLabeledValue] { get }     var socialProfiles: [CNLabeledValue] { get }     var instantMessageAddresses: [CNLabeledValue] { get }     @NSCopying var birthday: NSDateComponents? { get }     @NSCopying var nonGregorianBirthday: NSDateComponents? { get }     var dates: [CNLabeledValue] { get }     func isKeyAvailable(_ key: String) -> Bool     func areKeysAvailable(_ keyDescriptors: [CNKeyDescriptor]) -> Bool     class func localizedStringForKey(_ key: String) -> String     class func comparatorForNameSortOrder(_ sortOrder: CNContactSortOrder) -> NSComparator     class func descriptorForAllComparatorKeys() -> CNKeyDescriptor     func isUnifiedWithContactWithIdentifier(_ contactIdentifier: String) -> Bool } extension CNContact {     class func predicateForContactsMatchingName(_ name: String) -> NSPredicate     class func predicateForContactsWithIdentifiers(_ identifiers: [String]) -> NSPredicate     class func predicateForContactsInGroupWithIdentifier(_ groupIdentifier: String) -> NSPredicate     class func predicateForContactsInContainerWithIdentifier(_ containerIdentifier: String) -> NSPredicate } ``` | AnyObject, NSCoding, NSCopying, NSMutableCopying, NSSecureCoding |
| To | ``` class CNContact : NSObject, NSCopying, NSMutableCopying, NSSecureCoding {     var identifier: String { get }     var contactType: CNContactType { get }     var namePrefix: String { get }     var givenName: String { get }     var middleName: String { get }     var familyName: String { get }     var previousFamilyName: String { get }     var nameSuffix: String { get }     var nickname: String { get }     var phoneticGivenName: String { get }     var phoneticMiddleName: String { get }     var phoneticFamilyName: String { get }     var organizationName: String { get }     var departmentName: String { get }     var jobTitle: String { get }     var note: String { get }     @NSCopying var imageData: NSData? { get }     @NSCopying var thumbnailImageData: NSData? { get }     var imageDataAvailable: Bool { get }     var phoneNumbers: [CNLabeledValue] { get }     var emailAddresses: [CNLabeledValue] { get }     var postalAddresses: [CNLabeledValue] { get }     var urlAddresses: [CNLabeledValue] { get }     var contactRelations: [CNLabeledValue] { get }     var socialProfiles: [CNLabeledValue] { get }     var instantMessageAddresses: [CNLabeledValue] { get }     @NSCopying var birthday: NSDateComponents? { get }     @NSCopying var nonGregorianBirthday: NSDateComponents? { get }     var dates: [CNLabeledValue] { get }     func isKeyAvailable(_ key: String) -> Bool     func areKeysAvailable(_ keyDescriptors: [CNKeyDescriptor]) -> Bool     class func localizedStringForKey(_ key: String) -> String     class func comparatorForNameSortOrder(_ sortOrder: CNContactSortOrder) -> NSComparator     class func descriptorForAllComparatorKeys() -> CNKeyDescriptor     func isUnifiedWithContactWithIdentifier(_ contactIdentifier: String) -> Bool } extension CNContact {     class func predicateForContactsMatchingName(_ name: String) -> NSPredicate     class func predicateForContactsWithIdentifiers(_ identifiers: [String]) -> NSPredicate     class func predicateForContactsInGroupWithIdentifier(_ groupIdentifier: String) -> NSPredicate     class func predicateForContactsInContainerWithIdentifier(_ containerIdentifier: String) -> NSPredicate } ``` | NSCopying, NSMutableCopying, NSSecureCoding |

Modified [CNContactDisplayNameOrder [enum]](https://developer.apple.com/documentation/contacts/cncontactdisplaynameorder)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CNContactFetchRequest](https://developer.apple.com/documentation/contacts/cncontactfetchrequest)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CNContactFormatter](https://developer.apple.com/documentation/contacts/cncontactformatter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CNContactFormatterStyle [enum]](https://developer.apple.com/documentation/contacts/cncontactformatterstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CNContactProperty](https://developer.apple.com/documentation/contacts/cncontactproperty)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CNContactProperty : NSObject, NSCopying, NSSecureCoding, NSCoding {     @NSCopying var contact: CNContact { get }     var key: String { get }     var value: AnyObject? { get }     var identifier: String? { get }     var label: String? { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CNContactProperty : NSObject, NSCopying, NSSecureCoding {     @NSCopying var contact: CNContact { get }     var key: String { get }     var value: AnyObject? { get }     var identifier: String? { get }     var label: String? { get } } ``` | NSCopying, NSSecureCoding |

Modified [CNContactRelation](https://developer.apple.com/documentation/contacts/cncontactrelation)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CNContactRelation : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init(name name: String)     class func contactRelationWithName(_ name: String) -> Self     init(name name: String)     var name: String { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CNContactRelation : NSObject, NSCopying, NSSecureCoding {     convenience init(name name: String)     class func contactRelationWithName(_ name: String) -> Self     init(name name: String)     var name: String { get } } ``` | NSCopying, NSSecureCoding |

Modified [CNContactSortOrder [enum]](https://developer.apple.com/documentation/contacts/cncontactsortorder)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CNContactStore](https://developer.apple.com/documentation/contacts/cncontactstore)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CNContactsUserDefaults](https://developer.apple.com/documentation/contacts/cncontactsuserdefaults)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CNContactType [enum]](https://developer.apple.com/documentation/contacts/cncontacttype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CNContactVCardSerialization](https://developer.apple.com/documentation/contacts/cncontactvcardserialization)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CNContainer](https://developer.apple.com/documentation/contacts/cncontainer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CNContainer : NSObject, NSCopying, NSSecureCoding, NSCoding {     var identifier: String { get }     var name: String { get }     var type: CNContainerType { get } } extension CNContainer {     class func predicateForContainersWithIdentifiers(_ identifiers: [String]) -> NSPredicate     class func predicateForContainerOfContactWithIdentifier(_ contactIdentifier: String) -> NSPredicate     class func predicateForContainerOfGroupWithIdentifier(_ groupIdentifier: String) -> NSPredicate } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CNContainer : NSObject, NSCopying, NSSecureCoding {     var identifier: String { get }     var name: String { get }     var type: CNContainerType { get } } extension CNContainer {     class func predicateForContainersWithIdentifiers(_ identifiers: [String]) -> NSPredicate     class func predicateForContainerOfContactWithIdentifier(_ contactIdentifier: String) -> NSPredicate     class func predicateForContainerOfGroupWithIdentifier(_ groupIdentifier: String) -> NSPredicate } ``` | NSCopying, NSSecureCoding |

Modified [CNContainerType [enum]](https://developer.apple.com/documentation/contacts/cncontainertype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CNEntityType [enum]](https://developer.apple.com/documentation/contacts/cnentitytype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CNErrorCode [enum]](https://developer.apple.com/documentation/contacts/cnerrorcode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum CNErrorCode : Int {     case CommunicationError     case DataAccessError     case AuthorizationDenied     case RecordDoesNotExist     case InsertedRecordAlreadyExists     case ContainmentCycle     case ContainmentScope     case ParentRecordDoesNotExist     case ValidationMultipleErrors     case ValidationTypeMismatch     case ValidationConfigurationError     case PredicateInvalid     case PolicyViolation } extension CNErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension CNErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable |
| To | ``` enum CNErrorCode : Int {     case CommunicationError     case DataAccessError     case AuthorizationDenied     case RecordDoesNotExist     case InsertedRecordAlreadyExists     case ContainmentCycle     case ContainmentScope     case ParentRecordDoesNotExist     case ValidationMultipleErrors     case ValidationTypeMismatch     case ValidationConfigurationError     case PredicateInvalid     case PolicyViolation } extension CNErrorCode : _BridgedNSError { } extension CNErrorCode : _BridgedNSError { } ``` | -- |

Modified [CNGroup](https://developer.apple.com/documentation/contacts/cngroup)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CNGroup : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     var identifier: String { get }     var name: String { get } } extension CNGroup {     class func predicateForGroupsWithIdentifiers(_ identifiers: [String]) -> NSPredicate     class func predicateForSubgroupsInGroupWithIdentifier(_ parentGroupIdentifier: String) -> NSPredicate     class func predicateForGroupsInContainerWithIdentifier(_ containerIdentifier: String) -> NSPredicate } ``` | AnyObject, NSCoding, NSCopying, NSMutableCopying, NSSecureCoding |
| To | ``` class CNGroup : NSObject, NSCopying, NSMutableCopying, NSSecureCoding {     var identifier: String { get }     var name: String { get } } extension CNGroup {     class func predicateForGroupsWithIdentifiers(_ identifiers: [String]) -> NSPredicate     class func predicateForSubgroupsInGroupWithIdentifier(_ parentGroupIdentifier: String) -> NSPredicate     class func predicateForGroupsInContainerWithIdentifier(_ containerIdentifier: String) -> NSPredicate } ``` | NSCopying, NSMutableCopying, NSSecureCoding |

Modified [CNInstantMessageAddress](https://developer.apple.com/documentation/contacts/cninstantmessageaddress)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CNInstantMessageAddress : NSObject, NSCopying, NSSecureCoding, NSCoding {     var username: String { get }     var service: String { get }     init(username username: String, service service: String)     class func localizedStringForKey(_ key: String) -> String     class func localizedStringForService(_ service: String) -> String } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CNInstantMessageAddress : NSObject, NSCopying, NSSecureCoding {     var username: String { get }     var service: String { get }     init(username username: String, service service: String)     class func localizedStringForKey(_ key: String) -> String     class func localizedStringForService(_ service: String) -> String } ``` | NSCopying, NSSecureCoding |

Modified CNKeyDescriptor

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol CNKeyDescriptor : NSObjectProtocol, NSSecureCoding, NSCoding, NSCopying { } ``` | NSCoding, NSCopying, NSObjectProtocol, NSSecureCoding |
| To | ``` protocol CNKeyDescriptor : NSObjectProtocol, NSSecureCoding, NSCopying { } ``` | NSCopying, NSObjectProtocol, NSSecureCoding |

Modified [CNLabeledValue](https://developer.apple.com/documentation/contacts/cnlabeledvalue)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CNLabeledValue : NSObject, NSCopying, NSSecureCoding, NSCoding {     var identifier: String { get }     var label: String { get }     @NSCopying var value: protocol<NSCopying, NSSecureCoding> { get }     convenience init(label label: String?, value value: protocol<NSCopying, NSSecureCoding>)     class func labeledValueWithLabel(_ label: String?, value value: protocol<NSCopying, NSSecureCoding>) -> Self     init(label label: String?, value value: protocol<NSCopying, NSSecureCoding>)     func labeledValueBySettingLabel(_ label: String?) -> Self     func labeledValueBySettingValue(_ value: protocol<NSCopying, NSSecureCoding>) -> Self     func labeledValueBySettingLabel(_ label: String?, value value: protocol<NSCopying, NSSecureCoding>) -> Self     class func localizedStringForLabel(_ label: String) -> String } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CNLabeledValue : NSObject, NSCopying, NSSecureCoding {     var identifier: String { get }     var label: String { get }     @NSCopying var value: protocol<NSCopying, NSSecureCoding> { get }     convenience init(label label: String?, value value: protocol<NSCopying, NSSecureCoding>)     class func labeledValueWithLabel(_ label: String?, value value: protocol<NSCopying, NSSecureCoding>) -> Self     init(label label: String?, value value: protocol<NSCopying, NSSecureCoding>)     func labeledValueBySettingLabel(_ label: String?) -> Self     func labeledValueBySettingValue(_ value: protocol<NSCopying, NSSecureCoding>) -> Self     func labeledValueBySettingLabel(_ label: String?, value value: protocol<NSCopying, NSSecureCoding>) -> Self     class func localizedStringForLabel(_ label: String) -> String } ``` | NSCopying, NSSecureCoding |

Modified [CNMutableContact](https://developer.apple.com/documentation/contacts/cnmutablecontact)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CNMutableGroup](https://developer.apple.com/documentation/contacts/cnmutablegroup)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CNMutablePostalAddress](https://developer.apple.com/documentation/contacts/cnmutablepostaladdress)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CNPhoneNumber](https://developer.apple.com/documentation/contacts/cnphonenumber)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CNPhoneNumber : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init(stringValue stringValue: String)     class func phoneNumberWithStringValue(_ stringValue: String) -> Self     init(stringValue string: String)     var stringValue: String { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CNPhoneNumber : NSObject, NSCopying, NSSecureCoding {     convenience init(stringValue stringValue: String)     class func phoneNumberWithStringValue(_ stringValue: String) -> Self     init(stringValue string: String)     var stringValue: String { get } } ``` | NSCopying, NSSecureCoding |

Modified [CNPostalAddress](https://developer.apple.com/documentation/contacts/cnpostaladdress)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CNPostalAddress : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     var street: String { get }     var city: String { get }     var state: String { get }     var postalCode: String { get }     var country: String { get }     var ISOCountryCode: String { get }     class func localizedStringForKey(_ key: String) -> String } ``` | AnyObject, NSCoding, NSCopying, NSMutableCopying, NSSecureCoding |
| To | ``` class CNPostalAddress : NSObject, NSCopying, NSMutableCopying, NSSecureCoding {     var street: String { get }     var city: String { get }     var state: String { get }     var postalCode: String { get }     var country: String { get }     var ISOCountryCode: String { get }     class func localizedStringForKey(_ key: String) -> String } ``` | NSCopying, NSMutableCopying, NSSecureCoding |

Modified [CNPostalAddressFormatter](https://developer.apple.com/documentation/contacts/cnpostaladdressformatter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CNPostalAddressFormatterStyle [enum]](https://developer.apple.com/documentation/contacts/cnpostaladdressformatterstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CNSaveRequest](https://developer.apple.com/documentation/contacts/cnsaverequest)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CNSocialProfile](https://developer.apple.com/documentation/contacts/cnsocialprofile)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CNSocialProfile : NSObject, NSCopying, NSSecureCoding, NSCoding {     var urlString: String { get }     var username: String { get }     var userIdentifier: String { get }     var service: String { get }     init(urlString urlString: String?, username username: String?, userIdentifier userIdentifier: String?, service service: String?)     class func localizedStringForKey(_ key: String) -> String     class func localizedStringForService(_ service: String) -> String } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CNSocialProfile : NSObject, NSCopying, NSSecureCoding {     var urlString: String { get }     var username: String { get }     var userIdentifier: String { get }     var service: String { get }     init(urlString urlString: String?, username username: String?, userIdentifier userIdentifier: String?, service service: String?)     class func localizedStringForKey(_ key: String) -> String     class func localizedStringForService(_ service: String) -> String } ``` | NSCopying, NSSecureCoding |

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
