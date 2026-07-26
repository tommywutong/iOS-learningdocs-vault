---
title: Multi-GPU systems
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/multi-gpu-systems
source_url: 'https://developer.apple.com/documentation/metal/multi-gpu-systems'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/multi-gpu-systems.json'
content_hash: 'sha256:aa37490294f51323'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [GPU devices and work submission](gpu-devices-and-work-submission.md)

# Multi-GPU systems

<sub>API Collection</sub>

Locate and work with internal and external GPUs and their displays, video memory, and performance tradeoffs.

## Overview

Your app can submit work to any or all of the GPUs of a system that supports multiple GPUs. For example, every Mac notebook, such as a MacBook Pro, has an internal GPU, but some have two.

![A system diagram that shows two built-in GPUs within a MacBook Pro.](../../../attachments/b022119842cf3a4a9bc64718e4ac3a20/assessing-multi-gpu-and-multi-display-setups-on-an-intel-based-mac-3@2x.png)

A Mac may have a Thunderbolt connection to an external GPU and its displays.

![A system diagram that shows an external GPU that connects a MacBook Pro to an external display.](../../../attachments/b22a3f95645c4220377c91079b7fb6c5/assessing-multi-gpu-and-multi-display-setups-on-an-intel-based-mac-6@2x.png)

Some systems may have even more complicated arrangements of internal and multiple external GPUs and displays.

![](../../../attachments/b505af846a78d0167e779ce702fb7d61/assessing-multi-gpu-and-multi-display-setups-on-an-intel-based-mac-7@2x.png)

<sub>A system diagram that shows an iMac Pro connected to an external display, an external GPU, and another external GPU that’s also connected to two additional external displays.</sub>

For more information about Mac configurations with GPUs and displays, see [Assessing multi-GPU and multidisplay setups on an Intel-based Mac](assessing-multi-gpu-and-multi-display-setups-on-an-intel-based-mac.md).

Start by locating all GPUs in a system and identifying their types (see [Finding multiple GPUs on an Intel-based Mac](finding-multiple-gpus-on-an-intel-based-mac.md)). Alternatively, you can locate a specific GPU that’s driving a display (see [Getting the GPU that drives a view’s display](getting-the-gpu-that-drives-a-views-display.md)).

When selecting a GPU, consider its memory bandwidth and the storage mode options for its memory resources (see [Adjusting for GPU memory bandwidth tradeoffs](adjusting-for-gpu-memory-bandwidth-tradeoffs.md)).

For examples of how to use external GPUs in your graphics rendering or compute processing workflows, see the following:

- [Selecting device objects for graphics rendering](selecting-device-objects-for-graphics-rendering.md)
- [Selecting device objects for compute processing](selecting-device-objects-for-compute-processing.md)

For more information about external GPU configurations, see [Use an external graphics processor with your Mac](https://support.apple.com/kb/HT208544).

> [!note] Note
> The system may gain or lose an external GPU at any time (see [Handling external GPU additions and removals](handling-external-gpu-additions-and-removals.md)).

## Topics

### Locating GPUs

- [Finding multiple GPUs on an Intel-based Mac](finding-multiple-gpus-on-an-intel-based-mac.md) — Locate, identify, and choose suitable GPUs for your app.
- [Getting the GPU that drives a view’s display](getting-the-gpu-that-drives-a-views-display.md) — Keep up to date with the optimal device for your display.
- [MTLCopyAllDevices](<mtlcopyalldevices().md>) — Returns an array of all the Metal device instances in the system.
- [MTLCopyAllDevicesWithObserver(handler:)](<mtlcopyalldeviceswithobserver(handler_).md>) — Returns an array of all the Metal GPU devices in the system and registers a notification handler that Metal calls when the device list changes.
- [MTLRemoveDeviceObserver](<mtlremovedeviceobserver(__).md>) — Removes a registered observer of device notifications. _(deprecated)_
- [CGDirectDisplayCopyCurrentMetalDevice(_:)](<../coregraphics/cgdirectdisplaycopycurrentmetaldevice(__).md>) — Returns the GPU device instance that’s currently driving a display.
- [MTLDeviceNotificationHandler](mtldevicenotificationhandler.md) — A Swift closure or an Objective-C block that Metal calls when the system adds or removes a GPU device. _(deprecated)_
- [MTLDeviceNotificationName](mtldevicenotificationname.md) — A notification that represents a change to a GPU device in the system. _(deprecated)_

### Selecting GPUs

- [Adjusting for GPU memory bandwidth tradeoffs](adjusting-for-gpu-memory-bandwidth-tradeoffs.md) — Choose a suitable GPU and memory storage mode for tasks based on that GPU’s memory bandwidth on a Mac.
- [Assessing multi-GPU and multidisplay setups on an Intel-based Mac](assessing-multi-gpu-and-multi-display-setups-on-an-intel-based-mac.md) — Learn the possible GPU and display configurations for a Mac and their limitations.
- [Selecting device objects for graphics rendering](selecting-device-objects-for-graphics-rendering.md) — Switch dynamically between multiple GPUs to efficiently render to a display.
- [Selecting device objects for compute processing](selecting-device-objects-for-compute-processing.md) — Switch dynamically between multiple GPUs to efficiently execute a compute-intensive simulation.

### Working with external GPUs

- [Handling external GPU additions and removals](handling-external-gpu-additions-and-removals.md) — Register and respond to external GPU notifications that a person initiates.
- [Transferring data between connected GPUs](transferring-data-between-connected-gpus.md) — Use high-speed connections between GPUs to transfer data quickly.

## See Also

### Locating and inspecting a GPU device

- [Getting the default GPU](getting-the-default-gpu.md) — Select the system’s default GPU device on which to run your Metal code.
- [Detecting GPU features and Metal software versions](detecting-gpu-features-and-metal-software-versions.md) — Use the device object’s properties to determine how you perform tasks in Metal.
- [MTLCreateSystemDefaultDevice](<mtlcreatesystemdefaultdevice().md>) — Returns the device instance Metal selects as the default.
- [MTLDevice](mtldevice.md) — The main Metal interface to a GPU that apps use to draw graphics and run computations in parallel.
