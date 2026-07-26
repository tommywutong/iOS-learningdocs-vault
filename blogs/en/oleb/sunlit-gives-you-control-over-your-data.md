---
title: Sunlit Gives You Control Over Your Data
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/01/sunlit-gives-you-control-over-your-data/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:4fc5ea26c062c3d2'
translated: false
---

> 原文：[Sunlit Gives You Control Over Your Data](https://oleb.net/blog/2014/01/sunlit-gives-you-control-over-your-data/)　·　Ole Begemann

# Sunlit Gives You Control Over Your Data

![Screenshots of Sunlit for the iPhone](https://oleb.net/media/sunlit-app-screenshots-1280px.jpg)

After my previous post about the [data lock-in of the Storehouse app](https://oleb.net/blog/2014/01/storehouse/), I would be remiss not to mention [Sunlit](http://sunlit.io), Manton Reece’s new app that was released on the same day as Storehouse. The two apps are actually quite different, but they both try to solve a similar need: provide an easy way to create stories around your photos and share them with others on the web.

There is one crucial difference, though: by using Sunlit you don’t give up control over the content that you create. While the app does publish your story under the [sunlit.io](http://sunlit.io) domain, it uses the [App.net file storage](http://blog.app.net/2013/01/28/announcing-the-app-net-file-api/) to store the actual content — and that includes not only the images but also a static HTML file that you can easily copy over to your own server to publish the story under your control.[1](#fn:1) Manton has written about [how it works and they decided to do it this way](http://www.manton.org/2014/01/sunlit_sync_and.html):

> We think this approach makes the whole system a lot more flexible and open. Your data is never hidden inside the app and your published pages are never locked behind a server.

# The Best of Both Worlds

I love this approach. It makes the app useful for people like me who like the idea of having an easy-to-use publishing interface but want to retain control of their content while keeping it simple for users who don’t want to deal with this kind of stuff. And it is no accident that an app like this comes from Manton Reece. By [switching from Twitter to App.net](http://www.manton.org/2013/01/three_months_without.html), Manton has already shown that he cares deeply about corporate data silos. Kudos!

1. Support for this use case is not quite perfect because the HTML references images with their absolute URLs on App.net, so you would have to manually edit the HTML if you also wanted to copy the photos over to another server. I would prefer if Sunlit uploaded another version of the HTML file with relative references to dependencies. [↩︎](#fnref:1)
