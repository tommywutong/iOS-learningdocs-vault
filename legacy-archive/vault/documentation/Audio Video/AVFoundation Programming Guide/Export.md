---
title: AVFoundation Programming Guide
apple_id: TP40010188
resource_type: Guide
platform: tvOS|iOS|macOS
topic: null
technology: AVFoundation
published: '2015-06-30'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/AVFoundationPG/Articles/05_Export.html
archived_at: '2026-07-15T05:21:00.204042Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AVFoundation Programming Guide](About%20AVFoundation.md)


[Next](Time%20and%20Media%20Representations.md)[Previous](Still%20and%20Video%20Media%20Capture.md)

# Export

To read and write audiovisual assets, you must use the export APIs provided by the AVFoundation framework. The [AVAssetExportSession](https://developer.apple.com/documentation/avfoundation/avassetexportsession) class provides an interface for simple exporting needs, such as modifying the file format or trimming the length of an asset (see [Trimming and Transcoding a Movie](Using%20Assets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcobyfvbuqnznknltq)). For more in-depth exporting needs, use the [AVAssetReader](https://developer.apple.com/documentation/avfoundation/avassetreader) and [AVAssetWriter](https://developer.apple.com/documentation/avfoundation/avassetwriter) classes.

Use an `AVAssetReader` when you want to perform an operation on the contents of an asset. For example, you might read the audio track of an asset to produce a visual representation of the waveform. To produce an asset from media such as sample buffers or still images, use an `AVAssetWriter` object.

Each `AVAssetReader` object can be associated only with a single asset at a time, but this asset may contain multiple tracks. For this reason, you must assign concrete subclasses of the [AVAssetReaderOutput](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput) class to your asset reader before you begin reading in order to configure how the media data is read. There are three concrete subclasses of the `AVAssetReaderOutput` base class that you can use for your asset reading needs: [AVAssetReaderTrackOutput](https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput), [AVAssetReaderAudioMixOutput](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput), and [AVAssetReaderVideoCompositionOutput](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput).

All you need to initialize an `AVAssetReader` object is the asset that you want to read.

```
NSError *outError;
AVAsset *someAsset = <#AVAsset that you want to read#>;
AVAssetReader *assetReader = [AVAssetReader assetReaderWithAsset:someAsset error:&outError];
BOOL success = (assetReader != nil);
```


After you have created your asset reader, set up at least one output to receive the media data being read. When setting up your outputs, be sure to set the [alwaysCopiesSampleData](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/1389189-alwayscopiessampledata) property to `NO`. In this way, you reap the benefits of performance improvements. In all of the examples within this chapter, this property could and should be set to `NO`.

If you want only to read media data from one or more tracks and potentially convert that data to a different format, use the `AVAssetReaderTrackOutput` class, using a single track output object for each [AVAssetTrack](https://developer.apple.com/documentation/avfoundation/avassettrack) object that you want to read from your asset. To decompress an audio track to Linear PCM with an asset reader, you set up your track output as follows:

```
AVAsset *localAsset = assetReader.asset;
// Get the audio track to read.
AVAssetTrack *audioTrack = [[localAsset tracksWithMediaType:AVMediaTypeAudio] objectAtIndex:0];
// Decompression settings for Linear PCM
NSDictionary *decompressionAudioSettings = @{ AVFormatIDKey : [NSNumber numberWithUnsignedInt:kAudioFormatLinearPCM] };
// Create the output with the audio track and decompression settings.
AVAssetReaderOutput *trackOutput = [AVAssetReaderTrackOutput assetReaderTrackOutputWithTrack:audioTrack outputSettings:decompressionAudioSettings];
// Add the output to the reader if possible.
if ([assetReader canAddOutput:trackOutput])
    [assetReader addOutput:trackOutput];
```

You use the `AVAssetReaderAudioMixOutput` and `AVAssetReaderVideoCompositionOutput` classes to read media data that has been mixed or composited together using an [AVAudioMix](https://developer.apple.com/documentation/avfoundation/avaudiomix) object or [AVVideoComposition](https://developer.apple.com/documentation/avfoundation/avvideocomposition) object, respectively. Typically, these outputs are used when your asset reader is reading from an [AVComposition](https://developer.apple.com/documentation/avfoundation/avcomposition) object.

With a single audio mix output, you can read multiple audio tracks from your asset that have been mixed together using an `AVAudioMix` object. To specify how the audio tracks are mixed, assign the mix to the `AVAssetReaderAudioMixOutput` object after initialization. The following code displays how to create an audio mix output with all of the audio tracks from your asset, decompress the audio tracks to Linear PCM, and assign an audio mix object to the output. For details on how to configure an audio mix, see [Editing](Editing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcobyfvbuqobnknltc).

```
AVAudioMix *audioMix = <#An AVAudioMix that specifies how the audio tracks from the AVAsset are mixed#>;
// Assumes that assetReader was initialized with an AVComposition object.
AVComposition *composition = (AVComposition *)assetReader.asset;
// Get the audio tracks to read.
NSArray *audioTracks = [composition tracksWithMediaType:AVMediaTypeAudio];
// Get the decompression settings for Linear PCM.
NSDictionary *decompressionAudioSettings = @{ AVFormatIDKey : [NSNumber numberWithUnsignedInt:kAudioFormatLinearPCM] };
// Create the audio mix output with the audio tracks and decompression setttings.
AVAssetReaderOutput *audioMixOutput = [AVAssetReaderAudioMixOutput assetReaderAudioMixOutputWithAudioTracks:audioTracks audioSettings:decompressionAudioSettings];
// Associate the audio mix used to mix the audio tracks being read with the output.
audioMixOutput.audioMix = audioMix;
// Add the output to the reader if possible.
if ([assetReader canAddOutput:audioMixOutput])
    [assetReader addOutput:audioMixOutput];
```

The video composition output behaves in much the same way: You can read multiple video tracks from your asset that have been composited together using an `AVVideoComposition` object. To read the media data from multiple composited video tracks and decompress it to ARGB, set up your output as follows:

```
AVVideoComposition *videoComposition = <#An AVVideoComposition that specifies how the video tracks from the AVAsset are composited#>;
// Assumes assetReader was initialized with an AVComposition.
AVComposition *composition = (AVComposition *)assetReader.asset;
// Get the video tracks to read.
NSArray *videoTracks = [composition tracksWithMediaType:AVMediaTypeVideo];
// Decompression settings for ARGB.
NSDictionary *decompressionVideoSettings = @{ (id)kCVPixelBufferPixelFormatTypeKey : [NSNumber numberWithUnsignedInt:kCVPixelFormatType_32ARGB], (id)kCVPixelBufferIOSurfacePropertiesKey : [NSDictionary dictionary] };
// Create the video composition output with the video tracks and decompression setttings.
AVAssetReaderOutput *videoCompositionOutput = [AVAssetReaderVideoCompositionOutput assetReaderVideoCompositionOutputWithVideoTracks:videoTracks videoSettings:decompressionVideoSettings];
// Associate the video composition used to composite the video tracks being read with the output.
videoCompositionOutput.videoComposition = videoComposition;
// Add the output to the reader if possible.
if ([assetReader canAddOutput:videoCompositionOutput])
    [assetReader addOutput:videoCompositionOutput];
```


To start reading after setting up all of the outputs you need, call the [startReading](https://developer.apple.com/documentation/avfoundation/avassetreader/1390286-startreading) method on your asset reader. Next, retrieve the media data individually from each output using the [copyNextSampleBuffer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/1385732-copynextsamplebuffer) method. To start up an asset reader with a single output and read all of its media samples, do the following:

```
// Start the asset reader up.
[self.assetReader startReading];
BOOL done = NO;
while (!done)
{
  // Copy the next sample buffer from the reader output.
  CMSampleBufferRef sampleBuffer = [self.assetReaderOutput copyNextSampleBuffer];
  if (sampleBuffer)
  {
    // Do something with sampleBuffer here.
    CFRelease(sampleBuffer);
    sampleBuffer = NULL;
  }
  else
  {
    // Find out why the asset reader output couldn't copy another sample buffer.
    if (self.assetReader.status == AVAssetReaderStatusFailed)
    {
      NSError *failureError = self.assetReader.error;
      // Handle the error here.
    }
    else
    {
      // The asset reader output has read all of its samples.
      done = YES;
    }
  }
}
```


The [AVAssetWriter](https://developer.apple.com/documentation/avfoundation/avassetwriter) class to write media data from multiple sources to a single file of a specified file format. You don’t need to associate your asset writer object with a specific asset, but you must use a separate asset writer for each output file that you want to create. Because an asset writer can write media data from multiple sources, you must create an [AVAssetWriterInput](https://developer.apple.com/documentation/avfoundation/avassetwriterinput) object for each individual track that you want to write to the output file. Each `AVAssetWriterInput` object expects to receive data in the form of [CMSampleBufferRef](https://developer.apple.com/documentation/coremedia/cmsamplebuffer) objects, but if you want to append [CVPixelBufferRef](https://developer.apple.com/documentation/corevideo/cvpixelbuffer) objects to your asset writer input, use the [AVAssetWriterInputPixelBufferAdaptor](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor) class.

To create an asset writer, specify the URL for the output file and the desired file type. The following code displays how to initialize an asset writer to create a QuickTime movie:

```
NSError *outError;
NSURL *outputURL = <#NSURL object representing the URL where you want to save the video#>;
AVAssetWriter *assetWriter = [AVAssetWriter assetWriterWithURL:outputURL
                                                      fileType:AVFileTypeQuickTimeMovie
                                                         error:&outError];
BOOL success = (assetWriter != nil);
```


For your asset writer to be able to write media data, you must set up at least one asset writer input. For example, if your source of media data is already vending media samples as `CMSampleBufferRef` objects, just use the `AVAssetWriterInput` class. To set up an asset writer input that compresses audio media data to 128 kbps AAC and connect it to your asset writer, do the following:

```
// Configure the channel layout as stereo.
AudioChannelLayout stereoChannelLayout = {
    .mChannelLayoutTag = kAudioChannelLayoutTag_Stereo,
    .mChannelBitmap = 0,
    .mNumberChannelDescriptions = 0
};

// Convert the channel layout object to an NSData object.
NSData *channelLayoutAsData = [NSData dataWithBytes:&stereoChannelLayout length:offsetof(AudioChannelLayout, mChannelDescriptions)];

// Get the compression settings for 128 kbps AAC.
NSDictionary *compressionAudioSettings = @{
    AVFormatIDKey         : [NSNumber numberWithUnsignedInt:kAudioFormatMPEG4AAC],
    AVEncoderBitRateKey   : [NSNumber numberWithInteger:128000],
    AVSampleRateKey       : [NSNumber numberWithInteger:44100],
    AVChannelLayoutKey    : channelLayoutAsData,
    AVNumberOfChannelsKey : [NSNumber numberWithUnsignedInteger:2]
};

// Create the asset writer input with the compression settings and specify the media type as audio.
AVAssetWriterInput *assetWriterInput = [AVAssetWriterInput assetWriterInputWithMediaType:AVMediaTypeAudio outputSettings:compressionAudioSettings];
// Add the input to the writer if possible.
if ([assetWriter canAddInput:assetWriterInput])
    [assetWriter addInput:assetWriterInput];
```

Your asset writer input can optionally include some metadata or specify a different transform for a particular track using the [metadata](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1386328-metadata) and [transform](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/1390183-transform) properties respectively. For an asset writer input whose data source is a video track, you can maintain the video’s original transform in the output file by doing the following:

```
AVAsset *videoAsset = <#AVAsset with at least one video track#>;
AVAssetTrack *videoAssetTrack = [[videoAsset tracksWithMediaType:AVMediaTypeVideo] objectAtIndex:0];
assetWriterInput.transform = videoAssetTrack.preferredTransform;
```

When writing media data to the output file, sometimes you may want to allocate pixel buffers. To do so, use the `AVAssetWriterInputPixelBufferAdaptor` class. For greatest efficiency, instead of adding pixel buffers that were allocated using a separate pool, use the pixel buffer pool provided by the pixel buffer adaptor. The following code creates a pixel buffer object working in the RGB domain that will use [CGImage](https://developer.apple.com/documentation/uikit/uiimage/1624159-cgimage) objects to create its pixel buffers.

```
NSDictionary *pixelBufferAttributes = @{
     kCVPixelBufferCGImageCompatibilityKey : [NSNumber numberWithBool:YES],
     kCVPixelBufferCGBitmapContextCompatibilityKey : [NSNumber numberWithBool:YES],
     kCVPixelBufferPixelFormatTypeKey : [NSNumber numberWithInt:kCVPixelFormatType_32ARGB]
};
AVAssetWriterInputPixelBufferAdaptor *inputPixelBufferAdaptor = [AVAssetWriterInputPixelBufferAdaptor assetWriterInputPixelBufferAdaptorWithAssetWriterInput:self.assetWriterInput sourcePixelBufferAttributes:pixelBufferAttributes];
```


When you have configured all of the inputs needed for your asset writer, you are ready to begin writing media data. As you did with the asset reader, initiate the writing process with a call to the [startWriting](https://developer.apple.com/documentation/avfoundation/avassetwriter/1386724-startwriting) method. You then need to start a sample-writing session with a call to the [startSessionAtSourceTime:](https://developer.apple.com/documentation/avfoundation/avassetwriter/1389908-startsessionatsourcetime) method. All writing done by an asset writer has to occur within one of these sessions and the time range of each session defines the time range of media data included from within the source. For example, if your source is an asset reader that is supplying media data read from an [AVAsset](https://developer.apple.com/documentation/avfoundation/avasset) object and you don’t want to include media data from the first half of the asset, you would do the following:

```
CMTime halfAssetDuration = CMTimeMultiplyByFloat64(self.asset.duration, 0.5);
[self.assetWriter startSessionAtSourceTime:halfAssetDuration];
//Implementation continues.
```

Normally, to end a writing session you must call the [endSessionAtSourceTime:](https://developer.apple.com/documentation/avfoundation/avassetwriter/1389921-endsession) method. However, if your writing session goes right up to the end of your file, you can end the writing session simply by calling the [finishWriting](https://developer.apple.com/documentation/avfoundation/avassetwriter/1426644-finishwriting) method. To start up an asset writer with a single input and write all of its media data, do the following:

```
// Prepare the asset writer for writing.
[self.assetWriter startWriting];
// Start a sample-writing session.
[self.assetWriter startSessionAtSourceTime:kCMTimeZero];
// Specify the block to execute when the asset writer is ready for media data and the queue to call it on.
[self.assetWriterInput requestMediaDataWhenReadyOnQueue:myInputSerialQueue usingBlock:^{
     while ([self.assetWriterInput isReadyForMoreMediaData])
     {
          // Get the next sample buffer.
          CMSampleBufferRef nextSampleBuffer = [self copyNextSampleBufferToWrite];
          if (nextSampleBuffer)
          {
               // If it exists, append the next sample buffer to the output file.
               [self.assetWriterInput appendSampleBuffer:nextSampleBuffer];
               CFRelease(nextSampleBuffer);
               nextSampleBuffer = nil;
          }
          else
          {
               // Assume that lack of a next sample buffer means the sample buffer source is out of samples and mark the input as finished.
               [self.assetWriterInput markAsFinished];
               break;
          }
     }
}];
```

The `copyNextSampleBufferToWrite` method in the code above is simply a stub. The location of this stub is where you would need to insert some logic to return `CMSampleBufferRef` objects representing the media data that you want to write. One possible source of sample buffers is an asset reader output.

You can use an asset reader and asset writer object in tandem to convert an asset from one representation to another. Using these objects, you have more control over the conversion than you do with an `AVAssetExportSession` object. For example, you can choose which of the tracks you want to be represented in the output file, specify your own output format, or modify the asset during the conversion process. The first step in this process is just to set up your asset reader outputs and asset writer inputs as desired. After your asset reader and writer are fully configured, you start up both of them with calls to the `startReading` and `startWriting` methods, respectively. The following code snippet displays how to use a single asset writer input to write media data supplied by a single asset reader output:

```
NSString *serializationQueueDescription = [NSString stringWithFormat:@"%@ serialization queue", self];

// Create a serialization queue for reading and writing.
dispatch_queue_t serializationQueue = dispatch_queue_create([serializationQueueDescription UTF8String], NULL);

// Specify the block to execute when the asset writer is ready for media data and the queue to call it on.
[self.assetWriterInput requestMediaDataWhenReadyOnQueue:serializationQueue usingBlock:^{
     while ([self.assetWriterInput isReadyForMoreMediaData])
     {
          // Get the asset reader output's next sample buffer.
          CMSampleBufferRef sampleBuffer = [self.assetReaderOutput copyNextSampleBuffer];
          if (sampleBuffer != NULL)
          {
               // If it exists, append this sample buffer to the output file.
               BOOL success = [self.assetWriterInput appendSampleBuffer:sampleBuffer];
               CFRelease(sampleBuffer);
               sampleBuffer = NULL;
               // Check for errors that may have occurred when appending the new sample buffer.
               if (!success && self.assetWriter.status == AVAssetWriterStatusFailed)
               {
                    NSError *failureError = self.assetWriter.error;
                    //Handle the error.
               }
          }
          else
          {
               // If the next sample buffer doesn't exist, find out why the asset reader output couldn't vend another one.
               if (self.assetReader.status == AVAssetReaderStatusFailed)
               {
                    NSError *failureError = self.assetReader.error;
                    //Handle the error here.
               }
               else
               {
                    // The asset reader output must have vended all of its samples. Mark the input as finished.
                    [self.assetWriterInput markAsFinished];
                    break;
               }
          }
     }
}];
```


This brief code example illustrates how to use an asset reader and writer to reencode the first video and audio track of an asset into a new file. It shows how to:

- Use serialization queues to handle the asynchronous nature of reading and writing audiovisual data
- Initialize an asset reader and configure two asset reader outputs, one for audio and one for video
- Initialize an asset writer and configure two asset writer inputs, one for audio and one for video
- Use an asset reader to asynchronously supply media data to an asset writer through two different output/input combinations
- Use a dispatch group to be notified of completion of the reencoding process
- Allow a user to cancel the reencoding process once it has begun

Before you create your asset reader and writer and configure their outputs and inputs, you need to handle some initial setup. The first part of this setup involves creating three separate serialization queues to coordinate the reading and writing process.

```
NSString *serializationQueueDescription = [NSString stringWithFormat:@"%@ serialization queue", self];

// Create the main serialization queue.
self.mainSerializationQueue = dispatch_queue_create([serializationQueueDescription UTF8String], NULL);
NSString *rwAudioSerializationQueueDescription = [NSString stringWithFormat:@"%@ rw audio serialization queue", self];

// Create the serialization queue to use for reading and writing the audio data.
self.rwAudioSerializationQueue = dispatch_queue_create([rwAudioSerializationQueueDescription UTF8String], NULL);
NSString *rwVideoSerializationQueueDescription = [NSString stringWithFormat:@"%@ rw video serialization queue", self];

// Create the serialization queue to use for reading and writing the video data.
self.rwVideoSerializationQueue = dispatch_queue_create([rwVideoSerializationQueueDescription UTF8String], NULL);
```

The main serialization queue is used to coordinate the starting and stopping of the asset reader and writer (perhaps due to cancellation) and the other two serialization queues are used to serialize the reading and writing by each output/input combination with a potential cancellation.

Now that you have some serialization queues, load the tracks of your asset and begin the reencoding process.

```
self.asset = <#AVAsset that you want to reencode#>;
self.cancelled = NO;
self.outputURL = <#NSURL representing desired output URL for file generated by asset writer#>;
// Asynchronously load the tracks of the asset you want to read.
[self.asset loadValuesAsynchronouslyForKeys:@[@"tracks"] completionHandler:^{
     // Once the tracks have finished loading, dispatch the work to the main serialization queue.
     dispatch_async(self.mainSerializationQueue, ^{
          // Due to asynchronous nature, check to see if user has already cancelled.
          if (self.cancelled)
               return;
          BOOL success = YES;
          NSError *localError = nil;
          // Check for success of loading the assets tracks.
          success = ([self.asset statusOfValueForKey:@"tracks" error:&localError] == AVKeyValueStatusLoaded);
          if (success)
          {
               // If the tracks loaded successfully, make sure that no file exists at the output path for the asset writer.
               NSFileManager *fm = [NSFileManager defaultManager];
               NSString *localOutputPath = [self.outputURL path];
               if ([fm fileExistsAtPath:localOutputPath])
                    success = [fm removeItemAtPath:localOutputPath error:&localError];
          }
          if (success)
               success = [self setupAssetReaderAndAssetWriter:&localError];
          if (success)
               success = [self startAssetReaderAndWriter:&localError];
          if (!success)
               [self readingAndWritingDidFinishSuccessfully:success withError:localError];
     });
}];
```

When the track loading process finishes, whether successfully or not, the rest of the work is dispatched to the main serialization queue to ensure that all of this work is serialized with a potential cancellation. Now all that’s left is to implement the cancellation process and the three custom methods at the end of the previous code listing.

The custom `setupAssetReaderAndAssetWriter:` method initializes the reader and writer and configures two output/input combinations, one for an audio track and one for a video track. In this example, the audio is decompressed to Linear PCM using the asset reader and compressed back to 128 kbps AAC using the asset writer. The video is decompressed to YUV using the asset reader and compressed to H.264 using the asset writer.

```objc
- (BOOL)setupAssetReaderAndAssetWriter:(NSError **)outError
{
     // Create and initialize the asset reader.
     self.assetReader = [[AVAssetReader alloc] initWithAsset:self.asset error:outError];
     BOOL success = (self.assetReader != nil);
     if (success)
     {
          // If the asset reader was successfully initialized, do the same for the asset writer.
          self.assetWriter = [[AVAssetWriter alloc] initWithURL:self.outputURL fileType:AVFileTypeQuickTimeMovie error:outError];
          success = (self.assetWriter != nil);
     }

     if (success)
     {
          // If the reader and writer were successfully initialized, grab the audio and video asset tracks that will be used.
          AVAssetTrack *assetAudioTrack = nil, *assetVideoTrack = nil;
          NSArray *audioTracks = [self.asset tracksWithMediaType:AVMediaTypeAudio];
          if ([audioTracks count] > 0)
               assetAudioTrack = [audioTracks objectAtIndex:0];
          NSArray *videoTracks = [self.asset tracksWithMediaType:AVMediaTypeVideo];
          if ([videoTracks count] > 0)
               assetVideoTrack = [videoTracks objectAtIndex:0];

          if (assetAudioTrack)
          {
               // If there is an audio track to read, set the decompression settings to Linear PCM and create the asset reader output.
               NSDictionary *decompressionAudioSettings = @{ AVFormatIDKey : [NSNumber numberWithUnsignedInt:kAudioFormatLinearPCM] };
               self.assetReaderAudioOutput = [AVAssetReaderTrackOutput assetReaderTrackOutputWithTrack:assetAudioTrack outputSettings:decompressionAudioSettings];
               [self.assetReader addOutput:self.assetReaderAudioOutput];
               // Then, set the compression settings to 128kbps AAC and create the asset writer input.
               AudioChannelLayout stereoChannelLayout = {
                    .mChannelLayoutTag = kAudioChannelLayoutTag_Stereo,
                    .mChannelBitmap = 0,
                    .mNumberChannelDescriptions = 0
               };
               NSData *channelLayoutAsData = [NSData dataWithBytes:&stereoChannelLayout length:offsetof(AudioChannelLayout, mChannelDescriptions)];
               NSDictionary *compressionAudioSettings = @{
                    AVFormatIDKey         : [NSNumber numberWithUnsignedInt:kAudioFormatMPEG4AAC],
                    AVEncoderBitRateKey   : [NSNumber numberWithInteger:128000],
                    AVSampleRateKey       : [NSNumber numberWithInteger:44100],
                    AVChannelLayoutKey    : channelLayoutAsData,
                    AVNumberOfChannelsKey : [NSNumber numberWithUnsignedInteger:2]
               };
               self.assetWriterAudioInput = [AVAssetWriterInput assetWriterInputWithMediaType:[assetAudioTrack mediaType] outputSettings:compressionAudioSettings];
               [self.assetWriter addInput:self.assetWriterAudioInput];
          }

          if (assetVideoTrack)
          {
               // If there is a video track to read, set the decompression settings for YUV and create the asset reader output.
               NSDictionary *decompressionVideoSettings = @{
                    (id)kCVPixelBufferPixelFormatTypeKey     : [NSNumber numberWithUnsignedInt:kCVPixelFormatType_422YpCbCr8],
                    (id)kCVPixelBufferIOSurfacePropertiesKey : [NSDictionary dictionary]
               };
               self.assetReaderVideoOutput = [AVAssetReaderTrackOutput assetReaderTrackOutputWithTrack:assetVideoTrack outputSettings:decompressionVideoSettings];
               [self.assetReader addOutput:self.assetReaderVideoOutput];
               CMFormatDescriptionRef formatDescription = NULL;
               // Grab the video format descriptions from the video track and grab the first one if it exists.
               NSArray *videoFormatDescriptions = [assetVideoTrack formatDescriptions];
               if ([videoFormatDescriptions count] > 0)
                    formatDescription = (__bridge CMFormatDescriptionRef)[formatDescriptions objectAtIndex:0];
               CGSize trackDimensions = {
                    .width = 0.0,
                    .height = 0.0,
               };
               // If the video track had a format description, grab the track dimensions from there. Otherwise, grab them direcly from the track itself.
               if (formatDescription)
                    trackDimensions = CMVideoFormatDescriptionGetPresentationDimensions(formatDescription, false, false);
               else
                    trackDimensions = [assetVideoTrack naturalSize];
               NSDictionary *compressionSettings = nil;
               // If the video track had a format description, attempt to grab the clean aperture settings and pixel aspect ratio used by the video.
               if (formatDescription)
               {
                    NSDictionary *cleanAperture = nil;
                    NSDictionary *pixelAspectRatio = nil;
                    CFDictionaryRef cleanApertureFromCMFormatDescription = CMFormatDescriptionGetExtension(formatDescription, kCMFormatDescriptionExtension_CleanAperture);
                    if (cleanApertureFromCMFormatDescription)
                    {
                         cleanAperture = @{
                              AVVideoCleanApertureWidthKey            : (id)CFDictionaryGetValue(cleanApertureFromCMFormatDescription, kCMFormatDescriptionKey_CleanApertureWidth),
                              AVVideoCleanApertureHeightKey           : (id)CFDictionaryGetValue(cleanApertureFromCMFormatDescription, kCMFormatDescriptionKey_CleanApertureHeight),
                              AVVideoCleanApertureHorizontalOffsetKey : (id)CFDictionaryGetValue(cleanApertureFromCMFormatDescription, kCMFormatDescriptionKey_CleanApertureHorizontalOffset),
                              AVVideoCleanApertureVerticalOffsetKey   : (id)CFDictionaryGetValue(cleanApertureFromCMFormatDescription, kCMFormatDescriptionKey_CleanApertureVerticalOffset)
                         };
                    }
                    CFDictionaryRef pixelAspectRatioFromCMFormatDescription = CMFormatDescriptionGetExtension(formatDescription, kCMFormatDescriptionExtension_PixelAspectRatio);
                    if (pixelAspectRatioFromCMFormatDescription)
                    {
                         pixelAspectRatio = @{
                              AVVideoPixelAspectRatioHorizontalSpacingKey : (id)CFDictionaryGetValue(pixelAspectRatioFromCMFormatDescription, kCMFormatDescriptionKey_PixelAspectRatioHorizontalSpacing),
                              AVVideoPixelAspectRatioVerticalSpacingKey   : (id)CFDictionaryGetValue(pixelAspectRatioFromCMFormatDescription, kCMFormatDescriptionKey_PixelAspectRatioVerticalSpacing)
                         };
                    }
                    // Add whichever settings we could grab from the format description to the compression settings dictionary.
                    if (cleanAperture || pixelAspectRatio)
                    {
                         NSMutableDictionary *mutableCompressionSettings = [NSMutableDictionary dictionary];
                         if (cleanAperture)
                              [mutableCompressionSettings setObject:cleanAperture forKey:AVVideoCleanApertureKey];
                         if (pixelAspectRatio)
                              [mutableCompressionSettings setObject:pixelAspectRatio forKey:AVVideoPixelAspectRatioKey];
                         compressionSettings = mutableCompressionSettings;
                    }
               }
               // Create the video settings dictionary for H.264.
               NSMutableDictionary *videoSettings = (NSMutableDictionary *) @{
                    AVVideoCodecKey  : AVVideoCodecH264,
                    AVVideoWidthKey  : [NSNumber numberWithDouble:trackDimensions.width],
                    AVVideoHeightKey : [NSNumber numberWithDouble:trackDimensions.height]
               };
               // Put the compression settings into the video settings dictionary if we were able to grab them.
               if (compressionSettings)
                    [videoSettings setObject:compressionSettings forKey:AVVideoCompressionPropertiesKey];
               // Create the asset writer input and add it to the asset writer.
               self.assetWriterVideoInput = [AVAssetWriterInput assetWriterInputWithMediaType:[videoTrack mediaType] outputSettings:videoSettings];
               [self.assetWriter addInput:self.assetWriterVideoInput];
          }
     }
     return success;
}
```


Provided that the asset reader and writer are successfully initialized and configured, the `startAssetReaderAndWriter:` method described in [Handling the Initial Setup](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcobyfvbuqojnknltc) is called. This method is where the actual reading and writing of the asset takes place.

```objc
- (BOOL)startAssetReaderAndWriter:(NSError **)outError
{
     BOOL success = YES;
     // Attempt to start the asset reader.
     success = [self.assetReader startReading];
     if (!success)
          *outError = [self.assetReader error];
     if (success)
     {
          // If the reader started successfully, attempt to start the asset writer.
          success = [self.assetWriter startWriting];
          if (!success)
               *outError = [self.assetWriter error];
     }

     if (success)
     {
          // If the asset reader and writer both started successfully, create the dispatch group where the reencoding will take place and start a sample-writing session.
          self.dispatchGroup = dispatch_group_create();
          [self.assetWriter startSessionAtSourceTime:kCMTimeZero];
          self.audioFinished = NO;
          self.videoFinished = NO;

          if (self.assetWriterAudioInput)
          {
               // If there is audio to reencode, enter the dispatch group before beginning the work.
               dispatch_group_enter(self.dispatchGroup);
               // Specify the block to execute when the asset writer is ready for audio media data, and specify the queue to call it on.
               [self.assetWriterAudioInput requestMediaDataWhenReadyOnQueue:self.rwAudioSerializationQueue usingBlock:^{
                    // Because the block is called asynchronously, check to see whether its task is complete.
                    if (self.audioFinished)
                         return;
                    BOOL completedOrFailed = NO;
                    // If the task isn't complete yet, make sure that the input is actually ready for more media data.
                    while ([self.assetWriterAudioInput isReadyForMoreMediaData] && !completedOrFailed)
                    {
                         // Get the next audio sample buffer, and append it to the output file.
                         CMSampleBufferRef sampleBuffer = [self.assetReaderAudioOutput copyNextSampleBuffer];
                         if (sampleBuffer != NULL)
                         {
                              BOOL success = [self.assetWriterAudioInput appendSampleBuffer:sampleBuffer];
                              CFRelease(sampleBuffer);
                              sampleBuffer = NULL;
                              completedOrFailed = !success;
                         }
                         else
                         {
                              completedOrFailed = YES;
                         }
                    }
                    if (completedOrFailed)
                    {
                         // Mark the input as finished, but only if we haven't already done so, and then leave the dispatch group (since the audio work has finished).
                         BOOL oldFinished = self.audioFinished;
                         self.audioFinished = YES;
                         if (oldFinished == NO)
                         {
                              [self.assetWriterAudioInput markAsFinished];
                         }
                         dispatch_group_leave(self.dispatchGroup);
                    }
               }];
          }

          if (self.assetWriterVideoInput)
          {
               // If we had video to reencode, enter the dispatch group before beginning the work.
               dispatch_group_enter(self.dispatchGroup);
               // Specify the block to execute when the asset writer is ready for video media data, and specify the queue to call it on.
               [self.assetWriterVideoInput requestMediaDataWhenReadyOnQueue:self.rwVideoSerializationQueue usingBlock:^{
                    // Because the block is called asynchronously, check to see whether its task is complete.
                    if (self.videoFinished)
                         return;
                    BOOL completedOrFailed = NO;
                    // If the task isn't complete yet, make sure that the input is actually ready for more media data.
                    while ([self.assetWriterVideoInput isReadyForMoreMediaData] && !completedOrFailed)
                    {
                         // Get the next video sample buffer, and append it to the output file.
                         CMSampleBufferRef sampleBuffer = [self.assetReaderVideoOutput copyNextSampleBuffer];
                         if (sampleBuffer != NULL)
                         {
                              BOOL success = [self.assetWriterVideoInput appendSampleBuffer:sampleBuffer];
                              CFRelease(sampleBuffer);
                              sampleBuffer = NULL;
                              completedOrFailed = !success;
                         }
                         else
                         {
                              completedOrFailed = YES;
                         }
                    }
                    if (completedOrFailed)
                    {
                         // Mark the input as finished, but only if we haven't already done so, and then leave the dispatch group (since the video work has finished).
                         BOOL oldFinished = self.videoFinished;
                         self.videoFinished = YES;
                         if (oldFinished == NO)
                         {
                              [self.assetWriterVideoInput markAsFinished];
                         }
                         dispatch_group_leave(self.dispatchGroup);
                    }
               }];
          }
          // Set up the notification that the dispatch group will send when the audio and video work have both finished.
          dispatch_group_notify(self.dispatchGroup, self.mainSerializationQueue, ^{
               BOOL finalSuccess = YES;
               NSError *finalError = nil;
               // Check to see if the work has finished due to cancellation.
               if (self.cancelled)
               {
                    // If so, cancel the reader and writer.
                    [self.assetReader cancelReading];
                    [self.assetWriter cancelWriting];
               }
               else
               {
                    // If cancellation didn't occur, first make sure that the asset reader didn't fail.
                    if ([self.assetReader status] == AVAssetReaderStatusFailed)
                    {
                         finalSuccess = NO;
                         finalError = [self.assetReader error];
                    }
                    // If the asset reader didn't fail, attempt to stop the asset writer and check for any errors.
                    if (finalSuccess)
                    {
                         finalSuccess = [self.assetWriter finishWriting];
                         if (!finalSuccess)
                              finalError = [self.assetWriter error];
                    }
               }
               // Call the method to handle completion, and pass in the appropriate parameters to indicate whether reencoding was successful.
               [self readingAndWritingDidFinishSuccessfully:finalSuccess withError:finalError];
          });
     }
     // Return success here to indicate whether the asset reader and writer were started successfully.
     return success;
}
```

During reencoding, the audio and video tracks are asynchronously handled on individual serialization queues to increase the overall performance of the process, but both queues are contained within the same dispatch group. By placing the work for each track within the same dispatch group, the group can send a notification when all of the work is done and the success of the reencoding process can be determined.

To handle the completion of the reading and writing process, the `readingAndWritingDidFinishSuccessfully:` method is called—with parameters indicating whether or not the reencoding completed successfully. If the process didn’t finish successfully, the asset reader and writer are both canceled and any UI related tasks are dispatched to the main queue.

```objc
- (void)readingAndWritingDidFinishSuccessfully:(BOOL)success withError:(NSError *)error
{
     if (!success)
     {
          // If the reencoding process failed, we need to cancel the asset reader and writer.
          [self.assetReader cancelReading];
          [self.assetWriter cancelWriting];
          dispatch_async(dispatch_get_main_queue(), ^{
               // Handle any UI tasks here related to failure.
          });
     }
     else
     {
          // Reencoding was successful, reset booleans.
          self.cancelled = NO;
          self.videoFinished = NO;
          self.audioFinished = NO;
          dispatch_async(dispatch_get_main_queue(), ^{
               // Handle any UI tasks here related to success.
          });
     }
}
```


Using multiple serialization queues, you can allow the user of your app to cancel the reencoding process with ease. On the main serialization queue, messages are asynchronously sent to each of the asset reencoding serialization queues to cancel their reading and writing. When these two serialization queues complete their cancellation, the dispatch group sends a notification to the main serialization queue where the `cancelled` property is set to `YES`. You might associate the `cancel` method from the following code listing with a button on your UI.

```objc
- (void)cancel
{
     // Handle cancellation asynchronously, but serialize it with the main queue.
     dispatch_async(self.mainSerializationQueue, ^{
          // If we had audio data to reencode, we need to cancel the audio work.
          if (self.assetWriterAudioInput)
          {
               // Handle cancellation asynchronously again, but this time serialize it with the audio queue.
               dispatch_async(self.rwAudioSerializationQueue, ^{
                    // Update the Boolean property indicating the task is complete and mark the input as finished if it hasn't already been marked as such.
                    BOOL oldFinished = self.audioFinished;
                    self.audioFinished = YES;
                    if (oldFinished == NO)
                    {
                         [self.assetWriterAudioInput markAsFinished];
                    }
                    // Leave the dispatch group since the audio work is finished now.
                    dispatch_group_leave(self.dispatchGroup);
               });
          }

          if (self.assetWriterVideoInput)
          {
               // Handle cancellation asynchronously again, but this time serialize it with the video queue.
               dispatch_async(self.rwVideoSerializationQueue, ^{
                    // Update the Boolean property indicating the task is complete and mark the input as finished if it hasn't already been marked as such.
                    BOOL oldFinished = self.videoFinished;
                    self.videoFinished = YES;
                    if (oldFinished == NO)
                    {
                         [self.assetWriterVideoInput markAsFinished];
                    }
                    // Leave the dispatch group, since the video work is finished now.
                    dispatch_group_leave(self.dispatchGroup);
               });
          }
          // Set the cancelled Boolean property to YES to cancel any work on the main queue as well.
          self.cancelled = YES;
     });
}
```


The [AVOutputSettingsAssistant](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant) class aids in creating output-settings dictionaries for an asset reader or writer. This makes setup much simpler, especially for high frame rate H264 movies that have a number of specific presets. Listing 5-1 shows an example that uses the output settings assistant to use the settings assistant.

__Listing 5-1__  AVOutputSettingsAssistant sample

```
AVOutputSettingsAssistant *outputSettingsAssistant = [AVOutputSettingsAssistant outputSettingsAssistantWithPreset:<some preset>];
CMFormatDescriptionRef audioFormat = [self getAudioFormat];

if (audioFormat != NULL)
    [outputSettingsAssistant setSourceAudioFormat:(CMAudioFormatDescriptionRef)audioFormat];

CMFormatDescriptionRef videoFormat = [self getVideoFormat];

if (videoFormat != NULL)
    [outputSettingsAssistant setSourceVideoFormat:(CMVideoFormatDescriptionRef)videoFormat];

CMTime assetMinVideoFrameDuration = [self getMinFrameDuration];
CMTime averageFrameDuration = [self getAvgFrameDuration]

[outputSettingsAssistant setSourceVideoAverageFrameDuration:averageFrameDuration];
[outputSettingsAssistant setSourceVideoMinFrameDuration:assetMinVideoFrameDuration];

AVAssetWriter *assetWriter = [AVAssetWriter assetWriterWithURL:<some URL> fileType:[outputSettingsAssistant outputFileType] error:NULL];
AVAssetWriterInput *audioInput = [AVAssetWriterInput assetWriterInputWithMediaType:AVMediaTypeAudio outputSettings:[outputSettingsAssistant audioSettings] sourceFormatHint:audioFormat];
AVAssetWriterInput *videoInput = [AVAssetWriterInput assetWriterInputWithMediaType:AVMediaTypeVideo outputSettings:[outputSettingsAssistant videoSettings] sourceFormatHint:videoFormat];
```

[Next](Time%20and%20Media%20Representations.md)[Previous](Still%20and%20Video%20Media%20Capture.md)

