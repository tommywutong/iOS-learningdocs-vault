---
title: Hello Metronome
apple_id: TP40017587
resource_type: Sample Code
platform: watchOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-02-24'
source_url: https://developer.apple.com/library/archive/samplecode/HelloMetronome/Listings/HelloMetronome_main_m.html
archived_at: '2026-07-18T03:11:51.270855Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Hello Metronome](Hello%20Metronome.md)


[Next](HelloMetronome-Metronome.m.md)[Previous](Hello%20Metronome.md)

# HelloMetronome/main.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

*/

#import <Foundation/Foundation.h>
#import "Metronome.h"

// Set to use the included file for metronome bip.
#define USE_FILE_FOR_BIP 1

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        printf("Hello, Metronome!\n");

        NSURL *fileURL = nil;

    #if USE_FILE_FOR_BIP
        printf("Usage:\n -f use the MoreCowbell.caf file for the metronome bip.\n\n");
        if (argc == 2 && (0 == strcmp(argv[1], "-f"))) {
            printf("Using MoreCowbell.caf for Metronome bips.\n");
            fileURL = [[NSBundle mainBundle] URLForResource:@"MoreCowbell" withExtension:@"caf"];
        } else {
            printf("Using generated audio for Metronome bips.\n\n");
        }
    #endif

        Metronome *metronome = [[Metronome alloc] init:fileURL];

        [metronome start];

        sleep(10);

        [metronome stop];
    }

    return 0;
}
```

[Next](HelloMetronome-Metronome.m.md)[Previous](Hello%20Metronome.md)

