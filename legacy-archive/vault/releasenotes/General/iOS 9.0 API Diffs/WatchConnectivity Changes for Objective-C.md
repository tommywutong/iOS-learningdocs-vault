---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/WatchConnectivity.html
archived_at: '2026-07-18T02:56:38.278923Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# WatchConnectivity Changes for Objective-C

### WatchConnectivity (Added)

#### WCDefines.h (Added)

Added #def WC_EXTERN

#### WCError.h (Added)

Added [WCErrorCode](https://developer.apple.com/documentation/watchconnectivity/wcerror/code)Added [WCErrorCodeDeliveryFailed](https://developer.apple.com/documentation/watchconnectivity/wcerrorcode/wcerrorcodedeliveryfailed)Added [WCErrorCodeDeviceNotPaired](https://developer.apple.com/documentation/watchconnectivity/wcerror/code/devicenotpaired)Added [WCErrorCodeFileAccessDenied](https://developer.apple.com/documentation/watchconnectivity/wcerror/code/fileaccessdenied)Added [WCErrorCodeGenericError](https://developer.apple.com/documentation/watchconnectivity/wcerrorcode/wcerrorcodegenericerror)Added [WCErrorCodeInsufficientSpace](https://developer.apple.com/documentation/watchconnectivity/wcerror/code/insufficientspace)Added [WCErrorCodeInvalidParameter](https://developer.apple.com/documentation/watchconnectivity/wcerrorcode/wcerrorcodeinvalidparameter)Added [WCErrorCodeMessageReplyFailed](https://developer.apple.com/documentation/watchconnectivity/wcerrorcode/wcerrorcodemessagereplyfailed)Added [WCErrorCodeMessageReplyTimedOut](https://developer.apple.com/documentation/watchconnectivity/wcerrorcode/wcerrorcodemessagereplytimedout)Added [WCErrorCodeNotReachable](https://developer.apple.com/documentation/watchconnectivity/wcerrorcode/wcerrorcodenotreachable)Added [WCErrorCodePayloadTooLarge](https://developer.apple.com/documentation/watchconnectivity/wcerrorcode/wcerrorcodepayloadtoolarge)Added [WCErrorCodePayloadUnsupportedTypes](https://developer.apple.com/documentation/watchconnectivity/wcerrorcode/wcerrorcodepayloadunsupportedtypes)Added [WCErrorCodeSessionMissingDelegate](https://developer.apple.com/documentation/watchconnectivity/wcerror/code/sessionmissingdelegate)Added [WCErrorCodeSessionNotActivated](https://developer.apple.com/documentation/watchconnectivity/wcerror/code/sessionnotactivated)Added [WCErrorCodeSessionNotSupported](https://developer.apple.com/documentation/watchconnectivity/wcerror/code/sessionnotsupported)Added [WCErrorCodeWatchAppNotInstalled](https://developer.apple.com/documentation/watchconnectivity/wcerror/code/watchappnotinstalled)Added [WCErrorDomain](https://developer.apple.com/documentation/watchconnectivity/wcerrordomain)

#### WCSession.h (Added)

Added [WCSession](https://developer.apple.com/documentation/watchconnectivity/wcsession)Added [-[WCSession activateSession]](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615655-activatesession)Added [WCSession.applicationContext](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615643-applicationcontext)Added [WCSession.complicationEnabled](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615625-complicationenabled)Added [+[WCSession defaultSession]](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615673-defaultsession)Added [WCSession.delegate](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615675-delegate)Added [+[WCSession isSupported]](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615647-issupported)Added [WCSession.outstandingFileTransfers](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615641-outstandingfiletransfers)Added [WCSession.outstandingUserInfoTransfers](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615627-outstandinguserinfotransfers)Added [WCSession.paired](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615665-ispaired)Added [WCSession.reachable](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615683-isreachable)Added [WCSession.receivedApplicationContext](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615635-receivedapplicationcontext)Added [-[WCSession sendMessage:replyHandler:errorHandler:]](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615687-sendmessage)Added [-[WCSession sendMessageData:replyHandler:errorHandler:]](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615617-sendmessagedata)Added [-[WCSession transferCurrentComplicationUserInfo:]](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615639-transfercurrentcomplicationuseri)Added [-[WCSession transferFile:metadata:]](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615667-transferfile)Added [-[WCSession transferUserInfo:]](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615671-transferuserinfo)Added [-[WCSession updateApplicationContext:error:]](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615621-updateapplicationcontext)Added [WCSession.watchAppInstalled](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615623-watchappinstalled)Added [WCSession.watchDirectoryURL](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615645-watchdirectoryurl)Added [WCSessionDelegate](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate)Added [-[WCSessionDelegate session:didFinishFileTransfer:error:]](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615657-session)Added [-[WCSessionDelegate session:didFinishUserInfoTransfer:error:]](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615668-session)Added [-[WCSessionDelegate session:didReceiveApplicationContext:]](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615619-session)Added [-[WCSessionDelegate session:didReceiveFile:]](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615651-session)Added [-[WCSessionDelegate session:didReceiveMessage:]](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615637-session)Added [-[WCSessionDelegate session:didReceiveMessage:replyHandler:]](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615677-session)Added [-[WCSessionDelegate session:didReceiveMessageData:]](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615686-session)Added [-[WCSessionDelegate session:didReceiveMessageData:replyHandler:]](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615653-session)Added [-[WCSessionDelegate session:didReceiveUserInfo:]](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615633-session)Added [-[WCSessionDelegate sessionReachabilityDidChange:]](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615662-sessionreachabilitydidchange)Added [-[WCSessionDelegate sessionWatchStateDidChange:]](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615689-sessionwatchstatedidchange)

#### WCSessionFile.h (Added)

Added [WCSessionFile](https://developer.apple.com/documentation/watchconnectivity/wcsessionfile)Added [WCSessionFile.fileURL](https://developer.apple.com/documentation/watchconnectivity/wcsessionfile/1622170-fileurl)Added [WCSessionFile.metadata](https://developer.apple.com/documentation/watchconnectivity/wcsessionfile/1622172-metadata)Added [WCSessionFileTransfer](https://developer.apple.com/documentation/watchconnectivity/wcsessionfiletransfer)Added [-[WCSessionFileTransfer cancel]](https://developer.apple.com/documentation/watchconnectivity/wcsessionfiletransfer/1622166-cancel)Added [WCSessionFileTransfer.file](https://developer.apple.com/documentation/watchconnectivity/wcsessionfiletransfer/1622169-file)Added [WCSessionFileTransfer.transferring](https://developer.apple.com/documentation/watchconnectivity/wcsessionfiletransfer/1622167-transferring)

#### WCSessionUserInfoTransfer.h (Added)

Added [WCSessionUserInfoTransfer](https://developer.apple.com/documentation/watchconnectivity/wcsessionuserinfotransfer)Added [-[WCSessionUserInfoTransfer cancel]](https://developer.apple.com/documentation/watchconnectivity/wcsessionuserinfotransfer/1623890-cancel)Added [WCSessionUserInfoTransfer.currentComplicationInfo](https://developer.apple.com/documentation/watchconnectivity/wcsessionuserinfotransfer/1623891-iscurrentcomplicationinfo)Added [WCSessionUserInfoTransfer.transferring](https://developer.apple.com/documentation/watchconnectivity/wcsessionuserinfotransfer/1623892-istransferring)Added [WCSessionUserInfoTransfer.userInfo](https://developer.apple.com/documentation/watchconnectivity/wcsessionuserinfotransfer/1623888-userinfo)

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
