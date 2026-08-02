---
title: CryptoCompatibility
apple_id: DTS40013654
resource_type: Sample Code
platform: iOS|macOS
topic: Security
technology: Security
published: '2016-11-17'
source_url: https://developer.apple.com/library/archive/samplecode/CryptoCompatibility/Listings/Tool_ToolCommon_h.html
archived_at: '2026-07-18T03:05:22.357298Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CryptoCompatibility](CryptoCompatibility.md)


[Next](Tool-DigestCommands.h.md)[Previous](Tool-QToolCommand.h.md)

# Tool/ToolCommon.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Utilities used by various tool commands.
 */

@import Foundation;

NS_ASSUME_NONNULL_BEGIN

/*! description
 *  \details Utilities used by various tool commands and tests.
 */

@interface ToolCommon : NSObject

/*! Instance shared between all the tool commands and tests.
 */

+ (ToolCommon *)sharedInstance;

/*! Runs the supplied operation synchronously.
 *  \details This has two modes.  If `debugRunOpOnMainThread` is NO, it runs 
 *      the operation on a default operation queue and then waits for it to 
 *      complete.  OTOH, if it's YES, it actually calls the `-main` method of the 
 *      operation directly.  The later is used by the tool (when in debug mode) and 
 *      the unit tests to ensure that everything runs on the main thread.
 */

- (void)synchronouslyRunOperation:(NSOperation *)op;

/*! Controls the behaviour of `-synchronouslyRunOperation:`.
 */

@property (atomic, assign, readwrite) BOOL   debugRunOpOnMainThread;

@end

NS_ASSUME_NONNULL_END
```

[Next](Tool-DigestCommands.h.md)[Previous](Tool-QToolCommand.h.md)

