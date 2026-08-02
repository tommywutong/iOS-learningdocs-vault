---
title: MovieAudioExtraction - Ensure a Movie is fully loaded before starting an extraction
  session
apple_id: DTS10003914
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2006-03-29'
source_url: https://developer.apple.com/library/archive/qa/qa1469/_index.html
archived_at: '2026-07-18T02:30:57.042543Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1469

# MovieAudioExtraction - Ensure a Movie is fully loaded before starting an extraction session

## Q:  I'm using the QuickTime MovieAudioExtraction APIs to extract audio from MP3 files opened with QTKit. This seems to work for some MP3 files but for others I get the first few minutes of audio extracted then silence. What's going on?

A: I'm using the QuickTime MovieAudioExtraction APIs to extract audio from MP3 files opened with QTKit. This seems to work for some MP3 files but for others I get the first few minutes of audio extracted then silence. What's going on?

Before any audio can be extracted from a QuickTime Movie, you must ensure that the Movie's load state is `kMovieLoadStateComplete`.

If QuickTime detects a VBR header in an MP3 file, or finds variable packet sizes in the first second's worth of data, it will scan the entire file in order to create an accurate sample table. The larger the MP3 file, the longer QuickTime will take to complete the scan. If your application is using QTKit, this import scan operation is happening asynchronously and the Movie's load state will not be set to `kMovieLoadStateComplete` until the entire sample table has been built.

While you may be able to play the Movie once the load state has transitioned to `kMovieLoadStatePlayable`, other operations such as saving or conversion will not be possible or may yield unexpected results.

Since the release of QuickTime 4.1 the asynchronous Movie loading model has been the preferred import method for QuickTime. Instead of a fully formed Movie being immediately available and playable, the returned Movie will transition though a number of different load states depending on the type of import operation being performed.

A Movie may transition from `kMovieLoadStateLoading` directly to `kMovieLoadStateComplete` while other times (over a slow network connection for example) may explicitly transition through each load state over time.


```
enum {   kMovieLoadStateError          = -1L,   kMovieLoadStateLoading        = 1000,   kMovieLoadStateLoaded         = 2000,   kMovieLoadStatePlayable       = 10000,   kMovieLoadStatePlaythroughOK  = 20000,   kMovieLoadStateComplete       = 100000L };
```

Instead of applications being blocked waiting on the availability of a fully formed Movie (`kMovieLoadStateComplete`), they can use the time during media loading to perform other operations creating a more responsive user experience.

Asynchronous Movie Loading is an opt-in behavior. Applications choose to opt-in by setting the `newMovieAsyncOK` flag when calling any of the `NewMovieFrom...` APIs. One of the responsibilities of applications setting the `newMovieAsyncOK` flag is to preflight operations by checking the load state and to prevent certain operations if the load state has not passed a specific threshold. For example, prevent playing if the movie load state is not at least `kMovieLoadStatePlayable` and prevent saving or exporting if the movie load state is not `kMovieLoadStateComplete`.

By default, the higher level QTKit framework opts-in to the asynchronous Movie loading model on behalf of its client and therefore takes on the responsibility of preflighting saving, flattening, and conversion operations by checking the Movie's load state when `writeToFile:withAttributes` is invoked.

When extending QTKit through direct use of Movie Toolbox APIs, it is your responsibility to do likewise. Audio extraction is a conversion operation and as such cannot be performed before a Movie returns the `kMovieLoadStateComplete` load state.

__Listing 1__  Checking load state with QTKit.

```
long movieLoadState = [[myQTMovie attributeForKey:QTMovieLoadStateAttribute] longValue];
```


__Listing 2__  Checking load state with the Movie Toolbox.

```
long movieLoadState = GetMovieLoadState(myMovie);
```


__Listing 3__  Installing a QTKit notification for Movie load state changes.

```
// install a QTMovieLoadStateDidChangeNotification notification -(void)installMovieLoadStateDidChangeNotification {     NSNotificationCenter *nc = [NSNotificationCenter defaultCenter];      [nc addObserver:self selector:@selector(movieLoadStateDidChange:)              name:@"QTMovieLoadStateDidChangeNotification" object:nil]; }  // movieLoadStateDidChange is called for QTMovieLoadStateDidChangeNotification notifications. - (void) movieLoadStateDidChange:(NSNotification *)notification {     movieLoadState = [[myQTMovie attributeForKey:QTMovieLoadStateAttribute] longValue]; }
```

It is possible to avoid asynchronous loading when using QTKit by invoking `initWithAttributes:error:` and passing in an `NSDictionary` that has the `QTMovieOpenAsyncOKAttribute` attribute set to `NO`. You may want to do this if for example, you were writing a simple command line tool that exports audio immediately after a movie file is imported and you are not concerned about user interface or waiting for QuickTime to synchronously import the file.

- [Introduction of Asynchronous Movie Loading](https://developer.apple.com/documentation/QuickTime/REF/QT41_HTML/QT41WhatsNew-81.html)
- [Monitoring the Load State](https://developer.apple.com/documentation/QuickTime/RM/MovieBasics/MTOpenPlayMovies/5openplaymovies_loadstate/chapter_1000_section_1.html)
- [QTKit initWithAttributes:error: method.](https://developer.apple.com/documentation/QuickTime/Reference/QTCocoaObjCKit/Classes/QTMovie.html#//apple_ref/occ/instm/QTMovie/initWithAttributes:error:)
- [GetMovieLoadState](https://developer.apple.com/documentation/QuickTime/APIREF/getmovieloadstate.htm)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-03-29 | New document that describes the importance of making sure a Movie is fully loaded before extracting audio. |

