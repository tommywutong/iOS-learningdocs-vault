---
title: Updated OBShapedButton
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/04/updated-obshapedbutton/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:3593d6b828658022'
translated: false
---

> 原文：[Updated OBShapedButton](https://oleb.net/blog/2011/04/updated-obshapedbutton/)　·　Ole Begemann

# Updated OBShapedButton

I finally found the time to fix some embarrassing bugs in my [`OBShapedButton`](https://github.com/ole/OBShapedButton) class to create non-rectangular tap targets on iOS, which I [introduced in October 2009](https://oleb.net/blog/2009/10/obshapedbutton-non-rectangular-buttons-on-the-iphone/).

The updated code should now also work with non-symmetrical button shapes and on the iPhone 4’s retina display. Thanks to all of you who reported bugs and fixes.

![The demo project for OBShapedButton](https://oleb.net/media/obshapedbutton-demo.png)

<sub>The demo project for OBShapedButton.</sub>
