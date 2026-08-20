---
title: Audio Unit Programming Guide
apple_id: TP40003278
resource_type: Guide
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/MusicAudio/Conceptual/AudioUnitProgrammingGuide/Introduction/Introduction.html
archived_at: '2026-07-15T08:17:32.038139Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Audio%20Unit%20Development%20Fundamentals.md)

# Introduction

This document describes _audio units_ and how to create them. Audio units are digital audio plug-ins based on Apple’s world class Core Audio technology for OS X.

As a hobbyist or a computer science student, you can design and build your own audio units to make applications like GarageBand do new things with sound.

As a commercial developer, you can create professional quality software components that provide features like filtering, reverb, dynamics processing, and sample-based looping. You can also create simple or elaborate MIDI-based music synthesizers, as well as more technical audio units such as time and pitch shifters and data format converters.

As part of Core Audio and being integral to OS X, audio units offer a development approach for audio plug-ins that excels in terms of performance, robustness, and ease of deployment. With audio units, you also gain by providing a consistent, simple experience for end-users.

Your target market is wide, including performers, DJs, recording and mastering engineers, and anyone who likes to play with sound on their iMac.

To use this document, you should already be familiar with the C programming language. You should be comfortable with using Xcode to create an OS X plug-in as described in the _[Xcode Overview](https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/index.html#//apple_ref/doc/uid/TP40010215)_. For example, you should know about Xcode’s various build options, such as ZeroLink, and when to use them. You should also know how and why to include frameworks and files in the linking phase of an Xcode build.

It’s very helpful in using this document to have enough familiarity with the C++ programming language to read header and implementation files. It’s also helpful to have a basic understanding of the OS X Component Manager as described in _[Component Manager for QuickTime](../../Quick%20Time/Component%20Manager%20for%20QuickTime/Introduction%20to%20Component%20Manager%20for%20QuickTime.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnjy)_, as well as a grounding in digital audio coding and audio DSP (digital signal processing).

This document does not address the needs of audio unit host application developers, whose code opens, connects, and uses audio units. Nor is this document an audio unit cookbook. It devotes very few pages to DSP or music synthesis techniques, which work essentially the same way in audio units as in other audio software technologies

Depending on your needs and your learning style, you can use this document in the following ways.

- If you want to get your hands on building an audio unit right away, go straight to [Tutorial: Building a Simple Effect Unit with a Generic View](Tutorial-%20Building%20a%20Simple%20Effect%20Unit%20with%20a%20Generic%20View.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenzyfvbuqnjnknlti). As you build the audio unit, you can refer to other sections in this document for conceptual information related to what you’re doing.
- If you prefer to build your knowledge incrementally, starting with a solid conceptual foundation before seeing the technology in action, read the chapters in order.
- If you already have some familiarity with building your own audio units, you may want to go straight to [The Audio Unit](The%20Audio%20Unit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenzyfvbuqmjsfvjvomi) and [Appendix: Audio Unit Class Hierarchy](Appendix-%20Audio%20Unit%20Class%20Hierarchy.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenzyfvbuqojnknlte). You might also want to review [A Quick Tour of the Core Audio SDK](A%20Quick%20Tour%20of%20the%20Core%20Audio%20SDK.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenzyfvbuqmjrfvjvomi) to see if the SDK contains some treasures you haven’t been using until now.

This document contains the following chapters:

- Audio Unit Development Fundamentals, a bird's eye view of audio unit development, covering Xcode, the Core Audio SDK, design, development, testing, and deployment
- The Audio Unit, design and programming considerations for the part of an audio unit that performs the audio work
- The Audio Unit View, a description of the two audio unit view types—generic and custom—as well as an explanation of parameter automation
- A Quick Tour of the Core Audio SDK: Taking advantage of the code in the Core Audio SDK is the fastest route to audio unit development
- Tutorial: Building a Simple Effect Unit with a Generic View, a tutorial that takes you from zero to a fully functioning effect unit
- Appendix: Audio Unit Class Hierarchy, a tour of the audio unit class hierarchy provided by the Core Audio SDK

To go forward in developing your own audio units based on what you learn here, you will need:

- The ability to develop plug-ins using the C++ programming language, because the audio unit class hierarchy in the Core Audio SDK uses C++.
- A grounding in audio DSP, including the requisite mathematics. Alternatively, you can work with someone who can provide DSP code for your audio units, along with someone who can straddle the audio unit and math worlds. For optimum quality and performance of an audio unit, DSP code needs to be correctly incorporated into the audio unit scaffolding.
- A grounding in MIDI, if you are developing instrument units.

When you perform a full installation of the current version of OS X, including Xcode Tools, you’ll have everything you need on your system for audio unit development. These items are also available free from Apple’s developer website, [http://developer.apple.com](https://developer.apple.com/):

- _The latest version of Xcode._ The examples in this document use Xcode version 2.4.
- _The latest OS X header files._ The examples in this document use the header files in the 10.4.0 OS X SDK, installed with Apple’s Xcode Tools.
- _The latest Core Audio development kit._ The examples in this document use Core Audio SDK v1.4.3, installed with Apple’s Xcode Tools at this location on your system: `/Developer/Examples/CoreAudio`
- _At least one audio unit hosting application._ Apple recommends the AU Lab application, installed with Apple’s Xcode Tools at this location on your system: `/Developer/Applications/Audio/AU Lab`
- _The audio unit validation command-line tool_, `auval`, Apple’s validation tool for audio units, provided with OS X.

As you learn about developing audio units, you may find the following information and tools helpful:

- The [coreaudio-api mailing list](http://www.lists.apple.com/mailman/listinfo/coreaudio-api), a very active discussion forum hosted by Apple that covers all aspects of audio unit design and development.
- Audio Unit framework API documentation (preliminary), available from the [Audio Topic](https://developer.apple.com/audio/) page on Apple’s [developer website](https://developer.apple.com/).
- Additional audio unit API reference available in the [Core Audio Framework Reference](https://developer.apple.com/documentation/MusicAudio/Reference/CACoreAudioReference/) in Apple’s Reference Library.
- The [TremoloUnit](https://developer.apple.com/samplecode/TremoloUnit/) sample project, which corresponds to the audio unit you build in [Tutorial: Building a Simple Effect Unit with a Generic View](Tutorial-%20Building%20a%20Simple%20Effect%20Unit%20with%20a%20Generic%20View.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenzyfvbuqnjnknlti).
- _[Core Audio Overview](../Core%20Audio%20Overview/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztknzx)_, which surveys all of the features available in Core Audio, and describes where audio units fit in.
- _[Bundle Programming Guide](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_, which describes the file-system packaging mechanism in OS X used for audio units.
- _[Component Manager Reference](https://developer.apple.com/documentation/coreservices/carbon_core/component_manager)_, which describes the API of the Component Manager, the OS X technology that manages audio units at the system level. To learn more about the Component Manager you can refer to _[Component Manager for QuickTime](../../Quick%20Time/Component%20Manager%20for%20QuickTime/Introduction%20to%20Component%20Manager%20for%20QuickTime.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnjy)_.
[Next](Audio%20Unit%20Development%20Fundamentals.md)

