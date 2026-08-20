---
title: Audio Device Driver Programming Guide
apple_id: TP30000729
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2009-03-04'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WritingAudioDrivers/About/About.html
archived_at: '2026-07-15T07:31:40.587569Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Audio%20on%20OS%20X.md)

# Introduction to Audio Device Driver Programming Guide

This book describes the architecture, services, and mechanisms of the I/O Kit’s Audio family, and explains how you use the APIs of the family to write an audio device driver for OS X. It does not cover any aspect of user-space audio programming (MIDI, synthesizers, CD players, and so on) except to discuss the overall composition of the OS X audio system, which includes Core Audio and other audio frameworks.

To gain the most value from reading this book, it helps to be familiar with the I/O Kit and object-oriented programming, preferably C++ programming. The book _[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_ provides a thorough introduction to the I/O Kit; see [Additional Information on the I/O Kit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomrzfvbuqmrqgqwviucykjcummjqgq) for details on this and other I/O Kit documentation.

As with any kernel-level device driver, you should only write a driver if there is no other way to achieve your goals. Many audio devices are supported natively in OS X. If your device complies with USB or FireWire audio standards, you should not need to write a custom driver unless you need to implement features beyond those supported in the relevant audio standards.

In some cases, even if you need to do special device-specific processing, you may be able to do so without writing an entire driver. For example, some USB audio hardware (for USB speakers, for example) may require additional software filtering, such as equalization. OS X provides a mechanism in the kernel for doing this through the AppleUSBAudio plug-in model. For more information, see the _[SampleUSBAudioPlugin](../../../samplecode/SampleUSBAudioPlugin/SampleUSBAudioPlugin.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbxge)_ example code.

This document describes all aspects of creating an audio device driver using the I/O Kit’s Audio family. It includes conceptual and procedural information and consists of the following chapters:

- [Audio on OS X](Audio%20on%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzqfvkfawcsivddcmbr)—Describes the features, benefits, and architecture of the OS X audio system. It includes an overview of the audio I/O model.
- [Audio Family Design](Audio%20Family%20Design.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzrfvbuuqscifduurq)—Presents a comprehensive overview of the Audio family’s architecture, classes, object relationships, and primary mechanisms. It also goes into more detail about the workings of the audio I/O model in OS X.
- [Implementing an Audio Driver](Implementing%20an%20Audio%20Driver.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzsfvbecsseizcessa)—Describes the various steps required to design and implement an audio device driver using the Audio family. Most steps are amply illustrated with sample code.

For details of specific methods, structures, and other API elements, consult the reference documentation for the Audio family. See [Additional Information on the I/O Kit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomrzfvbuqmrqgqwviucykjcummjqgq) for instructions on accessing this documentation.

Apple offers several other resources to developers of audio software for OS X, including:

- See [http://developer.apple.com/audio](https://developer.apple.com/audio) for a page full of links to audio-related material.
- See _Core Audio_ for a description of the Core Audio framework (Audio HAL).
- For information on MIDI frameworks, see _[CoreMIDI Framework Reference](https://developer.apple.com/documentation/coremidi)_ and _CoreMIDIServer Framework Reference_.
- See `/Developer/Examples/Kernel/IOKit/Audio` for some sample audio driver projects and other code examples relevant to audio development.

### Additional Information on the I/O Kit

For additional information on the I/O Kit in general, see the following documents:

- Overviews of the Darwin kernel, including _[Kernel Programming Guide](../../Darwin/Kernel%20Programming%20Guide/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbv)_.
- The aforementioned _[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_ describes the features, architecture, classes, and general mechanisms of the I/O Kit and includes discussions of driver matching and loading, event handling, memory management, and power management.
- _[IOKit Device Driver Design Guidelines](../IOKit%20Device%20Driver%20Design%20Guidelines/Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmoju)_, which describes the general steps required to design, code, debug, and build a device driver that will be resident in the kernel.
- _[Kernel Extension Programming Topics](../../Darwin/Kernel%20Extension%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrt)_, a collection of tutorials that introduce you to the development tools and take you through the steps required to create, debug, and package kernel extensions and I/O Kit drivers (a type of kernel extension).
- Reference documentation on I/O Kit families and classes.

Of course, you can always browse the header files shipped with the I/O Kit, which are installed in `Kernel.framework/Headers/iokit` (kernel-resident) and `IOKit.framework/Headers` (user-space).

The documentation is in HTML or PDF format. You can access the HTML documentation (and download the PDF) from the Xcode Help menu. To view, click Help > Show Documentation Window. You can then search for specific API or view the entire developer documentation library. You can also access developer documentation on the Apple Developer Connection website at [http://developer.apple.com/documentation/index.html](https://developer.apple.com/documentation/index.html).

### Other Information on the Web

Apple maintains websites where developers can go for general and technical information on OS X.

- Apple Developer Connection: OS X ([http://developer.apple.com/devcenter/macosx](https://developer.apple.com/devcenter/macosx)) offers SDKs, release notes, product notes and news, and other resources and information related to OS X.
- Apple Support Area ([http://www.apple.com/support/](http://www.apple.com/support/)) enables you to locate technical articles on OS X (and other areas) using a natural language search.

[Next](Audio%20on%20OS%20X.md)

