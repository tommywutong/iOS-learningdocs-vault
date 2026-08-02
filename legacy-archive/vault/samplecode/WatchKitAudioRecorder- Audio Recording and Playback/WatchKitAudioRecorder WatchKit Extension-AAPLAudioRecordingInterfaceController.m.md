---
title: 'WatchKitAudioRecorder: Audio Recording and Playback'
apple_id: TP40016225
resource_type: Sample Code
platform: watchOS
topic: Audio, Video, & Visual Effects
technology: WatchKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/WatchKitAudioRecorder/Listings/WatchKitAudioRecorder_WatchKit_Extension_AAPLAudioRecordingInterfaceController_m.html
archived_at: '2026-07-18T03:28:07.549469Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WatchKitAudioRecorder: Audio Recording and Playback](WatchKitAudioRecorder-%20Audio%20Recording%20and%20Playback.md)


[Next](WatchKitAudioRecorder%20WatchKit%20Extension-AAPLExtensionDelegate.m.md)[Previous](WatchKitAudioRecorder%20WatchKit%20Extension-AAPLExtensionDelegate.h.md)

# WatchKitAudioRecorder WatchKit Extension/AAPLAudioRecordingInterfaceController.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    'AAPLAudioRecordingInterfaceController' implements audio recording based on a preset that the user has chosen, saves the recording, and plays back the last recording that was made.
 */

@import WatchConnectivity;
#import "AAPLAudioRecordingInterfaceController.h"
#import "AAPLAppConfiguration.h"

@interface AAPLAudioRecordingInterfaceController () <WCSessionDelegate>

@property (weak, nonatomic) IBOutlet WKInterfacePicker *picker;

@property NSArray <WKPickerItem *> *pickerItems;

@property NSURL *lastRecordingURL;

@property WKPickerItem *selectedItem;

@property NSUInteger numberOfRecordings;

@end


@implementation AAPLAudioRecordingInterfaceController

- (instancetype)init {
    self = [super init];

    if (self) {
        // Create Picker Items fro our Picker.
        WKPickerItem *narrowBand = [[WKPickerItem alloc] init];
        narrowBand.title = @"Narrow Band";

        WKPickerItem *wideBand = [[WKPickerItem alloc] init];
        wideBand.title = @"Wide Band";

        WKPickerItem *highQuality = [[WKPickerItem alloc] init];
        highQuality.title = @"High Quality";

        // Activate the session on both sides to enable communication.
        [WCSession defaultSession].delegate = self;
        [[WCSession defaultSession] activateSession];

        // Keep track of the picker items to know which one has been selected.
        _pickerItems = @[narrowBand, wideBand, highQuality];

        // Set the picker items on the picker.
        [_picker setItems:self.pickerItems];

        _numberOfRecordings = 0;
    }

    return self;
}

#pragma mark - IBActions

- (IBAction)pickerValueSelected:(NSInteger)value {
    self.selectedItem = self.pickerItems[value];
}

- (IBAction)startRecording {
    WKAudioRecorderPreset preset = [self audioRecordingPresetForPickerItem:self.selectedItem];

    NSLog(@"preset: %d", preset);

    // Get the directory from the app group.
    NSURL *directory = [[NSFileManager defaultManager] containerURLForSecurityApplicationGroupIdentifier:AAPLAppConfigurationApplicationGroupsPrimary];
    NSUInteger timeAtRecording = (NSUInteger)[NSDate timeIntervalSinceReferenceDate];
    __block NSString *recordingName = [NSString stringWithFormat:@"AudioRecording-%d.mp4", timeAtRecording];
    __block NSURL * outputURL = [directory URLByAppendingPathComponent:recordingName];
    __weak AAPLAudioRecordingInterfaceController *weakSelf = self;
    [self presentAudioRecorderControllerWithOutputURL:outputURL preset:preset options:nil completion:^(BOOL didSave, NSError * _Nullable error) {
        __strong AAPLAudioRecordingInterfaceController *strongSelf = weakSelf;

        if (!strongSelf) {
            return;
        }

        if (didSave) {
            /*
                After saving we need to move the file to our documents directory
                so that WatchConnectivity can transfer it.
            */
            NSURL *extensionDirectory = [[NSFileManager defaultManager] URLsForDirectory:NSDocumentDirectory inDomains:NSUserDomainMask].firstObject;

            NSURL *outputExtensionURL = [extensionDirectory URLByAppendingPathComponent:recordingName];

            NSError *moveError;

            NSLog(@"outputURL: %@", outputURL);
            NSLog(@"outputExtensionURL: %@", outputExtensionURL);

            // Move the file.
            BOOL success = [[NSFileManager defaultManager] moveItemAtURL:outputURL toURL:outputExtensionURL error:&moveError];

            if (!success) {
                NSLog(@"Failed to move the outputURL to the extension's documents direcotry: %@", error);
            }
            else {
                strongSelf.lastRecordingURL = outputExtensionURL;
                NSLog(@"lastRecordingURL: %@.", strongSelf.lastRecordingURL);

                // Activate the session before transferring the file.
                [[WCSession defaultSession] transferFile:outputExtensionURL metadata:nil];
            }

            self.numberOfRecordings++;
        }

        if (error) {
            NSLog(@"There was an error with the audio recording: %@.", error);
        }
    }];
}

- (IBAction)playLastRecording {
    // Present the media player controller for the last recorded URL.
    NSDictionary *options = @{
        WKMediaPlayerControllerOptionsAutoplayKey : @YES
    };

    [self presentMediaPlayerControllerWithURL:self.lastRecordingURL options:options completion:^(BOOL didPlayToEnd, NSTimeInterval endTime, NSError * __nullable error) {
        if (!didPlayToEnd) {
            NSLog(@"The player did not play all the way to the end. The player only played until time - %.2f.", endTime);
        }

        if (error) {
            NSLog(@"There was an error with playback: %@.", error);
        }
    }];
}

#pragma mark - Audio Preset Helpers

- (WKAudioRecorderPreset)audioRecordingPresetForPickerItem:(WKPickerItem *)pickerItem {
    // Get the audio recording preset from the picker item.
    NSString *title = pickerItem.title;

    WKAudioRecorderPreset preset = WKAudioRecorderPresetHighQualityAudio;

    if ([title isEqualToString:@"Narrow Band"]) {
        preset = WKAudioRecorderPresetNarrowBandSpeech;
    }
    else if ([title isEqualToString:@"Wide Band"]) {
        preset = WKAudioRecorderPresetWideBandSpeech;
    }

    return preset;
}

#pragma mark - WCSessionDelegate

- (void)session:(nonnull WCSession *)session didFinishFileTransfer:(nonnull WCSessionFileTransfer *)fileTransfer error:(nullable NSError *)error {
    // This method is called on the sending side when the file has successfully transfered.
    if (error) {
        NSLog(@"There was an error transferring the file: %@", error);
    }
    else {
        NSLog(@"The file was transfered succesfully!");
    }
}

@end
```

[Next](WatchKitAudioRecorder%20WatchKit%20Extension-AAPLExtensionDelegate.m.md)[Previous](WatchKitAudioRecorder%20WatchKit%20Extension-AAPLExtensionDelegate.h.md)

