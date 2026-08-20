---
title: QuickTime & Memory
apple_id: DTS10001971
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb01.html
archived_at: '2026-07-18T02:38:47.632747Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Movie Basics](https://developer.apple.com/referencelibrary/QuickTime/idxMovieBasics-date.html)

|  |
| --- |
| Technical Q&A QTMTB01QuickTime & Memory |

|  |
| --- |
| Q We're developing a CD- ROM-based application for kids. Because many Macintoshes have only 4MB of RAM, we've taken steps to ensure that our application can run in a 2048KB partition, so that users who have System 7 installed (with a low number of INITS) will have enough memory to run our application. Our application supports QuickTime 2.0. In it, we have 320 x 240 movies that are in millions of colors and are compressed with CinePak compression. We are experiencing the following problem:  When we play a movie, especially on a slower Macintosh, such as a IIci, there are a lot of sound and frame dropouts. This situation only happens when there is no system memory left when we start up. If there is 500KB or more available, the movies play normally. We found that when we start to play a movie, about 500KB is allocated in the system heap, if this much is available. If 500KB isn't available, the movie plays very poorly. We have attempted to always have approximately 800KB of unfragmented memory available in our heap when we start to play a movie.  It would be very difficult to reduce our application partition below 2048KB, even though we can provide 800KB of unfragmented memory when we are playing movies. Is there a way to have QuickTime allocate the necessary memory from our application heap instead of from system memory when additional system memory is not available?  A In general, you use QuickTime structures to allocate memory in the application heap, with the exception of a small amount of QT globals and any codecs that you load when needed. QuickTime allocates very few memory-based resources as part of the EnterMovies call. After this, the memory used for various operations depends on what functionality the program calls, either QT API-based functionality, or functions that the application itself handles. Bear in mind that other system resources also require memory in the system heap, such as the Sound Manager (when it allocates sound channels).  Allocating Master Pointers  The application itself may allocate many handles during QuickTime-toolbox related operations, such as when opening movie files, creating movies, and otherwise operating on movie resources. This is why it's very important to allocate enough master pointers.  If there are not enough master pointers allocated at the init phase of the application, the Memory Manager must create new pointers on-the-fly during handle-creation operations. These additional master pointers usually end up as islands somewhere in the middle of the application heap, causing memory compaction and slowness when allocating more handle space.  Expanding the Application Heap Zone and Allocating Master Pointers  You also need to call MaxApplZone to expand the application heap zone so it includes all available heap memory (note that MaxApplZone doesn't purge any current blocks in the application heap). Because the Memory Manager grows the heap only when there is no purgeable or free space left, QuickTime doesn't have the space needed to play back a movie optimally.  You should then call MoreMasters N times. Each time MoreMasters is called, it allocates 64 master pointers (assuming you are using the application heap and not the system heap). You'll probably need to call MoreMasters at least 10 times.  To empirically measure how many Master Pointers the application needs at the maximal point, use MacsBug, as follows:  Drop down to MacsBug, and type hd. If the size of the entry in the length column is 100 (256 bytes), the entry is probably a master pointer. By determining the number of master pointers that were allocated during the application's peak memory-allocation period (or possibly at the end of a long application session), you can determine how many master pointers the application needs, and allocate them when the application starts.  The example below shows how all this works together:   ``` const kMasterCalls 10;  void main() {    MaxApplZone();     long i;    for(i = 0; i< kMasterCalls; i++)       MoreMasters();   // continue with the normal inits    InitGraf(&qd.thePort); // ... ```   Memory Use During Playback  In some cases, a QuickTime-aware application or a multimedia title requires a great deal of memory, using most of the available RAM in smaller footprint systems for the application heap. For example, in a 4MB system, the system may use 1.5MB and the application 2.4MB, leaving only 900KB in the application heap. If the Sound Manager allocates sound channels, it uses the system heap. Running out of system-heap space makes it impossible to play sound resources and/or movie tracks. If you don't quite run out of system-heap space, but very little system-heap space is left, performance suffers.  The Apple Multimedia tuner patches the Sound Manager, so that it tries to allocate sound channels using the application heap (provided there's free application-heap space) in situations where system-heap space is limited or non-existent.  You can also purge unused resources, handles/pointers, and code segments in the application frequently using a GrowZoneProc that indicates when the application is running low on memory. You could also configure the GrowZoneProc to signal the end user when the application requires more memory. In a worst-case situation, the end user can try to free up memory to enlarge the application heap, or even purchase more RAM.  If the application uses some handles on a temporary basis only, you can use the MultiFinder's temp memory calls to decrease the size of the application heap.  Memory Movement During Playback  Callbacks that occur during normal movie playback (during MoviesTask time) should execute as quickly as possible to improve performance by reducing the amount of work the callbacks need to do. One aspect of this is memory allocation. If the proc allocates a handle every time it's called, and due to lack of space, the Memory Manager needs to compact the heap, this decreases performance. If possible, allocate data structures and handles before the proc is called. In some cases, this is a necessity, but you should preallocate whenever it's possible.  Loading Movies in RAM.  The QuickTime LoadMovieIntoRam function loads all of a movie's data into memory. If the movie does not fit in available memory, LoadMovieIntoRam returns an error. If you don't check for this error, you may erroneously assume that the movie was indeed loaded into RAM, but performance is still poor.  Checking for an error from LoadMovieIntoRam also allows you to ensure that you have enough heap space allocated for such operations. To test this, load the biggest movie you have into RAM. You can use Swatch, ZoneRanger, and/or the MacsBug HT command to provide information about how many free blocks are available in the application heap, and you can fine-tune the loading process by specifying the time and duration of the movie to be loaded. There is additional information regarding other parameters you can use with LoadMovieIntoRam on page 2-140 of _Inside Macintosh:QuickTime_.  If necessary, you can load a specific track of a movie into memory using LoadTrackIntoRam, or you can load the media of a movie into RAM using LoadMediaIntoRam. In QuickTime 2.0 you can specify options for preloading into the movie itself. When you use the new SetTrackLoadSettings function, you don't need to call LoadTrackIntoRam every time. Smaller tracks, such as text tracks and small sound tracks that are frequently used, are good candidates for preloading in RAM. [May 01 1995] |

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
