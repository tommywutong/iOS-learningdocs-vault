---
title: qtflattentohandle.win
apple_id: DTS10000896
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtflattentohandle.win/Introduction/Intro.html
archived_at: '2026-07-26T19:52:49.292128Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](README.txt.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# qtflattentohandle.win

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 DataHandlerType provides data input and output services to the media handler. Open movie, flatten, then play |
| __Build Requirements:__ | QTWindows SDK |
| __Runtime Requirements:__ | Carbon |

__Important__ This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

This sample code has been updated for QuickTime 5.0 README - QTFlattenToHandle QTFlattenToHandle.c defines functions that illustrate how to use the handle data handler. A data handler is a component (of type DataHandlerType) that is responsible for reading and writing a media's data. In other words, a data handler provides data input and output services to the media's media handler. Originally, QuickTime included a file data handler. QuickTime version 2.0 introduced the handle data handler (component subtype HandleDataHandlerSubType), which allows you to play movie data stored in memory rather than in a file. This sample code shows how to work with the handle data handler. Here, we will open a movie file and then flatten the movie data into a handle. Then we will play the movie from the handle. The essential step is to create a data reference record describing the handle and then pass that record, instead of an FSSpec record, to FlattenMovieData. To do this, set the flattenFSSpecPtrIsDataRefRecordPtr flag when calling FlattenMovieData.

[Next](README.txt.md)

