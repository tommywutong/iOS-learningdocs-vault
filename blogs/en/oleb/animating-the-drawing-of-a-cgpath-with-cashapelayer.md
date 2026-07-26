---
title: Animating the Drawing of a CGPath With CAShapeLayer
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2010/12/animating-drawing-of-cgpath-with-cashapelayer/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:adf7224a18abd24c'
translated: false
---

> 原文：[Animating the Drawing of a CGPath With CAShapeLayer](https://oleb.net/blog/2010/12/animating-drawing-of-cgpath-with-cashapelayer/)　·　Ole Begemann

# Animating the Drawing of a CGPath With CAShapeLayer

One of the nice little additions in iOS SDK 4.2 are two new properties for [`CAShapeLayer`](http://developer.apple.com/library/ios/#documentation/GraphicsImaging/Reference/CAShapeLayer_class/Reference/Reference.html): [`strokeStart`](http://developer.apple.com/library/ios/documentation/GraphicsImaging/Reference/CAShapeLayer_class/Reference/Reference.html#//apple_ref/doc/uid/TP40008314-CH1-SW16) and [`strokeEnd`](http://developer.apple.com/library/ios/documentation/GraphicsImaging/Reference/CAShapeLayer_class/Reference/Reference.html#//apple_ref/doc/uid/TP40008314-CH1-SW15). Both are floats that hold a value between `0.0` and `1.0`, indicating the relative location along the shape layer’s path at which to start and stop stroking the path.

The default values are `0.0` for `strokeStart` and `1.0` for `strokeEnd`, obviously, which causes the shape layer’s path to be stroked along its entire length. If you would, say, set `layer.strokeEnd = 0.5f`, only the first half of the path would be stroked. So far so good.

The really nice thing about these properties is that they are animatable. By animating `strokeEnd` from `0.0` to `1.0` over a duration of a few seconds, we can easily display the path as it is being drawn:

```
CABasicAnimation *pathAnimation = [CABasicAnimation animationWithKeyPath:@"strokeEnd"];
pathAnimation.duration = 10.0;
pathAnimation.fromValue = [NSNumber numberWithFloat:0.0f];
pathAnimation.toValue = [NSNumber numberWithFloat:1.0f];
[self.pathLayer addAnimation:pathAnimation forKey:@"strokeEndAnimation"];
```

Finally, add a second layer containing the image of a pen and use a [`CAKeyframeAnimation`](http://developer.apple.com/library/ios/#documentation/GraphicsImaging/Reference/CAKeyframeAnimation_class/Introduction/Introduction.html) to animate it along the path with the same speed to make the illusion perfect:

```
CAKeyframeAnimation *penAnimation = [CAKeyframeAnimation animationWithKeyPath:@"position"];
penAnimation.duration = 10.0;
penAnimation.path = self.pathLayer.path;
penAnimation.calculationMode = kCAAnimationPaced;
[self.penLayer addAnimation:penAnimation forKey:@"penAnimation"];
```

<sub>[Download the video](https://oleb.net/media/AnimatedPathsHausVomNikolaus.mp4).</sub>

This also works with text; we just have to convert the glyphs to a `CGPath`. Core Text offers a function to do just that, [`CTFontCreatePathForGlyph()`](http://developer.apple.com/library/ios/documentation/Carbon/Reference/CTFontRef/Reference/reference.html#//apple_ref/c/func/CTFontCreatePathForGlyph). To use it, we need to create an attributed string with the text we want to render and split it up first into lines and then into glyphs. After converting the glyphs to paths, we add them all to a single `CGPath` as subpaths. See the excellent article [Low-level text rendering](http://www.codeproject.com/KB/iPhone/Glyph.aspx) by [Ohmu](http://www.codeproject.com/script/Membership/View.aspx?mid=2887692) for details. The result looks cool:

<sub>[Download the video](https://oleb.net/media/AnimatedPathsHelloWorld.mp4).</sub>

[Get the sample project](https://github.com/ole/Animated-Paths) (for the iPad) on GitHub. I am releasing the parts I wrote under the [MIT License](http://www.opensource.org/licenses/mit-license.php), and the code I took from the article I mentioned above is released under the equally liberal [Code Project Open License](http://www.codeproject.com/info/cpol10.aspx).
