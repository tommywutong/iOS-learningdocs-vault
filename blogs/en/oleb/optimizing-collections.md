---
title: Optimizing Collections
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/06/optimizing-collections-book/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:9cdc96a9c39c0d6f'
translated: false
---

> 原文：[Optimizing Collections](https://oleb.net/blog/2017/06/optimizing-collections-book/)　·　Ole Begemann

# Optimizing Collections

![Optimizing Collections Book Cover](https://oleb.net/media/optimizing-collections-book-cover-600px.png)

A new Swift book is out: [_Optimzing Collections_](https://www.objc.io/books/optimizing-collections/) by [Károly Lőrentey](https://twitter.com/lorentey). I had a small part in this as the book’s technical reviewer, and I highly recommend it.

Károly first released the book as a beta version a few months ago and now the final version has been published through [objc.io](https://www.objc.io).

You’ll learn:

- `Collection`

  protocols.
- copy-on-write

  behavior in your own types.
- How to measure the performance of your custom collection and make it a lot faster than the built-in collection types (for certain tasks; different data structures make different tradeoffs).

This isn’t a book that just scratches the surface. Károly really goes into detail, especially on that last point. I love how practially every chapter ends with a set of charts illustrating the performance characteristics of the code written in that chapter — and those results in turn form the basis for subsequent optimizations in the next chapter.

If you want to get a feel for the book, watch [Károly’s talk at dotSwift 2017](https://www.dotconferences.com/2017/01/karoly-lorentey-optimizing-swift-collections). If you like the talk and would like to learn more, I guarantee you’ll love the book.

Lastly, I think the book is a very nice companion to [_Advanced Swift_](https://www.objc.io/books/advanced-swift/). Collections also play a big role in _Advanced Swift_, but with a different focus: we explore the collection protocols in more detail, but we don’t discuss the performance aspects at the level of _Optimizing Collections_.
