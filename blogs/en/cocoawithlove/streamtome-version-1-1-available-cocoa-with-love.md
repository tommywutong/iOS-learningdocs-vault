---
title: 'StreamToMe Version 1.1 available | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/09/streamtome-version-11-available.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:57b8ba0025e541c0'
translated: false
---

> 原文：[StreamToMe Version 1.1 available | Cocoa with Love](https://www.cocoawithlove.com/2009/09/streamtome-version-11-available.html)　·　Cocoa with Love (Matt Gallagher)

The latest version of [StreamToMe](http://zqueue.com/streamtome/index.html) — for streaming audio and video from your Mac to your iPhone/iPod Touch — is [now available on the App Store](http://itunes.apple.com/WebObjects/MZStore.woa/wa/viewSoftware?id=325327899&mt=8). It has only been one month [since I released version 1.0](https://www.cocoawithlove.com/2009/08/streamtome-iphone-app-released.html) but I have lots of new changes to share.

## New Features

> download the latest version of ServeToMe
> 
> to take advantage of these new features.

### The "Seek to anywhere" update

StreamToMe version 1.1 adds a number of requested features, most prominent of which is "seek to anywhere". You no longer need to wait for the end of the file to be encoded before you jump ahead — you can seek to anywhere at anytime and it will "just work".

### Remote WiFi and 3G access

StreamToMe now supports connections via 3G and from non-local WiFi locations. Bitrates between 96k and 1600k are chosen by the iPhone based on the available data rate. These lower bitrates are also available on local WiFi connections for situations where interference means a lower bitrate is required.

A remote connection requires that you have configured your Mac's network to make ServeToMe's port accessible remotely. This configuration is left to you since it is dependent on how you are connected to the internet, your modem/router and firewalls.

### Password protection

To protect access to your files (especially when made available over the internet) you can now password protect the server.

## Minor changes and fixes

Of course, there are numerous little fixes and changes too:

- Fixed playback of many common MOV codecs, so many more Quicktime MOV files will be supported.
- The server now only encodes video as needed, resulting in much lower average CPU usage.
- Fixes for occasional broken socket (network dropout) problems on Snow Leopard.
- Fixes for session ID problems that caused "The requested file couldn't be converted for streaming" to be incorrectly sent for supported files.
- Scroll indexes now used for large directories.
- Shinier file and folder icons.

## Still coming...

I can't deliver everything all at once but the following frequently requested features are still planned for a future version:

- Windows support for ServeToMe
- Alternate audio tracks
- Subtitles
- Thumbnail previews

## Screenshots

Here are some screenshots of the updated application in action:

![](https://www.cocoawithlove.com/assets/objc-era/screenshot3.png)

![](https://www.cocoawithlove.com/assets/objc-era/screenshot1.png)

![](https://www.cocoawithlove.com/assets/objc-era/screenshot5.png)
