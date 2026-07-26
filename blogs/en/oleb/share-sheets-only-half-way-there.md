---
title: 'Share Sheets: Only Half Way There'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/02/share-sheets-only-half-way-there/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c328d2bd861cebdc'
translated: false
---

> 原文：[Share Sheets: Only Half Way There](https://oleb.net/blog/2012/02/share-sheets-only-half-way-there/)　·　Ole Begemann

# Share Sheets: Only Half Way There

When I read the news about OS X Mountain Lion yesterday, one of the most exciting new features was the concept of [Share Sheets](http://www.apple.com/macosx/mountain-lion/features.html#sharesheet), the system-wide component that enables any app to let users easily share content with a number of popular OS and web services.

# Not Extensible by Third-Party Apps

At the time, I assumed that this service was completely open to third party apps. Apps should not only be able to _show_ the system-wide sharing UI; they should also be allowed to offer _additional_ sharing services that would then be displayed among the built-in options by any other app that supported share sheets.

This seems to be a sensible idea, after all. Different users have different sharing preferences and while the list of built-in services includes some high-profile sites like Twitter, Flickr and Vimeo, it is hardly complete (not to mention the dozens of new services that spring up every year, like Instagram).

Sadly, according to [Nilay Patel’s Mountain Lion preview for The Verge](http://www.theverge.com/2012/2/16/2801047/mac-os-x-10-8-mountain-lion-preview-photos-video), this is not the case:

> There’s an API that lets developers add share buttons to third party apps, but there’s no way to add additional services — a pity, since Facebook and YouTube are notable omissions.

On OS X, this limitation is actually not that big a deal. In fact, OS X makes manual sharing between one app and another or between an app and the web so easy that the whole idea of a system-wide UI component for sharing seems almost superfluous. I can just as quickly copy and paste or drag and drop a URL from the browser to the Twitter app as I can tweet about it using a share sheet.

What I am worried about is what this means for iOS.

# A Missed Opportunity for iOS?

On iOS, sharing content between apps is hard. Yes, there is copy and paste but repeatedly switching between apps still takes a lot of effort. And sharing content via URL schemes only works if the sending app explicitly supports the receiving app’s format, which is a problem whose solution just doesn’t scale.

Moreover, iOS could soon be at a major disadvantage compared to its competitors when it comes to sharing content. Both Android (with its existing system of [Activities and Intents](https://developer.android.com/training/sharing/send.html)) and soon Windows (Phone) (with [Contracts](http://msdn.microsoft.com/en-us/library/windows/apps/hh464906.aspx) coming in Windows 8) offer a system-wide solution for apps to interact with each other. Meanwhile, iOS only offers built-in sharing via e-mail, SMS/iMessage and Twitter.

Imagine if Apple not only ported the existing share sheets API to iOS 6 but also added third-party extensibility along the way. Any app, be it from Apple or a third-party developer, could announce via its `Info.plist` the types of content (text, URLs, photos, videos, etc.) it understands. And every app that had something to share would, when the user taps its share button, ask the OS to display a list of apps that can deal with the current content. The system’s sharing service would automatically launch the app the user selected and ask it to display its special sharing view controller^[1](#fn:1).

Any app that implemented share sheets would automatically support any other app that can deal with the same content type. You could send URLs from Safari directly to the Instapaper app, without having to install a bookmarklet. A photo editing app would support uploading to any photo service without having to implement dozens of APIs^[2](#fn:2). You could post your high score from any game to your social network of choice. The possibilities are endless.

I can only hope Apple will still do this for iOS 6. Seeing only part of it in Mountain Lion makes me pessimistic.

**Update February 20, 2012:** I wrote a follow-up to this article: [What iOS Should Learn from Android and Windows 8](https://oleb.net/blog/2012/02/what-ios-should-learn-from-android-and-windows-8/).

1. Optionally, an app could perhaps act to share things silently without displaying its own UI. In that case, the sharing service could just call a special block of code in the receiving app’s executable that automatically uploads the content. In such a scenario, sending a URL to Instapaper would be even more seamless. [↩︎](#fnref:1)
2. And the companies that run the photo services could concentrate on an app that excels in uploading new content and browsing the existing site rather than investing in photo editing and filtering capabilities that other, specialized apps could do better. [↩︎](#fnref:2)
