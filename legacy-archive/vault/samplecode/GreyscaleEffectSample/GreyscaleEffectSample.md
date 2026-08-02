---
title: GreyscaleEffectSample
apple_id: DTS10000828
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-02-25'
source_url: https://developer.apple.com/library/archive/samplecode/GreyscaleEffectSample/Introduction/Intro.html
archived_at: '2026-07-18T03:11:01.713226Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](README.txt.md)

# GreyscaleEffectSample

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-02-25 Shows how to build a custom single source effect component for QuickTime. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon QuickTime 5+, Metrowerks CodeWarrior 7+, ProjectBuilder 1.1.1+, Mac OS 9, Mac OS X 10.1+ |

This sample shows how to build a custom single source effect component for QuickTime. This effect uses a single source as input, and renders that source in greyscale. It also allows for a brightness value which can range from -100...0...100. A value of 0 signifies no change in brightness. This is a very basic sample and a good place to start if you've never looked at QuickTime effect code before. This sample makes use of some code from the Dimmer2 Effect Framework and Dimmer2 Effect is a recommended companion to this sample. It is however more complex, using multiple sources, multiple pixel formats, non-Macintosh support, tweens etc. For developers who have asked for a quick and dirty single source filter sample, this one's for you eh? CodeWarrior and Project Builder projects are included: - The CodeWarrior targets build a traditional PPC code resource, Carbon CFM component and a Carbon Mach-O component. The last two for Mac OS X only. - The Project Builder target will build a Mach-O dylib for Mac OS X. Requirements: QuickTime 5+, Metrowerks CodeWarrior 7+, ProjectBuilder 1.1.1+, Mac OS 9, Mac OS X 10.1+ Keywords: QuickTime Effects Components

[Next](README.txt.md)

