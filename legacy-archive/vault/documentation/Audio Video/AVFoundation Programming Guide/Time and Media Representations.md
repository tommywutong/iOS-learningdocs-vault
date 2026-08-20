---
title: AVFoundation Programming Guide
apple_id: TP40010188
resource_type: Guide
platform: tvOS|iOS|macOS
topic: null
technology: AVFoundation
published: '2015-06-30'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/AVFoundationPG/Articles/06_MediaRepresentations.html
archived_at: '2026-07-15T05:21:00.239606Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AVFoundation Programming Guide](About%20AVFoundation.md)


[Next](Document%20Revision%20History.md)[Previous](Export.md)

# Time and Media Representations

Time-based audiovisual data, such as a movie file or a video stream, is represented in the AV Foundation framework by `AVAsset`. Its structure dictates much of the framework works. Several low-level data structures that AV Foundation uses to represent time and media such as sample buffers come from the Core Media framework.

[AVAsset](https://developer.apple.com/documentation/avfoundation/avasset) is the core class in the AV Foundation framework. It provides a format-independent abstraction of time-based audiovisual data, such as a movie file or a video stream. The primary relationships are shown in Figure 6-1. In many cases, you work with one of its subclasses: You use the composition subclasses when you create new assets (see [Editing](About%20AVFoundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcobyfvbuqmjnknltc)), and you use [AVURLAsset](https://developer.apple.com/documentation/avfoundation/avurlasset) to create a new asset instance from media at a given URL (including assets from the MPMedia framework or the Asset Library framework—see [Using Assets](Using%20Assets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcobyfvbuqnznknltc)).

__Figure 6-1__  AVAsset provides an abstraction of time-based audiovisual data

!

An asset contains a collection of tracks that are intended to be presented or processed together, each of a uniform media type, including (but not limited to) audio, video, text, closed captions, and subtitles. The asset object provides information about whole resource, such as its duration or title, as well as hints for presentation, such as its natural size. Assets may also have metadata, represented by instances of [AVMetadataItem](https://developer.apple.com/documentation/avfoundation/avmetadataitem).

A track is represented by an instance of [AVAssetTrack](https://developer.apple.com/documentation/avfoundation/avassettrack), as shown in Figure 6-2. In a typical simple case, one track represents the audio component and another represents the video component; in a complex composition, there may be multiple overlapping tracks of audio and video.

__Figure 6-2__  AVAssetTrack

!

A track has a number of properties, such as its type (video or audio), visual and/or audible characteristics (as appropriate), metadata, and timeline (expressed in terms of its parent asset). A track also has an array of format descriptions. The array contains `CMFormatDescription` objects (see [CMFormatDescriptionRef](https://developer.apple.com/documentation/coremedia/cmformatdescriptionref)), each of which describes the format of media samples referenced by the track. A track that contains uniform media (for example, all encoded using to the same settings) will provide an array with a count of 1.

A track may itself be divided into segments, represented by instances of [AVAssetTrackSegment](https://developer.apple.com/documentation/avfoundation/avassettracksegment). A segment is a time mapping from the source to the asset track timeline.

Time in AV Foundation is represented by primitive structures from the Core Media framework.

[CMTime](https://developer.apple.com/documentation/coremedia/cmtime) is a C structure that represents time as a rational number, with a numerator (an `int64_t` value), and a denominator (an `int32_t` timescale). Conceptually, the timescale specifies the fraction of a second each unit in the numerator occupies. Thus if the timescale is 4, each unit represents a quarter of a second; if the timescale is 10, each unit represents a tenth of a second, and so on. You frequently use a timescale of 600, because this is a multiple of several commonly used frame rates: 24 fps for film, 30 fps for NTSC (used for TV in North America and Japan), and 25 fps for PAL (used for TV in Europe). Using a timescale of 600, you can exactly represent any number of frames in these systems.

In addition to a simple time value, a `CMTime` structure can represent nonnumeric values: +infinity, -infinity, and indefinite. It can also indicate whether the time been rounded at some point, and it maintains an epoch number.

You create a time using [CMTimeMake](https://developer.apple.com/documentation/coremedia/1400785-cmtimemake) or one of the related functions such as [CMTimeMakeWithSeconds](https://developer.apple.com/documentation/coremedia/1400797-cmtimemakewithseconds) (which allows you to create a time using a float value and specify a preferred timescale). There are several functions for time-based arithmetic and for comparing times, as illustrated in the following example:

```
CMTime time1 = CMTimeMake(200, 2); // 200 half-seconds
CMTime time2 = CMTimeMake(400, 4); // 400 quarter-seconds

// time1 and time2 both represent 100 seconds, but using different timescales.
if (CMTimeCompare(time1, time2) == 0) {
    NSLog(@"time1 and time2 are the same");
}

Float64 float64Seconds = 200.0 / 3;
CMTime time3 = CMTimeMakeWithSeconds(float64Seconds , 3); // 66.66... third-seconds
time3 = CMTimeMultiply(time3, 3);
// time3 now represents 200 seconds; next subtract time1 (100 seconds).
time3 = CMTimeSubtract(time3, time1);
CMTimeShow(time3);

if (CMTIME_COMPARE_INLINE(time2, ==, time3)) {
    NSLog(@"time2 and time3 are the same");
}
```

For a list of all the available functions, see _[CMTime Reference](https://developer.apple.com/documentation/coremedia/cmtime-u58)_.

Core Media provides constants for special values: `kCMTimeZero`, `kCMTimeInvalid`, `kCMTimePositiveInfinity`, and `kCMTimeNegativeInfinity`. There are many ways in which a `CMTime` structure can, for example, represent a time that is invalid. To test whether a `CMTime` is valid, or a nonnumeric value, you should use an appropriate macro, such as [CMTIME_IS_INVALID](https://developer.apple.com/documentation/coremedia/cmtime_is_invalid), [CMTIME_IS_POSITIVE_INFINITY](https://developer.apple.com/documentation/coremedia/cmtime_is_positive_infinity), or [CMTIME_IS_INDEFINITE](https://developer.apple.com/documentation/coremedia/cmtime_is_indefinite).

```
CMTime myTime = <#Get a CMTime#>;
if (CMTIME_IS_INVALID(myTime)) {
    // Perhaps treat this as an error; display a suitable alert to the user.
}
```

You should not compare the value of an arbitrary `CMTime` structure with `kCMTimeInvalid`.

If you need to use `CMTime` structures in annotations or Core Foundation containers, you can convert a `CMTime` structure to and from a `CFDictionary` opaque type (see [CFDictionaryRef](https://developer.apple.com/documentation/corefoundation/cfdictionaryref)) using the [CMTimeCopyAsDictionary](https://developer.apple.com/documentation/coremedia/1400845-cmtimecopyasdictionary) and [CMTimeMakeFromDictionary](https://developer.apple.com/documentation/coremedia/1400819-cmtimemakefromdictionary) functions, respectively. You can also get a string representation of a `CMTime` structure using the [CMTimeCopyDescription](https://developer.apple.com/documentation/coremedia/1400791-cmtimecopydescription) function.

The epoch number of a `CMTime` structure is usually set to 0, but you can use it to distinguish unrelated timelines. For example, the epoch could be incremented through each cycle using a presentation loop, to differentiate between time `N` in loop 0 and time `N` in loop 1.

[CMTimeRange](https://developer.apple.com/documentation/coremedia/cmtimerange) is a C structure that has a start time and duration, both expressed as `CMTime` structures. A time range does not include the time that is the start time plus the duration.

You create a time range using [CMTimeRangeMake](https://developer.apple.com/documentation/coremedia/1462785-cmtimerangemake) or [CMTimeRangeFromTimeToTime](https://developer.apple.com/documentation/coremedia/1462817-cmtimerangefromtimetotime). There are constraints on the value of the `CMTime` epochs:

- `CMTimeRange` structures cannot span different epochs.
- The epoch in a `CMTime` structure that represents a timestamp may be nonzero, but you can only perform range operations (such as [CMTimeRangeGetUnion](https://developer.apple.com/documentation/coremedia/1462837-cmtimerangegetunion)) on ranges whose start fields have the same epoch.
- The epoch in a `CMTime` structure that represents a duration should always be 0, and the value must be nonnegative.

Core Media provides functions you can use to determine whether a time range contains a given time or other time range, to determine whether two time ranges are equal, and to calculate unions and intersections of time ranges, such as [CMTimeRangeContainsTime](https://developer.apple.com/documentation/coremedia/1462775-cmtimerangecontainstime), [CMTimeRangeEqual](https://developer.apple.com/documentation/coremedia/1462841-cmtimerangeequal), [CMTimeRangeContainsTimeRange](https://developer.apple.com/documentation/coremedia/1462830-cmtimerangecontainstimerange), and [CMTimeRangeGetUnion](https://developer.apple.com/documentation/coremedia/1462837-cmtimerangegetunion).

Given that a time range does not include the time that is the start time plus the duration, the following expression always evaluates to false:

```
CMTimeRangeContainsTime(range, CMTimeRangeGetEnd(range))
```

For a list of all the available functions, see _[CMTimeRange Reference](https://developer.apple.com/documentation/coremedia/cmtimerange-qts)_.

Core Media provides constants for a zero-length range and an invalid range, [kCMTimeRangeZero](https://developer.apple.com/documentation/coremedia/kcmtimerangezero) and [kCMTimeRangeInvalid](https://developer.apple.com/documentation/coremedia/kcmtimerangeinvalid), respectively. There are many ways, though in which a `CMTimeRange` structure can be invalid, or zero—or indefinite (if one of the `CMTime` structures is indefinite. If you need to test whether a `CMTimeRange` structure is valid, zero, or indefinite, you should use an appropriate macro: [CMTIMERANGE_IS_VALID](https://developer.apple.com/documentation/coremedia/cmtimerange_is_valid), [CMTIMERANGE_IS_INVALID](https://developer.apple.com/documentation/coremedia/cmtimerange_is_invalid), [CMTIMERANGE_IS_EMPTY](https://developer.apple.com/documentation/coremedia/cmtimerange_is_empty), or [CMTIMERANGE_IS_EMPTY](https://developer.apple.com/documentation/coremedia/cmtimerange_is_empty).

```
CMTimeRange myTimeRange = <#Get a CMTimeRange#>;
if (CMTIMERANGE_IS_EMPTY(myTimeRange)) {
    // The time range is zero.
}
```

You should not compare the value of an arbitrary `CMTimeRange` structure with `kCMTimeRangeInvalid`.

If you need to use `CMTimeRange` structures in annotations or Core Foundation containers, you can convert a `CMTimeRange` structure to and from a `CFDictionary` opaque type (see [CFDictionaryRef](https://developer.apple.com/documentation/corefoundation/cfdictionaryref)) using [CMTimeRangeCopyAsDictionary](https://developer.apple.com/documentation/coremedia/1462781-cmtimerangecopyasdictionary) and [CMTimeRangeMakeFromDictionary](https://developer.apple.com/documentation/coremedia/1462777-cmtimerangemakefromdictionary), respectively. You can also get a string representation of a `CMTime` structure using the [CMTimeRangeCopyDescription](https://developer.apple.com/documentation/coremedia/1462823-cmtimerangecopydescription) function.

Video data and its associated metadata are represented in AV Foundation by opaque objects from the Core Media framework. Core Media represents video data using `CMSampleBuffer` (see [CMSampleBufferRef](https://developer.apple.com/documentation/coremedia/cmsamplebuffer)). `CMSampleBuffer` is a Core Foundation-style opaque type; an instance contains the sample buffer for a frame of video data as a Core Video pixel buffer (see [CVPixelBufferRef](https://developer.apple.com/documentation/corevideo/cvpixelbuffer)). You access the pixel buffer from a sample buffer using [CMSampleBufferGetImageBuffer](https://developer.apple.com/documentation/coremedia/1489236-cmsamplebuffergetimagebuffer):

```
CVPixelBufferRef pixelBuffer = CMSampleBufferGetImageBuffer(<#A CMSampleBuffer#>);
```

From the pixel buffer, you can access the actual video data. For an example, see [Converting CMSampleBuffer to a UIImage Object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcobyfvbuqmrnknlti).

In addition to the video data, you can retrieve a number of other aspects of the video frame:

- __Timing information__. You get accurate timestamps for both the original presentation time and the decode time using [CMSampleBufferGetPresentationTimeStamp](https://developer.apple.com/documentation/coremedia/1489252-cmsamplebuffergetpresentationtim) and [CMSampleBufferGetDecodeTimeStamp](https://developer.apple.com/documentation/coremedia/1489404-cmsamplebuffergetdecodetimestamp) respectively.
- __Format information__. The format information is encapsulated in a CMFormatDescription object (see [CMFormatDescriptionRef](https://developer.apple.com/documentation/coremedia/cmformatdescriptionref)). From the format description, you can get for example the pixel type and video dimensions using `CMVideoFormatDescriptionGetCodecType` and [CMVideoFormatDescriptionGetDimensions](https://developer.apple.com/documentation/coremedia/1489287-cmvideoformatdescriptiongetdimen) respectively.
- __Metadata__. Metadata are stored in a dictionary as an _attachment_. You use [CMGetAttachment](https://developer.apple.com/documentation/coremedia/1470707-cmgetattachment) to retrieve the dictionary:

```
CMSampleBufferRef sampleBuffer = <#Get a sample buffer#>;
CFDictionaryRef metadataDictionary =
    CMGetAttachment(sampleBuffer, CFSTR("MetadataDictionary", NULL);
if (metadataDictionary) {
    // Do something with the metadata.
}
```


The following code shows how you can convert a `CMSampleBuffer` to a `UIImage` object. You should consider your requirements carefully before using it. Performing the conversion is a comparatively expensive operation. It is appropriate to, for example, create a still image from a frame of video data taken every second or so. You should not use this as a means to manipulate every frame of video coming from a capture device in real time.

```objc
// Create a UIImage from sample buffer data
- (UIImage *) imageFromSampleBuffer:(CMSampleBufferRef) sampleBuffer
{
    // Get a CMSampleBuffer's Core Video image buffer for the media data
    CVImageBufferRef imageBuffer = CMSampleBufferGetImageBuffer(sampleBuffer);
    // Lock the base address of the pixel buffer
    CVPixelBufferLockBaseAddress(imageBuffer, 0);

    // Get the number of bytes per row for the pixel buffer
    void *baseAddress = CVPixelBufferGetBaseAddress(imageBuffer);

    // Get the number of bytes per row for the pixel buffer
    size_t bytesPerRow = CVPixelBufferGetBytesPerRow(imageBuffer);
    // Get the pixel buffer width and height
    size_t width = CVPixelBufferGetWidth(imageBuffer);
    size_t height = CVPixelBufferGetHeight(imageBuffer);

    // Create a device-dependent RGB color space
    CGColorSpaceRef colorSpace = CGColorSpaceCreateDeviceRGB();

    // Create a bitmap graphics context with the sample buffer data
    CGContextRef context = CGBitmapContextCreate(baseAddress, width, height, 8,
      bytesPerRow, colorSpace, kCGBitmapByteOrder32Little | kCGImageAlphaPremultipliedFirst);
    // Create a Quartz image from the pixel data in the bitmap graphics context
    CGImageRef quartzImage = CGBitmapContextCreateImage(context);
    // Unlock the pixel buffer
    CVPixelBufferUnlockBaseAddress(imageBuffer,0);

    // Free up the context and color space
    CGContextRelease(context);
    CGColorSpaceRelease(colorSpace);

    // Create an image object from the Quartz image
    UIImage *image = [UIImage imageWithCGImage:quartzImage];

    // Release the Quartz image
    CGImageRelease(quartzImage);

    return (image);
}
```

[Next](Document%20Revision%20History.md)[Previous](Export.md)

