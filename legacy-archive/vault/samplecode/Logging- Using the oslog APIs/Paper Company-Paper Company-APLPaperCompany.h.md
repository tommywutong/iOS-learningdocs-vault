---
title: 'Logging: Using the os_log APIs'
apple_id: TP40017510
resource_type: Sample Code
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Logging/Listings/Paper_Company_Paper_Company_APLPaperCompany_h.html
archived_at: '2026-07-18T03:13:47.414841Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Logging: Using the os_log APIs](Logging-%20Using%20the%20oslog%20APIs.md)


[Next](Paper%20Company-Paper%20Company-APLViewController.m.md)[Previous](Paper%20Company-Paper%20Company-APLAppDelegate.m.md)

# Paper Company/Paper Company/APLPaperCompany.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A paper company which handles trees, logs, and paper. Uses a custom logging component.
 */

@import Foundation;


@interface APLPaperCompany : NSObject

@property (nonatomic, readonly) NSString *companyName;
@property (nonatomic, readonly) NSUInteger numTrees;
@property (nonatomic, readonly) NSUInteger numLogs;
@property (nonatomic, readonly) NSUInteger numPapers;

/**
 * Create a new paper company.
 *
 * @param name The new company's name.
 */
- (instancetype)initWithCompanyName:(NSString *)name;

/// Chop down a tree, turning it into a log.
- (void)chopDownTree;

/// Turn all available logs into paper.
- (void)makePaper;

@end
```

[Next](Paper%20Company-Paper%20Company-APLViewController.m.md)[Previous](Paper%20Company-Paper%20Company-APLAppDelegate.m.md)

