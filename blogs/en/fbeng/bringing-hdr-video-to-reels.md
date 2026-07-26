---
title: Bringing HDR video to Reels
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2023/07/17/video-engineering/hdr-video-reels-meta/'
original_language: en
published: 2023-07-17
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:9b6b6061c5f24286'
translated: false
---

> 原文：[Bringing HDR video to Reels](https://engineering.fb.com/2023/07/17/video-engineering/hdr-video-reels-meta/)　·　Meta Engineering — iOS

- Meta has made it possible for people to upload high dynamic range (HDR) videos from their phone’s camera roll to Reels on Facebook and Instagram.
- To show standard dynamic range (SDR) UI elements and overlays legibly on top of HDR video, we render them at a brightness level comparable to the video itself.
- We solved various technical challenges to ensure a smooth transition to HDR video across the diverse range of old and new devices that people use to interact with our services every day.

Over the past year, the Video Infrastructure teams at Facebook and Instagram have seen a significant increase in the amount of HDR content being uploaded to our apps, with millions of HDR videos uploaded every day. As a result, we have been working to bring true HDR video support to our family of apps, starting with Reels. Today, people now have the ability to upload HDR videos from their phone’s camera roll to Reels and to have that video playback in full HDR . To make this possible, we needed to overcome a few technical challenges to ensure a smooth transition to HDR video across the diverse range of old and new devices that people use to interact with our services every day.

The journey to HDR can be better understood if we look at how the introduction of color television, for instance, was a game changer, allowing viewers to watch programs in full color, a vastly different experience from the black-and-white broadcasting of the past. This marked a step change in bringing video closer to reality, setting the stage for future advancements, such as high-definition (HD) content, that continue raising the bar for the viewer experience.

Now we are at the dawn of the next generation of video with the transition to HDR video. Unlike SDR video, HDR video has a wider range of luminosity and color, which results in brighter whites, darker blacks, and a larger potential number of visible colors for more vivid and true-to-life images. The growing adoption of HDR cameras and displays, especially on mobile devices, allows a wider audience to experience its benefits.

## Challenge: Differing device support for HDR

The rollout of HDR cameras and displays has resulted in an extensive range of devices with disparate capabilities, which makes implementing end-to-end HDR video creation and delivery challenging. It’s more complicated than simply enabling HDR video creation and upload for supported devices. From a product perspective, we need to ensure that HDR is correctly preserved through our entire media pipeline to provide a quality user experience all the way from the creator’s device through our server-side video processing/storage and, ultimately, view-side delivery and playback.

![HDR on Reels](https://engineering.fb.com/wp-content/uploads/2023/06/CC23_021-Visual-5_Lifecycle.png?w=916)

One of the main challenges with having a wide range of devices with various capabilities is ensuring compatibility across different devices. HDR video standards have specific hardware requirements for both creation and consumption, and not all devices support these new standards. This means that some consumers may not be able to view HDR content. Even worse, they may see a degraded version of the video with incorrect colors, resulting in a less satisfying viewing experience.

HDR video also comes with the challenge of different HDR formats, such as HLG and PQ, either of which may contain HDR10+ or Dolby Vision dynamic metadata. Different device manufacturers may choose to implement their own standards, with each having unique capabilities in terms of the range of luminosity and color gamut they support. Different sensors also result in different colors. These distinctions all result in additional characteristics for us to account for to ensure that a given video appears consistently and correctly across all devices. For example, if a video is encoded in HDR10 and played on a device with an 8-bit display, in some cases the video may look worse than if it were an SDR video, with washed-out or unnatural-looking colors. If we didn’t address this, it would be difficult for creators to accurately showcase their work and guarantee the viewing experience of their audiences.

## Challenge: Accurate tone mapping

Since not all devices support HDR displays, we need to provide backward compatibility by offering an SDR representation of the HDR video. Tone mapping is the process of scaling down the dynamic range and color space of an image or video while aiming to preserve the original appearance of the image. Improper tone mapping may cause color shifts that look unnatural, such as trees that appear blue. Tone-mapped videos may be too bright or too dark. In a professional studio, manual tone mapping or color grading involves adjusting the parameters until the results look pleasing. However, we need a solution that can run automatically on billions of videos without needing human review with the tone-mapped SDR encoding closely resembling the original HDR video.

![HDR on Reels](https://engineering.fb.com/wp-content/uploads/2023/06/CC23_021-Visual-3_ColorGamutChart.png?w=1024)Sophisticated tone mapping algorithms can be used to preserve quality and minimize any artifacts that were introduced. Objective visual quality metrics for tone mapping remain an open research problem in the industry, but based on our internal testing, we were able to tune the popular [Hable](http://filmicworlds.com/blog/filmic-tonemapping-with-piecewise-power-curves/) tone mapping operator to produce results that reasonably represent the creator’s original intent.

## Tone mapping on the client

When creators first began uploading HDR video content, our media pipeline was not prepared to handle 10-bit colors. So HDR videos had overexposed colors, resulting in a dissatisfying experience. iOS devices were the first to enable HDR by default and, as such, were where we began to see HDR uploads coming from our users. To mitigate this, we converted all compositions containing HDR content to SDR on the device prior to upload with client-side tone mapping.

We used Apple’s native tone mapping APIs to quickly release a fix, mapping HDR videos to SDR color space prior to uploading to our servers. This way all uploads were guaranteed to look good across all devices, even if they were coming from newer phones that captured HDR video.

![HDR on Reels](https://engineering.fb.com/wp-content/uploads/2023/06/CC23_021-Visual-7_ToneMapping.png?w=916)

On Android the story was a bit different. With a more diverse device landscape that lacked standardization for HDR in its early phases, we weren’t able to rely on OS-level tone mapping to maintain a consistent appearance. Some devices were creating HDR videos with the PQ transfer function, while others used HLG. These different standards resulted in different representations of color and, as a result, there was no one-size-fits-all solution for tone mapping all Android HDR uploads into accurate SDR representations.

_Bhumi Sabarwal, a software engineer at Meta, discusses the challenges around enabling tone mapping on Android. (from: Video @Scale 2022)_

For Android, we needed to implement a deeper solution. The early experience for Android HDR Reels resulted in washed out colors for users with newer devices. So we built custom tone mapping shaders to accurately convert both PQ and HLG HDR into accurate SDR. First, we extracted the video metadata while decoding the frames to determine which transfer function was used (e.g., PQ or HLG). Next, once we had each frame in YUV colorspace, we could apply appropriate transformation matrices to convert into the target SDR colorspace (BT.709). Once we had the SDR rendition, the rest of the creation process, including creative effects, AR filters, and complex media composition, were able to function appropriately.

With client-side tone mapping in place, we had alleviated the issue with washed out colors, but we were still not delivering a true HDR experience for those creators who had HDR content.

## Tone mapping on the server

With client-side tone mapping, we were able to mitigate the visual quality degradation associated with HDR video processed in a media pipeline that only supported SDR. This fixed the issues we were observing, but our ultimate goal was still to unlock the power of newer devices with HDR displays and deliver a full HDR experience to them. This meant building robust end-to-end HDR support while also supporting a satisfying user experience for older devices that may not support HDR.

As part of the creation process, we already [transcode all uploaded videos into different resolutions and bitrates](https://engineering.fb.com/2021/04/05/video-engineering/how-facebook-encodes-your-videos/) to provide a smooth playback experience for all devices and network conditions with [adaptive bitrate streaming](https://en.wikipedia.org/wiki/Adaptive_bitrate_streaming) (ABR). With HDR videos, however, this can get a bit more complicated since they require 10 bits per color component per pixel, and are often encoded with newer codecs, such as HEVC, VP9, or [AV1](https://engineering.fb.com/2023/02/21/video-engineering/av1-codec-facebook-instagram-reels/). These characteristics increase the decode complexity, and thus require higher performance devices to support smooth decoding and playback. If we delivered HDR content to all devices, including those without adequate support, we could introduce degraded performance as the higher requisite bitrates result in wasted bandwidth, which leads to increased buffering, more frequent in-play stalls, and lower battery life.

Therefore, to build an experience optimized for all users, we need to have a way to deliver SDR encodings to devices that can’t take advantage of the benefits of HDR. To address the challenge of delivering HDR video across a diverse device ecosystem, we built tone mapping into our server-side processing.

![HDR on Reels](https://engineering.fb.com/wp-content/uploads/2023/07/CC23_021_Visual-4_Pipeline_0717.png?w=1024)

With server-side tone mapping, we upload content to our servers with the original HDR color information intact, and generate both HDR and SDR representations for delivery. Doing both HDR and SDR encodes doubles our compute for the HDR videos. Leveraging our [Meta Scalable Video Processor for HDR processing,](https://ai.facebook.com/blog/meta-scalable-video-processor-MSVP/)we are able to handle this load without increased energy requirements.

If a device does not support HDR, only the SDR representation will be delivered for playback. Additionally, the tone-mapped SDR variants of HDR videos are useful for mixed scenarios, like the [Instagram Explore](https://ai.meta.com/blog/powered-by-ai-instagrams-explore-recommender-system/) page or the [Facebook Feed](https://engineering.fb.com/2021/01/26/ml-applications/news-feed-ranking/), where the user experience is best with a uniform brightness across all thumbnails and previews.

## Challenge: Managing brightness

Within our apps, we also faced challenges around maintaining the consistency of the app experience when introducing HDR brightness and colors in the context of the user interfaces designed around SDR video. This often resulted in inconsistent or unsatisfying experiences in our testing.

As mentioned above, HDR does not only expand the range of colors, but also contrast by enabling higher levels of brightness. This begs the question of how an already bright display can become even brighter to sufficiently accommodate the dynamic range needed for HDR, while also ensuring that SDR content remains correctly and relatively represented. On iOS devices, the default system behavior is quite interesting. The brightest ranges of the display become reserved for HDR content, and the SDR content actually becomes dimmer.

![HDR on Reels](https://engineering.fb.com/wp-content/uploads/2023/06/CC23_021-Visual-6_ManagingBrightness.png?w=916)

_Inconsistent brightness when displaying HDR and SDR in a mixed scenario. The leftmost video in the third row is an HDR video and is much brighter than the other videos._

What is happening may not be noticeable in an app where the entirety of the screen is occupied by a single video. However, in an app like Instagram, where a video is displayed alongside others, this effect can be quite dissatisfying and challenges us to define a new standard for an optimal user experience.

One case is the [Explore tab](https://engineering.fb.com/2020/12/10/web/how-instagram-suggests-new-content/), which presents a mix of photos and videos displayed in a grid. If we simply enabled HDR in this setting the HDR videos would draw extra attention, leading to an unbalanced experience. In this scenario we’d use the same client-side tone mapping that we had used during video creation to tone map videos on the fly.

Another case is Reels, where we display a single full-screen video at a time, overlaid by UI indicating the author, caption, comments, and other metadata. These interface elements are SDR and, as such, they are subject to the same dimming behavior when they’re displayed alongside HDR content. This led to issues in our early experiments where white text appeared gray when rendered alongside HDR video. We wanted to ensure that our overlay text would always be rendered in true white because the gray – being dimmer and completely illegible in some cases – posed a usability concern.

Because our objective is to actually show HDR videos, simply tone mapping back to SDR was not the ideal option. Instead, we worked the problem from the other side, rendering the overlays in HDR when accompanying an HDR video. To do this, we apply a brightness multiplier to the overlay colors, extending into the HDR parts of the spectrum and thus rendering at the same brightness levels.

_Chris Ellsworth, a software engineer at Meta, discusses our work supporting HDR on iOS. (from: Video @Scale 2022)_

## Acknowledgements

_This work is the result of a collaborative effort between the entire Video Infrastructure and Instagram Media Platform teams at Meta. The authors would like to extend special thanks to the following people: Anthony Dito, Rex Jin, Ioannis Katsavounidis, Ryan Lei, Wen Li, Richard Liu, Denise Noyes, Ryan Peterman, David Ronca, Bhumi Sabarwal, Moisés Ferrer Serra, Ravi Shah, Zafar Shahid, Haixia Shi, Nidhi Singh, and Kyle Yoon._
