---
title: More on Remote View Controllers
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/10/more-on-remote-view-controllers/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:7bfbebb78479da9b'
translated: false
---

> 原文：[More on Remote View Controllers](https://oleb.net/blog/2012/10/more-on-remote-view-controllers/)　·　Ole Begemann

# More on Remote View Controllers

A few days ago, I wrote about my research into [remote view controllers in iOS 6](https://oleb.net/blog/2012/10/remote-view-controllers-in-ios-6/). If you haven’t read that article yet, please do so first before you continue, because this post takes off where part 1 left off.

# The connectionHandler Block

Last time, we swizzled the `+requestViewController:fromServiceWithBundleIdentifier:connectionHandler:` of the undocumented [`_UIRemoteViewController`](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/UIKit.framework/_UIRemoteViewController.h) class because we (correctly) assumed it played a central role in setting up the connection between the local app and the remote XPC service. The third argument of this method was a block that we have not yet investigated closely.

Oliver Letterer [pointed me](https://twitter.com/iHubSC/statuses/253027868131602432) to his [`CTBlockDescription`](https://github.com/ebf/CTObjectiveCRuntimeAdditions/blob/master/CTObjectiveCRuntimeAdditions/CTObjectiveCRuntimeAdditions/CTBlockDescription.h) class that lets us do just that. With `CTBlockDescription`, we can introspect the block and determine the number and types of its arguments and return value. The code looks like this:

```
CTBlockDescription *blockDescription = [[CTBlockDescription alloc] initWithBlock:connectionHandlerBlock];
NSMethodSignature *blockSignature = blockDescription.blockSignature;
NSLog(@"connectionHandlerBlock signature: %@", blockSignature);
```

And this is the log output:

```
<NSMethodSignature: 0xb287dd0>
number of arguments = 3
frame size = 12
is special struct return? NO
return value: -------- -------- -------- --------
type encoding (v) 'v'
flags {}
modifiers {}
frame {offset = 0, offset adjust = 0, size = 0, size adjust = 0}
memory {offset = 0, size = 0}
argument 0: -------- -------- -------- --------
type encoding (@) '@?'
flags {isObject, isBlock}
modifiers {}
frame {offset = 0, offset adjust = 0, size = 4, size adjust = 0}
memory {offset = 0, size = 4}
argument 1: -------- -------- -------- --------
type encoding (@) '@'
flags {isObject}
modifiers {}
frame {offset = 4, offset adjust = 0, size = 4, size adjust = 0}
memory {offset = 0, size = 4}
argument 2: -------- -------- -------- --------
type encoding (@) '@'
flags {isObject}
modifiers {}
frame {offset = 8, offset adjust = 0, size = 4, size adjust = 0}
memory {offset = 0, size = 4}
```

This tells us that the block has a return type of `void` (`'v'`) and two arguments that are objects (`'@'`). With this information, we can create our own custom connection handler block and pass it to the method, letting us log the arguments that are passed to the block when it is executed. As long as we take care to call the original block from inside our own custom block, this little man-in-the-middle attack should be completely transparent to the other objects involved. The code:

```
// Create a type for the block signature we have identified
typedef void (^ConnectionHandler)(id blockArg1, id blockArg2);

// We need to copy the original block from the stack to the heap
ConnectionHandler originalBlock = [(ConnectionHandler)connectionHandlerBlock copy];

// Replace the connectionHandlerBlock with our own implementation
ConnectionHandler swizzledBlock = ^(id blockArg1, id blockArg2) {
    NSLog(@"connectionHandlerBlock called");
    NSLog(@"blockArg1: %@ %@", [blockArg1 class], blockArg1);
    NSLog(@"blockArg2: %@ %@", [blockArg2 class], blockArg2);

    // Call the original block
    originalBlock(blockArg1, blockArg2);
};
```

I had originally assumed that the connectionHandler block would be called multiple times, whenever there was a new message from the remote service. However, that is not the case. The block is only called once, presumably when the XPC connection is first established. The log output looks like this:

```
connectionHandlerBlock called
blockArg1: MFMailComposeRemoteViewController <MFMailComposeRemoteViewController: 0xb570ae0>
blockArg2: (null) (null)
```

This looks great. The first parameter that gets passed to the connectionHandler block is the instance to the concrete `_UIRemoteViewController` subclass we wanted to create. So `+[_UIRemoteViewController requestViewController:fromServiceWithBundleIdentifier:connectionHandler:]` acts like an asynchronous factory for remote view controllers. The second parameter was always `nil` in my tests (perhaps an `NSError *` object in case of failure?).

Note the naming convention here: classes with the name `…Remote…ViewController` act as the _local_ app’s interface to the view controller of the remote XPC service. So despite their name, `…Remote…ViewController`s are just normal _local_ objects. The class names of the _remote_ view controllers that run in the remote process are of no interest to us (though we need to know them because they constitute the first argument to the factory method – see [part 1](https://oleb.net/blog/2012/10/remote-view-controllers-in-ios-6/) for details).

# _UIAsyncInvocation

In [part 1](https://oleb.net/blog/2012/10/remote-view-controllers-in-ios-6/), I wondered about the purpose of the factory method’s return value, an instance of [`_UIAsyncInvocation`](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/UIKit.framework/_UIAsyncInvocation.h). I now believe that the initiator of the remote connection can use this object to cancel the XPC connection before it has been established. One piece of evidence that led me in this direction is the fact that `_UIRemoteViewController` has an instance variable named `_UIAsyncInvocation *_terminationInvocation;`.

# Logging Proxy

Now that we have access to a concrete `_UIRemoteViewController` object that clearly represents a central part in the XPC communication, it would be nice to see what messages this object receives. For this purpose, I wrote a very simple proxy class that can stand in for the remote view controller. All it does is log all messages it receives and then forward them to the actual remote view controller instance. Thanks to Objective-C’s runtime capabilities, the code for this class is very straightforward:

```
// LoggerProxy.h
@interface LoggerProxy : NSProxy
- (id)initWithForwardingTarget:(id)forwardingTarget;
@end

// LoggerProxy.m
@implementation LoggerProxy {
    id _forwardingTarget;
}

- (id)initWithForwardingTarget:(id)forwardingTarget
{
    NSAssert(forwardingTarget != nil, @"forwardingTarget must not be nil");
    _forwardingTarget = forwardingTarget;
    return self;
}

- (NSMethodSignature *)methodSignatureForSelector:(SEL)selector
{
    // Just ask our forwarding target for the method signature
    return [_forwardingTarget methodSignatureForSelector:selector];
}

- (void)forwardInvocation:(NSInvocation *)invocation
{
    // Log the message
    NSLog(@"Logger Proxy: [%@ %@]", _forwardingTarget, NSStringFromSelector([invocation selector]));

    // Forward message to forwarding target
    [invocation invokeWithTarget:_forwardingTarget];
}

@end
```

With this implementation, we can only log selector names but not the particular arguments and return values of the messages that are being sent. To improve this, we have to introspect the `NSInvocation` object that is passed to the `forwardInvocation:` method. It contains all the information about a method’s arguments and return value. Unfortunately, parsing this data into a log-friendly format is pretty cumbersome because every argument type needs to be handled differently. You can have a look at [my test app on GitHub](https://github.com/ole/RemoteViewControllers) to see how I did it.[1](#fn:1)

Now we can replace the remote view controller instance we receive in the connectionHandler block with the proxy object:

```
ConnectionHandler swizzledBlock = ^(_UIRemoteViewController *remoteViewController, id blockArg2) {
    NSLog(@"connectionHandlerBlock called");
    NSLog(@"blockArg1: %@ %@", [remoteViewController class], remoteViewController);
    NSLog(@"blockArg2: %@ %@", [blockArg2 class], blockArg2);

    LoggerProxy *loggerProxy = [[LoggerProxy alloc] initWithForwardingTarget:remoteViewController];

    // Call the original block
    originalBlock((_UIRemoteViewController *)loggerProxy, blockArg2);
};
```

Note that the proxy is not a perfect replacement for the original object. For instance, I did not make any effort to mask the class of the proxy. If another object bases its own actions on the particular class of the remote view controller, the code would behave differently with the proxy in place. I noticed a few non-reproducible crashes in my testing that could have been causes by something like this, but most of the time everything seemed to work just fine.

A sample log output of the `LoggerProxy` looks like this:

```
Logger Proxy: [<MFMailComposeRemoteViewController: 0x1c576600> serviceViewControllerProxy]
  return value: @: <_UIViewServiceImplicitAnimationEncodingProxy: 0x1d83e4a0; target: <_XPCProxyReplyHandlerQueueRedirectingProxy: 0x1d8701d0; target: <_UIViewServiceXPCProxy: 0x1d8613c0>>>

Logger Proxy: [<MFMailComposeRemoteViewController: 0x1c576600> setDelegate:]
  called with arguments: (
    "@: <MFMailComposeInternalViewController: 0x1c56f9c0>"
  )
  return value: v: (void)

Logger Proxy: [<MFMailComposeRemoteViewController: 0x1c576600> parentViewController]
  return value: @: (null)

Logger Proxy: [<MFMailComposeRemoteViewController: 0x1c576600> view]
  return value: @: XX ('MFMailComposeRemoteViewController:0x1c576600' <_UISizeTrackingView: 0x1d855440; frame = (0 0; 0 0); clipsToBounds = YES; autoresize = W+H; layer = <CALayer: 0x1d865e90>>)

Logger Proxy: [<MFMailComposeRemoteViewController: 0x1c576600> parentViewController]
  return value: @: (null)

Logger Proxy: [<MFMailComposeRemoteViewController: 0x1c576600> _existingView]
  return value: @: 'MFMailComposeRemoteViewController:0x1c576600' <_UISizeTrackingView: 0x1d855440; frame = (0 0; 320 416); clipsToBounds = YES; autoresize = W+H; layer = <CALayer: 0x1d865e90>>

Logger Proxy: [<MFMailComposeRemoteViewController: 0x1c576600> _existingView]
  return value: @: 'MFMailComposeRemoteViewController:0x1c576600' <_UISizeTrackingView: 0x1d855440; frame = (0 0; 320 416); clipsToBounds = YES; autoresize = W+H; layer = <CALayer: 0x1d865e90>>

Logger Proxy: [<MFMailComposeRemoteViewController: 0x1c576600> parentViewController]
  return value: @: (null)

Logger Proxy: [<MFMailComposeRemoteViewController: 0x1c576600> setParentViewController:]
  called with arguments: (
    "@: <MFMailComposeInternalViewController: 0x1c56f9c0>"
  )
  return value: v: (void)

Logger Proxy: [<MFMailComposeRemoteViewController: 0x1c576600> willMoveToParentViewController:]
  called with arguments: (
    "@: <MFMailComposeInternalViewController: 0x1c56f9c0>"
  )
  return value: v: (void)
…
```

What we see here is how the `MFMailComposeInternalViewController` integrates the `MFMailComposeRemoteViewController` it has received from the factory method into its own view hierarchy and sets itself as its delegate. Unfortunately, we do not gain any further insight into the actual XPC communication.

# The Test App on GitHub

I want to conclude this article here. A further investigation should probably attempt to replace more objects that are involved in the process with custom proxy objects to be able to follow the entire flow of messages. If you are interested in following up on my research, feel free to check out my [Test app on GitHub](https://github.com/ole/RemoteViewControllers) and extend it with your own experiments.

# List of Remote View Controller Usage in iOS 6

Pavel Dudek [pointed out to me](https://twitter.com/eldudi/statuses/253438028163457024) that, in addition to the remote view controllers I had identified, Quick Look also uses the new setup. I then went through the iOS 6 class dumps again and found a few more places where remote view controllers are (possibly) being used. See the table below for the instances I found. If you find more, I’d love to update this list.

| Public Class | Local Class Name (the [_UI­Remote­View­Controller](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/UIKit.framework/_UIRemoteViewController.h) subclass) | Remote Class Name | XPC Service Bundle ID | XPC Service Name | Framework |
|---|---|---|---|---|---|
| [MF­Mail­Compose­View­Controller](http://developer.apple.com/library/ios/#documentation/MessageUI/Reference/MFMailComposeViewController_class/Reference/Reference.html) | [MF­Mail­Compose­Remote­View­Controller](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/MessageUI.framework/MFMailComposeRemoteViewController.h) | [Compose­Service­Remote­View­Controller](https://gist.github.com/3813291#file_compose_service_remote_view_controller.h) | com.­apple.­Mail­Composition­Service | Mail­Composition­Service.app | Messages­UI |
| [MF­Message­Compose­View­Controller](http://developer.apple.com/library/ios/#Documentation/MessageUI/Reference/MFMessageComposeViewController_class/Reference/Reference.html) | [CK­SMS­Compose­Remote­View­Controller](https://github.com/nst/iOS-Runtime-Headers/blob/master/PrivateFrameworks/ChatKit.framework/CKSMSComposeRemoteViewController.h) | [CK­SMS­Compose­View­Service­Controller](https://github.com/nst/iOS-Runtime-Headers/blob/master/PrivateFrameworks/ChatKit.framework/CKSMSComposeViewServiceController.h) | com.­apple.­mobilesms.­compose | Messages­View­Service.app | ChatKit (private) |
| [SL­Compose­View­Controller](http://developer.apple.com/library/ios/#documentation/NetworkingInternet/Reference/SLComposeViewController_Class/Reference/Reference.html) | [SL­Facebook­Remote­Compose­View­Controller](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/Social.framework/SLFacebookRemoteComposeViewController.h) | [SL­Facebook­Internal­Compose­View­Controller](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/Social.framework/SLFacebookInternalComposeViewController.h) | com.­apple.­social.­remoteui.­SocialUIService | Social­UI­Service.app | Social |
| [QL­Preview­Controller](http://developer.apple.com/library/ios/#documentation/NetworkingInternet/Reference/QLPreviewController_Class/Reference/Reference.html) | [QL­Remote­Preview­Content­Controller](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/QuickLook.framework/QLRemotePreviewContentController.h) | [QL­Service­Preview­Content­Controller](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/QuickLook.framework/QLServicePreviewContentController.h) | com.­apple.­quicklook.­quicklookd | quicklookd.app | Quick­Look |
| [SK­Store­Product­View­Controller](http://developer.apple.com/library/ios/#documentation/StoreKit/Reference/SKITunesProductViewController_Ref/Introduction/Introduction.html) | [SK­Remote­Product­View­Controller](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/StoreKit.framework/SKRemoteProductViewController.h) | Service­Product­Page­View­Controller | com.­apple.­ios.­Store­Kit­UIService | Store­Kit­UIService.app | Store­Kit |
| [_UI­Web­View­Controller](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/UIKit.framework/_UIWebViewController.h) (?) | [_UI­Remote­Web­View­Controller](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/UIKit.framework/_UIRemoteWebViewController.h) | [_UI­Service­Web­View­Controller](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/UIKit.framework/_UIServiceWebViewController.h) (?) | com.­apple.­Web­View­Service (?) | Web­View­Service.app (?) | UIKit |
| ? | [GK­Remote­View­Controller](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/GameKit.framework/GKRemoteViewController.h) | GK­Service­View­Controller (?) | com.­apple.­gamecenter.­GameCenterUIService (?) | Game­Center­UIService (?) | Game­Kit |
| — | [GK­Remote­Authenticate­View­Controller](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/GameKit.framework/GKRemoteAuthenticateViewController.h) | Authenticate­Service­View­Controller | com.­apple.­gamecenter.­GameCenterUIService (?) | Game­Center­UIService (?) | Game­Kit |
| [GK­Friend­Request­Compose­View­Controller](http://developer.apple.com/library/ios/#documentation/GameKit/Reference/GKFriendRequestComposeViewController_Ref/Reference/Reference.html) (?) | [GK­Compose­Remote­View­Controller](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/GameKit.framework/GKComposeRemoteViewController.h) | [GK­Compose­Hosted­View­Controller](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/GameKit.framework/GKComposeHostedViewController.h) (?) | com.­apple.­gamecenter.­GameCenterUIService (?) | Game­Center­UIService (?) | Game­Kit |
| — | [AD­Remote­View­Controller](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/iAd.framework/ADRemoteViewController.h) | ? | com.­apple.­AdSheet­Phone (?) | AdSheet.app (?) | iAd |
| — | [PK­Remote­Add­Passes­View­Controller](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/PassKit.framework/PKRemoteAddPassesViewController.h) | [PK­Service­Add­Passes­View­Controller](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/PassKit.framework/PKServiceAddPassesViewController.h) (?) | com.­apple.­Shoebox­UIService | Shoebox­UIService.app | Pass­Kit |
| — | [DD­Remote­Action­View­Controller](https://github.com/nst/iOS-Runtime-Headers/blob/master/PrivateFrameworks/DataDetectorsUI.framework/DDRemoteActionViewController.h) | [DD­Add­To­Contacts­View­Controller](https://github.com/nst/iOS-Runtime-Headers/blob/master/PrivateFrameworks/DataDetectorsUI.framework/DDAddToContactsViewController.h), DD­Event­Edit­View­Controller (?) | com.­apple.­datadetectors.­DDActionsService | DDActions­Service.app | Data­Detectors­UI (private) |

**Update October 8, 2012:** Read on in [part 3 of this series](https://oleb.net/blog/2012/10/update-on-remote-view-controllers/).

1. Particularly, have a look at the [`MethodArgument`](https://github.com/ole/RemoteViewControllers/blob/master/RemoteViewControllers/MethodArgument.m) class. It is responsible for decoding the type of a variable and providing a memory buffer and appropriate log output based on the type. The class is definitely not perfect (it does not handle all possible argument types correctly, for example), but it might provide a useful starting point for other applications. [↩︎](#fnref:1)
