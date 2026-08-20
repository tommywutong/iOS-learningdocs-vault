---
title: Capturing Speech Manager Output
apple_id: DTS10002182
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-05-18'
source_url: https://developer.apple.com/library/archive/qa/snd/snd15.html
archived_at: '2026-07-18T02:38:54.685854Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Audio](https://developer.apple.com/library/archive/technicalqas/MusicAudio/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/MusicAudio/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Audio > Carbon](https://developer.apple.com/referencelibrary/MusicAudio/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A SND15Capturing Speech Manager Output |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Q Is it possible to capture the output from the Speech Synthesis Manager so I can save it to a file or modify it?   A There is no direct provision in the Speech Synthesis Manager for doing this; however, it is possible if you are willing to do it in a roundabout fashion. The Speech Synthesis Manager, via the `soSoundOutput` selector, has the ability to direct speech to any arbitrary sound output device. Because the Speech Synthesis Manager speaks by creating buffers of speech and then playing those buffers via the Sound Manager, it can use the Sound Manager's ability to [direct sounds to a specific sound output component.](https://developer.apple.com/documentation/mac/Sound/Sound-97.html#HEADING97-0)  This feature was designed so that the Speech Synthesis Manager could speak over the phone, but it is not limited to just talking over the phone. If you create a sound output component that saves the sounds played to it (either to memory or to a file), you can have the Speech Synthesis Manager speak to this sound output component and use it to capture the Speech Synthesis Manager's output. From here, you can do whatever you want with the captured sound.  A DTS sample called [AIFF-Writer](https://developer.apple.com/samplecode/Sample_Code/Sound.htm) is a sample sound output component that saves whatever sound is played through it to an AIFF file, so this is a good starting point for the sound output component.  The [Component Manager](https://developer.apple.com/documentation/mac/MoreToolbox/MoreToolbox-333.html#HEADING333-0) allows you to register a component from any resource file. Normally components are in separate files placed in the Extensions folder, but this is not a requirement. For instance, your component can reside in your application's resource fork rather than in a separate file. Furthermore, the Component Manager allows you to register a component locally so that it is available only to your application and the Mac OS. This ability allows for the stealthy use of the AIFF-Writer component (or any other component). The user does not ever have to know that you have installed your custom version of the AIFF-Writer component. You can install it, select it, use it, and unregister it--all without the user ever knowing that anything interesting happened.   |  | | --- | | Note: The installation of your custom sound output component does not affect the normal playing of sounds from your application or any other application. Only sounds that are specifically directed to your custom sound output component will play through it. |     |  | | --- | | Note: When sounds are being played to your custom sound output device component, they are not heard (because they are not going to the default sound output component). If you want them to be heard, you will have to play the sound twice, once to the default sound output device (so it can be heard), and once to your custom output device (so it can be captured). The Sound Manager will allow you to play a sound simultaneously to multiple different output components, so playing the sound twice does not require any extra time. |   Here is some sample code that shows how to install and use your custom sound output component with the Speech Synthesis Manager:   |  | | --- | | ```     OSErr                   theErr              = noErr;     ComponentDescription    writerOutputDev;     Component               theWriterComponent  = 0;     SpeechChannel           theWriterSpeechChan = nil;      // Load the AIFF-Writer component resources from our resource fork     numCompsReg = RegisterComponentResourceFile (CurResFile(), 0);      writerOutputDev.componentType = kSoundOutputDeviceType;     writerOutputDev.componentSubType = 'AIFW';     writerOutputDev.componentManufacturer = kAppleManufacturer;     writerOutputDev.componentFlags = 0;     writerOutputDev.componentFlagsMask = 0;      // Find AIFF-Writer's component instance     theWriterComponent = FindNextComponent (0, &writerOutputDev);      theErr = NewSpeechChannel (nil, &theWriterSpeechChan);     if (theErr != noErr)         return theErr;      // Change output device to talk through AIFF-Writer     theErr = SetSpeechInfo (theWriterSpeechChan, soSoundOutput, &theWriterComponent); ``` |  Further References  |  | | --- | | - [Inside   Macintosh: Sound](https://developer.apple.com/documentation/mac/Sound/Sound-2.html) - [Inside   Macintosh: Sound, Chapter 4 - Speech Manager](https://developer.apple.com/documentation/mac/Sound/Sound-187.html#HEADING187-0) - [Inside   Macintosh: More Macintosh Toolbox, Chapter 6 - Component   Manager](https://developer.apple.com/documentation/mac/MoreToolbox/MoreToolbox-333.html#HEADING333-0) - [QuickTime   3.0 Documentation](https://developer.apple.com/documentation/quicktime/qtdevdocs/RM/frameset.htm) |    [May 18 1998] |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
