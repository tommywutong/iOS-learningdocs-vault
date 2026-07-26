---
title: 'Friday Q&A 2009-12-04: Building Standalone iPhone Web Apps'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-12-04-building-standalone-iphone-web-apps.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4f7ccec239546a1f'
translated: false
---

> 原文：[Friday Q&A 2009-12-04: Building Standalone iPhone Web Apps](https://www.mikeash.com/pyblog/friday-qa-2009-12-04-building-standalone-iphone-web-apps.html)　·　mikeash.com Friday Q&A

Posted at 2009-12-04 19:29 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-12-11: A GCD Case Study: Building an HTTP Server](https://www.mikeash.com/pyblog/friday-qa-2009-12-11-a-gcd-case-study-building-an-http-server.html)  
Previous article: [Friday Q&A 2009-11-27: Using Accessors in Init and Dealloc](https://www.mikeash.com/pyblog/friday-qa-2009-11-27-using-accessors-in-init-and-dealloc.html)  
Tags: [html](https://www.mikeash.com/pyblog/?tag=html) [iphone](https://www.mikeash.com/pyblog/?tag=iphone) [javascript](https://www.mikeash.com/pyblog/?tag=javascript) [web](https://www.mikeash.com/pyblog/?tag=web)

Friday Q&A 2009-12-04: Building Standalone iPhone Web Apps

by [Mike Ash](https://www.mikeash.com/)

iPhone web apps have been in the news a fair bit lately as a way to bypass Apple's troublesome review process. While web apps aren't as capable as native apps, and almost certainly never will be, they're still interesting to work with simply because they're so much simpler to develop and deploy.

[Neven Mrgan's Pie Guy](http://mrgan.com/pieguy/) is perhaps the most prominent example. It's a complete Pac-Man look-alike built as a standalone web app, albeit one which, because it's all HTML and JavaScript, requires a 3GS to run smoothly.

While the ability to build apps like this is well known, I haven't seen anything that gathers all the requisite parts in one place and walks through how to build one, so that's my intent today. I cribbed much of this information from dissecting how Pie Guy does it, and don't think for a moment that I discovered any of this stuff myself.

**Getting Started**  
 In this post I'll walk through the process of creating a basic standalone web app. My example app simply queries the JavaScript location object and displays your latitude and longitude. You can [try the completed app](http://mikeash.com/PhoneWebApp/), or get its source with Subversion:

```
    svn co http://mikeash.com/svn/PhoneWebApp
```

The scope of this post is simply building the parts that are special to iPhone standalone web apps. The actual HTML and JavaScript for the app functionality itself is beyond the scope of the discussion, but there are of course a wide range of resources out there for them.

**Separate Program** The first thing that you want in a standalone web app is for it to start as its own program, rather than loading into Safari, when the user taps your icon on the home screen. To make this happen, you simply add a `` tag to your ``setting `apple-mobile-web-app-capable` to `yes`, like so:

```
    <meta name="apple-mobile-web-app-capable" content="yes">
```

While you're in there, it can be useful to set the viewport of your web page to achieve 1x zoom instead of the default (which is around ⅓x zoom), and to disallow the user from changing the zoom factor. This helps make your web page act more like a real app. You can do this by adding another

tag:

```
    <meta name="viewport"
          content="width=device-width; height=device-height; initial-scale=1.0; maximum-scale=1.0; user-scalable=no;">
```

**Icons and Startup Images**  
 Another thing that's a must for real iPhone apps is to have an actual icon and a startup image that's displayed while the app is loading. You can specify an icon by referencing it in a `` tag with `apple-touch-icon-precomposed` set as the relationship, and you can specify a startup image with `apple-touch-startup-image`:

```
    <link rel="apple-touch-icon-precomposed" href="icon.png">
    <link rel="apple-touch-startup-image" href="default.png">
```

The images themselves need to be 57x57 for the icon and 320x460 for the startup image.

**``**  
 Putting the above together, and with the page title and link to the app's JavaScript code, the entire `` tag looks like this:

```
    <head>
        <title>PhoneWebApp</title>
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="viewport" content="width=device-width; height=device-height; initial-scale=1.0; maximum-scale=1.0; user-scalable=no;">
        
        <link rel="apple-touch-icon-precomposed" href="icon.png">
        <link rel="apple-touch-startup-image" href="default.png">
        
        <script src="main.js" type="text/javascript" />
    </head>
```

**Body**  
 The body of the page is, of course, where you put all the stuff for your web app to interact with the user. Beyond the basic functionality of your app, you'll also want some iPhone-specific sections. You'll want to display a different page to users who view the app on a non-iPhone browser, to tell them to reload it with an iPhone. You'll also want to display a different page to users who view the app on an iPhone, but who have not yet installed it, to tell them how to install it.

For this particular app, I also have three more pages. One is a "loading" page, which is visible on initial load and gives the computer something to display until the JavaScript kicks in. One is a page to display in case navigation services aren't available for some reason. And finally, I hae the real page that displays the navigation data.
