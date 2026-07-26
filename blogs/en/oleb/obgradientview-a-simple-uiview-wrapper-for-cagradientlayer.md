---
title: 'OBGradientView: A Simple UIView Wrapper for CAGradientLayer'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2010/04/obgradientview-a-simple-uiview-wrapper-for-cagradientlayer/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:e70e484b7f8c89a8'
translated: false
---

> 原文：[OBGradientView: A Simple UIView Wrapper for CAGradientLayer](https://oleb.net/blog/2010/04/obgradientview-a-simple-uiview-wrapper-for-cagradientlayer/)　·　Ole Begemann

# OBGradientView: A Simple UIView Wrapper for CAGradientLayer

[`CAGradientLayer`](http://developer.apple.com/iphone/library/documentation/GraphicsImaging/Reference/CAGradientLayer_class/Reference/Reference.html) is the simplest way to display gradients on the iPhone. And while Core Animation layers are simple enough to use, I repeatedly find myself missing the ability to simply add a gradient directly to a view (as a replacement for its background color) without having to write the code to manually add a CAGradientLayer to the view. So I wrote a little class that does just that.

[`OBGradientView`](https://github.com/ole/OBGradientView) is a very simple UIView subclass that wraps the functionality of CAGradientLayer in a view. It exposes all of the layer’s gradient-related properties (`colors`, `locations`, `startPoint`, `endPoint`, and `type`) as its own properties. Calls of the setters and getters are simply forwarded to the underlying CAGradientLayer so you can use the same syntax to define the gradient. In addition, to make it more UIKit-friendly, `OBGradientView` allows you to set the `colors` property with an array of `UIColor` instances instead of `CGColorRef`s.

Dealing with a view instead of a Core Animation layer is especially useful when you want to use autoresizing masks, which are not available for CALayer on the iPhone. For example, adding a subtle background gradient to your view controller’s main view that autoresizes automatically is very simple:

```
OBGradientView *backgroundView = [[OBGradientView alloc] initWithFrame:self.view.bounds];
backgroundView.colors = [NSArray arrayWithObjects:
                         [UIColor lightGrayColor],
                         [UIColor darkGrayColor],
                         nil];
backgroundView.autoresizingMask = UIViewAutoresizingFlexibleWidth |
                                  UIViewAutoresizingFlexibleHeight;
```

[Get the code for OBGradientView from GitHub](https://github.com/ole/OBGradientView). I am releasing it under the [MIT License](http://www.opensource.org/licenses/mit-license.php).

![Screenshot of the OBGradientViewDemo project](https://oleb.net/media/OBGradientViewDemo-screenshot.png)
