---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/IMServicePlugIn.html
archived_at: '2026-07-18T02:52:30.791104Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# IMServicePlugIn Changes

## IMServicePlugIn

Modified IMServicePlugIn.init(serviceApplication: IMServiceApplication!)

|  | Declaration |
| --- | --- |
| From | ``` init(serviceApplication serviceApplication: IMServiceApplication!) ``` |
| To | ``` init!(serviceApplication serviceApplication: IMServiceApplication!) ``` |

Modified IMServicePlugInMessage.content

|  | Declaration |
| --- | --- |
| From | ``` var content: NSAttributedString! ``` |
| To | ``` @NSCopying var content: NSAttributedString! ``` |

Modified IMServicePlugInMessage.init(content: NSAttributedString!)

|  | Declaration |
| --- | --- |
| From | ``` init(content content: NSAttributedString!) ``` |
| To | ``` init!(content content: NSAttributedString!) ``` |

Modified IMServicePlugInMessage.init(content: NSAttributedString!, date: NSDate!)

|  | Declaration |
| --- | --- |
| From | ``` init(content content: NSAttributedString!, date date: NSDate!) ``` |
| To | ``` init!(content content: NSAttributedString!, date date: NSDate!) ``` |

Modified IMServicePlugInMessage.date

|  | Declaration |
| --- | --- |
| From | ``` var date: NSDate! ``` |
| To | ``` @NSCopying var date: NSDate! ``` |

Modified IMAccountSettingLoginHandle

|  | Declaration |
| --- | --- |
| From | ``` let IMAccountSettingLoginHandle: NSString! ``` |
| To | ``` let IMAccountSettingLoginHandle: String ``` |

Modified IMAccountSettingPassword

|  | Declaration |
| --- | --- |
| From | ``` let IMAccountSettingPassword: NSString! ``` |
| To | ``` let IMAccountSettingPassword: String ``` |

Modified IMAccountSettingServerHost

|  | Declaration |
| --- | --- |
| From | ``` let IMAccountSettingServerHost: NSString! ``` |
| To | ``` let IMAccountSettingServerHost: String ``` |

Modified IMAccountSettingServerPort

|  | Declaration |
| --- | --- |
| From | ``` let IMAccountSettingServerPort: NSString! ``` |
| To | ``` let IMAccountSettingServerPort: String ``` |

Modified IMAccountSettingUsesSSL

|  | Declaration |
| --- | --- |
| From | ``` let IMAccountSettingUsesSSL: NSString! ``` |
| To | ``` let IMAccountSettingUsesSSL: String ``` |

Modified IMAttributeBackgroundColor

|  | Declaration |
| --- | --- |
| From | ``` let IMAttributeBackgroundColor: NSString! ``` |
| To | ``` let IMAttributeBackgroundColor: String ``` |

Modified IMAttributeBaseWritingDirection

|  | Declaration |
| --- | --- |
| From | ``` let IMAttributeBaseWritingDirection: NSString! ``` |
| To | ``` let IMAttributeBaseWritingDirection: String ``` |

Modified IMAttributeBold

|  | Declaration |
| --- | --- |
| From | ``` let IMAttributeBold: NSString! ``` |
| To | ``` let IMAttributeBold: String ``` |

Modified IMAttributeFontFamily

|  | Declaration |
| --- | --- |
| From | ``` let IMAttributeFontFamily: NSString! ``` |
| To | ``` let IMAttributeFontFamily: String ``` |

Modified IMAttributeFontSize

|  | Declaration |
| --- | --- |
| From | ``` let IMAttributeFontSize: NSString! ``` |
| To | ``` let IMAttributeFontSize: String ``` |

Modified IMAttributeForegroundColor

|  | Declaration |
| --- | --- |
| From | ``` let IMAttributeForegroundColor: NSString! ``` |
| To | ``` let IMAttributeForegroundColor: String ``` |

Modified IMAttributeItalic

|  | Declaration |
| --- | --- |
| From | ``` let IMAttributeItalic: NSString! ``` |
| To | ``` let IMAttributeItalic: String ``` |

Modified IMAttributeLink

|  | Declaration |
| --- | --- |
| From | ``` let IMAttributeLink: NSString! ``` |
| To | ``` let IMAttributeLink: String ``` |

Modified IMAttributeMessageBackgroundColor

|  | Declaration |
| --- | --- |
| From | ``` let IMAttributeMessageBackgroundColor: NSString! ``` |
| To | ``` let IMAttributeMessageBackgroundColor: String ``` |

Modified IMAttributePreformatted

|  | Declaration |
| --- | --- |
| From | ``` let IMAttributePreformatted: NSString! ``` |
| To | ``` let IMAttributePreformatted: String ``` |

Modified IMAttributeStrikethrough

|  | Declaration |
| --- | --- |
| From | ``` let IMAttributeStrikethrough: NSString! ``` |
| To | ``` let IMAttributeStrikethrough: String ``` |

Modified IMAttributeUnderline

|  | Declaration |
| --- | --- |
| From | ``` let IMAttributeUnderline: NSString! ``` |
| To | ``` let IMAttributeUnderline: String ``` |

Modified IMGroupListDefaultGroup

|  | Declaration |
| --- | --- |
| From | ``` let IMGroupListDefaultGroup: NSString! ``` |
| To | ``` let IMGroupListDefaultGroup: String ``` |

Modified IMGroupListHandlesKey

|  | Declaration |
| --- | --- |
| From | ``` let IMGroupListHandlesKey: NSString! ``` |
| To | ``` let IMGroupListHandlesKey: String ``` |

Modified IMGroupListNameKey

|  | Declaration |
| --- | --- |
| From | ``` let IMGroupListNameKey: NSString! ``` |
| To | ``` let IMGroupListNameKey: String ``` |

Modified IMGroupListPermissionsKey

|  | Declaration |
| --- | --- |
| From | ``` let IMGroupListPermissionsKey: NSString! ``` |
| To | ``` let IMGroupListPermissionsKey: String ``` |

Modified IMHandleCapabilityChatRoom

|  | Declaration |
| --- | --- |
| From | ``` let IMHandleCapabilityChatRoom: NSString! ``` |
| To | ``` let IMHandleCapabilityChatRoom: String ``` |

Modified IMHandleCapabilityFileTransfer

|  | Declaration |
| --- | --- |
| From | ``` let IMHandleCapabilityFileTransfer: NSString! ``` |
| To | ``` let IMHandleCapabilityFileTransfer: String ``` |

Modified IMHandleCapabilityHandlePicture

|  | Declaration |
| --- | --- |
| From | ``` let IMHandleCapabilityHandlePicture: NSString! ``` |
| To | ``` let IMHandleCapabilityHandlePicture: String ``` |

Modified IMHandleCapabilityMessaging

|  | Declaration |
| --- | --- |
| From | ``` let IMHandleCapabilityMessaging: NSString! ``` |
| To | ``` let IMHandleCapabilityMessaging: String ``` |

Modified IMHandleCapabilityOfflineMessaging

|  | Declaration |
| --- | --- |
| From | ``` let IMHandleCapabilityOfflineMessaging: NSString! ``` |
| To | ``` let IMHandleCapabilityOfflineMessaging: String ``` |

Modified IMHandlePropertyAlias

|  | Declaration |
| --- | --- |
| From | ``` let IMHandlePropertyAlias: NSString! ``` |
| To | ``` let IMHandlePropertyAlias: String ``` |

Modified IMHandlePropertyAuthorizationStatus

|  | Declaration |
| --- | --- |
| From | ``` let IMHandlePropertyAuthorizationStatus: NSString! ``` |
| To | ``` let IMHandlePropertyAuthorizationStatus: String ``` |

Modified IMHandlePropertyAvailability

|  | Declaration |
| --- | --- |
| From | ``` let IMHandlePropertyAvailability: NSString! ``` |
| To | ``` let IMHandlePropertyAvailability: String ``` |

Modified IMHandlePropertyCapabilities

|  | Declaration |
| --- | --- |
| From | ``` let IMHandlePropertyCapabilities: NSString! ``` |
| To | ``` let IMHandlePropertyCapabilities: String ``` |

Modified IMHandlePropertyEmailAddress

|  | Declaration |
| --- | --- |
| From | ``` let IMHandlePropertyEmailAddress: NSString! ``` |
| To | ``` let IMHandlePropertyEmailAddress: String ``` |

Modified IMHandlePropertyFirstName

|  | Declaration |
| --- | --- |
| From | ``` let IMHandlePropertyFirstName: NSString! ``` |
| To | ``` let IMHandlePropertyFirstName: String ``` |

Modified IMHandlePropertyIdleDate

|  | Declaration |
| --- | --- |
| From | ``` let IMHandlePropertyIdleDate: NSString! ``` |
| To | ``` let IMHandlePropertyIdleDate: String ``` |

Modified IMHandlePropertyLastName

|  | Declaration |
| --- | --- |
| From | ``` let IMHandlePropertyLastName: NSString! ``` |
| To | ``` let IMHandlePropertyLastName: String ``` |

Modified IMHandlePropertyPictureData

|  | Declaration |
| --- | --- |
| From | ``` let IMHandlePropertyPictureData: NSString! ``` |
| To | ``` let IMHandlePropertyPictureData: String ``` |

Modified IMHandlePropertyPictureIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let IMHandlePropertyPictureIdentifier: NSString! ``` |
| To | ``` let IMHandlePropertyPictureIdentifier: String ``` |

Modified IMHandlePropertyStatusMessage

|  | Declaration |
| --- | --- |
| From | ``` let IMHandlePropertyStatusMessage: NSString! ``` |
| To | ``` let IMHandlePropertyStatusMessage: String ``` |

Modified IMSessionPropertyAvailability

|  | Declaration |
| --- | --- |
| From | ``` let IMSessionPropertyAvailability: NSString! ``` |
| To | ``` let IMSessionPropertyAvailability: String ``` |

Modified IMSessionPropertyIdleDate

|  | Declaration |
| --- | --- |
| From | ``` let IMSessionPropertyIdleDate: NSString! ``` |
| To | ``` let IMSessionPropertyIdleDate: String ``` |

Modified IMSessionPropertyIsInvisible

|  | Declaration |
| --- | --- |
| From | ``` let IMSessionPropertyIsInvisible: NSString! ``` |
| To | ``` let IMSessionPropertyIsInvisible: String ``` |

Modified IMSessionPropertyPictureData

|  | Declaration |
| --- | --- |
| From | ``` let IMSessionPropertyPictureData: NSString! ``` |
| To | ``` let IMSessionPropertyPictureData: String ``` |

Modified IMSessionPropertyStatusMessage

|  | Declaration |
| --- | --- |
| From | ``` let IMSessionPropertyStatusMessage: NSString! ``` |
| To | ``` let IMSessionPropertyStatusMessage: String ``` |

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
