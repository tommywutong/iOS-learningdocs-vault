---
title: DVD Playback Services Programming Guide
apple_id: TP40002163
resource_type: Guide
platform: macOS
topic: Audio, Video, & Visual Effects
technology: DVDPlayback
published: '2010-03-24'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/DVDPlaybackGuide/dvdguide_glossary/dvdguide_glossary.html
archived_at: '2026-07-15T07:35:41.730844Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [DVD Playback Services Programming Guide](Introduction%20to%20DVD%20Playback%20Services%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Additional%20Programming%20Tasks.md)

# Glossary

- __angle__

  In DVD-Video, a specific view of a scene, usually recorded from a certain camera angle. Different angles can be chosen while viewing the scene.

- __aspect ratio__

  The width-to-height ratio of an image. For example, a 4:3 aspect ratio means the horizontal size is a third again wider than the vertical size. Every title on a DVD is authored for one of two aspect ratios: standard (4:3) or wide (16:9).

- __bookmark__

  A data object that specifies the current media position during playback. Because the byte length of a bookmark is known, you can save the bookmark in a file for later use.

- __chapter__

  1. In DVD-Video, a division of a title. Technically called a part of title (PTT). 2. A method of organizing different scenes of a movie for easy navigation and access. DVDs are indexed by chapter, similar to the way a CD has a track. DVD players allow you to skip to a particular chapter or scene.

- __disc menu__

  The main menu from which titles are selected. The disc menu is sometimes called the title menu, which more accurately refers to the menu within a title from which chapters and other features can be selected.

- __DVD (digital versatile disc)__

  A high-capacity optical disc used to store everything from massive computer applications to full-length movies. A standard single-layer, single-sided DVD can store 4.7GB of data.

- __DVD-Video__

  A standard for storing and reproducing audio and video on DVD-ROM discs, based on MPEG-2 video compression, Dolby Digital and MPEG audio, and other proprietary data formats.

- __DVD@ccess__

  An Apple technology you can use to add interactivity to a DVD when played on a computer. DVD@ccess makes it possible to open a web browser to display HTML files, or open a program to view PDF, PICT, or JPEG files.

- __DVD event__

  A notification of a state change in DVD Playback Services during playback. An event is specified with a type identifier and associated data. Client applications can register callback functions to receive events of interest.

- __DVD player__

  1. A hardware product that decodes and plays DVD-Video media stored on an optical disc. The output device is generally a television set, although some players have built-in displays and speakers. 2. A computer software program that decodes and plays DVD-Video media stored on an optical disc or a mass storage device such as a hard drive.

- __format standard__

  A television video broadcast format standard. DVD Playback Services supports two format standards: the NTSC format used in North America and Japan, and the PAL format used in Europe and other continents.

- __media folder__

  The video directory on a DVD disc volume. See VIDEO_TS.

- __media ID__

  A unique identifier assigned to a media folder by DVD Playback Services. This identifier can be used as a key when saving information about media playback, such as bookmarks.

- __play state__

  During playback, a DVD can be in one of four play states—playing at a normal rate, paused, scanning forward, or scanning backward.

- __region code__

  A code identifying one of the world regions for restricting DVD-Video playback. The different areas of the globe have been divided into eight separate regions to accommodate the varying release patterns of movies by the major studios. Therefore, each DVD player is compatible with a certain region: Region 1 for the United States and Canada, for example, and Region 2 for Japan and Europe. A DVD designated Region 0 can be played on any player regardless of its nationality.

- __scan direction__

  A forward or backward direction with respect to the video stream.

- __scan rate__

  A constant used in DVD Playback Services to specify the speed of play. A scan rate of 1x represents the normal playback speed; other scan rates are multiples of the normal speed.

- __scene__

  See chapter.

- __stream__

  In DVD-Video, a flow of data that contains information of a specific type, such as video, audio, subpictures, navigation data, and so on.

- __subpicture__

  A graphic bitmap overlay used in DVD-Video to create subtitles, captions, karaoke lyrics, menu highlighting effects, and so on.

- __title__

  The largest unit of a DVD-Video disc (other than the entire volume or side). Usually a movie, TV program, music album, or the like. A disc can hold up to 99 titles, which can be selected from the disc menu.

- __VIDEO_TS__

  The file name used for the video directory or folder on a standard-definition DVD disc volume. Files inside this directory contain pointers to the sectors on the disc which hold the program streams.

[Next](Document%20Revision%20History.md)[Previous](Additional%20Programming%20Tasks.md)

