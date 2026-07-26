---
title: Porting RRGlossCausticShader to the iPhone
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2010/02/porting-rrglosscausticshader-to-the-iphone/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:fd2b0043854e71a5'
translated: false
---

> 原文：[Porting RRGlossCausticShader to the iPhone](https://oleb.net/blog/2010/02/porting-rrglosscausticshader-to-the-iphone/)　·　Ole Begemann

# Porting RRGlossCausticShader to the iPhone

[![Screenshot of the iPhone sample app for the gloss caustic shader](https://oleb.net/media/gloss-caustic-shader-screenshot.png)](https://oleb.net/media/gloss-caustic-shader-screenshot.png)

<sub>Screenshot of the iPhone sample app for the gloss caustic shader.</sub>

In September 2008, Matt Gallagher published [Drawing gloss gradients in CoreGraphics](http://cocoawithlove.com/2008/09/drawing-gloss-gradients-in-coregraphics.html), a very nice piece of code that will draw a ‘gloss’ gradient in a single statement. All colors in the gradient are calculated from the single color parameter. Roy Ratcliffe later [complemented Matt’s article](http://blog.pioneeringsoftware.co.uk/2008/12/09/gloss-caustic-shading) with a generalized Objective-C class called `RRGlossCausticShader` that exposes a number of parameters to modify the gloss effect to your liking. [Roy’s code](https://github.com/royratcliffe/gloss-caustic-shader/tree/master) also includes a nice OS X sample application that helps visualizing the effects of parameter changes on the final result. Unfortunately, neither Matt’s original version nor Roy’s refactoring work on the iPhone out of the box, mainly because they rely on [NSColor](https://developer.apple.com/mac/library/documentation/Cocoa/Reference/ApplicationKit/Classes/NSColor_Class/Reference/Reference.html), which is only available on the Mac platform. I recently ported Roy’s code to the iPhone and also wrote a little iPhone sample app for it. Porting was fairly easy:

- Use conditional compilation (`#if TARGET_OS_IPHONE`) to substitute [UIColor](http://developer.apple.com/iphone/library/documentation/UIKit/Reference/UIColor_Class/index.html) for NSColor.
- Add some functionality that NSColor has but UIColor lacks, namely getting individual color component values and converting colors between RGB and HSB.

For the iPhone sample app, I wanted to do a little more than just copy the existing OS X app, so I added a button to print the shader’s current settings to the debugger console. That way, you can play with the sliders until you find a shading you like and then just copy and paste the code from the console to your project to configure the shader with the correct settings. The app will also save the current settings to the user defaults on exit.

[![Screenshot of the debugger console with the iPhone gloss caustic shader sample app running](https://oleb.net/media/gloss-caustic-shader-settings-console-screenshot.png)](https://oleb.net/media/gloss-caustic-shader-settings-console-screenshot.png)

<sub>You can print the gloss caustic shader's current settings to the debugger console and copy and paste them into your code from there.</sub>

Here are a few example shadings that can be created with `RRGlossCausticShader`:

[![Gloss caustic shader examples](https://oleb.net/media/gloss-caustic-shader-examples.png)](https://oleb.net/media/gloss-caustic-shader-examples.png)

**Updates:**

**March 5, 2010:** Message from Roy:

> Excellent work Ole! I’ve [merged your enhancements](https://github.com/royratcliffe/gloss-caustic-shader/) as requested, albeit with a few more enhancements. Makes you wonder: where should it go from here?

**April 14, 2010:** Message from [tato123](http://www.glassboxdesigns.com/):

> I had to make a change for iPad SDK 3.2+, for some reason the gradient appeared yellowish at the bottom section. I adjusted the following, in RRGlossCausticShader.m
> 
> From:
> 
> ```
> void RRGlossCausticShaderEvaluate
> …
> CGFloat f = RRExponentialFunctionEvaluate(&INFO(exponentialFunction), 2*(x – 0.5f));
> …
> ```
> 
> To:
> 
> ```
> void RRGlossCausticShaderEvaluate
> …
> CGFloat f = RRExponentialFunctionEvaluate(&INFO(exponentialFunction), 0.7*(x – 0.5f));
> …
> ```
