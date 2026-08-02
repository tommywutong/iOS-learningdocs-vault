---
title: QuickTime 2.0 & MIDI
apple_id: DTS10001940
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qtma/qtma03.html
archived_at: '2026-07-18T02:38:46.321929Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Audio](https://developer.apple.com/referencelibrary/QuickTime/idxMusicAudio-date.html)

|  |
| --- |
| Technical Q&A QTMA03QuickTime 2.0 & MIDI |

|  |
| --- |
| Q The READ ME file on the System 7.5 disk says that there are approximately 42 MIDI instruments in the QuickTime MIDI Musical Instruments extension, but it doesn't list any of them or indicate their relationship to General MIDI. It also doesn't state whether you can play an existing MIDI file using QuickTime 2.0. I am interested in experimenting with this as a developer. Where can I find information on QuickTime 2.0 MIDI support?   A Here's a brief introduction on how to use QuickTime 2.0 Music Tracks with the MIDI Manager. Converting Std MIDI files to QuickTime Music Track Movies:  To play an existing MIDI file using QuickTime 2.0, you need MoviePlayer 1.1d1 or later. In MoviePlayer, choose Open or Import in the file menu to select a Standard MIDI file, and then choose Convert. Click the Options button in the Save Converted File As dialog box to access additional dialog boxes that allow you to change the instrument settings. Then, when you save the file, it is saved as a Movie with a music track. Once you have a movie that contains a music track, MoviePlayer 1.1d1's GetInfo menu displays a dialog box that shows a popup menu. Select Music Track and Instruments, and double-click on an instrument in the list to bring up the Instrument Picker dialog.  Playing a movie's music track on internal synth voices or on an external MIDI device:  To switch the default setting of a music track, you need a specific configuration control device that is available on the QuickTime 2.0 SDK CD. This application lets you switch the default from internal synth to external MIDI synth.  Recording MIDI in a QuickTime 2.0 MusicTrack Movie:  Use the Grab Exerciser application to open a musicTrack sequence grabber channel. Select Record, and start sending MIDI data from your external MIDI device. Click the mouse to stop recording. Save the file you have created, and use MoviePlayer to play it.  Playing internal synth voices from external MIDI devices:  Use the Grab Exerciser application to open a musicTrack sequence grabber channel, but don't record anything -- just use the channel's pass-through feature. Make sure the port your MIDI interface is connected to is also connected between QuickTime and the Apple MIDI Driver in the MidiManagers PatchBay. The internal synth must also be selected in the Music Device dialog  Playing internal synth voices from your MIDI manager-compatible application:  Use the Grab Exerciser application to open a musicTrack sequence grabber channel, but don't record anything -- just use the channel's pass-through feature. Make sure the port your MIDI interface is connected to is also connected between QuickTime and the Apple MIDI Driver in the MidiManagers PatchBay. The internal synth must also be selected in the Music Device dialog, but connect your application's MIDI Manager port to QuickTime in PatchBay instead of connecting QuickTime to the Apple MIDI Driver port.  Note: Instead of using the Grab Exerciser, you can use the MyCaptureApp DTS sample application, which includes source code for opening a sequence grabber channel. [May 01 1995] |

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
