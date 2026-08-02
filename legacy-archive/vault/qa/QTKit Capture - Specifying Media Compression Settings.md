---
title: QTKit Capture - Specifying Media Compression Settings
apple_id: DTS10004614
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QTKit
published: '2009-10-09'
source_url: https://developer.apple.com/library/archive/qa/qa1586/_index.html
archived_at: '2026-07-18T02:32:20.051153Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1586

# QTKit Capture - Specifying Media Compression Settings

## Q:  How can I compress media being captured to a movie file when using the `QTCaptureMovieFileOutput` object?

A: How can I compress media being captured to a movie file when using the `QTCaptureMovieFileOutput` object?

`QTCaptureMovieFileOutput` is the concrete subclass of the `QTCaptureFileOutput` object that writes media to QuickTime movie files (.mov) and represents the output destination for a `QTCaptureSession`.

The method responsible for configuring media compression settings for the `QTCaptureMovieFileOutput` object is named conveniently enough `setCompressionOptions:forConnection:`. This method accepts a `QTCompressionOptions` object (the object encapsulating preset compression settings) and a `QTCaptureConnection` object for the media being captured.

When calling `setCompressionOptions:forConnection:`, a `QTCaptureConnection` object is retrieved by sending the message `connections` to an instance of `QTCaptureMovieFileOutput`. This method is inherited from `QTCaptureOutput` and is used to retrieve `QTCaptureConnection` instances representing individual media streams.


```objc
- (void)setCompressionOptions:(QTCompressionOptions *)compressionOptions                  forConnection:(QTCaptureConnection *)connection  Description:  Sets the options the receiver uses to compress media on the given connection as it is being captured.  Parameters:  compressionOptionscompressionOptions - A QTCompressionOptions object detailing the options being used to compress captured media, or nil if the media should not be compressed.  connection - The QTCaptureConnection connection containing the media to be compressed.  Discussion:  This method sets the options for compressing media as it is being captured. If compression cannot be performed in real time, the receiver will drop frames in order to remain synchronized with the session. If the receiver does not recompress the output media, this method should be passed nil. The default value is nil.
```

To configure an instance of a `QTCaptureMovieFileOutput` object to compress the captured media, first create a `QTCompressionOptions` instance specifying how you would like the media compressed (using one of the preset identifiers below), then simply call `setCompressionOptions:forConnection:` passing in the initialized `QTCompressionOptions` instance and the `QTCaptureConnection` for the media stream to be compressed.

__Listing 1__  Setting compression options for Video.

```
QTCaptureSession            *mCaptureSession; QTCaptureDeviceInput        *mCaptureDeviceInput; QTCaptureMovieFileOutput    *mCaptureMovieFileOutput; NSError *error;  ...  mCaptureSession = [[QTCaptureSession alloc] init];  // find a video device and add it to the session QTCaptureDevice *device = [QTCaptureDevice defaultInputDeviceWithMediaType:QTMediaTypeVideo]; if (device) [device open:&error];  mCaptureDeviceInput = [[QTCaptureDeviceInput alloc] initWithDevice:device]; [mCaptureSession addInput:mCaptureDeviceInput error:&error];  // create the movie file output and add it to the session mCaptureMovieFileOutput = [[QTCaptureMovieFileOutput alloc] init]; [mCaptureSession addOutput:mCaptureMovieFileOutput error:&error];  // set the compression options for the movie file output QTCaptureConnection *connection  = [[mCaptureMovieFileOutput connections] lastObject]; QTCompressionOptions *compressionOptions = [QTCompressionOptions                                              compressionOptionsWithIdentifier:                                             @"QTCompressionOptionsSD480SizeH264Video"];  [mCaptureMovieFileOutput setCompressionOptions:compressionOptions forConnection:connection];  ...
```


__Listing 2__  Setting compression options for Audio and Video.

```
...  NSEnumerator *connectionEnumerator = [[mCaptureMovieFileOutput connections] objectEnumerator]; QTCaptureConnection *connection;  // iterate over each output connection for the capture session and specify the desired compression while ((connection = [connectionEnumerator nextObject])) {     NSString *mediaType = [connection mediaType];     QTCompressionOptions *compressionOptions = nil;      // specify the compression options according to the media type     // (note: a list of other valid compression types can be found in the     // QTCompressionOptions.h interface file)     if ([mediaType isEqualToString:QTMediaTypeVideo]) {         // use H.264         compressionOptions = [QTCompressionOptions                                 compressionOptionsWithIdentifier:@"QTCompressionOptions240SizeH264Video"];     } else if ([mediaType isEqualToString:QTMediaTypeSound]) {         // use AAC Audio         compressionOptions = [QTCompressionOptions                                compressionOptionsWithIdentifier:@"QTCompressionOptionsHighQualityAACAudio"];     }      // set the compression options for the movie file output     [mCaptureMovieFileOutput setCompressionOptions:compressionOptions forConnection:connection]; }  ...
```

A `QTCompressionOptions` object can be created with any of the following identifiers, each representing a set of options that determine how media will be compressed.


```
Video compression options identifiers ( QTMediaTypeVideo ):  These compression options are appropriate for high quality intermediate video that requires further processing.      QTCompressionOptionsLosslessAppleIntermediateVideo     QTCompressionOptionsLosslessAnimationVideo     QTCompressionOptionsJPEGVideo  These compression options are appropriate for medium and low quality video that will be used for delivery to destinations such as the internet.      QTCompressionOptions120SizeH264Video     QTCompressionOptions240SizeH264Video     QTCompressionOptionsSD480SizeH264Video     QTCompressionOptions120SizeMPEG4Video     QTCompressionOptions240SizeMPEG4Video     QTCompressionOptionsSD480SizeMPEG4Video
```



```
Audio compression options identifiers ( QTMediaTypeSound ):  This compression option is appropriate for lossless audio that requires further processing, or is intended for high fidelity destinations.      QTCompressionOptionsLosslessALACAudio  These compression options are appropriate for audio delivered with lossy compression.  For music and other high quality audio.      QTCompressionOptionsHighQualityAACAudio  For voice recordings.      QTCompressionOptionsVoiceQualityAACAudio
```

If a codec required by a specific compression option in not installed, calling `compressionOptionsWithIdentifier:` will return `nil` and the identifier will not be included in the array returned by `compressionOptionsIdentifiersForMediaType:`. For example, the `QTCompressionOptionsLosslessAppleIntermediateVideo` identifier requires that the Apple Intermediate Codec is installed on the system.

- [QTKit Capture Guide](https://developer.apple.com/mac/library/documentation/Cocoa/Conceptual/QTKitApplicationProgrammingGuide/UsingQTKit/UsingQTKit.html#//apple_ref/doc/uid/TP40008156-CH108-SW9)
- [Technical Note TN2219, 'Managing QTCompressionOptions - An overview of the QTCompressionOptionsWindow sample'](https://developer.apple.com/technotes/tn2008/tn2219.html)
- [QTCompressionOptionsWindow Sample Code](https://developer.apple.com/samplecode/QTCompressionOptionsWindow/index.html)
- [MyRecorder Sample](https://developer.apple.com/samplecode/MYRecorder/index.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-10-09 | Editorial |
| 2008-03-11 | Editorial |
| 2008-02-13 | New document that describes how to configure a file output object to save compressed captured media. |

