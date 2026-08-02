---
title: MovieAudioExtraction - Extracting all available audio samples
apple_id: DTS10003965
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2006-07-18'
source_url: https://developer.apple.com/library/archive/qa/qa1481/_index.html
archived_at: '2026-07-18T02:31:23.016522Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1481

# MovieAudioExtraction - Extracting all available audio samples

## Q:  MovieAudioExtraction seems to be missing a small number of audio samples from the end of some audio files. How can I guarantee that all audio samples are returned during extraction?

A: QuickTime represents the duration of a movie as a duple of `TimeValue` / `TimeScale`. This is the length of a `Movie` or `Media` structure in terms of time units. Each chunk of media referenced by a track has its own time scale determined by its sample rate and QuickTime will automatically translate between the `Movie` time scale and the time scales of its various `Media`.

The default time scale of a `Movie` imported from an audio files happens to be 600 (actually, this is the default time scale for all newly created `Movies` in QuickTime). Small rounding errors may occur when calculating durations as you lose the granularity from larger time scale value.

As an example let's take an AIFF audio file that has exactly 1024 samples (mono, 16 bit, 8000Hz sampling rate).

When this file is imported by QuickTime a new `Movie` is created with a `TimeScale` of 600 containing a single track. This track contains a sound media with a `TimeScale` of 8000. The media duration is represented as 1024/8000 (number of samples / sample rate) and after time scale conversion the `Movie` duration is represented as 76/600.

Converting back to 8000Hz (the media time scale) yields 1013.3333 samples. This leaves a media duration of 1014 samples, notably a few samples short of the original 1024.

If the `Movie` duration were 77/600, then it would work out to 1026.6666 samples, but that would be too long (since this is more data than is contained in the media). QuickTime doesn't do that, therefore downward rounding happens during time scale conversion which results in a `Movie` duration of 76 time units.

It is important to note that all the media is still available and accessible, the issue involves the track edit created by QuickTime during the import process. Because we know this, we can remove the original edit, change the `Movie` time scale and create a more accurate edit specifically for the extraction process.

__Listing 1__  Example of how to correct the edit.

```
// The FixSoundTrackEdit function will ONLY perform this fix for a Movie if it has:
// - single sound track
// - single edit that spans the entire media duration
// - edit rate of 1
// - converted Movie and Media durations indicate truncated media
// If any of these checks fail, the function will not perform any corrections and will return 0.
// If the function performs the fix it will return 1.
// If any other error occurs, the appropriate error code will be returned.
//
// We delete the edit with the incorrect duration by calling DeleteTrackSegment,
// change the Movie TimeScale to that of the Media using SetMovieTimeScale,
// then create a new edit by calling InsertMediaIntoTrack.

OSStatus FixSoundTrackEdit(Movie inMovie)
{
    Track theTrack;
    Media theMedia;
    SInt32 numberOfTracks;
    TimeValue editTrackStart = 0, editTrackDuration = 0;
    TimeValue editMediaTime;
    TimeValue testMovieDuration, testMediaDuration;
    Fixed editRate;

    OSStatus status = false;

    if (NULL == inMovie) { status = missingRequiredParameterErr; goto bail; }

    /*** Perform sanity checks to make sure the application of the fix is not unintentional ***/

    // make sure there's only a single track
    numberOfTracks = GetMovieTrackCount(inMovie);
    if (numberOfTracks != 1) goto bail;

    // must be an enabled sound track
    theTrack = GetMovieIndTrackType(inMovie, 1, SoundMediaType, movieTrackMediaType | movieTrackEnabledOnly);
    if (NULL == theTrack) goto bail;

    // get the media
    theMedia = GetTrackMedia(theTrack);
    if (NULL == theMedia) goto bail;

    // check the edits
    GetTrackNextInterestingTime(theTrack, nextTimeTrackEdit | nextTimeEdgeOK, editTrackStart, fixed1,
                                &editTrackStart, &editTrackDuration);
    status = GetMoviesError();
    if (status) goto bail;

    // check for an empty edit
    editMediaTime = TrackTimeToMediaTime(editTrackStart, theTrack);
    if (editMediaTime == -1) goto bail;

    // check that the edit rate is 1
    editRate = GetTrackEditRate(theTrack, editTrackStart);
    if (editRate != fixed1) goto bail;

    // check for another edit - we should only have a single edit
    GetTrackNextInterestingTime(theTrack, nextTimeTrackEdit, editTrackStart + editTrackDuration, fixed1,
                                &editTrackStart, &editTrackDuration);
    status = GetMoviesError();
    if (status) goto bail;

    if (editTrackStart != -1) goto bail;

    // check the converted durations

    // don't apply the fix if the Movie duration in media time scale
    // is the same as the media duration -- no truncation has occurred
    testMovieDuration = ceil(((Float64)GetTrackDuration(theTrack) / (Float64)GetMovieTimeScale(inMovie))
                          * GetMediaTimeScale(theMedia));
    testMediaDuration = GetMediaDuration(theMedia);
    if (testMediaDuration == testMovieDuration) goto bail;

    // don't apply the fix if the Media duration in movie time scale
    // is not the same as the Movie duration -- no truncation has occurred
    testMovieDuration = GetMovieDuration(inMovie);
    testMediaDuration = ((Float64)GetMediaDuration(theMedia) / (Float64)GetMediaTimeScale(theMedia))
                          * GetMovieTimeScale(inMovie);
    if (testMovieDuration != testMediaDuration) goto bail;

    /*** Perform the fix ***/

    // if we made it this far we know some truncation has occurred
    // most likely during an import operation

    // delete the track edit
    // this will not remove the media, but will remove the edits that reference it
    status = DeleteTrackSegment(theTrack, 0, GetTrackDuration(theTrack));
    if (status) goto bail;

    // change the movie time scale to the media time scale
    SetMovieTimeScale(inMovie, GetMediaTimeScale(theMedia));
    status = GetMoviesError();
    if (status) goto bail;

    // create a new edit
    status = InsertMediaIntoTrack(theTrack, 0, 0, GetMediaDuration(theMedia), fixed1);
    if (status) goto bail;

    status = true;

bail:

    return status;
}
```


- [Technical Q&A QTMCC17, 'Track Editing'](https://developer.apple.com/qa/qtmcc/qtmcc17.html)
- [Technical Q&A QA1110, 'QuickTime Media Editing'](https://developer.apple.com/qa/qa2001/qa1110.html)
- [Movie Time - Time Coordinate System](https://developer.apple.com/quicktime/qttutorial/movies.html#MovieTime)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-07-18 | New document that describes how to correct for MovieAudioExtraction missing some audio samples at the end of audio files. |

