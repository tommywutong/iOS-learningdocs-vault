---
title: QuickTime 7 Update Guide
apple_id: TP40001163
resource_type: Guide
platform: macOS
topic: null
technology: QuickTime
published: '2005-04-29'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/Conceptual/QT7UpdateGuide/Chapter02/02QT7_Update_Guide.html
archived_at: '2026-07-18T01:54:31.922192Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [QuickTime 7 Update Guide](Introduction%20to%20QuickTime%207.md)


[Next](New%20Functions%2C%20Data%20Types%2C%20and%20Constants%20in%20QuickTime%207.md)[Previous](Introduction%20to%20QuickTime%207.md)

# What’s New in QuickTime 7

This chapter describes in detail the many new
and enhanced features available in QuickTime 7. It is intended to
provide developers with a conceptual overview, in addition code
samples and illustrations of usage, so that developers can take
advantage of many of these new features in QuickTime 7 in their
applications.

The new functions discussed in this chapter are cross-referenced,
with links, to their complete descriptions in Chapter 3, [New Functions, Data Types, and Constants in QuickTime 7](New%20Functions%2C%20Data%20Types%2C%20and%20Constants%20in%20QuickTime%207.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwviucykjcummjqge).

If you are a QuickTime API-level developer, content author,
multimedia producer, or Webmaster who is currently working with
QuickTime, you should read this chapter in order to understand the
fundamental changes that have taken place in the QuickTime software
architecture.

QuickTime 7 is installed automatically as part of Mac OS X
v10.4.

QuickTime 7 requires the following minimum configuration:

- Mac OS X v10.4, v10.3, or Windows
- PowerPC G3 or better running at 400 MHz or higher
- At least 256 MB of RAM

QuickTime 7 replaces existing point releases of QuickTime
6 for Mac OS X. A new Pro key is required; QuickTime 6 Pro keys
will not unlock the Pro features of QuickTime 7.

The QuickTime API is dedicated to extending the reach of application
developers by letting them invoke the full range of multimedia’s
capabilities. It supports a wide range of standards-based formats,
in addition to proprietary formats from Apple and others. The QuickTime
API is not static, however, and has evolved over the course of the
last decade to adopt new idioms, new data structures, and new ways
of doing things.

The C/C++ portion of the QuickTime API comprises more than
2500 functions that provide services to applications. These services
include audio and video capture and playback; movie editing, composition,
and streaming; still image import, export, and display; audio-visual
interactivity, and more.

A new Cocoa (Objective-C) API for QuickTime, available in
Mac OS X v10.4 and v10.3, provides a much less complex programmer
interface, and represents a distillation and abstraction of the
most essential QuickTime functions as a small set of classes and methods.
A great deal of functionality has been packed into a relatively
small objective API.

This release of QuickTime includes a number of major new features
for users, developers, and content creators, including improvements
in the QuickTime architecture, file format, user interface, and
API. There are significant improvements in the audio, video, and metadata
capabilities, as well as a new Cocoa API, and numerous other enhancements.

- [Changes to QuickTime Player and QuickTime Pro](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgmwtomzzgq4da) describes the
  new user interface for QuickTime Player and QuickTime Pro and some
  of the changes from previous versions of the player.
- [New QuickTime Kit Framework](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgmwtonbygiztm) describes a new Cocoa (Objective-C)
  framework for developing QuickTime applications. This new API opens
  the world of QuickTime programming to a new group of developers
  without requiring them to learn the large, complex C/C++ QuickTime
  API. The new framework encapsulates a tremendous amount of QuickTime
  functionality in a small, easily-mastered API with a handful of new
  objects, classes, and methods.
- [Audio Enhancements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgmwtomjyhaytg) describes the many new audio features
  of QuickTime 7, including support for multichannel sound, playback,
  capture, compression, and export of high-resolution audio, a new
  sound description, and new functions for movie audio control, audio
  conversion configuration, audio extraction, movie export, and level
  and frequency metering.
- [Video Enhancements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgmwtmnrsgy4de) describes QuickTime’s new support for
  frame reordering video compression and the H.264 codec. Frame reordering
  support is a major advance that involves new sample tables for video,
  allowing video frames to have independent decode and display times.
  This allows improved display, editing, and compression of H.264
  and other advanced video codecs. A new set of functions and structures
  are introduced to allow developers to work with samples that have
  independent decode and display times.
- [New Abstractions Layers For OpenGL Rendering](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgmwtomzwha2dk) describes
  the new Visual Context, an abstraction layer that eliminates dependence
  on graphics worlds (GWorlds) and supports rendering directly to
  engines such as OpenGL.
- [Replacing NewMovieFrom... Functions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgmwtknjwgaztg) describes the `[NewMovieFromProperties](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxu4zlxjvxxm2lfizzg63kqojxxazlsoruwk4y)` function,
  which allows you to set up properties before creating a movie. This
  function also allows you to create movies that are not necessarily
  associated with a graphics world, movies that can render their output
  to a visual context, such as an OpenGL texture buffer, and movies
  that play to a particular audio device.
- [QuickTime Metadata Enhancements and API](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgmwtmnzuguydi) describes the new QuickTime extensible
  metadata format, allowing developers to efficiently reference text,
  audio, video, or other material that describes a movie, a track,
  or a media. Support is also added for including metadata from other
  file types in native format; the QuickTime 7 release includes native
  support for iTunes metadata.
- [QuickTime Sample Table API](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgmwtmnzygu4to) describes the new API for working
  with QT Sample Tables, a logical replacement for arrays of media
  sample references. The new API greatly extends the functionality
  of media sample references, and the new API supports frame reordering
  compressed media.
- [JavaScript Support and Accessibility in Safari](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgmwtmnbyga4dg) describes the
  JavaScript support for the Safari browser. This means you can now
  use JavaScript to control QuickTime when web pages are viewed using
  Safari.
- [Other Changes and Enhancements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgmwtoobygmzdk) discusses QuickTime 7’s
  new persistent cache option, which is important for web authors
  and content developers to understand because it may impact the way
  that QuickTime content is downloaded and saved from their websites.
  New updates and fixes to QuickTime for Java are also discussed in
  this section.

Key areas of change evident in QuickTime 7 are:

- A shift of emphasis toward a Core Audio approach
  to sound, and away from the Sound Manager approach, throughout QuickTime.
- A shift of emphasis toward configuring components using component
  properties and an abstraction layer, or context, and away from the
  exclusive use of standard dialogs supplemented by direct access
  to low-level components.
- A shift of emphasis toward a more object-oriented organization,
  with more high-level functionality in QuickTime itself supporting
  lighter-weight applications.

If you work with audio at a relatively low level, you should
become familiar with the Mac OS X Core Audio framework and learn
how it differs from the older Sound Manager. The use of Core Audio
concepts and data structures is becoming ubiquitous in QuickTime
for both Mac OS X and Windows. For details, see Apple’s [Core Audio](https://developer.apple.com/documentation/MusicAudio/Reference/CoreAudio/index.html) documentation.

If you work directly with components, you should become familiar
with the API for discovering, getting, and setting component properties.
While standard dialogs for configuration are still common, there
are often times when either no dialog or an application-specific
dialog is preferable, as well as cases where low-level control or device-specific
configuration is needed that a standard dialog cannot supply.

For example, the component property API allows configuration
at any level of detail without requiring a user interface dialog
or direct communication with low-level components. In many cases,
an abstraction layer, or __context__––either
visual or audio––can be created, allowing transparent connection
to different kinds of low-level components, devices, or rendering
engines.

The new extensible QuickTime metadata format, discussed in
the section [QuickTime Metadata Enhancements and API](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgmwtmnzuguydi), uses a similar method of configuration
through an abstract set of properties, as a means of “future-proofing”
the architecture. The same is true of the new API for working with
QuickTime sample tables, described in the section [QuickTime Sample Table API](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgmwtmnzygu4to).

A substantial reorganization of the QuickTime engine has been
taking place “under the hood” in this software release. This
reorganization is intended to allow increased access to QuickTime
functionality from object-oriented frameworks such as Cocoa (Objective-C).

As the QuickTime document object model continues to evolve,
the goal is to provide developers with easier access to the more
powerful parts of the QuickTime engine using relatively lightweight
object-oriented applications or even scripts––without having
to delve into the large and sometimes complex procedural C/C++ QuickTime
API. If you haven’t experimented with Cocoa and the Xcode tools
yet, this is a good time to get started.

The following table summarizes the point releases of QuickTime
6 and the features of QuickTime 7.

| QuickTime version | Mac OS X | Windows | Mac OS 9 | Features |
| --- | --- | --- | --- | --- |
| 6 | x | x | x | MPEG-4 and lots more. |
| 6.01 | x | x | x | Bug fix for QuickTime 6. Last version for all three platforms. |
| 6.03 |  |  | x | Bug fixes to address security issues. Mac OS 9 only. |
| 6.1 | x | x |  | Improved MPEG-4 video, full-screen modes, wired actions. |
| 6.2 | x |  |  | Support for iTunes 4, enhanced AAC codec, limited DRM. |
| 6.3 | x | x |  | Improved AAC codec, 3GPP support, which includes AMR codec. |
| 6.4 for Mac OS X | x |  |  | New data reference functions, multithreading, new graphics functions, component and movie property access, other API additions. |
| 6.5 | x | x |  | 3GPP, 3GPP2, and AMC support for mobile multimedia, Unicode text support. |
| 6.5.1 | x | x |  | Apple Lossless codec for audio. |
| 7 | x | x |  | High-resolution, multichannel audio support, frame reordering video and H.264 support, new Cocoa API, support for rendering to OpenGL and elimination of dependence on graphics worlds (GWorlds), new metadata format, QuickTime sample table API, changes to QuickTime Player and Pro UI. |

QuickTime 7 introduces a number of new features and changes
to the user interface of QuickTime Player and QuickTime Pro. These
are briefly described in this section. Both Player and Pro are available
in Mac OS X v10.4 and are also backward-compatible with Mac OS X
v10.3.

The new QuickTime Player, shown in Figure 2-1,
is a native Cocoa application. The intent of this new design is
to better integrate QuickTime Player in general with the Mac OS
X user experience.

__Figure 2-1__  The new QuickTime Player application

!

The following are some of the new user-level features available
in QuickTime Player:

- __H.264 video support__. This
  state-of-the-art, standards-based codec delivers exceptional-quality
  video at the lowest data rate possible, across the entire bandwidth spectrum.
- __New audio and playback controls__. Users
  can use the new A/V Controls window (previously available only to
  QuickTime Pro users) to adjust settings for the best audio and playback
  experience. Users can now easily change settings, including playback speed,
  volume, bass, treble, and balance, as shown in Figure 2-2.

  __Figure 2-2__  New audio, playback, and video controls
  in QuickTime Player and QuickTime Player with Core Image support
  in Mac OSX v10.4

  !!

  A
  new video controls panel is also available, as shown in the right
  portion of Figure 2-2. This option, however, is only available
  for users with a special video card on Mac OS X v10.4 where Core
  Image support is provided. The video controls let the user adjust
  for brightness, color, contrast, and tint.
- __Zero-configuration streaming__. You no longer
  need to set your Internet connection speed in QuickTime Preferences.
  QuickTime automatically determines the best connection speed for
  your computer. If a connection is lost during streaming, QuickTime
  automatically reconnects to the server.
- __Live resize__. Playback continues smoothly
  as you change the size of the QuickTime Player window. (Note that
  there may be hardware dependencies that affect the speed and smoothness
  of live resizing.)
- __Multichannel audio__. QuickTime Player can
  now play 24 audio channels––and beyond. With external speakers,
  you can enjoy the full sound effects of movies and games.

  By
  accessing the Window > Show Movie Properties dialog and selecting
  Audio Settings, as shown in Figure 2-3, you can set
  the volume, balance, bass, and treble for a QuickTime movie. In
  addition, if you select the sound track property in the dialog,
  you can set the speaker for each audio channel in that track, specifying
  the speaker through which the audio can be heard.

  __Figure 2-3__  The audio settings dialog with sliders
  for audio control and channel speaker assignments

  !
- __All-new content guide__. The completely redesigned
  QuickTime Content Guide provides the latest in news, education,
  and entertainment on the Internet.
- __Screen-reader compatibility__. Using VoiceOver,
  included with Mac OS X v10.4, users with visual disabilities can
  enjoy QuickTime Player features.
- __Spotlight-friendly content__. New in Mac
  OS X v10.4, Spotlight makes it easy to find your QuickTime content.
  Spotlight can search for movie attributes such as artist, copyright,
  codec, and so on.
- __Easy access to QuickTime Pro__. Items available
  only in QuickTime Pro display “Pro” by their names. If you choose
  one of these items, you’ll see a definition of the feature and
  learn how to upgrade to QuickTime Pro. Note that the designation
  “Pro” is only present when QuickTime Player is not the Pro version.

The following are some of the new user-level features available
in the Pro version of QuickTime Player:

- __Creating H.264 video.__ Users
  can take advantage of this codec for a variety of video needs, ranging
  from HD (high definition) to 3G (for mobile devices). This new codec provides
  better quality at lower bandwidth, enabling users to deliver high-quality video
  over the Internet.
- __Creating multichannel audio__. Users can
  create a rich multimedia experience by labeling each audio channel
  (for example, Left, Right, Left Surround, LFE, and so on), as shown
  in Figure 2-3. QuickTime automatically mixes the audio
  to work with the speaker setup of each user.
- __Recording audio and video__. With a digital
  video camera connected to your computer, you can enrich your email
  messages with video clips. In addition, with enhanced recording
  of audio and video, users can add narration, for example, to their
  slide shows.
- __Sharing movies__. Users can easily create
  a movie file for sending via email or posting to your .Mac HomePage.
  Select File > Share and a dialog appears that lets you choose
  a maximum size for the attached movie you want to share and then
  exports the movie to either your Mail program or to your .Mac HomePage,
  as shown in Figure 2-4.

  __Figure 2-4__  Sharing
  attached movies either as email or on your .Mac HomePage

  !
- __Full screen playback enhancements__. Full
  screen mode now provides floating Dashboard-style controls similar
  to the controls available for DVD Player. These include pause, play,
  stop, fast forward, and rewind, as illustrated in Figure 2-5.
  Users move the pointer to display the controller; after a few seconds,
  the controller fades away. Note that the controller does not appear
  with interactive movies when the mouse is moved, so that it does
  not interfer with movie content. Users can press the keyboard control-C
  to make it appear or disappear immediately. This new zooming transition, enabling
  you to go in and out of Full Screen, is dependent on the user’s
  computer hardware, as well as the media being played back.

  __Figure 2-5__  Full screen controls with a floating
  movie controller

  !!

  Users can access full screen
  mode by choosing the View > Full Screen or using its keyboard
  equivalent. To display the DVD-style full screen controls, users
  choose QuickTime Player > Preferences > Full Screen and select
  “Display full screen controls,” as shown in Figure 2-6.

  __Figure 2-6__  Full Screen preferences with the full
  screen controls selected

  !
- __Concurrent exports__. Users can export multiple
  files at once—and continue with their next playback or editing
  task. Figure 2-7 shows the default export settings for exporting a
  movie to a QuickTime movie.

  __Figure 2-7__  The default export settings for exporting
  a movie to a QuickTime movie

  !
- The export options enable Pro users to export to a variety
  of image, text, audio, and movie formats, as shown in Figure 2-8.

  __Figure 2-8__  Export options available in QuickTime
  Pro

  !
- __Enhanced and redesigned interface for movie settings__.
  The Movie Properties window has been redesigned to facilitate movie
  authoring. Figure 2-9 illustrates the Movie Properties dialog,
  with annotations of the movie selected.

  __Figure 2-9__  The Movie Properties dialog

  !
- __New options for image manipulation__ in the
  Visual Settings pane of the Movie Properties dialog of a video track,
  as shown in Figure 2-10.

  __Figure 2-10__  QuickTime Pro visual settings options
  for image control and manipulation

  !

  In addition,
  users are provided with other options to manipulate and control
  image transparency in QuickTime movies and image files, shown in Figure 2-11.

__Figure 2-11__  QuickTime Pro user options for controlling
image transparency

!

QuickTime Preferences now has the option “Use high quality
video setting when available.” Users can set this as the default
for displaying high-quality video tracks, such as DV. Figure 2-12 shows
the options available in the General pane of QuickTime Player Preferences.

__Figure 2-12__  The General pane in QuickTime Player
Preferences

!

Figure 2-13 shows the new File menu in QuickTime Player.
The Open File command enables users to open any of a number of digital
media types that QuickTime supports, including movies, still images,
VR panoramas, Flash, and so on.

__Figure 2-13__  The new File menu in the QuickTime
Player with New Movie Recording selected

!

Choosing the File > New Movie Recording menu item enables
you to record video from an external digital video camera. Recording
is transparent and easy to use, as QuickTime automatically recognizes
the device and opens a new QuickTime Player with a red button in
the lower center, as shown in Figure 2-14. The Player
also displays the current recording duration, as well as the size
of the recording in megabytes.

__Figure 2-14__  Movie recording from a digital device
in a new QuickTime player

!

Choosing the File > New Audio Recording menu item enables
you to record audio from an external or internal audio device. Once
recording begins, a new QuickTime Player appears, as shown in Figure 2-15.

__Figure 2-15__  Audio recording

!

To change the video or audio source for your recording, or
to specify the quality of recording you want, you choose QuickTime
Player > Preferences > Recording, as shown in Figure 2-16.

__Figure 2-16__  Recording preferences

!

The Save dialog that the Save As command opens now has a “Make
movie as a self-contained,” selected by default, which is a change
from previous versions of QuickTime Player.

Choosing the File > Update Existing Software menu item
shown in Figure 2-17 lets you update the version to the latest
version of QuickTime available through Software Update.

__Figure 2-17__  The new QuickTime Player menu

!

The Edit menu has changed from previous versions of QuickTime,
as shown in Figure 2-18.

Support for multiple undos is now provided. There is a command
Trim to Selection (instead of Trim) and there is no longer a Replace
command (users can’t do delete and paste as a single operation).

__Figure 2-18__  The QuickTime Pro Edit menu items
with Trim to Selection selected

!

The Movie menu has been renamed and is now the View menu,
as shown in Figure 2-19. The Show Movie Properties command has been
moved to the Windows menu. Note that this overrides any full screen
settings made in user preferences for the current presentation only.

__Figure 2-19__  The View menu options

!

The Present Movie command now opens a sheet as shown in Figure 2-20.
The same functionality as in previous versions is provided.

__Figure 2-20__  The Present Movie sheet

!

The Window menu (Figure 2-21) now provides
commands for getting movie properties and showing audio/video controls.

__Figure 2-21__  The Window menu with Show A/V Controls
selected

!

Choosing the Window > Show Movie Properties menu item and
selecting Video Track 1 (shown in Figure 2-22) enables you
to specify certain properties of that track. For example, if you
select Annotations and want to add a field, you have multiple choices,
including Album, Artist, Author, and so on.

__Figure 2-22__  Movie properties with annotations
and added fields selected

!

Choosing the Window > Show Movie Properties menu item and
selecting Video Track 1 (shown in Figure 2-23) with Other
Settings selected enables you to specify certain properties of that
track, including language, preloading of the track, caching, and
so on.

__Figure 2-23__  Other settings available in the movie
properties pane

!

The movie properties window has been reorganized, as shown
in Figure 2-24. The Presentation pane provides users with
four choices for presenting movie, as well as options for displaying
various types of movie controllers.

__Figure 2-24__  The Presentation pane with a QTVR
controller selected

!

- __New selection handles and fade in/out
  behavior__. When the user moves the mouse over a selection
  of the movie, ticks appear that indicate you can make a selection
  over that area. When you move the mouse over the playbar, the movie
  will fade the selection indicators in and out. Users can also set
  in and out points now by placing the current time marker and typing
  I or O.

QuickTime 7 introduces Cocoa developers to a new QuickTime
Kit framework (`QTKit.framework`).
The QuickTime Kit is a Objective-C framework with a rich API for manipulating
time-based media.

At a basic level, QuickTime Kit provides support for displaying
and editing QuickTime movies, relying on abstractions and data types
that are already familiar to many Cocoa programmers, such as delegation
and notification. QuickTime Kit introduces new data types for QuickTime-related
operations only when necessary.

Specifically, two QuickTime Kit classes––`QTMovie` and `QTMovieView`––are
intended to replace the existing Application Kit classes `NSMovie` and `NSMovieView`.

The QuickTime Kit framework is new in Mac OS X v10.4 but is
also backward-compatible with Mac OS X v10.3 (Panther) as well.

The QuickTime Kit framework provides a set of Objective-C
classes and methods designed for the basic manipulation of media,
including movie playback, editing, import and export to standard
media formats, among other capabilities. The QuickTime Kit framework
is at once powerful, yet easy to include in your Cocoa application. Figure 2-25 shows
the QuickTime Kit framework’s class hierarchy.

__Figure 2-25__  The QuickTime Kit framework class
hierarchy

!

Although the QuickTime Kit framework contains only five classes,
you can use these classes and their associated methods, notifications,
and protocols to accomplish a broad range of tasks, such as displaying,
controlling, and editing QuickTime movies in your Cocoa applications.

A QTKit palette is also provided in Interface Builder that
lets you simply drag a QuickTime movie object, complete with a controller
for playback, into a window, and then set attributes for the movie––all
of this without writing a single line of code.

Figure 2-26 shows an animated version of what happens
in Interface Builder when you drag the QuickTime object from the
QTKit palette to the application window.

__Figure 2-26__  The QuickTime object dragged to the
application window

!

After you drag the QuickTime object into the application window,
you have a QuickTime movie view object with a control bar in the
bottom-left corner of the window, as shown in Figure 2-27.
By dragging the QuickTime movie view object by its corner handle
to the upper-right corner of the window, the entire window fills
up so that the movie view object with its control bar is visible.

__Figure 2-27__  The QuickTime movie view object dragged
to fill the entire contents of the window

!

The QuickTime Kit framework is documented in the [QuickTime Kit Reference](https://developer.apple.com/documentation/qtkit) in conformance with the standards established
for Apple’s Cocoa documentation suite. A tutorial for using the
new framework, [QuickTime Kit Programming Guide](../QuickTime%20Kit%20Programming%20Guide/Introduction%20to%20QuickTime%20Kit%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenbv), is also available online and in
PDF format. You can learn how to take advantage of the new QuickTime
Kit framework classes and methods and build your own QTKitPlayer application,
as well as learn how to extend its functionality.

QuickTime 7 breaks free of the limitations of the Sound Manager,
adding many new features and capabilities that developers can take
advantage of in their audio playback and capture applications.

Notably, QuickTime 7 now supports __high-resolution
audio__, that is, audio sampled at sample rates higher than
64 kHz and up to 192 kHz, with up to 24 channels and support for
surround sound. This is in stark contrast to the implementation
of the Sound Manager, which only supported mono and stereo. High-resolution
audio is supported by Apple’s Core Audio technology.

The result of these new audio enhancements is as follows:

- A much richer approach to sound in QuickTime,
  with support for higher sampling rates, such as 96 kHz and 192 kHz,
  multiple channels and multiple channel layouts, including 5.1 surround
  sound and up to 24 discrete channels, meaning channels without any
  layout imposed on them. Support is also provided for a variety of
  more accurate audio representations, such as 24-bit uncompressed
  audio, during capture, playback, and export. Synchronization and
  access to uncompressed audio on a per-sample basis is also greatly
  improved, including access to raw PCM audio samples from VBR-compressed
  audio sources.
- The introduction of a new abstraction layer: the audio context.
  An audio context represents a connection to a particular audio device.
  Using an audio context allows you to easily connect a movie to an
  audio device.
- A more flexible architecture for capturing audio. For instance,
  multiple sequence grabber audio channels `SGAudioMediaType`)
  can capture from a single device at the same time, even if the device
  doesn’t permit multiple clients directly, and devices with different
  channel layouts or different PCM audio formats can be interconnected seamlessly.
- Conversion of audio from one format to another on the fly,
  performing channel mix-down or remapping, upsampling or downsampling,
  and sample conversion as needed. This conversion can be performed
  during export, or as part of the output chain to a device with different
  playback characteristics than the stored audio, or as part of the
  capture and storage chain to map input from one or more devices
  into one or more storage formats.

Most components, with a few exceptions such as streaming and
MPEG-4 exporting, will be able to make use of these new capabilities
immediately. This release of QuickTime updates a number of components
so that it is possible to capture, play back, edit, and export a
broad variety of enhanced audio right away.

In brief, QuickTime 7 includes the following enhancements,
discussed in this section:

- A new abstraction layer for audio
- A new sound description
- A suite of sound description functions
- New movie property to prevent pitch-shifting
- New functions for gain, balance, and mute
- New level and frequency metering API
- New audio extraction and conversion API
- New audio compression configuration component
- New movie export properties to support high-resolution audio
- New sequence grabber component for audio (`SGAudioMediaType`)

QuickTime 7 introduces the __audio context__––a
new abstraction that represents playing to an audio device.

As defined, a QuickTime audio context is an abstraction for
a connection to an audio device. This allows you to work more easily
and efficiently with either single or multiple audio devices in
your application.

To create an audio context, you call `[QTAudioContextCreateForAudioDevice](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvcbovsgs32dn5xhizlyorbxezlborsum33sif2wi2lpirsxm2ldmu)` and
pass in the UID of the device, which is typically a `CFString`.
An audio context is then returned. You can then pass that audio
content either into `[NewMovieFromProperties](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxu4zlxjvxxm2lfizzg63kqojxxazlsoruwk4y)`,
as you would pass in a visual context, or you can open your movie
however you would normally open it and call `[SetMovieAudioContext](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvgzlujvxxm2lfif2wi2lpinxw45dfpb2a)`.
What that does is route all the sound tracks of the movie to that particular
device.

Note that if you want to route two different movies to the
same device, you cannot use the same audio context because the audio
context is a single connection to that device. What you do is call `[QTAudioContextCreateForAudioDevice](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvcbovsgs32dn5xhizlyorbxezlborsum33sif2wi2lpirsxm2ldmu)` again
and pass in the same device UID to get another `AudioContext` for
the same device, and pass that to your second movie.

High-resolution audio makes use of an enhanced sound description
with the ability to describe high sampling rates, multiple channels,
and more accurate audio representation and reproduction.

Significantly, the new sound description has larger fields
to describe the sampling rate and number of channels, so that the
sound description is no longer the limiting factor for these characteristics.

The sound description has built-in support for variable-bit-rate
(VBR) audio encoding with variable-duration compressed frames. Extensions
to the sound description allow you to describe the spatial layout
of the channels, such as quadraphonic and 5.1 surround sound, or
to label channels as __discrete__––that is, not
tied to a particular geometry. For more information, see `[“SoundDescriptionV2”](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3umfts6u3povxgirdfonrxe2lqoruw63swgi)`.

New movie audio properties include a summary channel layout
property, providing a nonredundant listing of all the channel types
used in the movie—such as L/R for stereo, or L/R/Ls/Rs/C for 5-channel
surround sound—and a device channel layout, listing all the channel
types used by the movie’s output device.

Figure 2-28 shows the layout of surround speakers. The
terminology is defined in Table 1-1.

__Figure 2-28__  Layout of surround speakers

!

__Table 2-1__  Surround sound definitions

| Speaker | Definition |
| L | Left speaker |
| R | Right speaker |
| C | Center speaker |
| Ls | Left surround speaker |
| Rs | Right surround speaker |
| LFE | Sub-woofer (Note that LFE is an abbreviation for low-frequency effects) |

The new sound description is supported by the data types and
structures used in the Core Audio framework for Mac OS X (see [Core Audio](https://developer.apple.com/documentation/MusicAudio/Reference/CoreAudio/index.html) documentation). While the Core Audio API itself is not
available to Windows programmers, QuickTime for Windows may include the
relevant data structures, such as audio buffers and stream descriptions,
audio time stamps and channel layouts, and so on, described in the
Core Audio documentation.

A suite of functions has been included to support the handling
of sound descriptions opaquely.

Playback at the high level is automatic and transparent; if
you play a movie that contains 96 kHz or 192 kHz sound, it should
just work. You should not have to modify your code. The same is
true for cut-and-paste editing. If the chosen output device does
not support the channel layout, sampling rate, or sample size of
the movie audio, mix-down and resampling are performed automatically.

Import of high-resolution audio is automatic, provided the
import component has been updated to support high-resolution audio.

Export of high-resolution audio is likewise transparent at
the high level. Export at the lower levels requires some additional
code. Your application must “opt in” to the new audio features
explicitly if it “talks” directly to an export component instance.
You do this by calling `[QTSetComponentProperty](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvctmv2eg33nobxw4zloorihe33qmvzhi6i)` on
the exporter component instance and passing in the `kQTMovieExporterPropertyID_EnableHighResolutionAudioFeatures` property.
This is illustrated in the code sample [Listing 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgmwtonrwga4ta).

Capturing high-resolution audio requires new code to configure
and use the new sequence grabber component for audio. The new audio
capture API offers a number of improvements, including the ability
to share an input device among multiple sequence grabber channels
and the usage of multiple threads for increased efficiency.

When all components in a chain are able to work with high-resolution
audio, clock information can be preserved across operations for
sample-accurate synchronization.

QuickTime 7 provides new functions that let you create, access,
and convert sound descriptions.

Sound descriptions can take three basic inputs: an `AudioStreamBasicDescription`,
a channel layout, and magic cookie. Sound descriptions are now treated
as if they are opaque. In QuickTime 7, when you are handed a sound
description, for example, you don’t have to go in and look at
the version field.

If you want to create a sound description, you can simply
hand it an `AudioStreamBasicDescription`,
an optional channel layout if you have one, and an optional magic
cookie if you need one for the described audio format. Note that
it is the format (codec) of the audio that determines whether it
needs a magic cookie, not the format of the sound description.

By calling `[QTSoundDescriptionCreate](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjw65lomrcgk43dojuxa5djn5xeg4tfmf2gk)`, you can make
a sound description of any version you choose––for example,
one that is of the lowest possible version, given that it is stereo and
16-bit, or one of any particular version you want or request.

The main point about the new API is the capability provided
to create a sound description and the usage of new property getters
and setters. To accomplish this, follow these steps:

1. Get an `AudioStreamBasicDescription` from
   a sound description.
2. Get a channel layout from a sound description (if there is
   one).
3. Get the magic cookie from magic cookie (if there is one).

At this point, you have all the information you need to talk
to Core Audio about this audio. You can also:

1. Get a user-readable textual description of the
   format described by the `SoundDescription`.
2. Add or replace a channel layout to an existing sound description.
   For example, this is what QuickTime Player does in the properties
   panel where the user can change the channel assignments.
3. Add a magic cookie to a sound description. (This is not needed
   very often unless you are writing a movie importer, for example.)

To convert an existing QuickTime sound description into the
new V2 sound description, you call `[QTSoundDescriptionConvert](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjw65lomrcgk43dojuxa5djn5xeg33oozsxe5a)`. This lets
you convert sound descriptions from one version to another.

For a description of versions 0 and 1 of the `SoundDescription` record,
see the documentation for the [QuickTime File Format](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000433-TP30000509).

For a description of version 2 of the `SoundDescription` record,
see `[“SoundDescriptionV2”](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3umfts6u3povxgirdfonrxe2lqoruw63swgi)`. For details
of the sound description functions, see `[QTSoundDescriptionCreate](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjw65lomrcgk43dojuxa5djn5xeg4tfmf2gk)` and `[QTSoundDescriptionConvert](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjw65lomrcgk43dojuxa5djn5xeg33oozsxe5a)`.

In addition to playing back high-resolution audio, QuickTime
7 introduces the following audio playback enhancements:

- The ability to play movies at a nonstandard rate
  without pitch-shifting the audio.
- Getting and setting the gain, balance, and mute values for
  a movie, or the gain and mute values for a track.
- Providing audio level and frequency metering during playback.

A new property is available for use with the `[NewMovieFromProperties](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxu4zlxjvxxm2lfizzg63kqojxxazlsoruwk4y)` function: [kQTAudioPropertyID_RateChangesPreservePitch](https://developer.apple.com/library/archive/documentation/QuickTime/Reference/QT7-1_Update_Reference/Constants.html#//apple_ref/doc/c_ref/kQTAudioPropertyID_RateChangesPreservePitch).
When this property is set, changing the movie playback rate will
not result in pitch-shifting of the audio. This allows you to fast-forward
through a movie without hearing chipmunks.

Setting this property also affects playback of scaled edits,
making it possible to change the tempo of a sound segment or scale
it to line up with a video segment, for example, without changing
the pitch of the sound.

New functions are available to set the left-right balance
for a movie, set the gain for a movie or track, or to mute and unmute
a movie or track without changing the gain or balance settings.

The gain and mute functions duplicate existing functions for
setting track and movie volume, but the new functions present a
simpler and more consistant programmer interface.

For example, to mute the movie using the old `SetMovieVolume` function,
you would pass in a negative volume value; to preserve the current
volume over a mute and unmute operation, you had to first read the
volume, then negate it and set it for muting, then negate it and
set it again to unmute. By comparison, the new `[SetMovieAudioMute](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvgzlujvxxm2lfif2wi2lpjv2xizi)` function
simply mutes or unmutes the movie without changing the gain value.

For details, see

- `[GetTrackAudioGain](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2fi4tbmnvuc5lenfxuoyljny)`
- `[SetTrackAudioGain](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2tmv2fi4tbmnvuc5lenfxuoyljny)`
- `[GetTrackAudioMute](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2fi4tbmnvuc5lenfxu25lumu)`
- `[SetTrackAudioMute](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2tmv2fi4tbmnvuc5lenfxu25lumu)`
- `[GetMovieAudioGain](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2e233wnfsuc5lenfxuoyljny)`
- `[SetMovieAudioGain](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2tmv2e233wnfsuc5lenfxuoyljny)`
- `[GetMovieAudioMute](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2e233wnfsuc5lenfxu25lumu)`
- `[SetMovieAudioMute](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2tmv2e233wnfsuc5lenfxu25lumu)`
- `[GetMovieAudioBalance](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2e233wnfsuc5lenfxueylmmfxggzi)`
- `[SetMovieAudioBalance](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2tmv2e233wnfsuc5lenfxueylmmfxggzi)`

It is now easy to obtain real-time measurements of the average
audio output power level in one or more frequency bands.

You can specify the number of frequency bands to meter. QuickTime
divides the possible frequency spectrum (approximately half the
audio sampling rate) into that many bands. You can ask QuickTime
for the center frequency of each resulting band for display in your user
interface.

You can measure the levels either before or after any mix-down
or remapping to an output device. For example, if you are playing
four-channel surround sound into a stereo output device, you might
want to meter the audio levels of all four channels, or you might
prefer to see the actual output values delivered to the stereo device.

To use the frequency metering API, follow these steps:

1. Set the number of frequency bands to meter using `[SetMovieAudioFrequencyMeteringNumBands](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvgzlujvxxm2lfif2wi2lpizzgk4lvmvxgg6knmv2gk4tjnztu45lnijqw4zdt)`.
2. Call `[GetMovieAudioFrequencyMeteringBandFrequencies](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxuozlujvxxm2lfif2wi2lpizzgk4lvmvxgg6knmv2gk4tjnztueylomrdhezlrovsw4y3jmvzq)` if
   you need to know the frequencies of the resulting bands.
3. Finally, make periodic calls to `[GetMovieAudioFrequencyLevels](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxuozlujvxxm2lfif2wi2lpizzgk4lvmvxgg6kmmv3gk3dt)` to
   obtain measurements in all specified bands. You can obtain either
   the average values, the peak hold values, or both.

For details, see

- `[GetMovieAudioVolumeMeteringEnabled](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2e233wnfsuc5lenfxvm33movwwktlforsxe2lom5cw4ylcnrswi)`
- `[SetMovieAudioVolumeMeteringEnabled](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2tmv2e233wnfsuc5lenfxvm33movwwktlforsxe2lom5cw4ylcnrswi)`
- `[GetMovieAudioVolumeLevels](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2e233wnfsuc5lenfxvm33movwwktdfozswy4y)`
- `[GetMovieAudioFrequencyMeteringNumBands](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2e233wnfsuc5lenfxum4tfof2wk3tdpfgwk5dfojuw4z2oovwueylomrzq)`
- `[SetMovieAudioFrequencyMeteringNumBands](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2tmv2e233wnfsuc5lenfxum4tfof2wk3tdpfgwk5dfojuw4z2oovwueylomrzq)`
- `[GetMovieAudioFrequencyMeteringBandFrequencies](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2e233wnfsuc5lenfxum4tfof2wk3tdpfgwk5dfojuw4z2cmfxgirtsmvyxkzlomnuwk4y)`
- `[GetMovieAudioFrequencyLevels](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2e233wnfsuc5lenfxum4tfof2wk3tdpfggk5tfnrzq)`

The new audio extraction API lets you retrieve mixed, uncompressed
audio from a movie.

Note that the audio extraction API currently _only_ mixes
audio from sound tracks. Other media types, such as muxed MPEG-1
audio inside a program stream, are not currently supported.

To use the audio extraction API, follow these steps:

1. Begin by calling `[MovieAudioExtractionBegin](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2nn53gszkbovsgs32fpb2heyldoruw63scmvtws3q)`. This returns
   an opaque session object that you pass to subsequent extraction
   routines.
2. You can then get the `AudioStreamBasicDescription` for
   the audio or layout. Note that some properties are of variable size,
   such as the channel layout, depending on the audio format, so getting
   the information involves a two-step process.

   1. First,
      you call `[MovieAudioExtractionGetPropertyInfo](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2nn53gszkbovsgs32fpb2heyldoruw63shmv2fa4tpobsxe5dzjfxgm3y)` to
      find out how much space to allocate.
   2. Next, call `[MovieAudioExtractionGetProperty](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2nn53gszkbovsgs32fpb2heyldoruw63shmv2fa4tpobsxe5dz)` to obtain
      the actual value of the property.
3. You can use the `AudioStreamBasicDescription` to
   specify a different uncompressed format than Float 32. This causes
   the extraction API to automatically convert from the stored audio
   format into your specified format.
4. Use the `[MovieAudioExtractionSetProperty](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2nn53gszkbovsgs32fpb2heyldoruw63stmv2fa4tpobsxe5dz)` function
   to specify channel remapping––that is, a different layout––sample
   rate conversion, and preferred sample size. You can also use this
   function to specify interleaved samples (default is non-interleaved)
   or to set the movie time to an arbitrary point.

Note that there are basically two things you set here: an
audio stream basic description (ASBD) and a channel layout. (ASBD
sets the format, sample, number of channels, interleavings, and
so on.)

Setup is now complete. You can now make a series of calls
to `[MovieAudioExtractionFillBuffer](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxu233wnfsuc5lenfxuk6duojqwg5djn5xem2lmnrbhkztgmvza)` to
receive uncompressed PCM audio in your chosen format.

1. The default is for the first call to begin extracting
   audio at the start of the movie, and for subsequent calls to begin
   where the last call left off, but you can set the extraction point anywhere
   in the movie timeline by calling `[MovieAudioExtractionSetProperty](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxu233wnfsuc5lenfxuk6duojqwg5djn5xfgzlukbzg64dfoj2hs)` and setting
   the movie time.
2. `[MovieAudioExtractionFillBuffer](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxu233wnfsuc5lenfxuk6duojqwg5djn5xem2lmnrbhkztgmvza)` will
   set `kMovieAudioExtractionComplete` in _outFlags_ when
   you reach the end of the movie audio.
3. You must call `[MovieAudioExtractionEnd](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxu233wnfsuc5lenfxuk6duojqwg5djn5xek3te)` when
   you are done. This deallocates internal buffers and data structures
   that would otherwise continue to use memory and resources.

_A caveat:_ Ideally, the uncompressed samples
would be bitwise identical whether you obtained the samples by starting
at the beginning of the movie and iterating through it, or by randomly
setting the movie time and extracting audio samples. This is typically
the case, but for some compression schemes the output of the decompressor
depends not only on the compressed sample, but the seed value in
the decompressor that remains after previous operations.

The current release of QuickTime does not perform the necessary
work to determine what the seed value would be when the movie time
is changed prior to extracting audio; while the extracted audio
is generally indistinguishable by ear, it may not always be bitwise identical.

For details about audio conversion, export, and extraction,
refer to the information about the following functions:

- `[MovieAudioExtractionBegin](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2nn53gszkbovsgs32fpb2heyldoruw63scmvtws3q)`
- `[MovieAudioExtractionGetPropertyInfo](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2nn53gszkbovsgs32fpb2heyldoruw63shmv2fa4tpobsxe5dzjfxgm3y)`
- `[MovieAudioExtractionGetProperty](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2nn53gszkbovsgs32fpb2heyldoruw63shmv2fa4tpobsxe5dz)`
- `[MovieAudioExtractionSetProperty](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2nn53gszkbovsgs32fpb2heyldoruw63stmv2fa4tpobsxe5dz)`
- `[MovieAudioExtractionFillBuffer](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2nn53gszkbovsgs32fpb2heyldoruw63sgnfwgyqtvmztgk4q)`
- `[MovieAudioExtractionEnd](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2nn53gszkbovsgs32fpb2heyldoruw63sfnzsa)`

QuickTime 7 introduces a new standard compressor component, `StandardCompressionSubTypeAudio`,
that adds the ability to configure high-resolution audio output
formats. It uses Core Audio internally instead of the Sound Manager,
and has a full set of component properties to make configuration
easier, especially when the developer wishes to bring up an application-specific
dialog, or no dialog, rather than the typical compression dialog.

This component essentially replaces the `StandardCompressionSubTypeSound` component, which
is limited to 1 or 2 channel sound with sampling rates of 65 kHz
or less. That component is retained for backward compatability with
existing code, but its use is no longer recommended.

The `StandardCompressionSubTypeAudio` component
is configured by getting and setting component properties, instead
of using GetInfo and SetInfo calls. These properties have a class
and ID, instead of just a single selector.

The component property API allows configuration at any level
of detail without requiring a user interface dialog or direct communication
with low-level components.

For details, refer to the sections [SGAudio Component Property Classes](New%20Functions%2C%20Data%20Types%2C%20and%20Constants%20in%20QuickTime%207.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtknjqg4yde)and [SGAudio Component Property IDs](New%20Functions%2C%20Data%20Types%2C%20and%20Constants%20in%20QuickTime%207.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtknjqhazts).

If you use `MovieExportToDataRefFromProcedures`,
your getProperty proc will need to support some of these property
IDs as new selectors. Note that the Movie Exporter getProperty proc
API is not changing to add a class (the class is implied).

Some movie export components now support high-resolution audio.

Export of high-resolution audio is transparent at the high
level. If you export from a movie containing high-resolution audio
to a format whose export component supports it, the transfer of
data is automatic; if the export component does not support high-resolution audio,
mix-down, resampling, and sound description conversion are automatic.

Export at the lower levels requires some additional code.
Your application must “opt in” to the new audio features explicitly
if it talks directly to an export component instance. (This is to
prevent applications that have inadvisedly chosen to “walk”
the opaque atom settings structure from crashing when they encounter
the new and radically different structure.) The following code snippet
(Listing 2-1) illustrates the opt-in process.

__Listing 2-1__  Opting
in for high-resolution audio export

```
ComponentInstance exporterCI;
ComponentDescription search = { ’spit’, ’MooV’, ’appl’, 0, 0 };
Boolean useHighResolutionAudio = true, canceled;
OSStatus err = noErr;

Component c = FindNextComponent(NULL, &search);
exporterCI = OpenComponent(c);

// Hey exporter, I understand high-resolution audio!!
(void) QTSetComponentProperty(// disregard error
        exporterCI,
        kQTPropertyClass_MovieExporter,
        kQTMovieExporterPropertyID_EnableHighResolutionAudioFeatures,
        sizeof(Boolean),
        &useHighResolutionAudio);

err = MovieExportDoUserDialog(exporterCI, myMovie, NULL, 0, 0, &canceled);
```

For additional details, see `[“Movie Exporter Properties”](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtknjqgu3dg)`.

There is a new sequence grabber channel component (`’sgch’`)
subtype for audio, `SGAudioMediaType` (`’audi’`),
which allows capture of high-resolution audio, supporting multi-channel,
high sample rate, high accuracy sound. This is intended to replace
the older `SoundMediaType` component.

The new audio channel component has a number of noteworthy
features, including:

- audio capture to VBR compressed formats
- enabling or disabling of source channels on a multi-channel
  input device
- mix-down and remapping of multi-channel audio source material
- discrete and spatial labeling of channels (for example, 5.1
  or discrete)
- audio format and sample rate conversion during capture
- sharing of audio input devices among multiple sequence grabber
  audio channels
- sharing of audio playback devices among multiple sequence
  grabber audio channels
- notification of audio device hotplug/unplug events
- audio preview of source data or compressed data
- splitting audio channels from a record device to separate
  tracks in a movie
- redundant capture of multichannel audio to separate tracks
  in a movie (with independent data rates and compression settings)
- client callbacks of audio pre- and post-mixdown, and pre-
  and post-conversion with propagation of audio time stamps and audio
  samples to interested clients
- improved A/V sync
- improved threading model compared with the legacy `SoundMediaType`
- lower latency audio grabs
- reduced dependency on frequent `SGIdle` calls

This new, advanced functionality makes extensive use of Core
Audio methodology and data structures.

The audio channel component can be configured
using component properties. This has several advantages over using
a sequence grabber panel. For one thing, it can be configured without
a user dialog, or using an application-specific dialog. For another,
it is possible to test for properties and get or set them dynamically,
allowing the same code to configure multiple audio input devices,
including unfamiliar devices.

The application does not need to bypass the channel component
and connect directly to an input device, such as a `SoundInputDriver`,
to set low-level properties. This allows multiple capture channels
to share a single input device, and keeps application code from
becoming tied to a particular device type.

For a full list of the `SGAudioMediaType` component
properties, see `[“SGAudio Component Property IDs”](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtknjqhazts)`.
For a full list of component property classes, see `[“SGAudio Component Property Classes”](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtknjqg4yde)`.

Once the component is configured, the audio capture—plus
any desired mixdown, format or sample-rate conversion, and compression—take
place in a combination of real-time and high-priority threads. Multichannel
data is interleaved and samples are put into a queue. You can set
up callbacks to watch the data at any of several points in the chain: pre-mixdown,
post-mixdown, pre-conversion, or post-conversion.

The actual writing of the captured audio to a storage medium,
such as a disk file, takes place during calls to `SGIdle`.

One input device can be shared by multiple sequence grabber
channels, as illustrated in Figure 2-29. Because independent
mix and conversion stages exist for each sequence grabber audio
channel, the sequence grabber audio channels can capture different
channel mixes, sampling rates, sample sizes, or compression schemes
from the same source. Similarly, multiple sequence grabber audio
channels can share a common output device for previewing.

Channel mixdown or remapping, sample conversion, and any compression
are all performed on high-priority threads. Each sequence grabber
channel receives data from only those audio channels it has requested,
in the format it has specified. The following processing may occur
in the background:

- software gain adjustment
- mixing
- sample rate conversion
- bit-depth widening or shortening
- float to integer conversion
- byte-order conversion (big-endian to little-endian or vice-versa)
- encoding of frames into compressed packets of data in the
  specified format
- interleaving

The resulting frames or packets are held in a queue, to be
written to file or broadcast stream on the main thread. This is
accomplished during calls to `SGIdle`,
at which time the audio is chunked and interleaved with any video
data being captured.

Figure 2-29 is a high-level diagram that shows some
of the internal workings of the sequence grabber audio channel,
such as the Core Audio matrix mixer and the audio converter that
lets you convert, compress, and interleave audio, and then queue
the audio. From the queue, the audio can be written to disk in desired
chunk sizes. One distinct advantage of this process is that you
can take a single device and share it among multiple channels. This
results in simultaneous recording from multiple devices into multiple tracks
in a QuickTime movie. In addition, you can record multiple tracks
from a single device.

__Figure 2-29__  QuickTime audio device sharing among
sequence grabber channels

!

Figure 2-30 illustrates a usage case that involves client
channel mapping. This shows how a client can instantiate multiple
sequence grabber audio channels that share a recording device. This
enables the “splitting” of device channels across multiple tracks
in a QuickTime movie. In Figure 2-30, there is single
recording device, with four channels. The first two channels record
into Track 1 in a QuickTime movie. The second sequence grabber audio
channel, which records into Track 2 in a QuickTime movie, only wants
channel 4 from the recording device, so that you can get one stereo
track and one mono track.

In this example, device Track 0 will get into Movie Track
1, while Movie Track 3 has only one slot to fill. You can mix and
match different channel map valences in such a way as to disable
certain tracks in a movie and get submixes, for example. In code,
it looks like this:

```
SInt32 map 1 [ ] = { 0, 1 };
SInt32 map 2 [ ] = { 3 };
```


__Figure 2-30__  Client channel mapping with “splitting”
of device channels

!

Figure 2-31 shows another usage case that also involves
client channel mapping.

A sequence grabber audio channel shown in the illustration
can get four channels from a device in any order that makes sense
for the client. Consider, for instance, a device that supports four-channels
of audio. Using the channel map property IDs ([SGAudio Component Property IDs](New%20Functions%2C%20Data%20Types%2C%20and%20Constants%20in%20QuickTime%207.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtknjqhazts)),
you can reorder channels from a recording device to a desired movie
channel valence. In code, it looks like this:

```
SInt32 map [ 4 ] = { 3, 2, 1, 0 };
```


__Figure 2-31__  Channel mapping with reordering of
channels

!

Figure 2-32 shows another example of what you can do
with the feature of channel mapping, in this case __mult’-ing__,
that is, duplicating channels from a recording device into multiple
output channels in QuickTime movie tracks. For instance, you can
take advantage of this channel mapping feature if you have one recording
device and two sequence grabber audio channels, and they’re both
going to make the same movie. The first sequence grabber audio channel
wants the first stereo pair twice (1, 2, 1, 2), while the second
wants the second stereo pair twice (3, 4, 3, 4). In code, it looks
like this (zero-based indexing):

```
SInt32 map 1 [ ] = { 0, 1, 0, 1 };
SInt32 map 2 [ ] = { 2, 3, 2, 3 };
```


__Figure 2-32__  Channel mapping enabling mult-ing

!

Figure 2-33 illustrates the what you can do with multiple
mixes. Because you can duplicate device channels onto multiple output
tracks, you can create a movie containing multiple mixes of the
same source material.

This is useful for a recording situation where you have a
six channel recording device and are presenting 5.1 material. You
could make a QuickTime movie that has four tracks in it. In this
case, the first track is getting the raw, unmixed source––that
is, channels one through six. You will have a six discrete channel
track, meaning that the first channel plays out to the first speaker,
the second channel out to the second speaker, and so on.

In sequence grabber audio channel #2, you’ll get a 5.1 mix
and apply spatial orientation to the six channels, specifying the
speakers to which the audio will play. All four tracks are going
into a QuickTime movie. Sequence grabber audio channel #3 presents
a stereo mix-down, while sequence grabber audio channel #4 presents
a mono mix-down.

__Figure 2-33__  Channel mapping with simultaneous
multiple mixes

!

Figure 2-34 shows channel mapping with multi-date rates,
similar to multiple mixes, except that you can also apply compression
to the mixes. As a result, you can broadcast multiple streams at
once.

__Figure 2-34__  Channel mapping with multi-data rates

!

Figure 2-35 shows sequence grabber audio callbacks,
which are analogous to the `VideoMediaType` sequence
grabber channel video bottlenecks. The callbacks provide developers
with different places in the audio chain where they can “pipe
in” and look at the samples.

__Figure 2-35__  Sequence grabber audio callbacks,
analogous to sequence grabber video bottlenecks callbacks

!

Figure 2-36 shows sequence grabber audio callbacks,
with real-time preview. Clients can specify what they want to preview,
using the sequence grabber channel play flags.

__Figure 2-36__  SGAudio callbacks with real-time
preview

!

To make use of the new sequence grabber audio features, follow
these steps:

1. Instantiate a sequence grabber channel of subtype `SGAudioMediaType` (`’audi’`),
   by calling `SGNewChannel``(sg,
   SGAudioMediaType, &audiChannel)`.
2. Use the QuickTime component property API to obtain a list
   of available input and preview devices from the sequence grabber
   channel, by getting the property `kQTSGPropertyID_DeviceListWithAttributes` (`’#dva’`).
3. Use the same component property API to get the input device
   characteristics and set the desired audio format and device settings.
   See `[“SGAudio Component Property Classes”](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtknjqg4yde)` and `[“SGAudio Component Property IDs”](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtknjqhazts)` for
   details. Note that this is sometimes a two-stage process, as next
   described.
4. 1. Use `[QTGetComponentPropertyInfo](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6kjnztg6)` to
      determine the size of the property value.
   2. Allocate the necessary container and use `[QTGetComponentProperty](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6i)` to
      obtain the actual value. This is necessary with properties such
      as channel layout, which is a variable length structure.
5. Call `SGStartRecord` or `SGStartPreview`,
   enabling the sequence grabber, and then make periodic calls to `SGIdle`.

If you are capturing only sequence grabber audio media, it
is no longer necessary to make extremely frequent calls to `SGIdle`,
since this function is only used to write the samples to storage,
not to capture data from the input device. When capturing video
or using an old-style sequence grabber sound media component, however,
you must still call `SGIdle` frequently
(at a frequency greater than the video sample rate or the sound
chunk rate).

By setting the appropriate sequence grabber channel properties
and setting up a callback, you can examine samples at various points
in the input chain, such as premix, postmix, preconversion, and
postconversion. For details, see `[SGAudioCallbackProc](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2ti5axkzdjn5bwc3dmmjqwg22qojxwg)`, `[SGAudioCallbackStruct](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3umfts6u2hif2wi2lpinqwy3dcmfrwwu3uoj2wg5a)`, `[“SGAudio Component Property Classes”](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtknjqg4yde)` and `[“SGAudio Component Property IDs”](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtknjqhazts)`.

QuickTime 7 introduces a number of important video enhancements,
discussed in this section. These include

- Support for compressed video using frame reordering.
  Support is added for compression, playback, streaming, and low-level
  access to stored samples.
- A new visual context that provides an abstraction layer that
  is intended to decouple QuickTime from graphics worlds (GWorlds).
  This decoupling allows programmers to work in QuickTime without
  needing to understand QuickDraw, and to more easily render QuickTime
  directly using engines such as OpenGL.
- Support for H.264 video compression, including QuickTime components
  for export, playback, and live streaming.

QuickTime 7 adds support for __frame reordering__ video
compression. This is a major advance that involves new sample tables
for video to allow video frames to have independent decode and display
times.

The result of using frame reordering for video compression
is improved display, editing, and capture in H.264 and other advanced
video codec formats. Enhancements include a new API for working
with media sample times, adding and finding samples, and a new Image
Compression Manager (ICM) API.

QuickTime supports many types of video compression, including
spatial compression algorithms, such as photo-JPEG, and temporal
compression algorithms, in which some video frames are described
completely, while other frames are described in terms of their differences
from other video frames.

Up until the introduction of H.264 in QuickTime 7, video frames
could be of three kinds:

- I-frames (independently decodable)
- P-frames (predicted from a previous I- or P-frame)
- B-frames (predicted from one past and one future I- or P-frame)

Because B-frames predict from a future frame, that frame has
to be decoded before the B-frame, yet displayed after it; this is
why frame reordering is needed.The decoded order is no longer the
same as the displayed order.The QuickTime support for frame reordering is
quite general.In the H.264 codec, the concepts of the direction
of prediction, and the numbers of referenced frames, and the kind
of frame that is referenced, are all decoupled. In H.264, an encoder
may choose to make a stream in which P-frames refer to a future frame,
or a B-frame which refers to two past or future frames, for example.

For decompressors that don’t use frame reorderings, the
decode order and the display order are the same, and QuickTime sample
tables are traditionally organized to reflect this. Samples are
stored in decode order, which is presumed to be the display order,
and the sample tables specify the duration of each sample’s display;
the display time is the time when the track begins plus the duration
of all previous samples.

The addition of frame reordering support means that QuickTime
now has an optional sample table for video that specifies the offset
between the decode time and the display time. This allows frames
to be stored in decode order but displayed in a different order. The
decode time is still the beginning of the track plus the decode
duration of all previous samples, but it is now necessary to examine
the offset table to determine which samples precede others and calculate
the correct display time.

For high-level programmers, this all happens transparently.
Developers who work directly with sample numbers and sample times,
however, must be aware of this new feature. A new, expanded API
is available to support this.

Developers who need to work with specific samples based on
the samples’ display times, or who are adding samples to a media
directly, need to use a different API when working with media that
uses frame reorderings.

For example, programmers who use the function `MediaTimeToSampleNum` must
instead use the two functions `[MediaDecodeTimeToSampleNum](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxu2zlenfquizldn5sgkvdjnvsvi32tmfwxa3dfjz2w2)` and `[MediaDisplayTimeToSampleNum](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxu2zlenfqui2ltobwgc6kunfwwkvdpknqw24dmmvhhk3i)` when working
with frame reordering compressed video, as each sample now has a
decode time and a display time instead of a single media time (combined
decode/display time).

Similarly, when adding samples to a media that permits display
offsets, it is necessary to use the new `[AddMediaSample2](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxuczdejvswi2lbknqw24dmmuza)` instead
of `AddMediaSample`, as the new function
permits the user to pass a display offset and specify properties
that are unique to media with display offsets, such as whether subsequent
samples are allowed to have earlier display times than the current
sample.

Calling one of the old functions that use a single media time
value on new-format media that contains display offsets will return
the error code `kQTErrMediaHasDisplayOffsets`.

The new API elements all use 64-bit time values, whereas the
older API elements use 32-bit values. Calling one of the old functions
with a 64-bit time value returns the error code `kQTErrTimeValueTooBig`.

When creating a media for frame reordering compressed video
track, pass in the new flag `kCharacteristicSupportsDisplayOffsets`.

For details, see:

- `[AddMediaSample2](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2bmrse2zlenfqvgylnobwgkmq)`
- `[ExtendMediaDecodeDurationToDisplayEndTime](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2fpb2gk3tejvswi2lbirswg33emvchk4tboruw63sun5cgs43qnrqxsrlomrkgs3lf)`
- `[GetMediaAdvanceDecodeTime](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2e2zlenfquczdwmfxggzkemvrw6zdfkruw2zi)`
- `[GetMediaDataSizeTime64](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2e2zlenfquiylumfjws6tfkruw2zjwgq)`
- `[GetMediaDecodeDuration](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2e2zlenfquizldn5sgkrdvojqxi2lpny)`
- `[GetMediaDisplayDuration](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2e2zlenfqui2ltobwgc6keovzgc5djn5xa)`
- `[GetMediaDisplayEndTime](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2e2zlenfqui2ltobwgc6kfnzsfi2lnmu)`
- `[GetMediaDisplayStartTime](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2e2zlenfqui2ltobwgc6ktorqxe5cunfwwk)`
- `[GetMediaNextInterestingDecodeTime](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2e2zlenfqu4zlyorew45dfojsxg5djnztuizldn5sgkvdjnvsq)`
- `[GetMediaNextInterestingDisplayTime](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2e2zlenfqu4zlyorew45dfojsxg5djnztui2ltobwgc6kunfwwk)`
- `[GetMediaSample2](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2e2zlenfqvgylnobwgkmq)`
- `[MediaContainsDisplayOffsets](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2nmvsgsykdn5xhiyljnzzui2ltobwgc6kpmzthgzluom)`
- `[MediaDecodeTimeToSampleNum](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2nmvsgsykemvrw6zdfkruw2zkun5jwc3lqnrsu45ln)`
- `[MediaDisplayTimeToSampleNum](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2nmvsgsykenfzxa3dbpfkgs3lfkrxvgylnobwgkttvnu)`
- `[TrackTimeToMediaDisplayTime](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2uojqwg22unfwwkvdpjvswi2lbiruxg4dmmf4vi2lnmu)`

There is additional support for programmers who work directly
with arrays of media sample references. Although these new functions
work with frame reordering video or other media with independent
decode and display times, they can also be used with ordinary media
types. See [QuickTime Sample Table API](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgmwtmnzygu4to).

When compressing video that uses frame reordering, there is
no longer a one-to-one correspondence between submitting a frame
for compression and getting back a compressed sample. The Image
Compression Manager (ICM) and the compressor component may buffer
multiple images before determining that a series of frames should be
B-frames and a subsequent image should be decompressed out of order
so that the B-frames can refer to it. The new ICM functions do not
require a strict correlation between input frames and output frames.
Frames may be rearranged by compression and decompression modules.

The new functions allow groups of multiple pixel buffers to
be in use at various processing points in order to avoid unnecessary
copying of data, using `CVPixelBuffers` and `CVPixelBufferPool`s.
These new types are Core Foundation based. They follow Core Foundation’s
protocols for reference counting (create/copy/retain/release). Each
type has its own retain and release functions which are type-safe
and NULL-safe, but otherwise equivalent to `CFRetain` and `CFRelease`.
Note that the CVPixelBuffer functions generally provide their output
data through callbacks, rather than as return values or function parameters.

In general, the new functions return `OSStatus`,
with the exception of some simple Get functions that return single
values.

Clients create compression sessions using `[ICMCompressionSessionCreate](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2jingug33nobzgk43tnfxw4u3fonzws33oinzgkylumu)`. They then
feed pixel buffers in display order to `[ICMCompressionSessionEncodeFrame](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2jingug33nobzgk43tnfxw4u3fonzws33oivxgg33emvdheylnmu)`. Encoded
frames may not be output immediately, and may not be returned in
the same order as they are input—encoded frames will be returned
in decode order, which will sometimes differ from display order.
One of the parameters to `[ICMCompressionSessionCreate](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxusq2ninxw24dsmvzxg2lpnzjwk43tnfxw4q3smvqxizi)` specifies
a callback routine that QuickTime will call when each encoded frame
is ready. Frames should be stored in the order they are output (decode
order).

To force frames up to a certain display time to be encoded
and output, call `[ICMCompressionSessionCompleteFrames](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2jingug33nobzgk43tnfxw4u3fonzws33oinxw24dmmv2gkrtsmfwwk4y)`.

To obtain a pixel buffer pool that satisfies the requirements
of both your pixel buffer producer and the compressor, pass the
pixel buffer producer’s pixel buffer options into `[ICMCompressionSessionCreate](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxusq2ninxw24dsmvzxg2lpnzjwk43tnfxw4q3smvqxizi)`,
and then call `[ICMCompressionSessionGetPixelBufferPool](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2jingug33nobzgk43tnfxw4u3fonzws33oi5sxiudjpbswyqtvmztgk4sqn5xwy)`. The
compression session constructs an appropriate pixel buffer pool.

Alternatively, you can create your own pixel buffer pool by
obtaining the compressor’s pixel buffer attributes, choosing a
format compatible with your pixel buffer producer, and setting that
compressor’s input format using the component properties API.
The process of obtaining the pixel buffer attributes is illustrated
in the following code snippet.

```
CFDictionaryRef attributesDictionary = NULL;

err = ICMCompressionSessionGetProperty(
    session,
    kQTPropertyClass_ICMCompressionSession,
    kICMCompressionSessionPropertyID_CompressorPixelBufferAttributes,
    sizeof(CFDictionaryRef),
    &attributesDictionary,
    NULL);

if (attributesDictionary) {
    // ...use...
    CFRelease(attributesDictionary);
}
```

You can also pass arbitrary pixel buffers to `[ICMCompressionSessionEncodeFrame](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxusq2ninxw24dsmvzxg2lpnzjwk43tnfxw4rlomnxwizkgojqw2zi)`;
if they’re incompatible with the compressor’s requirements,
then the compression session will make compatible copies and pass
those to the compressor. This requires less setup but can result in
significantly slower operation.

When the compressor no longer needs a source pixel buffer,
it will release it. You may also pass `[ICMCompressionSessionEncodeFrame](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxusq2ninxw24dsmvzxg2lpnzjwk43tnfxw4rlomnxwizkgojqw2zi)` a
callback to be called when the source pixel buffer is released.

Clients may call `[ICMCompressionSessionGetImageDescription](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2jingug33nobzgk43tnfxw4u3fonzws33oi5sxislnmftwkrdfonrxe2lqoruw63q)` to
get the image description for the encoded frames. Where possible,
the ICM will allow this to be called before the first frame is encoded.

For additional details, see:

- `[ICMCompressionSessionCreate](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2jingug33nobzgk43tnfxw4u3fonzws33oinzgkylumu)`
- `[ICMCompressionSessionGetProperty](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2jingug33nobzgk43tnfxw4u3fonzws33oi5sxiudsn5ygk4tupe)`
- `[ICMCompressionSessionGetPixelBufferPool](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2jingug33nobzgk43tnfxw4u3fonzws33oi5sxiudjpbswyqtvmztgk4sqn5xwy)`
- `[ICMCompressionSessionEncodeFrame](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2jingug33nobzgk43tnfxw4u3fonzws33oivxgg33emvdheylnmu)`
- `[ICMCompressionSessionGetImageDescription](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2jingug33nobzgk43tnfxw4u3fonzws33oi5sxislnmftwkrdfonrxe2lqoruw63q)`
- `[ICMCompressionSessionCompleteFrames](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2jingug33nobzgk43tnfxw4u3fonzws33oinxw24dmmv2gkrtsmfwwk4y)`

The H.264 codec is the latest standards-based video codec.
Published jointly by the ITU as H.264––Advanced Video Coding,
and by ISO as MPEG-4 Part 10––Advanced Video Coding, the H.264
codec promises better image quality at lower bit rates than the
current MPEG-4 video codec, and also better live streaming characteristics
than the current H.263 codec.

This represents a significant increase in quality and performance,
while operating in a standards-based framework.

QuickTime 7 for Mac OS X v10.4 includes a QuickTime decompressor
component and an exporter component for creating and playing H.264-encoded
video in QuickTime.

The H.264 codec makes use of QuickTime 7’s new support for
frame reordering video compression.

QuickTime 7 introduces the __visual context__—an
abstraction that represents a visual output destination for a movie—and
the __OpenGL texture context__, an implementation
of the visual context that renders a movie’s output as a series
of OpenGL textures.

A QuickTime visual context provides an abstraction layer that
decouples QuickTime movies from GWorlds. This allows you to work
in QuickTime without have to rely on QuickDraw concepts and structures.
A visual context enables you to render QuickTime output using engines
such as OpenGL.

A visual context can act as a virtual output device, rendering
the movie’s visual output, streaming it, storing it, or processing
it in any number of ways.

A visual context can also act as a bridge between a QuickTime
movie and an application’s visual rendering environment. For example,
you can set up a visual context for OpenGL textures. This causes
a movie to produce its visual output as a series of OpenGL textures. You
can then pass the textures to OpenGL for rendering, without having
to copy the contents of a GWorld and transform it into an OpenGL
texture yourself. In this case, the visual context performs the
transformation from pixel buffers to OpenGL textures and delivers
the visual output to your application.

A `QTVisualContextRef` is
an opaque token that represents a drawing destination for a movie.
The visual context is, in object-oriented terms, a base class for
other concrete implementations of visual rendering environments.
The output of the visual context depends entirely on the implementation.
The implementation supplied with QuickTime 7 produces a series of
OpenGL textures, but the list of possible outputs is extensible.

You create a visual context by calling a function that instantiates
a context of a particular type, such as `[QTOpenGLTextureContextCreate](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvcpobsw4r2mkrsxq5dvojsug33oorsxq5cdojswc5df)`.
This allocates a context object suitable for passing to functions
such as `[SetMovieVisualContext](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvgzlujvxxm2lfkzuxg5lbnrbw63tumv4hi)` or `[NewMovieFromProperties](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2omv3u233wnfsum4tpnvihe33qmvzhi2lfom)`, which target
the visual output of the movie to the specified context.

In order to use a visual context with a QuickTime movie, you
should instantiate the movie using the new `[NewMovieFromProperties](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2omv3u233wnfsum4tpnvihe33qmvzhi2lfom)` function. This
creates a movie that can accept a visual context. You can either
specify the desired visual context when you instantiate the movie,
or set the initial visual context to `NIL` (to
prevent the movie from inheriting the current GWorld), and set the
visual context later using `[SetMovieVisualContext](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvgzlujvxxm2lfkzuxg5lbnrbw63tumv4hi)`.
See [Replacing NewMovieFrom... Functions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgmwtknjwgaztg) for details.

It is also possible to set a visual context for a movie that
was instantiated using an older function, such as `NewMovieFromFile`.
Such a movie will be associated with a GWorld. You change this to
a visual context by first calling `[SetMovieVisualContext](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvgzlujvxxm2lfkzuxg5lbnrbw63tumv4hi)` on
the movie with the visual context set to `NIL`.
This disassociates the movie from its GWorld (or any previous visual
context). You can then call `[SetMovieVisualContext](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvgzlujvxxm2lfkzuxg5lbnrbw63tumv4hi)` a
second time, this time passing in a `QTVisualContextRef`.

QuickTime 7 includes an OpenGL texture context.

A `QTOpenGLTextureContext` is
a specific implementation of the visual context that provides the
movie’s visual data to a client application as OpenGL textures.
These textures can then be rendered to the screen using OpenGL,
composited with other graphics, run through CoreImage filters, or
whatever else you, as the application developer, choose to do.

To use a `QTOpenGLTextureContext` for
rendering to OpenGL, you must first set up an OpenGL session using
your own code (Carbon, Cocoa, or CGL, for example).

Follow these steps:

1. Create an OpenGL texture context by calling `[QTOpenGLTextureContextCreate](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvcpobsw4r2mkrsxq5dvojsug33oorsxq5cdojswc5df)`,
   passing in the desired `CGLContext` and `CGLPixelFormat`.
2. Use the `QTVisualContextRef` that
   you get back to refer to your new visual context in other functions.

1. You can use the function `[QTVisualContextSetImageAvailableCallback](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvcwnfzxkylminxw45dfpb2fgzlujfwwcz3fif3gc2lmmfrgyzkdmfwgyytbmnvq)` to
   pass in an optional callback function if you want to be notified
   when the context has a new texture ready. A visual context callback
   of this type notifies you that a texture is available, but it may
   not actually be created until you ask for it. It is even possible
   for a texture to become invalid and be flushed after the callback
   and before the retrieval. Consequently, you should always poll for
   a new texture by calling `[QTVisualContextIsNewImageAvailable](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvcwnfzxkylminxw45dfpb2es42omv3us3lbm5suc5tbnfwgcytmmu)` in
   your render loop.
2. The two functions that check for availability, `QTVisualContextNewImageAvailable` and the
   callback function, are the _only_ QuickTime OpenGL
   texture context functions that are completely thread safe. All the
   other texture context functions must be called from a point in your
   application when it can be guaranteed that no other thread will
   make OpenGL calls to the same OpenGL context used by the texture
   context.
3. Set the `QTVisualContext` as the
   visual output of a movie by calling `[NewMovieFromProperties](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2omv3u233wnfsum4tpnvihe33qmvzhi2lfom)` or `[SetMovieVisualContext](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvgzlujvxxm2lfkzuxg5lbnrbw63tumv4hi)`.
   Note that `[SetMovieVisualContext](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvgzlujvxxm2lfkzuxg5lbnrbw63tumv4hi)` will
   fail if the movie was not opened using `[NewMovieFromProperties](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxu4zlxjvxxm2lfizzg63kqojxxazlsoruwk4y)`.
   Additionally, this call may fail if the host hardware is incapable
   of supporting the visual context for any reason. For example, many
   current graphics cards have a size limit of 2048 pixels in any dimension
   for OpenGL textures, so the attempt to set the visual context to
   OpenGL textures would fail with a larger movie. (One work-around
   for this problem is to resize the movie to fit within the hardware
   limitations given by `glGetIntegerv(GL_MAX_TEXTURE_SIZE,
   &maxTextureSize)`).
4. Poll for the availability of new textures by calling `QTVisualContextNewImageAvailable` during
   your render loop. Be aware that this function, or the optional callback,
   may be notifying you of a texture’s availability well ahead of
   its display time, while previous undisplayed textures remain enqueued.
5. Your application can get a texture when you are ready to work
   with it by calling `[QTVisualContextCopyImageForTime](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvcwnfzxkylminxw45dfpb2eg33qpfew2ylhmvdg64sunfwwk)`.
   You may then pass the texture to OpenGL for display. Be aware, however,
   that calls to this function may produce a null texture at times
   when there is no visual output at the specified point in the movie
   timeline.

1. You should make periodic calls to `[QTVisualContextTask](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvcwnfzxkylminxw45dfpb2fiyltnm)` during
   your program to allocate time for the OpenGL visual context to do
   its work.
2. Again, it is critical that this OpenGL texture function be
   called only at a point in your application when it can be guaranteed
   that no other thread will make OpenGL calls to the same OpenGL context
   used by the QuickTime visual context.
3. When you are done with the visual context, release it by calling `[QTVisualContextRelease](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvcwnfzxkylminxw45dfpb2fezlmmvqxgzi)`.
   You can nest calls that retain and release the context as needed.
   These calls increment and decrement the context’s reference count.
   When the count reachs zero, the context is deallocated and disposed.
   If your application creates the `QTOpenGLContext`,
   it is responsible for releasing it.

For additional details, see:

- `QTVisualContextRef`
- `[QTVisualContextCopyImageForTime](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrlgs43vmfweg33oorsxq5cdn5yhsslnmftwkrtpojkgs3lf)`
- `[QTVisualContextGetAttribute](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrlgs43vmfweg33oorsxq5chmv2ec5duojuwe5lumu)`
- `[QTVisualContextGetTypeID](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrlgs43vmfweg33oorsxq5chmv2fi6lqmveui)`
- `[QTVisualContextIsNewImageAvailable](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrlgs43vmfweg33oorsxq5cjonhgk52jnvqwozkbozqws3dbmjwgk)`
- `[QTVisualContextSetAttribute](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrlgs43vmfweg33oorsxq5ctmv2ec5duojuwe5lumu)`
- `[QTVisualContextSetImageAvailableCallback](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrlgs43vmfweg33oorsxq5ctmv2es3lbm5suc5tbnfwgcytmmvbwc3dmmjqwg2y)`
- `[QTVisualContextRetain](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrlgs43vmfweg33oorsxq5csmv2gc2lo)`
- `[QTVisualContextRelease](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrlgs43vmfweg33oorsxq5csmvwgkyltmu)`
- `[QTVisualContextTask](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrlgs43vmfweg33oorsxq5cumfzww)`
- `[SetMovieVisualContext](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvgzlujvxxm2lfkzuxg5lbnrbw63tumv4hi)`
- `[GetMovieVisualContext](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxuozlujvxxm2lfkzuxg5lbnrbw63tumv4hi)`
- `[QTOpenGLTextureContextCreate](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrhxazloi5gfizlyor2xezkdn5xhizlyorbxezlborsq)`
- `[QTVisualContextRetain](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvcwnfzxkylminxw45dfpb2fezlumfuw4)`
- `[QTVisualContextRelease](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvcwnfzxkylminxw45dfpb2fezlmmvqxgzi)`
- `[QTOpenGLTextureAvailableCallbackProc](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrhxazloi5gfizlyor2xezkbozqws3dbmjwgkq3bnrwgeyldnnihe33d)`

Developers working on non-QuartzExtreme computers should be
aware of a specific limitation with QTVisualContext. The limitation
is that with QuartzExtreme turned off, the creation of a QTVisualContext
fails with error -108.

If you launch QuartzDebug and turn off QuartzExtreme, and
then launch the LiveVideoMixer and import a movie into a channel,
it won’t play. In the console, the following error message is
returned: `QTVisualContext creation failed with
error:-108`.

QuickTime 7 introduces a replacement––`[NewMovieFromProperties](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2omv3u233wnfsum4tpnvihe33qmvzhi2lfom)`–– for `NewMovie`, `NewMovieFromDataRef`,
and all other `NewMovieFrom...` functions.

In previous versions of QuickTime, you could use other functions
that create new movies, including `NewMovieFromFile` and `NewMovieFromDataRef`.
These functions accept flags that allow you to set some movie characteristics
at creation time, but other movie characteristics are always set
by default. For example, there must be a valid graphics port associated
with a movie created by these functions, even if the movie does
not output video.

`[NewMovieFromProperties](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2omv3u233wnfsum4tpnvihe33qmvzhi2lfom)` allows you to
configure an extensible set of properties before creating a movie.
This has a number of advantages.

- You can open a movie with exactly the properties
  you want, preventing QuickTime from taking undesired default actions.
- You can also specify properties that the older functions do
  not know about, such as a visual context for the movie.

To instantiate a movie using `[NewMovieFromProperties](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxu4zlxjvxxm2lfizzg63kqojxxazlsoruwk4y)`,
follow these steps:

1. Pass in a CFString file path, a URL, or set up
   a data reference, just as you would for `NewMovieFromDataRef` or
   one of the other `NewMovieFrom_` functions.
2. Next, set up a visual context for the movie to use by calling
   a function that creates a context of a the desired type, such as `[QTOpenGLTextureContextCreate](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvcpobsw4r2mkrsxq5dvojsug33oorsxq5cdojswc5df)`.
   Similarly, you can set up an audio context if you want a device
   other than the default device.
3. Call `[NewMovieFromProperties](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2omv3u233wnfsum4tpnvihe33qmvzhi2lfom)`, passing in the
   data reference for the movie and the `QTVisualContextRef` for
   the visual context, plus any appropriate properties listed in the `QTNewMoviePropertyArray`.

Properties are passed in using a `QTNewMoviePropertyElement` struct,
which specifies the property class and property ID of each property.

The movie will automatically retain the visual context, so
if your application does not need to work with the context directly,
you may release it now.

For additional details, see:

- `QTNewMoviePropertyArray`
- `[QTNewMoviePropertyElement](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvcomv3u233wnfsva4tpobsxe5dzivwgk3lfnz2a)`
- `[NewMovieFromProperties](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2omv3u233wnfsum4tpnvihe33qmvzhi2lfom)`

QuickTime 7 introduces a new extensible metadata storage format
that allows more flexible and efficient storage of metadata, including
encapsulated storage of metadata in native format (without translating
to and from a defined QuickTime format). For developers, this means
that you can now write cleaner, more generic code that enables you to
look at, for example, all the metadata in a QuickTime or iTunes
music track using just a single function call.

Metadata, of course, is information about a file, track, or
media, such as the white balance used to create a photographic image
or the artist, album, and title of an MP3 track. Traditionally,
metadata information is stored in QuickTime user data items or in
ancilliary tracks in a movie. For example, copyright information
is normally stored in a `’@cpy’` user data
item, while cover art for an AAC audio track is normally stored
in a track that is not displayed by all applications.

The new metadata enhancements in QuickTime 7 allow you to
access both old (QuickTime) and new (iTunes) formats. The new metadata
storage format is intended as a replacement for QuickTime user data,
which was limited in features and robustness. Specifically, the
metadata enhancements introduced in QuickTime 7 provide the following capabilities:

- The ability to assign data types to any metadata
  that you place into the new storage format.
- The ability to assign locale information––for example,
  a particular language or country––to the format.
- The ability to use a more descriptive key in the storage format––for
  example, a reverse DNS format, such as com.apple.quicktime.mov.

The new metadata format allows storage of data that is not
possible in user data items, without extending the list of item
types exhaustively, and allows labeling of metadata unambiguously,
rather than as data in an undisplayed media track. It also permits inclusion
of metadata that is always stored external to the movie, even when
the movie is flattened (saved as self-contained).

Metadata is encapsulated in an opaque container and accessed
using a `QTMetDataRef`.
A `QTMetaDataRef` represents a metadata
repository consisting of one or more native metadata containers.
The QuickTime metadata API supports unified access to and management
of these containers.

Each container consists of some number of metadata items.
Metadata items correspond to individually labeled values with characteristics
such as keys, data types, locale information, and so on. Note that
what QuickTime calls _items_ are sometimes referred
to as _attributes_ or _properties_ in
other metadata systems.

You address each container by its storage format (`kQTMetaDataStorageFormat`).
Initially, there is support for classic QuickTime user data items,
iTunes metadata, and a richer QuickTime metadata container format.
A `QTMetaDataRef` may have one or all
of these. No direct access to the native storage containers is provided.

`QTMetaDataRefs` may be associated
with a movie, track or media. This parallels user data atoms usage
but provides access to other kinds of metadata storage at those
levels.

A metadata item is assigned a runtime identifier (`QTMetaDataItem`)
that along with the `QTMetaDataRef` identifies
the particular item (and value) across all native containers managed
by the `QTMetaDataRef`.

Each item is addressed by a key, or label. The key is not
necessarily unique within its container, as it is possible to have
multiple items with the same key (for example, multiple author items).
Functions exist to enumerate all items or only items with a particular
key.

Because a `QTMetaDataRef` may
provide access to different native metadata containers with differing
key structures—a four-char-code for one, a string for another,
and so on—the key structure is also specified. A `QTMetaDataKeyFormat` indicates
the key structure to functions that take keys. This also supports
container formats that allow multiple key structures or multiple
versions of key structures.

To allow unified access across disparate containers, you can
specify a wildcard storage format. This can be used for operations
such as searches across container formats. A special key format
called `kQTMetaDataKeyFormatCommon` indicates
one of a set of common keys that can be handled by multiple native
containers (for example, copyright).

Both modes of operation are illustrated in Figure 2-37.

__Figure 2-37__  Metadata modes of operations

!

The QuickTime metadata format is inherently extensible. Instead
of a set of structures and enumerated parameters, the metadata API
uses a set of properties that can be enumerated, and whose characteristics
can be discovered, dynamically at runtime. This is analogous to the
QuickTime component property function in that you first get the
property info, such as its size and format, and then you allocate
the appropriate container or structure to get or set the actual
property.

The new QuickTime metadata format and API consist of the following
structures, enumerations, and functions, grouped in sections followed
by the specific functions:

- `[“Metadata Format Constants”](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtknjtge4tk)`
- `[“Metadata Property IDs”](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtknjtgm3tq)`
- `[“Metadata Key Constants”](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtknjtg4zda)`
- `[“Metadata Error Codes”](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtmmrvheyds)`
- `[QTCopyMovieMetaData](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrbw64dzjvxxm2lfjvsxiykemf2gc)`
- `[QTCopyTrackMetaData](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrbw64dzkrzgcy3ljvsxiykemf2gc)`
- `[QTCopyMediaMetaData](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrbw64dzjvswi2lbjvsxiykemf2gc)`
- `[QTMetaDataAddItem](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrgwk5dbirqxiykbmrses5dfnu)`
- `[QTMetaDataGetItemCount](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrgwk5dbirqxiykhmv2es5dfnvbw65looq)`
- `[QTMetaDataGetItemProperty](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrgwk5dbirqxiykhmv2es5dfnvihe33qmvzhi6i)`
- `[QTMetaDataGetItemPropertyInfo](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrgwk5dbirqxiykhmv2es5dfnvihe33qmvzhi6kjnztg6)`
- `[QTMetaDataGetItemValue](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrgwk5dbirqxiykhmv2es5dfnvlgc3dvmu)`
- `[QTMetaDataGetNextItem](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrgwk5dbirqxiykhmv2e4zlyorexizln)`
- `[QTMetaDataGetProperty](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrgwk5dbirqxiykhmv2fa4tpobsxe5dz)`
- `[QTMetaDataGetPropertyInfo](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrgwk5dbirqxiykhmv2fa4tpobsxe5dzjfxgm3y)`
- `[QTMetaDataRetain](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrgwk5dbirqxiyksmv2gc2lo)`
- `[QTMetaDataRelease](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrgwk5dbirqxiyksmvwgkyltmu)`
- `[QTMetaDataRemoveItem](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrgwk5dbirqxiyksmvww65tfjf2gk3i)`
- `[QTMetaDataRemoveItemsWithKey](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrgwk5dbirqxiyksmvww65tfjf2gk3ltk5uxi2clmv4q)`
- `[QTMetaDataSetItem](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrgwk5dbirqxiyktmv2es5dfnu)`
- `[QTMetaDataSetItemProperty](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrgwk5dbirqxiyktmv2es5dfnvihe33qmvzhi6i)`
- `[QTMetaDataSetProperty](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrgwk5dbirqxiyktmv2fa4tpobsxe5dz)`

The new QuickTime sample table API in QuickTime 7 is used
when you need to obtain information about samples—such as their
size, location, and sample descriptions—or to set this kind of
information (for example, when adding samples or blocks of samples
to a media directly, without using the services of an importer or
sequence grabber).

This new API introduces `QTSampleTable` as
a logical replacement for the arrays of sample reference records
used with the older functions `AddMediaSampleReferences` and `AddMediaSampleReferences64`.
New functions allow you to operate on whole tables of data simultaneously.

Like many new QuickTime APIs, the QuickTime sample table API
uses opaque data types whose properties can be discovered dynamically
at runtime. This is analogous to the component properties API for
configuring components. You use a `GetPropertyInfo` function
to discover the size and format of a property, then allocate the
necessary container or structure to get or set the actual property.

This API works with both simple media types that have a single
media time for each sample and new media types such as frame reordering
video that have independent decode and display times for samples.

In the QuickTime sample table API, sample numbers for audio
always refer to packets. This is simpler and more consistant, but
it means that a new function may not return the same value as an
older, analogous function when called with reference to compressed
CBR sound. For example, `[QTSampleTableGetNumberOfSamples](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvctmfwxa3dfkrqwe3dfi5sxittvnvrgk4spmzjwc3lqnrsxg)` may
return a different sample count than `GetMediaSampleCount`.

All compressed audio is quantized into packets, and each packet
can be decompressed into multiple PCM samples. With previous APIs,
media sample numbers for CBR sound refer to PCM samples, rather
than the compressed packets. When the same APIs are applied to variable-bit-rate
(VBR) sound, however, the sample numbers refer to packets. This inconsistency
means that code using these older APIs must handle CBR and VBR differently.
In this API, by contrast, sample numbers always refer to packets.

This applies only to _compressed_ CBR sound,
however. In uncompressed sound tracks, each packet is simply an
uncompressed PCM frame, so the value is the same whether the sample
number refers to packets or PCM samples.

For full details of the QuickTime sample table API, see:

- `[QTSampleTableCreateMutable](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjwc3lqnrsviylcnrsug4tfmf2gktlvorqwe3df)`
- `[QTSampleTableCreateMutableCopy](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjwc3lqnrsviylcnrsug4tfmf2gktlvorqwe3dfinxxa6i)`
- `[QTSampleTableAddSampleDescription](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjwc3lqnrsviylcnrsuczdeknqw24dmmvcgk43dojuxa5djn5xa)`
- `[QTSampleTableCopySampleDescription](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjwc3lqnrsviylcnrsug33qpfjwc3lqnrsuizltmnzgs4dunfxw4)`
- `[QTSampleTableAddSampleReferences](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjwc3lqnrsviylcnrsuczdeknqw24dmmvjgkztfojsw4y3fom)`
- `[AddSampleTableToMedia](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2bmrsfgylnobwgkvdbmjwgkvdpjvswi2lb)`
- `[CopyMediaMutableSampleTable](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dn5yhstlfmruwctlvorqwe3dfknqw24dmmvkgcytmmu)`
- `[QTSampleTableReplaceRange](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjwc3lqnrsviylcnrsvezlqnrqwgzksmfxgozi)`
- `[QTSampleTableGetProperty](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjwc3lqnrsviylcnrsuozlukbzg64dfoj2hs)`
- `[QTSampleTableSetProperty](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjwc3lqnrsviylcnrsvgzlukbzg64dfoj2hs)`
- `[QTSampleTableGetPropertyInfo](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjwc3lqnrsviylcnrsuozlukbzg64dfoj2hsslomzxq)`
- `[QTSampleTableGetNumberOfSamples](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjwc3lqnrsviylcnrsuozlujz2w2ytfojhwmu3bnvygyzlt)`
- `[QTSampleTableGetSampleDescriptionID](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjwc3lqnrsviylcnrsuozluknqw24dmmvcgk43dojuxa5djn5xesra)`
- `[QTSampleTableGetDataSizePerSample](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjwc3lqnrsviylcnrsuozluirqxiyktnf5gkudfojjwc3lqnrsq)`
- `[QTSampleTableGetSampleFlags](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjwc3lqnrsviylcnrsuozluknqw24dmmvdgyylhom)`
- `[QTSampleTableGetDataOffset](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjwc3lqnrsviylcnrsuozluirqxiykpmzthgzlu)`
- `[QTSampleTableGetDisplayOffset](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjwc3lqnrsviylcnrsuozluiruxg4dmmf4u6ztgonsxi)`
- `[QTSampleTableGetTypeID](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjwc3lqnrsviylcnrsuozlukr4xazkjiq)`
- `[QTSampleTableGetDecodeDuration](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjwc3lqnrsviylcnrsuozluirswg33emvchk4tboruw63q)`
- `[QTSampleTableGetNextAttributeChange](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjwc3lqnrsviylcnrsuozlujzsxq5cbor2he2lcov2gkq3imfxgozi)`
- `[QTSampleTableGetTimeScale](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjwc3lqnrsviylcnrsuozlukruw2zktmnqwyzi)`
- `[QTSampleTableRelease](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjwc3lqnrsviylcnrsvezlmmvqxgzi)`
- `[QTSampleTableReplaceRange](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjwc3lqnrsviylcnrsvezlqnrqwgzksmfxgozi)`
- `[QTSampleTableRetain](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjwc3lqnrsviylcnrsvezlumfuw4)`
- `[QTSampleTableSetTimeScale](../Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2rkrjwc3lqnrsviylcnrsvgzlukruw2zktmnqwyzi)`

New in QuickTime 7, the QuickTime plug-in for Safari is now
fully scriptable using JavaScript. This means you can now use JavaScript
to control QuickTime when webpages are viewed using Safari.

Two plug-ins are available in QuickTime 7 for Mac OS X v10.4:
Carbon and a new Cocoa plug-in. From the user’s perspective, these
plug-ins look and behave the same. The Cocoa plug-in works only
in Safari, however. The benefit for both users and developers is
that the plug-in is now scriptable.

To control a movie through the QuickTime plug-in using JavaScript,
you must include the parameter `EnableJavaSript="true"` in
the movie’s `EMBED` tag
(this parameter is not needed in the `OBJECT` tag,
but it does no harm there).

JavaScript treats each embedded QuickTime movie in a webpage
as a separately addressable object. Movies can be identified by
name if there is a `NAME` parameter
in the movie’s `EMBED` tag
and an `ID` attribute in
the movie’s `OBJECT` tag.
Internet Explorer for Windows uses the `ID` attribute.
Other browsers use the `NAME` parameter.
Both `NAME` and `ID` should
be set to the same value.

For example, to create a movie that can be addressed in JavaScript
as `Movie1`, your `OBJECT` and `EMBED` tags
would look something like this:

```
<OBJECT classid="clsid:02BF25D5-8C17-4B23-BC80-D3488ABDDC6B"
    codebase="http://www.apple.com/qtactivex/qtplugin.cab"
    width="180" height="160"
    id="movie1" >

    <PARAM name="src" value="My.mov">

    <EMBED width="180" height="160"
        src="My.mov"
        name="movie1"
        enablejavascript="true">
    </EMBED>
</OBJECT>
```

Movies can also be identified by their ordinal number in the
JavaScript `embeds[]` array.

An example of usage and syntax, showing JavaScript control
of multiple QuickTime movies using different methods of addressing,
can be found in [Sample JavaScript Usage](https://developer.apple.com/documentation/QuickTime/REF/QT41_HTML/QT41WhatsNew-80.html).

QuickTime exposes dozens of methods to JavaScript, allowing
you to control not only the standard user interface actions, such
as playing and stopping a movie, but also more complex actions,
such as layering and compositing. You can use JavaScript, for example, to
enable and disable alternate audio, text, or video tracks, or change
a video track’s graphics mode or a sprite’s current image.

Detailed descriptions of the QuickTime methods and properties
available to JavaScript can be found in [JavaScript Support](https://developer.apple.com/documentation/QuickTime/REF/QT41_HTML/QT41WhatsNew-72.html).

This section discusses the following changes and enhancements
that are available in QuickTime 7.

QuickTime 7 introduces a new __persistent cache__ option,
which is enabled in the System Preferences > QuickTime > Browser
panel, as shown in Figure 2-38. Users, web
authors, and web content developers should understand the consequences
of this new option because it may impact the way that QuickTime
content is downloaded and saved from their websites. The reason
is that QuickTime’s caching behavior has changed in this release.

__Figure 2-38__  QuickTime Browser preferences with
the Save movies in disk cache box checked

!

By default, the user preference is set to “Save movies in
disk cache.” This means that files downloaded by QuickTime and
written to the cache will now stay in the cache when the last connection
to the file is closed. By contrast, in pre-QuickTime 7 versions,
downloaded files would be written to disk and but only remain there
as long as the user kept open a connection to the file. After the
movie was closed, the local file would be deleted. If you wanted
to look at the movie again, you would have to download the file
in its entirety another time.

If the user unchecks the preference, QuickTime’s old behavior
prevails—that is, movies downloaded to disk will only be saved
as long as they remain open. There may be situations, for example,
when unchecking the box is warranted: users don’t want any QuickTime
content to be cached perhaps for privacy reasons, or if they don’t
have enough disk space on their computers.

When the preference is checked, movies downloaded by QuickTime
will be saved in the cache. The slider allows the user to set the
maximum size of the cache (the minimum is 100 MB). Note that QuickTime’s
cache is per user, not computer wide. This means that if you have
more than one account on the computer, each user’s setting and
cached movies are for themselves only.

When the cache is on, files may not remain in the persistent
cache because of settings on the server. If you have administrator
(admin) access to a server, you can tell the server to include information
in the file header that specifies how long it is allowed to stay
on the user’s computer. The header can say, “Don’t cache this
at all.” Or, “Only keep it for a week.” QuickTime pays close
attention to the information that is stored in the headers.

In particular, when the cache is enabled QuickTime honors
the “expiration date,” often supplied by web servers to inform
clients of how long a file remains valid after it has been downloaded.
Until the expiration date supplied by the server is reached, QuickTime
will respond to additional requests for the file by supplying the
file from the cache instead of by fetching it again from the server.
This remains true even if the file is changed on the server before
the expiration date is reached. Previous versions of QuickTime as
described above always downloaded a file afresh, if a previous version
of it was no longer still open and in use, and therefore changes
to files made before the expiration date would often be accessible
immediately.

There are several ways to control QuickTime’s file caching
behavior. Each step, listed below, may be appropriate for a different
situation:

- __HTTP headers__. Useful only
  if you have admin access to the server on which the files are posted.
  Consult your web server documentation for specifics (for example,
  look for “Cache-Control: no-cache” and “Expires:”).
- __“cache” EMBED/OBJECT attribute__. Useful
  if your movies are embedded in HTML pages, but you don’t have
  adminaccess to the server. This is a very common situation.

  In
  previous versions of QuickTime, this tag told the plug-in to ask
  the browser not to keep an embedded movie in its cache. This is
  still true, but now it also tells the plug-in to not keep the movie
  in the QuickTime persistent cache either.
- __XML movies__. The “cache” attribute has
  been added to QuickTime Media Link importer. Adding ‘cache=”false”’
  to a media link movie will keep it from being saved in QuickTime’s
  persistent cache. See the documentation [QuickTime Media Links XML Importer](https://developer.apple.com/documentation/QuickTime/WhatsNewQT5/QT5NewChapt1/chapter_1_section_39.html) for more information about this movie
  importer.

When a movie is tagged as “not cacheable” with any of
these methods, QuickTime will not keep the movie or any media loaded
by it in the persistent cache (for example, sprite images loaded
by URL).

QuickTime for Java (QTJ) is now fully supported in QuickTime
7. QTJ is now installed by default in QuickTime 7.

This release includes a number of important bug fixes requested
by QuickTime for Java developers. These are as follows:

- Major fixes for issues related to drawing and
  correct QTComponent rendering
- Compatibility with headless applications
- Fixes for issues related to movie progress procedures and
  movie exporting
- Fixes for Applet issues, including support for MPEG video
  playback in an applet
- Support for 2-byte character file names
- Security fixes

QuickTime can read Quartz Composers. Also, Quartz Composer
compositions can be exported as QuickTime movies.

You can accomplish this either by using the Export menu command
in the Quartz Composer Editor, or by opening the composition in
QuickTime Player and saving it as a movie.

[Next](New%20Functions%2C%20Data%20Types%2C%20and%20Constants%20in%20QuickTime%207.md)[Previous](Introduction%20to%20QuickTime%207.md)

