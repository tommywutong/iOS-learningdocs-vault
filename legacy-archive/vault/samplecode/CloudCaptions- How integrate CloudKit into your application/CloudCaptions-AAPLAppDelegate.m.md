---
title: 'CloudCaptions: How integrate CloudKit into your application'
apple_id: TP40014732
resource_type: Sample Code
platform: iOS
topic: null
technology: CloudKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/CloudCaptions/Listings/CloudCaptions_AAPLAppDelegate_m.html
archived_at: '2026-07-18T03:03:29.868893Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudCaptions: How integrate CloudKit into your application](CloudCaptions-%20How%20integrate%20CloudKit%20into%20your%20application.md)


[Next](CloudCaptions-AAPLSubmitPostViewController.h.md)[Previous](CloudCaptions-AAPLExistingImageViewController.h.md)

# CloudCaptions/AAPLAppDelegate.m

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 */

@import CloudKit;
#import "AAPLAppDelegate.h"
#import "AAPLTableViewController.h"

@interface AAPLAppDelegate ()
@end

@implementation AAPLAppDelegate


- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // Override point for customization after application launch.
    UIUserNotificationSettings *notificationSettings = [UIUserNotificationSettings settingsForTypes:UIUserNotificationTypeAlert categories:nil];
    [application registerUserNotificationSettings:notificationSettings];
    [application registerForRemoteNotifications];
    return YES;
}

- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo
{
    if(self.tableController)
    {
        // Sends the ID of the record save that triggered the push to the tableViewController
        CKQueryNotification *recordInfo = [CKQueryNotification notificationFromRemoteNotificationDictionary:userInfo];
        [self.tableController loadNewPostsWithRecordID:recordInfo.recordID];
    }
}

@end
```

[Next](CloudCaptions-AAPLSubmitPostViewController.h.md)[Previous](CloudCaptions-AAPLExistingImageViewController.h.md)

