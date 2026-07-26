---
title: 'Playground: What’s new in Swift 4'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/05/whats-new-in-swift-4-playground/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:ad0d8aa04de2c366'
translated: false
---

> 原文：[Playground: What’s new in Swift 4](https://oleb.net/blog/2017/05/whats-new-in-swift-4-playground/)　·　Ole Begemann

# Playground: What’s new in Swift 4

I made an Xcode playground that lets you try out many of the new features coming in Swift 4. You can [download it on GitHub](https://github.com/ole/whats-new-in-swift-4).

The cool thing is that you can run the playground right now in Xcode 8.3; you don’t have to wait for the first official Swift 4.0 beta, which will probably come as part of Xcode 9 at WWDC. All you need to do is install [the latest Swift snapshot from swift.org](https://swift.org/download/#snapshots) (don’t worry, it’s easy).

![The What’s new in Swift 4 playground](https://oleb.net/media/whats-new-in-swift-4-playground.png)

# Toolchain installation

1. the snapshots download page on swift.org

  and download the latest snapshot for Xcode.
2. Run the installer to install the snapshot.
3. In Xcode, go to _Xcode \> Toolchains \> Manage Toolchains…_ and select the snapshot. It might be a good idea to quit and relaunch Xcode after switching snapshots. I had occasional problems with syntax highlighting and error reporting, and a relaunch fixed them.

  ![Toolchain selection in Xcode 8.3](https://oleb.net/media/xcode-8-3-toolchain-dialog.png)

  <sub>Toolchain selection in Xcode.</sub>

I plan to keep the playground up to date over the summer as Swift 4.0 matures and more features get implemented.

1. You can choose between two branches: _Trunk Development_ (the master branch) and _Swift 4.0 Development_. I recommend the latter because that’s the branch the final Swift 4.0 release will be made from. [↩︎](#fnref:snapshots)
