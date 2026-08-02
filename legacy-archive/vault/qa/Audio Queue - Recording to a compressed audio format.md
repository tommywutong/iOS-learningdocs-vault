---
title: Audio Queue - Recording to a compressed audio format.
apple_id: DTS40008016
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2009-05-21'
source_url: https://developer.apple.com/library/archive/qa/qa1615/_index.html
archived_at: '2026-07-18T02:32:46.943456Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1615

# Audio Queue - Recording to a compressed audio format.

## Q:  My Audio Queue recording code is based on the SpeakHere sample and I’d like to record using a compressed audio format instead of linear PCM, how can I do that?

A: My Audio Queue recording code is based on the SpeakHere sample and I’d like to record using a compressed audio format instead of linear PCM, how can I do that?

The iPhone OS supports recording a .caf file using a number of different compressed audio encoding formats:

- Apple Lossless - `kAudioFormatAppleLossless`
- iLBC (Internet Low Bitrate Codec) - `kAudioFormatiLBC`
- IMA/ADPCM (aka IMA4) - `kAudioFormatAppleIMA4`
- µLaw - `kAudioFormatULaw`
- aLaw - `kAudioFormatALaw`

Using Audio Queue services to record audio in one of the supported compressed formats requires setting up an `AudioStreamBasicDescription` structure (also called an ASBD) that describes the format. You then pass this description to the `AudioQueueNewInput` function. You must provide a valid sample rate, format ID and number of channels in the ASBD structure.

For example, listing 1 from the SpeakHere sample demonstrates how to change the `AudioStreamBasicDescription` structure for a different recording format. By default `kAudioFormatLinearPCM` is used, but this can easily be changed to `kAudioFormatAppleIMA4` or any other format from the options list.

__Listing 1__  SpeakHere - initWithURL: in AudioRecorder.m

```objc
- (id) initWithURL: fileURL {     NSLog (@"initializing a recorder object.");     self = [super init];      if (self != nil) {          // Specify the recording format. Options are:         //         //      kAudioFormatLinearPCM         //      kAudioFormatAppleLossless         //      kAudioFormatAppleIMA4         //      kAudioFormatiLBC         //      kAudioFormatULaw         //      kAudioFormatALaw         //         // When targeting the Simulator, SpeakHere uses linear PCM regardless of the format         //  specified here. See the setupAudioFormat: method in this file.         [self setupAudioFormat: kAudioFormatLinearPCM];          OSStatus result =   AudioQueueNewInput (                                 &audioFormat,                                 recordingCallback,                                 self,                   // userData                                 NULL,                   // run loop                                 NULL,                   // run loop mode                                 0,                      // flags                                 &queueObject                             );          NSLog (@"Attempted to create new recording audio queue object. Result: %f", result);          // get the recording format back from the audio queue's audio converter --         //  the file may require a more specific stream description than was          //  necessary to create the encoder.         UInt32 sizeOfRecordingFormatASBDStruct = sizeof (audioFormat);          AudioQueueGetProperty (             queueObject,             kAudioQueueProperty_StreamDescription,  // this constant is only available in iPhone OS             &audioFormat,             &sizeOfRecordingFormatASBDStruct         );          ...     }      return self; }   // Configures the audio data format for recording - (void) setupAudioFormat: (UInt32) formatID {      // Obtains the hardware sample rate for use in the recording     // audio format. Each time the audio route changes, the sample rate     // needs to get updated.     UInt32 propertySize = sizeof (self.hardwareSampleRate);      AudioSessionGetProperty (         kAudioSessionProperty_CurrentHardwareSampleRate,         &propertySize,         &hardwareSampleRate     );  // When running in the Simulator, the kAudioSessionProperty_CurrentHardwareSampleRate //  property is not available, so set it manually. #if TARGET_IPHONE_SIMULATOR         audioFormat.mSampleRate = 44100.0; #warning *** Simulator mode: using 44.1 kHz sample rate. #else         audioFormat.mSampleRate = self.hardwareSampleRate; #endif      NSLog (@"Hardware sample rate = %f", self.audioFormat.mSampleRate);      audioFormat.mFormatID           = formatID;     audioFormat.mChannelsPerFrame   = 1;      if (formatID == kAudioFormatLinearPCM) {          audioFormat.mFormatFlags        = kAudioFormatFlagIsSignedInteger | kAudioFormatFlagIsPacked;         audioFormat.mFramesPerPacket    = 1;         audioFormat.mBitsPerChannel     = 16;         audioFormat.mBytesPerPacket     = 2;         audioFormat.mBytesPerFrame      = 2;     } }
```


- [SpeakHere](https://developer.apple.com/iphone/library/samplecode/SpeakHere/)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-05-21 | Updated to reference SpeakHere v2.0 |
| 2009-01-27 | Updated URLs |
| 2008-09-24 | New document that describes how to change the SpeakHere iPhone sample allowing it to record compressed audio. |

