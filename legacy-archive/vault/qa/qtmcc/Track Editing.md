---
title: Track Editing
apple_id: DTS10001960
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2011-07-12'
source_url: https://developer.apple.com/library/archive/qa/qtmcc/qtmcc17.html
archived_at: '2026-07-18T02:38:47.358878Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/QuickTime/index.html) > [Movie Basics](https://developer.apple.com/library/archive/technicalqas/QuickTime/idxMovieBasics-date.html) >

|  |
| --- |
| Technical Q&A QTMCC17Track Editing |

|  |
| --- |
| ---   Q: I've been working with QuickTime edit lists and would like some clarification regarding the track-editing APIs. I've noticed QuickTime routines such as `NewTrackEditState`, `UseTrackEditState` and `DisposeTrackEditState`: what are these used for?  To modify the entries in a QuickTime movies edit list table I use APIs such as `InsertTrackSegment` and `DeleteTrackSegment`, how do these calls affect the actual media samples? For example, if I use `DeleteTrackSegment`, are the media samples in the segment actually deleted?  How does `InsertEmptyTrackSegment` work? Does it put a "zero-sample" in the media data or does it tell the movie controller to do nothing in the specified time interval? Which field of which atom is being modified by this routine?  A: Each track in a QuickTime movie contains a list of references which identify the portions of the tracks media being used. The `TrackEditState` identifier which is returned from `NewTrackEditState` contains all the information describing a track's contents; this includes the identity of the media data associated with the track and all the tracks edit lists. This "state" can then be used with `UseTrackEditState` to return a track to its previously created edit state (i.e., "Undo"). `DisposeTrackEditState` simply disposes of the `TrackEditState` identifier created when `NewTrackEditState` is called. Although these APIs allow you to work with the track's edit state, they do not allow you to modify this state.  To modify the entries in a QuickTime Movies edit list, you need to use a number of track related editing APIs. These include `InsertMediaIntoTrack`, `InsertTrackSegment`, `DeleteTrackSegment`, `ScaleTrackSegment` and `InsertEmptyTrackSegment`. If you would like to perform the same operations across all tracks of a movie use `InsertMovieSegment`, `DeleteMovieSegment`, `ScaleMovieSegment` and `InsertEmptyMovieSegment`.  None of the editing APIs will modify or delete already written media samples. `DeleteTrackSegment` and `InsertEmptyTrackSegment` just update the Track's edit list structure which maps from the movie's play list to the media to actually play.  When you call `DeleteTrackSegment`, the deleted segment is removed from the edit list and all following references to the media are moved forward. `InsertEmptyTrackSegment` adds a special sentinel value to the edit list, indicating that no media should be played for that empty segment's duration. `InsertTrackSegment` copies references. `ScaleTrackSegment` changes the edit list in such a way that the media referenced changes its rate so as to fill the new duration.  There is an exception with `InsertTrackSegment` if you have enabled media changes by calling `BeginMediaEdits`. In this case, if you are inserting sample references to as yet un-referenced media in the destination track, the sample data will be copied the first time it is referenced. If you don't want this behavior just don't call `BeginMediaEdits`.  In all cases where `BeginMediaEdits` has not been called, no media is harmed.  The editing APIs all make adjustments to the `'elst'` atom found in the `'edts'` atom found in the `'trak'` atom found in the `'moov'` atom. Consult the file format documentation for more information regarding these atoms.  Finally, you cannot insert an empty segment at the end of the track and then add sample references. An empty insertion at the end of the track will disappear, since after the end of the track there is already an empty segment. If you must add empty space before some sample references, add the sample references and then insert the empty segment before the references which will move them into place.  For more information regarding editing and the `'elst'` atom consult the following:   - [Movie Toolbox: Editing](https://developer.apple.com/documentation/quicktime/qtdevdocs/RM/rmMTEditing.htm) - [QuickTime File Format: June 2000](https://developer.apple.com/documentation/quicktime/qtdevdocs/PDF/QTFileFormat.pdf)  ---  [Sep 22 2000] |

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
