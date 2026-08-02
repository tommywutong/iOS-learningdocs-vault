---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/AddressBook.html
archived_at: '2026-07-18T02:55:06.474130Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# AddressBook Changes for Swift

### AddressBook

Modified [ABAuthorizationStatus [enum]](https://developer.apple.com/documentation/addressbook/abauthorizationstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum ABAuthorizationStatus : CFIndex {     case NotDetermined     case Restricted     case Denied     case Authorized } ``` |
| To | ``` enum ABAuthorizationStatus : CFIndex {     case notDetermined     case restricted     case denied     case authorized } ``` |

Modified [ABAuthorizationStatus.authorized](https://developer.apple.com/documentation/addressbook/abauthorizationstatus/kabauthorizationstatusauthorized)

|  | Declaration |
| --- | --- |
| From | ``` case Authorized ``` |
| To | ``` case authorized ``` |

Modified [ABAuthorizationStatus.denied](https://developer.apple.com/documentation/addressbook/abauthorizationstatus/denied)

|  | Declaration |
| --- | --- |
| From | ``` case Denied ``` |
| To | ``` case denied ``` |

Modified [ABAuthorizationStatus.notDetermined](https://developer.apple.com/documentation/addressbook/abauthorizationstatus/kabauthorizationstatusnotdetermined)

|  | Declaration |
| --- | --- |
| From | ``` case NotDetermined ``` |
| To | ``` case notDetermined ``` |

Modified [ABAuthorizationStatus.restricted](https://developer.apple.com/documentation/addressbook/abauthorizationstatus/kabauthorizationstatusrestricted)

|  | Declaration |
| --- | --- |
| From | ``` case Restricted ``` |
| To | ``` case restricted ``` |

Modified [ABAddressBookAddRecord(_: ABAddressBook!, _: ABRecord!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/addressbook/1621987-abaddressbookaddrecord)

|  | Declaration |
| --- | --- |
| From | ``` func ABAddressBookAddRecord(_ addressBook: ABAddressBook!, _ record: ABRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ABAddressBookAddRecord(_ addressBook: ABAddressBook!, _ record: ABRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ABAddressBookCreateWithOptions(_: CFDictionary!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ABAddressBook>!](https://developer.apple.com/documentation/addressbook/1621991-abaddressbookcreatewithoptions)

|  | Declaration |
| --- | --- |
| From | ``` func ABAddressBookCreateWithOptions(_ options: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ABAddressBook>! ``` |
| To | ``` func ABAddressBookCreateWithOptions(_ options: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ABAddressBook>! ``` |

Modified [ABAddressBookRegisterExternalChangeCallback(_: ABAddressBook!, _: AddressBook.ABExternalChangeCallback!, _: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/addressbook/1621989-abaddressbookregisterexternalcha)

|  | Declaration |
| --- | --- |
| From | ``` func ABAddressBookRegisterExternalChangeCallback(_ addressBook: ABAddressBook!, _ callback: ABExternalChangeCallback!, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func ABAddressBookRegisterExternalChangeCallback(_ addressBook: ABAddressBook!, _ callback: AddressBook.ABExternalChangeCallback!, _ context: UnsafeMutableRawPointer!) ``` |

Modified [ABAddressBookRemoveRecord(_: ABAddressBook!, _: ABRecord!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/addressbook/1622008-abaddressbookremoverecord)

|  | Declaration |
| --- | --- |
| From | ``` func ABAddressBookRemoveRecord(_ addressBook: ABAddressBook!, _ record: ABRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ABAddressBookRemoveRecord(_ addressBook: ABAddressBook!, _ record: ABRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ABAddressBookRequestAccessCompletionHandler](https://developer.apple.com/documentation/addressbook/abaddressbookrequestaccesscompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias ABAddressBookRequestAccessCompletionHandler = (Bool, CFError!) -> Void ``` |
| To | ``` typealias ABAddressBookRequestAccessCompletionHandler = (Bool, CFError?) -> Swift.Void ``` |

Modified [ABAddressBookRequestAccessWithCompletion(_: ABAddressBook!, _: AddressBook.ABAddressBookRequestAccessCompletionHandler!)](https://developer.apple.com/documentation/addressbook/1622001-abaddressbookrequestaccesswithco)

|  | Declaration |
| --- | --- |
| From | ``` func ABAddressBookRequestAccessWithCompletion(_ addressBook: ABAddressBook!, _ completion: ABAddressBookRequestAccessCompletionHandler!) ``` |
| To | ``` func ABAddressBookRequestAccessWithCompletion(_ addressBook: ABAddressBook!, _ completion: AddressBook.ABAddressBookRequestAccessCompletionHandler!) ``` |

Modified [ABAddressBookSave(_: ABAddressBook!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/addressbook/1621996-abaddressbooksave)

|  | Declaration |
| --- | --- |
| From | ``` func ABAddressBookSave(_ addressBook: ABAddressBook!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ABAddressBookSave(_ addressBook: ABAddressBook!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ABAddressBookUnregisterExternalChangeCallback(_: ABAddressBook!, _: AddressBook.ABExternalChangeCallback!, _: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/addressbook/1622004-abaddressbookunregisterexternalc)

|  | Declaration |
| --- | --- |
| From | ``` func ABAddressBookUnregisterExternalChangeCallback(_ addressBook: ABAddressBook!, _ callback: ABExternalChangeCallback!, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func ABAddressBookUnregisterExternalChangeCallback(_ addressBook: ABAddressBook!, _ callback: AddressBook.ABExternalChangeCallback!, _ context: UnsafeMutableRawPointer!) ``` |

Modified [ABExternalChangeCallback](https://developer.apple.com/documentation/addressbook/abexternalchangecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias ABExternalChangeCallback = (ABAddressBook!, CFDictionary!, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias ABExternalChangeCallback = (ABAddressBook?, CFDictionary?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [ABGroupAddMember(_: ABRecord!, _: ABRecord!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/addressbook/1430147-abgroupaddmember)

|  | Declaration |
| --- | --- |
| From | ``` func ABGroupAddMember(_ group: ABRecord!, _ person: ABRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ABGroupAddMember(_ group: ABRecord!, _ person: ABRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ABGroupRemoveMember(_: ABRecord!, _: ABRecord!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/addressbook/1430206-abgroupremovemember)

|  | Declaration |
| --- | --- |
| From | ``` func ABGroupRemoveMember(_ group: ABRecord!, _ member: ABRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ABGroupRemoveMember(_ group: ABRecord!, _ member: ABRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ABMultiValueAddValueAndLabel(_: ABMutableMultiValue!, _: CFTypeRef!, _: CFString!, _: UnsafeMutablePointer<ABMultiValueIdentifier>!) -> Bool](https://developer.apple.com/documentation/addressbook/1624556-abmultivalueaddvalueandlabel)

|  | Declaration |
| --- | --- |
| From | ``` func ABMultiValueAddValueAndLabel(_ multiValue: ABMutableMultiValue!, _ value: AnyObject!, _ label: CFString!, _ outIdentifier: UnsafeMutablePointer<ABMultiValueIdentifier>) -> Bool ``` |
| To | ``` func ABMultiValueAddValueAndLabel(_ multiValue: ABMutableMultiValue!, _ value: CFTypeRef!, _ label: CFString!, _ outIdentifier: UnsafeMutablePointer<ABMultiValueIdentifier>!) -> Bool ``` |

Modified [ABMultiValueCopyValueAtIndex(_: ABMultiValue!, _: CFIndex) -> Unmanaged<CFTypeRef>!](https://developer.apple.com/documentation/addressbook/1430101-abmultivaluecopyvalueatindex)

|  | Declaration |
| --- | --- |
| From | ``` func ABMultiValueCopyValueAtIndex(_ multiValue: ABMultiValue!, _ index: CFIndex) -> Unmanaged<AnyObject>! ``` |
| To | ``` func ABMultiValueCopyValueAtIndex(_ multiValue: ABMultiValue!, _ index: CFIndex) -> Unmanaged<CFTypeRef>! ``` |

Modified [ABMultiValueGetFirstIndexOfValue(_: ABMultiValue!, _: CFTypeRef!) -> CFIndex](https://developer.apple.com/documentation/addressbook/1624557-abmultivaluegetfirstindexofvalue)

|  | Declaration |
| --- | --- |
| From | ``` func ABMultiValueGetFirstIndexOfValue(_ multiValue: ABMultiValue!, _ value: AnyObject!) -> CFIndex ``` |
| To | ``` func ABMultiValueGetFirstIndexOfValue(_ multiValue: ABMultiValue!, _ value: CFTypeRef!) -> CFIndex ``` |

Modified [ABMultiValueInsertValueAndLabelAtIndex(_: ABMutableMultiValue!, _: CFTypeRef!, _: CFString!, _: CFIndex, _: UnsafeMutablePointer<ABMultiValueIdentifier>!) -> Bool](https://developer.apple.com/documentation/addressbook/1624555-abmultivalueinsertvalueandlabela)

|  | Declaration |
| --- | --- |
| From | ``` func ABMultiValueInsertValueAndLabelAtIndex(_ multiValue: ABMutableMultiValue!, _ value: AnyObject!, _ label: CFString!, _ index: CFIndex, _ outIdentifier: UnsafeMutablePointer<ABMultiValueIdentifier>) -> Bool ``` |
| To | ``` func ABMultiValueInsertValueAndLabelAtIndex(_ multiValue: ABMutableMultiValue!, _ value: CFTypeRef!, _ label: CFString!, _ index: CFIndex, _ outIdentifier: UnsafeMutablePointer<ABMultiValueIdentifier>!) -> Bool ``` |

Modified [ABMultiValueReplaceValueAtIndex(_: ABMutableMultiValue!, _: CFTypeRef!, _: CFIndex) -> Bool](https://developer.apple.com/documentation/addressbook/1624562-abmultivaluereplacevalueatindex)

|  | Declaration |
| --- | --- |
| From | ``` func ABMultiValueReplaceValueAtIndex(_ multiValue: ABMutableMultiValue!, _ value: AnyObject!, _ index: CFIndex) -> Bool ``` |
| To | ``` func ABMultiValueReplaceValueAtIndex(_ multiValue: ABMutableMultiValue!, _ value: CFTypeRef!, _ index: CFIndex) -> Bool ``` |

Modified [ABMutableMultiValue](https://developer.apple.com/documentation/addressbook/abmutablemultivalue-klq)

|  | Declaration |
| --- | --- |
| From | ``` typealias ABMutableMultiValueRef = ABMutableMultiValue ``` |
| To | ``` typealias ABMutableMultiValue = CFTypeRef ``` |

Modified [ABPersonRemoveImageData(_: ABRecord!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/addressbook/1619739-abpersonremoveimagedata)

|  | Declaration |
| --- | --- |
| From | ``` func ABPersonRemoveImageData(_ person: ABRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ABPersonRemoveImageData(_ person: ABRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ABPersonSetImageData(_: ABRecord!, _: CFData!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/addressbook/1430107-abpersonsetimagedata)

|  | Declaration |
| --- | --- |
| From | ``` func ABPersonSetImageData(_ person: ABRecord!, _ imageData: CFData!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ABPersonSetImageData(_ person: ABRecord!, _ imageData: CFData!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ABRecordCopyValue(_: ABRecord!, _: ABPropertyID) -> Unmanaged<CFTypeRef>!](https://developer.apple.com/documentation/addressbook/1430135-abrecordcopyvalue)

|  | Declaration |
| --- | --- |
| From | ``` func ABRecordCopyValue(_ record: ABRecord!, _ property: ABPropertyID) -> Unmanaged<AnyObject>! ``` |
| To | ``` func ABRecordCopyValue(_ record: ABRecord!, _ property: ABPropertyID) -> Unmanaged<CFTypeRef>! ``` |

Modified [ABRecordRemoveValue(_: ABRecord!, _: ABPropertyID, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/addressbook/1430090-abrecordremovevalue)

|  | Declaration |
| --- | --- |
| From | ``` func ABRecordRemoveValue(_ record: ABRecord!, _ property: ABPropertyID, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ABRecordRemoveValue(_ record: ABRecord!, _ property: ABPropertyID, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ABRecordSetValue(_: ABRecord!, _: ABPropertyID, _: CFTypeRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/addressbook/1430168-abrecordsetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func ABRecordSetValue(_ record: ABRecord!, _ property: ABPropertyID, _ value: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ABRecordSetValue(_ record: ABRecord!, _ property: ABPropertyID, _ value: CFTypeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

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
