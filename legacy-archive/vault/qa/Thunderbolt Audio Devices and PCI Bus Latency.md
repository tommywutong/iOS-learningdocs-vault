---
title: Thunderbolt Audio Devices and PCI Bus Latency
apple_id: DTS40014114
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: IOKit
published: '2014-01-30'
source_url: https://developer.apple.com/library/archive/qa/qa1452/_index.html
archived_at: '2026-07-27T06:57:05.357249Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1452

# Thunderbolt Audio Devices and PCI Bus Latency

## Q:  I have a Thunderbolt audio interface which experiences audio glitching when attached to a Mac that is not doing much other work. What could be causing this?

A: The processors in modern Macs have low-power states that reduce the processor speed and voltage when in idle mode to decrease power consumption and heat generation.

When power management decides to change the processor power state, it's necessary to switch the power state of all of the processor cores simultaneously. PCI bus traffic is held off while these transitions are under way. It is this additional latency that can cause side effects such as audio glitching.

The best way by far to handle this is to change how you schedule your time-critical DMA operations in your driver such that an occasional delay will not affect the proper functioning of your device. However, if this is not possible, your driver can inform power management when a time-critical transfer begins and ends so that the system will not enter the lowest power states during that time. To do this, pass a value to `requireMaxBusStall` that informs power management of the maximum memory access latency in nanoseconds that can be tolerated by the driver. This value is hardware dependent and is related to the amount of buffering available in the hardware.

__Important:__ Pass the largest value possible to `requireMaxBusStall` that works for your device. This will minimize power consumption and maximize battery life by still allowing some level of CPU power management.

Because audio transfers only occur while your audio engine is running, you can override the virtual methods `performAudioEngineStart` and `performAudioEngineStop` in `IOAudioEngine` as shown in Listing 1.

__Listing 1__  Informing power management about a time-critical DMA transfer.

```swift
/* Header file */
class MyAudioEngine : public IOAudioEngine
{
    /* virtual overrides, custom function, variables, etc... */

public:
    virtual IOReturn performAudioEngineStart();
    virtual IOReturn performAudioEngineStop();
}

/* Implementation file */
IOReturn MyAudioEngine::performAudioEngineStart()
{
    // Latency tolerance interval in nanoseconds
    const UInt32 maxLatencyTolerance_ns = 10*1000;

    requireMaxBusStall(maxLatencyTolerance_ns);
    return IOAudioEngine::performAudioEngineStart();
}

IOReturn MyAudioEngine::performAudioEngineStop()
{
    // Zero means restore default bus stall time.
    // It's now safe to go into lowest-power states.
    requireMaxBusStall(0);
    return IOAudioEngine::performAudioEngineStop();
}
```

__Warning:__ You should only use `requireMaxBusStall` if there is no other way to make your device and driver more tolerant of increased memory latency. It is very important that you not abuse this API. By preventing the system from going into its most power-thrifty states, your customers can see significantly-reduced battery life on portable systems. It can also cause system fans spin up and run longer, producing more noise. Abuse of this API can also lead to kernel panics.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-01-30 | New document that explains how Thunderbolt audio devices can be affected by higher latency in low-power states. |
