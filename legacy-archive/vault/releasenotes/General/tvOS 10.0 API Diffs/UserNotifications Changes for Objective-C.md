---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Objective-C/UserNotifications.html
archived_at: '2026-07-18T02:57:28.608222Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# UserNotifications Changes for Objective-C

### UserNotifications (Added)

#### NSString+UserNotifications.h (Added)

Added NSString(UNUserNotificationCenterSupport)

#### UNError.h (Added)

Added [UNErrorCode](https://developer.apple.com/documentation/usernotifications/unerrorcode)Added [UNErrorCodeAttachmentCorrupt](https://developer.apple.com/documentation/usernotifications/unerrorcode/unerrorcodeattachmentcorrupt)Added [UNErrorCodeAttachmentInvalidFileSize](https://developer.apple.com/documentation/usernotifications/unerror/code/attachmentinvalidfilesize)Added [UNErrorCodeAttachmentInvalidURL](https://developer.apple.com/documentation/usernotifications/unerror/code/attachmentinvalidurl)Added [UNErrorCodeAttachmentMoveIntoDataStoreFailed](https://developer.apple.com/documentation/usernotifications/unerrorcode/unerrorcodeattachmentmoveintodatastorefailed)Added [UNErrorCodeAttachmentNotInDataStore](https://developer.apple.com/documentation/usernotifications/unerror/code/attachmentnotindatastore)Added [UNErrorCodeAttachmentUnrecognizedType](https://developer.apple.com/documentation/usernotifications/unerrorcode/unerrorcodeattachmentunrecognizedtype)Added [UNErrorCodeNotificationInvalidNoContent](https://developer.apple.com/documentation/usernotifications/unerror/code/notificationinvalidnocontent)Added [UNErrorCodeNotificationInvalidNoDate](https://developer.apple.com/documentation/usernotifications/unerrorcode/unerrorcodenotificationinvalidnodate)Added [UNErrorCodeNotificationsNotAllowed](https://developer.apple.com/documentation/usernotifications/unerrorcode/unerrorcodenotificationsnotallowed)Added [UNErrorDomain](https://developer.apple.com/documentation/usernotifications/unerrordomain)

#### UNNotification.h (Added)

Added [UNNotification](https://developer.apple.com/documentation/usernotifications/unnotification)Added [UNNotification.date](https://developer.apple.com/documentation/usernotifications/unnotification/1649326-date)Added [UNNotification.request](https://developer.apple.com/documentation/usernotifications/unnotification/1649324-request)

#### UNNotificationAction.h (Added)

Added [UNNotificationActionOptions](https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions)

#### UNNotificationAttachment.h (Added)

Added [UNNotificationAttachmentOptionsThumbnailClippingRectKey](https://developer.apple.com/documentation/usernotifications/unnotificationattachmentoptionsthumbnailclippingrectkey)Added [UNNotificationAttachmentOptionsThumbnailHiddenKey](https://developer.apple.com/documentation/usernotifications/unnotificationattachmentoptionsthumbnailhiddenkey)Added [UNNotificationAttachmentOptionsThumbnailTimeKey](https://developer.apple.com/documentation/usernotifications/unnotificationattachmentoptionsthumbnailtimekey)Added [UNNotificationAttachmentOptionsTypeHintKey](https://developer.apple.com/documentation/usernotifications/unnotificationattachmentoptionstypehintkey)

#### UNNotificationCategory.h (Added)

Added [UNNotificationCategoryOptions](https://developer.apple.com/documentation/usernotifications/unnotificationcategoryoptions)

#### UNNotificationContent.h (Added)

Added [UNMutableNotificationContent](https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent)Added [UNMutableNotificationContent.badge](https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/1649875-badge)Added [UNMutableNotificationContent.userInfo](https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/1649867-userinfo)Added [UNNotificationContent](https://developer.apple.com/documentation/usernotifications/unnotificationcontent)Added [UNNotificationContent.badge](https://developer.apple.com/documentation/usernotifications/unnotificationcontent/1649864-badge)

#### UNNotificationRequest.h (Added)

Added [UNNotificationRequest](https://developer.apple.com/documentation/usernotifications/unnotificationrequest)Added [UNNotificationRequest.content](https://developer.apple.com/documentation/usernotifications/unnotificationrequest/1649637-content)Added [UNNotificationRequest.identifier](https://developer.apple.com/documentation/usernotifications/unnotificationrequest/1649634-identifier)Added [+[UNNotificationRequest requestWithIdentifier:content:trigger:]](https://developer.apple.com/documentation/usernotifications/unnotificationrequest/1649633-init)Added [UNNotificationRequest.trigger](https://developer.apple.com/documentation/usernotifications/unnotificationrequest/1649635-trigger)

#### UNNotificationSettings.h (Added)

Added [UNNotificationSettings](https://developer.apple.com/documentation/usernotifications/unnotificationsettings)Added [UNNotificationSettings.authorizationStatus](https://developer.apple.com/documentation/usernotifications/unnotificationsettings/1648391-authorizationstatus)Added [UNNotificationSettings.badgeSetting](https://developer.apple.com/documentation/usernotifications/unnotificationsettings/1648389-badgesetting)Added [UNAlertStyle](https://developer.apple.com/documentation/usernotifications/unalertstyle)Added [UNAuthorizationStatus](https://developer.apple.com/documentation/usernotifications/unauthorizationstatus)Added [UNAuthorizationStatusAuthorized](https://developer.apple.com/documentation/usernotifications/unauthorizationstatus/authorized)Added [UNAuthorizationStatusDenied](https://developer.apple.com/documentation/usernotifications/unauthorizationstatus/unauthorizationstatusdenied)Added [UNAuthorizationStatusNotDetermined](https://developer.apple.com/documentation/usernotifications/unauthorizationstatus/unauthorizationstatusnotdetermined)Added [UNNotificationSetting](https://developer.apple.com/documentation/usernotifications/unnotificationsetting)Added [UNNotificationSettingDisabled](https://developer.apple.com/documentation/usernotifications/unnotificationsetting/unnotificationsettingdisabled)Added [UNNotificationSettingEnabled](https://developer.apple.com/documentation/usernotifications/unnotificationsetting/enabled)Added [UNNotificationSettingNotSupported](https://developer.apple.com/documentation/usernotifications/unnotificationsetting/notsupported)

#### UNNotificationTrigger.h (Added)

Added [UNCalendarNotificationTrigger](https://developer.apple.com/documentation/usernotifications/uncalendarnotificationtrigger)Added [UNCalendarNotificationTrigger.dateComponents](https://developer.apple.com/documentation/usernotifications/uncalendarnotificationtrigger/1649784-datecomponents)Added [-[UNCalendarNotificationTrigger nextTriggerDate]](https://developer.apple.com/documentation/usernotifications/uncalendarnotificationtrigger/1649775-nexttriggerdate)Added [+[UNCalendarNotificationTrigger triggerWithDateMatchingComponents:repeats:]](https://developer.apple.com/documentation/usernotifications/uncalendarnotificationtrigger/1649772-triggerwithdatematchingcomponent)Added [UNNotificationTrigger](https://developer.apple.com/documentation/usernotifications/unnotificationtrigger)Added [UNNotificationTrigger.repeats](https://developer.apple.com/documentation/usernotifications/unnotificationtrigger/1649782-repeats)Added [UNPushNotificationTrigger](https://developer.apple.com/documentation/usernotifications/unpushnotificationtrigger)Added [UNTimeIntervalNotificationTrigger](https://developer.apple.com/documentation/usernotifications/untimeintervalnotificationtrigger)Added [-[UNTimeIntervalNotificationTrigger nextTriggerDate]](https://developer.apple.com/documentation/usernotifications/untimeintervalnotificationtrigger/1649783-nexttriggerdate)Added [UNTimeIntervalNotificationTrigger.timeInterval](https://developer.apple.com/documentation/usernotifications/untimeintervalnotificationtrigger/1649779-timeinterval)Added [+[UNTimeIntervalNotificationTrigger triggerWithTimeInterval:repeats:]](https://developer.apple.com/documentation/usernotifications/untimeintervalnotificationtrigger/1649777-triggerwithtimeinterval)

#### UNUserNotificationCenter.h (Added)

Added [UNUserNotificationCenter](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter)Added [-[UNUserNotificationCenter addNotificationRequest:withCompletionHandler:]](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649508-addnotificationrequest)Added [+[UNUserNotificationCenter currentNotificationCenter]](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649510-current)Added [UNUserNotificationCenter.delegate](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649522-delegate)Added [-[UNUserNotificationCenter getNotificationSettingsWithCompletionHandler:]](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649524-getnotificationsettingswithcompl)Added [-[UNUserNotificationCenter getPendingNotificationRequestsWithCompletionHandler:]](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649513-getpendingnotificationrequests)Added [-[UNUserNotificationCenter removeAllPendingNotificationRequests]](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649509-removeallpendingnotificationrequ)Added [-[UNUserNotificationCenter removePendingNotificationRequestsWithIdentifiers:]](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649517-removependingnotificationrequest)Added [-[UNUserNotificationCenter requestAuthorizationWithOptions:completionHandler:]](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649527-requestauthorization)Added [UNUserNotificationCenter.supportsContentExtensions](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/2196946-supportscontentextensions)Added [UNUserNotificationCenterDelegate](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate)Added [-[UNUserNotificationCenterDelegate userNotificationCenter:willPresentNotification:withCompletionHandler:]](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate/1649518-usernotificationcenter)Added [UNAuthorizationOptionAlert](https://developer.apple.com/documentation/usernotifications/unauthorizationoptions/unauthorizationoptionalert)Added [UNAuthorizationOptionBadge](https://developer.apple.com/documentation/usernotifications/unauthorizationoptions/1649526-badge)Added [UNAuthorizationOptionCarPlay](https://developer.apple.com/documentation/usernotifications/unauthorizationoptions/1649525-carplay)Added [UNAuthorizationOptionNone](https://developer.apple.com/documentation/usernotifications/unauthorizationoptionnone)Added [UNAuthorizationOptions](https://developer.apple.com/documentation/usernotifications/unauthorizationoptions)Added [UNAuthorizationOptionSound](https://developer.apple.com/documentation/usernotifications/unauthorizationoptions/1649505-sound)Added [UNNotificationPresentationOptionAlert](https://developer.apple.com/documentation/usernotifications/unnotificationpresentationoptions/unnotificationpresentationoptionalert)Added [UNNotificationPresentationOptionBadge](https://developer.apple.com/documentation/usernotifications/unnotificationpresentationoptions/1649515-badge)Added [UNNotificationPresentationOptionNone](https://developer.apple.com/documentation/usernotifications/unnotificationpresentationoptionnone)Added [UNNotificationPresentationOptions](https://developer.apple.com/documentation/usernotifications/unnotificationpresentationoptions)Added [UNNotificationPresentationOptionSound](https://developer.apple.com/documentation/usernotifications/unnotificationpresentationoptions/unnotificationpresentationoptionsound)

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
