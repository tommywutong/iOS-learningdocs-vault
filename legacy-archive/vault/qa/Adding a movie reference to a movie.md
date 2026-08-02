---
title: Adding a movie reference to a movie
apple_id: DTS10003400
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2004-09-16'
source_url: https://developer.apple.com/library/archive/qa/qa1376/_index.html
archived_at: '2026-07-18T02:30:27.769971Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1376

# Adding a movie reference to a movie

## Q:  I'd like to add a reference for a movie to another movie, for example to "merge" two movies together so one will playback right after the other. Is this done with data references? Or do I use an alias approach? I'm confused. Please explain.

A: The easiest way to do this is with the Movie Toolbox Editing routine `InsertMovieSegment`. This function copies part of one movie to another. Simply call this function and specify which part of the destination movie you'd like copied to the source movie.

For example, to add a reference to some source movie to a destination movie use `InsertMovieSegment` as shown in the code snippet below:

__Listing 1__  Adding a movie reference using `InsertMovieSegment`.

```
void addMovieReference(Movie destMovie, Movie sourceMovie)
{
  TimeValue srcMovieDuration, destMovieDuration;
  OSErr err = noErr;

  srcMovieDuration = GetMovieDuration(sourceMovie);
  destMovieDuration = GetMovieDuration(destMovie);

   // add to destMovie a reference to sourceMovie
  err = InsertMovieSegment(
          sourceMovie,             // source movie
          destMovie,               // destination movie for the insert
          0,                       // insert from beginning of source movie
          srcMovieDuration,        // duration of source movie segment to insert
          destMovieDuration        // where to insert the source segment into the dest.
        );

  .
  .
  .
}
```

Also, call CopyMovieSettings if you wish to copy movie settings such as preferred rate and volume, and so on, from the source movie to the destination movie:

__Listing 2__  Using CopyMovieSettings to copy movie attributes.

```
err = CopyMovieSettings (srcMovie,
                         destMovie );
```

Note that some or all of the media of the source movie may be copied to the destination if one or more calls to `BeginMediaEdits` precede the call to `InsertMovieSegment`. For our purposes, we make certain that no such calls are made. In this case, only references to the actual media in the source movie to be stored in the destination movie will be copied. The actual media itself is not copied.

Finally, don't forget to call `UpdateMovieResource` (or `UpdateMovieInStorage` if the movie was created with `CreateMovieStorage`) for the destination movie to save your changes.

Adding a reference to a movie can also be accomplished using data references. However, this is a more complicated approach, and in this case we can get the same result using `InsertMovieSegment`.

For an example of how to create a reference to a movie using data references, see the [Sample Code 'qtdataref'](https://developer.apple.com/samplecode/qtdataref/index.html).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-09-16 | New document that demonstrates how to add a reference for a movie to another movie |

