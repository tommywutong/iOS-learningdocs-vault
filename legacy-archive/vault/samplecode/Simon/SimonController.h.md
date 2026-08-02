---
title: Simon
apple_id: DTS10000402
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Simon/Listings/SimonController_h.html
archived_at: '2026-07-18T03:23:51.379662Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Simon](Simon.md)


[Next](SimonController.m.md)[Previous](main.m.md)

# SimonController.h

```objc
/*
    File:       SimonController.h   

    Contains:   A sample of a simple cocoa application.

    Written by:     Karl Groethe

    Copyright:  Copyright © 2000 by Apple Computer, Inc., All Rights Reserved.

            You may incorporate this Apple sample source code into your program(s) without
            restriction. This Apple sample source code has been provided "AS IS" and the
            responsibility for its operation is yours. You are not permitted to redistribute
            this Apple sample source code as "Apple sample source code" after having made
            changes. If you're going to re-distribute the source, we require that you make
            it clear in the source that the code was descended from Apple sample source
            code, but that you've made changes.

    Change History (most recent first):
                        6/00    created


*/
#import <AppKit/AppKit.h>
#define MAX_SEQUENCE_LENGTH 100

@interface SimonController : NSObject
{
    id myButton1;
    id myButton2;
    id myButton3;
    id myButton4;
    id myCounter;
    id myMessage;
    id myStartStop;

    int listening;
    int sequenceLength;
    id sequence[MAX_SEQUENCE_LENGTH];
}
- (void)StartStopGame:(id)sender;
- (void)ListenSequence:(id)sender;
- (void)PlaySequence;
@end
```

[Next](SimonController.m.md)[Previous](main.m.md)

