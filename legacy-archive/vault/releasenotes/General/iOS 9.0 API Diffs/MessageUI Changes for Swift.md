---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/MessageUI.html
archived_at: '2026-07-18T02:56:54.989391Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# MessageUI Changes for Swift

### MessageUI

Removed MessageComposeResult.valueRemoved MFMailComposeErrorCode.valueRemoved MFMailComposeResult.valueAdded MessageComposeResult.init(rawValue: UInt32)Added MessageComposeResult.rawValueAdded MFMailComposeErrorCode.init(rawValue: UInt32)Added MFMailComposeErrorCode.rawValueAdded MFMailComposeResult.init(rawValue: UInt32)Added MFMailComposeResult.rawValueModified [MessageComposeResult [struct]](https://developer.apple.com/documentation/messageui/messagecomposeresult)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MessageComposeResult {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct MessageComposeResult : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [MFMailComposeErrorCode [struct]](https://developer.apple.com/documentation/messageui/mfmailcomposeerrorcode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MFMailComposeErrorCode {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct MFMailComposeErrorCode : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [MFMailComposeResult [struct]](https://developer.apple.com/documentation/messageui/mfmailcomposeresult)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MFMailComposeResult {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct MFMailComposeResult : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [MFMailComposeViewController](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class MFMailComposeViewController : UINavigationController {     class func canSendMail() -> Bool     unowned(unsafe) var mailComposeDelegate: MFMailComposeViewControllerDelegate!     func setSubject(_ subject: String!)     func setToRecipients(_ toRecipients: [AnyObject]!)     func setCcRecipients(_ ccRecipients: [AnyObject]!)     func setBccRecipients(_ bccRecipients: [AnyObject]!)     func setMessageBody(_ body: String!, isHTML isHTML: Bool)     func addAttachmentData(_ attachment: NSData!, mimeType mimeType: String!, fileName filename: String!) } ``` |
| To | ``` class MFMailComposeViewController : UINavigationController {     class func canSendMail() -> Bool     unowned(unsafe) var mailComposeDelegate: MFMailComposeViewControllerDelegate?     func setSubject(_ subject: String)     func setToRecipients(_ toRecipients: [String]?)     func setCcRecipients(_ ccRecipients: [String]?)     func setBccRecipients(_ bccRecipients: [String]?)     func setMessageBody(_ body: String, isHTML isHTML: Bool)     func addAttachmentData(_ attachment: NSData, mimeType mimeType: String, fileName filename: String) } ``` |

Modified [MFMailComposeViewController.addAttachmentData(_: NSData, mimeType: String, fileName: String)](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/1616885-addattachmentdata)

|  | Declaration |
| --- | --- |
| From | ``` func addAttachmentData(_ attachment: NSData!, mimeType mimeType: String!, fileName filename: String!) ``` |
| To | ``` func addAttachmentData(_ attachment: NSData, mimeType mimeType: String, fileName filename: String) ``` |

Modified [MFMailComposeViewController.mailComposeDelegate](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/1616890-mailcomposedelegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var mailComposeDelegate: MFMailComposeViewControllerDelegate! ``` |
| To | ``` unowned(unsafe) var mailComposeDelegate: MFMailComposeViewControllerDelegate? ``` |

Modified [MFMailComposeViewController.setBccRecipients(_: [String]?)](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/1616887-setbccrecipients)

|  | Declaration |
| --- | --- |
| From | ``` func setBccRecipients(_ bccRecipients: [AnyObject]!) ``` |
| To | ``` func setBccRecipients(_ bccRecipients: [String]?) ``` |

Modified [MFMailComposeViewController.setCcRecipients(_: [String]?)](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/1616889-setccrecipients)

|  | Declaration |
| --- | --- |
| From | ``` func setCcRecipients(_ ccRecipients: [AnyObject]!) ``` |
| To | ``` func setCcRecipients(_ ccRecipients: [String]?) ``` |

Modified [MFMailComposeViewController.setMessageBody(_: String, isHTML: Bool)](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/1616881-setmessagebody)

|  | Declaration |
| --- | --- |
| From | ``` func setMessageBody(_ body: String!, isHTML isHTML: Bool) ``` |
| To | ``` func setMessageBody(_ body: String, isHTML isHTML: Bool) ``` |

Modified [MFMailComposeViewController.setSubject(_: String)](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/1616874-setsubject)

|  | Declaration |
| --- | --- |
| From | ``` func setSubject(_ subject: String!) ``` |
| To | ``` func setSubject(_ subject: String) ``` |

Modified [MFMailComposeViewController.setToRecipients(_: [String]?)](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/1616872-settorecipients)

|  | Declaration |
| --- | --- |
| From | ``` func setToRecipients(_ toRecipients: [AnyObject]!) ``` |
| To | ``` func setToRecipients(_ toRecipients: [String]?) ``` |

Modified [MFMailComposeViewControllerDelegate](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol MFMailComposeViewControllerDelegate : NSObjectProtocol {     optional func mailComposeController(_ controller: MFMailComposeViewController!, didFinishWithResult result: MFMailComposeResult, error error: NSError!) } ``` |
| To | ``` protocol MFMailComposeViewControllerDelegate : NSObjectProtocol {     optional func mailComposeController(_ controller: MFMailComposeViewController, didFinishWithResult result: MFMailComposeResult, error error: NSError?) } ``` |

Modified [MFMailComposeViewControllerDelegate.mailComposeController(_: MFMailComposeViewController, didFinishWithResult: MFMailComposeResult, error: NSError?)](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontrollerdelegate/1616880-mailcomposecontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func mailComposeController(_ controller: MFMailComposeViewController!, didFinishWithResult result: MFMailComposeResult, error error: NSError!) ``` |
| To | ``` optional func mailComposeController(_ controller: MFMailComposeViewController, didFinishWithResult result: MFMailComposeResult, error error: NSError?) ``` |

Modified [MFMessageComposeViewController](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class MFMessageComposeViewController : UINavigationController {     class func canSendText() -> Bool     class func canSendSubject() -> Bool     class func canSendAttachments() -> Bool     class func isSupportedAttachmentUTI(_ uti: String!) -> Bool     unowned(unsafe) var messageComposeDelegate: MFMessageComposeViewControllerDelegate!     func disableUserAttachments()     var recipients: [AnyObject]!     var body: String!     var subject: String!     var attachments: [AnyObject]! { get }     func addAttachmentURL(_ attachmentURL: NSURL!, withAlternateFilename alternateFilename: String!) -> Bool     func addAttachmentData(_ attachmentData: NSData!, typeIdentifier uti: String!, filename filename: String!) -> Bool } ``` |
| To | ``` class MFMessageComposeViewController : UINavigationController {     class func canSendText() -> Bool     class func canSendSubject() -> Bool     class func canSendAttachments() -> Bool     class func isSupportedAttachmentUTI(_ uti: String) -> Bool     unowned(unsafe) var messageComposeDelegate: MFMessageComposeViewControllerDelegate?     func disableUserAttachments()     var recipients: [String]?     var body: String?     var subject: String?     var attachments: [[NSObject : AnyObject]]? { get }     func addAttachmentURL(_ attachmentURL: NSURL, withAlternateFilename alternateFilename: String?) -> Bool     func addAttachmentData(_ attachmentData: NSData, typeIdentifier uti: String, filename filename: String) -> Bool } ``` |

Modified [MFMessageComposeViewController.addAttachmentData(_: NSData, typeIdentifier: String, filename: String) -> Bool](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/1614069-addattachmentdata)

|  | Declaration |
| --- | --- |
| From | ``` func addAttachmentData(_ attachmentData: NSData!, typeIdentifier uti: String!, filename filename: String!) -> Bool ``` |
| To | ``` func addAttachmentData(_ attachmentData: NSData, typeIdentifier uti: String, filename filename: String) -> Bool ``` |

Modified [MFMessageComposeViewController.addAttachmentURL(_: NSURL, withAlternateFilename: String?) -> Bool](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/1614078-addattachmenturl)

|  | Declaration |
| --- | --- |
| From | ``` func addAttachmentURL(_ attachmentURL: NSURL!, withAlternateFilename alternateFilename: String!) -> Bool ``` |
| To | ``` func addAttachmentURL(_ attachmentURL: NSURL, withAlternateFilename alternateFilename: String?) -> Bool ``` |

Modified [MFMessageComposeViewController.attachments](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/1614066-attachments)

|  | Declaration |
| --- | --- |
| From | ``` var attachments: [AnyObject]! { get } ``` |
| To | ``` var attachments: [[NSObject : AnyObject]]? { get } ``` |

Modified [MFMessageComposeViewController.body](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/1614060-body)

|  | Declaration |
| --- | --- |
| From | ``` var body: String! ``` |
| To | ``` var body: String? ``` |

Modified [MFMessageComposeViewController.isSupportedAttachmentUTI(_: String) -> Bool [class]](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/1614075-issupportedattachmentuti)

|  | Declaration |
| --- | --- |
| From | ``` class func isSupportedAttachmentUTI(_ uti: String!) -> Bool ``` |
| To | ``` class func isSupportedAttachmentUTI(_ uti: String) -> Bool ``` |

Modified [MFMessageComposeViewController.messageComposeDelegate](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/1614070-messagecomposedelegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var messageComposeDelegate: MFMessageComposeViewControllerDelegate! ``` |
| To | ``` unowned(unsafe) var messageComposeDelegate: MFMessageComposeViewControllerDelegate? ``` |

Modified [MFMessageComposeViewController.recipients](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/1614071-recipients)

|  | Declaration |
| --- | --- |
| From | ``` var recipients: [AnyObject]! ``` |
| To | ``` var recipients: [String]? ``` |

Modified [MFMessageComposeViewController.subject](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/1614062-subject)

|  | Declaration |
| --- | --- |
| From | ``` var subject: String! ``` |
| To | ``` var subject: String? ``` |

Modified [MFMessageComposeViewControllerDelegate](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol MFMessageComposeViewControllerDelegate : NSObjectProtocol {     func messageComposeViewController(_ controller: MFMessageComposeViewController!, didFinishWithResult result: MessageComposeResult) } ``` |
| To | ``` protocol MFMessageComposeViewControllerDelegate : NSObjectProtocol {     func messageComposeViewController(_ controller: MFMessageComposeViewController, didFinishWithResult result: MessageComposeResult) } ``` |

Modified [MFMessageComposeViewControllerDelegate.messageComposeViewController(_: MFMessageComposeViewController, didFinishWithResult: MessageComposeResult)](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontrollerdelegate/1614061-messagecomposeviewcontroller)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func messageComposeViewController(_ controller: MFMessageComposeViewController!, didFinishWithResult result: MessageComposeResult) ``` | iOS 8.0 |
| To | ``` func messageComposeViewController(_ controller: MFMessageComposeViewController, didFinishWithResult result: MessageComposeResult) ``` | iOS 4.0 |

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
