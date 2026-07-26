---
title: The Core Data Book
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2015/12/core-data-book/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:781c0872d601e54d'
translated: false
---

> 原文：[The Core Data Book](https://oleb.net/blog/2015/12/core-data-book/)　·　Ole Begemann

# The Core Data Book

[![Core Data Book Cover](https://oleb.net/media/core-data-book-cover.png)](https://www.objc.io/books/core-data/)

Florian Kugler and Daniel Eggert’s [new book about Core Data](https://www.objc.io/books/core-data/) is now available. I also had a small part in this as the technical reviewer.

My favorite thing about the book is that it is way more than a collection of how-tos for various features. Florian and Daniel explain _how_ all levels of Core Data work, from the managed object context down to the persistent store. They teach you how to use this knowledge to choose the right concurrency model for your application (there isn’t one right answer) and to avoid performance pitfalls.

In the section on concurrency and syncing, they discuss tons of stuff you won’t find covered elsewhere in this much detail. (The sample app uses CloudKit as the server component, but it’s fully applicable to any other typical web service.)

I really enjoyed working with Daniel and Florian on this project. I learned a lot from them, not just about Core Data, but also about app architecture. For instance, they wrote an abstraction for the sync engine that allows them to replace the calls to CloudKit with another implementation that just logs the commands that should be sent to the server. What started as a workaround to allow readers to run the sample app without provisioning problems turned into something that can be used in testing.

The authors have fully embraced Swift. The sample code is a great learning resource for using Cocoa effectively in Swift. Daniel and Florian teach some nice patterns to make Cocoa APIs (not just Core Data) safer and more pleasant to use when called from Swift.

I highly recommend the book.
