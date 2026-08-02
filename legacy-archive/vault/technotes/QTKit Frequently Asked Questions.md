---
title: QTKit Frequently Asked Questions
apple_id: DTS10003755
resource_type: Technical Note
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QTKit
published: '2008-04-24'
source_url: https://developer.apple.com/library/archive/technotes/tn2138/_index.html
archived_at: '2026-07-26T19:54:08.530848Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2138

# QTKit Frequently Asked Questions

This Technote covers the following frequently asked QTKit questions.

[Getting a movie frame image](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzvguwugsbrfvjukq2ujfhu4mi)[Nothing happens when I try to play a sound file](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzvguwugsbrfvjukq2ujfhu4mq)[How do I add a QTTrack to a QTMovie?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzvguwugsbrfvjukq2ujfhu4my)[When does the QTMovieTimeDidChangeNotification notification fire?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzvguwugsbrfvjukq2ujfhu4na)[Creating an empty movie and adding images to it](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzvguwugsbrfvjukq2ujfhu4ni)[Exporting a QTMovie to a new file on disk](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzvguwugsbrfvjukq2ujfhu4nq)[Getting a list of QuickTime supported file types or extensions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzvguwugsbrfvjukq2ujfhu4ny)[How does the QTMakeTimeFromString/QTTimeFromString function work?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzvguwugsbrfvjukq2ujfhu4oa)[QTMovie object not fully-formed?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzvguwugsbrfvjukq2ujfhu4oi)[Finding the last movie frame](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzvguwugsbrfvjukq2ujfhu4mjq)[Using QTMovie objects on background threads?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzvguwugsbrfvjukq2ujfhu4mjr)[Subclassing QTMovieView](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzvguwugsbrfvjukq2ujfhu4mjs)[QTMovie unexpectedly draws to upper left portion of screen?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzvguwugsbrfvjukq2ujfhu4mjt)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzvguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Getting a movie frame image

Q: I'd like to be able to get an image for a movie frame at a specific time. Is this possible?

A: Yes. Use the `frameImageAtTime:` method, which was introduced in Mac OS X 10.3:

```objc
- (NSImage *)frameImageAtTime:(QTTime)time;
```

The `QTMovie` `frameImageAtTime:` method was also updated in Mac OS X 10.5 to accept a dictionary of attributes.

```objc
- (void *)frameImageAtTime:(QTTime)time                 withAttributes:(NSDictionary *)attributes                          error:(NSError **)errorPtr;
```

The dictionary of attributes may contain the following keys:

```
 QTMovieFrameImageSize     QTMovieFrameImageType     QTMovieFrameImageRepresentationsType     QTMovieFrameImageOpenGLContext     QTMovieFrameImagePixelFormat     QTMovieFrameImageDeinterlaceFields     QTMovieFrameImageHighQuality     QTMovieFrameImageSingleField
```

See `QTMovie`.h for additional information about these attributes.

For the `QTMovieFrameImageType` attribute the possible values are as follows:

```
 QTMovieFrameImageTypeNSImage     QTMovieFrameImageTypeCGImageRef     QTMovieFrameImageTypeCIImage     QTMovieFrameImageTypeCVPixelBufferRef     QTMovieFrameImageTypeCVOpenGLTextureRef
```

For example, here's how to ask for a particular image type (`NSImage` is the default, and the default representation is `NSBitmapImageRep`):

__Listing 1__  How to get a CGImage for a movie frame at a given time.

```
 NSDictionary *dict = [NSDictionary                        dictionaryWithObject:QTMovieFrameImageTypeCGImageRef                                      forKey:QTMovieFrameImageType];     QTTime time = [movie currentTime];      CGImageRef theImage = (CGImageRef)[movie frameImageAtTime:time                                     withAttributes:dict error:NULL];
```

See the [QTKitMovieFrameImage sample code](https://developer.apple.com/samplecode/QTKitMovieFrameImage/index.html) for a complete example.

[Back to Top](#)

## Nothing happens when I try to play a sound file

Q: I'm using QTKit to open and play a sound file, but when I do this nothing happens. I hear no sound at all. But if I set my `QTMovie` to a `QTMovieView` using the `setMovie:` method it works just fine. Here's my code. What am I doing wrong?

```
 QTMovie *aMovie;     QTMovieView *aMovieView;      aMovie = [QTMovie movieWithFile:s error:nil];     [aMovie setVolume: volumeVal];  // [aMovieView setMovie:aMovie]; // doing this makes it work!     [aMovie play];
```

A: The following line of code creates an autoreleased (`QTMovie`) object:

```
 aMovie = [QTMovie movieWithFile:s error:nil];
```

Once you re-enter the run loop the object is disposed of, which would explain why nothing happens when you try to use the object again.

The reason your code works when you assign the `QTMovie` to a `QTMovieView` is the `QTMovieView` retains the `QTMovie` object, and the retained `QTMovie` gets idled through the normal idling mechanism built into `QTMovie` - hence the movie plays.

Instead, create the `QTMovie` object using the `alloc:` method so it is not placed in the autorelease pool. Then simply release the object when you are done with it. Here's how it looks:

```
 QTMovie* aMovie;     aMovie = [[QTMovie alloc] initWithFile:s error:nil];     [aMovie setVolume: volumeVal];     [aMovie play];   ... /* do stuff */      [aMovie release]; // release object when done
```

Alternately, you could use the `movieWithFile:` method as was done in the original code snippet, but then immediately retain the object:

```
 QTMovie* aMovie;     aMovie = [QTMovie movieWithFile:s error:nil];     [aMovie retain]; // retain the object     [aMovie setVolume: volumeVal];     [aMovie play];  ... /* do stuff */      [aMovie release]; // release object when done
```

[Back to Top](#)

## How do I add a QTTrack to a QTMovie?

Q: How do I to add a `QTTrack` to a `QTMovie`? A quick check of the QTKit reference documentation doesn't reveal an easy way to do this.

A: There are currently no QTKit methods for adding tracks to a `QTMovie` object. However, you can use the standard QuickTime APIs to add tracks to the Movie associated with a `QTMovie` (namely, `NewMovieTrack`, `NewTrackMedia`, and so on). This should work fine.

Here's a quick outline of what you need to do:

- create a `QTMovie`
- get the QuickTime movie associated with the `QTMovie`
- create a new track with `NewMovieTrack`
- use that track to initialize a `QTTrack`

Here's a code snippet showing how it's done.

__Listing 2__  Adding a `QTTrack` to a `QTMovie`

```objc
@implementation QTMovie (QTMovieExtensions)  -(BOOL)isEditable {     NSDictionary *movieDict = [self movieAttributes];      NSNumber *isEditable = [movieDict objectForKey:QTMovieEditableAttribute];      return [isEditable boolValue]; }  - (QTTrack *) addVideoTrackWithSize:(NSSize) aSize {     QTTrack *newTrack = nil;      require( [self isEditable] == YES, NOT_EDITABLE);      Track videoTrack = NewMovieTrack ([self quickTimeMovie],                                      FixRatio (aSize.width, 1),                                      FixRatio(aSize.height, 1),                                      kFullVolume);     require (GetMoviesError() == noErr, NEWTRACK_ERROR);      Handle dataRef = NULL;     Handle hMovieData = NewHandle (0);     require (hMovieData != nil, NEWHANDLE_ERR);     OSErr osErr = PtrToHand (&hMovieData, &dataRef, sizeof(Handle));     require (osErr == noErr, PTRTOHAND_ERROR);      Media videoMedia = NewTrackMedia (videoTrack,                                      VideoMediaType,                                      [[self timeScale] longValue],                                      dataRef,                                      HandleDataHandlerSubType);     require (GetMoviesError() == noErr, TRACKMEDIA_ERROR);      QTTime movieDuration = [self duration];     InsertMediaIntoTrack (videoTrack, 0, 0, movieDuration.timeValue, fixed1);      require (GetMoviesError() == noErr, INSERTMEDIA_ERROR);      newTrack = [QTTrack trackWithQuickTimeTrack: videoTrack error:nil];      return newTrack;  INSERTMEDIA_ERROR:     DisposeTrackMedia(videoMedia); TRACKMEDIA_ERROR: PTRTOHAND_ERROR:     DisposeHandle(hMovieData); NEWHANDLE_ERR:     DisposeMovieTrack (videoTrack); NEWTRACK_ERROR: NOT_EDITABLE:      return nil; }   @end
```

[Back to Top](#)

## When does the QTMovieTimeDidChangeNotification notification fire?

Q: When does the `QTMovieTimeDidChangeNotification` notification fire? I had expected it to fire when the timecode of a movie changed, such as when a new frame is being displayed but that doesn't seem to be the case. I'd like to be able to display the movie's current time as it is playing.

A: The `QTMovieTimeDidChangeNotification` is fired whenever the movie time changes to a time \*\*\*other than what it would be during normal playback\*\*\*. So it's not fired every frame.

Some examples are: the user clicks in the movie controller bar to change the movie time, or a wired action changes the movie time.

Instead, you might consider using an `NSTimer`, or even a Movie Controller action filter function (see the Movie Toolbox function `MCSetActionFilterWithRefCon`).

[Back to Top](#)

## Creating an empty movie and adding images to it

Q: I'd like to create a 10-second long `QTMovie` from a single `NSImage` and save it as a QuickTime movie (.mov) file. However, there doesn't seem to be any provision in QTKit for creating an "empty" movie. Is this true?

A: QuickTime 7.2.1 provides a new method `initToWritableFile:` to create an "empty" `QTMovie` (in QuickTime terminology, a movie with a writable data reference):

```objc
- (id)initToWritableFile:(NSString *)filename error:(NSError **)errorPtr;
```

For versions of QuickTime prior to 7.2.1, you can use the native QuickTime API `CreateMovieStorage` to create a QuickTime movie with a writable data reference, then use the QTKit `movieWithQuickTimeMovie:` method to instantiate a `QTMovie` from this QuickTime movie.

The [Sample Code 'QTKitCreateMovie'](https://developer.apple.com/samplecode/QTKitCreateMovie/index.html) demonstrates both of these techniques.

You can also initialize a `QTMovie` directly from your `NSImage` and then export it as you are currently doing. Here's a code snippet showing this technique:

__Listing 3__  Initializing a `QTMovie` from an `NSImage`.

```
 // instantiate an NSImage object for our image         NSImage *image = [NSImage imageNamed:@"some_image"];         if (image)          {             // Returns a data object containing TIFF for all representations             NSData *data = [image TIFFRepresentation];             QTDataReference *dataRef = [QTDataReference dataReferenceWithReferenceToData:data                                                                name:@"some_image.tiff" MIMEType:nil];             // make a QTMovie from the NSImage             QTMovie *movie = [QTMovie movieWithDataReference:dataRef error:nil];              // make the movie editable             [movie setAttribute:[NSNumber numberWithBool:YES] forKey:QTMovieEditableAttribute];              // set the duration to 10 seconds             QTTimeRange range = QTMakeTimeRange(QTZeroTime, [movie duration]);             [movie scaleSegment:range newDuration:QTMakeTime(10, 1)];              // export as a 3GPP file; or use your existing export code here....              // setup the proper export attributes in a dictionary             NSDictionary *dict= [NSDictionary dictionaryWithObjectsAndKeys:                 [NSNumber numberWithBool:YES], QTMovieExport,                 [NSNumber numberWithLong:kQTFileType3GPP], QTMovieExportType, nil];              // write the QTMovie to a 3GPP movie file on disk             [movie writeToFile:@"/tmp/my3GP.mov" withAttributes:dict];         }
```

[Back to Top](#)

## Exporting a QTMovie to a new file on disk

Q: I have a `QTMovie` that I'd like to write to my hard drive. I'm using the `writeToFile:` method to do this, and the file is created on my disk, but the movie shows a blank (white) screen when I play it.

Here is my code :

```
// My movie QTMovie *movie = [qtPlayer movie];  // The codec dictionary NSDictionary *codecDictionary =      [NSDictionary dictionaryWithObjectsAndKeys: @"jpeg",     QTAddImageCodecType, [NSNumber numberWithInt: codecNormalQuality],     QTAddImageCodecQuality, nil];  // The moviePath is also correct [movie writeToFile: moviePath withAttributes: codecDictionary];
```

A: The keys `QTAddImageCodecType` and `QTAddImageCodecQuality` are intended for use in the dictionary passed to the -[`QTMovie` `addImage:forDuration:withAttributes:`] method.

With the `writeToFile:withAttributes:` method you need to instead use the following keys (these taken from the `QTMovie`.h interface file):

```
 // writeToFile: attributes dictionary keys QTKIT_EXTERN NSString *QTMovieExport          AVAILABLE_MAC_OS_X_VERSION_10_4_AND_LATER; // NSNumber (BOOL) QTKIT_EXTERN NSString *QTMovieExportType          AVAILABLE_MAC_OS_X_VERSION_10_4_AND_LATER; // NSNumber (long) QTKIT_EXTERN NSString *QTMovieFlatten          AVAILABLE_MAC_OS_X_VERSION_10_4_AND_LATER; // NSNumber (BOOL) QTKIT_EXTERN NSString *QTMovieExportSettings          AVAILABLE_MAC_OS_X_VERSION_10_4_AND_LATER; // NSData (QTAtomContainer) QTKIT_EXTERN NSString *QTMovieExportManufacturer          AVAILABLE_MAC_OS_X_VERSION_10_4_AND_LATER; // NSNumber (long)
```

The following samples shows how to perform an export operation: [Sample Code 'QTKitCreateMovie'](https://developer.apple.com/samplecode/QTKitCreateMovie/index.html), [Sample Code 'QTKitProgressTester'](https://developer.apple.com/samplecode/QTKitProgressTester/index.html) and [Sample Code 'QTKitCommandLine'](https://developer.apple.com/samplecode/QTKitCommandLine/index.html) .

[Back to Top](#)

## Getting a list of QuickTime supported file types or extensions

Q: How can I get a list of file types or extensions that QuickTime can handle?

A: See the `QTMovie` `movieFileTypes:` class method. It should do exactly what you want. Just pass the output of this method to the `NSSavePanel` `setAllowedFileTypes:` method. Check the [Sample Code 'QTKitAdvancedDocument'](https://developer.apple.com/samplecode/QTKitAdvancedDocument/index.html) to see how this is done.

This will work fine, and it allows you to selectively include still image types, translatable types, and types that require "aggressive" importers (like text and html files) by adjusting the set of flags passed to the `movieFileTypes:` method.

There is however, an even easier technique, and that is to use the `canInitWithFile:` method:. Here's a code snippet showing how it's done:

```objc
- (BOOL)panel:(id)sender shouldShowFilename:(NSString *)filename {     BOOL isDir = NO;      [[NSFileManager defaultManager] fileExistsAtPath:filename isDirectory:&isDir];      return isDir ? YES : [QTMovie canInitWithFile:filename]; }
```

This technique is basically equivalent to passing in the array of file types returned by the `movieFileTypes:` method with the `QTIncludeAllTypes` flag.

[Back to Top](#)

## How does the QTMakeTimeFromString/QTTimeFromString function work?

Q: How does the `QTMakeTimeFromString`/`QTTimeFromString` function work?

The current documentation states this function is called `QTMakeTimeFromString`, however if look in the header file QTTime.h, you won't find that function. It is actually called `QTTimeFromString`. Here is the code I am using:

```
QTTime oldTime = [qtMovie currentTime]; QTTime incTime = QTTimeFromString( @"00:02:00.00" ); QTTime newTime = QTTimeIncrement( oldTime, incTime );  NSLog( QTStringFromTime( oldTime ) ); NSLog( QTStringFromTime( incTime ) ); NSLog( QTStringFromTime( newtime ) );
```

I get the following results:

```
    0:00:00:00.00/48000     0:00:00:00.00/1000000     0:00:00:00.00/1000000
```

I have also tried setting the time string to `@"0:00:02:00.00", @"0:0:2:0.0",` and other variations. No luck.

What am I doing wrong?

A: You'll notice the following comment in QTTime.h:

```
// ,,,dd:hh:mm:ss.ff/ts
```

which translates into:

```
days:hours:minutes:seconds:frames/timescale
```

So you should try a string like:

```
QTTime incTime = QTTimeFromString( @"00:00:02:00.00/600" ); NSLog( QTStringFromTime( incTime ) );
```

which should work fine. The current documentation is incorrect.

[Back to Top](#)

## QTMovie object not fully-formed?

Q:

I'm able to successfully instantiate a `QTMovie` object using the `movieWithFile:` method in my application, but right after I do this I query the object and notice it doesn't contain any tracks, and only very few attributes. And if I try to get the QTMovieNaturalSizeAttribute attribute it reports a size of 0,0.

Is there something else I must do to properly instantiate a `QTMovie` object?

A:

If you query the `QTMovie` object immediately after initialization with the `movieWithFile:` method the `QTMovie` object may not be fully-formed -- in the sense that you can ask for its attributes or perform certain operations on it like calling the `writeToFile:` method and others. This is because all `QTMovie` initialization methods occur aysnchronously by default.

To prevent this, you can make the initialization call synchronously. To do this, you need to use the `initWithAttributes:` method and make sure you set the `QTMovieOpenAsyncOKAttribute` to NO. Here's a code snippet:

```
NSSize movieSize; NSDictionary *attrs = [NSDictionary dictionaryWithObjectsAndKeys:         (id)url, QTMovieURLAttribute,         [NSNumber numberWithBool:NO], QTMovieOpenAsyncOKAttribute,         nil]; QTMovie *movie = [QTMovie movieWithAttributes:attrs error:nil]; movieSize = [[movie attributeForKey:QTMovieNaturalSizeAttribute] sizeValue];  [movie play]; ...
```

The other option is to install a notification handler for the `QTMovieLoadStateDidChangeNotification` notification, and don't query the `QTMovie` object for any attributes until the load state is at least `QTMovieLoadStateLoaded`. Here's a code snippet:

```
// install a notification handler for QTMovieLoadStateDidChangeNotification QTMovie *movie = [QTMovie movieWithURL:url error:nil]; [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(loadStateChanged:) name:QTMovieLoadStateDidChangeNotification object:movie]; . . . // check for load state changes -(void)loadStateChanged:(QTMovie *)movie {     long loadState = [[movie attributeForKey:QTMovieLoadStateAttribute] longValue];     if (loadState >= QTMovieLoadStatePlayable)     {         // the movie has loaded enough media data to begin playing         [movie play];     }     else if (loadState >= QTMovieLoadStateLoaded)     {         // the movie atom has loaded; it's safe to query movie properties         NSSize movieSize;         movieSize = [[movie attributeForKey:QTMovieNaturalSizeAttribute] sizeValue];         /* ... */     }     else if (loadState == -1)     {         /* error occurred; handle it */     } }
```

[Back to Top](#)

## Finding the last movie frame

Q:

How can I determine when I've arrived at the last frame of a movie?

I tried using the `stepForward:` method, but it does not report back whether it actually succeeded or not. Will the `QTMovieDidEndNotification` give me this information?

A:

The `QTMovieDidEndNotification` is not issued when stepping to the end of a movie.

One alternative would be to define your own custom `QTMovie` category with new methods for these operations as shown below (notice we have prepended each method with the prefix "rt_" so these do not conflict with any current or future QTKit methods.):

```objc
@implementation QTMovie (MyQTMovieExtension)  - (BOOL)rt_stepForward {   QTTime curTime, newTime;    curTime = [self currentTime];   [self stepForward];   newTime = [self currentTime];    return (QTTimeCompare(curTime, newTime) != NSOrderedSame); }  - (BOOL)rt_stepBackward {   QTTime curTime, newTime;    curTime = [self currentTime];   [self stepBackward];   newTime = [self currentTime];    return (QTTimeCompare(curTime, newTime) != NSOrderedSame); }  @end
```

[Back to Top](#)

## Using QTMovie objects on background threads?

Q:

I just read the article [TN2125: Thread-safe programming in QuickTime](https://developer.apple.com/technotes/tn/tn2125.html) , but it doesn't say anything about QTKit. How do I safely use `QTMovie` objects on a background thread?

A:

Observe the following guidelines when working with `QTMovie` objects on background threads:

(1) allocate all `QTMovie` objects on the main thread.

The reason for this is quite simple: a `QTMovie` is always associated with a movie controller component instance, and currently no movie controller components are thread-safe. While a non-nil `QTMovie` can indeed be created on a background thread, the associated movie controller will always be NULL. This by itself is not fatal; many operations can be performed on a `QTMovie` object that has been initialized on a background thread. But certain operations will not work correctly, including most all of the notifications and even asynchronous movie-loading. That's why allocating a `QTMovie` on a background thread is not advised.

(2) if you want to operate on a `QTMovie` on a different thread, detach it from the current thread using the Movie Toolbox C API `DetachMovieFromCurrentThread` (on the QuickTime movie associated with that `QTMovie` as gotten with the `quickTimeMovie:` method); then attach it to the different thread using `AttachMovieToCurrentThread`. Also, to workaround a bug in QTKit we recommend you call the private method `setIdling:` here to make sure the movie is not tasked on a background thread.

(3) call `EnterMoviesOnThread` before you make any other QuickTime or QTKit calls on a secondary thread.

(4) call `ExitMoviesOnThread` before exiting a thread you have made QuickTIme calls on.

(5) be prepared to handle errors from any of those calls; some movies cannot be moved to secondary threads (this is codec specific).

QTKit does not do any of this automatically for you, but we are working on some new APIs that will perhaps make this process easier (or at least more Cocoa-like).

Here's a short code snippet showing how to perform a movie export on a background thread:

```objc
- (void)doExportOnThread:(QTMovie *)movie {     NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];      EnterMoviesOnThread(0);     AttachMovieToCurrentThread([movie quickTimeMovie]);      // To workaround a bug in QTKit we need to call the private     // method setIdling: to make sure the movie is not tasked on      // a background thread     if ([movie respondsToSelector:@selector(setIdling:)])         [movie setIdling:NO];      // do export     [movie writeToFile:....];      DetachMovieFromCurrentThread([movie quickTimeMovie]);     ExitMoviesOnThread();      [pool release]; }
```

[Back to Top](#)

## Subclassing QTMovieView

Q:

I've tried overriding the `mouseDown:` method of the `QTMovieView` class without success. Please show me how to properly override `QTMovieView`.

A:

This is a known issue with `QTMovieView` in QTKit 1.0 that has been subsequently fixed in QuickTime 7.0.4. Make sure you have QuickTime 7.0.4 installed.

[Back to Top](#)

## QTMovie unexpectedly draws to upper left portion of screen?

Q:

If I create a movie with the Movie Toolbox C API `CreateMovieStorage`, add frames to it, then instantiate a `QTMovie` from this QuickTime movie it will unexpectedly draw to the upper left portion of the screen. What's going on?

A:

You have run into an issue that may arise when mixing the QuickTime Carbon APIs and QTKit. When creating a movie using the native Carbon QuickTime APIs you must always have a valid port set beforehand so the movie knows where to draw. Here's a Q&A which describes this:

[QA1345: The QuickTime Movie Toolbox requires a valid graphics port for all movies.](https://developer.apple.com/qa/qa2001/qa1345.html)

What's happening in your case is at the time you call `CreateMovieStorage` the active port is set to the screen, therefore your movie will draw to the screen unless otherwise specified (for example, by making a call to `SetMovieGWorld` for the movie to specify a different port).

To avoid this you can:

1) Use any of the available QTKit methods to open the movie file, such as `movieWithFile:`. QTKit ensures that any movie file you open using its APIs will have a valid GWorld.

2) Create a "dummy" GWorld just before creating the new movie with `CreateMovieStorage`. Here's how:

```objc
-(void)QTKitMovieExample:(NSString *)inMoviePath {     GWorldPtr gworld = NULL;     Rect rect = {0, 0, 1, 1};        // create a "dummy" gworld for our movie     QDErr qtErr = NewGWorld(&gworld, 32, &rect, NULL, NULL, 0);     NSAssert( qtErr == 0, @"NewGWorld failed");      OSErr   err            = noErr;     Handle  dataRefH       = nil;     OSType  dataRefType;      // create a file data reference for our movie     err = QTNewDataReferenceFromFullPathCFString((CFStringRef)inMoviePath,                                                   kQTNativeDefaultPathStyle,                                                   0,                                                   &dataRefH,                                                   &dataRefType);     NSAssert( err == noErr, @"QTNewDataReferenceFromFullPathCFString failed");      // create a QuickTime movie from our movie file data reference     Movie   nativeMovie = nil;     DataHandler outDataHandlerRef;     CreateMovieStorage (dataRefH,                         dataRefType,                         'TVOD',                         smSystemScript,                         newMovieActive,                          &outDataHandlerRef,                         &nativeMovie);     err = GetMoviesError();     NSAssert( err == noErr, @"CreateMovieStorage failed");        // set the gworld for the native QuickTime movie     SetMovieGWorld(nativeMovie, gworld, NULL);      // instantiate a QTKit QTMovie from our QuickTime movie     QTMovie *qtMovie = [QTMovie movieWithQuickTimeMovie:nativeMovie disposeWhenDone:NO error:nil];     NSAssert( qtMovie != nil, @"movieWithQuickTimeMovie failed");     [qtMovie retain];              // ... do stuff with movie here        if (dataRefH)     {         DisposeHandle(dataRefH);     }      if (qtMovie)     {         [qtMovie release];     }      if (nativeMovie)     {         DisposeMovie(nativeMovie);     }  }
```

Thereafter the movie will draw to the "dummy" gworld destination.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-04-24 | Added how to get a movie frame as an image, plus updates for existing Q&As about creating a movie and adding images, adding a QTTrack, QTMovie object not fully formed and movie unexpectedly draws to upper left of screen. |
| 2006-09-25 | New Q&A additions to cover threading, synchronous movie instantiation and others. |
| 2005-12-19 | Fix to pass correct time scale value to NewTrackMedia |
| 2005-07-14 | New document that provides answers to many frequently asked QTKit questions. |

