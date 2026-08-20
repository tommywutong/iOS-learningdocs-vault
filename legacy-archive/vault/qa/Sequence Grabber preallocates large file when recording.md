---
title: Sequence Grabber preallocates large file when recording
apple_id: DTS10003505
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2006-02-06'
source_url: https://developer.apple.com/library/archive/qa/qa1411/_index.html
archived_at: '2026-07-18T02:30:32.113837Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1411

# Sequence Grabber preallocates large file when recording

## Q:  I'm using the sequence grabber to record video to a movie. I call `SGSetDataOutput` with the `seqGrabToDisk` flag to specify the recorded video be written to a movie file on disk. However, when I begin recording by calling either `SGPrepare` or `SGStartRecord` QuickTime will preallocate a large file that fills up much of my disk. How can I prevent this?

A: QuickTime 7 for Mac OS X version 10.4 introduced the `seqGrabDontPreAllocateFileSize` flag which you can use to prevent the sequence grabber from preallocating a large file when recording to a movie file on disk.

The following Objective-C code listing demonstrates how to specify the destination data reference for a record operation using the `seqGrabDontPreAllocateFileSize` flag, taking into account the state of the `seqGrabAppendToFile` flag as well:

__Listing 1__  Configuring the destination data reference for a sequence grabber record operation.

```objc
- (OSStatus)setCapturePath:(NSString*)filePath flags:(long)flags
{
    OSStatus err = noErr;
    Handle dataRef = NULL;
    OSType dataRefType = 0;

    if (filePath)
    {
        require(QTNewDataReferenceFromFullPathCFString(
                        (CFStringRef)filePath,
                        (UInt32)kQTNativeDefaultPathStyle,
                        0, &dataRef, &dataRefType) == noErr, bail);
    }

    if ( !(flags & seqGrabDontMakeMovie) )
    {
        if ( (flags & seqGrabDontPreAllocateFileSize) &&
            !(flags & seqGrabAppendToFile) )
        {
            // Sequence Grabber will still preallocate the file on disk unless
            // seqGrabAppendToFile is also set. So if you wish to keep
            // Sequence Grabber from preallocating a large file on disk, but
            // you don't want to append to an existing file, you need to open
            // up the desired file and truncate it first, then set the
            // seqGrabAppendToFile flag.

            // truncate the file on disk first
            fclose(fopen([filePath cString], "w"));
            flags |= seqGrabAppendToFile;
        }
    }

    err = SGSetDataRef(mSeqGrab, dataRef, dataRefType, flags);

bail:
    DisposeHandle(dataRef);
    return err;
}
```

For applications which must run pre-QuickTime 7, you can specify a maximum offset for data written to a given sequence grabber output using the `SGSetOutputMaximumOffset` function. If an attempt is made to write data beyond the maximum offset, the sequence grabber switches to the next output as designated by `SGSetOutputNextOutput`. If no more outputs are available, an end-of-file error is returned and recording ends.

To monitor the space used by a sequence grabber output while recording, use `SGGetStorageSpaceRemaining` or `SGGetStorageSpaceRemaining`64. This will return a value indicating the amount of space remaining for the current record operation. If you are recording to memory, this value contains information about the amount of memory remaining. If you are recording to a movie file, this value contains information about the amount of storage space available on the device that holds the file.

If you are using multiple sequence grabber outputs, use `SGGetDataOutputStorageSpaceRemaining` or `SGGetDataOutputStorageSpaceRemaining`64 to monitor the available space while recording.

- [SGSetDataOutput](https://developer.apple.com/documentation/QuickTime/APIREF/sgsetdataoutput.htm)
- [SGStartRecord](https://developer.apple.com/documentation/QuickTime/APIREF/sgstartrecord.htm)
- [SGSetOutputMaximumOffset](https://developer.apple.com/documentation/QuickTime/APIREF/sgsetoutputmaximumoffset.htm)
- [SGSetOutputNextOutput](https://developer.apple.com/documentation/QuickTime/APIREF/sgsetoutputnextoutput.htm)
- [SGGetStorageSpaceRemaining](https://developer.apple.com/documentation/QuickTime/APIREF/sggetstoragespaceremaining.htm)
- [SGGetStorageSpaceRemaining64](https://developer.apple.com/documentation/QuickTime/APIREF/sggetstoragespaceremaining64.htm)
- [SGGetDataOutputStorageSpaceRemaining](https://developer.apple.com/documentation/QuickTime/APIREF/sggetdataoutputstoragespaceremaining.htm)
- [SGGetDataOutputStorageSpaceRemaining64](https://developer.apple.com/documentation/QuickTime/APIREF/sggetdataoutputstoragespaceremaining64.htm)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-02-06 | added seqGrabDontPreAllocateFileSize flag info. |
| 2005-02-22 | New document that describes how to prevent the Sequence Grabber from filling your entire disk when recording. |

