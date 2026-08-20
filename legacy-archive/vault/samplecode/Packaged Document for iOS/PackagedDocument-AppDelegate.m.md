---
title: Packaged Document for iOS
apple_id: DTS40014139
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Foundation
published: '2016-02-04'
source_url: https://developer.apple.com/library/archive/samplecode/sc2281/Listings/PackagedDocument_AppDelegate_m.html
archived_at: '2026-07-26T19:54:13.685145Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Packaged Document for iOS](Packaged%20Document%20for%20iOS.md)


[Next](PackagedDocument-ImageViewController.h.md)[Previous](PackagedDocument-FileRepresentation.h.md)

# PackagedDocument/AppDelegate.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 UIApplication delegate for the application.
 */

#import "AppDelegate.h"

@implementation AppDelegate

// The app delegate must implement the window @property
// from UIApplicationDelegate @protocol to use a main storyboard file.
@synthesize window;

+ (NSURL *)localDocumentsDirectoryURL
{
    // returns the directory in which documents are stored
    static NSURL *localDocumentsDirectoryURL = nil;

    if (localDocumentsDirectoryURL == nil)
    {
        NSString *documentsDirectoryPath = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES)[0];
        localDocumentsDirectoryURL = [NSURL fileURLWithPath:documentsDirectoryPath];
    }
    return localDocumentsDirectoryURL;
}

@end
```

[Next](PackagedDocument-ImageViewController.h.md)[Previous](PackagedDocument-FileRepresentation.h.md)

