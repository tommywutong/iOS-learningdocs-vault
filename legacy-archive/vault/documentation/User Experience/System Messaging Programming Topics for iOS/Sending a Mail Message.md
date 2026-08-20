---
title: System Messaging Programming Topics for iOS
apple_id: TP40010404
resource_type: Guide
platform: iOS
topic: User Experience
technology: MessageUI
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/SystemMessaging_TopicsForIOS/Articles/SendingaMailMessage.html
archived_at: '2026-07-18T02:12:51.973458Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [System Messaging Programming Topics for iOS](About%20System%20Messaging.md)


[Next](Sending%20an%20SMS%20Message.md)[Previous](About%20System%20Messaging.md)

# Sending a Mail Message

In iOS 3.0 and later, you can use the [MFMailComposeViewController](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller) class to present a standard mail composition interface inside your app. Prior to displaying the interface, you use the methods of the class to configure the email recipients, the subject, body, and any attachments you want to include. When you present the interface (using standard view controller techniques), the user has the option of editing the contents of the message before submitting it to the Mail app for delivery. The user also has the option to cancel the email altogether.

To use the mail composition interface, you must add `MessageUI.framework` to your Xcode project and link against it in any relevant targets. To access the classes and headers of the framework, include an `#import <MessageUI/MessageUI.h>` statement at the top of any relevant source files. For information on how to add frameworks to your project, see [Files in Projects](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeProjectManagement/130-Files_in_Projects/project_files.html#//apple_ref/doc/uid/TP40002666) in _[Xcode Project Management Guide](../../Developer%20Tools/Xcode%20Project%20Management%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dsmjx)_.

To use the `MFMailComposeViewController` class in your app, you [create an instance](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39) and use its methods to set the initial email data. You must also assign an object to the [mailComposeDelegate](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/1616890-mailcomposedelegate)[property](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13) of the [view controller](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11) to handle the dismissal of the interface when the user accepts or cancels the email. The [delegate object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) you specify must conform to the [MFMailComposeViewControllerDelegate](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontrollerdelegate)[protocol](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45).

When specifying email addresses for the mail composition interface, you specify plain string objects. If you want to use email addresses from the user’s list of contacts, you can use the Address Book framework to retrieve that information. For more information on how to get email and other information using this framework, see _[Address Book Programming Guide for iOS](../../Address%20Book%20Programming%20Guide%20for%20iOS/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tonbu)_.

Listing 1 shows the code for creating the `MFMailComposeViewController` object and displaying the mail composition interface modally in your app. You would include the `displayComposerSheet` method in one of your custom view controllers and call the method as needed to display the interface. In this example, the parent view controller assigns itself as the delegate and implements the [mailComposeController:didFinishWithResult:error:](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontrollerdelegate/1616880-mailcomposecontroller) method. The delegate method dismisses the delegate without taking any further actions. In your own app, you could use the delegate to track whether the user sent or canceled the email by examining the value in the _result_ parameter.

__Listing 1__  Posting the mail composition interface

```objc
@implementation WriteMyMailViewController (MailMethods)

-(void)displayComposerSheet
{
    MFMailComposeViewController *picker = [[MFMailComposeViewController alloc] init];
    picker.mailComposeDelegate = self;

    [picker setSubject:@"Hello from California!"];

    // Set up the recipients.
    NSArray *toRecipients = [NSArray arrayWithObjects:@"first@example.com",
                                   nil];
    NSArray *ccRecipients = [NSArray arrayWithObjects:@"second@example.com",
                                   @"third@example.com", nil];
    NSArray *bccRecipients = [NSArray arrayWithObjects:@"four@example.com",
                                   nil];

    [picker setToRecipients:toRecipients];
    [picker setCcRecipients:ccRecipients];
    [picker setBccRecipients:bccRecipients];

    // Attach an image to the email.
    NSString *path = [[NSBundle mainBundle] pathForResource:@"ipodnano"
                                 ofType:@"png"];
    NSData *myData = [NSData dataWithContentsOfFile:path];
    [picker addAttachmentData:myData mimeType:@"image/png"
                                 fileName:@"ipodnano"];

    // Fill out the email body text.
    NSString *emailBody = @"It is raining in sunny California!";
    [picker setMessageBody:emailBody isHTML:NO];

    // Present the mail composition interface.
    [self presentModalViewController:picker animated:YES];
    [picker release]; // Can safely release the controller now.
}

// The mail compose view controller delegate method
- (void)mailComposeController:(MFMailComposeViewController *)controller
              didFinishWithResult:(MFMailComposeResult)result
              error:(NSError *)error
{
    [self dismissModalViewControllerAnimated:YES];
}
@end
```

For more information on the standard view controller techniques for displaying interfaces, see _[View Controller Programming Guide for iOS](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457)_. For information about the classes of the Message UI framework, see _[Message UI Framework Reference](https://developer.apple.com/documentation/messageui)_.

[Next](Sending%20an%20SMS%20Message.md)[Previous](About%20System%20Messaging.md)

