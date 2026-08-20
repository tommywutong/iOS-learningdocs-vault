---
title: AVAudioSession - Requesting Audio Session Preferences
apple_id: DTS40008120
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2015-10-14'
source_url: https://developer.apple.com/library/archive/qa/qa1631/_index.html
archived_at: '2026-07-18T02:33:02.544650Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1631

# AVAudioSession - Requesting Audio Session Preferences

## Q:  Can I set a preferred value for an `AVAudioSession`'s buffer duration or sample rate at any time?

A: While it is safe to set the `AVAudioSession` audio category (`setCategory:error:`) or notification listeners like `AVAudioSessionRouteChangeNotification` for example, regardless of activation state, it is generally better to make preference requests such as preferred hardware buffer duration (`setPreferredIOBufferDuration:error:`) or preferred hardware sample rate (`setPreferredSampleRate:error:`) when the `AVAudioSession` is __NOT__ active.

These preferred values are simply hints to the operating system, the actual buffer duration or sample rate __may be different__ once the `AVAudioSession` has been activated. Therefore, asking for the current hardware buffer duration or sample rate before `AVAudioSession` activation could return incorrect values.

Follow these guidelines:

- Set "preferred" values when the audio session is not active.
- Get "current" values once the audio session has been activated.

__Listing 1__

```
// Configure the audio session for playback and recording
NSError *audioSessionError = nil;

AVAudioSession *session = [AVAudioSession sharedInstance];

[session setCategory:AVAudioSessionCategoryPlayback error:&audioSessionError];
if (audioSessionError) {
    NSLog(@"Error %ld, %@",
          (long)audioSessionError.code, audioSessionError.localizedDescription);
}

// Set some preferred values
NSTimeInterval bufferDuration = .005; // I would prefer a 5ms buffer duration
[session setPreferredIOBufferDuration:bufferDuration error:&audioSessionError];
if (audioSessionError) {
    NSLog(@"Error %ld, %@",
          (long)audioSessionError.code, audioSessionError.localizedDescription);
}

double sampleRate = 44100.0; // I would prefer a sample rate of 44.1kHz
[session setPreferredSampleRate:sampleRate error:&audioSessionError];
if (audioSessionError) {
    NSLog(@"Error %ld, %@",
          (long)audioSessionError.code, audioSessionError.localizedDescription);
}

// Register for Route Change notifications
[[NSNotificationCenter defaultCenter] addObserver: self
                                         selector: @selector(handleRouteChange:)
                                             name: AVAudioSessionRouteChangeNotification
                                           object: session];

// *** Activate the audio session before asking for the "Current" values ***
[session setActive:YES error:&audioSessionError];
if (audioSessionError) {
    NSLog(@"Error %ld, %@",
          (long)audioSessionError.code, audioSessionError.localizedDescription);
}

// Get current values
sampleRate = session.sampleRate;
bufferDuration = session.IOBufferDuration;

NSLog(@"Sample Rate:%0.0fHz I/O Buffer Duration:%f", sampleRate, bufferDuration);

...
```

In Listing 1 the `AVAudioSession` has been activated prior to asking for the current hardware sample rate and current hardware buffer duration. These returned values will accurately reflect what the hardware will present to the client. As previously stated, these values __may__ be different then what was asked for using the "Preferred" APIs.

When an application sets a preferred value, it will not take effect until the audio session has been activated. In most cases where setting a preferred value causes some sort of audio system reconfiguration with an active audio session, audio data I/O will be stopped and then restarted. Therefore, if an application plans to set multiple preferred values, it is generally advisable to deactivate the session first, set the preferences, reactivate the session and then check the actual values.

There are several cases however where an application must first activate the audio session (after setting the appropriate category, category options and mode), in order to lean about the capabilities of the current configuration before being able to set a "preferred" value.

For example:

- In order to call `setPreferredInput:error:`, an active audio session is required before querying the `availableInputs` property.
- Prior to calling `setPreferredOutputNumberOfChannels:error:`, an active audio session is required before asking for `maximumOutputNumberOfChannels`.

- If `AVAudioSessionCategoryOptionDuckOthers` has been set, going inactive will end ducking. Once your audio session reactivates, ducking of other audio will resume. When ducking has been set, your session is always mixable. This is because setting `AVAudioSessionCategoryOptionDuckOthers` to `true` will automatically also set `AVAudioSessionCategoryOptionMixWithOthers` to `true`.
- Using the `AVAudioSessionSetActiveOptionNotifyOthersOnDeactivation` option when deactivating will reactivate other non-mixable applications.

It is recommended to __NOT__ use the `AVAudioSessionSetActiveOptionNotifyOthersOnDeactivation` option when going inactive for the purpose of changing some preferred values.

[Audio Session Programming Guide](https://developer.apple.com/library/ios/documentation/Audio/Conceptual/AudioSessionProgrammingGuide/Introduction/Introduction.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-10-14 | Added note for iPhone 6s and 6s Plus |
| 2013-10-29 | Updated for AVAudioSession |
| 2013-02-07 | Added "Note" section |
| 2008-12-08 | New document that describes when to request session preferences such as Preferred Hardware I/O Buffer Duration. |

