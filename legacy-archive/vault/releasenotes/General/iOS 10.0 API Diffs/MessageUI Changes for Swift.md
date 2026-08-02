---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/MessageUI.html
archived_at: '2026-07-18T02:55:32.171247Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# MessageUI Changes for Swift

### MessageUI

Removed MessageComposeResult.init(_: UInt32)Removed MessageComposeResult.init(rawValue: UInt32)Removed MessageComposeResult.rawValueRemoved MFMailComposeErrorCode.init(_: UInt32)Removed MFMailComposeErrorCode.init(rawValue: UInt32)Removed MFMailComposeErrorCode.rawValueRemoved MFMailComposeResult.init(_: UInt32)Removed MFMailComposeResult.init(rawValue: UInt32)Removed MFMailComposeResult.rawValueAdded [MFMailComposeError [struct]](https://developer.apple.com/documentation/messageui/mfmailcomposeerror)Added MFMailComposeError.init(_nsError: NSError)Added [MFMailComposeError.saveFailed](https://developer.apple.com/documentation/messageui/mfmailcomposeerror/2340120-savefailed)Added [MFMailComposeError.sendFailed](https://developer.apple.com/documentation/messageui/mfmailcomposeerror/2340119-sendfailed)Added [MFMessageComposeViewController.message](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/2213331-message)Modified [MessageComposeResult [enum]](https://developer.apple.com/documentation/messageui/messagecomposeresult)

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` struct MessageComposeResult : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable | iOS 8.1 | -- |
| To | ``` enum MessageComposeResult : Int {     case cancelled     case sent     case failed } ``` | -- | iOS 4.0 | Int |

Modified [MessageComposeResult.cancelled](https://developer.apple.com/documentation/messageui/messagecomposeresult/cancelled)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | MessageComposeResultCancelled | ``` var MessageComposeResultCancelled: MessageComposeResult { get } ``` | iOS 8.0 |
| To | cancelled | ``` case cancelled ``` | iOS 10.0 |

Modified [MessageComposeResult.failed](https://developer.apple.com/documentation/messageui/messagecomposeresult/messagecomposeresultfailed)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | MessageComposeResultFailed | ``` var MessageComposeResultFailed: MessageComposeResult { get } ``` | iOS 8.0 |
| To | failed | ``` case failed ``` | iOS 10.0 |

Modified [MessageComposeResult.sent](https://developer.apple.com/documentation/messageui/messagecomposeresult/sent)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | MessageComposeResultSent | ``` var MessageComposeResultSent: MessageComposeResult { get } ``` | iOS 8.0 |
| To | sent | ``` case sent ``` | iOS 10.0 |

Modified [MFMailComposeError.Code [enum]](https://developer.apple.com/documentation/messageui/mfmailcomposeerrorcode)

|  | Name | Declaration | Protocols | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | MFMailComposeError | ``` struct MFMailComposeErrorCode : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable | -- |
| To | MFMailComposeError.Code | ``` enum Code : Int {         typealias _ErrorType = MFMailComposeError         case saveFailed         case sendFailed     } ``` | -- | Int |

Modified [MFMailComposeError.Code.saveFailed](https://developer.apple.com/documentation/messageui/mfmailcomposeerror/code/savefailed)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | MFMailComposeErrorCodeSaveFailed | ``` var MFMailComposeErrorCodeSaveFailed: MFMailComposeErrorCode { get } ``` | iOS 8.0 |
| To | saveFailed | ``` case saveFailed ``` | iOS 10.0 |

Modified [MFMailComposeError.Code.sendFailed](https://developer.apple.com/documentation/messageui/mfmailcomposeerror/code/sendfailed)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | MFMailComposeErrorCodeSendFailed | ``` var MFMailComposeErrorCodeSendFailed: MFMailComposeErrorCode { get } ``` | iOS 8.0 |
| To | sendFailed | ``` case sendFailed ``` | iOS 10.0 |

Modified [MFMailComposeResult [enum]](https://developer.apple.com/documentation/messageui/mfmailcomposeresult)

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` struct MFMailComposeResult : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable | iOS 8.1 | -- |
| To | ``` enum MFMailComposeResult : Int {     case cancelled     case saved     case sent     case failed } ``` | -- | iOS 3.0 | Int |

Modified [MFMailComposeResult.cancelled](https://developer.apple.com/documentation/messageui/mfmailcomposeresult/cancelled)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | MFMailComposeResultCancelled | ``` var MFMailComposeResultCancelled: MFMailComposeResult { get } ``` | iOS 8.0 |
| To | cancelled | ``` case cancelled ``` | iOS 10.0 |

Modified [MFMailComposeResult.failed](https://developer.apple.com/documentation/messageui/mfmailcomposeresult/failed)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | MFMailComposeResultFailed | ``` var MFMailComposeResultFailed: MFMailComposeResult { get } ``` | iOS 8.0 |
| To | failed | ``` case failed ``` | iOS 10.0 |

Modified [MFMailComposeResult.saved](https://developer.apple.com/documentation/messageui/mfmailcomposeresult/mfmailcomposeresultsaved)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | MFMailComposeResultSaved | ``` var MFMailComposeResultSaved: MFMailComposeResult { get } ``` | iOS 8.0 |
| To | saved | ``` case saved ``` | iOS 10.0 |

Modified [MFMailComposeResult.sent](https://developer.apple.com/documentation/messageui/mfmailcomposeresult/sent)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | MFMailComposeResultSent | ``` var MFMailComposeResultSent: MFMailComposeResult { get } ``` | iOS 8.0 |
| To | sent | ``` case sent ``` | iOS 10.0 |

Modified [MFMailComposeViewController](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class MFMailComposeViewController : UINavigationController {     class func canSendMail() -> Bool     unowned(unsafe) var mailComposeDelegate: MFMailComposeViewControllerDelegate?     func setSubject(_ subject: String)     func setToRecipients(_ toRecipients: [String]?)     func setCcRecipients(_ ccRecipients: [String]?)     func setBccRecipients(_ bccRecipients: [String]?)     func setMessageBody(_ body: String, isHTML isHTML: Bool)     func addAttachmentData(_ attachment: NSData, mimeType mimeType: String, fileName filename: String) } ``` |
| To | ``` class MFMailComposeViewController : UINavigationController {     class func canSendMail() -> Bool     unowned(unsafe) var mailComposeDelegate: MFMailComposeViewControllerDelegate?     func setSubject(_ subject: String)     func setToRecipients(_ toRecipients: [String]?)     func setCcRecipients(_ ccRecipients: [String]?)     func setBccRecipients(_ bccRecipients: [String]?)     func setMessageBody(_ body: String, isHTML isHTML: Bool)     func addAttachmentData(_ attachment: Data, mimeType mimeType: String, fileName filename: String) } ``` |

Modified [MFMailComposeViewController.addAttachmentData(_: Data, mimeType: String, fileName: String)](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/1616885-addattachmentdata)

|  | Declaration |
| --- | --- |
| From | ``` func addAttachmentData(_ attachment: NSData, mimeType mimeType: String, fileName filename: String) ``` |
| To | ``` func addAttachmentData(_ attachment: Data, mimeType mimeType: String, fileName filename: String) ``` |

Modified [MFMailComposeViewControllerDelegate](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol MFMailComposeViewControllerDelegate : NSObjectProtocol {     optional func mailComposeController(_ controller: MFMailComposeViewController, didFinishWithResult result: MFMailComposeResult, error error: NSError?) } ``` |
| To | ``` protocol MFMailComposeViewControllerDelegate : NSObjectProtocol {     optional func mailComposeController(_ controller: MFMailComposeViewController, didFinishWith result: MFMailComposeResult, error error: Error?) } ``` |

Modified [MFMailComposeViewControllerDelegate.mailComposeController(_: MFMailComposeViewController, didFinishWith: MFMailComposeResult, error: Error?)](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontrollerdelegate/1616880-mailcomposecontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func mailComposeController(_ controller: MFMailComposeViewController, didFinishWithResult result: MFMailComposeResult, error error: NSError?) ``` |
| To | ``` optional func mailComposeController(_ controller: MFMailComposeViewController, didFinishWith result: MFMailComposeResult, error error: Error?) ``` |

Modified [MFMessageComposeViewController](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class MFMessageComposeViewController : UINavigationController {     class func canSendText() -> Bool     class func canSendSubject() -> Bool     class func canSendAttachments() -> Bool     class func isSupportedAttachmentUTI(_ uti: String) -> Bool     unowned(unsafe) var messageComposeDelegate: MFMessageComposeViewControllerDelegate?     func disableUserAttachments()     var recipients: [String]?     var body: String?     var subject: String?     var attachments: [[NSObject : AnyObject]]? { get }     func addAttachmentURL(_ attachmentURL: NSURL, withAlternateFilename alternateFilename: String?) -> Bool     func addAttachmentData(_ attachmentData: NSData, typeIdentifier uti: String, filename filename: String) -> Bool } ``` |
| To | ``` class MFMessageComposeViewController : UINavigationController {     class func canSendText() -> Bool     class func canSendSubject() -> Bool     class func canSendAttachments() -> Bool     class func isSupportedAttachmentUTI(_ uti: String) -> Bool     unowned(unsafe) var messageComposeDelegate: MFMessageComposeViewControllerDelegate?     func disableUserAttachments()     var recipients: [String]?     var body: String?     var subject: String?     var attachments: [[AnyHashable : Any]]? { get }     @NSCopying var message: MSMessage?     func addAttachmentURL(_ attachmentURL: URL, withAlternateFilename alternateFilename: String?) -> Bool     func addAttachmentData(_ attachmentData: Data, typeIdentifier uti: String, filename filename: String) -> Bool } ``` |

Modified [MFMessageComposeViewController.addAttachmentData(_: Data, typeIdentifier: String, filename: String) -> Bool](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/1614069-addattachmentdata)

|  | Declaration |
| --- | --- |
| From | ``` func addAttachmentData(_ attachmentData: NSData, typeIdentifier uti: String, filename filename: String) -> Bool ``` |
| To | ``` func addAttachmentData(_ attachmentData: Data, typeIdentifier uti: String, filename filename: String) -> Bool ``` |

Modified [MFMessageComposeViewController.addAttachmentURL(_: URL, withAlternateFilename: String?) -> Bool](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/1614078-addattachmenturl)

|  | Declaration |
| --- | --- |
| From | ``` func addAttachmentURL(_ attachmentURL: NSURL, withAlternateFilename alternateFilename: String?) -> Bool ``` |
| To | ``` func addAttachmentURL(_ attachmentURL: URL, withAlternateFilename alternateFilename: String?) -> Bool ``` |

Modified [MFMessageComposeViewController.attachments](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/1614066-attachments)

|  | Declaration |
| --- | --- |
| From | ``` var attachments: [[NSObject : AnyObject]]? { get } ``` |
| To | ``` var attachments: [[AnyHashable : Any]]? { get } ``` |

Modified [MFMessageComposeViewControllerDelegate](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol MFMessageComposeViewControllerDelegate : NSObjectProtocol {     func messageComposeViewController(_ controller: MFMessageComposeViewController, didFinishWithResult result: MessageComposeResult) } ``` |
| To | ``` protocol MFMessageComposeViewControllerDelegate : NSObjectProtocol {     func messageComposeViewController(_ controller: MFMessageComposeViewController, didFinishWith result: MessageComposeResult) } ``` |

Modified [MFMessageComposeViewControllerDelegate.messageComposeViewController(_: MFMessageComposeViewController, didFinishWith: MessageComposeResult)](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontrollerdelegate/1614061-messagecomposeviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` func messageComposeViewController(_ controller: MFMessageComposeViewController, didFinishWithResult result: MessageComposeResult) ``` |
| To | ``` func messageComposeViewController(_ controller: MFMessageComposeViewController, didFinishWith result: MessageComposeResult) ``` |

Modified [NSNotification.Name.MFMessageComposeViewControllerTextMessageAvailabilityDidChange](https://developer.apple.com/documentation/foundation/nsnotification/name/1614064-mfmessagecomposeviewcontrollerte)

|  | Name | Declaration |
| --- | --- | --- |
| From | MFMessageComposeViewControllerTextMessageAvailabilityDidChangeNotification | ``` let MFMessageComposeViewControllerTextMessageAvailabilityDidChangeNotification: String ``` |
| To | MFMessageComposeViewControllerTextMessageAvailabilityDidChange | ``` static let MFMessageComposeViewControllerTextMessageAvailabilityDidChange: NSNotification.Name ``` |

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
