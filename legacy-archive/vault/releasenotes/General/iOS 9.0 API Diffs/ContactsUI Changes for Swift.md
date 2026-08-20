---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/ContactsUI.html
archived_at: '2026-07-18T02:56:42.714234Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# ContactsUI Changes for Swift

### ContactsUI (Added)

Added [CNContactPickerDelegate](https://developer.apple.com/documentation/contactsui/cncontactpickerdelegate)Added [CNContactPickerDelegate.contactPicker(_: CNContactPickerViewController, didSelectContact: CNContact)](https://developer.apple.com/documentation/contactsui/cncontactpickerdelegate/1522595-contactpicker)Added [CNContactPickerDelegate.contactPicker(_: CNContactPickerViewController, didSelectContactProperties: [CNContactProperty])](https://developer.apple.com/documentation/contactsui/cncontactpickerdelegate/1619202-contactpicker)Added [CNContactPickerDelegate.contactPicker(_: CNContactPickerViewController, didSelectContactProperty: CNContactProperty)](https://developer.apple.com/documentation/contactsui/cncontactpickerdelegate/1522593-contactpicker)Added [CNContactPickerDelegate.contactPicker(_: CNContactPickerViewController, didSelectContacts: [CNContact])](https://developer.apple.com/documentation/contactsui/cncontactpickerdelegate/1619207-contactpicker)Added [CNContactPickerDelegate.contactPickerDidCancel(_: CNContactPickerViewController)](https://developer.apple.com/documentation/contactsui/cncontactpickerdelegate/1619204-contactpickerdidcancel)Added [CNContactPickerViewController](https://developer.apple.com/documentation/contactsui/cncontactpickerviewcontroller)Added [CNContactPickerViewController.delegate](https://developer.apple.com/documentation/contactsui/cncontactpickerviewcontroller/1619206-delegate)Added [CNContactPickerViewController.displayedPropertyKeys](https://developer.apple.com/documentation/contactsui/cncontactpickerviewcontroller/1619203-displayedpropertykeys)Added [CNContactPickerViewController.predicateForEnablingContact](https://developer.apple.com/documentation/contactsui/cncontactpickerviewcontroller/1619201-predicateforenablingcontact)Added [CNContactPickerViewController.predicateForSelectionOfContact](https://developer.apple.com/documentation/contactsui/cncontactpickerviewcontroller/1619200-predicateforselectionofcontact)Added [CNContactPickerViewController.predicateForSelectionOfProperty](https://developer.apple.com/documentation/contactsui/cncontactpickerviewcontroller/1619205-predicateforselectionofproperty)Added [CNContactViewController](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller)Added [CNContactViewController.allowsActions](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/1616913-allowsactions)Added [CNContactViewController.allowsEditing](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/1616920-allowsediting)Added [CNContactViewController.alternateName](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/1616911-alternatename)Added [CNContactViewController.contact](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/1522596-contact)Added [CNContactViewController.contactStore](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/1616912-contactstore)Added [CNContactViewController.delegate](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/1616918-delegate)Added [CNContactViewController.descriptorForRequiredKeys() -> CNKeyDescriptor [class]](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/1550990-descriptorforrequiredkeys)Added [CNContactViewController.displayedPropertyKeys](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/1616915-displayedpropertykeys)Added [CNContactViewController.highlightPropertyWithKey(_: String, identifier: String?)](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/1616921-highlightpropertywithkey)Added [CNContactViewController.init(forContact: CNContact)](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/1616927-viewcontrollerforcontact)Added [CNContactViewController.init(forNewContact: CNContact?)](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/1616922-viewcontrollerfornewcontact)Added [CNContactViewController.init(forUnknownContact: CNContact)](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/1616916-init)Added [CNContactViewController.message](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/1616923-message)Added [CNContactViewController.parentContainer](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/1616926-parentcontainer)Added [CNContactViewController.parentGroup](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/1616919-parentgroup)Added [CNContactViewController.shouldShowLinkedContacts](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/1616917-shouldshowlinkedcontacts)Added [CNContactViewControllerDelegate](https://developer.apple.com/documentation/contactsui/cncontactviewcontrollerdelegate)Added [CNContactViewControllerDelegate.contactViewController(_: CNContactViewController, didCompleteWithContact: CNContact?)](https://developer.apple.com/documentation/contactsui/cncontactviewcontrollerdelegate/1616925-contactviewcontroller)Added [CNContactViewControllerDelegate.contactViewController(_: CNContactViewController, shouldPerformDefaultActionForContactProperty: CNContactProperty) -> Bool](https://developer.apple.com/documentation/contactsui/cncontactviewcontrollerdelegate/1616914-contactviewcontroller)Added [UIApplicationShortcutIcon.init(contact: CNContact)](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/1616849-iconwithcontact)

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
