---
title: Video
apple_id: 10000106i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2002-11-12'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Video/Tasks/archiving.html
archived_at: '2026-07-15T07:21:07.341989Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Video](Introduction%20to%20Video.md)


[Next](Document%20Revision%20History.md)[Previous](QuickTime%20Movies%20In%20Cocoa.md)

# Archiving NSMovie Objects

When an NSMovie object is archived, its data is encoded either
as a simple path to the original movie file or as a special QuickTime-defined
description of the movie’s contents. When initialized from a URL,
using `initWithURL:byReference:` or `NSMovie(aURL,
byRef)`, the movie’s URL is archived if the _byRef_ parameter
is `YES`. The archived URL is then
used when unarchiving to load the movie data from the original file.
If _byRef_ is `NO`,
the movie’s QuickTime header information is archived. This information
describes the movie’s contents, such as number of tracks and media
format. When possible, the header information contains references
to the files in which the original media samples are stored rather
than the samples themselves. When unarchived, QuickTime relocates
the source files (even if they have been moved or renamed) and reconstructs
the movie. To produce a self-contained movie with all the data in
a single file, obtain the QuickTime `Movie` object from `QTMovie` (Objective-C
only) and then use the QuickTime function `FlattenMovieData` to save
the data to disk.

Similarly, when initialized from a pasteboard, using `initWithPasteboard:` or `NSMovie(aPasteboard)`,
the movie’s URL is archived if the pasteboard contains `NSFilenamesPboardType`.
If the pasteboard instead contains the movie data, the movie’s header
information is archived.

A modified movie is always archived by archiving its header
information.

[Next](Document%20Revision%20History.md)[Previous](QuickTime%20Movies%20In%20Cocoa.md)

