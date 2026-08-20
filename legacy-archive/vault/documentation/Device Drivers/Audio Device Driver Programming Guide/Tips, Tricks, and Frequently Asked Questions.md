---
title: Audio Device Driver Programming Guide
apple_id: TP30000729
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2009-03-04'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WritingAudioDrivers/CustomControls/CustomControls.html
archived_at: '2026-07-15T07:31:45.097119Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Audio Device Driver Programming Guide](Introduction%20to%20Audio%20Device%20Driver%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Implementing%20an%20Audio%20Driver.md)

# Tips, Tricks, and Frequently Asked Questions

This chapter contains various tips on general concepts, sample buffers, and custom controls.

**What is the effect of aggregate devices from a driver programming perspective?**
: Aggregate devices cause multiple devices to behave as a single device. In the process, Core Audio does some extra work to smooth out timing inconsistencies.

The process should be transparent to driver writers, provided that your timestamps are reasonably correct.

**Should I create a “whole device” stream containing all outputs from my device, or just a stream for each pair of inputs/outputs?**
: That’s entirely up to you. Aggregate devices make this largely a non-issue. However, it may be convenient to provide a “whole device” stream to better support audio applications in versions of OS X prior to version 10.4.

**How do drivers interact with Audio/MIDI Setup?**
: Audio/MIDI Setup presents the standard controls for an audio device, along with stream selection capabilities. There’s no magic here. However, this question often comes up in conjunction with the issue of custom controls. In that case, some additional work is needed. This process is described further in [Creating Custom Controls](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomrzfvbuqmrtgywugsceizcumscb).

**What is the minimum (practical) size of a sample buffer, and what happens if a driver’s buffer is too small?**
: The size of a sample buffer is limited by a number of factors. For one, the sample offset (_not_ sample latency) must be taken into account. If the audio engine is set to read 1000 samples behind the hardware (for example), there had better be room for more than 1000 samples in the buffer. In fact, there should be at least two additional frames—the one in which the hardware is writing and the frame being erased ahead of it.

If your buffer is hopelessly too small, a good indicator is a continuous stream of errors indicating that the data has already been clipped. If the buffer is only slightly too small, you will merely experience a large number of glitches as the audio engine fails to keep up with the hardware.

**What is the difference between sample latency and sample offset?**
: Sample latency refers to the amount of time the audio hardware requires to reproduce a sound. This includes all delays in the input or output chain. For example, a device might take a few milliseconds between when it posts an interrupt indicating it read the start of the buffer and when the sound is actually played.

Sample offset is a feature designed for audio devices based on block I/O. Consider an output device as an example. If the audio device transfers data in a 32-sample block transaction, it must have at least 32 samples available when the audio engine wakes up. Otherwise, the engine won’t be able to queue up a block transfer, and will end up slipping a cycle, potentially resulting in a glitch. To solve this problem, you can specify a sample offset to guarantee that the higher levels stay a certain distance ahead of the I/O head.

**I’m having significant performance problems when doing custom input/output filtering in my driver. How can I improve performance?**
: A common cause of poor performance is using a separate thread for such audio filters. You can get a significant performance gain by doing this processing in your clipping or conversion routines instead.

Another possible performance problem is forgetting to turn off floating point emulation. Software floating point is significantly slower than hardware floating point and should generally be avoided in the critical path for audio data.

**I’m not doing any custom filtering, but I’m still having performance problems (dropouts, stuttering, and so on). Any ideas?**
: The most common cause of audio glitches is bad timestamping. See [Taking a Timestamp](Implementing%20an%20Audio%20Driver.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzsfvbecssfivduiry) for detailed suggestions. If you are using block devices or other devices where the timestamp can’t be taken precisely when the buffer wraps around, you may also find the code example in [Faking Timestamps](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomrzfvbuqmrtgywugsceinauescg) helpful.

One common problem that many audio device driver writers face is working around a transport layer that does not provide a timestamp when each audio packet is sent. If you take a timestamp based on receiving a packet that is larger than the remaining space in the buffer (where wrapping occurs mid-packet), your timestamp will not be particularly accurate.

The following code snippet shows a simple example of how to work around this problem:

```
void set_timestamp_adjusted(int current_bufpos)
{
    static int sec=0, usec=0, lastsec, lastusec=0, lastpos=0;
    int len, stampsec, stampusec;
    uint64_t curtm, lasttm, stampoff, stamptm


    clock_get_system_microtime(&sec, &usec);
    if (!lastsec && !lastusec) {
        // Engine just started. Initialize values.
        lastsec = sec;
        lastusec = sec;
    }

    curtm = (sec * 1000000UL) + usec; // usec since startup.
    lasttm = (lastsec * 1000000UL) + lastusec;
    stampoff = ((lasttm - curtm) * (uint64_t)(BUFFER_SIZE - lastpos))  /
            (uint64_t)len;
    stamptm = lasttm + stampoff;

    stampsec = (int)(stamptm / 1000000ULL);
    stampusec = (int)(stamptm % 1000000ULL);
    lastpos = current_bufpos;

    // set timestamp here.
}
```

Note that, if at all possible, you should attempt to take a time stamp (ideally at primary interrupt time for maximum accuracy) when the device wraps around to the start of the buffer. If it is possible to obtain a stamp precisely when the device wraps around, these sorts of calculations should not be necessary.

For most common purposes, the standard audio controls are sufficient. However, in some cases, you may need to create a custom control type.

The first step in creating a custom audio control is to subclass either the [IOAudioControl](https://developer.apple.com/documentation/kernel/ioaudiocontrol) or [IOAudioLevelControl](https://developer.apple.com/documentation/kernel/ioaudiolevelcontrol) class. In general, most typical controls express a continuous floating-point value across a particular range. For those controls, subclassing [IOAudioLevelControl](https://developer.apple.com/documentation/kernel/ioaudiolevelcontrol) is more appropriate. The more general [IOAudioControl](https://developer.apple.com/documentation/kernel/ioaudiocontrol) class is more appropriate for creating toggles and other controls that express noncontinuous values.

The second step is to write a `setValue` method. This method must interpret what those values mean and set appropriate instance variables accordingly, performing any range conversion calculations as needed.

The final step is to implement an application for managing these controls. Nonstandard controls can be manipulated using the same mechanisms as any other controls, but most applications won’t do anything with them because they don’t know to look for them (or what to do with them when they find them).

[Next](Document%20Revision%20History.md)[Previous](Implementing%20an%20Audio%20Driver.md)

