---
title: 'CocoaSlideCollection: Using NSCollectionView on OS X 10.11'
apple_id: TP40016149
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaSlideCollection/Listings/CocoaSlideCollection_Model_AAPLFileTreeWatcherThread_m.html
archived_at: '2026-07-18T03:03:43.420947Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CocoaSlideCollection: Using NSCollectionView on OS X 10.11](CocoaSlideCollection-%20Using%20NSCollectionView%20on%20OS%20X%2010.11.md)


[Next](CocoaSlideCollection-Model-AAPLImageFile.m.md)[Previous](CocoaSlideCollection-Model-AAPLImageCollection.h.md)

# CocoaSlideCollection/Model/AAPLFileTreeWatcherThread.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the "FileTreeWatcherThread" class implementation.
*/

#import "AAPLFileTreeWatcherThread.h"

static void AAPLFileTreeWatcherEventStreamCallback(ConstFSEventStreamRef streamRef, void *clientCallBackInfo, size_t numEvents, void *eventPaths, const FSEventStreamEventFlags eventFlags[], const FSEventStreamEventId eventIds[]);

@implementation AAPLFileTreeWatcherThread

- initWithPath:(NSString *)pathToWatch changeHandler:(void (^)(void))changeHandler {
    NSParameterAssert(pathToWatch);
    NSParameterAssert(changeHandler);
    self = [self init];
    if (self) {
        [self setName:@"AAPLFileTreeWatcherThread"];
        paths = @[pathToWatch];
        @synchronized(self) {
            handler = [changeHandler copy];
        }
    }
    return self;
}

- (void)invokeChangeHandler {
    @synchronized(self) {
        if (handler) {
            [[NSOperationQueue mainQueue] addOperationWithBlock:handler];
        }
    }
}

- (void)detachChangeHandler {
    @synchronized(self) {
        handler = nil;
    }
}

- (void)main {
    @autoreleasepool {

        // Create our fsEventStream.
        FSEventStreamContext context;
        context.version = 0;
        context.info = (__bridge void *)self;
        context.retain = NULL;
        context.release = NULL;
        context.copyDescription = NULL;
        fsEventStream = FSEventStreamCreate(kCFAllocatorDefault, AAPLFileTreeWatcherEventStreamCallback, &context, CFBridgingRetain(paths), kFSEventStreamEventIdSinceNow, 1.0, kFSEventStreamCreateFlagUseCFTypes | kFSEventStreamCreateFlagWatchRoot | kFSEventStreamCreateFlagIgnoreSelf);
        if (fsEventStream != NULL) {

            // Schedule the fsEventStream on our thread's run loop.
            NSRunLoop *runLoop = [NSRunLoop currentRunLoop];
            CFRunLoopRef cfRunLoop = [runLoop getCFRunLoop];
            FSEventStreamScheduleWithRunLoop(fsEventStream, cfRunLoop, kCFRunLoopCommonModes);

            // Open the faucet.
            FSEventStreamStart(fsEventStream);

            // Run until we're asked to stop.
            while (![self isCancelled]) {
                [runLoop runUntilDate:[NSDate dateWithTimeIntervalSinceNow:0.25]];
            }

            // Shut off the faucet.
            FSEventStreamStop(fsEventStream);

            // Unschedule the fsEventStream on our thread's run loop.
            FSEventStreamUnscheduleFromRunLoop(fsEventStream, cfRunLoop, kCFRunLoopCommonModes);

            // Invalidate and release fsEventStream.
            FSEventStreamInvalidate(fsEventStream);
            FSEventStreamRelease(fsEventStream);
            fsEventStream = NULL;
        }
    }
}

@end

static void AAPLFileTreeWatcherEventStreamCallback(ConstFSEventStreamRef streamRef, void *clientCallBackInfo, size_t numEvents, void *eventPaths, const FSEventStreamEventFlags eventFlags[], const FSEventStreamEventId eventIds[]) {
    if (numEvents > 0) {
        AAPLFileTreeWatcherThread *thread = (__bridge AAPLFileTreeWatcherThread *)clientCallBackInfo;

        [thread invokeChangeHandler];
    }
}
```

[Next](CocoaSlideCollection-Model-AAPLImageFile.m.md)[Previous](CocoaSlideCollection-Model-AAPLImageCollection.h.md)

