---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/AddressBook.html
archived_at: '2026-07-18T02:51:57.549331Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# AddressBook Changes

## AddressBook

Added NSObject.actionProperty() -> String!Added NSObject.performActionForPerson(ABPerson!, identifier: String!)Added NSObject.shouldEnableActionForPerson(ABPerson!, identifier: String!) -> BoolAdded NSObject.titleForPerson(ABPerson!, identifier: String!) -> String!Modified ABAddressBook.addRecord(ABRecord!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified ABAddressBook.defaultCountryCode() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified ABAddressBook.defaultNameOrdering() -> Int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified ABAddressBook.formattedAddressFromDictionary([NSObject: AnyObject]!) -> NSAttributedString!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified ABAddressBook.recordClassFromUniqueId(String!) -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified ABAddressBook.removeRecord(ABRecord!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified ABAddressBook.saveAndReturnError(NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified ABPeoplePickerView.target

|  | Declaration |
| --- | --- |
| From | ``` var target: AnyObject! ``` |
| To | ``` unowned(unsafe) var target: AnyObject! ``` |

Modified ABPerson.init(VCardRepresentation: NSData!)

|  | Declaration |
| --- | --- |
| From | ``` init(VCardRepresentation vCardData: NSData!) ``` |
| To | ``` init!(VCardRepresentation vCardData: NSData!) ``` |

Modified ABPerson.linkedPeople() -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified ABPersonView.shouldShowLinkedPeople

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified ABRecord.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified ABRecord.init(addressBook: ABAddressBook!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(addressBook addressBook: ABAddressBook!) ``` | OS X 10.10 |
| To | ``` init!(addressBook addressBook: ABAddressBook!) ``` | OS X 10.5 |

Modified ABRecord.isReadOnly() -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified ABRecord.setValue(AnyObject!, forProperty: String!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified ABSearchElement.init(forConjunction: ABSearchConjunction, children:[AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(forConjunction conjuction: ABSearchConjunction, children children: [AnyObject]!) -> ABSearchElement ``` |
| To | ``` init!(forConjunction conjuction: ABSearchConjunction, children children: [AnyObject]!) -> ABSearchElement ``` |

Modified ABAddressBookErrorDomain

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var ABAddressBookErrorDomain: NSString! ``` | OS X 10.10 |
| To | ``` let ABAddressBookErrorDomain: String ``` | OS X 10.7 |

Modified ABBeginLoadingImageDataForClient(ABPerson!, ABImageClientCallback, UnsafeMutablePointer<Void>) -> CFIndex

|  | Declaration |
| --- | --- |
| From | ``` func ABBeginLoadingImageDataForClient(_ person: ABPerson!, _ callback: ABImageClientCallback, _ refcon: UnsafePointer<()>) -> CFIndex ``` |
| To | ``` func ABBeginLoadingImageDataForClient(_ person: ABPerson!, _ callback: ABImageClientCallback, _ refcon: UnsafeMutablePointer<Void>) -> CFIndex ``` |

Modified ABCopyDefaultCountryCode(ABAddressBook!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified ABCopyRecordTypeFromUniqueId(ABAddressBook!, CFString!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified ABCreateFormattedAddressFromDictionary(ABAddressBook!, CFDictionary!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified ABImageClientCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias ABImageClientCallback = CFunctionPointer<((CFData!, CFIndex, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias ABImageClientCallback = CFunctionPointer<((CFData!, CFIndex, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified ABMultiValueAdd(ABMutableMultiValue!, AnyObject!, CFString!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ABMultiValueAdd(_ multiValue: ABMutableMultiValue!, _ value: AnyObject!, _ label: CFString!, _ outIdentifier: UnsafePointer<Unmanaged<CFString>?>) -> Bool ``` |
| To | ``` func ABMultiValueAdd(_ multiValue: ABMutableMultiValue!, _ value: AnyObject!, _ label: CFString!, _ outIdentifier: UnsafeMutablePointer<Unmanaged<CFString>?>) -> Bool ``` |

Modified ABMultiValueIdentifiersErrorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var ABMultiValueIdentifiersErrorKey: NSString! ``` | OS X 10.10 |
| To | ``` let ABMultiValueIdentifiersErrorKey: String ``` | OS X 10.7 |

Modified ABMultiValueInsert(ABMutableMultiValue!, AnyObject!, CFString!, CFIndex, UnsafeMutablePointer<Unmanaged<CFString>?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ABMultiValueInsert(_ multiValue: ABMutableMultiValue!, _ value: AnyObject!, _ label: CFString!, _ index: CFIndex, _ outIdentifier: UnsafePointer<Unmanaged<CFString>?>) -> Bool ``` |
| To | ``` func ABMultiValueInsert(_ multiValue: ABMutableMultiValue!, _ value: AnyObject!, _ label: CFString!, _ index: CFIndex, _ outIdentifier: UnsafeMutablePointer<Unmanaged<CFString>?>) -> Bool ``` |

Modified ABPeoplePickerDisplayedPropertyDidChangeNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ABPeoplePickerDisplayedPropertyDidChangeNotification: NSString! ``` | OS X 10.10 |
| To | ``` let ABPeoplePickerDisplayedPropertyDidChangeNotification: String ``` | OS X 10.3 |

Modified ABPeoplePickerGroupSelectionDidChangeNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ABPeoplePickerGroupSelectionDidChangeNotification: NSString! ``` | OS X 10.10 |
| To | ``` let ABPeoplePickerGroupSelectionDidChangeNotification: String ``` | OS X 10.3 |

Modified ABPeoplePickerNameSelectionDidChangeNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ABPeoplePickerNameSelectionDidChangeNotification: NSString! ``` | OS X 10.10 |
| To | ``` let ABPeoplePickerNameSelectionDidChangeNotification: String ``` | OS X 10.3 |

Modified ABPeoplePickerValueSelectionDidChangeNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ABPeoplePickerValueSelectionDidChangeNotification: NSString! ``` | OS X 10.10 |
| To | ``` let ABPeoplePickerValueSelectionDidChangeNotification: String ``` | OS X 10.3 |

Modified ABRecordCreateCopy(ABRecordRef) -> ABRecordRef

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified ABRecordIsReadOnly(ABRecordRef) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified ABRecordRef

|  | Declaration |
| --- | --- |
| From | ``` typealias ABRecordRef = UnsafePointer<()> ``` |
| To | ``` typealias ABRecordRef = UnsafeMutablePointer<Void> ``` |

Modified kABAddressCityKey

|  | Declaration |
| --- | --- |
| From | ``` let kABAddressCityKey: NSString! ``` |
| To | ``` let kABAddressCityKey: String ``` |

Modified kABAddressCountryCodeKey

|  | Declaration |
| --- | --- |
| From | ``` let kABAddressCountryCodeKey: NSString! ``` |
| To | ``` let kABAddressCountryCodeKey: String ``` |

Modified kABAddressCountryKey

|  | Declaration |
| --- | --- |
| From | ``` let kABAddressCountryKey: NSString! ``` |
| To | ``` let kABAddressCountryKey: String ``` |

Modified kABAddressHomeLabel

|  | Declaration |
| --- | --- |
| From | ``` let kABAddressHomeLabel: NSString! ``` |
| To | ``` let kABAddressHomeLabel: String ``` |

Modified kABAddressProperty

|  | Declaration |
| --- | --- |
| From | ``` let kABAddressProperty: NSString! ``` |
| To | ``` let kABAddressProperty: String ``` |

Modified kABAddressStateKey

|  | Declaration |
| --- | --- |
| From | ``` let kABAddressStateKey: NSString! ``` |
| To | ``` let kABAddressStateKey: String ``` |

Modified kABAddressStreetKey

|  | Declaration |
| --- | --- |
| From | ``` let kABAddressStreetKey: NSString! ``` |
| To | ``` let kABAddressStreetKey: String ``` |

Modified kABAddressWorkLabel

|  | Declaration |
| --- | --- |
| From | ``` let kABAddressWorkLabel: NSString! ``` |
| To | ``` let kABAddressWorkLabel: String ``` |

Modified kABAddressZIPKey

|  | Declaration |
| --- | --- |
| From | ``` let kABAddressZIPKey: NSString! ``` |
| To | ``` let kABAddressZIPKey: String ``` |

Modified kABAlternateBirthdayComponentsProperty

|  | Declaration |
| --- | --- |
| From | ``` let kABAlternateBirthdayComponentsProperty: NSString! ``` |
| To | ``` let kABAlternateBirthdayComponentsProperty: String ``` |

Modified kABAnniversaryLabel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABAnniversaryLabel: NSString! ``` | OS X 10.10 |
| To | ``` let kABAnniversaryLabel: String ``` | OS X 10.3 |

Modified kABAssistantLabel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABAssistantLabel: NSString! ``` | OS X 10.10 |
| To | ``` let kABAssistantLabel: String ``` | OS X 10.3 |

Modified kABBirthdayComponentsProperty

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABBirthdayComponentsProperty: NSString! ``` | OS X 10.10 |
| To | ``` let kABBirthdayComponentsProperty: String ``` | OS X 10.7 |

Modified kABBirthdayProperty

|  | Declaration |
| --- | --- |
| From | ``` let kABBirthdayProperty: NSString! ``` |
| To | ``` let kABBirthdayProperty: String ``` |

Modified kABBrotherLabel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABBrotherLabel: NSString! ``` | OS X 10.10 |
| To | ``` let kABBrotherLabel: String ``` | OS X 10.3 |

Modified kABCalendarURIsProperty

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABCalendarURIsProperty: NSString! ``` | OS X 10.10 |
| To | ``` let kABCalendarURIsProperty: String ``` | OS X 10.5 |

Modified kABChildLabel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABChildLabel: NSString! ``` | OS X 10.10 |
| To | ``` let kABChildLabel: String ``` | OS X 10.3 |

Modified kABCreationDateProperty

|  | Declaration |
| --- | --- |
| From | ``` let kABCreationDateProperty: NSString! ``` |
| To | ``` let kABCreationDateProperty: String ``` |

Modified kABDatabaseChangedExternallyNotification

|  | Declaration |
| --- | --- |
| From | ``` let kABDatabaseChangedExternallyNotification: NSString! ``` |
| To | ``` let kABDatabaseChangedExternallyNotification: String ``` |

Modified kABDatabaseChangedNotification

|  | Declaration |
| --- | --- |
| From | ``` let kABDatabaseChangedNotification: NSString! ``` |
| To | ``` let kABDatabaseChangedNotification: String ``` |

Modified kABDeletedRecords

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABDeletedRecords: NSString! ``` | OS X 10.10 |
| To | ``` let kABDeletedRecords: String ``` | OS X 10.3 |

Modified kABDepartmentProperty

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABDepartmentProperty: NSString! ``` | OS X 10.10 |
| To | ``` let kABDepartmentProperty: String ``` | OS X 10.3 |

Modified kABEmailHomeLabel

|  | Declaration |
| --- | --- |
| From | ``` let kABEmailHomeLabel: NSString! ``` |
| To | ``` let kABEmailHomeLabel: String ``` |

Modified kABEmailMobileMeLabel

|  | Declaration |
| --- | --- |
| From | ``` let kABEmailMobileMeLabel: NSString! ``` |
| To | ``` let kABEmailMobileMeLabel: String ``` |

Modified kABEmailProperty

|  | Declaration |
| --- | --- |
| From | ``` let kABEmailProperty: NSString! ``` |
| To | ``` let kABEmailProperty: String ``` |

Modified kABEmailWorkLabel

|  | Declaration |
| --- | --- |
| From | ``` let kABEmailWorkLabel: NSString! ``` |
| To | ``` let kABEmailWorkLabel: String ``` |

Modified kABFatherLabel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABFatherLabel: NSString! ``` | OS X 10.10 |
| To | ``` let kABFatherLabel: String ``` | OS X 10.3 |

Modified kABFirstNamePhoneticProperty

|  | Declaration |
| --- | --- |
| From | ``` let kABFirstNamePhoneticProperty: NSString! ``` |
| To | ``` let kABFirstNamePhoneticProperty: String ``` |

Modified kABFirstNameProperty

|  | Declaration |
| --- | --- |
| From | ``` let kABFirstNameProperty: NSString! ``` |
| To | ``` let kABFirstNameProperty: String ``` |

Modified kABFriendLabel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABFriendLabel: NSString! ``` | OS X 10.10 |
| To | ``` let kABFriendLabel: String ``` | OS X 10.3 |

Modified kABGroupNameProperty

|  | Declaration |
| --- | --- |
| From | ``` let kABGroupNameProperty: NSString! ``` |
| To | ``` let kABGroupNameProperty: String ``` |

Modified kABHomeLabel

|  | Declaration |
| --- | --- |
| From | ``` let kABHomeLabel: NSString! ``` |
| To | ``` let kABHomeLabel: String ``` |

Modified kABHomePageLabel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABHomePageLabel: NSString! ``` | OS X 10.10 |
| To | ``` let kABHomePageLabel: String ``` | OS X 10.4 |

Modified kABHomePageProperty

|  | Declaration |
| --- | --- |
| From | ``` let kABHomePageProperty: NSString! ``` |
| To | ``` let kABHomePageProperty: String ``` |

Modified kABInsertedRecords

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABInsertedRecords: NSString! ``` | OS X 10.10 |
| To | ``` let kABInsertedRecords: String ``` | OS X 10.3 |

Modified kABInstantMessageProperty

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABInstantMessageProperty: NSString! ``` | OS X 10.10 |
| To | ``` let kABInstantMessageProperty: String ``` | OS X 10.7 |

Modified kABInstantMessageServiceAIM

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABInstantMessageServiceAIM: NSString! ``` | OS X 10.10 |
| To | ``` let kABInstantMessageServiceAIM: String ``` | OS X 10.7 |

Modified kABInstantMessageServiceFacebook

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABInstantMessageServiceFacebook: NSString! ``` | OS X 10.10 |
| To | ``` let kABInstantMessageServiceFacebook: String ``` | OS X 10.7 |

Modified kABInstantMessageServiceGaduGadu

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABInstantMessageServiceGaduGadu: NSString! ``` | OS X 10.10 |
| To | ``` let kABInstantMessageServiceGaduGadu: String ``` | OS X 10.7 |

Modified kABInstantMessageServiceGoogleTalk

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABInstantMessageServiceGoogleTalk: NSString! ``` | OS X 10.10 |
| To | ``` let kABInstantMessageServiceGoogleTalk: String ``` | OS X 10.7 |

Modified kABInstantMessageServiceICQ

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABInstantMessageServiceICQ: NSString! ``` | OS X 10.10 |
| To | ``` let kABInstantMessageServiceICQ: String ``` | OS X 10.7 |

Modified kABInstantMessageServiceJabber

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABInstantMessageServiceJabber: NSString! ``` | OS X 10.10 |
| To | ``` let kABInstantMessageServiceJabber: String ``` | OS X 10.7 |

Modified kABInstantMessageServiceKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABInstantMessageServiceKey: NSString! ``` | OS X 10.10 |
| To | ``` let kABInstantMessageServiceKey: String ``` | OS X 10.7 |

Modified kABInstantMessageServiceMSN

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABInstantMessageServiceMSN: NSString! ``` | OS X 10.10 |
| To | ``` let kABInstantMessageServiceMSN: String ``` | OS X 10.7 |

Modified kABInstantMessageServiceQQ

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABInstantMessageServiceQQ: NSString! ``` | OS X 10.10 |
| To | ``` let kABInstantMessageServiceQQ: String ``` | OS X 10.7 |

Modified kABInstantMessageServiceSkype

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABInstantMessageServiceSkype: NSString! ``` | OS X 10.10 |
| To | ``` let kABInstantMessageServiceSkype: String ``` | OS X 10.7 |

Modified kABInstantMessageServiceYahoo

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABInstantMessageServiceYahoo: NSString! ``` | OS X 10.10 |
| To | ``` let kABInstantMessageServiceYahoo: String ``` | OS X 10.7 |

Modified kABInstantMessageUsernameKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABInstantMessageUsernameKey: NSString! ``` | OS X 10.10 |
| To | ``` let kABInstantMessageUsernameKey: String ``` | OS X 10.7 |

Modified kABJobTitleProperty

|  | Declaration |
| --- | --- |
| From | ``` let kABJobTitleProperty: NSString! ``` |
| To | ``` let kABJobTitleProperty: String ``` |

Modified kABLastNamePhoneticProperty

|  | Declaration |
| --- | --- |
| From | ``` let kABLastNamePhoneticProperty: NSString! ``` |
| To | ``` let kABLastNamePhoneticProperty: String ``` |

Modified kABLastNameProperty

|  | Declaration |
| --- | --- |
| From | ``` let kABLastNameProperty: NSString! ``` |
| To | ``` let kABLastNameProperty: String ``` |

Modified kABMaidenNameProperty

|  | Declaration |
| --- | --- |
| From | ``` let kABMaidenNameProperty: NSString! ``` |
| To | ``` let kABMaidenNameProperty: String ``` |

Modified kABManagerLabel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABManagerLabel: NSString! ``` | OS X 10.10 |
| To | ``` let kABManagerLabel: String ``` | OS X 10.3 |

Modified kABMiddleNamePhoneticProperty

|  | Declaration |
| --- | --- |
| From | ``` let kABMiddleNamePhoneticProperty: NSString! ``` |
| To | ``` let kABMiddleNamePhoneticProperty: String ``` |

Modified kABMiddleNameProperty

|  | Declaration |
| --- | --- |
| From | ``` let kABMiddleNameProperty: NSString! ``` |
| To | ``` let kABMiddleNameProperty: String ``` |

Modified kABMobileMeLabel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABMobileMeLabel: NSString! ``` | OS X 10.10 |
| To | ``` let kABMobileMeLabel: String ``` | OS X 10.7 |

Modified kABModificationDateProperty

|  | Declaration |
| --- | --- |
| From | ``` let kABModificationDateProperty: NSString! ``` |
| To | ``` let kABModificationDateProperty: String ``` |

Modified kABMotherLabel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABMotherLabel: NSString! ``` | OS X 10.10 |
| To | ``` let kABMotherLabel: String ``` | OS X 10.3 |

Modified kABNicknameProperty

|  | Declaration |
| --- | --- |
| From | ``` let kABNicknameProperty: NSString! ``` |
| To | ``` let kABNicknameProperty: String ``` |

Modified kABNoteProperty

|  | Declaration |
| --- | --- |
| From | ``` let kABNoteProperty: NSString! ``` |
| To | ``` let kABNoteProperty: String ``` |

Modified kABOrganizationProperty

|  | Declaration |
| --- | --- |
| From | ``` let kABOrganizationProperty: NSString! ``` |
| To | ``` let kABOrganizationProperty: String ``` |

Modified kABOtherDateComponentsProperty

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABOtherDateComponentsProperty: NSString! ``` | OS X 10.10 |
| To | ``` let kABOtherDateComponentsProperty: String ``` | OS X 10.7 |

Modified kABOtherDatesProperty

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABOtherDatesProperty: NSString! ``` | OS X 10.10 |
| To | ``` let kABOtherDatesProperty: String ``` | OS X 10.3 |

Modified kABOtherLabel

|  | Declaration |
| --- | --- |
| From | ``` let kABOtherLabel: NSString! ``` |
| To | ``` let kABOtherLabel: String ``` |

Modified kABParentLabel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABParentLabel: NSString! ``` | OS X 10.10 |
| To | ``` let kABParentLabel: String ``` | OS X 10.3 |

Modified kABPartnerLabel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABPartnerLabel: NSString! ``` | OS X 10.10 |
| To | ``` let kABPartnerLabel: String ``` | OS X 10.3 |

Modified kABPersonFlags

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABPersonFlags: NSString! ``` | OS X 10.10 |
| To | ``` let kABPersonFlags: String ``` | OS X 10.3 |

Modified kABPhoneHomeFAXLabel

|  | Declaration |
| --- | --- |
| From | ``` let kABPhoneHomeFAXLabel: NSString! ``` |
| To | ``` let kABPhoneHomeFAXLabel: String ``` |

Modified kABPhoneHomeLabel

|  | Declaration |
| --- | --- |
| From | ``` let kABPhoneHomeLabel: NSString! ``` |
| To | ``` let kABPhoneHomeLabel: String ``` |

Modified kABPhoneMainLabel

|  | Declaration |
| --- | --- |
| From | ``` let kABPhoneMainLabel: NSString! ``` |
| To | ``` let kABPhoneMainLabel: String ``` |

Modified kABPhoneMobileLabel

|  | Declaration |
| --- | --- |
| From | ``` let kABPhoneMobileLabel: NSString! ``` |
| To | ``` let kABPhoneMobileLabel: String ``` |

Modified kABPhonePagerLabel

|  | Declaration |
| --- | --- |
| From | ``` let kABPhonePagerLabel: NSString! ``` |
| To | ``` let kABPhonePagerLabel: String ``` |

Modified kABPhoneProperty

|  | Declaration |
| --- | --- |
| From | ``` let kABPhoneProperty: NSString! ``` |
| To | ``` let kABPhoneProperty: String ``` |

Modified kABPhoneWorkFAXLabel

|  | Declaration |
| --- | --- |
| From | ``` let kABPhoneWorkFAXLabel: NSString! ``` |
| To | ``` let kABPhoneWorkFAXLabel: String ``` |

Modified kABPhoneWorkLabel

|  | Declaration |
| --- | --- |
| From | ``` let kABPhoneWorkLabel: NSString! ``` |
| To | ``` let kABPhoneWorkLabel: String ``` |

Modified kABPhoneiPhoneLabel

|  | Declaration |
| --- | --- |
| From | ``` let kABPhoneiPhoneLabel: NSString! ``` |
| To | ``` let kABPhoneiPhoneLabel: String ``` |

Modified kABRelatedNamesProperty

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABRelatedNamesProperty: NSString! ``` | OS X 10.10 |
| To | ``` let kABRelatedNamesProperty: String ``` | OS X 10.3 |

Modified kABSisterLabel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABSisterLabel: NSString! ``` | OS X 10.10 |
| To | ``` let kABSisterLabel: String ``` | OS X 10.3 |

Modified kABSocialProfileProperty

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABSocialProfileProperty: NSString! ``` | OS X 10.10 |
| To | ``` let kABSocialProfileProperty: String ``` | OS X 10.7 |

Modified kABSocialProfileServiceFacebook

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABSocialProfileServiceFacebook: NSString! ``` | OS X 10.10 |
| To | ``` let kABSocialProfileServiceFacebook: String ``` | OS X 10.7 |

Modified kABSocialProfileServiceFlickr

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABSocialProfileServiceFlickr: NSString! ``` | OS X 10.10 |
| To | ``` let kABSocialProfileServiceFlickr: String ``` | OS X 10.7 |

Modified kABSocialProfileServiceKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABSocialProfileServiceKey: NSString! ``` | OS X 10.10 |
| To | ``` let kABSocialProfileServiceKey: String ``` | OS X 10.7 |

Modified kABSocialProfileServiceLinkedIn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABSocialProfileServiceLinkedIn: NSString! ``` | OS X 10.10 |
| To | ``` let kABSocialProfileServiceLinkedIn: String ``` | OS X 10.7 |

Modified kABSocialProfileServiceMySpace

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABSocialProfileServiceMySpace: NSString! ``` | OS X 10.10 |
| To | ``` let kABSocialProfileServiceMySpace: String ``` | OS X 10.7 |

Modified kABSocialProfileServiceSinaWeibo

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABSocialProfileServiceSinaWeibo: NSString! ``` | OS X 10.10 |
| To | ``` let kABSocialProfileServiceSinaWeibo: String ``` | OS X 10.8 |

Modified kABSocialProfileServiceTencentWeibo

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABSocialProfileServiceTencentWeibo: NSString! ``` | OS X 10.10 |
| To | ``` let kABSocialProfileServiceTencentWeibo: String ``` | OS X 10.9 |

Modified kABSocialProfileServiceTwitter

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABSocialProfileServiceTwitter: NSString! ``` | OS X 10.10 |
| To | ``` let kABSocialProfileServiceTwitter: String ``` | OS X 10.7 |

Modified kABSocialProfileServiceYelp

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABSocialProfileServiceYelp: NSString! ``` | OS X 10.10 |
| To | ``` let kABSocialProfileServiceYelp: String ``` | OS X 10.9 |

Modified kABSocialProfileURLKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABSocialProfileURLKey: NSString! ``` | OS X 10.10 |
| To | ``` let kABSocialProfileURLKey: String ``` | OS X 10.7 |

Modified kABSocialProfileUserIdentifierKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABSocialProfileUserIdentifierKey: NSString! ``` | OS X 10.10 |
| To | ``` let kABSocialProfileUserIdentifierKey: String ``` | OS X 10.7 |

Modified kABSocialProfileUsernameKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABSocialProfileUsernameKey: NSString! ``` | OS X 10.10 |
| To | ``` let kABSocialProfileUsernameKey: String ``` | OS X 10.7 |

Modified kABSpouseLabel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABSpouseLabel: NSString! ``` | OS X 10.10 |
| To | ``` let kABSpouseLabel: String ``` | OS X 10.3 |

Modified kABSuffixProperty

|  | Declaration |
| --- | --- |
| From | ``` let kABSuffixProperty: NSString! ``` |
| To | ``` let kABSuffixProperty: String ``` |

Modified kABTitleProperty

|  | Declaration |
| --- | --- |
| From | ``` let kABTitleProperty: NSString! ``` |
| To | ``` let kABTitleProperty: String ``` |

Modified kABUIDProperty

|  | Declaration |
| --- | --- |
| From | ``` let kABUIDProperty: NSString! ``` |
| To | ``` let kABUIDProperty: String ``` |

Modified kABURLsProperty

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABURLsProperty: NSString! ``` | OS X 10.10 |
| To | ``` let kABURLsProperty: String ``` | OS X 10.4 |

Modified kABUpdatedRecords

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kABUpdatedRecords: NSString! ``` | OS X 10.10 |
| To | ``` let kABUpdatedRecords: String ``` | OS X 10.3 |

Modified kABWorkLabel

|  | Declaration |
| --- | --- |
| From | ``` let kABWorkLabel: NSString! ``` |
| To | ``` let kABWorkLabel: String ``` |

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
