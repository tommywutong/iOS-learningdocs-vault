---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Swift/AddressBook.html
archived_at: '2026-07-18T02:53:50.045240Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# AddressBook Changes for Swift

### AddressBook

Modified [ABAddressBookRef](https://developer.apple.com/documentation/addressbook/abaddressbookref)

|  | Name | Declaration |
| --- | --- | --- |
| From | ABAddressBook | ``` typealias ABAddressBookRef = ABAddressBook ``` |
| To | ABAddressBookRef | ``` class ABAddressBookRef { } ``` |

Modified [ABGroupRef](https://developer.apple.com/documentation/addressbook/abgroupref)

|  | Declaration |
| --- | --- |
| From | ``` typealias ABGroupRef = ABGroup ``` |
| To | ``` class ABGroupRef { } ``` |

Modified [ABMultiValueRef](https://developer.apple.com/documentation/addressbook/abmultivalueref)

|  | Name | Declaration |
| --- | --- | --- |
| From | ABMultiValue | ``` typealias ABMultiValueRef = ABMultiValue ``` |
| To | ABMultiValueRef | ``` class ABMultiValueRef { } ``` |

Modified [ABMutableMultiValueRef](https://developer.apple.com/documentation/addressbook/abmutablemultivalueref)

|  | Declaration |
| --- | --- |
| From | ``` typealias ABMutableMultiValueRef = ABMutableMultiValue ``` |
| To | ``` class ABMutableMultiValueRef { } ``` |

Modified [ABPersonRef](https://developer.apple.com/documentation/addressbook/abpersonref)

|  | Declaration |
| --- | --- |
| From | ``` typealias ABPersonRef = ABPerson ``` |
| To | ``` class ABPersonRef { } ``` |

Modified [ABSearchElementRef](https://developer.apple.com/documentation/addressbook/absearchelementref)

|  | Declaration |
| --- | --- |
| From | ``` typealias ABSearchElementRef = ABSearchElement ``` |
| To | ``` class ABSearchElementRef { } ``` |

Modified [ABAddPropertiesAndTypes(_: ABAddressBookRef!, _: CFString!, _: CFDictionary!) -> CFIndex](https://developer.apple.com/documentation/addressbook/1430200-abaddpropertiesandtypes)

|  | Declaration |
| --- | --- |
| From | ``` func ABAddPropertiesAndTypes(_ addressBook: ABAddressBook!, _ recordType: CFString!, _ propertiesAndTypes: CFDictionary!) -> CFIndex ``` |
| To | ``` func ABAddPropertiesAndTypes(_ addressBook: ABAddressBookRef!, _ recordType: CFString!, _ propertiesAndTypes: CFDictionary!) -> CFIndex ``` |

Modified [ABAddRecord(_: ABAddressBookRef!, _: ABRecordRef) -> Bool](https://developer.apple.com/documentation/addressbook/1430088-abaddrecord)

|  | Declaration |
| --- | --- |
| From | ``` func ABAddRecord(_ addressBook: ABAddressBook!, _ record: ABRecordRef) -> Bool ``` |
| To | ``` func ABAddRecord(_ addressBook: ABAddressBookRef!, _ record: ABRecordRef) -> Bool ``` |

Modified [ABBeginLoadingImageDataForClient(_: ABPersonRef!, _: ABImageClientCallback!, _: UnsafeMutablePointer<Void>) -> CFIndex](https://developer.apple.com/documentation/addressbook/1430129-abbeginloadingimagedataforclient)

|  | Declaration |
| --- | --- |
| From | ``` func ABBeginLoadingImageDataForClient(_ person: ABPerson!, _ callback: ABImageClientCallback!, _ refcon: UnsafeMutablePointer<Void>) -> CFIndex ``` |
| To | ``` func ABBeginLoadingImageDataForClient(_ person: ABPersonRef!, _ callback: ABImageClientCallback!, _ refcon: UnsafeMutablePointer<Void>) -> CFIndex ``` |

Modified [ABCopyArrayOfAllGroups(_: ABAddressBookRef!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/addressbook/1430084-abcopyarrayofallgroups)

|  | Declaration |
| --- | --- |
| From | ``` func ABCopyArrayOfAllGroups(_ addressBook: ABAddressBook!) -> Unmanaged<CFArray>! ``` |
| To | ``` func ABCopyArrayOfAllGroups(_ addressBook: ABAddressBookRef!) -> Unmanaged<CFArray>! ``` |

Modified [ABCopyArrayOfAllPeople(_: ABAddressBookRef!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/addressbook/1430121-abcopyarrayofallpeople)

|  | Declaration |
| --- | --- |
| From | ``` func ABCopyArrayOfAllPeople(_ addressBook: ABAddressBook!) -> Unmanaged<CFArray>! ``` |
| To | ``` func ABCopyArrayOfAllPeople(_ addressBook: ABAddressBookRef!) -> Unmanaged<CFArray>! ``` |

Modified [ABCopyArrayOfMatchingRecords(_: ABAddressBookRef!, _: ABSearchElementRef!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/addressbook/1430194-abcopyarrayofmatchingrecords)

|  | Declaration |
| --- | --- |
| From | ``` func ABCopyArrayOfMatchingRecords(_ addressBook: ABAddressBook!, _ search: ABSearchElement!) -> Unmanaged<CFArray>! ``` |
| To | ``` func ABCopyArrayOfMatchingRecords(_ addressBook: ABAddressBookRef!, _ search: ABSearchElementRef!) -> Unmanaged<CFArray>! ``` |

Modified [ABCopyArrayOfPropertiesForRecordType(_: ABAddressBookRef!, _: CFString!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/addressbook/1430151-abcopyarrayofpropertiesforrecord)

|  | Declaration |
| --- | --- |
| From | ``` func ABCopyArrayOfPropertiesForRecordType(_ addressBook: ABAddressBook!, _ recordType: CFString!) -> Unmanaged<CFArray>! ``` |
| To | ``` func ABCopyArrayOfPropertiesForRecordType(_ addressBook: ABAddressBookRef!, _ recordType: CFString!) -> Unmanaged<CFArray>! ``` |

Modified [ABCopyDefaultCountryCode(_: ABAddressBookRef!) -> Unmanaged<CFString>!](https://developer.apple.com/documentation/addressbook/1430188-abcopydefaultcountrycode)

|  | Declaration |
| --- | --- |
| From | ``` func ABCopyDefaultCountryCode(_ addressBook: ABAddressBook!) -> Unmanaged<CFString>! ``` |
| To | ``` func ABCopyDefaultCountryCode(_ addressBook: ABAddressBookRef!) -> Unmanaged<CFString>! ``` |

Modified [ABCopyRecordForUniqueId(_: ABAddressBookRef!, _: CFString!) -> ABRecordRef](https://developer.apple.com/documentation/addressbook/1430103-abcopyrecordforuniqueid)

|  | Declaration |
| --- | --- |
| From | ``` func ABCopyRecordForUniqueId(_ addressBook: ABAddressBook!, _ uniqueId: CFString!) -> ABRecordRef ``` |
| To | ``` func ABCopyRecordForUniqueId(_ addressBook: ABAddressBookRef!, _ uniqueId: CFString!) -> ABRecordRef ``` |

Modified [ABCopyRecordTypeFromUniqueId(_: ABAddressBookRef!, _: CFString!) -> Unmanaged<CFString>!](https://developer.apple.com/documentation/addressbook/1430092-abcopyrecordtypefromuniqueid)

|  | Declaration |
| --- | --- |
| From | ``` func ABCopyRecordTypeFromUniqueId(_ addressBook: ABAddressBook!, _ uniqueId: CFString!) -> Unmanaged<CFString>! ``` |
| To | ``` func ABCopyRecordTypeFromUniqueId(_ addressBook: ABAddressBookRef!, _ uniqueId: CFString!) -> Unmanaged<CFString>! ``` |

Modified [ABCreateFormattedAddressFromDictionary(_: ABAddressBookRef!, _: CFDictionary!) -> Unmanaged<CFString>!](https://developer.apple.com/documentation/addressbook/1430209-abcreateformattedaddressfromdict)

|  | Declaration |
| --- | --- |
| From | ``` func ABCreateFormattedAddressFromDictionary(_ addressBook: ABAddressBook!, _ address: CFDictionary!) -> Unmanaged<CFString>! ``` |
| To | ``` func ABCreateFormattedAddressFromDictionary(_ addressBook: ABAddressBookRef!, _ address: CFDictionary!) -> Unmanaged<CFString>! ``` |

Modified [ABGetMe(_: ABAddressBookRef!) -> Unmanaged<ABPersonRef>!](https://developer.apple.com/documentation/addressbook/1430190-abgetme)

|  | Declaration |
| --- | --- |
| From | ``` func ABGetMe(_ addressBook: ABAddressBook!) -> Unmanaged<ABPerson>! ``` |
| To | ``` func ABGetMe(_ addressBook: ABAddressBookRef!) -> Unmanaged<ABPersonRef>! ``` |

Modified [ABGetSharedAddressBook() -> Unmanaged<ABAddressBookRef>!](https://developer.apple.com/documentation/addressbook/1430178-abgetsharedaddressbook)

|  | Declaration |
| --- | --- |
| From | ``` func ABGetSharedAddressBook() -> Unmanaged<ABAddressBook>! ``` |
| To | ``` func ABGetSharedAddressBook() -> Unmanaged<ABAddressBookRef>! ``` |

Modified [ABGroupAddGroup(_: ABGroupRef!, _: ABGroupRef!) -> Bool](https://developer.apple.com/documentation/addressbook/1430096-abgroupaddgroup)

|  | Declaration |
| --- | --- |
| From | ``` func ABGroupAddGroup(_ group: ABGroup!, _ groupToAdd: ABGroup!) -> Bool ``` |
| To | ``` func ABGroupAddGroup(_ group: ABGroupRef!, _ groupToAdd: ABGroupRef!) -> Bool ``` |

Modified [ABGroupAddMember(_: ABGroupRef!, _: ABPersonRef!) -> Bool](https://developer.apple.com/documentation/addressbook/1430147-abgroupaddmember)

|  | Declaration |
| --- | --- |
| From | ``` func ABGroupAddMember(_ group: ABGroup!, _ personToAdd: ABPerson!) -> Bool ``` |
| To | ``` func ABGroupAddMember(_ group: ABGroupRef!, _ personToAdd: ABPersonRef!) -> Bool ``` |

Modified [ABGroupCopyArrayOfAllMembers(_: ABGroupRef!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/addressbook/1430149-abgroupcopyarrayofallmembers)

|  | Declaration |
| --- | --- |
| From | ``` func ABGroupCopyArrayOfAllMembers(_ group: ABGroup!) -> Unmanaged<CFArray>! ``` |
| To | ``` func ABGroupCopyArrayOfAllMembers(_ group: ABGroupRef!) -> Unmanaged<CFArray>! ``` |

Modified [ABGroupCopyArrayOfAllSubgroups(_: ABGroupRef!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/addressbook/1430162-abgroupcopyarrayofallsubgroups)

|  | Declaration |
| --- | --- |
| From | ``` func ABGroupCopyArrayOfAllSubgroups(_ group: ABGroup!) -> Unmanaged<CFArray>! ``` |
| To | ``` func ABGroupCopyArrayOfAllSubgroups(_ group: ABGroupRef!) -> Unmanaged<CFArray>! ``` |

Modified [ABGroupCopyDistributionIdentifier(_: ABGroupRef!, _: ABPersonRef!, _: CFString!) -> Unmanaged<CFString>!](https://developer.apple.com/documentation/addressbook/1430187-abgroupcopydistributionidentifie)

|  | Declaration |
| --- | --- |
| From | ``` func ABGroupCopyDistributionIdentifier(_ group: ABGroup!, _ person: ABPerson!, _ property: CFString!) -> Unmanaged<CFString>! ``` |
| To | ``` func ABGroupCopyDistributionIdentifier(_ group: ABGroupRef!, _ person: ABPersonRef!, _ property: CFString!) -> Unmanaged<CFString>! ``` |

Modified [ABGroupCopyParentGroups(_: ABGroupRef!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/addressbook/1430153-abgroupcopyparentgroups)

|  | Declaration |
| --- | --- |
| From | ``` func ABGroupCopyParentGroups(_ group: ABGroup!) -> Unmanaged<CFArray>! ``` |
| To | ``` func ABGroupCopyParentGroups(_ group: ABGroupRef!) -> Unmanaged<CFArray>! ``` |

Modified [ABGroupCreate() -> Unmanaged<ABGroupRef>!](https://developer.apple.com/documentation/addressbook/1430086-abgroupcreate)

|  | Declaration |
| --- | --- |
| From | ``` func ABGroupCreate() -> Unmanaged<ABGroup>! ``` |
| To | ``` func ABGroupCreate() -> Unmanaged<ABGroupRef>! ``` |

Modified [ABGroupCreateSearchElement(_: CFString!, _: CFString!, _: CFString!, _: AnyObject!, _: ABSearchComparison) -> Unmanaged<ABSearchElementRef>!](https://developer.apple.com/documentation/addressbook/1430122-abgroupcreatesearchelement)

|  | Declaration |
| --- | --- |
| From | ``` func ABGroupCreateSearchElement(_ property: CFString!, _ label: CFString!, _ key: CFString!, _ value: AnyObject!, _ comparison: ABSearchComparison) -> Unmanaged<ABSearchElement>! ``` |
| To | ``` func ABGroupCreateSearchElement(_ property: CFString!, _ label: CFString!, _ key: CFString!, _ value: AnyObject!, _ comparison: ABSearchComparison) -> Unmanaged<ABSearchElementRef>! ``` |

Modified [ABGroupRemoveGroup(_: ABGroupRef!, _: ABGroupRef!) -> Bool](https://developer.apple.com/documentation/addressbook/1430186-abgroupremovegroup)

|  | Declaration |
| --- | --- |
| From | ``` func ABGroupRemoveGroup(_ group: ABGroup!, _ groupToRemove: ABGroup!) -> Bool ``` |
| To | ``` func ABGroupRemoveGroup(_ group: ABGroupRef!, _ groupToRemove: ABGroupRef!) -> Bool ``` |

Modified [ABGroupRemoveMember(_: ABGroupRef!, _: ABPersonRef!) -> Bool](https://developer.apple.com/documentation/addressbook/1430206-abgroupremovemember)

|  | Declaration |
| --- | --- |
| From | ``` func ABGroupRemoveMember(_ group: ABGroup!, _ personToRemove: ABPerson!) -> Bool ``` |
| To | ``` func ABGroupRemoveMember(_ group: ABGroupRef!, _ personToRemove: ABPersonRef!) -> Bool ``` |

Modified [ABGroupSetDistributionIdentifier(_: ABGroupRef!, _: ABPersonRef!, _: CFString!, _: CFString!) -> Bool](https://developer.apple.com/documentation/addressbook/1430174-abgroupsetdistributionidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func ABGroupSetDistributionIdentifier(_ group: ABGroup!, _ person: ABPerson!, _ property: CFString!, _ identifier: CFString!) -> Bool ``` |
| To | ``` func ABGroupSetDistributionIdentifier(_ group: ABGroupRef!, _ person: ABPersonRef!, _ property: CFString!, _ identifier: CFString!) -> Bool ``` |

Modified [ABHasUnsavedChanges(_: ABAddressBookRef!) -> Bool](https://developer.apple.com/documentation/addressbook/1430155-abhasunsavedchanges)

|  | Declaration |
| --- | --- |
| From | ``` func ABHasUnsavedChanges(_ addressBook: ABAddressBook!) -> Bool ``` |
| To | ``` func ABHasUnsavedChanges(_ addressBook: ABAddressBookRef!) -> Bool ``` |

Modified [ABMultiValueAdd(_: ABMutableMultiValueRef!, _: AnyObject!, _: CFString!, _: UnsafeMutablePointer<Unmanaged<CFString>?>) -> Bool](https://developer.apple.com/documentation/addressbook/1430137-abmultivalueadd)

|  | Declaration |
| --- | --- |
| From | ``` func ABMultiValueAdd(_ multiValue: ABMutableMultiValue!, _ value: AnyObject!, _ label: CFString!, _ outIdentifier: UnsafeMutablePointer<Unmanaged<CFString>?>) -> Bool ``` |
| To | ``` func ABMultiValueAdd(_ multiValue: ABMutableMultiValueRef!, _ value: AnyObject!, _ label: CFString!, _ outIdentifier: UnsafeMutablePointer<Unmanaged<CFString>?>) -> Bool ``` |

Modified [ABMultiValueCopyIdentifierAtIndex(_: ABMultiValueRef!, _: CFIndex) -> Unmanaged<CFString>!](https://developer.apple.com/documentation/addressbook/1430125-abmultivaluecopyidentifieratinde)

|  | Declaration |
| --- | --- |
| From | ``` func ABMultiValueCopyIdentifierAtIndex(_ multiValue: ABMultiValue!, _ index: CFIndex) -> Unmanaged<CFString>! ``` |
| To | ``` func ABMultiValueCopyIdentifierAtIndex(_ multiValue: ABMultiValueRef!, _ index: CFIndex) -> Unmanaged<CFString>! ``` |

Modified [ABMultiValueCopyLabelAtIndex(_: ABMultiValueRef!, _: CFIndex) -> Unmanaged<CFString>!](https://developer.apple.com/documentation/addressbook/1430131-abmultivaluecopylabelatindex)

|  | Declaration |
| --- | --- |
| From | ``` func ABMultiValueCopyLabelAtIndex(_ multiValue: ABMultiValue!, _ index: CFIndex) -> Unmanaged<CFString>! ``` |
| To | ``` func ABMultiValueCopyLabelAtIndex(_ multiValue: ABMultiValueRef!, _ index: CFIndex) -> Unmanaged<CFString>! ``` |

Modified [ABMultiValueCopyPrimaryIdentifier(_: ABMultiValueRef!) -> Unmanaged<CFString>!](https://developer.apple.com/documentation/addressbook/1430098-abmultivaluecopyprimaryidentifie)

|  | Declaration |
| --- | --- |
| From | ``` func ABMultiValueCopyPrimaryIdentifier(_ multiValue: ABMultiValue!) -> Unmanaged<CFString>! ``` |
| To | ``` func ABMultiValueCopyPrimaryIdentifier(_ multiValue: ABMultiValueRef!) -> Unmanaged<CFString>! ``` |

Modified [ABMultiValueCopyValueAtIndex(_: ABMultiValueRef!, _: CFIndex) -> Unmanaged<AnyObject>!](https://developer.apple.com/documentation/addressbook/1430101-abmultivaluecopyvalueatindex)

|  | Declaration |
| --- | --- |
| From | ``` func ABMultiValueCopyValueAtIndex(_ multiValue: ABMultiValue!, _ index: CFIndex) -> Unmanaged<AnyObject>! ``` |
| To | ``` func ABMultiValueCopyValueAtIndex(_ multiValue: ABMultiValueRef!, _ index: CFIndex) -> Unmanaged<AnyObject>! ``` |

Modified [ABMultiValueCount(_: ABMultiValueRef!) -> CFIndex](https://developer.apple.com/documentation/addressbook/1430111-abmultivaluecount)

|  | Declaration |
| --- | --- |
| From | ``` func ABMultiValueCount(_ multiValue: ABMultiValue!) -> CFIndex ``` |
| To | ``` func ABMultiValueCount(_ multiValue: ABMultiValueRef!) -> CFIndex ``` |

Modified [ABMultiValueCreate() -> Unmanaged<ABMultiValueRef>!](https://developer.apple.com/documentation/addressbook/1430183-abmultivaluecreate)

|  | Declaration |
| --- | --- |
| From | ``` func ABMultiValueCreate() -> Unmanaged<ABMultiValue>! ``` |
| To | ``` func ABMultiValueCreate() -> Unmanaged<ABMultiValueRef>! ``` |

Modified [ABMultiValueCreateCopy(_: ABMultiValueRef!) -> Unmanaged<ABMultiValueRef>!](https://developer.apple.com/documentation/addressbook/1430207-abmultivaluecreatecopy)

|  | Declaration |
| --- | --- |
| From | ``` func ABMultiValueCreateCopy(_ multiValue: ABMultiValue!) -> Unmanaged<ABMultiValue>! ``` |
| To | ``` func ABMultiValueCreateCopy(_ multiValue: ABMultiValueRef!) -> Unmanaged<ABMultiValueRef>! ``` |

Modified [ABMultiValueCreateMutable() -> Unmanaged<ABMutableMultiValueRef>!](https://developer.apple.com/documentation/addressbook/1430166-abmultivaluecreatemutable)

|  | Declaration |
| --- | --- |
| From | ``` func ABMultiValueCreateMutable() -> Unmanaged<ABMutableMultiValue>! ``` |
| To | ``` func ABMultiValueCreateMutable() -> Unmanaged<ABMutableMultiValueRef>! ``` |

Modified [ABMultiValueCreateMutableCopy(_: ABMultiValueRef!) -> Unmanaged<ABMutableMultiValueRef>!](https://developer.apple.com/documentation/addressbook/1430159-abmultivaluecreatemutablecopy)

|  | Declaration |
| --- | --- |
| From | ``` func ABMultiValueCreateMutableCopy(_ multiValue: ABMultiValue!) -> Unmanaged<ABMutableMultiValue>! ``` |
| To | ``` func ABMultiValueCreateMutableCopy(_ multiValue: ABMultiValueRef!) -> Unmanaged<ABMutableMultiValueRef>! ``` |

Modified [ABMultiValueIndexForIdentifier(_: ABMultiValueRef!, _: CFString!) -> CFIndex](https://developer.apple.com/documentation/addressbook/1430185-abmultivalueindexforidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func ABMultiValueIndexForIdentifier(_ multiValue: ABMultiValue!, _ identifier: CFString!) -> CFIndex ``` |
| To | ``` func ABMultiValueIndexForIdentifier(_ multiValue: ABMultiValueRef!, _ identifier: CFString!) -> CFIndex ``` |

Modified [ABMultiValueInsert(_: ABMutableMultiValueRef!, _: AnyObject!, _: CFString!, _: CFIndex, _: UnsafeMutablePointer<Unmanaged<CFString>?>) -> Bool](https://developer.apple.com/documentation/addressbook/1430109-abmultivalueinsert)

|  | Declaration |
| --- | --- |
| From | ``` func ABMultiValueInsert(_ multiValue: ABMutableMultiValue!, _ value: AnyObject!, _ label: CFString!, _ index: CFIndex, _ outIdentifier: UnsafeMutablePointer<Unmanaged<CFString>?>) -> Bool ``` |
| To | ``` func ABMultiValueInsert(_ multiValue: ABMutableMultiValueRef!, _ value: AnyObject!, _ label: CFString!, _ index: CFIndex, _ outIdentifier: UnsafeMutablePointer<Unmanaged<CFString>?>) -> Bool ``` |

Modified [ABMultiValuePropertyType(_: ABMultiValueRef!) -> ABPropertyType](https://developer.apple.com/documentation/addressbook/1430124-abmultivaluepropertytype)

|  | Declaration |
| --- | --- |
| From | ``` func ABMultiValuePropertyType(_ multiValue: ABMultiValue!) -> ABPropertyType ``` |
| To | ``` func ABMultiValuePropertyType(_ multiValue: ABMultiValueRef!) -> ABPropertyType ``` |

Modified [ABMultiValueRemove(_: ABMutableMultiValueRef!, _: CFIndex) -> Bool](https://developer.apple.com/documentation/addressbook/1430115-abmultivalueremove)

|  | Declaration |
| --- | --- |
| From | ``` func ABMultiValueRemove(_ multiValue: ABMutableMultiValue!, _ index: CFIndex) -> Bool ``` |
| To | ``` func ABMultiValueRemove(_ multiValue: ABMutableMultiValueRef!, _ index: CFIndex) -> Bool ``` |

Modified [ABMultiValueReplaceLabel(_: ABMutableMultiValueRef!, _: CFString!, _: CFIndex) -> Bool](https://developer.apple.com/documentation/addressbook/1430204-abmultivaluereplacelabel)

|  | Declaration |
| --- | --- |
| From | ``` func ABMultiValueReplaceLabel(_ multiValue: ABMutableMultiValue!, _ label: CFString!, _ index: CFIndex) -> Bool ``` |
| To | ``` func ABMultiValueReplaceLabel(_ multiValue: ABMutableMultiValueRef!, _ label: CFString!, _ index: CFIndex) -> Bool ``` |

Modified [ABMultiValueReplaceValue(_: ABMutableMultiValueRef!, _: AnyObject!, _: CFIndex) -> Bool](https://developer.apple.com/documentation/addressbook/1430211-abmultivaluereplacevalue)

|  | Declaration |
| --- | --- |
| From | ``` func ABMultiValueReplaceValue(_ multiValue: ABMutableMultiValue!, _ value: AnyObject!, _ index: CFIndex) -> Bool ``` |
| To | ``` func ABMultiValueReplaceValue(_ multiValue: ABMutableMultiValueRef!, _ value: AnyObject!, _ index: CFIndex) -> Bool ``` |

Modified [ABMultiValueSetPrimaryIdentifier(_: ABMutableMultiValueRef!, _: CFString!) -> Bool](https://developer.apple.com/documentation/addressbook/1430141-abmultivaluesetprimaryidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func ABMultiValueSetPrimaryIdentifier(_ multiValue: ABMutableMultiValue!, _ identifier: CFString!) -> Bool ``` |
| To | ``` func ABMultiValueSetPrimaryIdentifier(_ multiValue: ABMutableMultiValueRef!, _ identifier: CFString!) -> Bool ``` |

Modified [ABPersonCopyImageData(_: ABPersonRef!) -> Unmanaged<CFData>!](https://developer.apple.com/documentation/addressbook/1430180-abpersoncopyimagedata)

|  | Declaration |
| --- | --- |
| From | ``` func ABPersonCopyImageData(_ person: ABPerson!) -> Unmanaged<CFData>! ``` |
| To | ``` func ABPersonCopyImageData(_ person: ABPersonRef!) -> Unmanaged<CFData>! ``` |

Modified [ABPersonCopyParentGroups(_: ABPersonRef!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/addressbook/1430094-abpersoncopyparentgroups)

|  | Declaration |
| --- | --- |
| From | ``` func ABPersonCopyParentGroups(_ person: ABPerson!) -> Unmanaged<CFArray>! ``` |
| To | ``` func ABPersonCopyParentGroups(_ person: ABPersonRef!) -> Unmanaged<CFArray>! ``` |

Modified [ABPersonCopyVCardRepresentation(_: ABPersonRef!) -> Unmanaged<CFData>!](https://developer.apple.com/documentation/addressbook/1430099-abpersoncopyvcardrepresentation)

|  | Declaration |
| --- | --- |
| From | ``` func ABPersonCopyVCardRepresentation(_ person: ABPerson!) -> Unmanaged<CFData>! ``` |
| To | ``` func ABPersonCopyVCardRepresentation(_ person: ABPersonRef!) -> Unmanaged<CFData>! ``` |

Modified [ABPersonCreate() -> Unmanaged<ABPersonRef>!](https://developer.apple.com/documentation/addressbook/1430127-abpersoncreate)

|  | Declaration |
| --- | --- |
| From | ``` func ABPersonCreate() -> Unmanaged<ABPerson>! ``` |
| To | ``` func ABPersonCreate() -> Unmanaged<ABPersonRef>! ``` |

Modified [ABPersonCreateSearchElement(_: CFString!, _: CFString!, _: CFString!, _: AnyObject!, _: ABSearchComparison) -> Unmanaged<ABSearchElementRef>!](https://developer.apple.com/documentation/addressbook/1430105-abpersoncreatesearchelement)

|  | Declaration |
| --- | --- |
| From | ``` func ABPersonCreateSearchElement(_ property: CFString!, _ label: CFString!, _ key: CFString!, _ value: AnyObject!, _ comparison: ABSearchComparison) -> Unmanaged<ABSearchElement>! ``` |
| To | ``` func ABPersonCreateSearchElement(_ property: CFString!, _ label: CFString!, _ key: CFString!, _ value: AnyObject!, _ comparison: ABSearchComparison) -> Unmanaged<ABSearchElementRef>! ``` |

Modified [ABPersonCreateWithVCardRepresentation(_: CFData!) -> Unmanaged<ABPersonRef>!](https://developer.apple.com/documentation/addressbook/1430143-abpersoncreatewithvcardrepresent)

|  | Declaration |
| --- | --- |
| From | ``` func ABPersonCreateWithVCardRepresentation(_ vCard: CFData!) -> Unmanaged<ABPerson>! ``` |
| To | ``` func ABPersonCreateWithVCardRepresentation(_ vCard: CFData!) -> Unmanaged<ABPersonRef>! ``` |

Modified [ABPersonSetImageData(_: ABPersonRef!, _: CFData!) -> Bool](https://developer.apple.com/documentation/addressbook/1430107-abpersonsetimagedata)

|  | Declaration |
| --- | --- |
| From | ``` func ABPersonSetImageData(_ person: ABPerson!, _ imageData: CFData!) -> Bool ``` |
| To | ``` func ABPersonSetImageData(_ person: ABPersonRef!, _ imageData: CFData!) -> Bool ``` |

Modified [ABRemoveProperties(_: ABAddressBookRef!, _: CFString!, _: CFArray!) -> CFIndex](https://developer.apple.com/documentation/addressbook/1430157-abremoveproperties)

|  | Declaration |
| --- | --- |
| From | ``` func ABRemoveProperties(_ addressBook: ABAddressBook!, _ recordType: CFString!, _ properties: CFArray!) -> CFIndex ``` |
| To | ``` func ABRemoveProperties(_ addressBook: ABAddressBookRef!, _ recordType: CFString!, _ properties: CFArray!) -> CFIndex ``` |

Modified [ABRemoveRecord(_: ABAddressBookRef!, _: ABRecordRef) -> Bool](https://developer.apple.com/documentation/addressbook/1430196-abremoverecord)

|  | Declaration |
| --- | --- |
| From | ``` func ABRemoveRecord(_ addressBook: ABAddressBook!, _ record: ABRecordRef) -> Bool ``` |
| To | ``` func ABRemoveRecord(_ addressBook: ABAddressBookRef!, _ record: ABRecordRef) -> Bool ``` |

Modified [ABSave(_: ABAddressBookRef!) -> Bool](https://developer.apple.com/documentation/addressbook/1430123-absave)

|  | Declaration |
| --- | --- |
| From | ``` func ABSave(_ addressBook: ABAddressBook!) -> Bool ``` |
| To | ``` func ABSave(_ addressBook: ABAddressBookRef!) -> Bool ``` |

Modified [ABSearchElementCreateWithConjunction(_: ABSearchConjunction, _: CFArray!) -> Unmanaged<ABSearchElementRef>!](https://developer.apple.com/documentation/addressbook/1430082-absearchelementcreatewithconjunc)

|  | Declaration |
| --- | --- |
| From | ``` func ABSearchElementCreateWithConjunction(_ conjunction: ABSearchConjunction, _ childrenSearchElement: CFArray!) -> Unmanaged<ABSearchElement>! ``` |
| To | ``` func ABSearchElementCreateWithConjunction(_ conjunction: ABSearchConjunction, _ childrenSearchElement: CFArray!) -> Unmanaged<ABSearchElementRef>! ``` |

Modified [ABSearchElementMatchesRecord(_: ABSearchElementRef!, _: ABRecordRef) -> Bool](https://developer.apple.com/documentation/addressbook/1430184-absearchelementmatchesrecord)

|  | Declaration |
| --- | --- |
| From | ``` func ABSearchElementMatchesRecord(_ searchElement: ABSearchElement!, _ record: ABRecordRef) -> Bool ``` |
| To | ``` func ABSearchElementMatchesRecord(_ searchElement: ABSearchElementRef!, _ record: ABRecordRef) -> Bool ``` |

Modified [ABSetMe(_: ABAddressBookRef!, _: ABPersonRef!)](https://developer.apple.com/documentation/addressbook/1430150-absetme)

|  | Declaration |
| --- | --- |
| From | ``` func ABSetMe(_ addressBook: ABAddressBook!, _ moi: ABPerson!) ``` |
| To | ``` func ABSetMe(_ addressBook: ABAddressBookRef!, _ moi: ABPersonRef!) ``` |

Modified [ABTypeOfProperty(_: ABAddressBookRef!, _: CFString!, _: CFString!) -> ABPropertyType](https://developer.apple.com/documentation/addressbook/1430160-abtypeofproperty)

|  | Declaration |
| --- | --- |
| From | ``` func ABTypeOfProperty(_ addressBook: ABAddressBook!, _ recordType: CFString!, _ property: CFString!) -> ABPropertyType ``` |
| To | ``` func ABTypeOfProperty(_ addressBook: ABAddressBookRef!, _ recordType: CFString!, _ property: CFString!) -> ABPropertyType ``` |

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
