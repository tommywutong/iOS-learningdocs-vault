---
title: bMoviePaletteCocoa
apple_id: DTS10000379
resource_type: Sample Code
platform: Xcode Developer Tools
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/bMoviePaletteCocoa/Introduction/Intro.html
archived_at: '2026-07-18T03:29:00.863565Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](MovieEditingController.h.md)

# bMoviePaletteCocoa

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 A QuickTime movie editor in Cocoa as an Interface Builder Palette. From the 2001 WWDC. |
| __Build Requirements:__ | Project Builder 1.0 |
| __Runtime Requirements:__ | Mac OS X Mac OS X 10.0, Project Builder 1.0 |

bMoviePalette is an example of how to do a rudimentary QuickTime movie editor in Cocoa as a Interface Builder Palette. This example was shown at the 2001 WWDC conference in San Jose. bMoviePalette contains 5 objects: MovieController The Main controller object. This object has 2 outlets, a movieClipView (which gets connected to a tableView) and a movieView (which gets connected to a NSMovieView) MovieEditorPalette A subclass of IBPalette. Provides the glue code between IB and the MovieController. MyMovie A subclass of NSMovie, this class handles all of the various editing tasks on a movie (splitting a movie, appending one movie to another, etc..), it also provides a small bit of encapsulation of the QuickTime API in Cocoa form. (Getting the posterImage of a movie as a NSImage, and adding writeToFile:atomically:) SoundFileWell A subclass of NSImageView, that allows files to be dragged into it, when the file is dragged into the SoundFileWell the target and action method is called. This class really should be just a FileWell instead of a SoundFileWell. It really does accept anything TimeFormatter A subclass of NSFormatter that takes a NSNumber as input and formats it in standard time format hh:mm:ss Requirements: Mac OS X 10.0, Project Builder 1.0 Keywords: Cocoa, Quicktime, cocoa, quicktime, Interface Builder, movie, WWDC

[Next](MovieEditingController.h.md)

