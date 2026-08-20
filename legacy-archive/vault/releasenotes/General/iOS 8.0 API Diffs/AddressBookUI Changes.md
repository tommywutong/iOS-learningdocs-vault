---
title: iOS 8.0 API Diffs
apple_id: TP40014455
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS80APIDiffs/frameworks/AddressBookUI.html
archived_at: '2026-07-18T02:55:55.517799Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.0 API Diffs](iOS%207.1%20to%20iOS%208.0%20API%20Differences.md)


# AddressBookUI Changes

## AddressBookUI

ABPeoplePickerNavigationController.hAdded [ABPeoplePickerNavigationController.predicateForEnablingPerson](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/1614417-predicateforenablingperson)Added [ABPeoplePickerNavigationController.predicateForSelectionOfPerson](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/1614400-predicateforselectionofperson)Added [ABPeoplePickerNavigationController.predicateForSelectionOfProperty](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/1614422-predicateforselectionofproperty)Added [-[ABPeoplePickerNavigationControllerDelegate peoplePickerNavigationController:didSelectPerson:]](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontrollerdelegate/1614403-peoplepickernavigationcontroller)Added [-[ABPeoplePickerNavigationControllerDelegate peoplePickerNavigationController:didSelectPerson:property:identifier:]](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontrollerdelegate/1614402-peoplepickernavigationcontroller)Added [ABPersonBirthdayProperty](https://developer.apple.com/documentation/addressbookui/abpersonbirthdayproperty)Added [ABPersonDatesProperty](https://developer.apple.com/documentation/addressbookui/abpersondatesproperty)Added [ABPersonDepartmentNameProperty](https://developer.apple.com/documentation/addressbookui/abpersondepartmentnameproperty)Added [ABPersonEmailAddressesProperty](https://developer.apple.com/documentation/addressbookui/abpersonemailaddressesproperty)Added [ABPersonFamilyNameProperty](https://developer.apple.com/documentation/addressbookui/abpersonfamilynameproperty)Added [ABPersonGivenNameProperty](https://developer.apple.com/documentation/addressbookui/abpersongivennameproperty)Added [ABPersonInstantMessageAddressesProperty](https://developer.apple.com/documentation/addressbookui/abpersoninstantmessageaddressesproperty)Added [ABPersonJobTitleProperty](https://developer.apple.com/documentation/addressbookui/abpersonjobtitleproperty)Added [ABPersonMiddleNameProperty](https://developer.apple.com/documentation/addressbookui/abpersonmiddlenameproperty)Added [ABPersonNamePrefixProperty](https://developer.apple.com/documentation/addressbookui/abpersonnameprefixproperty)Added [ABPersonNameSuffixProperty](https://developer.apple.com/documentation/addressbookui/abpersonnamesuffixproperty)Added [ABPersonNicknameProperty](https://developer.apple.com/documentation/addressbookui/abpersonnicknameproperty)Added [ABPersonNoteProperty](https://developer.apple.com/documentation/addressbookui/abpersonnoteproperty)Added [ABPersonOrganizationNameProperty](https://developer.apple.com/documentation/addressbookui/abpersonorganizationnameproperty)Added [ABPersonPhoneNumbersProperty](https://developer.apple.com/documentation/addressbookui/abpersonphonenumbersproperty)Added [ABPersonPhoneticFamilyNameProperty](https://developer.apple.com/documentation/addressbookui/abpersonphoneticfamilynameproperty)Added [ABPersonPhoneticGivenNameProperty](https://developer.apple.com/documentation/addressbookui/abpersonphoneticgivennameproperty)Added [ABPersonPhoneticMiddleNameProperty](https://developer.apple.com/documentation/addressbookui/abpersonphoneticmiddlenameproperty)Added [ABPersonPostalAddressesProperty](https://developer.apple.com/documentation/addressbookui/abpersonpostaladdressesproperty)Added [ABPersonPreviousFamilyNameProperty](https://developer.apple.com/documentation/addressbookui/abpersonpreviousfamilynameproperty)Added [ABPersonRelatedNamesProperty](https://developer.apple.com/documentation/addressbookui/abpersonrelatednamesproperty)Added [ABPersonSocialProfilesProperty](https://developer.apple.com/documentation/addressbookui/abpersonsocialprofilesproperty)Added [ABPersonUrlAddressesProperty](https://developer.apple.com/documentation/addressbookui/abpersonurladdressesproperty)Modified [-[ABPeoplePickerNavigationControllerDelegate peoplePickerNavigationController:shouldContinueAfterSelectingPerson:]](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontrollerdelegate/1614405-peoplepickernavigationcontroller)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 8.0 | yes |

Modified [-[ABPeoplePickerNavigationControllerDelegate peoplePickerNavigationController:shouldContinueAfterSelectingPerson:property:identifier:]](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontrollerdelegate/1614408-peoplepickernavigationcontroller)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 8.0 | yes |

Modified [-[ABPeoplePickerNavigationControllerDelegate peoplePickerNavigationControllerDidCancel:]](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontrollerdelegate/1614415-peoplepickernavigationcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

ABUnknownPersonViewController.hModified [-[ABUnknownPersonViewControllerDelegate unknownPersonViewController:shouldPerformDefaultActionForPerson:property:identifier:]](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontrollerdelegate/1621815-unknownpersonviewcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

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
