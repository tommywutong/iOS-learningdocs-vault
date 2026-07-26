---
title: Why xHE-AAC is being embraced at Meta
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2023/04/11/video-engineering/high-quality-audio-xhe-aac-codec-meta/'
original_language: en
published: 2023-04-11
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0096753ea6040a7f'
translated: false
---

> 原文：[Why xHE-AAC is being embraced at Meta](https://engineering.fb.com/2023/04/11/video-engineering/high-quality-audio-xhe-aac-codec-meta/)　·　Meta Engineering — iOS

- We’re sharing how Meta delivers high-quality audio at scale with the [xHE-AAC audio codec](https://www.iis.fraunhofer.de/en/ff/amm/broadcast-streaming/xheaac.html).
- xHE-AAC has already been deployed on Facebook and Instagram to provide enhanced audio for features like Reels and Stories.

At Meta, we serve every media use case imaginable for billions of people across the world — from short-form, user-generated content, such as [Reels](https://engineering.fb.com/2023/02/21/video-engineering/av1-codec-facebook-instagram-reels/), to premium [video on demand (VOD)](https://engineering.fb.com/2021/04/05/video-engineering/how-facebook-encodes-your-videos/) and [live broadcasts](https://engineering.fb.com/2020/10/22/video-engineering/live-streaming/). Given this, we need a next-generation audio codec that supports a range of operating points with excellent compression efficiency and modern, system-level audio features.

To address these needs now and into the future, Meta has embraced xHE-AAC as the vehicle for delivering high-quality audio at scale.

## The benefits of xHE-AAC

xHE-AAC is the latest member of the MPEG AAC audio codec family. The [Fraunhofer Institute for Integrated Circuits IIS](https://www.iis.fraunhofer.de/en/ff/amm/broadcast-streaming/xheaac.html) played a substantial role in the development of xHE-AAC and the MPEG-D DRC standard.

Today, xHE-AAC is already providing a superior audio experience on Facebook and Instagram — including on [Reels](https://engineering.fb.com/2023/02/21/video-engineering/av1-codec-facebook-instagram-reels/) and [Stories](https://engineering.fb.com/2022/07/18/developer-tools/building-text-animations-for-instagram-stories/) — and has a number of valuable features.

### Loudness management

With [hundreds of millions of uploads per day across Facebook and Instagram](https://engineering.fb.com/2021/04/05/video-engineering/how-facebook-encodes-your-videos/), we receive audio tracks with loudness levels ranging from silence to full scale, and everything in between.

![xHE-AAC codec at Meta](https://engineering.fb.com/wp-content/uploads/2023/03/xHE-AAC-Meta-Visual-1.jpg?w=1024)

When people play these videos sequentially, they can perceive some audio as being too loud or too quiet. This creates listener fatigue from having to constantly adjust the volume.

![xHE-AAC codec at Meta](https://engineering.fb.com/wp-content/uploads/2023/03/xHE-AAC-Meta-Visual-2.jpg?w=1024)

xHE-AAC’s integrated loudness management system solves for loudness inconsistency while meticulously preserving creator intent by bringing the average loudness of all sessions to the same target level and managing the dynamic range of each session to fit the playback environment.

Instead of burning in a specific target level and dynamic range compression (DRC) profile during encoding, xHE-AAC allows us to leave the original audio characteristics untouched and delegate loudness management processing to the client via loudness metadata, for the optimal audio experience based on context.

![xHE-AAC codec at Meta](https://engineering.fb.com/wp-content/uploads/2023/03/xHE-AAC-Meta-Visual-3.jpg?w=1024)

As a result of xHE-AAC’s loudness management, people can spend more time immersed in their favorite content and less time fiddling with the volume control.

### Adaptive bit rate audio

Most people who use our apps consume media on mobile devices and expect the highest audio quality without interruption. This presents a challenge for streaming media because connection quality varies on mobile and can result in a very uneven user experience.

![xHE-AAC codec at Meta](https://engineering.fb.com/wp-content/uploads/2023/03/xHE-AAC-Meta-Visual-4.jpg?w=1024)

To optimize quality under dynamic bandwidth constraints, we produce[multiple video and audio qualities](https://engineering.fb.com/2021/04/05/video-engineering/how-facebook-encodes-your-videos/) to match varying network conditions at playback time. Even though we produce multiple audio lanes, we have historically only employed[adaptive bit rate (ABR)](https://engineering.fb.com/2022/11/04/video-engineering/instagram-video-processing-encoding-reduction/) algorithms to switch video qualities during playback because it’s difficult to enable adaptive bit rate audio without compromising quality during lane transitions.

In order to enable seamless audio ABR, xHE-AAC introduces the concept of immediate playout frames (IPFs) that contain all the data necessary to start playing a new audio lane without relying on data from other frames. By placing an IPF at the beginning of each Dynamic Adaptive Streaming over HTTP (DASH) segment and aligning the segment durations of each lane, we can seamlessly switch between audio lanes during playback to provide the highest-quality audio at any available bandwidth while avoiding playback stalls.

![xHE-AAC codec at Meta](https://engineering.fb.com/wp-content/uploads/2023/03/xHE-AAC_Visual-5.jpg?w=1024)

After launching audio ABR on Facebook for Android, we were able to improve user experience by reducing the number of sessions where playback stalls.

## How we deployed xHE-AAC

We generate xHE-AAC bitstreams using an encoder SDK provided by the Fraunhofer Institute for Integrated Circuits IIS, and then prepare the resulting audio files for DASH streaming with shaka-packager. The xHE-AAC encoder’s two-pass encoding mode is used to measure the input loudness envelope and average program loudness on the first pass and perform the actual audio data compression on the second pass. As an added benefit, two-pass encoding allows us to use loudness range control (LRAC) DRC, which mitigates pumping artifacts otherwise introduced by single-pass DRC algorithms.  ![xHE-AAC codec at Meta](https://engineering.fb.com/wp-content/uploads/2023/03/xHE-AAC-Meta-Visual-6.jpg?w=742)

To prepare an xHE-AAC audio adaptation set for ABR delivery, IPFs are inserted at constant time intervals, audio configuration parameters such as sample rate and channel configuration are kept constant, and unique stream identifiers are selected for each lane in the audio adaptation set.

At playback time, we custom-fit the audio to the listening environment by configuring a target loudness level and DRC effect type based on context, and thanks to the embedded loudness metadata, we can adapt a single xHE-AAC bitstream to a variety of audio consumption use cases, from headphones to device speakers and various levels of background noise. Finally, if the client is starved for data or bandwidth is plentiful, audio ABR will automatically switch audio qualities to ensure that the highest audio quality is played without interrupting the playback session.

## Where can you experience xHE-AAC today?

You can experience xHE-AAC audio on Facebook for iOS and Android, as well as on targeted surfaces on Instagram, such as Reels and Stories. We encourage you to install the latest version of Facebook and Instagram apps on iOS 13+ and Android 9+ to ensure that you can experience it.

## Acknowledgements

_This work is the collective result of the entire Video Infrastructure and Instagram Media Platform teams at Meta in collaboration with Fraunhofer__Institute for Integrated Circuits__IIS. The author would like to extend special thanks to Abhishek Gera, Tim Harris, Arun Kotiedath, Edward Li, Meng Li, Srinivas Lingutla, Denise Noyes, Mohanish Penta, David Ronca, Haixia Shi, Mike Starr, Cosmin Stejerean, Jithin Parayil Thomas, Simha Venkataramaiah, Juehui Zhang, Runshen Zhu, and the engineering team at Fraunhofer__Institute for Integrated Circuits__IIS._
