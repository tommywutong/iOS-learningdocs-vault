---
title: ICM Drawing non-scheduled frames with QuickTime 6
apple_id: DTS10003089
resource_type: Technical Note
platform: macOS
topic: null
technology: QuickTime
published: '2009-10-09'
source_url: https://developer.apple.com/library/archive/technotes/tn2060/_index.html
archived_at: '2026-07-26T19:53:49.801989Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



# Retired Document

__Important:__
This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Technical Note TN2060

# ICM Drawing non-scheduled frames with QuickTime 6

__Important:__ This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

This technote discusses changes to how the Image Compression Manager draws non-scheduled frames in QuickTime 6 on Mac OS X.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbyhewugsbrfvjukq2ujfhu4mi)[Some terminology](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbyhewugsbrfvjukq2ujfhu4mq)[What happens when my application draws using QuickDraw?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbyhewugsbrfvjukq2ujfhu4my)[What did QuickTime 5 do?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbyhewugsbrfvjukq2ujfhu4na)[What changed in QuickTime 6?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbyhewugsbrfvjukq2ujfhu4ni)[So, what's the problem?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbyhewugsbrfvjukq2ujfhu4nq)[What should I do if my application encounters this problem?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbyhewugsbrfvjukq2ujfhu4ny)[1. Let the run loop run.](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbyhewugsbrfvjukq2ujfhu4nzngfpv6tcfkrpviscfl5jfkts7jrhu6uc7kjku4xy)[2. Call QDFlushPortBuffer.](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbyhewugsbrfvjukq2ujfhu4nzngjpv6q2bjrgf6ukeizgfku2ikbhvevcckvdemrksl4)[3. Tell the Image Compression Manager to flush.](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbyhewugsbrfvjukq2ujfhu4nzngnpv6vcfjrgf6vciivpustkbi5cv6q2pjviferktkneu6ts7jvau4qkhivjf6vcpl5deyvktjbpq)[4. Tell the Movie Toolbox to flush.](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbyhewugsbrfvjukq2ujfhu4nzngrpv6vcfjrgf6vciivpu2t2wjfcv6vcpj5geet2yl5ke6x2gjrkvgsc7)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbyhewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

Windows on Mac OS X are double-buffered. In other words, every window has an offscreen buffer associated with it, and applications draw into the offscreen buffer (using QuickDraw, Quartz, QuickTime, or OpenGL). When an application is done drawing into the offscreen buffer, the image is copied to the frame buffer by the Quartz Compositor. Sending the image to the Quartz Compositor is called flushing.

Usually, Mac OS X handles window flushing for you, and your application does not need to be aware of it. However, there are some changes in the way QuickTime 6 handles this which may make application drawing behave differently.

[Back to Top](#)

## Some terminology

For the purposes of this note:

- flushing means sending part of a window's offscreen buffer to the Quartz Compositor for display on the screen.
- a run loop is a Core Foundation service that monitors sources of input to a task (such as events), calls callbacks to handle them, and sleeps in between. Carbon and Cocoa event loops are implemented using run loops.
- a decompression is any drawing operation mediated by the Image Compression Manager. This includes frames of video, images drawn with Graphics Importer components, and compressed pictures.
- a scheduled decompression is a decompression set up to occur at a specific time in the future.
- a non-scheduled decompression is a decompression that happens immediately.

Graphics Importers and compressed pictures always use non-scheduled decompression. When playing a movie, QuickTime tries to use scheduled decompression for drawing all video frames, because this allows for more accurate frame timing. However, certain things can cause QuickTime to fall back to non-scheduled decompression. These include video codecs that don't support scheduling and cases when there is not enough CPU power available to play the movie.

[Back to Top](#)

## What happens when my application draws using QuickDraw?

QuickDraw maintains a dirty region associated with each `GrafPort`. When an application draws into a `GrafPort`, the area drawn to is added to the ports dirty region. When your application returns to its run loop, Carbon walks the list of windows and flushes their dirty regions by calling `QDFlushPortBuffer`. This means that even if drawing operations took a while, everything appears on the screen in one crisp refresh.

[Back to Top](#)

## What did QuickTime 5 do?

QuickTime 5 did the same thing for both scheduled and non-scheduled decompressions: as soon as the drawing was complete, QuickTime would flush the image to the screen.

This is the correct thing to do for playing movies: every video frame should be displayed as soon as possible. However, it meant that applications that mixed still images drawn using Graphics Importers (for example) with other QuickDraw drawing would look bad, because the still images would be displayed on the screen before everything else -- not in one crisp refresh.

[Back to Top](#)

## What changed in QuickTime 6?

After scheduled decompressions, QuickTime 6 flushes images to the screen.

After non-scheduled decompressions, QuickTime 6 does not flush. Instead, it adds the drawn area to QuickDraw's dirty region for that `GrafPort`, expecting the run loop to flush the dirty region along with any other drawing. So applications that mix Graphics Importers and QuickDraw will get crisper screen updates than before.

[Back to Top](#)

## So, what's the problem?

While this change to the Image Compression Manager brings non-scheduled drawing into line with QuickDraw drawing, it means you may not actually see the results of a drawing operation if your application:

- uses an on-screen port that is not a Carbon window, or
- doesn't let the run loop execute regularly (e.g., sitting in a tight loop with no calls to `WaitNextEvent` or not returning control from a Carbon event handler).

In case you're curious, one example of an onscreen port that is not a Carbon window is the application dock tile port, which you can create by calling `BeginQDContextForApplicationDockTile`.

[Back to Top](#)

## What should I do if my application encounters this problem?

To avoid these drawing problems, applications are advised to implement one or more of the following:

- let the run loop run, if drawing is in a Carbon window.
- call `QDFlushPortBuffer` after any non-scheduled decompression, to flush explicitly.
- set the Image Compression Manager sequence `codecDSequenceFlushInsteadOfDirtying` flag for your decompression sequence causing the Image Compression Manager to implicitly flush.This can be done using the `SetDSequenceFlags` API.
- set the movie play hint `hintsFlushVideoInsteadOfDirtying` for your movie. This can be done using the `SetMoviePlayHints` API.

Let's go into each of these options in more detail.

### 1. Let the run loop run.

All sorts of things stop happening when you don't let the run loop run. Carbon event loop timers don't fire; your application doesn't receive events (so the dock will report that your application is not responding); and dirty regions in windows don't get flushed. If possible, look into restructuring your code so that your event handler returns. In some cases, using Carbon event loop timers can simplify your code and make it less CPU-greedy.

This won't help if your application is drawing into an on-screen port that is not a Carbon window, however, because it won't be found when Carbon walks the window list.

### 2. Call QDFlushPortBuffer.

This might be appropriate if you have a short animation drawn using QuickTime and it's not convenient for your event handler to return until it's done.

__Listing 1__  Use a Graphics Importer to draw and rotate an image.

```
WindowRef gWindow;

OSErr DoSillyRotation( const FSSpecPtr inFSSpec )
{
    GraphicsImportComponent importer = 0;
    Rect                    naturalBounds,
                            windowBounds;
    MatrixRecord            matrix;
    UInt32                  rotation = 0;
    OSErr                   err = noErr;

    err = GetGraphicsImporterForFile( inFSSpec, &importer );
    if ( err ) goto bail;

    // get the native size of the image
    err = GraphicsImportGetNaturalBounds( importer, &naturalBounds );
    if ( err ) goto bail;

    windowBounds = naturalBounds;
    OffsetRect( &windowBounds, 10, 45 );
    gWindow = NewCWindow( NULL, &windowBounds,
                         "\pSilly GImport Rotate", true, documentProc,
                         (WindowPtr)-1, true, 0);
    if ( NULL == gWindow ) goto bail;

    // set the graphics port for drawing
    err = GraphicsImportSetGWorld( importer,
                       GetWindowPort( gWindow ), NULL );
    if ( err ) goto bail;

    // do silly rotation
    do {

        // reset the matrix
        SetIdentityMatrix( &matrix );

        // modify the contents of a matrix so that it defines a
        // rotation operation - 'rotation' degrees to the right
        RotateMatrix( &matrix,
              Long2Fix( rotation ),
              Long2Fix(( naturalBounds.right - naturalBounds.left ) / 2 ),
              Long2Fix(( naturalBounds.bottom - naturalBounds.top ) / 2 ));

        // set the transformation matrix
        GraphicsImportSetMatrix( importer, &matrix );

        // draw
        err = GraphicsImportDraw( importer );
        if ( err ) break;

        // explicitly flush - required under QuickTime 6
        QDFlushPortBuffer( GetWindowPort( gWindow ), NULL );
        rotation += 30;

    } while ( rotation <= 360 );

bail:
    if ( importer ) CloseComponent( importer );

    return err;
}
```

### 3. Tell the Image Compression Manager to flush.

If you're using Image Compression Manager decompression sequences directly, you can set a flag to tell it to flush as it did in QuickTime 5.

```
enum {
    codecDSequenceFlushInsteadOfDirtying = (1L << 8)
};
```

__Listing 2__  Use a Decompression Sequence to draw and rotate an image.

```
WindowRef gWindow;

OSErr DoDSeqSillyRotation( const FSSpecPtr inFSSpec )
{
    GraphicsImportComponent importer = 0;
    Rect                    naturalBounds,
                            windowBounds;
    ImageSequence           seqID = 0;
    ImageDescriptionHandle  desc = NULL;
    Ptr                     pData = NULL;
    MatrixRecord            matrix;
    UInt32                  rotation = 0;
    GrafPtr                 savedPort;
    OSErr                   err = noErr;

    GetPort(&savedPort);

    err = GetGraphicsImporterForFile( inFSSpec, &importer );
    if ( err ) goto bail;

    // get the native size of the image associated with the importer
    err = GraphicsImportGetNaturalBounds( importer, &naturalBounds );
    if ( err ) goto bail;

    windowBounds = naturalBounds;
    OffsetRect( &windowBounds, 10, 45 );
    gWindow = NewCWindow( NULL, &windowBounds,
                         "\pSilly DSequence Rotate", true, documentProc,
                         (WindowPtr)-1, true, 0);
    if ( NULL == gWindow ) goto bail;

    SetPortWindowPort( gWindow );

    // get the image description
    err = GraphicsImportGetImageDescription( importer, &desc );
    if ( err ) goto bail;

    // we need to stick the image data somewhere
    pData = NewPtrClear( (**desc).dataSize );
    if ( MemError() || NULL == pData ) goto bail;

    // get the image data
    err = GraphicsImportReadData( importer, pData, 0, (**desc).dataSize );
    if ( err ) goto bail;

    // *** use a decompression sequence to draw ***

    // begin the sequence
    err = DecompressSequenceBeginS( &seqID, desc, NULL, 0,
                                    GetWindowPort( gWindow ), NULL, NULL,
                                    NULL, srcCopy, NULL, 0, codecNormalQuality,
                                    anyCodec );
    if ( err ) goto bail;

    // under QuickTime 6 setting the codecDSequenceFlushInsteadOfDirtying
    // flag for a decompression sequence causes the Image Compression Manager
    // to implicitly flush - setting this flag has no effect under QuickTime 5
    SetDSequenceFlags( seqID, codecDSequenceFlushInsteadOfDirtying,
                     codecDSequenceFlushInsteadOfDirtying ); // do a silly rotation
    do {

        // reset the matrix
        SetIdentityMatrix( &matrix );

        // modify the contents of a matrix so that it defines a rotation operation
        // 'rotation' degrees to the right
        RotateMatrix( &matrix,
                      Long2Fix( rotation ),
                      Long2Fix(( naturalBounds.right - naturalBounds.left ) / 2 ),
                      Long2Fix(( naturalBounds.bottom - naturalBounds.top ) / 2 ));

        // set the transformation matrix to use for drawing an image
        SetDSequenceMatrix( seqID, &matrix );

        // draw the image
        err = DecompressSequenceFrameS( seqID, pData, (**desc).dataSize, 0,
                                        NULL, NULL );
        if ( err ) goto bail;

        rotation += 30;

    } while ( rotation <= 360 );

bail:
    if ( seqID ) CDSequenceEnd( seqID );
    if ( importer ) CloseComponent( importer );
    if ( desc ) DisposeHandle( (Handle)desc );
    if ( pData ) DisposePtr( pData );

    SetPort( savedPort );

    return err;
}
```

__Note:__ Setting the `codecDSequenceFlushInsteadOfDirtying` flag has no effect under QuickTime 5.

### 4. Tell the Movie Toolbox to flush.

If you're playing a movie, you can set a play hint to tell the movie to flush. For movies that play using scheduled decompression (or using hardware acceleration) this may not appear to be necessary. Animated GIFs use neither, so if you change the movie to an animated GIF and you don't see frames, you may need to set this play hint.

```
enum {
    hintsFlushVideoInsteadOfDirtying = (1L << 22)
};
```

__Listing 3__  Play an animated GIF file as a movie.

```
WindowRef gWindow;
Movie     gMovie;

OSErr PlayAnimatedGIF( const FSSpecPtr inGifFile )
{
    short     refNum = 0;
    Rect      bounds;
    long      numberOfSamples;
    GrafPtr   savedPort;
    OSErr     err;

    GetPort( &savedPort );

    err = OpenMovieFile( inGifFile, &refNum, fsRdPerm );
    if (err) goto bail;

    // create a movie from the GIF
    err = NewMovieFromFile( &gMovie, refNum, NULL, NULL, newMovieActive, NULL );
    CloseMovieFile( refNum );
    if ( err || NULL == gMovie ) goto bail;

    GetMovieNaturalBoundsRect( gMovie, &bounds );
    OffsetRect( &bounds, -bounds.left, -bounds.top );
    OffsetRect( &bounds, 10, 45 );
    gWindow = NewCWindow( NULL, &bounds,
                         "\pPlay Animated GIF", true, documentProc,
                         (WindowPtr)-1, true, 0 );

    SetPortWindowPort( gWindow );

    // set the movies GWorld
    SetMovieGWorld( gMovie, GetWindowPort( gWindow ), NULL );

    // get the sample count - this will let us know if it's animated or not
    numberOfSamples =
          GetMediaSampleCount( GetTrackMedia( GetMovieIndTrack( gMovie, 1 ) ));

    // it's animated - under QuickTime 6 set the
    // hintsFlushVideoInsteadOfDirtying play hint
    if ( numberOfSamples > 1 ) {
        SetMoviePlayHints( gMovie, hintsFlushVideoInsteadOfDirtying,
                         hintsFlushVideoInsteadOfDirtying );
    }

    StartMovie( gMovie );

    do {
        MoviesTask( gMovie, 0 );
    } while ( !IsMovieDone( gMovie ) );

bail:
    SetPort( savedPort );

    return err;
}
```

Play hints are passed down to media handlers; media handlers should obey this play hint by making sure whatever they draw gets flushed -- possibly by calling `QDFlushPortBuffer` or by setting the `codecDSequenceFlushInsteadOfDirtying` flag discussed above on any decompression sequences they use.

__Note:__ Setting the `hintsFlushVideoInsteadOfDirtying` play hint has no effect under QuickTime 5.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-10-09 | Editorial |
| 2002-08-21 | New document that changes to how the Image Compression Manager draws non-scheduled frames in QuickTime 6 on Mac OS X. |

