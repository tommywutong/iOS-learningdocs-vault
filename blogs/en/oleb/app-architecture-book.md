---
title: App Architecture book
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2018/05/app-architecture-book/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:d453db772ff35856'
translated: false
---

> 原文：[App Architecture book](https://oleb.net/blog/2018/05/app-architecture-book/)　·　Ole Begemann

# App Architecture book

![Book cover: App Architecture: iOS Application Design Patterns in Swift, by Chris Eidhof, Matt Gallagher, and Florian Kugler](https://oleb.net/media/app-architecture-book-cover-900px.jpg)

The final version of [_App Architecture: iOS Application Design Patterns in Swift_](https://www.objc.io/books/app-architecture/), the new book by Chris Eidhof, [Matt Gallagher](https://www.cocoawithlove.com), and Florian Kugler is now available. As with previous [objc.io](https://www.objc.io) books, I had a small part in its creation as the technical reviewer, a job that [I enjoy immensely](https://twitter.com/olebegemann/status/993152885390274560).

I’m obviously biased, but I really recommend the book if you write iOS apps. Although you’ll probably be familiar with some of the architecture patterns discussed in the book, I’m sure you’ll learn something new in each chapter — I certainly did. The authors managed to bring a fresh perspective even to well-known patterns like MVC. While reading the book, I had several aha moments about concepts that are obvious in hindsight but that I never really thought about in the way they are presented in the book.

The book also includes discussions of three more experimental architectures. Writing a full iOS app in one of these patterns requires a stronger commitment to deviate from typical UIKit code (you’ll sometimes be fighting against Apple’s frameworks). But the good news is that you don’t have to switch your whole app to a new architecture to take advantage of its lessons. Most patterns are based on a relatively small set of core ideas, which often can be applied in isolation to existing MVC- or MVVM-based apps.

At any rate, if you haven’t had the chance to try out declarative UI programming (like [React](https://reactjs.org)), the book is a good learning opportunity. UIKit’s imperative style is getting long in the tooth, and I wouldn’t be surprised if Apple’s [rumored cross-platform UI project](https://daringfireball.net/2018/04/scuttlebutt_regarding_ui_project) also took inspiration from [Elm](https://guide.elm-lang.org/architecture/)/React.

Another plus: at a little more than 200 pages, the book is a relatively quick read. And if that’s not enough, there’s an option to buy an additional 7 hours video content that complements the book.
