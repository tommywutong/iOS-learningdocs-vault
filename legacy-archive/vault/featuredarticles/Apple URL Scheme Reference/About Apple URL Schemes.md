---
title: Apple URL Scheme Reference
apple_id: TP40007899
resource_type: Guide
platform: watchOS|Safari (Mobile)|Safari|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/Introduction/Introduction.html
archived_at: '2026-07-18T02:29:23.170958Z'
---
> 导航：[总目录](../../README.md) · [featuredarticles](../../_indexes/featuredarticles.md)


[Next](Mail%20Links.md)

# About Apple URL Schemes

This document describes several URL schemes that are supported by system apps on iOS, macOS, and watchOS 2 and later. Native iOS apps and web apps running in Safari on any platform can use these schemes to integrate with system apps and provide a more seamless experience for the user. For example, if your iOS app displays telephone numbers, you could use an appropriate URL to launch the Phone app whenever someone taps one of those numbers. Similarly, clicking an iTunes link launches the iTunes app and plays the song specified in the link. When a user clicks a link, what happens depends on the platform and the installed system apps.

This document describes those schemes that require special attributes or special formatting in order to be understood by the associated system app. As a result, this document does not describe all URL schemes supported on different Apple platforms.

You should read this document if you want to launch a system app from your iOS or macOS app, or from your web app running in Safari. This document contains both Cocoa Touch sample code—using the [openURL:options:completionHandler:](https://developer.apple.com/documentation/uikit/uiapplication/1648685-open) method of the shared `UIApplication` object to open URLs—and HTML samples.

### Composing Items Using Mail

Use the `mailto` scheme to open the Mail app and populate a new email with information.

### Starting a Phone or FaceTime Conversation

Use the `tel` and `facetime` schemes to initiate telephone or video conversations.

### Specifying Text Messages

Use the `sms` scheme to compose a text message and specify a recipient.

### Opening Locations in Maps

Use specially formatted URLs to open the Maps app and display directions or locations.

### Opening Items in iTunes

Use specially formatted URLs to open iTunes and display items in the iTunes Music Store.

### Opening YouTube Videos

Use specially formatted URLs to open YouTube videos in Safari.

[Next](Mail%20Links.md)

