---
title: Movie Export - Always fill in the MovieExportGetDataParams dataSize field
apple_id: DTS10003510
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2005-02-25'
source_url: https://developer.apple.com/library/archive/qa/qa1304/_index.html
archived_at: '2026-07-18T02:30:22.468642Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1304

# Movie Export - Always fill in the MovieExportGetDataParams dataSize field

## Q:  Our application uses `MovieExportFromProceduresToDataRef` to export video from a data source other than a QuickTime Movie. How important is it to fill in the `dataSize` parameter of the `MovieExportGetDataParams` structure? We've been using 0 hoping QuickTime will "do the right thing."

A: The size of the data being returned from this callback is a critical piece of information for QuickTime. So it's very important to correctly fill in the `MovieExportGetDataParams` `dataSize` field in your `MovieExportGetDataProc`. Some decompressors will not work unless they know the size of their sample data.

If the data is coming straight from a chunky raster image, `GWorld`, `PixMap`, or the image data associated with a `CGBitmapContext` for example, the `dataSize` should be (`rowBytes` \* `height`).

If you use the utility `MakeImageDescriptionForPixMap` API, it will fill in the correct `dataSize` value in the returned `ImageDescriptionHandle` which can then be used to fill in the `MovieExportGetDataParams` `dataSize` field. See Listing 1.

Failure to follow this guidelines will result in future compatibility issues.

__Listing 1__  A simple `MovieExportGetDataProc` providing video frames from a `PixMap`.

```swift
#define kMovieLengthInSeconds   10    // the length of our data in seconds
#define kVideoSampleRate        3000  // 30 frames per second
#define kVideoFrameDuration     100

#define kVideoFrameHeight       120L
#define kVideoFrameWidth        160L

// the structure that stores information we want passed to the app-defined
// procedure that generates video data
// a pointer to this struct is pass to MovieExportAddDataSource as the refCon
typedef struct {
  GWorldPtr              fGWorld;
  long                   fTrackID;
  long                   fDataSize;
  ImageDescriptionHandle fImageDescription;
} VideoDataRec, *VideoDataRecPtr;

static pascal OSErr My_VideoDataProc(void *inRefCon, MovieExportGetDataParams *inParams)
{
  CGrafPtr         myOldPort;
  GDHandle         myOldDevice;
  Rect             myRect;
  Str255           myString;
  static long      myFrameNum = 0;

  VideoDataRecPtr  myVideoDataRecPtr = (VideoDataRecPtr)inRefCon;

  if (NULL == myVideoDataRecPtr) return paramErr;

  // end the data after desired length of movie
  if (inParams->requestedTime >
       kVideoSampleRate * kMovieLengthInSeconds) return eofErr;

  // set the size of the video frame
  MacSetRect(&myRect, 0, 0, kVideoFrameWidth, kVideoFrameHeight);

  // if we haven't allocated a GWorld yet do it now
  // this is our "source" for the video frame
  if (NULL == myVideoDataRecPtr->fGWorld) {
      PixMapHandle myPixMap = NULL;
      OSErr        myErr = noErr;

      QTNewGWorld(&(myVideoDataRecPtr->fGWorld), k32ARGBPixelFormat,
                   &myRect, NULL, NULL, 0);
    if (NULL == myVideoDataRecPtr->fGWorld) return memFullErr;

    // grab the pixmap and create the ImageDescription
    myPixMap = GetGWorldPixMap(myVideoDataRecPtr->fGWorld);
    if (NULL == myPixMap) return memFullErr;

    LockPixels(myPixMap);

    // creates an Image Description for our "source" PixMap
    // MakeImageDescriptionForPixMap fills in the dataSize parameter of the
    // ImageDescription structure with the correct value
    myErr = MakeImageDescriptionForPixMap(myPixMap,
                                          &(myVideoDataRecPtr->fImageDescription));
    if (noErr != myErr) return myErr;

    myVideoDataRecPtr->fDataSize = (**(myVideoDataRecPtr->fImageDescription)).dataSize;
  }

  GetGWorld(&myOldPort, &myOldDevice);
  SetGWorld(myVideoDataRecPtr->fGWorld, NULL);

  // draw a frame:
  // white rectangle with black frame number centered horizontally in frame
  EraseRect(&myRect);

  ForeColor(whiteColor);
  PaintRect(&myRect);

  ForeColor(blackColor);
  NumToString(++myFrameNum, myString);
  MoveTo((short)(myRect.right / 2) - (StringWidth(myString) / 2),
         (short)(myRect.bottom / 2));
  TextSize((short)(myRect.bottom / 4));
  DrawString(myString);

  // fill in the MovieExportGetDataParams for QuickTime
  inParams->actualTime = inParams->requestedTime;
  inParams->dataPtr = GetPixBaseAddr(GetGWorldPixMap(myVideoDataRecPtr->fGWorld));

  // we know the dataSize is correct as MakeImageDescriptionForPixMap
  // supplied this value
  inParams->dataSize = myVideoDataRecPtr->fDataSize;
  inParams->desc = (SampleDescriptionHandle)(myVideoDataRecPtr->fImageDescription);

  inParams->descType = VideoMediaType;
  inParams->descSeed = 1;
  inParams->actualSampleCount = 1;
  inParams->durationPerSample = kVideoFrameDuration;
  inParams->sampleFlags = 0L; // sync sample

  // restore the original graphics port and device
  SetGWorld(myOldPort, myOldDevice);

  return noErr;
}
```


- [Exporting Data from Sources Other Than Movies](https://developer.apple.com/documentation/QuickTime/REF/refDataExchange.f.htm#pgfId=7909)
- [QTMovieFromProcs Sample](https://developer.apple.com/samplecode/qtmoviefromprocs/qtmoviefromprocs.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-02-25 | New document that outlines the importance of correctly filling in the MovieExportGetDataParams dataSize field when exporting from procedures. |

