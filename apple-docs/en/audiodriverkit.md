---
title: AudioDriverKit
framework: AudioDriverKit
symbol_kind: module
role: collection
role_heading: Framework
platforms: [DriverKit 21.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/audiodriverkit
source_url: 'https://developer.apple.com/documentation/audiodriverkit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/audiodriverkit.json'
content_hash: 'sha256:9297cb024ccb182b'
translated: false
---

> Navigation: [Technologies](technologies.md)

# AudioDriverKit

<sub>Framework</sub>

Develop drivers for audio devices.

## Overview

The AudioDriverKit framework supports the development of [DriverKit](driverkit.md)-based audio extensions that communicate with the CoreAudio HAL. AudioDriverKit handles all of the necessary user client communication between the CoreAudio HAL and the driver extension, which eliminates the need to implement an audio server plug-in. You can also integrate with transport-based driver extension frameworks like [PCIDriverKit](pcidriverkit.md).

Develop your driver by subclassing [IOUserAudioDriver](audiodriverkit/iouseraudiodriver.md). On macOS, use the [System Extensions](systemextensions.md) framework to install and upgrade your driver. On iPadOS, the system automatically discovers and upgrades drivers along with their host apps.

> [!note] Note
> AudioDriverKit is available on macOS for Intel and Apple Silicon devices, and on iPadOS for devices with an M-series processor.

## Topics

### Essentials

- [IOUserAudioObject](audiodriverkit/iouseraudioobject.md) — The base class for most classes in the framework.
- [IOUserAudioDriver](audiodriverkit/iouseraudiodriver.md) — A DriverKit provider object that manages communications with an audio device.
- [DriverKit Audio Family](bundleresources/entitlements/com.apple.developer.driverkit.family.audio.md) — A Boolean value that indicates whether the device supports audio functionality.
- [Creating an audio device driver](audiodriverkit/creating-an-audio-device-driver.md) — Implement a configurable audio input source as a driver extension that runs in user space in macOS and iPadOS.

### Working with Audio Devices

- [IOUserAudioClockDevice](audiodriverkit/iouseraudioclockdevice.md) — An audio clock device object, used to synchronize and perform I/O.
- [IOUserAudioDevice](audiodriverkit/iouseraudiodevice.md) — An audio clock device object that handles the configurations for running I/O.

### Containing Audio Objects

- [IOUserAudioBox](audiodriverkit/iouseraudiobox.md) — A container for other audio objects, typically audio devices and audio clock devices.

### Working with Audio Streams

- [IOUserAudioStream](audiodriverkit/iouseraudiostream.md) — An audio object that performs I/O for an audio device.

### Using Audio Controls

- [IOUserAudioControl](audiodriverkit/iouseraudiocontrol.md) — The base class for audio control objects.
- [IOUserAudioBooleanControl](audiodriverkit/iouseraudiobooleancontrol.md) — A control object that supports setting a Boolean value.
- [IOUserAudioStereoPanControl](audiodriverkit/iouseraudiostereopancontrol.md) — A control object that supports panning between stereo channels.
- [IOUserAudioSliderControl](audiodriverkit/iouseraudioslidercontrol.md) — A control object that supports setting a 32-bit integer value.
- [IOUserAudioSelectorControl](audiodriverkit/iouseraudioselectorcontrol.md) — A control object that supports selecting from a set of values.
- [IOUserAudioLevelControl](audiodriverkit/iouseraudiolevelcontrol.md) — A control object that supports setting an audio level, with either scalar or decibel values.

### Supporting Types

- [IOUserAudioReservedConfigChangeAction](audiodriverkit/audiodriverkit/iouseraudioreservedconfigchangeaction.md) — Identifiers for object state changes that require a configuration change.

### Namespaces

- [AudioDriverKit](audiodriverkit/audiodriverkit.md)

### Macros

- [DebugMsg](audiodriverkit/debugmsg.md)
- [FailIf](audiodriverkit/failif.md)
- [FailIfError](audiodriverkit/failiferror.md)
- [FailIfNULL](audiodriverkit/failifnull.md)
- [kIOUserAudioDriverUserClientType](audiodriverkit/kiouseraudiodriveruserclienttype.md)
