---
title: Announcing Picture Effects for iPad and iPhone
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2010/04/announcing-picture-effects-for-ipad-and-iphone/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:fc0ba920466a44f6'
translated: false
---

> 原文：[Announcing Picture Effects for iPad and iPhone](https://oleb.net/blog/2010/04/announcing-picture-effects-for-ipad-and-iphone/)　·　Ole Begemann

# Announcing Picture Effects for iPad and iPhone

[![Picture Effects Icon](https://oleb.net/media/picture-effects-icon-round-140x140.png)](http://pictureeffectsapp.com)

My new app, [Picture Effects](http://pictureeffectsapp.com), is now available on the App Store. It is a fun photo editor inspired by Apple’s Photo Booth on the Mac. You can distort your photos with some awesome effects like Twirl, Squeeze, Fisheye, etc. And all editing is done in realtime by dragging and pinching across the picture. I am really happy how it turned out. You can buy [Picture Effects on the App Store](http://itunes.apple.com/us/app/picture-effects/id362066808?mt=8) for $2.99.

While this app started out as an iPhone-only project, I have used the last couple of weeks to design a special iPad version and make it a universal app that looks great on both devices. Porting the project to the iPad went quite smoothly. Apple really has done a good job with the new iPhone SDK and the documentation. I am going to write a separate article about my learnings later.

Picture Effects was also my first project that involved OpenGL. To achieve the necessary performance for the realtime manipulation of the photos, I implemented the distortion filters as Open GL [fragment shaders](https://en.wikipedia.org/wiki/Fragment_shader). And while it was surprisingly simple (after I had found some inspiration on the net) to write the actual filter algorithms, the integration of OpenGL rendering with standard UIKit controls and the [MVC pattern](https://en.wikipedia.org/wiki/Model–view–controller) posed some problems on its own that also deserve a separate article in the future.

# Screenshots

Here are a few screenshots of Picture Effects on both the iPhone and iPad:

[![Screenshot 1 of Picture Effects on the iPhone](https://oleb.net/media/pictureeffects-iphone-screenshot-1-213x320.png)](https://oleb.net/media/pictureeffects-iphone-screenshot-1-213x320.png)

[![Screenshot 2 of Picture Effects on the iPhone](https://oleb.net/media/pictureeffects-iphone-screenshot-2-213x320.png)](https://oleb.net/media/pictureeffects-iphone-screenshot-2-213x320.png)

[![Screenshot 3 of Picture Effects on the iPhone](https://oleb.net/media/pictureeffects-iphone-screenshot-3-213x320.png)](https://oleb.net/media/pictureeffects-iphone-screenshot-3-213x320.png)

[![Screenshot of Picture Effects on the iPad](https://oleb.net/media/pictureeffects-ipad-device-screenshot-5.jpg)](https://oleb.net/media/pictureeffects-ipad-device-screenshot-5.jpg)

If you decide to try Picture Effects, I’d be very interested in your feedback.
