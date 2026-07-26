---
title: Enhancing HDR on Instagram for iOS With Dolby Vision
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2025/11/17/ios/enhancing-hdr-on-instagram-for-ios-with-dolby-vision/'
original_language: en
published: 2025-11-17
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6edc1ba0fe018f44'
translated: false
---

> 原文：[Enhancing HDR on Instagram for iOS With Dolby Vision](https://engineering.fb.com/2025/11/17/ios/enhancing-hdr-on-instagram-for-ios-with-dolby-vision/)　·　Meta Engineering — iOS

- We’re sharing how we’ve enabled Dolby Vision and ambient viewing environment (amve) on the Instagram iOS app to enhance the video viewing experience.
- HDR videos created on iPhones contain unique Dolby Vision and amve metadata that we needed to support end-to-end
- Instagram for iOS is now the first Meta app to support Dolby Vision video, with more support coming across all of Meta’s apps coming in the future.

Every iPhone-produced HDR video encoding includes two additional pieces of metadata that help ensure the picture is consistent between different displays and viewing conditions:

- Ambient viewing environment (amve), whichprovides the characteristics of the nominal ambient viewing environment for displaying associated video content. This information enables the final device to adjust the rendering of the video if the actual ambient viewing conditions differ from those for which it was encoded.
- Dolby Vision, which enhances color, brightness, and contrast to better match the video to the capabilities of the display.

While the Instagram and Facebook iOS apps [have supported high dynamic range (HDR) video](https://engineering.fb.com/2023/07/17/video-engineering/hdr-video-reels-meta/) since 2022, our initial rollout of HDR didn’t support Dolby Vision or amve delivery and playback. Our derived encodings were done with [FFmpeg](https://www.ffmpeg.org/), which has traditionally lacked support for Dolby Vision and amve. Since our tooling was discarding this metadata, it meant that pictures were not entirely representative of the way they were meant to be viewed – something that was particularly noticeable at low screen brightness levels.

Now, after hearing feedback from people using our iOS apps, we’ve worked with our partners to preserve the iOS-produced amve and Dolby Vision metadata from end-to-end and significantly enhanced the HDR viewing experience on iOS devices.

## How Meta Processes Video

It may first be helpful to give some background on the [lifecycle of a video at Meta](https://engineering.fb.com/2021/04/05/video-engineering/how-facebook-encodes-your-videos/).

The majority of videos uploaded through our apps go through three main stages:

### 1. Client Processing

In the client processing stage, the creator’s device flattens their composition into a single video file at a size appropriate for upload. For HDR videos produced by iOS devices this means encoding with HEVC using the Main 10 profile. This is the stage in which amve and Dolby Vision metadata are produced, added to the encoded bitstream, and uploaded to Meta’s servers.

### 2.  Server Processing

In the server processing stage, our transcoding system generates different versions of the video for different consumers. As playback occurs across a variety of devices with different capabilities, we need to produce the video in a format which will be optimal for each device. In the scope of HDR uploads, this means producing an SDR version for devices that don’t support HDR, a VP9 version to satisfy the majority of players, and (for our most popular videos) an[AV1 version](https://engineering.fb.com/2023/02/21/video-engineering/av1-codec-facebook-instagram-reels/) with the highest quality at the lowest file size.

Each of these versions is produced at a different bitrate (essentially, file size) to ensure that consumers with varying network conditions are all able to play the video without waiting for a large download to complete (the tradeoff is that lower bitrates have lower quality). All of our derived encodings are created with FFmpeg, which historically lacked support for amve and Dolby Vision. This is the stage where metadata was getting dropped.

### 3. Consumption

In the consumption stage, the viewer’s device picks the version that will play back smoothly (without stalls), decodes it frame by frame, and draws each frame onto the screen. In the context of iOS, all HDR playback is done using Apple’s AVSampleBufferDisplayLayer (AVSBDL). This is the class that consumes amve and Dolby Vision metadata along with each decoded frame.

## How We Added Support for amve

When we first set off to support amve in 2022, we noticed something interesting. As we operate on a decoupled architecture of lower-level components rather than a typical high-level AVPlayer setup, we were able to inspect an intact video encoding and get a look at the amve metadata in between the decoder and AVSBDL. We observed that every frame of every video seemed to have exactly the same metadata. This allowed us to hold ourselves over with a quick fix and hardcode these values directly into our player pipeline.

This was not a great situation to be in. Even though the value seemed to be static, there was nothing enforcing this. Maybe a new iPhone or iOS version would produce different values, then we’d be using the wrong ones. amve is also not a concept on Android, which would mean that viewing an Android-produced HDR encoding on iPhone would result in an image that was not technically accurate.

In 2024, we worked with the community to land amve support in FFmpeg. We also built in some logging, which showed that our two-year-old assertion that the values never change still stood. But if they ever do, we will be properly set up for it.

## Enabling Dolby Vision

Dolby Vision was not as straightforward as amve to adopt.

**Challenge #1: The extant specification was for carriage of metadata within an HEVC bitstream. We don’t deliver HEVC.**

iPhone-produced HDR uses Dolby Vision profile 8.4, where 8 indicates a profile using HEVC (the video codec) and .4 means cross-compatible with HLG (the standard for HDR video that players without Dolby Vision support would adhere to).

In order to deliver Dolby Vision metadata we needed to carry it within a codec that we do deliver. Fortunately, Dolby has created Profile 10 for carriage of Dolby Vision within AV1. As VP9 does not offer a facility for carriage of additional metadata there is no support for Dolby Vision at this time, but we are interested in exploring alternate delivery mechanisms.

However, Dolby Vision Profiles 10 and 8 were not properly supported by our existing video processing tools, including FFmpeg and [Shaka](https://github.com/shaka-project/shaka-packager) packager. Based on the specifications from Dolby, we collaborated with the FFmpeg developers to fully implement support for Dolby Vision Profile 8 and Profile 10. In particular, we enabled support within FFmpeg to transcode HEVC with Profile 8.4 into AV1 with Profile 10.4 using both the libaom and libsvtav1 encoders, and made fixes to other parts of the stack, including dav1d decoder and Shaka packager, to properly support Dolby Vision metadata.

**Challenge #2: Getting Dolby Vision into AVSampleBufferDisplayLayer**

When you feed AVSBDL an encoded bitstream in a supported format, e.g., HEVC from an iPhone camera, Dolby Vision just works for free. But we feed buffers that we decode independently, as we need to be able to decode formats that Apple does not offer out of the box (AV1 on devices before the iPhone 15 Pro, for example). Given this setup, it’s only fair that we’d have to extract Dolby Vision independently as well.

Following the newly-minted specification for carriage of Profile 10 within an AV1 bitstream from Dolby, we implemented manual extraction of Dolby Vision metadata, packaged it into the same format that AVSBDL expected, and we were in business.

To prove that our setup was working as expected, we set up a series of identical Instagram posts with and without Dolby Vision metadata. Our partners at Dolby measured the brightness of each of these posts using a display color analyzer, at varying levels of screen brightness.

They captured the following:

![](https://engineering.fb.com/wp-content/uploads/2025/11/Meta-Dolby-Vision-iOS-Instagram_image-1.jpg)

<sub>Screen brightness settings versus image brightness, with and without Dolby Vision.</sub>

In this chart, the X-axis represents the screen brightness setting and the Y-axis represents the observed image brightness. The results demonstrate that with Dolby Vision metadata present, the brightness of the content much more closely follows the brightness setting of the screen.

It worked!…But we were not done yet.

## Testing Our Dolby Vision Implementation

At Meta, we A/B test new features before shipping them to ensure they are performing as we expect. How do we A/B test metadata embedded within a video bitstream? The answer is that we produced an additional version of every video containing the new metadata. We delivered this new version to a randomly distributed test population while the randomly distributed control population continued receiving the existing experience. At our scale, we can assert that roughly an equal population will watch both flavors of each video.

For each flavor, we collected statistics such as how long the video was watched, how long it took to load, what type of connection it was watched on, and whether any errors were encountered during playback. Then we analyzed in aggregate to see how the flavor with metadata compared to the flavor without.

We hypothesized that if the metadata works as expected, videos with the new metadata would receive more watch time. But when we ran our initial test on Instagram Reels in 2024 we found that, on average, videos with Dolby Vision metadata were actually watched less than their standard counterparts.

How could this be possible? Isn’t Dolby Vision supposed to improve the image?

### Our First A/B Test With Dolby Vision Metadata

Our data indicated that people were watching less Dolby Vision video because the videos were taking too long to load and people were just moving on to the next Reel in their feed.

There was a reasonable cause for the longer load times: The new metadata added on the order of 100 kbps to every video on average. It sounds petty, but our encodings are highly optimized for all kinds of diverse viewing conditions. Every bit counts in some situations, and a 100-kbps overhead was enough to regress engagement at the margins.

The answer to this was a compressed metadata format. The team at Dolby offered another specification which would lower the metadata overhead by a factor of four, to 25 kbps on average.

Would it be enough? We had to run another test to find out. But there was more work to be done first.

We needed to implement support for Dolby Vision metadata compression (and decompression while we’re at it) in FFmpeg using a bitstream filter. Also, while the uncompressed format was something we could extract from the bitstream and hand off to Apple, the compressed format was not something that was supported by Apple out of the box. We had to implement client-side decompression on our own.

About 2000 lines of code later, we were ready.

### Our Successful A/B Test

This time, we found that consumers viewing with Dolby Vision metadata were spending more time in the app. We attribute this to people spending more time watching HDR videos in lower-light environments, when their screens are set to lower brightness levels and the HDR videos with proper metadata are less taxing on the eyes.

Because including Dolby Vision metadata had a tangibly positive outcome, we were able to make the case for shipping it across Instagram for iOS, making it our first app to take advantage of Dolby Vision. As of June 2025, all of our delivered AV1 encodings derived from iPhone-produced HDR include Dolby Vision metadata.

## The Future of Dolby Vision Across Meta

The final challenge in the scope of this post is that Dolby Vision is not widely supported within the web ecosystem across different browsers and displays. Thus, we cannot accurately show the difference that it makes on this page, and hope you will experience it on Instagram on iPhone for yourself. The support for Dolby vision and amve is now in our encoding recipes and as such it’s ready for deployment to other platforms as well as we’re currently working on extending the support to Facebook Reels.

In collaboration with Dolby, we’ve solved the perceptible problem of HDR metadata preservation and collaborated with the FFmpeg developers to implement its support and make it readily available to the community to take advantage of.

This is just the beginning. We look forward to expanding Dolby Vision to other Meta apps and their corresponding operating systems.

## Acknowledgements

_We’d like to thank Haixia Shi, the team at Dolby, and Niklas Haas from FFmpeg for their work supporting this effort._
