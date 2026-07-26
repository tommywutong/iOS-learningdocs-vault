---
title: Another issue with SwiftPM Xcode integration
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2020/03/04/another-issue-with-swiftpm-xcode-integration/'
original_language: en
published: 2020-03-04
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:91f9d9544e31df99'
translated: false
---

> 原文：[Another issue with SwiftPM Xcode integration](https://www.jessesquires.com/blog/2020/03/04/another-issue-with-swiftpm-xcode-integration/)　·　Jesse Squires

I recently [wrote about using SwiftPM instead of CocoaPods](https://www.jessesquires.com/blog/2020/02/24/replacing-cocoapods-with-swiftpm/), which included a list of pros and cons. While working on one of my projects that is using SwiftPM, I realized another issue with how SwiftPM currently integrates with Xcode.

I mentioned that there is no equivalent of a `Pods/` directory with SwiftPM and that package dependencies are stored in Xcode’s derived data directory, `~/Library/Developer/Xcode/DerivedData/`. This is problematic beyond not being able to check-in dependencies into source control. What I failed to realize at the time are the implications for cleaning or deleting derived data, which unfortunately is often necessary when working with Xcode. In fact, I have a custom shell command for doing this (which I call `xcclean`), and it runs `rm -rf ~/Library/Developer/Xcode/DerivedData`. Most folks I know have something similar, because Xcode.

This will not work if you are using SwiftPM. If you completely nuke your `DerivedData/` directory and then attempt to build your project, it will fail to build with the error “Missing package product” for each package. To trigger re-downloading, you must choose `File > Swift Packages > Resolve Package Versions`. What a pain this would be if you were working without an Internet connection.

Luckily, simply “cleaning” your build folder by choosing `Product > Clean Build Folder` in the Xcode file menu, or `cmd+shift+K` will do the correct thing, and leave your package sources intact.

I suppose I will have to update my `xcclean` command to be smarter.
