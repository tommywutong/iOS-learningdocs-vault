---
title: Facebook open-sources Spectrum 1.0.0 for better mobile image production
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2019/01/17/developer-tools/spectrum/'
original_language: en
published: 2019-01-17
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1f599be09277961e'
translated: false
---

> 原文：[Facebook open-sources Spectrum 1.0.0 for better mobile image production](https://engineering.fb.com/2019/01/17/developer-tools/spectrum/)　·　Meta Engineering — iOS

As mobile camera hardware rapidly improves, our phones capture and store larger and larger files. Uploading these large files can eat up mobile data; it can take forever for them to load; and, sometimes, the files fail to load at all. To make the upload process more efficient, we developed [Spectrum](https://libspectrum.io/), an image processing library for Android and iOS. With Spectrum, we have improved the reliability and quality of image uploads at a large scale across our apps. We recently presented Spectrum as an open source project at [droidcon SF](https://www.sf.droidcon.com/), and, today, we are officially releasing [Spectrum 1.0.0](https://github.com/facebookincubator/spectrum) on GitHub.

## The path to better mobile image production

Step one begins before an image is uploaded. By reducing the file size through transcoding, we can quickly reduce data consumption and improve upload reliability. It’s a simple solution, but reducing size while maintaining quality requires a deep understanding of the various processing steps and image formats.

Using the platform-provided APIs for image processing is one possible solution. But numerous mobile platforms and evolving APIs can result in divergent output. To serve a broad developer base, platforms hide details and parameters that we want to control to optimize the output. Often, common tasks, such as interpretation of EXIF metadata, can result in code duplication that hinders maintenance and global improvements. And making use of the latest compression libraries, such as MozJpeg, requires writing native code in C/C++. We wanted to make it easier for developers to send smaller files while maintaining control of the image quality — without needing to write custom or hard-to-maintain solutions.

![](https://engineering.fb.com/wp-content/uploads/2019/01/spectrum1.jpg)

_As modern smartphones capture high-resolution images, the large file size makes uploads unreliable on some mobile networks. Sending it at full resolution is often wasteful, as the content delivery network (CDN) will resize the image for the recipient anyway._

![](https://engineering.fb.com/wp-content/uploads/2019/01/Spectrum2.jpg)

_Resizing the image on the sender’s device reduces the bandwidth required to send the image. As a result, the entire pipeline has minimal payload overhead, improving the end-to-end experience. The remaining challenge is how to maintain image quality while benefiting from the smaller file._

## Spectrum: Building image processing infrastructure

Spectrum makes common image operations simple, efficient, and consistent for mobile developers. Its declarative API allows developers to focus on the desired output properties instead of the individual steps. Subsequently, this allows Spectrum to transparently choose the optimal way to fulfill the transcoding request. For instance, when given the opportunity, Spectrum prefers[lossless operations for cropping and rotating JPEG images](https://libspectrum.io/docs/supported_image_formats). Another example is [resizing](https://libspectrum.io/docs/resizing_images), where Spectrum optimizes the interplay between decoder sampling and pixel-perfect resizing.

“Recipes” help developers choose the optimal execution sequence for the individual requests. Plugins provide these. For example, the JPEG plugin will provide recipes for the lossless cropping and rotation of JPEG images. All recipes are aggregated internally and sorted such that lossless and efficient recipes are at the top. With every request, Spectrum will iterate the list to execute the first matching (and therefore most efficient) recipe. The last resort is a generic recipe that can handle any request by decoding and encoding the image.

The core of Spectrum is written in C++. This allows for sharing between our apps on Android and iOS, thus making our outputs more consistent. The offered [Java](https://libspectrum.io/docs/getting_started_android) and [Objective-C](https://libspectrum.io/docs/getting_started_ios) APIs are just thin wrappers around this core to make development easier. Furthermore, the C++ core provides greater control over allocations and often allows higher execution speed for computational intensive operations.

Integration with native libraries such as [MozJpeg](https://github.com/mozilla/mozjpeg) allows Spectrum to control encoding parameters beyond the general purpose platform APIs. It allows developers to utilize computationally intensive encoding, which requires more processing time but significantly reduces the file size. Examples are trellis quantization and scan optimization. This is an important trade-off on mobile, where a slow network connection can dominate the upload experience. It also allows us to control more advanced parameters such as [chroma subsampling](https://en.wikipedia.org/wiki/Chroma_subsampling) to improve the quality of images with sharp edges and illustrations. The consistent API makes these features accessible to developers who are not image experts.

![The core of the library is implemented in C++. It matches incoming requests against a set of “recipes” that can fulfill the image operation. Here, preference is given to more efficient and lossless operations. Plugins provide support for image formats and additional recipes.](https://engineering.fb.com/wp-content/uploads/2019/01/Spectrum3.jpg)

_The core of the library is implemented in C++. It matches incoming requests against a set of “recipes” that can fulfill the image operation. Here, preference is given to more efficient and lossless operations. Plugins provide support for image formats and additional recipes._

We hope Spectrum will benefit developers in the same way it has helped Facebook create a better image production experience. In our apps, Spectrum has improved the reliability and quality of image uploads at large scale across our apps. The default integration with Mozilla JPEG allows a reduction of up to 15 percent in upload file size compared with a baseline encoder. We are excited to see how the community uses the [Spectrum 1.0.0](https://github.com/facebookincubator/spectrum) library to improve the photo experiences in applications.
