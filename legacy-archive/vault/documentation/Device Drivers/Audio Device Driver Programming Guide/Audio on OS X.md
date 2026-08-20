---
title: Audio Device Driver Programming Guide
apple_id: TP30000729
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2009-03-04'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WritingAudioDrivers/AudioOnMacOSX/AudioOnMacOSX.html
archived_at: '2026-07-15T07:31:43.515695Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Audio Device Driver Programming Guide](Introduction%20to%20Audio%20Device%20Driver%20Programming%20Guide.md)


[Next](Audio%20Family%20Design.md)[Previous](Introduction%20to%20Audio%20Device%20Driver%20Programming%20Guide.md)

# Audio on OS X

This chapter gives an overview of audio on OS X, describing its capabilities, its interrelated technologies, and its architecture. Reading this chapter will help you to understand how the I/O Kit’s Audio family fits together and interacts with the other pieces of audio software on OS X.

In versions of Macintosh system software prior to OS X, the sound capabilities of a system largely depended on the availability of third-party audio and MIDI protocols and services. Apple has designed the OS X audio system to consolidate, integrate, and standardize these services and protocols, thereby streamlining configuration of audio and MIDI devices and development of future audio and MIDI technologies.

Audio on OS X comprises several audio technologies that, taken together, offer the following capabilities:

- Built-in support for a variety of audio formats, including formats based on pulse code modulation (PCM) and encoded formats such as AC-3 and MP3
- Multi-channel audio I/O that is scalable to a virtually unlimited number of channels
- Variable sample rates
- A remarkably clean signal path requiring little overhead
- Simultaneous access for multiple clients to all of the audio devices attached to the host, no matter how the connection is made (PCI, USB, FireWire, and so on)

Outside the kernel, OS X represents audio as 32-bit floating point data; this format allows efficient processing of data with today’s advanced audio peripherals (for example, those capable of 24-bit, 192 kHz operation) and ensures that the system can scale to future high-resolution formats.

The audio capabilities of OS X arise from several software technologies that are accessible through their public programming interfaces. These technologies are situated at different levels of the operating system where their relationships with each other can be characterized as client and provider. In other words, OS X audio software is layered, with one layer dependent on the layer “under” it and communicating, through defined interfaces, with adjoining layers (see [Figure 1-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzqfvbeeq2ginduurq)).

The relative locations of these technologies within the layers of system software suggest their degree of abstraction and their proximity to audio hardware. Some audio technologies in OS X are incorporated into the kernel environment (that is, Darwin) while others are packaged as frameworks for use by application environments, applications, and other user processes.

__Figure 1-1__  OS X audio layers

![OS X audio layers](attachments/Art/audioarchitecture.gif)

At the lowest level of the OS X audio stack is the driver that controls audio hardware. The driver is based on the I/O Kit’s audio family, which provides much of the functionality and data structures needed by the driver. For example, the Audio family implements the basic timing mechanisms, provides the user-client objects that communicate with the upper layers, and maintains the sample and mix buffers (which hold audio data for the hardware and the hardware’s clients, respectively).

The basic role of the audio driver is to control the process that moves audio data between the hardware and the sample buffer. It is responsible for providing that sample data to the upper layers of the system when necessary, making any necessary format conversions in the process. In addition, an audio driver must make the necessary calls to audio hardware in response to format and control changes (for example, volume and mute).

Immediately above the driver and the I/O Kit’s Audio family—and just across the boundary between kernel and user space—is the Audio Hardware Abstraction Layer (HAL). The Audio HAL functions as the device interface for the I/O Kit Audio family and its drivers. For input streams, its job is to make the audio data it receives from drivers accessible to its clients. For output streams, its job is to take the audio data from its clients and pass it to a particular audio driver.

The Audio Units and Audio Toolbox frameworks are two other frameworks that provide specialized audio services. They are both built on top of the Audio HAL, which is implemented in the Core Audio framework.

MIDI System Services, which comprises two other frameworks, is not directly dependent on the Audio HAL. As its name suggests, MIDI System Services makes MIDI services available to applications and presents an API for creating MIDI drivers.

Finally, the ultimate clients of audio on OS X—applications, frameworks, and other user processes—can directly access the Audio HAL or indirectly access it through one of the higher-level audio frameworks. They can also indirectly access the Audio HAL through the audio-related APIs of the application environments they belong to: Sound Manager in Carbon, [NSSound](https://developer.apple.com/documentation/appkit/nssound) in Cocoa, and the Java sound APIs.

The following sections examine each of these audio technologies of OS X in more detail.

The Audio Hardware Abstraction Layer (HAL) is the layer of the OS X audio system that acts as an intermediary between the I/O Kit drivers controlling audio hardware and the programs and frameworks in user space that are clients of the hardware. More specifically, the Audio HAL is the standardized device interface for the I/O Kit’s Audio family. It is implemented in the Core Audio framework (`CoreAudio.framework`) and presents both C-language and Java APIs. In the Audio HAL, all audio data is in 32-bit floating point format.

The API of the Audio HAL includes three main abstractions: audio hardware, audio device, and audio stream.

- The audio hardware API gives clients access to audio entities that exist in the “global” space, such as the list of current devices and the default device.
- The audio device API enables clients to manage and query a specific audio device and the I/O engines that it contains. An audio device in the Audio HAL represents a single I/O cycle, a clock source based on it, and all the buffers that are synchronized to this cycle. The audio device methods permit a client to, among other things, start and stop audio streams, retrieve and translate the time, and get and set properties of the audio device.
- The audio stream API enables a client to control and query an audio stream. Each audio device has one or more audio streams, which encapsulate the buffer of memory used for transferring audio data across the user/kernel boundary. They also specify the format of the audio data.

The abstractions of audio device and audio stream loosely correspond to different I/O Kit Audio family objects in the kernel (see [The Audio Family](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzqfvbeeq2fineuisi)). For example, the entity referred to as “audio device” in the Audio HAL corresponds to a combination of an [IOAudioDevice](https://developer.apple.com/documentation/kernel/ioaudiodevice) and [IOAudioEngine](https://developer.apple.com/documentation/kernel/ioaudioengine) in the kernel. For each [IOAudioEngine](https://developer.apple.com/documentation/kernel/ioaudioengine) the Audio HAL finds in the kernel, it generates an audio-device identifier. However, there is considerable overlap of role among the various Audio family and Audio HAL objects and entities.

A critical part of the APIs for audio hardware, devices, and streams involves audio properties and their associated notifications. These APIs allow clients to get and set properties of audio hardware. The “get” methods are synchronous, but the “set” methods work in an asynchronous manner that makes use of notifications. Clients of the Audio HAL implement “listener procs”—callback functions for properties associated with audio hardware, audio devices, or audio streams. When an audio driver changes a property of the hardware, either as a result of user manipulation of a physical control or in response to a “set” method, it sends notifications to interested Audio HAL clients. This results in the appropriate “listener procs” being called.

Just as important as the property APIs is the callback prototype ([AudioDeviceIOProc](https://developer.apple.com/documentation/coreaudio/audiodeviceioproc)) that the audio-device subset of the Audio HAL API defines for I/O management. Clients of the Audio HAL must implement a function or method conforming to this prototype to perform I/O transactions for a given device. Through this function, the Audio HAL presents all inputs and outputs simultaneously in an I/O cycle to the client for processing. In this function, a client of the Audio HAL must send audio data to the audio device (for output), or copy and process the audio data received from the audio device (for input).

OS X has several frameworks other than the Core Audio framework that offer audio-related functionality to applications. Two of these frameworks—Audio Units and Audio Toolbox—are built directly on the Core Audio framework. MIDI System Services (consisting of the Core MIDI and Core MIDI Server frameworks) does not directly depend on the Core Audio framework, but is still a consumer of the services of the audio frameworks.

All of these secondary frameworks are implemented in the C language and present their public programming interfaces in C. Thus, any application or other program in any application environment can take advantage of their capabilities.

The Audio Units framework (`AudioUnits.framework`) provides support for generating, processing, receiving, and manipulating or transforming streams of audio data. This functionality is based on the notion of audio units.

Audio units are one form of a building block called a component. A component is a piece of code that provides a defined set of services to one or more clients. In the case of audio units, these clients can use audio unit components either singly or connected together to form an audio signal graph. To compose an audio signal graph, clients can use the AUGraph API in the Audio Toolbox framework—see [Audio Toolbox](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzqfvbeeq2firfeqry) for details.

An audio unit can have one or more inputs and outputs. The inputs can accept either encoded audio data or MIDI data. The output is generally a buffer of audio data. Using a “pull I/O” model, an audio unit specifies the number and format of its inputs and outputs through its properties. Each output is in itself a stream of an arbitrary number of interleaved audio channels derived from the audio unit’s inputs. Clients also manage the connections between units through properties.

Examples of audio units are DSP processors (such as reverbs, filters, and mixers), format converters (for example, 16-bit integer to floating-point converters), interleavers-deinterleavers, and sample rate converters. In addition to defining the interface for custom audio units in the Audio Units framework, Apple ships a set of audio units. One of these is the MusicDevice component, which presents an API targeted specifically toward software synthesis.

The Audio Toolbox framework (`AudioToolbox.framework`) complements the Audio Units framework with two major abstractions: the AUGraph and the Music Player.

An AUGraph provides a complete description of an audio signal processing network. It is a programmatic entity that represents a set of audio units and the connections (input and output) among them. With the AUGraph APIs, you can construct arbitrary signal paths through which audio can be processed. Audio graphs enact real-time routing changes while audio is being processed, creating and breaking connections between audio units “on the fly,” thus maintaining the representation of the graph even when constituent audio units have not been instantiated.

The Music Player APIs use AUGraphs to provide the services of a sequencing toolbox that collects audio events into tracks, which can then be copied, pasted, and looped within a sequence. The APIs themselves consist of a number of related programmatic entities. A Music Player plays a Music Sequence, which can be created from a standard MIDI file. A Music Sequence contains an arbitrary number of tracks (Music Tracks), each of which contains timestamped audio events in ascending temporal order. A Music Sequence usually has an AUGraph associated with it, and a Music Track usually addresses its audio events to a specific Audio Unit within the graph. Events can involve tempo and extended events, as well as regular MIDI events.

The Audio Toolbox framework also includes APIs for converting audio data between different formats.

MIDI System Services is a technology that allows applications and MIDI devices to communicate with each other in a single, unified way. It comprises two frameworks: Core MIDI ([CoreMIDI.framework](https://developer.apple.com/documentation/coremidi)) and Core MIDI Server (`CoreMIDIServer.framework`).

MIDI System Services gives user processes high-performance access to MIDI hardware. In a manner similar to the Audio HAL, MIDI System Services implements a plug-in interface that enables clients to communicate with a MIDI device driver.

Apple provides several default MIDI drivers for interfaces that comply with USB and FireWire MIDI interface standards. Using the Core MIDI Server framework, third-party MIDI manufacturers can create their own driver plug-ins to support additional device-specific features. A MIDI server can then load and manage those drivers.

Applications can communicate with MIDI drivers through the client-side APIs of the Core MIDI framework.

The I/O Kit’s Audio family facilitates the creation of drivers for audio hardware. Drivers created through the Audio family can support any hardware on the system, including PCI, USB, and FireWire devices. Essentially, an I/O Kit audio driver transfers audio data between the hardware and the Audio HAL. It provides one or more sample buffers along with a process that moves data between the hardware and those sample buffers. Typically this is done with the audio hardware’s DMA engine.

Because the native format of audio data on OS X is 32-bit floating point, the driver must provide routines to convert between the hardware format of the data in the sample buffer and 32-bit floating point. The sequence of steps that a driver follows depends on the direction of the stream. For example, with input audio data, the driver is asked for a block of data. It obtains it from the sample buffer, converts it to the expected client format (32-bit floating point), and returns it. That data is then passed by the family to the Audio HAL through a user-client mechanism.

The interactions between the DMA engine, the driver, and the Audio HAL, are based on the assumption that, in any one direction, the stream of audio data proceeds continuously at the same rate. The Audio family sets up several timers (based on regularly taken timestamps) to synchronize the actions of the agents involved in this transfer of data. These timing mechanisms ensure that the audio data is processed at maximum speed and with minimum latency.

Take again an input stream as an example. Shortly after the DMA engine writes sample frames to the driver’s sample buffer, the driver reads that data, converts the integer format to 32-bit floating point, and writes the resulting frames to the mixer buffer, from whence they are passed on to the Audio HAL. Optionally, just before the DMA engine writes new frames to the same location in the sample buffer, an “erase head” zero-initializes the just-processed frames. (By default, however, the erase head only runs on output streams.)

For more on the sample buffer and the timer mechanisms used by the Audio family, see [The Audio I/O Model on OS X](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzqfvbeeq2dindemqi).

An I/O Kit audio driver consists of a number of objects, the most important of which are derived from the [IOAudioDevice](https://developer.apple.com/documentation/kernel/ioaudiodevice), [IOAudioEngine](https://developer.apple.com/documentation/kernel/ioaudioengine), [IOAudioStream](https://developer.apple.com/documentation/kernel/ioaudiostream), and [IOAudioControl](https://developer.apple.com/documentation/kernel/ioaudiocontrol) classes. These objects perform the following roles for the driver:

- A single instance of a custom subclass of [IOAudioDevice](https://developer.apple.com/documentation/kernel/ioaudiodevice) represents the audio device itself. The [IOAudioDevice](https://developer.apple.com/documentation/kernel/ioaudiodevice) subclass is the root object of a complete audio driver. It is responsible for mapping all hardware resources from the service-provider’s nub and for controlling all access to the hardware (handled automatically through a provided command gate). An [IOAudioDevice](https://developer.apple.com/documentation/kernel/ioaudiodevice) object manages one or more [IOAudioEngine](https://developer.apple.com/documentation/kernel/ioaudioengine) objects.
- An audio driver must contain one or more instances of a custom subclass of [IOAudioEngine](https://developer.apple.com/documentation/kernel/ioaudioengine). This custom subclass manages each audio I/O engine associated with the audio device. Its job is to control the process that transfers data between the hardware and a sample buffer. Typically the I/O process is implemented as a hardware DMA engine (although it doesn’t have to be). The sample buffer must be implemented as a ring buffer so that when the I/O process of a running [IOAudioEngine](https://developer.apple.com/documentation/kernel/ioaudioengine) reaches the end of the buffer, it wraps back around to the beginning and keeps going.

  An [IOAudioEngine](https://developer.apple.com/documentation/kernel/ioaudioengine) object is also responsible for starting and stopping the engine, and for taking a timestamp each time the sample buffer wraps around to the beginning. It contains one or more [IOAudioStream](https://developer.apple.com/documentation/kernel/ioaudiostream) objects and can contain any number of [IOAudioControl](https://developer.apple.com/documentation/kernel/ioaudiocontrol) objects.

  All sample buffers within a single [IOAudioEngine](https://developer.apple.com/documentation/kernel/ioaudioengine) must be the same size and running at the same rate. If you need to handle more than one buffer size or sampling rate, you must use more than one [IOAudioEngine](https://developer.apple.com/documentation/kernel/ioaudioengine).
- An instance of [IOAudioStream](https://developer.apple.com/documentation/kernel/ioaudiostream) represents a sample buffer, the associated mix buffer, and the direction of the stream. The [IOAudioStream](https://developer.apple.com/documentation/kernel/ioaudiostream) object also contains a representation of the current format of the sample buffer as well as a list of allowed formats for that buffer.
- An instance of [IOAudioControl](https://developer.apple.com/documentation/kernel/ioaudiocontrol) represents any controllable attribute of an audio device, such as volume or mute.

An I/O Kit audio driver uses two user-client objects to communicate with the Audio HAL layer. The Audio HAL communicates with the [IOAudioEngine](https://developer.apple.com/documentation/kernel/ioaudioengine) and [IOAudioControl](https://developer.apple.com/documentation/kernel/ioaudiocontrol) objects through the [IOAudioEngineUserClient](https://developer.apple.com/documentation/kernel/ioaudioengineuserclient) and [IOAudioControlUserClient](https://developer.apple.com/documentation/kernel/ioaudiocontroluserclient) objects, respectively. The audio family creates these objects as they are needed. The [IOAudioEngineUserClient](https://developer.apple.com/documentation/kernel/ioaudioengineuserclient) class provides the main linkage to an [IOAudioEngine](https://developer.apple.com/documentation/kernel/ioaudioengine) subclass; it allows the Audio HAL to control the [IOAudioEngine](https://developer.apple.com/documentation/kernel/ioaudioengine) and it enables the engine to pass notifications of changes back to the Audio HAL. For each [IOAudioControl](https://developer.apple.com/documentation/kernel/ioaudiocontrol) object in the driver, an [IOAudioControlUserClient](https://developer.apple.com/documentation/kernel/ioaudiocontroluserclient) object passes notifications of value changes to the Audio HAL.

For more detailed information on the classes and general architecture of the Audio family, see the chapter [Audio Family Design](Audio%20Family%20Design.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzrfvbuuqscifduurq).

Apple ships several audio device drivers with a standard OS X installation. These drivers are suitable for much of the audio hardware commonly found on Power PC computers. The “onboard driver” kernel extension—`AppleOnboardAudio.kext`—contains almost a half dozen audio drivers packaged as plug-ins. Each of these drivers is based on a specific subclass of [IOAudioDevice](https://developer.apple.com/documentation/kernel/ioaudiodevice) and each uses the code in the AppleDBDMAAudio kernel extension for the [IOAudioEngine](https://developer.apple.com/documentation/kernel/ioaudioengine) subclass. The I/O Kit, through its matching process, finds and loads the appropriate plug-ins based on existing audio hardware. For USB audio hardware, Apple includes the driver defined in the `AppleUSBAudio.kext` kernel extension.

Mac OS 9 and OS X perform audio I/O in very different ways. The differences between them are most salient in the lower layers of the audio stack, particularly the audio driver model and the audio access libraries.

In Mac OS 9, an audio driver’s DMA engine transfers audio data between a sample buffer, which is provided by the driver, and the hardware. The buffer holds a segment of the audio data containing a sequence of sample frames in temporal order.

The Mac OS 9 driver model uses double buffering to exchange audio data between the driver and its clients, so there are actually two sample buffers. In the case of audio output, after the driver’s clients (using the Sound Manager API) fill one of the buffers, the hardware (usually through its DMA engine) signals the driver (typically through an interrupt) that it is finished playing the other buffer and ready for more data. The driver then gives the hardware the buffer it just filled, receives the just-played buffer from the hardware, and signals the application that it needs more data.

__Figure 1-2__  Access to the sample buffer on Mac OS 9

![Access to the sample buffer on Mac OS 9](attachments/Art/os9audio.gif)

The architecture and goals of OS X made this design untenable. With the OS X kernel, an audio driver incurs a greater cost than on Mac OS 9 when it signals an application that more audio data is needed (or that new data is available). Moreover, a major goal of the OS X audio system is to support multiple simultaneous clients, which is not possible with the Mac OS 9 model. A new audio I/O model was needed not only for this goal but also to provide the highest possible performance and the lowest possible latency. [Figure 1-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzqfvbeeq2ijfdegrq) depicts the audio I/O model on OS X.

__Figure 1-3__  The OS X audio model

![The OS X audio model](attachments/Art/osXaudio.gif)

The key facet of the OS X audio I/O model involves predictive timing mechanisms. Instead of requiring the driver to message an application directly when an I/O cycle has completed, the timing mechanisms enable the Audio HAL to predict when the cycle will complete. The Audio HAL uses the extremely accurate timing code on OS X to ensure that clients perform their I/O at the proper time, based on the size of their buffers. The audio driver does its part to make this possible by setting up the hardware’s sample buffer as a ring buffer and by taking an accurate timestamp every time the I/O engine wraps to the beginning of the buffer.

The Audio HAL keeps track of each timestamp and uses the sequence of timestamps to predict the current location of the audio I/O engine (in terms of sample frame read or written) at any time. Given that information, it can predict when a cycle will complete and sets its wake-up timestamp accordingly. This model, combined with the ability of the I/O Kit Audio family to receive audio data from each client asynchronously, allows any number of clients to provide audio data that gets mixed into the final output. It also allows different client buffer sizes; one client can operate at a very low buffer size (and a correspondingly low latency) while at the same time another client may use a much larger buffer. As long as the timestamps provided by the driver are accurate, the family and the Audio HAL do all of the work to make this possible.

Another important difference between the audio I/O model on Mac OS 9 and the one on OS X is the native format of audio data in the system. In Mac OS 9, because the application (through the Sound Manager) has direct access to the hardware buffer, it has to deal with the native hardware format. Because of this reality, the Mac OS 9 audio libraries only support 16-bit one-channel or two-channel PCM audio data to simplify things.

In OS X, an application cannot directly access the sample buffer. This indirection permits the use of the 32-bit floating point format between the Audio HAL and an audio driver. Consequently, the driver is responsible for providing a routine that can clip and convert that 32-bit floating point output data into the buffer’s native format. It might also have to implement a routine to convert input data into 32-bit floating point. Both routines are called asynchronously as Audio HAL clients pass audio data to the driver and receive data from it.

For detailed information on the OS X audio I/O model, see [The Audio I/O Model Up Close](Audio%20Family%20Design.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzrfvbuuqsjiraueri).

[Next](Audio%20Family%20Design.md)[Previous](Introduction%20to%20Audio%20Device%20Driver%20Programming%20Guide.md)

