---
title: New AV Foundation APIs in OS X Yosemite for Professional Video Workflows
apple_id: DTS40015060
resource_type: Technical Note
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2014-12-01'
source_url: https://developer.apple.com/library/archive/technotes/tn2404/_index.html
archived_at: '2026-07-26T19:54:14.903936Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2404

# New AV Foundation APIs in OS X Yosemite for Professional Video Workflows

AV Foundation in OS X Yosemite introduces new features for professional video workflows. These include classes for iterating and examining the samples in a media, support for URL reference movies, writing of fragmented movie files, enhancements to DV file format support and uncompressed movie support.

This document provides a high-level overview of these new features.

[New classes for media sample introspection and loading: AVSampleCursor and AVSampleBufferGenerator](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytkmbwgawugsbrfvhekv27ingecu2tivjv6rspkjpu2rkejfav6u2bjvieyrk7jfhfiuspkniekq2ujfhu4x2bjzcf6tcpifcestshl5pucvstifgvatcfinkveu2pkjpuctsel5avmu2bjvieyrkckvdemrksi5cu4rksifke6uq)[AVSampleCursor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytkmbwgawugsbrfvhekv27ingecu2tivjv6rspkjpu2rkejfav6u2bjvieyrk7jfhfiuspkniekq2ujfhu4x2bjzcf6tcpifcestshl5pucvstifgvatcfinkveu2pkjpuctsel5avmu2bjvieyrkckvdemrksi5cu4rksifke6urniflfgqknkbgekq2vkjju6uq)[AVSampleBufferGenerator](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytkmbwgawugsbrfvhekv27ingecu2tivjv6rspkjpu2rkejfav6u2bjvieyrk7jfhfiuspkniekq2ujfhu4x2bjzcf6tcpifcestshl5pucvstifgvatcfinkveu2pkjpuctsel5avmu2bjvieyrkckvdemrksi5cu4rksifke6urniflfgqknkbgekqsvizdekushivhekusbkrhve)[URL Reference movie support](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytkmbwgawugsbrfvkvetc7kjcumrksivhegrk7jvhvmskfl5jvkucqj5jfi)[Fragmented movie support](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytkmbwgawugsbrfvdfeqkhjvcu4vcfirpu2t2wjfcv6u2vkbie6usu)[DV Stream File Format Support](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytkmbwgawugsbrfvcfmx2tkrjekqknl5destcfl5de6usnifkf6u2vkbie6usu)[Uncompressed Movie Support](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytkmbwgawugsbrfvku4q2pjviferktkncuix2nj5lesrk7knkvaucpkjka)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytkmbwgawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## New classes for media sample introspection and loading: AVSampleCursor and AVSampleBufferGenerator

### AVSampleCursor

`AVAssetTrack` now supports methods to create `AVSampleCursor` objects.  `AVSampleCursor` objects can be used to iterate and examine the samples in a media (as could be done with the now deprecated QuickTime APIs such as `GetMediaNextInterestingTime`, `GetMediaSampleReference` and `CopyMediaMutableSampleTable`).

The simplest case is creating an instance of `AVSampleCursor` from an `AVAssetTrack` and positioning it at the first (or last) media sample in decode order. You should always first check the `AVAssetTrack` `canProvideSampleCursors` property to determine whether the asset can provide instances of `AVSampleCursor` for traversing its media samples and discovering information about them. See Listing 1.

__Listing 1__  Creating an `AVSampleCursor` object from an `AVAssetTrack` instance.

```
AVAssetTrack *assetTrack = <#An AVAssetTrack#>;
if (assetTrack.canProvideSampleCursors)
{
    // Create an instance of AVSampleCursor and position it at the receiver's
    // first media sample in decode order.
    AVSampleCursor *cursor = [assetTrack makeSampleCursorAtFirstSampleInDecodeOrder];

    // Do something interesting with the AVSampleCursor

}
```

An `AVSampleCursor` can also be created and positioned at or near a specified presentation timestamp:

__Listing 2__  Create and initialize a `AVSampleCursor` object from an `AVAssetTrack` and time stamp.

```
AVAssetTrack *assetTrack = <#An AVAssetTrack#>;
if (assetTrack.canProvideSampleCursors)
{
    CMTime presentationTimeStamp = <#A time stamp#>;
    // Create an instance of AVSampleCursor and position it at the specified time stamp
    AVSampleCursor *cursor =
        [assetTrack makeSampleCursorWithPresentationTimeStamp:presentationTimeStamp];

    // Do something interesting with the AVSampleCursor

}
```

An `AVSampleCursor` can traverse across a given number of samples in decode order using the `stepInDecodeOrderByCount` method, or in presentation order using the `stepInPresentationOrderByCount` method. Similarly, you can reposition a cursor by a specific `deltaTime` on the decode or presentation timeline using the `stepByDecodeTime:wasPinned:` and `stepByPresentationTime:wasPinned:` methods, respectively.

You can compare the relative positions of two AVSampleCursors with the `comparePositionInDecodeOrderWithPositionOfCursor` method. You can also test a boundary in the reordering from decode order to presentation order with the `samplesWithEarlierDecodeTimeStampsMayHaveLaterPresentationTimeStampsThanCursor` and `samplesWithLaterDecodeTimeStampsMayHaveEarlierPresentationTimeStampsThanCursor` methods.

An `AVSampleCursor` object can provide various information about the media sample at its current position, such as its duration, presentation and decode timestamps, its ability to be decoded independently of other media samples, offset and length in its storage container, and whether or not the sample is intended to be loaded with other contiguous media samples in a "chunk".

See `AVSampleCursor`.h and `AVAssetTrack`.h for more information.

### AVSampleBufferGenerator

The `AVSampleBufferGenerator` class provides flexible services for loading samples referenced by `AVSampleCursor` into `CMSampleBuffer` objects.  Each request for `CMSampleBuffer` creation is described in an `AVSampleBufferRequest` object.

To use an `AVSampleBufferGenerator`, first create an `AVSampleBufferRequest` object and set its properties to configure your request:

__Listing 3__  Creating and configuring an `AVSampleBufferRequest` object.

```
// Create a AVSampleBufferRequest object from an AVSampleCursor.
AVSampleCursor *cursor = <#An AVSampleCursor#>;
AVSampleBufferRequest *sampleBufferRequest =
    [[AVSampleBufferRequest alloc] initWithStartCursor:cursor];
if (sampleBufferRequest)
{
    // Configure the AVSampleBufferRequest
    // See AVSampleBufferGenerator.h for more information
    sampleBufferRequest.direction = AVSampleBufferRequestDirectionForward;

    // Do something interesting with the AVSampleBufferRequest

}
```

You create an `AVSampleBufferGenerator` object from an `AVAsset` instance using the `initWithAsset` method. The request will be immediate if you pass `NULL` for the `CMTimebase` argument or set AVSampleBufferRequestModeImmediate as the mode; or scheduled if you pass a valid `CMTimebase` value and set AVSampleBufferRequestModeScheduled as the mode.

To generate a `CMSampleBuffer` from an `AVSampleBufferGenerator` object, call the `AVSampleBufferGenerator` `createSampleBufferForRequest` method, passing your `AVSampleBufferRequest` instance as a parameter. See Listing 4.

__Listing 4__  Generating a `CMSampleBuffer` from an `AVSampleBufferGenerator` object.

```
AVSampleBufferRequest *sampleBufferRequest = <#An AVSampleBufferRequest for the AVAsset#>;
AVAsset *asset = <#The AVAsset#>;
AVSampleBufferGenerator *generator =
    [[AVSampleBufferGenerator alloc] initWithAsset:asset timebase:NULL];
if (generator)
{
    CMSampleBufferRef samplebuffer =
        [generator createSampleBufferForRequest:sampleBufferRequest];

    // Do something interesting with sample buffer.

    // For example:
    // CMItemCount itemCount = CMSampleBufferGetNumSamples(samplebuffer);
    // etc.

    // See CMSampleBufferRef.h

    CFRelease(samplebuffer);
}
```

See `AVSampleBufferGenerator`.h for more information.

[Back to Top](#)

## URL Reference movie support

In OS X Yosemite, AV Foundation supports reference movies, where the movie file may not actually contain the movie's sample data.  Such movie files contain relative or absolute URLs to other files where sample data is stored.  URL reference movies may be played via `AVPlayer`.

__Important:__ Alias record-based reference movies are not supported.

A new `AVAssetReaderOutput` subclass, `AVAssetReaderSampleReferenceOutput`, lets you read `CMSampleBuffer`'s which contain the absolute URL and offset in place of the sample data.  To create an `AVAssetReaderSampleReferenceOutput` object, you supply the asset track for which which the resulting `AVAssetReaderSampleReferenceOutput` should provide sample references. The track must be one of the tracks contained by the target `AVAssetReader`'s asset.

Clients can extract information about the location (file URL and offset) of samples in a track by adding an instance of `AVAssetReaderSampleReferenceOutput` to an `AVAssetReader` using the `AVAssetReader` `addOutput` method as shown in Listing 5.

__Listing 5__  Creating an `AVAssetReaderSampleReferenceOutput` object and adding it as an `AVAssetReader` output.

```
AVAssetReader *assetReader = <#an asset reader#>;
AVAssetTrack *aTrack = <#an asset track contained by the asset reader's asset#>;

AVAssetReaderSampleReferenceOutput *sampleRefOutput =
    [AVAssetReaderSampleReferenceOutput assetReaderSampleReferenceOutputWithTrack: aTrack];

// Add AVAssetReaderSampleReferenceOutput to the AVAssetReader
[assetReader addOutput: sampleRefOutput];
```

No actual sample data can be extracted using the `AVAssetReaderSampleReferenceOutput` class. The location of the sample data is described by the `kCMSampleBufferAttachmentKey_SampleReferenceURL` and `kCMSampleBufferAttachmentKey_SampleReferenceByteOffset` attachments on the extracted sample buffer. Use the `CMGetAttachment` API to get these attachments from the sample buffer. Listing 6 shows an example.

__Listing 6__  Get the `kCMSampleBufferAttachmentKey_SampleReferenceURL`, `kCMSampleBufferAttachmentKey_SampleReferenceByteOffset` attachments from a sample buffer.

```
CMSampleBufferRef sampleBuffer = <#a sample buffer#>;

CMAttachmentMode attachmentMode;
CFURLRef url = CMGetAttachment(sampleBuffer, kCMSampleBufferAttachmentKey_SampleReferenceURL, &attachmentMode);
if (url)
{
    // Do something interesting with the URL.
}

CFNumberRef byteoffset = CMGetAttachment(sampleBuffer, kCMSampleBufferAttachmentKey_SampleReferenceByteOffset, &attachmentMode);
if (byteoffset)
{
    // Do something interesting with the byte offset.
}
```

More information about sample buffers describing sample references can be found in the `CMSampleBuffer` documentation. `CMSampleBuffer`'s constructed in this manner may be provided to `AVAssetWriterInput` to write sample references to new movie files.

A new `AVAssetWriterInput` property, `sampleReferenceBaseURL`, lets you specify a base URL that the sample reference URLs should be rewritten to be relative to. If the value of this property can be resolved as an absolute URL, the sample locations written to the file when appending sample references will be relative to this URL. The URL must point to a location that is in a directory that is a parent of the sample reference location. For example, setting the `sampleReferenceBaseURL` property to "file:///User/johnappleseed/Movies/" and appending sample buffers with the `kCMSampleBufferAttachmentKey_SampleReferenceURL` attachment set to "file:///User/johnappleseed/Movies/data/movie1.mov" will cause the sample reference "data/movie1.mov" to be written to the movie.

See `AVAssetReaderOutput`.h, `AVAssetWriterInput`.h and `CMSampleBuffer`.h for more information.

[Back to Top](#)

## Fragmented movie support

AVFoundation's `AVCaptureMovieFileOutput` and `AVAssetWriter` APIs support writing fragmented movie files. Such files have a regular movie header near the beginning that describes some initial period of media data, followed by "fragments" consisting of a period of media data and then a "movie fragment" describing that additional data.  This approach provides crash-resilience, since even if file writing stops abruptly, only the most recent fragment can be lost.

A new `AVAsset` subclass, `AVFragmentedMovie`, is aware of the presence of movie fragments, and a companion class, `AVFragmentedMovieMinder`, can be used to request that AVFoundation periodically examine the movie file to see if more movie fragments have been appended.  If they have, they are incorporated into the `AVAsset` and the newly added media data can immediately be played without needing to close and reopen the `AVAsset`. See AVMovie.h for additional information.

To enable writing of fragmented movie files using `AVCaptureMovieFileOutput` or `AVAssetWriter`, specify a time to elapse between writing movie fragments value for the `movieFragmentInterval` property on these classes (the default value is `kCMTimeInvalid`, which means that movie fragments should not be used).

In OS X Yosemite, QuickTime Player X uses these new services, so if you open a fragmented movie file while it is being captured by another process or computer, you will see its duration periodically increase, and you can scrub into and play portions of the movie that had not yet been captured when you first opened it.

[Back to Top](#)

## DV Stream File Format Support

Support for playback of DV stream files is now directly integrated into the AVFoundation/CoreMedia workflow on OS X Yosemite.

[Back to Top](#)

## Uncompressed Movie Support

Uncompressed movie formats now supported on OS X Yosemite include:

- R10k
- v210
- 2vuy

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-12-01 | New document that describes AV Foundation APIs in OS X Yosemite for professional video workflows. |

