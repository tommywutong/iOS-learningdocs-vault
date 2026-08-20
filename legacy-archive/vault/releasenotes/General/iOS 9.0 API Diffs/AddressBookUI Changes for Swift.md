---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/AddressBookUI.html
archived_at: '2026-07-18T02:56:40.370410Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# AddressBookUI Changes for Swift

### AddressBookUI

Modified [ABNewPersonViewController](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontroller)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` class ABNewPersonViewController : UIViewController {     unowned(unsafe) var newPersonViewDelegate: ABNewPersonViewControllerDelegate!     var addressBook: ABAddressBook!     var displayedPerson: ABRecord!     var parentGroup: ABRecord! } ``` | -- |
| To | ``` class ABNewPersonViewController : UIViewController {     unowned(unsafe) var newPersonViewDelegate: ABNewPersonViewControllerDelegate?     var addressBook: ABAddressBook?     var displayedPerson: ABRecord?     var parentGroup: ABRecord? } ``` | iOS 9.0 |

Modified [ABNewPersonViewController.addressBook](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontroller/1624264-addressbook)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var addressBook: ABAddressBook! ``` | -- |
| To | ``` var addressBook: ABAddressBook? ``` | iOS 9.0 |

Modified [ABNewPersonViewController.displayedPerson](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontroller/1624263-displayedperson)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var displayedPerson: ABRecord! ``` | -- |
| To | ``` var displayedPerson: ABRecord? ``` | iOS 9.0 |

Modified [ABNewPersonViewController.newPersonViewDelegate](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontroller/1624265-newpersonviewdelegate)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` unowned(unsafe) var newPersonViewDelegate: ABNewPersonViewControllerDelegate! ``` | -- |
| To | ``` unowned(unsafe) var newPersonViewDelegate: ABNewPersonViewControllerDelegate? ``` | iOS 9.0 |

Modified [ABNewPersonViewController.parentGroup](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontroller/1624260-parentgroup)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var parentGroup: ABRecord! ``` | -- |
| To | ``` var parentGroup: ABRecord? ``` | iOS 9.0 |

Modified [ABNewPersonViewControllerDelegate](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol ABNewPersonViewControllerDelegate : NSObjectProtocol {     func newPersonViewController(_ newPersonView: ABNewPersonViewController!, didCompleteWithNewPerson person: ABRecord!) } ``` |
| To | ``` protocol ABNewPersonViewControllerDelegate : NSObjectProtocol {     func newPersonViewController(_ newPersonView: ABNewPersonViewController, didCompleteWithNewPerson person: ABRecord?) } ``` |

Modified [ABNewPersonViewControllerDelegate.newPersonViewController(_: ABNewPersonViewController, didCompleteWithNewPerson: ABRecord?)](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontrollerdelegate/1624261-newpersonviewcontroller)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func newPersonViewController(_ newPersonView: ABNewPersonViewController!, didCompleteWithNewPerson person: ABRecord!) ``` | iOS 8.0 |
| To | ``` func newPersonViewController(_ newPersonView: ABNewPersonViewController, didCompleteWithNewPerson person: ABRecord?) ``` | iOS 2.0 |

Modified [ABPeoplePickerNavigationController](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` class ABPeoplePickerNavigationController : UINavigationController {     unowned(unsafe) var peoplePickerDelegate: ABPeoplePickerNavigationControllerDelegate!     var displayedProperties: [AnyObject]!     var addressBook: ABAddressBook!     @NSCopying var predicateForEnablingPerson: NSPredicate!     @NSCopying var predicateForSelectionOfPerson: NSPredicate!     @NSCopying var predicateForSelectionOfProperty: NSPredicate! } ``` | -- |
| To | ``` class ABPeoplePickerNavigationController : UINavigationController {     unowned(unsafe) var peoplePickerDelegate: ABPeoplePickerNavigationControllerDelegate?     var displayedProperties: [NSNumber]?     var addressBook: ABAddressBook?     @NSCopying var predicateForEnablingPerson: NSPredicate?     @NSCopying var predicateForSelectionOfPerson: NSPredicate?     @NSCopying var predicateForSelectionOfProperty: NSPredicate? } ``` | iOS 9.0 |

Modified [ABPeoplePickerNavigationController.addressBook](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/1614407-addressbook)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var addressBook: ABAddressBook! ``` | -- |
| To | ``` var addressBook: ABAddressBook? ``` | iOS 9.0 |

Modified [ABPeoplePickerNavigationController.displayedProperties](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/1614398-displayedproperties)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var displayedProperties: [AnyObject]! ``` | -- |
| To | ``` var displayedProperties: [NSNumber]? ``` | iOS 9.0 |

Modified [ABPeoplePickerNavigationController.peoplePickerDelegate](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/1614428-peoplepickerdelegate)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` unowned(unsafe) var peoplePickerDelegate: ABPeoplePickerNavigationControllerDelegate! ``` | -- |
| To | ``` unowned(unsafe) var peoplePickerDelegate: ABPeoplePickerNavigationControllerDelegate? ``` | iOS 9.0 |

Modified [ABPeoplePickerNavigationController.predicateForEnablingPerson](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/1614417-predicateforenablingperson)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @NSCopying var predicateForEnablingPerson: NSPredicate! ``` | -- |
| To | ``` @NSCopying var predicateForEnablingPerson: NSPredicate? ``` | iOS 9.0 |

Modified [ABPeoplePickerNavigationController.predicateForSelectionOfPerson](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/1614400-predicateforselectionofperson)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @NSCopying var predicateForSelectionOfPerson: NSPredicate! ``` | -- |
| To | ``` @NSCopying var predicateForSelectionOfPerson: NSPredicate? ``` | iOS 9.0 |

Modified [ABPeoplePickerNavigationController.predicateForSelectionOfProperty](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/1614422-predicateforselectionofproperty)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @NSCopying var predicateForSelectionOfProperty: NSPredicate! ``` | -- |
| To | ``` @NSCopying var predicateForSelectionOfProperty: NSPredicate? ``` | iOS 9.0 |

Modified [ABPeoplePickerNavigationControllerDelegate](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol ABPeoplePickerNavigationControllerDelegate : NSObjectProtocol {     optional func peoplePickerNavigationController(_ peoplePicker: ABPeoplePickerNavigationController!, didSelectPerson person: ABRecord!)     optional func peoplePickerNavigationController(_ peoplePicker: ABPeoplePickerNavigationController!, didSelectPerson person: ABRecord!, property property: ABPropertyID, identifier identifier: ABMultiValueIdentifier)     optional func peoplePickerNavigationControllerDidCancel(_ peoplePicker: ABPeoplePickerNavigationController!)     optional func peoplePickerNavigationController(_ peoplePicker: ABPeoplePickerNavigationController!, shouldContinueAfterSelectingPerson person: ABRecord!) -> Bool     optional func peoplePickerNavigationController(_ peoplePicker: ABPeoplePickerNavigationController!, shouldContinueAfterSelectingPerson person: ABRecord!, property property: ABPropertyID, identifier identifier: ABMultiValueIdentifier) -> Bool } ``` |
| To | ``` protocol ABPeoplePickerNavigationControllerDelegate : NSObjectProtocol {     optional func peoplePickerNavigationController(_ peoplePicker: ABPeoplePickerNavigationController, didSelectPerson person: ABRecord)     optional func peoplePickerNavigationController(_ peoplePicker: ABPeoplePickerNavigationController, didSelectPerson person: ABRecord, property property: ABPropertyID, identifier identifier: ABMultiValueIdentifier)     optional func peoplePickerNavigationControllerDidCancel(_ peoplePicker: ABPeoplePickerNavigationController)     optional func peoplePickerNavigationController(_ peoplePicker: ABPeoplePickerNavigationController, shouldContinueAfterSelectingPerson person: ABRecord) -> Bool     optional func peoplePickerNavigationController(_ peoplePicker: ABPeoplePickerNavigationController, shouldContinueAfterSelectingPerson person: ABRecord, property property: ABPropertyID, identifier identifier: ABMultiValueIdentifier) -> Bool } ``` |

Modified [ABPeoplePickerNavigationControllerDelegate.peoplePickerNavigationController(_: ABPeoplePickerNavigationController, didSelectPerson: ABRecord)](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontrollerdelegate/1614403-peoplepickernavigationcontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func peoplePickerNavigationController(_ peoplePicker: ABPeoplePickerNavigationController!, didSelectPerson person: ABRecord!) ``` |
| To | ``` optional func peoplePickerNavigationController(_ peoplePicker: ABPeoplePickerNavigationController, didSelectPerson person: ABRecord) ``` |

Modified [ABPeoplePickerNavigationControllerDelegate.peoplePickerNavigationController(_: ABPeoplePickerNavigationController, didSelectPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier)](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontrollerdelegate/1614402-peoplepickernavigationcontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func peoplePickerNavigationController(_ peoplePicker: ABPeoplePickerNavigationController!, didSelectPerson person: ABRecord!, property property: ABPropertyID, identifier identifier: ABMultiValueIdentifier) ``` |
| To | ``` optional func peoplePickerNavigationController(_ peoplePicker: ABPeoplePickerNavigationController, didSelectPerson person: ABRecord, property property: ABPropertyID, identifier identifier: ABMultiValueIdentifier) ``` |

Modified [ABPeoplePickerNavigationControllerDelegate.peoplePickerNavigationController(_: ABPeoplePickerNavigationController, shouldContinueAfterSelectingPerson: ABRecord) -> Bool](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontrollerdelegate/1614405-peoplepickernavigationcontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func peoplePickerNavigationController(_ peoplePicker: ABPeoplePickerNavigationController!, shouldContinueAfterSelectingPerson person: ABRecord!) -> Bool ``` |
| To | ``` optional func peoplePickerNavigationController(_ peoplePicker: ABPeoplePickerNavigationController, shouldContinueAfterSelectingPerson person: ABRecord) -> Bool ``` |

Modified [ABPeoplePickerNavigationControllerDelegate.peoplePickerNavigationController(_: ABPeoplePickerNavigationController, shouldContinueAfterSelectingPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier) -> Bool](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontrollerdelegate/1614408-peoplepickernavigationcontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func peoplePickerNavigationController(_ peoplePicker: ABPeoplePickerNavigationController!, shouldContinueAfterSelectingPerson person: ABRecord!, property property: ABPropertyID, identifier identifier: ABMultiValueIdentifier) -> Bool ``` |
| To | ``` optional func peoplePickerNavigationController(_ peoplePicker: ABPeoplePickerNavigationController, shouldContinueAfterSelectingPerson person: ABRecord, property property: ABPropertyID, identifier identifier: ABMultiValueIdentifier) -> Bool ``` |

Modified [ABPeoplePickerNavigationControllerDelegate.peoplePickerNavigationControllerDidCancel(_: ABPeoplePickerNavigationController)](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontrollerdelegate/1614415-peoplepickernavigationcontroller)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func peoplePickerNavigationControllerDidCancel(_ peoplePicker: ABPeoplePickerNavigationController!) ``` | iOS 8.0 |
| To | ``` optional func peoplePickerNavigationControllerDidCancel(_ peoplePicker: ABPeoplePickerNavigationController) ``` | iOS 2.0 |

Modified [ABPersonViewController](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` class ABPersonViewController : UIViewController, UIViewControllerRestoration {     unowned(unsafe) var personViewDelegate: ABPersonViewControllerDelegate!     var addressBook: ABAddressBook!     var displayedPerson: ABRecord!     var displayedProperties: [AnyObject]!     var allowsEditing: Bool     var allowsActions: Bool     var shouldShowLinkedPeople: Bool     func setHighlightedItemForProperty(_ property: ABPropertyID, withIdentifier identifier: ABMultiValueIdentifier) } ``` | -- |
| To | ``` class ABPersonViewController : UIViewController, UIViewControllerRestoration {     unowned(unsafe) var personViewDelegate: ABPersonViewControllerDelegate?     var addressBook: ABAddressBook?     var displayedPerson: ABRecord     var displayedProperties: [NSNumber]?     var allowsEditing: Bool     var allowsActions: Bool     var shouldShowLinkedPeople: Bool     func setHighlightedItemForProperty(_ property: ABPropertyID, withIdentifier identifier: ABMultiValueIdentifier) } ``` | iOS 9.0 |

Modified [ABPersonViewController.addressBook](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/1622196-addressbook)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var addressBook: ABAddressBook! ``` | -- |
| To | ``` var addressBook: ABAddressBook? ``` | iOS 9.0 |

Modified [ABPersonViewController.allowsActions](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/1622201-allowsactions)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ABPersonViewController.allowsEditing](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/1622202-allowsediting)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ABPersonViewController.displayedPerson](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/1622197-displayedperson)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var displayedPerson: ABRecord! ``` | -- |
| To | ``` var displayedPerson: ABRecord ``` | iOS 9.0 |

Modified [ABPersonViewController.displayedProperties](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/1622204-displayedproperties)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var displayedProperties: [AnyObject]! ``` | -- |
| To | ``` var displayedProperties: [NSNumber]? ``` | iOS 9.0 |

Modified [ABPersonViewController.personViewDelegate](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/1622199-personviewdelegate)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` unowned(unsafe) var personViewDelegate: ABPersonViewControllerDelegate! ``` | -- |
| To | ``` unowned(unsafe) var personViewDelegate: ABPersonViewControllerDelegate? ``` | iOS 9.0 |

Modified [ABPersonViewController.setHighlightedItemForProperty(_: ABPropertyID, withIdentifier: ABMultiValueIdentifier)](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/1622203-sethighlighteditemforproperty)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ABPersonViewController.shouldShowLinkedPeople](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/1622207-shouldshowlinkedpeople)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ABPersonViewControllerDelegate](https://developer.apple.com/documentation/addressbookui/abpersonviewcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol ABPersonViewControllerDelegate : NSObjectProtocol {     func personViewController(_ personViewController: ABPersonViewController!, shouldPerformDefaultActionForPerson person: ABRecord!, property property: ABPropertyID, identifier identifier: ABMultiValueIdentifier) -> Bool } ``` |
| To | ``` protocol ABPersonViewControllerDelegate : NSObjectProtocol {     func personViewController(_ personViewController: ABPersonViewController, shouldPerformDefaultActionForPerson person: ABRecord, property property: ABPropertyID, identifier identifier: ABMultiValueIdentifier) -> Bool } ``` |

Modified [ABPersonViewControllerDelegate.personViewController(_: ABPersonViewController, shouldPerformDefaultActionForPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier) -> Bool](https://developer.apple.com/documentation/addressbookui/abpersonviewcontrollerdelegate/1622200-personviewcontroller)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func personViewController(_ personViewController: ABPersonViewController!, shouldPerformDefaultActionForPerson person: ABRecord!, property property: ABPropertyID, identifier identifier: ABMultiValueIdentifier) -> Bool ``` | iOS 8.0 |
| To | ``` func personViewController(_ personViewController: ABPersonViewController, shouldPerformDefaultActionForPerson person: ABRecord, property property: ABPropertyID, identifier identifier: ABMultiValueIdentifier) -> Bool ``` | iOS 2.0 |

Modified [ABUnknownPersonViewController](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` class ABUnknownPersonViewController : UIViewController {     unowned(unsafe) var unknownPersonViewDelegate: ABUnknownPersonViewControllerDelegate!     var addressBook: ABAddressBook!     var displayedPerson: ABRecord!     var alternateName: String!     var message: String!     var allowsActions: Bool     var allowsAddingToAddressBook: Bool } ``` | -- |
| To | ``` class ABUnknownPersonViewController : UIViewController {     unowned(unsafe) var unknownPersonViewDelegate: ABUnknownPersonViewControllerDelegate?     var addressBook: ABAddressBook?     var displayedPerson: ABRecord     var alternateName: String?     var message: String?     var allowsActions: Bool     var allowsAddingToAddressBook: Bool } ``` | iOS 9.0 |

Modified [ABUnknownPersonViewController.addressBook](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller/1621810-addressbook)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var addressBook: ABAddressBook! ``` | -- |
| To | ``` var addressBook: ABAddressBook? ``` | iOS 9.0 |

Modified [ABUnknownPersonViewController.allowsActions](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller/1621811-allowsactions)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ABUnknownPersonViewController.allowsAddingToAddressBook](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller/1621816-allowsaddingtoaddressbook)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ABUnknownPersonViewController.alternateName](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller/1621812-alternatename)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var alternateName: String! ``` | -- |
| To | ``` var alternateName: String? ``` | iOS 9.0 |

Modified [ABUnknownPersonViewController.displayedPerson](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller/1621813-displayedperson)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var displayedPerson: ABRecord! ``` | -- |
| To | ``` var displayedPerson: ABRecord ``` | iOS 9.0 |

Modified [ABUnknownPersonViewController.message](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller/1621819-message)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var message: String! ``` | -- |
| To | ``` var message: String? ``` | iOS 9.0 |

Modified [ABUnknownPersonViewController.unknownPersonViewDelegate](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller/1621817-unknownpersonviewdelegate)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` unowned(unsafe) var unknownPersonViewDelegate: ABUnknownPersonViewControllerDelegate! ``` | -- |
| To | ``` unowned(unsafe) var unknownPersonViewDelegate: ABUnknownPersonViewControllerDelegate? ``` | iOS 9.0 |

Modified [ABUnknownPersonViewControllerDelegate](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol ABUnknownPersonViewControllerDelegate : NSObjectProtocol {     func unknownPersonViewController(_ unknownCardViewController: ABUnknownPersonViewController!, didResolveToPerson person: ABRecord!)     optional func unknownPersonViewController(_ personViewController: ABUnknownPersonViewController!, shouldPerformDefaultActionForPerson person: ABRecord!, property property: ABPropertyID, identifier identifier: ABMultiValueIdentifier) -> Bool } ``` |
| To | ``` protocol ABUnknownPersonViewControllerDelegate : NSObjectProtocol {     func unknownPersonViewController(_ unknownCardViewController: ABUnknownPersonViewController, didResolveToPerson person: ABRecord?)     optional func unknownPersonViewController(_ personViewController: ABUnknownPersonViewController, shouldPerformDefaultActionForPerson person: ABRecord, property property: ABPropertyID, identifier identifier: ABMultiValueIdentifier) -> Bool } ``` |

Modified [ABUnknownPersonViewControllerDelegate.unknownPersonViewController(_: ABUnknownPersonViewController, didResolveToPerson: ABRecord?)](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontrollerdelegate/1621814-unknownpersonviewcontroller)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func unknownPersonViewController(_ unknownCardViewController: ABUnknownPersonViewController!, didResolveToPerson person: ABRecord!) ``` | iOS 8.0 |
| To | ``` func unknownPersonViewController(_ unknownCardViewController: ABUnknownPersonViewController, didResolveToPerson person: ABRecord?) ``` | iOS 2.0 |

Modified [ABUnknownPersonViewControllerDelegate.unknownPersonViewController(_: ABUnknownPersonViewController, shouldPerformDefaultActionForPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier) -> Bool](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontrollerdelegate/1621815-unknownpersonviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func unknownPersonViewController(_ personViewController: ABUnknownPersonViewController!, shouldPerformDefaultActionForPerson person: ABRecord!, property property: ABPropertyID, identifier identifier: ABMultiValueIdentifier) -> Bool ``` |
| To | ``` optional func unknownPersonViewController(_ personViewController: ABUnknownPersonViewController, shouldPerformDefaultActionForPerson person: ABRecord, property property: ABPropertyID, identifier identifier: ABMultiValueIdentifier) -> Bool ``` |

Modified [ABCreateStringWithAddressDictionary(_: [NSObject : AnyObject], _: Bool) -> String](https://developer.apple.com/documentation/addressbookui/1624198-abcreatestringwithaddressdiction)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func ABCreateStringWithAddressDictionary(_ address: [NSObject : AnyObject]!, _ addCountryName: Bool) -> String! ``` | iOS 8.0 | -- |
| To | ``` func ABCreateStringWithAddressDictionary(_ address: [NSObject : AnyObject], _ addCountryName: Bool) -> String ``` | iOS 2.0 | iOS 9.0 |

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
