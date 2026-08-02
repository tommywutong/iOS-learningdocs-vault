---
title: Preventing Sensitive Information From Appearing In The Task Switcher
apple_id: DTS40014501
resource_type: QA
platform: iOS
topic: General
technology: null
published: '2014-05-12'
source_url: https://developer.apple.com/library/archive/qa/qa1838/_index.html
archived_at: '2026-07-18T02:35:09.270181Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1838

# Preventing Sensitive Information From Appearing In The Task Switcher

## Q:  How can I prevent sensitive information displayed by my app from appearing in the task switcher?

A: Immediately after your app moves to the background, the system captures a snapshot of your application's window and this snapshot is used to represent your application in the task switcher. By altering its view hierarchy prior to being suspended, an application can control how it appears in the task switcher.

Your application's delegate should implement the `-applicationDidEnterBackground:` method. In your implementation, configure the application's views as you want them to appear in the task switcher. An example is shown in Listing 1. If hiding sensitive information is better suited to objects besides the application's delegate, those objects can listen for the  `UIApplicationDidEnterBackgroundNotification`, which is posted immediately after the application's delegate receives a `-applicationDidEnterBackground:` message.

Before the application returns to the foreground, the application's delegate receives a `-applicationWillEnterForeground` . Your implementation should restore the view hierarchy back to a usable state as shown in Listing 2. Other interested objects can listen for the `UIApplicationWillEnterForegroundNotification`.

__Listing 1__  Hiding your application's contents before suspension

```objc
- (void)applicationDidEnterBackground:(UIApplication *)application
{
    // Your application can present a full screen modal view controller to
    // cover its contents when it moves into the background. If your
    // application requires a password unlock when it retuns to the
    // foreground, present your lock screen or authentication view controller here.

    UIViewController *blankViewController = [UIViewController new];
    blankViewController.view.backgroundColor = [UIColor blackColor];

    // Pass NO for the animated parameter. Any animation will not complete
    // before the snapshot is taken.
    [self.window.rootViewController presentViewController:blankViewController animated:NO completion:NULL];
}
```


__Listing 2__  Restoring your application's content before returning to the foreground.

```objc
- (void)applicationWillEnterForeground:(UIApplication *)application
{
    // This should be omitted if your application presented a lock screen
    // in -applicationDidEnterBackground:
    [self.window.rootViewController dismissViewControllerAnimated:NO completion:NO];
}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-05-12 | New document that describes how to hide sensitive information when your app is sent to the background. |

