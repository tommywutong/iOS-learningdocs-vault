---
title: System Messaging Programming Topics for iOS
apple_id: TP40010404
resource_type: Guide
platform: iOS
topic: User Experience
technology: MessageUI
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/SystemMessaging_TopicsForIOS/Articles/SendinganSMSMessage.html
archived_at: '2026-07-18T02:12:52.037432Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [System Messaging Programming Topics for iOS](About%20System%20Messaging.md)


[Next](Document%20Revision%20History.md)[Previous](Sending%20a%20Mail%20Message.md)

# Sending an SMS Message

In iOS 4.0 and later, you can send text messages from within your application. This feature is strictly for sending messages. Incoming SMS messages go to the built-in Messages app.

To use the SMS composition interface, you must add `MessageUI.framework` to your Xcode project and link against it in any relevant targets. To access the classes and headers of the framework, include an `#import <MessageUI/MessageUI.h>` statement at the top of any relevant source files. For information on how to add frameworks to your project, see [Files in Projects](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeProjectManagement/130-Files_in_Projects/project_files.html#//apple_ref/doc/uid/TP40002666) in _[Xcode Project Management Guide](../../Developer%20Tools/Xcode%20Project%20Management%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dsmjx)_.

To provide the standard user interface for composing an SMS (Short Message Service) message, use the [MFMessageComposeViewController](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller) class. [Create an instance](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39) of this class and assign it a [delegate](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) object. The delegate must conform to the [MFMessageComposeViewControllerDelegate](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontrollerdelegate) [protocol](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45).

Before presenting the composition interface to the user, you can configure initial recipients and message content. With setup complete, call the `UIViewController`[presentModalViewController:animated:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621465-presentmodalviewcontroller) method to present the SMS message composition view controller modally.

While the interface is visible, the user can edit the recipients list and message content. The user then sends the message, or cancels it, by tapping the appropriate control in the interface.

If the user requests that the message be sent, the system queues it for delivery and invokes the delegate object’s [messageComposeViewController:didFinishWithResult:](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontrollerdelegate/1614061-messagecomposeviewcontroller) method. The result is one of “sent,” “cancelled,” or “failed.”

Finally, the delegate is responsible for dismissing the message composition view controller, which it should do by calling the `UIViewController` [dismissModalViewControllerAnimated:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621369-dismissmodalviewcontrolleranimat) method.

For a complete description of the [MFMessageComposeViewController](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller) class, see _[MFMessageComposeViewController Class Reference](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller)_.

[Next](Document%20Revision%20History.md)[Previous](Sending%20a%20Mail%20Message.md)

