---
title: AUAudioFilePlayer - Using the Audio File Player Audio Unit
apple_id: DTS40013349
resource_type: QA
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2013-05-20'
source_url: https://developer.apple.com/library/archive/qa/qa1786/_index.html
archived_at: '2026-07-18T02:34:45.410755Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1786

# AUAudioFilePlayer - Using the Audio File Player Audio Unit

## Q:  How do I set up the Audio File Player audio unit to play back a file?

A: The `AUAudioFilePlayer` (`kAudioUnitSubType_AudioFilePlayer`) is a specialization (subclass) of the `AUScheduledSoundPlayer` that allows you to schedule regions of audio files for future playback with sample-accurate timing.

As discussed in `AudioUnitProperties.h`, as a subclass of the scheduled sound player the file player inherits all of its behaviors. In particular, the file player implements the `kAudioUnitProperty_ScheduleStartTimeStamp` and `kAudioUnitProperty_CurrentPlayTime` properties but instead of scheduling slices (buffers) of audio to be played (via `kAudioUnitProperty_ScheduleAudioSlice`), you schedule regions of audio files to be played (via `kAudioUnitProperty_ScheduledFileRegion`). The audio file player unit converts audio file data into its own internal buffers performing disk I/O on a high-priority thread shared among all instances of this unit within a process. Upon completion of a disk read, the unit internally schedules buffers for playback.

To get started with the `AUAudioFilePlayer` provide a file to play:


```
AudioFileID mAudioFile;

...

UInt32 size;
err = AudioFileOpenURL(mFileURL, kAudioFileReadPermission, 0, &mAudioFile);

size = sizeof(mFileDataFormat);
err = AudioFileGetProperty(mAudioFile, kAudioFilePropertyDataFormat, &size, &mFileDataFormat);

// it's simplest to set the file player's output format to be
// canonical float 32, with the file's sample rate and channel count
err = [self buildAUGraph];

...

// give the file(s) to the player
// kAudioUnitProperty_ScheduledFileIDs value is an array of AudioFileIDs
// you must set this property on scheduled file player for all files to be
//     played and must not be set during playback.
// the audio files must be kept open for the duration of playback
err = AudioUnitSetProperty(mFilePlayerAU, kAudioUnitProperty_ScheduledFileIDs,
                           kAudioUnitScope_Global, 0, &mAudioFile, sizeof(mAudioFile));

...
```

To start playback set up your playback region using the `ScheduledAudioFileRegion` structure:


```
...

ScheduledAudioFileRegion playRegion;
playRegion.mTimeStamp.mFlags = kAudioTimeStampSampleTimeValid;
playRegion.mTimeStamp.mSampleTime = 0;
playRegion.mCompletionProc = NULL;
playRegion.mCompletionProcUserData = NULL;
playRegion.mAudioFile = mAudioFile;
playRegion.mLoopCount = 0;
playRegion.mStartFrame = mStartSampleFrame;
playRegion.mFramesToPlay = UInt32(-1);

err = AudioUnitSetProperty(mFilePlayerAU, kAudioUnitProperty_ScheduledFileRegion,
                           kAudioUnitScope_Global, 0, &playRegion, sizeof(playRegion));

...
```

Prime after scheduling initial file regions to be played and before starting playback:


```
...

UInt32 primeFrames = 0; // use default value (0x10000)
err = AudioUnitSetProperty(mFilePlayerAU, kAudioUnitProperty_ScheduledFilePrime,
                          kAudioUnitScope_Global, 0, &primeFrames, sizeof(primeFrames));

...
```

Set the start time to start playback at the specified time:


```
...

// set start time on next render cycle
AudioTimeStamp startTime;
startTime.mFlags = kAudioTimeStampSampleTimeValid;
startTime.mSampleTime = -1;
err = AudioUnitSetProperty(mFilePlayerAU, kAudioUnitProperty_ScheduleStartTimeStamp,
                           kAudioUnitScope_Global, 0, &startTime, sizeof(startTime));

...
```

Once playing, obtain the play position relative to the start point in samples using the `kAudioUnitProperty_CurrentPlayTime` property:


```
...

AudioTimeStamp ts;
UInt32 size = sizeof(ts);
err = AudioUnitGetProperty(mFilePlayerAU, kAudioUnitProperty_CurrentPlayTime,
                           kAudioUnitScope_Global, 0, &ts, &size);

Float64 sampleFrame = ts.mSampleTime;

...
```

To stop, simply call `AudioUnitReset`:


```
...

err = AudioUnitReset(mFilePlayerAU, kAudioUnitScope_Global, 0);

...
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-05-20 | New document that discusses using the AUAudioFilePlayer audio unit. |

