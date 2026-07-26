---
title: The State of Sharing in iOS 6
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/09/the-state-of-sharing-in-ios-6/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:95e6db7eb6b8e8f1'
translated: false
---

> 原文：[The State of Sharing in iOS 6](https://oleb.net/blog/2012/09/the-state-of-sharing-in-ios-6/)　·　Ole Begemann

# The State of Sharing in iOS 6

In February 2012 I wrote an article outlining [my hope that Apple would introduce more powerful sharing features in iOS 6](https://oleb.net/blog/2012/02/what-ios-should-learn-from-android-and-windows-8/). Now that iOS 6 is out, it’s time to revisit this topic.

# New First-Class Citizens: Facebook and SinaWeibo

iOS 6 still does not have a full-fledged inter-app sharing mechanism. Instead, Apple chose to add two more very popular services, Facebook and [SinaWeibo](https://en.wikipedia.org/wiki/Sina_Weibo), to its existing support for Twitter in [Social.framework](https://developer.apple.com/reference/social). These are welcome additions, but certainly not a bold design that would allow third-party apps to offer their own sharing options.

[![Mobile Safari showing a UIActivityViewController in iOS 6](https://oleb.net/media/ios-6-uiactivityviewcontroller.png)](https://oleb.net/media/ios-6-uiactivityviewcontroller.png)

<sub>`UIActivityViewController` in action.</sub>

# UIActivityViewController

[`UIActivityViewController`](https://developer.apple.com/reference/uikit/uiactivityviewcontroller) is a new class that lets developers display a generic sharing interface to users without any effort. All you have to do is instantiate the view controller with the content you want to share (say, an array containing a string and an image), put it on the screen and it will do the rest.

`UIActivityViewController` creates a list of suitable sharing options (based on the content your app wants to share), presents it to the user and performs the respective action once the user had made a choice. It is very convenient compared to the old way of preparing a `UIActionSheet` with sharing options and handling them all yourself.

# UIActivity

You can even add support for your own custom sharing options and still let `UIActivityViewController` handle the interaction with the user. To do that, subclass the abstract [`UIActivity`](http://developer.apple.com/library/ios/#documentation/UIKit/Reference/UIActivity_Class/Reference/Reference.html) class and override the required methods (see the documentation for details).

A custom `UIActivity` has two tasks: first, it must provide information about itself (activity type, title and image) to the `UIActivityViewController`. Second, it must perform the actual sharing after the user has selected it. For that step, your activity has the option to display a user interface of its own (for example, to ask the user for login credentials) or perform the sharing silently without presenting any additional UI. It’s very straightforward.

# No UIActivity Sharing Between Apps

Apple has created a simple and easy-to-use sharing system. The generic sharing UI and the ability to extend it with custom activities is definitely an improvement over iOS 5 for both users and developers.

The only problem – and it is a big problem – is that the extensibility of `UIActivity` stops at app boundaries. It is not enough that a hypothetical Flickr app offered a generic “`FlickrActivity`”, which then could be used by any app that knew how to share images. On the contrary, _every_ app that wants to be able to upload to Flickr must provide a Flickr activity on its own inside its app bundle.

The obvious reason for this design is that, under the current iOS security model, apps simply cannot communicate or share code between each other. iOS would need some kind of plugin interface to make this work.^[1](#fn:1) Still, the resulting amount of code duplication and ineffeciency is regrettable.

One solution to the dilemma is the open-source community. I’d love to see `UIActivity` implementations for all popular web services that developers can then integrate into their apps. I have already seen activities for [Buffer](http://www.andydev.co.uk/blog/projects/buffer-uiactivity/) and [Instagram](https://github.com/coryalder/DMActivityInstagram) on GitHub. It’s not a perfect solution but it’s the best developers can do.

1. And there is hope that something like this is coming in a future iOS release. But that’s a topic for another blog post. [↩︎](#fnref:1)
