---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/AddressBook.html
archived_at: '2026-07-18T02:53:16.496227Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# AddressBook Changes for Swift

### AddressBook

Removed ABPeoplePickerSelectionBehavior.valueAdded ABPeoplePickerSelectionBehavior.init(rawValue: UInt32)Added ABPeoplePickerSelectionBehavior.rawValueModified [ABAddressBook](https://developer.apple.com/documentation/addressbook/abaddressbook)

|  | Declaration |
| --- | --- |
| From | ``` class ABAddressBook : NSObject {     class func sharedAddressBook() -> ABAddressBook!     init!() -> ABAddressBook     class func addressBook() -> ABAddressBook!     func recordsMatchingSearchElement(_ search: ABSearchElement!) -> [AnyObject]!     func save() -> Bool     func saveAndReturnError(_ error: NSErrorPointer) -> Bool     func hasUnsavedChanges() -> Bool     func me() -> ABPerson!     func setMe(_ moi: ABPerson!)     func recordForUniqueId(_ uniqueId: String!) -> ABRecord!     func addRecord(_ record: ABRecord!, error error: NSErrorPointer) -> Bool     func addRecord(_ record: ABRecord!) -> Bool     func removeRecord(_ record: ABRecord!, error error: NSErrorPointer) -> Bool     func removeRecord(_ record: ABRecord!) -> Bool     func people() -> [AnyObject]!     func groups() -> [AnyObject]!     func recordClassFromUniqueId(_ uniqueId: String!) -> String!     func formattedAddressFromDictionary(_ address: [NSObject : AnyObject]!) -> NSAttributedString!     func defaultCountryCode() -> String!     func defaultNameOrdering() -> Int } ``` |
| To | ``` class ABAddressBook : NSObject {     class func sharedAddressBook() -> ABAddressBook!      init!()     class func addressBook() -> ABAddressBook!     func recordsMatchingSearchElement(_ search: ABSearchElement!) -> [AnyObject]!     func save() -> Bool     func saveAndReturnError() throws     func hasUnsavedChanges() -> Bool     func me() -> ABPerson!     func setMe(_ moi: ABPerson!)     func recordForUniqueId(_ uniqueId: String!) -> ABRecord!     func addRecord(_ record: ABRecord!, error error: ()) throws     func addRecord(_ record: ABRecord!) -> Bool     func removeRecord(_ record: ABRecord!, error error: ()) throws     func removeRecord(_ record: ABRecord!) -> Bool     func people() -> [AnyObject]!     func groups() -> [AnyObject]!     func recordClassFromUniqueId(_ uniqueId: String!) -> String!     func formattedAddressFromDictionary(_ address: [NSObject : AnyObject]!) -> NSAttributedString!     func defaultCountryCode() -> String!     func defaultNameOrdering() -> Int } ``` |

Modified [ABAddressBook.addRecord(_: ABRecord!, error: ()) throws](https://developer.apple.com/documentation/addressbook/abaddressbook/1458709-add)

|  | Declaration |
| --- | --- |
| From | ``` func addRecord(_ record: ABRecord!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func addRecord(_ record: ABRecord!, error error: ()) throws ``` |

Modified [ABAddressBook.removeRecord(_: ABRecord!, error: ()) throws](https://developer.apple.com/documentation/addressbook/abaddressbook/1458388-remove)

|  | Declaration |
| --- | --- |
| From | ``` func removeRecord(_ record: ABRecord!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func removeRecord(_ record: ABRecord!, error error: ()) throws ``` |

Modified [ABAddressBook.saveAndReturnError() throws](https://developer.apple.com/documentation/addressbook/abaddressbook/1458623-saveandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` func saveAndReturnError(_ error: NSErrorPointer) -> Bool ``` |
| To | ``` func saveAndReturnError() throws ``` |

Modified [ABPeoplePickerSelectionBehavior [struct]](https://developer.apple.com/documentation/addressbook/abpeoplepickerselectionbehavior)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct ABPeoplePickerSelectionBehavior {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct ABPeoplePickerSelectionBehavior : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [ABRecord](https://developer.apple.com/documentation/addressbook/abrecord)

|  | Declaration |
| --- | --- |
| From | ``` class ABRecord : NSObject {     init!()     init!(addressBook addressBook: ABAddressBook!)     func valueForProperty(_ property: String!) -> AnyObject!     func setValue(_ value: AnyObject!, forProperty property: String!, error error: NSErrorPointer) -> Bool     func setValue(_ value: AnyObject!, forProperty property: String!) -> Bool     func removeValueForProperty(_ property: String!) -> Bool     func isReadOnly() -> Bool } extension ABRecord {     var uniqueId: String! { get }     var displayName: String! { get } } ``` |
| To | ``` class ABRecord : NSObject {     init!()     init!(addressBook addressBook: ABAddressBook!)     func valueForProperty(_ property: String!) -> AnyObject!     func setValue(_ value: AnyObject!, forProperty property: String!, error error: ()) throws     func setValue(_ value: AnyObject!, forProperty property: String!) -> Bool     func removeValueForProperty(_ property: String!) -> Bool     func isReadOnly() -> Bool } extension ABRecord {     var uniqueId: String! { get }     var displayName: String! { get } } ``` |

Modified [ABRecord.setValue(_: AnyObject!, forProperty: String!, error: ()) throws](https://developer.apple.com/documentation/addressbook/abrecord/1400521-setvalue)

|  | Declaration |
| --- | --- |
| From | ``` func setValue(_ value: AnyObject!, forProperty property: String!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func setValue(_ value: AnyObject!, forProperty property: String!, error error: ()) throws ``` |

Modified [ABSearchElement](https://developer.apple.com/documentation/addressbook/absearchelement)

|  | Declaration |
| --- | --- |
| From | ``` class ABSearchElement : NSObject {     init!(forConjunction conjuction: ABSearchConjunction, children children: [AnyObject]!) -> ABSearchElement     class func searchElementForConjunction(_ conjuction: ABSearchConjunction, children children: [AnyObject]!) -> ABSearchElement!     func matchesRecord(_ record: ABRecord!) -> Bool } ``` |
| To | ``` class ABSearchElement : NSObject {      init!(forConjunction conjuction: ABSearchConjunction, children children: [AnyObject]!)     class func searchElementForConjunction(_ conjuction: ABSearchConjunction, children children: [AnyObject]!) -> ABSearchElement!     func matchesRecord(_ record: ABRecord!) -> Bool } ``` |

Modified [ABSearchElement.init(forConjunction: ABSearchConjunction, children: [AnyObject]!)](https://developer.apple.com/documentation/addressbook/absearchelement/1458423-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(forConjunction conjuction: ABSearchConjunction, children children: [AnyObject]!) -> ABSearchElement ``` |
| To | ``` init!(forConjunction conjuction: ABSearchConjunction, children children: [AnyObject]!) ``` |

Modified [ABBeginLoadingImageDataForClient(_: ABPerson!, _: ABImageClientCallback!, _: UnsafeMutablePointer<Void>) -> CFIndex](https://developer.apple.com/documentation/addressbook/1430129-abbeginloadingimagedataforclient)

|  | Declaration |
| --- | --- |
| From | ``` func ABBeginLoadingImageDataForClient(_ person: ABPerson!, _ callback: ABImageClientCallback, _ refcon: UnsafeMutablePointer<Void>) -> CFIndex ``` |
| To | ``` func ABBeginLoadingImageDataForClient(_ person: ABPerson!, _ callback: ABImageClientCallback!, _ refcon: UnsafeMutablePointer<Void>) -> CFIndex ``` |

Modified [ABImageClientCallback](https://developer.apple.com/documentation/addressbook/abimageclientcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias ABImageClientCallback = CFunctionPointer<((CFData!, CFIndex, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias ABImageClientCallback = (CFData!, CFIndex, UnsafeMutablePointer<Void>) -> Void ``` |

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
