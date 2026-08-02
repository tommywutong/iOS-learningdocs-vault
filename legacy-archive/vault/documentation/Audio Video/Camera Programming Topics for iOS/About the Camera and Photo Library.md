---
title: Camera Programming Topics for iOS
apple_id: TP40010400
resource_type: Guide
platform: tvOS|iOS
topic: Audio, Video, & Visual Effects
technology: UIKit
published: '2012-07-17'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/CameraAndPhotoLib_TopicsForIOS/Introduction/Introduction.html
archived_at: '2026-07-15T05:21:02.201369Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Taking%20Pictures%20and%20Movies.md)

# About the Camera and Photo Library

iOS provides two technologies for taking pictures and movies.

- The [UIImagePickerController](https://developer.apple.com/documentation/uikit/uiimagepickercontroller) class provides basic, customizable user interfaces for taking pictures and movies and for giving the user some simple editing capability for newly-captured media. Use an image picker controller when you do not require a fully-custom solution.
- The AV Foundation framework provides flexible and powerful classes you can use, along with UIKit, to create fully-customized still image or movie capture for your app.

With either option, you can use the Assets Library framework to manage media metadata such as GPS location information.

Similarly, iOS provides two technologies for providing a user interface for picking saved pictures and movies from the user’s photo albums.

- Instantiate a `UIImagePickerController` object as a media browser to let the user pick an item from their photo library, using a basic, system-supplied user interface.
- Alternatively, you can create a fully-customized picture and movie browser using the Assets Library framework along with UIKit.

This document explains how to use an image picker controller for taking pictures and movies, and for choosing saved media. The steps are very similar for both tasks, as explained in this document’s articles.

To learn how to use the AV Foundation framework for fully-customized media capture, see [Media Capture](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/AVFoundationPG/Articles/04_MediaCapture.html#//apple_ref/doc/uid/TP40010188-CH5) in _[AVFoundation Programming Guide](../AVFoundation%20Programming%20Guide/About%20AVFoundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcoby)_.

For details on the Assets Library framework, which supports the creation of fully-customized media browsers, see _[Assets Library Framework Reference](https://developer.apple.com/documentation/assetslibrary)_.

This document includes the following articles:

- [Taking Pictures and Movies](Taking%20Pictures%20and%20Movies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydimbwfvjvomi) explains how to instantiate an image picker controller with a camera interface, and how to obtain the newly captured media when a user takes a picture or movie.
- [Picking an Item from the Photo Library](Picking%20an%20Item%20from%20the%20Photo%20Library.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydimbyfvjvomi) explains how to use an image picker controller as a media browser, allowing the user to pick an item from the device’s photo library.

[Next](Taking%20Pictures%20and%20Movies.md)

