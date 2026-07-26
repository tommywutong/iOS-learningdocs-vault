---
title: Inertia, Bouncing, and Rubber-Banding
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/05/scrollview-inertia-bouncing-rubberbanding/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ffe8007288f80229'
translated: false
---

> 原文：[Inertia, Bouncing, and Rubber-Banding](https://oleb.net/blog/2014/05/scrollview-inertia-bouncing-rubberbanding/)　·　Ole Begemann

# Inertia, Bouncing, and Rubber-Banding

In my [Understanding UIScrollView](https://oleb.net/blog/2014/04/understanding-uiscrollview/) post I showed how to write a minimum viable scroll view — one that lacked many essential features that make `UIScrollView` such a pleasure to use. Meanwhile, others have taken my article as an inspiration and added more functionality.

Rounak Jain used [Facebook’s Pop library](https://github.com/facebook/pop) to add inertial scrolling and wrote [a great article](http://iosdevtips.co/post/84571595353/replicating-uiscrollviews-deceleration-with-facebook) about it. [Grant Paul](http://grantpaul.com) then [added bouncing and rubber-banding](https://github.com/grp/CustomScrollView/tree/custom-scroll-with-pop) to it, again using Pop’s decay and spring animations. Awesome work!
