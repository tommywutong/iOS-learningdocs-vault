---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/AddressBookUI.html
archived_at: '2026-07-18T02:56:30.413226Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# AddressBookUI Changes for Objective-C

### AddressBookUI

#### ABAddressFormatting.h

Modified [ABCreateStringWithAddressDictionary()](https://developer.apple.com/documentation/addressbookui/1624198-abcreatestringwithaddressdiction)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### ABNewPersonViewController.h

Added [-[ABNewPersonViewController newPersonViewDelegate]](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontroller/1624262-newpersonviewdelegate)Modified [ABNewPersonViewController](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontroller)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ABNewPersonViewController.addressBook](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontroller/1624264-addressbook)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ABNewPersonViewController.displayedPerson](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontroller/1624263-displayedperson)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ABNewPersonViewController.newPersonViewDelegate](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontroller/1624265-newpersonviewdelegate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ABNewPersonViewController.parentGroup](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontroller/1624260-parentgroup)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### ABPeoplePickerNavigationController.h

Modified [ABPeoplePickerNavigationController](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ABPeoplePickerNavigationController.addressBook](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/1614407-addressbook)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ABPeoplePickerNavigationController.displayedProperties](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/1614398-displayedproperties)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *displayedProperties ``` | -- |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSNumber *> *displayedProperties ``` | iOS 9.0 |

Modified [ABPeoplePickerNavigationController.peoplePickerDelegate](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/1614428-peoplepickerdelegate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ABPeoplePickerNavigationController.predicateForEnablingPerson](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/1614417-predicateforenablingperson)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ABPeoplePickerNavigationController.predicateForSelectionOfPerson](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/1614400-predicateforselectionofperson)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ABPeoplePickerNavigationController.predicateForSelectionOfProperty](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/1614422-predicateforselectionofproperty)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### ABPersonViewController.h

Modified [ABPersonViewController](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ABPersonViewController.addressBook](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/1622196-addressbook)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

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

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ABPersonViewController.displayedProperties](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/1622204-displayedproperties)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *displayedProperties ``` | -- |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSNumber *> *displayedProperties ``` | iOS 9.0 |

Modified [ABPersonViewController.personViewDelegate](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/1622199-personviewdelegate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[ABPersonViewController setHighlightedItemForProperty:withIdentifier:]](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/1622203-sethighlighteditemforproperty)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ABPersonViewController.shouldShowLinkedPeople](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/1622207-shouldshowlinkedpeople)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### ABUnknownPersonViewController.h

Modified [ABUnknownPersonViewController](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ABUnknownPersonViewController.addressBook](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller/1621810-addressbook)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

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

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ABUnknownPersonViewController.displayedPerson](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller/1621813-displayedperson)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ABUnknownPersonViewController.message](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller/1621819-message)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ABUnknownPersonViewController.unknownPersonViewDelegate](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller/1621817-unknownpersonviewdelegate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

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
