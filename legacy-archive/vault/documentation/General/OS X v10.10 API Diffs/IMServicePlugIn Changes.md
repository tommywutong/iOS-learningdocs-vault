---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/IMServicePlugIn.html
archived_at: '2026-07-15T07:34:55.182209Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# IMServicePlugIn Changes

## IMServicePlugIn (Added)

Added IMGroupListPermissions [enum]Added IMGroupListPermissions.CanAddNewMembersAdded IMGroupListPermissions.CanRemoveMembersAdded IMGroupListPermissions.CanRenameGroupAdded IMGroupListPermissions.CanReorderGroupAdded IMGroupListPermissions.CanReorderMembersAdded IMHandleAuthorizationStatus [enum]Added IMHandleAuthorizationStatus.AcceptedAdded IMHandleAuthorizationStatus.DeclinedAdded IMHandleAuthorizationStatus.PendingAdded IMHandleAvailability [enum]Added IMHandleAvailability.AvailableAdded IMHandleAvailability.AwayAdded IMHandleAvailability.OfflineAdded IMHandleAvailability.UnknownAdded IMServiceApplicationAdded IMServiceApplication.plugInDidFailToAuthenticate()Added IMServiceApplication.plugInDidLogIn()Added IMServiceApplication.plugInDidLogOutWithError(NSError!, reconnect: Bool)Added IMServiceApplication.plugInDidUpdateProperties([NSObject: AnyObject]!, ofHandle: String!)Added IMServiceApplicationChatRoomSupportAdded IMServiceApplicationChatRoomSupport.handles([AnyObject]!, didJoinChatRoom: String!)Added IMServiceApplicationChatRoomSupport.handles([AnyObject]!, didLeaveChatRoom: String!)Added IMServiceApplicationChatRoomSupport.plugInDidJoinChatRoom(String!)Added IMServiceApplicationChatRoomSupport.plugInDidLeaveChatRoom(String!, error: NSError!)Added IMServiceApplicationChatRoomSupport.plugInDidReceiveInvitation(IMServicePlugInMessage!, forChatRoom: String!, fromHandle: String!)Added IMServiceApplicationChatRoomSupport.plugInDidReceiveMessage(IMServicePlugInMessage!, forChatRoom: String!, fromHandle: String!)Added IMServiceApplicationChatRoomSupport.plugInDidReceiveNotice(String!, forChatRoom: String!)Added IMServiceApplicationChatRoomSupport.plugInDidSendMessage(IMServicePlugInMessage!, toChatRoom: String!, error: NSError!)Added IMServiceApplicationGroupListAuthorizationSupportAdded IMServiceApplicationGroupListAuthorizationSupport.plugInDidReceiveAuthorizationRequestFromHandle(String!)Added IMServiceApplicationGroupListSupportAdded IMServiceApplicationGroupListSupport.plugInDidUpdateGroupList([AnyObject]!, error: NSError!)Added IMServiceApplicationInstantMessagingSupportAdded IMServiceApplicationInstantMessagingSupport.handleDidStartTyping(String!)Added IMServiceApplicationInstantMessagingSupport.handleDidStopTyping(String!)Added IMServiceApplicationInstantMessagingSupport.plugInDidReceiveMessage(IMServicePlugInMessage!, fromHandle: String!)Added IMServiceApplicationInstantMessagingSupport.plugInDidSendMessage(IMServicePlugInMessage!, toHandle: String!, error: NSError!)Added IMServicePlugInAdded IMServicePlugIn.login()Added IMServicePlugIn.logout()Added IMServicePlugIn.init(serviceApplication: IMServiceApplication!)Added IMServicePlugIn.updateAccountSettings([NSObject: AnyObject]!)Added IMServicePlugInChatRoomSupportAdded IMServicePlugInChatRoomSupport.declineChatRoomInvitation(String!)Added IMServicePlugInChatRoomSupport.inviteHandles([AnyObject]!, toChatRoom: String!, withMessage: IMServicePlugInMessage!)Added IMServicePlugInChatRoomSupport.joinChatRoom(String!)Added IMServicePlugInChatRoomSupport.leaveChatRoom(String!)Added IMServicePlugInChatRoomSupport.sendMessage(IMServicePlugInMessage!, toChatRoom: String!)Added IMServicePlugInGroupListAuthorizationSupportAdded IMServicePlugInGroupListAuthorizationSupport.acceptAuthorizationRequestFromHandle(String!)Added IMServicePlugInGroupListAuthorizationSupport.declineAuthorizationRequestFromHandle(String!)Added IMServicePlugInGroupListAuthorizationSupport.sendAuthorizationRequestToHandle(String!)Added IMServicePlugInGroupListEditingSupportAdded IMServicePlugInGroupListEditingSupport.addGroups([AnyObject]!)Added IMServicePlugInGroupListEditingSupport.addHandles([AnyObject]!, toGroup: String!)Added IMServicePlugInGroupListEditingSupport.removeGroups([AnyObject]!)Added IMServicePlugInGroupListEditingSupport.removeHandles([AnyObject]!, fromGroup: String!)Added IMServicePlugInGroupListEditingSupport.renameGroup(String!, toGroup: String!)Added IMServicePlugInGroupListHandlePictureSupportAdded IMServicePlugInGroupListHandlePictureSupport.requestPictureForHandle(String!, withIdentifier: String!)Added IMServicePlugInGroupListOrderingSupportAdded IMServicePlugInGroupListOrderingSupport.reorderGroups([AnyObject]!)Added IMServicePlugInGroupListOrderingSupport.reorderHandles([AnyObject]!, inGroup: String!)Added IMServicePlugInGroupListSupportAdded IMServicePlugInGroupListSupport.requestGroupList()Added IMServicePlugInInstantMessagingSupportAdded IMServicePlugInInstantMessagingSupport.sendMessage(IMServicePlugInMessage!, toHandle: String!)Added IMServicePlugInInstantMessagingSupport.userDidStartTypingToHandle(String!)Added IMServicePlugInInstantMessagingSupport.userDidStopTypingToHandle(String!)Added IMServicePlugInMessageAdded IMServicePlugInMessage.contentAdded IMServicePlugInMessage.init(content: NSAttributedString!)Added IMServicePlugInMessage.init(content: NSAttributedString!, date: NSDate!)Added IMServicePlugInMessage.dateAdded IMServicePlugInMessage.guidAdded IMServicePlugInMessage.servicePlugInMessageWithContent(NSAttributedString!) -> AnyObject! [class]Added IMServicePlugInMessage.servicePlugInMessageWithContent(NSAttributedString!, date: NSDate!) -> AnyObject! [class]Added IMServicePlugInPresenceSupportAdded IMServicePlugInPresenceSupport.updateSessionProperties([NSObject: AnyObject]!)Added IMSessionAvailability [enum]Added IMSessionAvailability.AvailableAdded IMSessionAvailability.AwayAdded IMAccountSettingLoginHandleAdded IMAccountSettingPasswordAdded IMAccountSettingServerHostAdded IMAccountSettingServerPortAdded IMAccountSettingUsesSSLAdded IMAttributeBackgroundColorAdded IMAttributeBaseWritingDirectionAdded IMAttributeBoldAdded IMAttributeFontFamilyAdded IMAttributeFontSizeAdded IMAttributeForegroundColorAdded IMAttributeItalicAdded IMAttributeLinkAdded IMAttributeMessageBackgroundColorAdded IMAttributePreformattedAdded IMAttributeStrikethroughAdded IMAttributeUnderlineAdded IMGroupListDefaultGroupAdded IMGroupListHandlesKeyAdded IMGroupListNameKeyAdded IMGroupListPermissionsKeyAdded IMHandleCapabilityChatRoomAdded IMHandleCapabilityFileTransferAdded IMHandleCapabilityHandlePictureAdded IMHandleCapabilityMessagingAdded IMHandleCapabilityOfflineMessagingAdded IMHandlePropertyAliasAdded IMHandlePropertyAuthorizationStatusAdded IMHandlePropertyAvailabilityAdded IMHandlePropertyCapabilitiesAdded IMHandlePropertyEmailAddressAdded IMHandlePropertyFirstNameAdded IMHandlePropertyIdleDateAdded IMHandlePropertyLastNameAdded IMHandlePropertyPictureDataAdded IMHandlePropertyPictureIdentifierAdded IMHandlePropertyStatusMessageAdded IMSessionPropertyAvailabilityAdded IMSessionPropertyIdleDateAdded IMSessionPropertyIsInvisibleAdded IMSessionPropertyPictureDataAdded IMSessionPropertyStatusMessage

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
