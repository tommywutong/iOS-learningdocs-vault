---
title: Update on Remote View Controllers
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/10/update-on-remote-view-controllers/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:41ec6f269d0cdb79'
translated: false
---

> 原文：[Update on Remote View Controllers](https://oleb.net/blog/2012/10/update-on-remote-view-controllers/)　·　Ole Begemann

# Update on Remote View Controllers

It’s time for another update on remote view controllers. For context, please read [part 1](https://oleb.net/blog/2012/10/remote-view-controllers-in-ios-6/) and [part 2](https://oleb.net/blog/2012/10/more-on-remote-view-controllers/) of this series first.

# Recreating Remote Views in iOS 5

Someone calling himself [iKy1e noticed something in my logs](https://iky1e.tumblr.com/post/33109276151/recreating-remote-views-ios5) that I paid little attention to: the [`_UIRemoteView`](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/UIKit.framework/_UIRemoteView.h) that sits at the bottom of a remote view controller hierarchy uses a [`CALayerHost`](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/QuartzCore.framework/CALayerHost.h) as its underlying Core Animation layer. According to iKy1e, a `CALayerHost` can not only display contents from another process; it also allows user interaction to pass from the host app to the remote process. In other words, this class is the key to transmitting both user actions and graphics across process boundaries.

With his knowledge of `CALayerHost`, iKy1e managed to [recreate a very similar remote view architecture on iOS 5](https://iky1e.tumblr.com/post/33109276151/recreating-remote-views-ios5#disqus_thread) (jailbreak required). As a replacement for XPC, he uses Apple’s private [`CPDistributedNotificationCenter`](https://github.com/nst/iOS-Runtime-Headers/blob/master/PrivateFrameworks/AppSupport.framework/CPDistributedNotificationCenter.h), which also allows communication between processes. The implementation isn’t perfect (for example, the keyboard doesn’t appear in the remote process; you can type blindly, however) but nevertheless it’s a very impressive demo.

# _UIWebViewController

With everything we have learned about remote view controllers, we should now be able to present a web view in a remote process. The hope is that [`_UIWebViewController`](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/UIKit.framework/_UIWebViewController.h) is the soon-to-be-public entry point. When we create an instance, it should in turn set up an internal XPC connection and manage a [`_UIRemoteWebViewController`](https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/UIKit.framework/_UIRemoteWebViewController.h) for us. The code is straightforward:

```
- (IBAction)openWebView:(id)sender
{
    _UIWebViewController *controller = [[_UIWebViewController alloc] init];
    controller.delegate = self;

    NSURL *url = [NSURL URLWithString:@"http://google.com"];
    NSURLRequest *request = [NSURLRequest requestWithURL:url];
    [controller loadRequest:request];

    [self presentViewController:controller animated:YES completion:^{
        // Log the view hierarchy here to see what's going on
        NSLog(@"View hierarchy: %@", [controller.view recursiveDescription]);
    }];
}
```

Sadly, this does not work. We seem to be on the right track, though. The log messages in the swizzled `+requestViewController:­fromServiceWithBundleIdentifier:­connectionHandler:` method prove that `_UIWebViewController` calls the method with seemingly the correct arguments:

```
self: _UIRemoteWebViewController
arg1: __NSCFConstantString _UIServiceWebViewController
arg2: __NSCFConstantString com.apple.WebViewService
arg3: __NSStackBlock__ <__NSStackBlock__: 0x2fdaa6bc>
Return Value: _UIAsyncInvocation <_UIAsyncInvocation: 0x1e0376f0>
```

We would expect to receive a valid `_UIRemoteViewController` in the `connectionHandler` block. Instead, the block arguments are `nil` and an `NSError` with a rather unhelpful error message:

```
blockArg1: (null) (null)
blockArg2: NSError Error Domain=XPCObjectsErrorDomain Code=2 "The operation couldn’t be completed. (XPCObjectsErrorDomain error 2.)"
Failed to get remote view controller with error: Error Domain=XPCObjectsErrorDomain Code=2 "The operation couldn’t be completed. (XPCObjectsErrorDomain error 2.)"
```

This at least confirms my earlier assumption that the second parameter of the `connectionHandler` block is an error object.

The only explanation I can think of why the above code does not work is that Apple has not yet completed the implementation of `_UIRemoteWebViewController` and its corresponding XPC service. That’s certainly a possibility, though I wonder why Apple would include code in the shipping version of iOS 6 that is so far from finished that Apple does not even use it itself.

I’d love to hear from you if you have any other idea what I might be doing wrong.
