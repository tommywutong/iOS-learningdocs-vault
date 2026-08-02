---
title: Video
apple_id: 10000106i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2002-11-12'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Video/Concepts/movies.html
archived_at: '2026-07-15T07:21:06.327742Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Video](Introduction%20to%20Video.md)


[Next](Archiving%20NSMovie%20Objects.md)[Previous](Introduction%20to%20Video.md)

# QuickTime Movies In Cocoa

Cocoa represents QuickTime movies as NSMovie objects. Any
QuickTime-readable movie can be loaded into an NSMovie object; the
movie data can be read from a pre-existing QuickTime movie pointer,
a URL, or a pasteboard. The NSMovie class does not define methods
for manipulating the movie data directly, but you can obtain a pointer
to the data (with the `QTMovie` method) and
then use the extensive QuickTime APIs. Primarily, NSMovie is used
to display a movie inside an NSMovieView.

An NSMovieView displays an NSMovie object in a frame and provides
methods for playing and editing the movie. With NSMovieView, you
can control the sound volume, play speed, looping mode, and movie
controller visibility. With the standard QuickTime movie controller
visible, the user can play the movie, set the volume, reposition
the play head, and make selections. (Note that the movie controller
operates directly on the movie, bypassing the NSMovieView methods.)
If the movie is editable, the user can also perform copy and paste
operations on the movie. (See [Archiving NSMovie Objects](Archiving%20NSMovie%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgaydalkcineuoskfinba) for details on saving a modified
movie to a file.)

[Next](Archiving%20NSMovie%20Objects.md)[Previous](Introduction%20to%20Video.md)

