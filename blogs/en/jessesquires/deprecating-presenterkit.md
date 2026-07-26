---
title: Deprecating PresenterKit
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2021/11/06/deprecating-presenterkit/'
original_language: en
published: 2021-11-06
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:dd7d4c2659b3ed29'
translated: false
---

> 原文：[Deprecating PresenterKit](https://www.jessesquires.com/blog/2021/11/06/deprecating-presenterkit/)　·　Jesse Squires

I’ve decided to deprecate one of my open source libraries, [PresenterKit](https://github.com/jessesquires/presenterkit). The library has been in a sort of “maintenance mode” for awhile now. It never really became what I hoped and anticipated. I think it implemented some neat ideas and helped removed some boilerplate from UIKit, but I don’t think what it provided necessarily justified a library anymore — at least not given the lack of activity around the project.

The goal of PresenterKit was to streamline the view controller presentation APIs in iOS and provide some helpful extensions, as well as offer interesting and useful custom presentation controllers. Many of the extensions are still worthwhile, but can be easily added to a project directly — no need for a library. As for custom presentation controllers, I only ever had time to add one, a [“half modal” presentation controller](https://jessesquires.github.io/PresenterKit/Classes.html#/c:@M@PresenterKit@objc(cs)HalfModalPresentationController), which has essentially been obsoleted by the [new and more modular `UISheetPresentationController`](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller). Finally, with SwiftUI on the horizon, this kind of library had a limited lifespan already.

If you are using PresenterKit, there’s honestly no need to be worried that it’s now deprecated. It doesn’t do anything complicated or unorthodox in UIKit. The code is straightforward and hasn’t needed to change significantly for years. I expect it should continue to work fine — and without warnings or other issues for the foreseeable future. The deprecation is mostly a notice that this project is entering a new phase, namely that I won’t be devoting any more time to it. If you are only using parts of the library, I would suggest that you just add them directly to your codebase.

The repo is still [available on GitHub](https://github.com/jessesquires/presenterkit), though now archived and read-only. A final release has been tagged on GitHub and pushed to CocoaPods to communicate the deprecation. If you have any questions, feel free to reach out.
