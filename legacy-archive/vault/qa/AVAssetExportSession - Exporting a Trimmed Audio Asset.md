---
title: AVAssetExportSession - Exporting a Trimmed Audio Asset
apple_id: DTS40010629
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2011-01-11'
source_url: https://developer.apple.com/library/archive/qa/qa1730/_index.html
archived_at: '2026-07-18T02:34:30.109456Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1730

# AVAssetExportSession - Exporting a Trimmed Audio Asset

## Q:  When creating .m4a output files, how do I configure an `AVAssetExportSession` object to trim audio assets and also perform a fade in?

A: When creating .m4a output files, how do I configure an `AVAssetExportSession` object to trim audio assets and also perform a fade in?

An `AVAssetExportSession` object is used to transcode the contents of an `AVAsset` source and has a number of configurable properties allowing the export operation to be customized. Output is described by a specified export preset, for example `AVAssetExportPresetAppleM4A` which will produce audio-only .m4a files.

Specifying the duration of the asset being exported may be done with the `timeRange` property. This property is a `CMTimeRange` describing start time and duration.

Another useful property is `audioMix`. By specifying a configured `AVAudioMix` object for the `audioMix` export property, you can perform custom audio processing on audio tracks during export.

Listing 1 demonstrates the basic configuration of an `AVAssetExportSession` object required to export an audio asset trimmed to 20 seconds with a 10 second fade in. The trim being set up in the code snippet takes place at the 30 second mark of the asset and therefore the track duration should be at least 50 seconds.

For more information regarding the AV Foundation APIs see the [AV Foundation Programming Guide.](https://developer.apple.com/library/ios/#documentation/AudioVideo/Conceptual/AVFoundationPG/Articles/00_Introduction.html)

__Listing 1__  Exporting a trimmed audio asset with a fade in.

```objc
- (BOOL)exportAsset:(AVAsset *)avAsset toFilePath:(NSString *)filePath {      // we need the audio asset to be at least 50 seconds long for this snippet     CMTime assetTime = [avAsset duration];     Float64 duration = CMTimeGetSeconds(assetTime);     if (duration < 50.0) return NO;      // get the first audio track     NSArray *tracks = [avAsset tracksWithMediaType:AVMediaTypeAudio];     if ([tracks count] == 0) return NO;      AVAssetTrack *track = [tracks objectAtIndex:0];      // create the export session     // no need for a retain here, the session will be retained by the     // completion handler since it is referenced there     AVAssetExportSession *exportSession = [AVAssetExportSession                                            exportSessionWithAsset:avAsset                                            presetName:AVAssetExportPresetAppleM4A];     if (nil == exportSession) return NO;      // create trim time range - 20 seconds starting from 30 seconds into the asset     CMTime startTime = CMTimeMake(30, 1);     CMTime stopTime = CMTimeMake(50, 1);     CMTimeRange exportTimeRange = CMTimeRangeFromTimeToTime(startTime, stopTime);      // create fade in time range - 10 seconds starting at the beginning of trimmed asset     CMTime startFadeInTime = startTime;     CMTime endFadeInTime = CMTimeMake(40, 1);     CMTimeRange fadeInTimeRange = CMTimeRangeFromTimeToTime(startFadeInTime,                                                             endFadeInTime);      // setup audio mix     AVMutableAudioMix *exportAudioMix = [AVMutableAudioMix audioMix];     AVMutableAudioMixInputParameters *exportAudioMixInputParameters =             [AVMutableAudioMixInputParameters audioMixInputParametersWithTrack:track];      [exportAudioMixInputParameters setVolumeRampFromStartVolume:0.0 toEndVolume:1.0                                    timeRange:fadeInTimeRange];      exportAudioMix.inputParameters = [NSArray                                       arrayWithObject:exportAudioMixInputParameters];       // configure export session  output with all our parameters     exportSession.outputURL = [NSURL fileURLWithPath:filePath]; // output path     exportSession.outputFileType = AVFileTypeAppleM4A; // output file type     exportSession.timeRange = exportTimeRange; // trim time range     exportSession.audioMix = exportAudioMix; // fade in audio mix      // perform the export     [exportSession exportAsynchronouslyWithCompletionHandler:^{          if (AVAssetExportSessionStatusCompleted == exportSession.status) {             NSLog(@"AVAssetExportSessionStatusCompleted");         } else if (AVAssetExportSessionStatusFailed == exportSession.status) {             // a failure may happen because of an event out of your control             // for example, an interruption like a phone call comming in             // make sure and handle this case appropriately             NSLog(@"AVAssetExportSessionStatusFailed");         } else {             NSLog(@"Export Session Status: %d", exportSession.status);         }     }];      return YES; }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-01-11 | New document that demonstrates how to configure an export session to trim an audio asset and add a fade in. |

