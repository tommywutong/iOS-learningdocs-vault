---
title: Advanced Swift, third edition
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/11/advanced-swift-3/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:38a4792843acabda'
translated: false
---

> 原文：[Advanced Swift, third edition](https://oleb.net/blog/2017/11/advanced-swift-3/)　·　Ole Begemann

# Advanced Swift, third edition

![Advanced Swift Cover](https://oleb.net/media/advanced-swift-3.0-cover-600px.png)

**Today we’re releasing the third edition of our book _[Advanced Swift](https://www.objc.io/books/advanced-swift/)_, updated for Swift 4.**

_Advanced Swift_ is the book for people who have read Apple’s _The Swift Programming Language_ and/or have been using Swift for some time and now want to dig deeper and really understand how everything works. It’s a book about Swift the language, not about iOS or macOS programming (though we do use Apple’s frameworks in some examples).

# New content

The new edition has been thoroughly updated and expanded for Swift 4. The highlights:

- encoding and decoding

  .
- chapter has a brand-new section on

  key paths

  , plus more about subscripts, property observers, lazy properties, and escaping vs. non-escaping closures.
- chapter grew by more than 40%, with lots of new examples and more in-depth explanations.
- chapter is easier to follow now.
- (although not all ranges are collections).
- chapter now includes a step-by-step guide how to set up a C library for use with the Swift Package Manager.

Plus a ton of small revisions and additions throughout the book. All in all, the book is approximately 20% longer than last year’s edition (from 376 to 458 pages for the paperback).

# Xcode playgrounds

The e-book download of _Advanced Swift_ also includes the full text of the book in the form of Xcode playgrounds (one playground per chapter). This means you can read the book on your Mac and play with the sample code directly inline.

![Screenshot of the Strings chapter of Advanced Swift in an Xcode 9.1 playground](https://oleb.net/media/advanced-swift-playground-screenshot-xcode-2212px.png)

<sub>_Advanced Swift_ in an Xcode playground.</sub>

Last year, we only offered a playground for the Swift Playgrounds app on iOS because the iOS app’s playground book file format allowed us to hide helper code that didn’t appear in the book but was necessary to run the examples. Xcode’s playground file format doesn’t support this — at least not in a way that’s easy for us to adopt.[1](#fn:1) As a consequence, you’ll come across blocks of utility code (marked as hidden with comments but fully visible). Feel free to ignore these.

Ultimately, while the iPad is a great match for reading a book, we feel that having the code available on your Mac is worth the slight inconvenience.[2](#fn:2) And you can still use the playgrounds on your iPad if you wish. Just copy the `.playground` files to iCloud Drive and open them in the Swift Playgrounds app.

# How to buy

You can [buy the e-book at objc.io](https://www.objc.io/books/advanced-swift/). The e-book download includes PDF, ePub, and Mobi (Kindle) files, all DRM-free. This version also includes the Xcode playgrounds. If you have bought any of the previous editions of the e-book, this is a free update for you.

If you prefer a printed book, you can order the paperback on [Amazon](https://www.amazon.com/Advanced-Swift-Updated-4/dp/1979725454/) ([amazon.com](https://www.amazon.com/Advanced-Swift-Updated-4/dp/1979725454/), [amazon.de](https://www.amazon.de/Advanced-Swift-Updated-4/dp/1979725454/), [amazon.co.uk](https://www.amazon.co.uk/Advanced-Swift-Updated-4/dp/1979725454/)).

---

Working on _Advanced Swift_ has become an annual highlight for me. I enjoy the work very much, and while there’s obviously never enough time to make everything perfect, I’m very proud of the result. If you decide to buy the book, thank you! I hope you enjoy it.

1. Xcode playgrounds _do_ support “hidden” utility code placed in a separate file, but that isn’t easy to support for our build system. We’d have to make a bunch of stuff `public` for the playground code to be able to see it in the other file, but we don’t those distracting annotations in the book. [↩︎](#fnref:1)
2. Due to [a bug in Xcode 9.1](https://twitter.com/justkwin/status/926488735025369089), playgrounds always switch back to the raw markup view when you go to another page. I hope this gets fixed soon. Until then, you’ll have to manually switch back to the rendered view using _Editor \> Show Rendered Markup_. [↩︎](#fnref:2)
