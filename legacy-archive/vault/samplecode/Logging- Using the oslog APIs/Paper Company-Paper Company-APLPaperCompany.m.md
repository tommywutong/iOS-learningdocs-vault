---
title: 'Logging: Using the os_log APIs'
apple_id: TP40017510
resource_type: Sample Code
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Logging/Listings/Paper_Company_Paper_Company_APLPaperCompany_m.html
archived_at: '2026-07-18T03:13:47.443698Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Logging: Using the os_log APIs](Logging-%20Using%20the%20oslog%20APIs.md)


[Next](Paper%20Company-Paper%20Company-APLAppDelegate.m.md)[Previous](Paper%20Company-Paper%20Company-APLViewController.h.md)

# Paper Company/Paper Company/APLPaperCompany.m

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A paper company which handles trees, logs, and paper. Uses a custom logging component.
 */

@import os.log;
#import "APLPaperCompany.h"


#define NUM_STARTING_TREES 5

// We want to use a custom logging component for our model (as in model-view-controller).
// This allows us to enable debug logging for just our model, so we don't have to wade
// through logs from the view just to see what's wrong with one method in our model.
static os_log_t model_log;


@interface APLPaperCompany ()

@property (nonatomic, readwrite) NSString *companyName;
@property (nonatomic, readwrite) NSUInteger numTrees;
@property (nonatomic, readwrite) NSUInteger numLogs;
@property (nonatomic, readwrite) NSUInteger numPapers;

@end


@implementation APLPaperCompany

+ (void)initialize {
    // We want to use a custom logging component for our model, so we need to set it up before its first use.
    model_log = os_log_create("com.example.apple-samplecode.Paper-Company", "Model");
}

- (instancetype)initWithCompanyName:(NSString *)name {
    if ((self = [super init])) {
        self.companyName = name;
        self.numTrees = NUM_STARTING_TREES;
        self.numLogs = 0;
        self.numPapers = 0;
    }
    return self;
}

- (void)chopDownTree {
    // Make sure we actually have a tree to chop down.
    if (self.numTrees == 0) {
        os_log_info(model_log, "No trees left to chop down!");
        return;
    }

    // We're good.
    os_log_info(model_log, "Chopped down a tree!");
    self.numTrees--;
    self.numLogs++;
    os_log_debug(model_log, "%lu trees remaining, %lu logs accumulated",
                 (unsigned long)self.numTrees, (unsigned long)self.numLogs);
}

- (void)makePaper {
    // Make sure we actually have a log to turn into paper.
    if (self.numLogs == 0) {
        os_log_info(model_log, "No logs to pulverize into paper!");
        return;
    }

    // We're good.
    os_log_info(model_log, "Making paper from our logs!");
    os_log_debug(model_log, "Pulverizing %lu logs into paper.", (unsigned long)self.numLogs);
    self.numPapers += self.numLogs;
    self.numLogs = 0;
    os_log_debug(model_log, "We now have %lu papers.", (unsigned long)self.numPapers);
}

@end
```

[Next](Paper%20Company-Paper%20Company-APLAppDelegate.m.md)[Previous](Paper%20Company-Paper%20Company-APLViewController.h.md)

