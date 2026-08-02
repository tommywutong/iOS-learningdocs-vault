---
title: 'WatchKitAudioRecorder: Audio Recording and Playback'
apple_id: TP40016225
resource_type: Sample Code
platform: watchOS
topic: Audio, Video, & Visual Effects
technology: WatchKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/WatchKitAudioRecorder/Listings/Configuration_AAPLAppConfiguration_m.html
archived_at: '2026-07-18T03:28:07.235245Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WatchKitAudioRecorder: Audio Recording and Playback](WatchKitAudioRecorder-%20Audio%20Recording%20and%20Playback.md)


[Next](Configuration-AAPLAppConfiguration.h.md)[Previous](LICENSE.txt.md)

# Configuration/AAPLAppConfiguration.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Handles application configuration logic and information.
*/

#import "AAPLAppConfiguration.h"

/*!
 The \c SAMPLE_BUNDLE_PREFIX_STRING preprocessor macro is used below to concatenate the value of the
 \c SAMPLE_BUNDLE_PREFIX user-defined build setting with other strings. This avoids the need for developers
 to edit both SAMPLE_BUNDLE_PREFIX and the code below. \c SAMPLE_BUNDLE_PREFIX_STRING is equal to
 \c @"SAMPLE_BUNDLE_PREFIX", i.e. an \c NSString literal for the value of \c SAMPLE_BUNDLE_PREFIX. (Multiple
 \c NSString literals can be concatenated at compile-time to create a new string literal.)
 */
NSString *const AAPLAppConfigurationApplicationGroupsPrimary = @"group."SAMPLE_BUNDLE_PREFIX_STRING@".WatchKitAudioRecorder";
```

[Next](Configuration-AAPLAppConfiguration.h.md)[Previous](LICENSE.txt.md)

