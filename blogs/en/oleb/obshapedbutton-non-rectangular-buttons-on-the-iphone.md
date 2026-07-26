---
title: 'OBShapedButton: Non-Rectangular Buttons on the iPhone'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2009/10/obshapedbutton-non-rectangular-buttons-on-the-iphone/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:4481ddfb5de911b0'
translated: false
---

> 原文：[OBShapedButton: Non-Rectangular Buttons on the iPhone](https://oleb.net/blog/2009/10/obshapedbutton-non-rectangular-buttons-on-the-iphone/)　·　Ole Begemann

# OBShapedButton: Non-Rectangular Buttons on the iPhone

`UIButton` has always been capable of displaying buttons with arbitrary non-rectangular shapes. All you have to do is use PNG images with alpha channels to define the transparent parts of the bounds rectangle.

While a button’s shape may be arbitrary, UIButton always responds to touches within its entire bounds, however. This could cause problems and confusion for the users, especially when multiple non-rectangular buttons are placed close together so that their frames overlap.

`OBShapedButton` is a replacement for UIButton that solves this issue. Instances of OBShapedButton only respond to touches where the button image is non-transparent. Here’s how to use it:

- Get the code from GitHub

  .
- ,

  ,

  , and

  to your Xcode project.
- Design your UI in Interface Builder with UIButtons as usual. Set the Button type to Custom and provide transparent PNG images for the different control states as needed.
- In the Identity Inspector in Interface Builder, set the Class of the button to OBShapedButton.

That’s it! Build and run the enclosed demo project to check it out. I am releasing this under the [MIT license](http://www.opensource.org/licenses/mit-license.php).

**Update April 24, 2011:** Many of you reported serious bugs with this class over the past 18 months, including wrong calculations of translation matrices and some obvious omissions that caused the class to not work with non-symmetrical shapes, non-correctly sized images, and the retina display. Thanks to everyone who identified the bugs and often even included a fix. I finally managed to update the code. [Get the updated code from GitHub](https://github.com/ole/OBShapedButton).
