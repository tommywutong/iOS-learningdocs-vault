---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/AddressBook.html
archived_at: '2026-07-18T02:56:40.102508Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# AddressBook Changes for Swift

### AddressBook

Removed ABPersonImageFormat.valueAdded ABPersonImageFormat.init(rawValue: UInt32)Added ABPersonImageFormat.rawValueAdded [ABAddressBookCreate() -> Unmanaged<ABAddressBook>!](https://developer.apple.com/documentation/addressbook/1621998-abaddressbookcreate)Added [ABPersonGetCompositeNameFormat() -> ABPersonCompositeNameFormat](https://developer.apple.com/documentation/addressbook/1619750-abpersongetcompositenameformat)Modified [ABAuthorizationStatus [enum]](https://developer.apple.com/documentation/addressbook/abauthorizationstatus)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.1 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABPersonImageFormat [struct]](https://developer.apple.com/documentation/addressbook/abpersonimageformat)

|  | Declaration | Protocols | Introduction | Deprecation |
| --- | --- | --- | --- | --- |
| From | ``` struct ABPersonImageFormat {     init(_ value: UInt32)     var value: UInt32 } ``` | -- | iOS 8.1 | -- |
| To | ``` struct ABPersonImageFormat : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable | iOS 2.0 | iOS 9.0 |

Modified ABPersonImageFormat.init(_: UInt32)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ABAddressBookAddRecord(_: ABAddressBook!, _: ABRecord!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/addressbook/1621987-abaddressbookaddrecord)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookCopyArrayOfAllGroups(_: ABAddressBook!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/addressbook/1616131-abaddressbookcopyarrayofallgroup)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookCopyArrayOfAllGroupsInSource(_: ABAddressBook!, _: ABRecord!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/addressbook/1616118-abaddressbookcopyarrayofallgroup)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 4.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookCopyArrayOfAllPeople(_: ABAddressBook!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/addressbook/1619817-abaddressbookcopyarrayofallpeopl)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookCopyArrayOfAllPeopleInSource(_: ABAddressBook!, _: ABRecord!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/addressbook/1619808-abaddressbookcopyarrayofallpeopl)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 4.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookCopyArrayOfAllPeopleInSourceWithSortOrdering(_: ABAddressBook!, _: ABRecord!, _: ABPersonSortOrdering) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/addressbook/1619787-abaddressbookcopyarrayofallpeopl)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 4.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookCopyArrayOfAllSources(_: ABAddressBook!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/addressbook/1619872-abaddressbookcopyarrayofallsourc)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 4.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookCopyDefaultSource(_: ABAddressBook!) -> Unmanaged<ABRecord>!](https://developer.apple.com/documentation/addressbook/1619869-abaddressbookcopydefaultsource)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 4.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookCopyLocalizedLabel(_: CFString!) -> Unmanaged<CFString>!](https://developer.apple.com/documentation/addressbook/1621994-abaddressbookcopylocalizedlabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookCopyPeopleWithName(_: ABAddressBook!, _: CFString!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/addressbook/1619789-abaddressbookcopypeoplewithname)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookCreateWithOptions(_: CFDictionary!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ABAddressBook>!](https://developer.apple.com/documentation/addressbook/1621991-abaddressbookcreatewithoptions)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 6.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookErrorDomain](https://developer.apple.com/documentation/addressbook/abaddressbookerrordomain)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookGetAuthorizationStatus() -> ABAuthorizationStatus](https://developer.apple.com/documentation/addressbook/1622002-abaddressbookgetauthorizationsta)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 6.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookGetGroupCount(_: ABAddressBook!) -> CFIndex](https://developer.apple.com/documentation/addressbook/1616124-abaddressbookgetgroupcount)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookGetGroupWithRecordID(_: ABAddressBook!, _: ABRecordID) -> Unmanaged<ABRecord>!](https://developer.apple.com/documentation/addressbook/1616120-abaddressbookgetgroupwithrecordi)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookGetPersonCount(_: ABAddressBook!) -> CFIndex](https://developer.apple.com/documentation/addressbook/1619801-abaddressbookgetpersoncount)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookGetPersonWithRecordID(_: ABAddressBook!, _: ABRecordID) -> Unmanaged<ABRecord>!](https://developer.apple.com/documentation/addressbook/1619820-abaddressbookgetpersonwithrecord)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookGetSourceWithRecordID(_: ABAddressBook!, _: ABRecordID) -> Unmanaged<ABRecord>!](https://developer.apple.com/documentation/addressbook/1619874-abaddressbookgetsourcewithrecord)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 4.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookHasUnsavedChanges(_: ABAddressBook!) -> Bool](https://developer.apple.com/documentation/addressbook/1621990-abaddressbookhasunsavedchanges)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookRef](https://developer.apple.com/documentation/addressbook/abaddressbook-kkq)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookRegisterExternalChangeCallback(_: ABAddressBook!, _: ABExternalChangeCallback!, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/addressbook/1621989-abaddressbookregisterexternalcha)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func ABAddressBookRegisterExternalChangeCallback(_ addressBook: ABAddressBook!, _ callback: ABExternalChangeCallback, _ context: UnsafeMutablePointer<Void>) ``` | iOS 8.0 | -- |
| To | ``` func ABAddressBookRegisterExternalChangeCallback(_ addressBook: ABAddressBook!, _ callback: ABExternalChangeCallback!, _ context: UnsafeMutablePointer<Void>) ``` | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookRemoveRecord(_: ABAddressBook!, _: ABRecord!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/addressbook/1622008-abaddressbookremoverecord)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookRequestAccessCompletionHandler](https://developer.apple.com/documentation/addressbook/abaddressbookrequestaccesscompletionhandler)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookRequestAccessWithCompletion(_: ABAddressBook!, _: ABAddressBookRequestAccessCompletionHandler!)](https://developer.apple.com/documentation/addressbook/1622001-abaddressbookrequestaccesswithco)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 6.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookRevert(_: ABAddressBook!)](https://developer.apple.com/documentation/addressbook/1621997-abaddressbookrevert)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookSave(_: ABAddressBook!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/addressbook/1621996-abaddressbooksave)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABAddressBookUnregisterExternalChangeCallback(_: ABAddressBook!, _: ABExternalChangeCallback!, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/addressbook/1622004-abaddressbookunregisterexternalc)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func ABAddressBookUnregisterExternalChangeCallback(_ addressBook: ABAddressBook!, _ callback: ABExternalChangeCallback, _ context: UnsafeMutablePointer<Void>) ``` | iOS 8.0 | -- |
| To | ``` func ABAddressBookUnregisterExternalChangeCallback(_ addressBook: ABAddressBook!, _ callback: ABExternalChangeCallback!, _ context: UnsafeMutablePointer<Void>) ``` | iOS 2.0 | iOS 9.0 |

Modified [ABExternalChangeCallback](https://developer.apple.com/documentation/addressbook/abexternalchangecallback)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` typealias ABExternalChangeCallback = CFunctionPointer<((ABAddressBook!, CFDictionary!, UnsafeMutablePointer<Void>) -> Void)> ``` | iOS 8.0 | -- |
| To | ``` typealias ABExternalChangeCallback = (ABAddressBook!, CFDictionary!, UnsafeMutablePointer<Void>) -> Void ``` | iOS 2.0 | iOS 9.0 |

Modified [ABGroupAddMember(_: ABRecord!, _: ABRecord!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/addressbook/1430147-abgroupaddmember)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABGroupCopyArrayOfAllMembers(_: ABRecord!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/addressbook/1430149-abgroupcopyarrayofallmembers)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABGroupCopyArrayOfAllMembersWithSortOrdering(_: ABRecord!, _: ABPersonSortOrdering) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/addressbook/1616126-abgroupcopyarrayofallmemberswith)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABGroupCopySource(_: ABRecord!) -> Unmanaged<ABRecord>!](https://developer.apple.com/documentation/addressbook/1616129-abgroupcopysource)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 4.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABGroupCreate() -> Unmanaged<ABRecord>!](https://developer.apple.com/documentation/addressbook/1430086-abgroupcreate)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABGroupCreateInSource(_: ABRecord!) -> Unmanaged<ABRecord>!](https://developer.apple.com/documentation/addressbook/1616128-abgroupcreateinsource)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 4.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABGroupRemoveMember(_: ABRecord!, _: ABRecord!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/addressbook/1430206-abgroupremovemember)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABMultiValueAddValueAndLabel(_: ABMutableMultiValue!, _: AnyObject!, _: CFString!, _: UnsafeMutablePointer<ABMultiValueIdentifier>) -> Bool](https://developer.apple.com/documentation/addressbook/1624556-abmultivalueaddvalueandlabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABMultiValueCopyArrayOfAllValues(_: ABMultiValue!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/addressbook/1624554-abmultivaluecopyarrayofallvalues)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABMultiValueCopyLabelAtIndex(_: ABMultiValue!, _: CFIndex) -> Unmanaged<CFString>!](https://developer.apple.com/documentation/addressbook/1430131-abmultivaluecopylabelatindex)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABMultiValueCopyValueAtIndex(_: ABMultiValue!, _: CFIndex) -> Unmanaged<AnyObject>!](https://developer.apple.com/documentation/addressbook/1430101-abmultivaluecopyvalueatindex)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABMultiValueCreateMutable(_: ABPropertyType) -> Unmanaged<ABMutableMultiValue>!](https://developer.apple.com/documentation/addressbook/1430166-abmultivaluecreatemutable)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABMultiValueCreateMutableCopy(_: ABMultiValue!) -> Unmanaged<ABMutableMultiValue>!](https://developer.apple.com/documentation/addressbook/1430159-abmultivaluecreatemutablecopy)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABMultiValueGetCount(_: ABMultiValue!) -> CFIndex](https://developer.apple.com/documentation/addressbook/1624560-abmultivaluegetcount)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABMultiValueGetFirstIndexOfValue(_: ABMultiValue!, _: AnyObject!) -> CFIndex](https://developer.apple.com/documentation/addressbook/1624557-abmultivaluegetfirstindexofvalue)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABMultiValueGetIdentifierAtIndex(_: ABMultiValue!, _: CFIndex) -> ABMultiValueIdentifier](https://developer.apple.com/documentation/addressbook/1624563-abmultivaluegetidentifieratindex)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABMultiValueGetIndexForIdentifier(_: ABMultiValue!, _: ABMultiValueIdentifier) -> CFIndex](https://developer.apple.com/documentation/addressbook/1624566-abmultivaluegetindexforidentifie)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABMultiValueGetPropertyType(_: ABMultiValue!) -> ABPropertyType](https://developer.apple.com/documentation/addressbook/1624559-abmultivaluegetpropertytype)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABMultiValueIdentifier](https://developer.apple.com/documentation/addressbook/abmultivalueidentifier)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABMultiValueInsertValueAndLabelAtIndex(_: ABMutableMultiValue!, _: AnyObject!, _: CFString!, _: CFIndex, _: UnsafeMutablePointer<ABMultiValueIdentifier>) -> Bool](https://developer.apple.com/documentation/addressbook/1624555-abmultivalueinsertvalueandlabela)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABMultiValueRef](https://developer.apple.com/documentation/addressbook/abmultivalue-kj7)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABMultiValueRemoveValueAndLabelAtIndex(_: ABMutableMultiValue!, _: CFIndex) -> Bool](https://developer.apple.com/documentation/addressbook/1624561-abmultivalueremovevalueandlabela)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABMultiValueReplaceLabelAtIndex(_: ABMutableMultiValue!, _: CFString!, _: CFIndex) -> Bool](https://developer.apple.com/documentation/addressbook/1624564-abmultivaluereplacelabelatindex)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABMultiValueReplaceValueAtIndex(_: ABMutableMultiValue!, _: AnyObject!, _: CFIndex) -> Bool](https://developer.apple.com/documentation/addressbook/1624562-abmultivaluereplacevalueatindex)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABMutableMultiValueRef](https://developer.apple.com/documentation/addressbook/abmutablemultivalue-klq)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABPersonComparePeopleByName(_: ABRecord!, _: ABRecord!, _: ABPersonSortOrdering) -> CFComparisonResult](https://developer.apple.com/documentation/addressbook/1619777-abpersoncomparepeoplebyname)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABPersonCompositeNameFormat](https://developer.apple.com/documentation/addressbook/abpersoncompositenameformat)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABPersonCopyArrayOfAllLinkedPeople(_: ABRecord!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/addressbook/1619799-abpersoncopyarrayofalllinkedpeop)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 4.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABPersonCopyCompositeNameDelimiterForRecord(_: ABRecord!) -> Unmanaged<CFString>!](https://developer.apple.com/documentation/addressbook/1619765-abpersoncopycompositenamedelimit)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 7.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABPersonCopyImageData(_: ABRecord!) -> Unmanaged<CFData>!](https://developer.apple.com/documentation/addressbook/1430180-abpersoncopyimagedata)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABPersonCopyImageDataWithFormat(_: ABRecord!, _: ABPersonImageFormat) -> Unmanaged<CFData>!](https://developer.apple.com/documentation/addressbook/1619742-abpersoncopyimagedatawithformat)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 4.1 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABPersonCopyLocalizedPropertyName(_: ABPropertyID) -> Unmanaged<CFString>!](https://developer.apple.com/documentation/addressbook/1619816-abpersoncopylocalizedpropertynam)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABPersonCopySource(_: ABRecord!) -> Unmanaged<ABRecord>!](https://developer.apple.com/documentation/addressbook/1619818-abpersoncopysource)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 4.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABPersonCreate() -> Unmanaged<ABRecord>!](https://developer.apple.com/documentation/addressbook/1430127-abpersoncreate)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABPersonCreateInSource(_: ABRecord!) -> Unmanaged<ABRecord>!](https://developer.apple.com/documentation/addressbook/1619793-abpersoncreateinsource)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 4.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABPersonCreatePeopleInSourceWithVCardRepresentation(_: ABRecord!, _: CFData!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/addressbook/1619772-abpersoncreatepeopleinsourcewith)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 5.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABPersonCreateVCardRepresentationWithPeople(_: CFArray!) -> Unmanaged<CFData>!](https://developer.apple.com/documentation/addressbook/1619779-abpersoncreatevcardrepresentatio)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 5.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABPersonGetCompositeNameFormatForRecord(_: ABRecord!) -> ABPersonCompositeNameFormat](https://developer.apple.com/documentation/addressbook/1619802-abpersongetcompositenameformatfo)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 7.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABPersonGetSortOrdering() -> ABPersonSortOrdering](https://developer.apple.com/documentation/addressbook/1619717-abpersongetsortordering)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABPersonGetTypeOfProperty(_: ABPropertyID) -> ABPropertyType](https://developer.apple.com/documentation/addressbook/1619810-abpersongettypeofproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABPersonHasImageData(_: ABRecord!) -> Bool](https://developer.apple.com/documentation/addressbook/1619712-abpersonhasimagedata)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABPersonRemoveImageData(_: ABRecord!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/addressbook/1619739-abpersonremoveimagedata)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABPersonSetImageData(_: ABRecord!, _: CFData!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/addressbook/1430107-abpersonsetimagedata)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABPersonSortOrdering](https://developer.apple.com/documentation/addressbook/abpersonsortordering)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABPropertyID](https://developer.apple.com/documentation/addressbook/abpropertyid)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABPropertyType](https://developer.apple.com/documentation/addressbook/abpropertytype)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABRecordCopyCompositeName(_: ABRecord!) -> Unmanaged<CFString>!](https://developer.apple.com/documentation/addressbook/1614748-abrecordcopycompositename)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABRecordCopyValue(_: ABRecord!, _: ABPropertyID) -> Unmanaged<AnyObject>!](https://developer.apple.com/documentation/addressbook/1430135-abrecordcopyvalue)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABRecordGetRecordID(_: ABRecord!) -> ABRecordID](https://developer.apple.com/documentation/addressbook/1614734-abrecordgetrecordid)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABRecordGetRecordType(_: ABRecord!) -> ABRecordType](https://developer.apple.com/documentation/addressbook/1614736-abrecordgetrecordtype)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABRecordID](https://developer.apple.com/documentation/addressbook/abrecordid)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABRecordRef](https://developer.apple.com/documentation/addressbook/abrecordref)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABRecordRemoveValue(_: ABRecord!, _: ABPropertyID, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/addressbook/1430090-abrecordremovevalue)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABRecordSetValue(_: ABRecord!, _: ABPropertyID, _: AnyObject!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/addressbook/1430168-abrecordsetvalue)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABRecordType](https://developer.apple.com/documentation/addressbook/abrecordtype)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [ABSourceType](https://developer.apple.com/documentation/addressbook/absourcetype)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABGroupNameProperty](https://developer.apple.com/documentation/addressbook/kabgroupnameproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABHomeLabel](https://developer.apple.com/documentation/addressbook/kabhomelabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABOtherLabel](https://developer.apple.com/documentation/addressbook/kabotherlabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonAddressCityKey](https://developer.apple.com/documentation/addressbook/kabpersonaddresscitykey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonAddressCountryCodeKey](https://developer.apple.com/documentation/addressbook/kabpersonaddresscountrycodekey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonAddressCountryKey](https://developer.apple.com/documentation/addressbook/kabpersonaddresscountrykey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonAddressProperty](https://developer.apple.com/documentation/addressbook/kabpersonaddressproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonAddressStateKey](https://developer.apple.com/documentation/addressbook/kabpersonaddressstatekey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonAddressStreetKey](https://developer.apple.com/documentation/addressbook/kabpersonaddressstreetkey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonAddressZIPKey](https://developer.apple.com/documentation/addressbook/kabpersonaddresszipkey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonAlternateBirthdayCalendarIdentifierKey](https://developer.apple.com/documentation/addressbook/kabpersonalternatebirthdaycalendaridentifierkey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonAlternateBirthdayDayKey](https://developer.apple.com/documentation/addressbook/kabpersonalternatebirthdaydaykey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonAlternateBirthdayEraKey](https://developer.apple.com/documentation/addressbook/kabpersonalternatebirthdayerakey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonAlternateBirthdayIsLeapMonthKey](https://developer.apple.com/documentation/addressbook/kabpersonalternatebirthdayisleapmonthkey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonAlternateBirthdayMonthKey](https://developer.apple.com/documentation/addressbook/kabpersonalternatebirthdaymonthkey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonAlternateBirthdayProperty](https://developer.apple.com/documentation/addressbook/kabpersonalternatebirthdayproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonAlternateBirthdayYearKey](https://developer.apple.com/documentation/addressbook/kabpersonalternatebirthdayyearkey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonAnniversaryLabel](https://developer.apple.com/documentation/addressbook/kabpersonanniversarylabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonAssistantLabel](https://developer.apple.com/documentation/addressbook/kabpersonassistantlabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonBirthdayProperty](https://developer.apple.com/documentation/addressbook/kabpersonbirthdayproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonBrotherLabel](https://developer.apple.com/documentation/addressbook/kabpersonbrotherlabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonChildLabel](https://developer.apple.com/documentation/addressbook/kabpersonchildlabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonCreationDateProperty](https://developer.apple.com/documentation/addressbook/kabpersoncreationdateproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonDateProperty](https://developer.apple.com/documentation/addressbook/kabpersondateproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonDepartmentProperty](https://developer.apple.com/documentation/addressbook/kabpersondepartmentproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonEmailProperty](https://developer.apple.com/documentation/addressbook/kabpersonemailproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonFatherLabel](https://developer.apple.com/documentation/addressbook/kabpersonfatherlabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonFirstNamePhoneticProperty](https://developer.apple.com/documentation/addressbook/kabpersonfirstnamephoneticproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonFirstNameProperty](https://developer.apple.com/documentation/addressbook/kabpersonfirstnameproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonFriendLabel](https://developer.apple.com/documentation/addressbook/kabpersonfriendlabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonHomePageLabel](https://developer.apple.com/documentation/addressbook/kabpersonhomepagelabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonInstantMessageProperty](https://developer.apple.com/documentation/addressbook/kabpersoninstantmessageproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonInstantMessageServiceAIM](https://developer.apple.com/documentation/addressbook/kabpersoninstantmessageserviceaim)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonInstantMessageServiceFacebook](https://developer.apple.com/documentation/addressbook/kabpersoninstantmessageservicefacebook)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 5.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonInstantMessageServiceGaduGadu](https://developer.apple.com/documentation/addressbook/kabpersoninstantmessageservicegadugadu)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 5.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonInstantMessageServiceGoogleTalk](https://developer.apple.com/documentation/addressbook/kabpersoninstantmessageservicegoogletalk)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 5.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonInstantMessageServiceICQ](https://developer.apple.com/documentation/addressbook/kabpersoninstantmessageserviceicq)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonInstantMessageServiceJabber](https://developer.apple.com/documentation/addressbook/kabpersoninstantmessageservicejabber)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonInstantMessageServiceKey](https://developer.apple.com/documentation/addressbook/kabpersoninstantmessageservicekey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonInstantMessageServiceMSN](https://developer.apple.com/documentation/addressbook/kabpersoninstantmessageservicemsn)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonInstantMessageServiceQQ](https://developer.apple.com/documentation/addressbook/kabpersoninstantmessageserviceqq)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 5.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonInstantMessageServiceSkype](https://developer.apple.com/documentation/addressbook/kabpersoninstantmessageserviceskype)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 5.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonInstantMessageServiceYahoo](https://developer.apple.com/documentation/addressbook/kabpersoninstantmessageserviceyahoo)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonInstantMessageUsernameKey](https://developer.apple.com/documentation/addressbook/kabpersoninstantmessageusernamekey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonJobTitleProperty](https://developer.apple.com/documentation/addressbook/kabpersonjobtitleproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonKindOrganization](https://developer.apple.com/documentation/addressbook/kabpersonkindorganization)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonKindPerson](https://developer.apple.com/documentation/addressbook/kabpersonkindperson)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonKindProperty](https://developer.apple.com/documentation/addressbook/kabpersonkindproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonLastNamePhoneticProperty](https://developer.apple.com/documentation/addressbook/kabpersonlastnamephoneticproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonLastNameProperty](https://developer.apple.com/documentation/addressbook/kabpersonlastnameproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonManagerLabel](https://developer.apple.com/documentation/addressbook/kabpersonmanagerlabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonMiddleNamePhoneticProperty](https://developer.apple.com/documentation/addressbook/kabpersonmiddlenamephoneticproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonMiddleNameProperty](https://developer.apple.com/documentation/addressbook/kabpersonmiddlenameproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonModificationDateProperty](https://developer.apple.com/documentation/addressbook/kabpersonmodificationdateproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonMotherLabel](https://developer.apple.com/documentation/addressbook/kabpersonmotherlabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonNicknameProperty](https://developer.apple.com/documentation/addressbook/kabpersonnicknameproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonNoteProperty](https://developer.apple.com/documentation/addressbook/kabpersonnoteproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonOrganizationProperty](https://developer.apple.com/documentation/addressbook/kabpersonorganizationproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonParentLabel](https://developer.apple.com/documentation/addressbook/kabpersonparentlabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonPartnerLabel](https://developer.apple.com/documentation/addressbook/kabpersonpartnerlabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonPhoneHomeFAXLabel](https://developer.apple.com/documentation/addressbook/kabpersonphonehomefaxlabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonPhoneIPhoneLabel](https://developer.apple.com/documentation/addressbook/kabpersonphoneiphonelabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 3.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonPhoneMainLabel](https://developer.apple.com/documentation/addressbook/kabpersonphonemainlabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonPhoneMobileLabel](https://developer.apple.com/documentation/addressbook/kabpersonphonemobilelabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonPhoneOtherFAXLabel](https://developer.apple.com/documentation/addressbook/kabpersonphoneotherfaxlabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 5.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonPhonePagerLabel](https://developer.apple.com/documentation/addressbook/kabpersonphonepagerlabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonPhoneProperty](https://developer.apple.com/documentation/addressbook/kabpersonphoneproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonPhoneWorkFAXLabel](https://developer.apple.com/documentation/addressbook/kabpersonphoneworkfaxlabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonPrefixProperty](https://developer.apple.com/documentation/addressbook/kabpersonprefixproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonRelatedNamesProperty](https://developer.apple.com/documentation/addressbook/kabpersonrelatednamesproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonSisterLabel](https://developer.apple.com/documentation/addressbook/kabpersonsisterlabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonSocialProfileProperty](https://developer.apple.com/documentation/addressbook/kabpersonsocialprofileproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 5.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonSocialProfileServiceFacebook](https://developer.apple.com/documentation/addressbook/kabpersonsocialprofileservicefacebook)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 5.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonSocialProfileServiceFlickr](https://developer.apple.com/documentation/addressbook/kabpersonsocialprofileserviceflickr)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 5.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonSocialProfileServiceGameCenter](https://developer.apple.com/documentation/addressbook/kabpersonsocialprofileservicegamecenter)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 5.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonSocialProfileServiceKey](https://developer.apple.com/documentation/addressbook/kabpersonsocialprofileservicekey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 5.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonSocialProfileServiceLinkedIn](https://developer.apple.com/documentation/addressbook/kabpersonsocialprofileservicelinkedin)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 5.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonSocialProfileServiceMyspace](https://developer.apple.com/documentation/addressbook/kabpersonsocialprofileservicemyspace)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 5.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonSocialProfileServiceSinaWeibo](https://developer.apple.com/documentation/addressbook/kabpersonsocialprofileservicesinaweibo)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 6.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonSocialProfileServiceTwitter](https://developer.apple.com/documentation/addressbook/kabpersonsocialprofileservicetwitter)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 5.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonSocialProfileURLKey](https://developer.apple.com/documentation/addressbook/kabpersonsocialprofileurlkey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 5.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonSocialProfileUserIdentifierKey](https://developer.apple.com/documentation/addressbook/kabpersonsocialprofileuseridentifierkey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 5.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonSocialProfileUsernameKey](https://developer.apple.com/documentation/addressbook/kabpersonsocialprofileusernamekey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 5.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonSpouseLabel](https://developer.apple.com/documentation/addressbook/kabpersonspouselabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonSuffixProperty](https://developer.apple.com/documentation/addressbook/kabpersonsuffixproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABPersonURLProperty](https://developer.apple.com/documentation/addressbook/kabpersonurlproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABSourceNameProperty](https://developer.apple.com/documentation/addressbook/kabsourcenameproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 4.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABSourceTypeProperty](https://developer.apple.com/documentation/addressbook/kabsourcetypeproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 4.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [kABWorkLabel](https://developer.apple.com/documentation/addressbook/kabworklabel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

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
