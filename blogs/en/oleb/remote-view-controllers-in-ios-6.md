---
title: Remote View Controllers in iOS 6
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/10/remote-view-controllers-in-ios-6/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:ff4f8bd576192ef1'
translated: false
---

> 原文：[Remote View Controllers in iOS 6](https://oleb.net/blog/2012/10/remote-view-controllers-in-ios-6/)　·　Ole Begemann

# Remote View Controllers in iOS 6

In my [previous article on sharing in iOS 6](https://oleb.net/blog/2012/09/the-state-of-sharing-in-ios-6/), I hinted at the possibility that Apple was working on a more powerful method to enable sharing between apps without compromising the iOS security architecture.

In fact, Apple is already using a new undocumented concept called _Remote View Controllers_ in iOS 6. This post is an attempt at investigating what is going on under the hood in iOS 6 and what this may mean for future versions of iOS.

I first learned about the existence of remote view controllers from a tweet by Grant Paul:

> New, private iOS 6 feature Apple is using: remote view controllers. For example: the Mail compose view is now run in a separate process.

This gives us a few hints where to begin the investigation. I wrote a very simple test app that presents one of four built-in sharing screens – [E-mail](http://developer.apple.com/library/ios/#documentation/MessageUI/Reference/MFMailComposeViewController_class/Reference/Reference.html), [SMS](http://developer.apple.com/library/ios/#Documentation/MessageUI/Reference/MFMessageComposeViewController_class/Reference/Reference.html), [Twitter and Facebook](http://developer.apple.com/library/ios/#documentation/NetworkingInternet/Reference/SLComposeViewController_Class/Reference/Reference.html) – of iOS 6 on tapping a button. I use Apple’s documented APIs, which haven’t changed in iOS 6[1](#fn:1), for this purpose. For example, the code to present the e-mail sharing view looks like this:

```
- (IBAction)openMailComposer:(id)sender
{
    if (![MFMailComposeViewController canSendMail]) {
        return;
    }
    MFMailComposeViewController *controller = [[MFMailComposeViewController alloc] init];
    [controller setMailComposeDelegate:self];
    [self presentViewController:controller animated:YES completion:nil];
}
```

When we run this app and monitor the system with Activity Monitor[2](#fn:2), we notice that a new process named _MailCompositionService_ launches once the app presents the e-mail compose sheet. Further inspection of the process reveals that this process resides in `/Applications/MailCompositionService.app/` and links with `/System/Library/PrivateFrameworks/XPCObjects.framework/`.

![Activity Monitor showing the MailCompositionService that is launched in iOS 6](https://oleb.net/media/activity-monitor-mailcompositionservice-ios6.png)

<sub>Activity Monitor showing the MailCompositionService that is launched in iOS 6 when an app presents an `MFMailComposeViewController`.</sub>

![Activity Monitor showing that MailCompositionService links with XPCObjects.framework](https://oleb.net/media/activity-monitor-mailcompositionservice-xpcobjects-framework.png)

<sub>The inspection view reveals that MailCompositionService links with the private XPCObjects.framework.</sub>

You don’t even have to write a new app if you want to confirm this for yourself. Any iOS app that offers the user to share something via e-mail should show the same results. This behavior is new in iOS 6. Running the same test on an iOS 5 device will not cause any new process to be launched.

# XPC

The frameworks `MailCompositionService.app` links with are the first hint that Apple is now using [XPC](http://developer.apple.com/library/mac/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingXPCServices.html#//apple_ref/doc/uid/10000172i-SW6-SW1) on iOS. Introduced in OS X 10.7 Lion, XPC defines an API that allows processes to communicate with each other asynchronously in a very simple and efficient manner.

Another feature of XPC is that the operating system can manage the lifetime of an XPC process. A host app does not have to manually start and stop a helper service (or constantly monitor it just to be able to restart it when it crashes); the host app just opens an XPC connection to the helper service and the OS will launch it when necessary and quit it when all connections have been closed.

Apple introduced XPC in OS X for security reasons. Apps are supposed to split themselves up into separate services that each handle a security-sensitive component. For example, a web browser might split up all its network communication and its HTML/Javascript parsing components into separate XPC services. That way, these services can run with very limited permissions (no access to the file system) and won’t be able to do much damage if they get compromised.

On iOS, apps already have a very limited set of permissions. While it might not seem as useful to split up iOS apps into multiple XPC services, the XPC architecture can also be used to allow existing apps to access certain system-wide services in a more secure manner or perhaps even to allow third-party apps to share data with each other without compromising the security model of the OS.

A class dump reveals that iOS 6 indeed includes the private [XPCKit.framework](https://github.com/nst/iOS-Runtime-Headers/tree/master/PrivateFrameworks/XPCKit.framework)[3](#fn:3), [XPCObjects.framework](https://github.com/nst/iOS-Runtime-Headers/tree/master/PrivateFrameworks/XPCObjects.framework) and [XPCService.framework](https://github.com/nst/iOS-Runtime-Headers/tree/master/PrivateFrameworks/XPCService.framework), which seem to be pretty much equivalent to the XPC functionality in OS X 10.8.

# View Hierarchy Ends with `_UIRemoteView`

## E-Mail Sharing

Next, let’s investigate the view hierarchy of the e-mail compose sheet. I set a breakpoint in the `mailComposeController:didFinishWithResult:error:` delegate method to stop the app in the debugger as soon as the user taps one of the buttons in the `MFMailComposeViewController` (just before we dismiss the view controller again):

```
(lldb) po controller
(MFMailComposeViewController *) $1 = 0x1e04f6d0 <MFMailComposeViewController: 0x1e04f6d0>
```

No surprises here. The view controller is indeed an instance of `MFMailComposeViewController`. Let’s have a look at the entire view hierarchy[4](#fn:4):

```
(lldb) po [controller.view recursiveDescription]
(id) $2 = 0x1e05c2e0 'MFMailComposeViewController:0x1e04f6d0' 1 child[MFMailComposeInternalViewController:0x1e02dfd0 ] <UILayoutContainerView: 0x1e04ffe0; frame = (0 0; 320 480); autoresize = W+H; layer = <CALayer: 0x1e0500a0>>
   | <UINavigationTransitionView: 0x1d57f6a0; frame = (0 0; 320 480); clipsToBounds = YES; autoresize = W+H; layer = <CALayer: 0x1d57f770>>
   |    | <UIViewControllerWrapperView: 0x1e04f600; frame = (0 20; 320 460); autoresize = W+H; layer = <CALayer: 0x1e0241f0>>
   |    |    | 'MFMailComposeInternalViewController:0x1e02dfd0' 1 child[MFMailComposeRemoteViewController:0x1e055230 ] <UIView: 0x1e05f9a0; frame = (0 0; 320 460); autoresize = W+H; layer = <CALayer: 0x1e05fa00>>
   |    |    |    | 'MFMailComposeRemoteViewController:0x1e055230' <_UISizeTrackingView: 0x1e05c030; frame = (0 0; 320 460); clipsToBounds = YES; autoresize = W+H; layer = <CALayer: 0x1e05c110>>
   |    |    |    |    | <_UIRemoteView: 0x1e05c300; frame = (0 0; 320 480); transform = [0.5, -0, 0, 0.5, -0, 0]; userInteractionEnabled = NO; layer = <CALayerHost: 0x1e05c460>>
```

Now that’s interesting. The view (controller) hierarchy consists of an [`MFMailComposeInternalViewController`](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/MessageUI.framework/MFMailComposeInternalViewController.h) at the top and goes down to an [`MFMailComposeRemoteViewController`](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/MessageUI.framework/MFMailComposeRemoteViewController.h), which in turn contains a [`_UIRemoteView`](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/UIKit.framework/_UIRemoteView.h). This `_UIRemoteView` is at the bottom of the view hierarchy; there is no evidence of the labels, text fields or text views that are visible in the mail composer’s user interface (which makes sense if you consider that these views now reside in a different process).

## Different Situation than in iOS 5

Compare this to the view hierarchy when the same app runs on an iOS 5 device:

```
(lldb) po controller
(MFMailComposeViewController *) $1 = 0x07ea0420 <MFMailComposeViewController: 0x7ea0420>
(lldb) po [controller.view recursiveDescription]
(id) $2 = 0x08bb4d50 'MFMailComposeViewController:0x7ea0420' 1 child[MFMailComposeController:0x89b0220 ] <UILayoutContainerView: 0x8b97e70; frame = (0 0; 320 480); autoresize = W+H; layer = <CALayer: 0x8b97ec0>>
   | <UINavigationTransitionView: 0x89b1460; frame = (0 0; 320 480); clipsToBounds = YES; autoresize = W+H; layer = <CALayer: 0x89b1500>>
   |    | <UIViewControllerWrapperView: 0x7e77990; frame = (0 64; 320 416); autoresize = W+H; layer = <CALayer: 0x7e98af0>>
   |    |    | 'MFMailComposeController:0x89b0220' <MFMailComposeView: 0x89b4410; baseClass = UITransitionView; frame = (0 0; 320 416); clipsToBounds = YES; autoresize = W+H; layer = <CALayer: 0x89b4530>>
   |    |    |    | <UIView: 0x89b1d50; frame = (0 0; 320 416); autoresize = W+H; layer = <CALayer: 0x898d130>>
   |    |    |    |    | <MFComposeScrollView: 0x89b4780; baseClass = UIScrollView; frame = (0 0; 320 416); clipsToBounds = YES; autoresize = W+H; layer = <CALayer: 0x89b4940>; contentOffset: {0, 0}>
   |    |    |    |    |    | <UIView: 0x89b56d0; frame = (0 0; 320 132); clipsToBounds = YES; autoresize = W; layer = <CALayer: 0x89b5700>>
   |    |    |    |    |    |    | <MFMailComposeRecipientView: 0x89b5d70; frame = (0 0; 320 44); text = ''; autoresize = W; layer = <CALayer: 0x89b5e70>>
   |    |    |    |    |    |    |    | <UIView: 0x89b5500; frame = (0 43; 320 1); autoresize = W; layer = <CALayer: 0x89b5e40>>
   |    |    |    |    |    |    |    | <_MFMailRecipientTextField: 0x89b5fe0; baseClass = UITextField; frame = (45 12; 275 25); text = ''; clipsToBounds = YES; opaque = NO; autoresize = W; layer = <CALayer: 0x89b4f30>>
   |    |    |    |    |    |    |    | <MFHeaderLabelView: 0x89b9350; frame = (8 10; 25 21); autoresize = RM+BM; layer = <CALayer: 0x89b9510>>
   |    |    |    |    |    |    | XX (<MFMailComposeRecipientView: 0x89bc020; frame = (0 44; 320 44); text = ''; alpha = 0; autoresize = W; layer = <CALayer: 0x89bc0b0>>)
   |    |    |    |    |    |    |    | XX (<UIView: 0x89bc100; frame = (0 43; 320 1); autoresize = W; layer = <CALayer: 0x89bc130>>)
   |    |    |    |    |    |    |    | XX (<_MFMailRecipientTextField: 0x89bc240; baseClass = UITextField; frame = (46 12; 274 25); text = ''; clipsToBounds = YES; opaque = NO; autoresize = W; layer = <CALayer: 0x89bc360>>)
   |    |    |    |    |    |    |    | XX (<MFHeaderLabelView: 0x89b6420; frame = (8 10; 26 21); autoresize = RM+BM; layer = <CALayer: 0x89b7d80>>)
   |    |    |    |    |    |    | XX (<MFMailComposeRecipientView: 0x89bd9a0; frame = (0 44; 320 44); text = ''; alpha = 0; autoresize = W; layer = <CALayer: 0x89bda30>>)
   |    |    |    |    |    |    |    | XX (<UIView: 0x89bda80; frame = (0 43; 320 1); autoresize = W; layer = <CALayer: 0x89bdab0>>)
   |    |    |    |    |    |    |    | XX (<_MFMailRecipientTextField: 0x89bdbc0; baseClass = UITextField; frame = (54 12; 266 25); text = ''; clipsToBounds = YES; opaque = NO; autoresize = W; layer = <CALayer: 0x89bdce0>>)
   |    |    |    |    |    |    |    | XX (<MFHeaderLabelView: 0x89bede0; frame = (8 10; 34 21); autoresize = RM+BM; layer = <CALayer: 0x89bee20>>)
   |    |    |    |    |    |    | XX (<MFComposeFromView: 0x89bf580; frame = (0 44; 320 44); alpha = 0; autoresize = W; layer = <CALayer: 0x89bf620>>)
   |    |    |    |    |    |    |    | XX (<UIView: 0x89bf7b0; frame = (0 43; 320 1); autoresize = W; layer = <CALayer: 0x89bf7e0>>)
   |    |    |    |    |    |    |    | XX (<MFHeaderLabelView: 0x89bf520; frame = (8 10; 45 21); autoresize = RM+BM; layer = <CALayer: 0x89bfd10>>)
   |    |    |    |    |    |    |    | XX (<UITextLabel: 0x89d2e70; frame = (57 9; 263 25); text = 'Example User <example@me....'; clipsToBounds = YES; autoresize = W; userInteractionEnabled = NO; layer = <CALayer: 0x89d2f10>>)
   |    |    |    |    |    |    | <MFComposeSubjectView: 0x89bffa0; frame = (0 88; 320 44); autoresize = W; layer = <CALayer: 0x89c0020>>
   |    |    |    |    |    |    |    | <UIView: 0x89c01b0; frame = (0 43; 320 1); autoresize = W; layer = <CALayer: 0x89c01e0>>
   |    |    |    |    |    |    |    | <MFHeaderLabelView: 0x89bff20; frame = (8 10; 62 21); autoresize = RM+BM; layer = <CALayer: 0x89bff60>>
   |    |    |    |    |    |    |    | <UITextField: 0x89c0710; frame = (76 12; 236 25); clipsToBounds = YES; opaque = NO; layer = <CALayer: 0x89bfff0>>
   |    |    |    |    |    |    | <MFComposeMultiView: 0x7e97270; frame = (0 44; 320 44); autoresize = W; layer = <CALayer: 0x7e97320>>
   |    |    |    |    |    |    |    | <UIView: 0x7e97500; frame = (0 43; 320 1); autoresize = W; layer = <CALayer: 0x7e97530>>
   |    |    |    |    |    |    |    | <MFHeaderLabelView: 0x7e97700; frame = (8 10; 59 21); autoresize = RM+BM; layer = <CALayer: 0x7e97740>>
   |    |    |    |    |    |    |    | <UILabel: 0x7e97770; frame = (73 9; 239 25); clipsToBounds = YES; userInteractionEnabled = NO; layer = <CALayer: 0x7e978c0>>
   |    |    |    |    |    | <MFComposeTextContentView: 0x89cf930; baseClass = UITextContentView; frame = (0 132; 320 284); text = '

Sent from my iPhone'; autoresize = W+H; layer = <CALayer: 0x8bae120>>
   |    |    |    |    |    |    | <MFComposeBodyField: 0x832f200; baseClass = UIWebDocumentView; frame = (0 0; 320 284); text = '

Sent from my iPhone'; opaque = NO; layer = <UIWebLayer: 0x7e988e0>>
   |    |    |    |    |    |    |    | <TileHostLayer: 0x89b2d70> (layer)
   |    |    |    |    |    |    |    |    | <TileLayer: 0x7e985c0> (layer)
   |    |    |    |    |    | XX (<UIImageView: 0x8dc6cc0; frame = (1 408; 318 7); alpha = 0; opaque = NO; autoresize = TM; userInteractionEnabled = NO; layer = <CALayer: 0x8dc6d30>>) - (null)
   |    |    |    |    |    | XX (<UIImageView: 0x8dc6d60; frame = (312 1; 7 384); alpha = 0; opaque = NO; autoresize = LM; userInteractionEnabled = NO; animations = { opacity=<CABasicAnimation: 0x89cea00>; }; layer = <CALayer: 0x8dc6dd0>>) - (null)
   | <UINavigationBar: 0x89b04f0; frame = (0 20; 320 44); autoresize = W; layer = <CALayer: 0x89b0a80>>
   |    | <UINavigationBarBackground: 0x89b0cb0; frame = (0 0; 320 44); opaque = NO; userInteractionEnabled = NO; layer = <CALayer: 0x89b0d40>> - (null)
   |    | <UINavigationItemView: 0x89b11d0; frame = (93 8; 133 27); opaque = NO; userInteractionEnabled = NO; layer = <CALayer: 0x89b1220>>
   |    | <UINavigationButton: 0x89b1bf0; frame = (5 7; 60 30); opaque = NO; layer = <CALayer: 0x89b1d80>>
   |    |    | <UIImageView: 0x89b2590; frame = (0 0; 60 30); clipsToBounds = YES; opaque = NO; userInteractionEnabled = NO; layer = <CALayer: 0x89b25d0>> - (null)
   |    |    | <UIButtonLabel: 0x89b20e0; frame = (10 7; 40 15); text = 'Cancel'; clipsToBounds = YES; opaque = NO; userInteractionEnabled = NO; layer = <CALayer: 0x89b2150>>
   |    | <UINavigationButton: 0x89b2020; frame = (265 7; 50 30); opaque = NO; layer = <CALayer: 0x89b1ae0>>
   |    |    | <UIImageView: 0x89b1020; frame = (0 0; 50 30); clipsToBounds = YES; opaque = NO; userInteractionEnabled = NO; layer = <CALayer: 0x89b2b00>> - (null)
   |    |    | <UIButtonLabel: 0x89b1560; frame = (10 7; 30 15); text = 'Send'; clipsToBounds = YES; opaque = NO; userInteractionEnabled = NO; layer = <CALayer: 0x89b15d0>>
```

The view hierarchy is a lot longer and does include all the labels and text views we would expect of a mail composition UI. As we have seen, the public API has remained the same while the underlying implementation has completely changed. If your app currently goes around the public API of `MFMailComposeViewController` and tries to access certain subviews directly, you’ll probably already have noticed that it no longer works as intended in iOS 6. (And there doesn’t seem to be a quick and easy way to make such a hack work again.)

## Facebook Sharing

We get a very similar result when we present a Facebook sharing sheet in iOS 6. Activity Monitor shows that a new process, `SocialUIService`, gets launched. And the view (controller) hierarchy looks like this:

```
(lldb) po [[[[UIApplication sharedApplication] keyWindow] rootViewController] presentedViewController]
(id) $1 = 0x1d545a10 <SLFacebookComposeViewController: 0x1d545a10>
(lldb) po [[[[[[UIApplication sharedApplication] keyWindow] rootViewController] presentedViewController] view] recursiveDescription]
(id) $2 = 0x1e02b4f0 'SLFacebookComposeViewController:0x1d545a10' 1 child[SLFacebookRemoteComposeViewController:0x1d5404b0 ] <UIView: 0x1d547f90; frame = (0 20; 320 460); opaque = NO; autoresize = W+H; layer = <CALayer: 0x1d57efa0>>
   | 'SLFacebookRemoteComposeViewController:0x1d5404b0' <_UISizeTrackingView: 0x1d586c00; frame = (0 0; 320 460); clipsToBounds = YES; autoresize = W+H; layer = <CALayer: 0x1d586c60>>
   |    | <_UIRemoteView: 0x1d586ce0; frame = (0 0; 320 480); transform = [0.5, -0, 0, 0.5, -0, 0]; userInteractionEnabled = NO; layer = <CALayerHost: 0x1d586d40>>
```

[`SLFacebookComposeViewController`](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/Social.framework/SLFacebookComposeViewController.h) has only one child, [`SLFacebookRemoteComposeViewController`](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/Social.framework/SLFacebookRemoteComposeViewController.h), which again hosts a `_UIRemoteView`. We have no information about the contents of the remote view.

## Twitter Sharing Not Yet Converted to XPC

Interestingly, I could _not_ observe a similar behavior when presenting the Tweet compose sheet with `SLComposeViewController`. While the Tweet compose sheet also causes a new process, `twitterd`, to launch, the view hierarchy includes all the expected subviews and no traces of `_UIRemoteView`.

I assume the task of `twitterd` is only to manage access to the Twitter accounts defined in iOS Settings. I suppose Apple has not yet converted the Tweet compose sheet to the new remote view controller pattern.

# A Closer Look At MailCompositionService

Let’s see what we can find out about these new processes that show up in Activity Monitor. Their binaries for the iOS Simulator are located in `/Applications/­Xcode.app/­Contents/­Developer/­Platforms/­iPhoneSimulator.platform/­Developer/­SDKs/­iPhoneSimulator6.0.sdk/­Applications`. In that directory, we find `MailCompositionService.app`, `MessagesViewService.app` (for the SMS/iMessage compose sheet), `SocialUIService.app` (for social sharing like Facebook, presumably SinaWeibo and, in the future, Twitter).

A [class dump of `MailCompositionService.app`](https://gist.github.com/3813291) reveals the following classes and protocols:

- and

  protocols
- , a

  subclass.
- , a

  subclass that implements, among others, the

  protocol. This class contains an ivar

  .

Without going into too much detail, it seems clear that the host app and the service set up proxy objects on either side of the process boundary. These proxy objects use XPC to communicate with each other. The two protocols, `MFMailComposeRemoteService` and `MFMailComposeRemoteHost`, define what messages can be sent in each direction.

The host app can initialize the data shown in the mail compose sheet, using messages like `setCompositionValues:`, `setUICustomizationData:` and `addAttachmentData:mimeType:fileName:identifier:` defined in `MFMailComposeRemoteService`. In turn, the MailCompositionService can signal its host app with the messages `bodyFinishedDrawing` and `compositionFinishedWithResult:error:` defined in `MFMailComposeRemoteHost`.

## Other Services

A class dump of the other processes I found in the simulator’s `/Applications` folder did not prove as fruitful as the MailCompositionService. Most of the other services did not reveal new classes or protocols that were modeled after the MailCompositionService example. I do not know whether this is because Apple’s implementation is not yet complete or due to a limitation of the iOS Simulator or due to an error on my part.

**Update October 5, 2012** After further investigation, I found out the reason for this observation. In many cases, the view controllers that are instantiated by the remote XPC services are already present in Apple’s iOS 6 frameworks and therefore do not have to be part of the XPC service binaries themselves. For instance, the `CK­SMS­Compose­Remote­View­Controller` class that is used to display an SMS/iMessage compose UI is part of the private ChatKit.framework rather than residing directly in Messages­View­Service.app.

As such, MailCompositionService.app is an exception as `Compose­Service­Remote­View­Controller` is _not_ part of MessageUI.framework. [The list of all remote view controllers I found](https://oleb.net/blog/2012/10/more-on-remote-view-controllers/) in part 2 of this series has the details.

## ShoeboxUISerice and WebViewService

Two other services are worth noting. I suppose `ShoeboxUIService.app` is used to present a Passbook UI in Safari and Mail when a user downloads or receives a pass (Shoebox was Apple’s code name for Passbook).

The presence of `WebViewService.app` suggests that Apple is also working on a remote process model for presenting a `UIWebView` from an app. This functionality could potentially mean that web views used by third-party apps would no longer have a performance disadvantage when compared against Mobile Safari due to Apple’s [disabling of Javascript just-in-time compilation in all apps except Safari for security reasons](http://daringfireball.net/2011/03/nitro_ios_43).

A further hint at such a feature is the presence of the private [`_UIRemoteWebViewController`](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/UIKit.framework/_UIRemoteWebViewController.h) class in the iOS 6 class dump. However, in my experiments I was not able to instantiate a remote web view.

# _UIRemoteViewController

`MFMailComposeRemoteViewController` and `SLFacebookRemoteComposeViewController`, the classes we saw in the view controller hierarchy above, both inherit from the private [`_UIRemoteViewController`](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/UIKit.framework/_UIRemoteViewController.h) class. I assume this class is one of the central elements of the remote view controller design. Looking at its interface, there is one class method that likely plays a big part in setting everything up:

```
+ (id)requestViewController:(id)arg1 fromServiceWithBundleIdentifier:(id)arg2 connectionHandler:(id)arg3;
```

I [swizzled](http://www.mikeash.com/pyblog/friday-qa-2010-01-29-method-replacement-for-fun-and-profit.html) this method in my test app to be able to set a breakpoint and look at the three arguments and the method’s return value. This is what I found:

![Xcode debugger showing call stack for MFMailComposeViewController](https://oleb.net/media/xcode-call-stack-mfmailcomposeviewcontroller-ios6.png)

<sub>The call stack in Xcode's debugger after we presented an `MFMailComposeViewController` on screen. Note that `MFMailComposeViewController` directly calls `requestViewController:fromServiceWithBundleIdentifier:connectionHandler:` to create the remote view controller and initiate the XPC process.</sub>

Have a look at the call stack above. My method `-[ViewController openMailComposer:]` creates the `MFMailComposeViewController` and presents it on screen. This leads directly to the creation of an `MFMailComposeIntervalViewController`, whose init method then calls the class method we have been looking for with these arguments:

```
[MFMailComposeRemoteViewController
                      requestViewController:@"ComposeServiceRemoteViewController"
            fromServiceWithBundleIdentifier:@"com.apple.MailCompositionService"
                          connectionHandler:<__NSStackBlock__: 0xbfffdc20>];
```

This fits our other findings perfectly. `@"com.apple.MailCompositionService"` is the bundle id of `MailCompositionService.app` and `@"ComposeServiceRemoteViewController"` is the name of the class the remote service should instantiate. The third argument is obviously a block that will be called by the XPC frameworks when the connection is established and/or when a new message from the remote service arrives.

# Dead End

The return value of `+requestViewController:­fromServiceWithBundleIdentifier:­connectionHandler:` is a [`_UIAsyncInvocation`](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/UIKit.framework/_UIAsyncInvocation.h) instance. Unfortunately, I could not find out much about the purpose of this class. It looks like a variant of [`NSInvocation`](https://developer.apple.com/library/ios/#documentation/Cocoa/Reference/Foundation/Classes/NSInvocation_Class/Reference/Reference.html) for asynchronous operations that want to notify some other object about their progress.

If I use the debugger to send an `invoke` message to this `_UIAsyncInvocation`, it returns a [`_UIAsyncInvocationObserver`](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/UIKit.framework/_UIAsyncInvocationObserver.h) instance. What this observer’s purpose is, I don’t know.

**Update October 5, 2012** I now believe the `_UIAsyncInvocation` can be used by the caller of the method to cancel the XPC connection prematurely. [Read more on this in part 2](https://oleb.net/blog/2012/10/more-on-remote-view-controllers/).

This is where I ran into a dead end with my experiments. Since I was not able to find out more about the signature of the connection handler block or the purpose of the method’s return value, I did not succeed in manually invoking a remote view controller. There are also other classes, such as [`_UIRemoteViewControllerConnectionRequest`](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/UIKit.framework/_UIRemoteViewControllerConnectionRequest.h), that need to be investigated closer. However, I am reasonably sure that I am on the right track.

# Outlook for iOS 7

Remote view controllers are an exciting new feature for iOS. I sincerely hope that Apple will use this technology in iOS 7 to enhance data sharing and communication between third-party apps without compromising the iOS security model. [We need it](https://oleb.net/blog/2012/02/what-ios-should-learn-from-android-and-windows-8/).

How could this work? Apple could ask developers who want to provide a sharing UI to other apps to include a second executable in their app bundle. This executable would be an XPC service that looks a lot like the `MailCompositionService.app` we analyzed above. Its main component would be a stand-alone view controller that was able to communicate via XPC and implemented some standard Apple-defined protocols named something like `UISharingRemoteHost` and `UISharingRemoteService`.

Apple’s existing `UIActivityViewController` would then maintain a list of registered sharing services and present these options to the user.

I hope we will see something like this next year.

**Update October 5, 2012:** [Continue reading about my remote view controller research in part 2 of this series](https://oleb.net/blog/2012/10/more-on-remote-view-controllers/).

1. In fact, the recommended way to present a Tweet compose UI _has_ changed slightly, as Twitter sharing is now incorporated in the Social.framework. The new `SLComposeViewController` class is to be used for sharing to all supported social services and should be preferred over the old `TWTweetComposeViewController`. However, this detail is not relevant to the rest of this investigation. [↩︎](#fnref:1)
2. You can either run the app on the iOS Simulator and use OS X’s Activity Monitor to watch what happens or attach Instruments (with the Activity Monitor instrument) to your device and run the app on the device. Both methods yield the same results. [↩︎](#fnref:2)
3. My links to the private and undocumented frameworks and APIs in iOS 6 point to Nicolas Seriot’s excellent [class dump of the iOS SDK’s Objective-C headers](https://github.com/nst/iOS-Runtime-Headers). These files have proven incredibly useful in the research for this article. [↩︎](#fnref:3)
4. I used Peter Steinberger’s [pimped version of `recursiveDescription`](http://petersteinberger.com/blog/2012/pimping-recursivedescription/) to log the view hierarchy in the debugger. Peter’s version has the advantage over [Apple’s own `recursiveDescription`](http://developer.apple.com/library/ios/technotes/tn2239/_index.html#//apple_ref/doc/uid/DTS40010638-CH1-SUBSECTION34) that it also outputs view _controllers_, not just views. [↩︎](#fnref:4)
