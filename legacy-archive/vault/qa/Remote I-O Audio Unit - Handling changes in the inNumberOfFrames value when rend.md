---
title: Remote I/O Audio Unit - Handling changes in the inNumberOfFrames value when
  rendering output
apple_id: DTS40013097
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2013-02-07'
source_url: https://developer.apple.com/library/archive/qa/qa1777/_index.html
archived_at: '2026-07-18T02:34:41.430155Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1777

# Remote I/O Audio Unit - Handling changes in the inNumberOfFrames value when rendering output

## Q:  The number of frames value (`inNumberFrames`) passed to my Remote I/O render callback seem to sometimes change from previous render calls when a new audio device is plugged in while running, how should my app handle this?

A: Stream Formats can change when a new audio device is connected and a Sample Rate Conversion may be introduced when this Stream Format change occurs. In the presence of Sample Rate Conversion, the max frame size is going to be upscaled and any previously negotiated max frame size (when used to calculate buffer sizes) may no longer be sufficient.

Applications should to be aware of this possibility and handle these changes appropriately. This can be done by using `AudioUnitAddPropertyListener` and listening for two properties depending on your specific requirements.


```
AudioUnitAddPropertyListener(theRemoteIOAU, kAudioUnitProperty_MaximumFramesPerSlice, myAudioUnitPropertyListenerProc, NULL)
```

Listen for this property when you do not care what the hardware sample rate is and you want to keep your audio processing at the same application sample rate, thereby leaving the work of matching your applications sample rate to the hardware sample rate to the AURemoteIO Audio Unit.

The Audio Unit will send you a notification that the Maximum Frames Per Slice value has changed if it gets a hardware configuration change it needed to handle. The new Maximum Frames Per Slice will then indicate what the unit can pull your application for. Your application will need to stop rendering, reconfigure any processing being done to deal with this new Maximum Frames Per Slice value, then start rendering again.

You could also cache the previous value and then conditionalize the Stop/Reconfigure/Start pattern on the new Maximum Frames Per Slice value being larger than the previous one.


```
AudioUnitAddPropertyListener(theRemoteIOAU, kAudioUnitProperty_SampleRate, myAudioUnitPropertyListenerProc, NULL)
```

Listen for this property when you do care what the hardware sample rate is and you want to match your audio processing to the hardware sample rate (this is the typical case).

The Audio Unit will send you a notification when the hardware sample rate changes. Your application will need to stop rendering, reconfigure any processing being done for the new sample rate, then start rendering again. The sample rate change will be on the `Output scope` of `Bus 0`.

Your application should check the rate when called and only do any reconfiguration when the new rate is different from the current rate. When the sample rates differ, stop rendering, reconfiguring your audio processing to the new sample rate and then restart.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-02-07 | New document that discusses how to handle changes in the inNumberOfFrames value when rendering output |

