---
title: Video Decode Acceleration Framework Reference
apple_id: DTS40009798
resource_type: Technical Note
platform: macOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2015-05-28'
source_url: https://developer.apple.com/library/archive/technotes/tn2267/_index.html
archived_at: '2026-07-26T19:54:09.816898Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2267

# Video Decode Acceleration Framework Reference

This reference describes the Video Decode Acceleration framework available on Mac OS X v10.6.3 and later with Mac models equipped with the NVIDIA GeForce 9400M, GeForce 320M, GeForce GT 330M, ATI HD Radeon GFX, Intel HD Graphics and others.

[Overview](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvke4vcbi4yq)[Functions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvke4vcbi4zq)[VDADecoderCreate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvke4vcbi4zs2vseifcekq2pircveq2sivaviri)[VDADecoderDestroy](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvke4vcbi4zs2vseifcekq2pircvercfknkfet2z)[VDADecoderDecode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvke4vcbi4zs2vseifcekq2pircvercfinhuiri)[VDADecoderFlush](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvke4vcbi4zs2vseifcekq2pircversmkvjuq)[Output Callback](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvke4vcbi42a)[Parameters](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvke4vcbi42c2ucbkjau2rkuivjfg)[Discussion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvke4vcbi42c2rcjknbvku2tjfhu4)[Data Types](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvke4vcbi42q)[VDADecoder](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvke4vcbi42s2vseifcekq2pircve)[Constants](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvke4vcbi43a)[Decoder Configuration Keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvcekq2pircugt2oizeuos2flfjq)[Destination Image Buffer Attribute Keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfveu2qkhivbfkrsgivjewrkzkm)[Decode Flags](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvcekq2pircumtcbi5jq)[Flush Flags](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvdeyvktjbdeyqkhkm)[Decode Info Flags](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvcekq2pircustsgj5deyqkhkm)[Result Codes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvke4vcbi43q)[Sample Code](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvke4vcbi44a)[Creating a Decoder](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvke4vcbi44c2q2sivaviskoi5pucx2eivbu6rcfki)[Output Callback](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvke4vcbi44c2t2vkrifkvc7inauytccifbuw)[Decoding A Frame](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvke4vcbi44c2rcfinhuiskoi5pucx2gkjau2rk7)[Reference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvjekrsfkjcu4q2f)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Overview

Framework VideoDecodeAcceleration
Header VDADecoder.h

The Video Decode Acceleration framework is a C programming interface providing low-level access to the H.264 decoding capabilities of compatible GPUs such as the NVIDIA GeForce 9400M, GeForce 320M, GeForce GT 330M, ATI HD Radeon GFX, Intel HD Graphics and others. It is intended for use by advanced developers who specifically need hardware accelerated decode of video frames.

The framework allows you to:

- Create a `VDADecoder` object which functions as the interface to hardware decode resources.
- Provide an output callback to receive a decompressed image buffer once decoding is complete.
- Pass in H.264 compressed video frames, one at a time to a `VDADecoder` object for decode.
- Cancel decompression of all non-decoded frames currently in flight.
- Destroy a `VDADecoder` object releasing hardware resources.

The Video Decode Acceleration framework is available on Mac OS X 10.6.3 and later.

__Important:__ The Video Decode Acceleration framework only decodes video frame data and does not provide video playback or stream parsing capabilities. Using the QTKit `QTMovie` object with `QTMovieOpenForPlaybackAttribute` enabled is the recommended way for applications to automatically access GPU accelerated playback of H.264 encoded media.

__Important:__ The availability of H.264 accelerated decode varies according to Mac model and Mac OS X version. Developers should always test for the availability of accelerated decode and have an alternative software decode path when hardware resources are not available.

[Back to Top](#)

## Functions

### VDADecoderCreate

Creates a new `VDADecoder` object.

```
OSStatus VDADecoderCreate(CFDictionaryRef           decoderConfiguration,
                          CFDictionaryRef           destinationImageBufferAttributes,
                          VDADecoderOutputCallback  *outputCallback,
                          void                      *decoderOutputCallbackRefcon,
                          VDADecoder                *decoderOut)
```

#### Parameters

- `decoderConfiguration` - A `CFDictionaryRef` containing `kVDADecoderConfiguratioXXX` keys describing the source data and configuration for the decoder. See [Decoder Configuration Keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvcekq2pircugt2oizeuos2flfjq).
- `destinationImageBufferAttributes`- A `CFDictionaryRef` describing the clients requirements for output image buffers. This parameter may be `NULL` if the client has no specific preference for the format of the output image buffers. If `NULL` is used, the client should make no assumptions regarding the returned image buffers. See [Destination Image Buffer Attribute Keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfveu2qkhivbfkrsgivjewrkzkm).
- `outputCallback`- A `VDADecoderOutputCallback` function called by the decoder when returning decompressed image buffers to the client.
- `decoderOutputCallbackRefcon` - A pointer to user data passed to the output callback for all frames from this decoder object.
- `decoderOut` - On output, the newly created decoder object.

#### Discussion

Creates an interface for utilizing hardware resources to decode video by returning a `VDADecoder` object. If hardware doesn't exist to decode the provided format or if there are insufficient hardware resources to perform hardware decoding, the appropriate result code will be returned.

Decoded frames are emitted via the `VDADecoderOutputCallback` function passed in by the caller.

__Note:__ Clients performing format-specific processing or rendering may have specific image buffer format preferences. In this case, the client should specify these preferences by using the `destinationImageBufferAttributes` dictionary.

`CVPixelBufferGetPixelFormatType` may be used to verify the pixel format of the returned image buffers to ensure the image buffer contains the format you are prepared to handle. It is good practice to verify the image buffer format before doing any format-specific processing.

__Important:__ The decoder object is using shared hardware resources across the system. When decompression services are no longer required, the client should dispose of the object thereby freeing up resources for other system services or applications.

Since there is no automatic software fallback when using the Video Decode Acceleration framework or an implicit guarantee that you will be able to access hardware accelerated decode (even on supported configurations), the client will need to respond accordingly if the attempt to create a decoder object fails and provide its own fallback strategy.

#### Return Value

A result code. See [Result Codes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvke4vcbi43q).

### VDADecoderDestroy

Releases the decoder object.

```
OSStatus VDADecoderDestroy(VDADecoder decoder)
```

#### Parameters

- `decoder` - The hardware decoder object being destroyed.

#### Discussion

This call frees the decoder object and releases all resources currently in use by the decoder. All queued frames will be flushed without invoking the output callback. The decoder instance should no longer be referenced after calling `VDADecoderDestroy`.

__Important:__ Image buffers are __NOT__ owned by the decoder instance. Image buffers previously retained by the client will remain valid after the life of the decoder instance and should be released when no longer needed.

#### Return Value

A result code. See [Result Codes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvke4vcbi43q).

### VDADecoderDecode

Send the included compressed data to the hardware decoder object for decoding.

```
OSStatus VDADecoderDecode(VDADecoder      decoder,
                          uint32_t        decodeFlags,
                          CFTypeRef       compressedBuffer,
                          CFDictionaryRef frameInfo)
```

#### Parameters

- `decoder` - The hardware decoder object performing the decode operation.
- `decodeFlags`- Flags containing any special requests for this decode operation. See [Decode Flags](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvcekq2pircumtcbi5jq).
- `compressedBuffer`- A `CFDataRef` containing a single H.264 compressed frame to be decoded.
- `frameInfo` - A `CFDictionaryRef` containing information to be returned in the output callback for this frame. This dictionary can contain client provided information associated with the frame being decoded, for example presentation time. The `CFDictionaryRef` will be retained by the framework.

#### Discussion

This call will send a single H.264 compressed frame packaged as a `CFDataRef` to the hardware decoder object for decoding. The decoded frame is output via the output callback.

#### Return Value

A result code. See [Result Codes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvke4vcbi43q).

### VDADecoderFlush

Flush all frames currently being decoded by the hardware decoder.

```
OSStatus VDADecoderFlush(VDADecoder decoder, uint32_t flushFlags)
```

#### Parameters

- `decoder` - The hardware decoder object performing the decode operation.
- `flushFlags`- Flags controlling flush behavior, for example, whether or not currently in flight decode operations will emit frames. See [Flush Flags](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvdeyvktjbdeyqkhkm).

#### Discussion

Flushing will cancel all currently queued frames which have not been completed. As the hardware decoder is generally running asynchronously, there is the possibility of a frame completing while the call to flush is in progress. No completed frames should be returned after control returns from this call.

The output callback is still called for all flushed frames, but no image buffers will be returned.

If the `kVDADecoderFlush_emitFrames` flag is specified, the flush operation will return image buffers in the output callback.

#### Return Value

A result code. [Result Codes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvke4vcbi43q).

[Back to Top](#)

## Output Callback

Prototype for a callback function invoked when a frame is decoded by calling `VDADecoderDecode`.

```c
typedef void (*VDADecoderOutputCallback)(void             *decompressionOutputRefCon,
                                         CFDictionaryRef  frameInfo,
                                         OSStatus         status,
                                         uint32_t         infoFlags,
                                         CVImageBufferRef imageBuffer)
```

### Parameters

- `decompressionOutputRefCon` - The user data pointer as passed into `VDADecoderCreate` for `decoderOutputCallbackRefcon`.
- `frameInfo`- The `frameInfo` dictionary passed to `VDADecoderDecode` for this frame. The `CFDictionaryRef` will be released after returning from the callback. The client must retain it if it is needed beyond the scope of the output callback.
- `status` - An error code is returned if decompression was not successful. See [Result Codes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvke4vcbi43q).
- `infoFlags` - Contains information about a decode operation. For example, the `kVDADecodeInfo_FrameDropped` flag may be set if the frame was dropped. See [Decode Info Flags](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzzhawugsbrfvcekq2pircustsgj5deyqkhkm).
- `imageBuffer` - A Core Video image buffer containing a decompressed video frame. The client should retain returned image buffers and release them when they are no longer needed. Image buffers are __NOT__ owned by the decoder instance.

### Discussion

When creating a `VDADecoder` object, pass in a `VDADecoderOutputCallback` function to be used to return decompressed frames. The output callback may be called in decode order rather than presentation order.

[Back to Top](#)

## Data Types

### VDADecoder

```
OpaqueVDADecoder*  VDADecoder
```

A reference to a video decoder object.

[Back to Top](#)

## Constants

### Decoder Configuration Keys

- `kVDADecoderConfiguration_Height` - A `CFNumberRef` specifying source height.
- `kVDADecoderConfiguration_Width` - A `CFNumberRef` specifying source width.
- `kVDADecoderConfiguration_SourceFormat` - A `CFNumberRef` (`kCFNumberSInt32Type` Four Character Code) specifying source format. For example, `'avc1'`.
- `kVDADecoderConfiguration_avcCData` - A `CFDataRef` containing `avcC` data from the H.264 bitstream. In a QuickTime movie file, this is the same data which is stored in the image description as the `avcC` atom.

### Destination Image Buffer Attribute Keys

Listed are the commonly used keys, for a full list of available Core Video Pixel Buffer keys see `CoreVideo/CVPixelBuffer.h`

- `kCVPixelBufferPixelFormatTypeKey` - A single `CFNumberRef` (OSType) or an array of `CFNumberRef` (OSTypes) specifying output pixel format. For example, `kCVPixelFormatType_422YpCbCr8`.
- `kCVPixelBufferWidthKey` -A `CFNumberRef` specifying the width of the pixel buffer.
- `kCVPixelBufferHeightKey` - A `CFNumberRef` specifying the height of the pixel buffer.
- `kCVPixelBufferIOSurfacePropertiesKey` - A `CFDictionaryRef` of IOSurface properties. The presence of this key requests buffer allocation via IOSurface. If a `destinationImageBufferAttributes` dictionary is specified in `VDADecoderCreate`, that dictionary __MUST__ contain this key. The value for the this key is most often just an empty dictionary. If `NULL` is specified in `VDADecoderCreate` for the `destinationImageBufferAttributes` dictionary, this key is assumed to be set. The hardware decoder requires IOSurface backed image buffers for rendering. See `IOSurface/IOSurfaceAPI.h` for the complete list of available IOSurface properties.

__Note:__ Specifying destination image buffer attributes may lead to additional buffer copies per frame since the framework may need to do some scaling and/or format conversion from the hardware preferred output format.

### Decode Flags

Flags used with the `VDADecoderDecode`.

```
kVDADecoderDecodeFlags_DontEmitFrame = 1 << 0
```

Specifies that the decoder should not return an image buffer in the output callback. Note that the output callback is still invoked.

### Flush Flags

Flags used with the `VDADecoderFlush`.

```
kVDADecoderFlush_EmitFrames = 1 << 0
```

During a flush operation this flag specifies that the decoder should decode and return image buffers for all currently queued frames.

### Decode Info Flags

During decode, flags may be set in the `infoFlags` field of the output callback conveying extra information about a decode operation.

```
kVDADecodeInfo_Asynchronous = 1UL << 0
kVDADecodeInfo_FrameDropped = 1UL << 1
```

- `kVDADecodeInfo_Asynchronous` - Indicates asynchronous decoding. As asynchronous decode is the normal operating mode of the decoder object, this flag will always be set during normal operation.
- `kVDADecodeInfo_FrameDropped` - Indicates the frame was dropped.
[Back to Top](#)

## Result Codes

Errors returned from the `VDADecoder` APIs.

```
kVDADecoderNoErr                    = 0
kVDADecoderHardwareNotSupportedErr  = -12470
kVDADecoderFormatNotSupportedErr    = -12471
kVDADecoderConfigurationError       = -12472
kVDADecoderDecoderFailedErr         = -12473
```

- `kVDADecoderNoErr` - Life is good.
- `kVDADecoderHardwareNotSupportedErr` - The hardware does not support accelerated video services required for hardware decode.
- `kVDADecoderFormatNotSupportedErr` - The hardware may support accelerated decode, but does not support the requested output format.
- `kVDADecoderConfigurationError` - Invalid or unsupported configuration parameters were specified in `VDADecoderCreate`.
- `kVDADecoderDecoderFailedErr` - An error was returned by the decoder layer. This may happen for example because of bitstream/data errors during a decode operation. This error may also be returned from `VDADecoderCreate` when hardware decoder resources are available on the system but currently in use by another process.

[Back to Top](#)

## Sample Code

The following data types and helper functions are referenced in the code listings below and presented for illustrative purposes only. They are not part of the framework.

```swift
// tracks a frame in and output queue in display order
typedef struct myDisplayFrame {
    int64_t                 frameDisplayTime;
    CVPixelBufferRef        frame;
    struct myDisplayFrame   *nextFrame;
} myDisplayFrame, *myDisplayFramePtr;

// some user data
typedef struct MyUserData
{
    ...

    myDisplayFramePtr displayQueue; // display-order queue - next display frame is always at the queue head
    int32_t           queueDepth; // we will try to keep the queue depth around 10 frames
    pthread_mutex_t   queueMutex; // mutex protecting queue manipulation

     ...
} MyUserData, *MyUserDataPtr;

// example helper function that wraps a time into a dictionary
static CFDictionaryRef MakeDictionaryWithDisplayTime(int64_t inFrameDisplayTime)
{
    CFStringRef key = CFSTR("MyFrameDisplayTimeKey");
    CFNumberRef value = CFNumberCreate(kCFAllocatorDefault, kCFNumberSInt64Type, &inFrameDisplayTime);

    return CFDictionaryCreate(kCFAllocatorDefault,
                              (const void **)&key,
                              (const void **)&value,
                              1,
                              &kCFTypeDictionaryKeyCallBacks,
                              &kCFTypeDictionaryValueCallBacks);
}

// example helper function to extract a time from our dictionary
static int64_t GetFrameDisplayTimeFromDictionary(CFDictionaryRef inFrameInfoDictionary)
{
    CFNumberRef timeNumber = NULL;
    int64_t outValue = 0;

    if (NULL == inFrameInfoDictionary) return 0;

    timeNumber = CFDictionaryGetValue(inFrameInfoDictionary, CFSTR("MyFrameDisplayTimeKey"));
    if (timeNumber) CFNumberGetValue(timeNumber, kCFNumberSInt64Type, &outValue);

    return outValue;
}
```

### Creating a Decoder

Listing 1 illustrates the basic steps required to create a decoder.

The function requires parameters describing the compressed source media bitstream (dimensions, format type and decoder configuration) to be passed in by the caller. These parameters are used to create the decoder configuration dictionary. An optional pixel format attribute dictionary is also created requesting '2vuy' as the format of the returned image buffers. This dictionary can be `NULL` if the caller has no preference regarding the pixel format of the returned image buffers.

If decoder creation was successful, a `VDADecoder` object is returned to the caller via `decoderOut`.

__Warning:__ As mentioned in the Constants section above, if a destination image buffer attributes dictionary is used to specify a preferred output image buffer pixel format as shown in listing 1, the dictionary __MUST__ contain an IOSurface properties dictionary (`kCVPixelBufferIOSurfacePropertiesKey`) or `VDADecoderCreate` will fail.

__Listing 1__

```
OSStatus CreateDecoder(SInt32 inHeight, SInt32 inWidth,
                       OSType inSourceFormat, CFDataRef inAVCCData,
                       VDADecoder *decoderOut)
{
    OSStatus status;

    CFMutableDictionaryRef decoderConfiguration = NULL;
    CFMutableDictionaryRef destinationImageBufferAttributes = NULL;
    CFDictionaryRef emptyDictionary;

    CFNumberRef height = NULL;
    CFNumberRef width= NULL;
    CFNumberRef sourceFormat = NULL;
    CFNumberRef pixelFormat = NULL;

    // source must be H.264
    if (inSourceFormat != 'avc1') {
        fprintf(stderr, "Source format is not H.264!\n");
        return paramErr;
    }

    // the avcC data chunk from the bitstream must be present
    if (inAVCCData == NULL) {
        fprintf(stderr, "avc1 decoder configuration data cannot be NULL!\n");
        return paramErr;
    }

    // create a CFDictionary describing the source material for decoder configuration
    decoderConfiguration = CFDictionaryCreateMutable(kCFAllocatorDefault,
                                                     4,
                                                     &kCFTypeDictionaryKeyCallBacks,
                                                     &kCFTypeDictionaryValueCallBacks);

    height = CFNumberCreate(kCFAllocatorDefault, kCFNumberSInt32Type, &inHeight);
    width = CFNumberCreate(kCFAllocatorDefault, kCFNumberSInt32Type, &inWidth);
    sourceFormat = CFNumberCreate(kCFAllocatorDefault, kCFNumberSInt32Type, &inSourceFormat);

    CFDictionarySetValue(decoderConfiguration, kVDADecoderConfiguration_Height, height);
    CFDictionarySetValue(decoderConfiguration, kVDADecoderConfiguration_Width, width);
    CFDictionarySetValue(decoderConfiguration, kVDADecoderConfiguration_SourceFormat, sourceFormat);
    CFDictionarySetValue(decoderConfiguration, kVDADecoderConfiguration_avcCData, inAVCCData);

    // create a CFDictionary describing the wanted destination image buffer
    destinationImageBufferAttributes = CFDictionaryCreateMutable(kCFAllocatorDefault,
                                                                 2,
                                                                 &kCFTypeDictionaryKeyCallBacks,
                                                                 &kCFTypeDictionaryValueCallBacks);

    OSType cvPixelFormatType = kCVPixelFormatType_422YpCbCr8;
    pixelFormat = CFNumberCreate(kCFAllocatorDefault, kCFNumberSInt32Type, &cvPixelFormatType);
    emptyDictionary = CFDictionaryCreate(kCFAllocatorDefault, // our empty IOSurface properties dictionary
                                         NULL,
                                         NULL,
                                         0,
                                         &kCFTypeDictionaryKeyCallBacks,
                                         &kCFTypeDictionaryValueCallBacks);

    CFDictionarySetValue(destinationImageBufferAttributes, kCVPixelBufferPixelFormatTypeKey, pixelFormat);
    CFDictionarySetValue(destinationImageBufferAttributes,
                         kCVPixelBufferIOSurfacePropertiesKey,
                         emptyDictionary);

    // create the hardware decoder object
    status = VDADecoderCreate(decoderConfiguration,
                              destinationImageBufferAttributes,
                              (VDADecoderOutputCallback*)myDecoderOutputCallback,
                              (void *)myUserData,
                              decoderOut);

    if (kVDADecoderNoErr != status) {
        fprintf(stderr, "VDADecoderCreate failed. err: %d\n", status);
    }

    if (decoderConfiguration) CFRelease(decoderConfiguration);
    if (destinationImageBufferAttributes) CFRelease(destinationImageBufferAttributes);
    if (emptyDictionary) CFRelease(emptyDictionary);

    return status;
}
```

### Output Callback

Listing 2 demonstrates a hypothetical output callback.

Clients should not perform any heavyweight tasks directly in the callback or call into any frameworks which may block for an extended period of time. If the intention is to display the frames, note that the image buffers may not be in display order. Ideally, frames returned in the output callback would be enqueued for processing or display on another thread.

__Listing 2__

```
void myDecoderOutputCallback(void               *decompressionOutputRefCon,
                             CFDictionaryRef    frameInfo,
                             OSStatus           status,
                             uint32_t           infoFlags,
                             CVImageBufferRef   imageBuffer)
{
    MyUserDataPtr myUserData = (MyUserDataPtr)decompressionOutputRefCon;

    myDisplayFramePtr newFrame = NULL;
    myDisplayFramePtr queueWalker = myUserData->displayQueue;

    if (NULL == imageBuffer) {
        printf("myDecoderOutputCallback - NULL image buffer!\n");
        if (kVDADecodeInfo_FrameDropped & infoFlags) {
            printf("myDecoderOutputCallback - frame dropped!\n");
        }
        return;
    }

    if ('2vuy' != CVPixelBufferGetPixelFormatType(imageBuffer)) {
        printf("myDecoderOutputCallback - image buffer format not '2vuy'!\n");
        return;
    }

    // allocate a new frame and populate it with some information
    // this pointer to a myDisplayFrame type keeps track of the newest decompressed frame
    // and is then inserted into a linked list of  frame pointers depending on the display time
    // parsed out of the bitstream and stored in the frameInfo dictionary by the client
    newFrame = calloc(sizeof(myDisplayFrame), 1);
    newFrame->frame = CVBufferRetain(imageBuffer);
    newFrame->frameDisplayTime = GetFrameDisplayTimeFromDictionary(frameInfo);

    // since the frames we get may be in decode order rather than presentation order
    // our hypothetical callback places them in a queue of frames which will
    // hold them in display order for display on another thread
    pthread_mutex_lock(&myUserData->queueMutex);

    if (!queueWalker || (newFrame->frameDisplayTime < queueWalker->frameDisplayTime)) {
        // we have an empty queue, or this frame earlier than the current queue head
        newFrame->nextFrame = queueWalker;
        myUserData->displayQueue = newFrame;
    } else {
        // walk the queue and insert this frame where it belongs in display order
        Boolean         frameInserted = false;
        myDisplayFramePtr nextFrame = NULL;

        while (!frameInserted) {
            nextFrame = queueWalker->nextFrame;
            if (!nextFrame || (newFrame->frameDisplayTime < nextFrame->frameDisplayTime)) {
                // if the next frame is the tail of the queue, or our new frame is ealier
                newFrame->nextFrame = nextFrame;
                queueWalker->nextFrame = newFrame;
                frameInserted = true;
            }
            queueWalker = nextFrame;
        }
    }

    myUserData->queueDepth++;

    pthread_mutex_unlock(&myUserData->queueMutex);
}
```

### Decoding A Frame

Listing 3 demonstrates the use of `VDADecoderDecode` to decompress a single frame of H.264 video.

The function takes a `CFDataRef` containing the compressed video frame and a frame time (provided by the client from the bitstream) which is packaged in a frame info dictionary. The frame info dictionary is passed along to the output callback for this frame when decompressed and may contain any number of custom defined properties supplied by the client as key/value pairs.

__Listing 3__

```
OSStatus DecodeAFrame(VDADecoder inDecoder, CFDataRef inCompressedFrame, int64_t inFrameDisplayTime)
{
    CFDictionaryRef frameInfo = NULL;
    OSStatus status = kVDADecoderNoErr;

    // create a dictionary containg some information about the frame being decoded
    // in this case, we pass in the display time aquired from the stream
    frameInfo = MakeDictionaryWithDisplayTime(inFrameDisplayTime);

    // ask the hardware to decode our frame, frameInfo will be retained and pased back to us
    // in the output callback for this frame
    status = VDADecoderDecode(inDecoder, 0, inCompressedFrame, frameInfo);
    if (kVDADecoderNoErr != status) {
        fprintf(stderr, "VDADecoderDecode failed. err: %d\n", status);
    }

    // the dictionary passed into decode is retained by the framework so
    // make sure to release it here
    CFRelease(frameInfo);

    return status;
}
```

[Back to Top](#)

## Reference

For Mac model information see: [About integrated video on Intel-based Macs](http://support.apple.com/kb/HT3246)

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-05-28 | Editorial |
| 2011-05-24 | Editorial |
| 2011-04-27 | Editorial |
| 2010-04-19 | Added a note describing where to get the framework to link against. |
| 2010-03-29 | New document that describes the Video Decode Acceleration Framework APIs available on Mac OS v10.6.3 and later with certain Mac models. |

