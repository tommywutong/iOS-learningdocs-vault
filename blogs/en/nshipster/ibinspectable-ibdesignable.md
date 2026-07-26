---
title: IBInspectable / IBDesignable
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/ibinspectable-ibdesignable/'
original_language: en
published: 2015-02-02
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:bf4b9f7075b6ad13'
translated: false
---

> 原文：[IBInspectable / IBDesignable](https://nshipster.com/ibinspectable-ibdesignable/)　·　NSHipster (Mattt)

# [IBInspectable / IBDesignable](https://nshipster.com/ibinspectable-ibdesignable/)

Written by  [Nate Cook](https://nshipster.com/authors/nate-cook/)  February 2^nd, 2015

Show, don’t tell. Seeing is believing. A picture is worth a thousand ~~emails~~ words.

Whatever the cliché, replacing an interface that requires us to memorize and type with one we can see and manipulate can be an enormous improvement. Xcode 6 makes just such a substitution, building new interactions on top of old technologies. With `IBInspectable` and `IBDesignable`, it’s possible to build a custom interface for configuring your custom controls and have them rendered in real-time while designing your project.

## IBInspectable

`IBInspectable` properties provide new access to an old feature: user-defined runtime attributes. Currently accessible from the identity inspector, these attributes have been available since before Interface Builder was integrated into Xcode. They provide a powerful mechanism for configuring any key-value coded property of an instance in a NIB, XIB, or storyboard:

![User-Defined Runtime Attributes](https://nshipster.com/assets/IBInspectable-runtime-attributes-01c803097c9e74b1b37ae52ebac863282a94a6220c13bd8f4d2100c8a1bfacc047560e8ca623fb0de33d89ace3e88a802b65f0824afb4432ec4fd296857f69ac.png)

While powerful, runtime attributes can be cumbersome to work with. The key path, type, and value of an attribute need to be set on each instance, without any autocompletion or type hinting, which requires trips to the documentation or a custom subclass’s source code to double-check the settings. `IBInspectable` properties solve this problem outright: in Xcode 6 you can now specify any property as inspectable and get a user interface built just for your custom class.

For example, these properties in a `UIView` subclass update the backing layer with their values:

```
@IBInspectable var cornerRadius: CGFloat = 0 {
   didSet {
       layer.cornerRadius = cornerRadius
       layer.masksToBounds = cornerRadius > 0
   }
}
@IBInspectable var borderWidth: CGFloat = 0 {
   didSet {
       layer.borderWidth = borderWidth
   }
}
@IBInspectable var borderColor: UIColor? {
   didSet {
       layer.borderColor = borderColor?.CGColor
   }
}
```

Marked with `@IBInspectable` (or `IBInspectable` in Objective-C), they are easily editable in Interface Builder’s inspector panel. Note that Xcode goes the extra mile here—property names are converted from camel- to title-case and related names are grouped together:

![IBInspectable Attribute Inspector](https://nshipster.com/assets/IBInspectable-inspectable-0c9204b234c8598cc0ba589f199b81a88808e764876318b4793ec18f719ba442b46f01519a5ee8528cfcdbbcb97c2bdddaaaa143ffdada0386592ba30562eb70.png)

Since inspectable properties are simply an interface on top of user-defined runtime attributes, the same list of types is supported: booleans, strings, and numbers (i.e., `NSNumber` or any of the numeric value types), as well as `CGPoint`, `CGSize`, `CGRect`, `UIColor`, and `NSRange`, adding `UIImage` for good measure.

> Those already familiar with runtime attributes will have noticed a bit of trickery in the example above. `UIColor` is the only color type supported, not the `CGColor` native to a view’s backing `CALayer`. The `borderColor` computed property maps the `UIColor` (set via runtime attribute) to the layer’s required `CGColor`.

### Making Existing Types Inspectable

Built-in Cocoa types can also be extended to have inspectable properties beyond the ones already in Interface Builder’s attribute inspector. If you like rounded corners, you’ll love this `UIView` extension:

```
extension UIView {
    @IBInspectable var cornerRadius: CGFloat {
        get {
            return layer.cornerRadius
        }
        set {
            layer.cornerRadius = newValue
            layer.masksToBounds = newValue > 0
        }
    }
}
```

Presto! A configurable border radius on any `UIView` you create.

## IBDesignable

As if that weren’t enough, `IBDesignable` custom views also debut in Xcode 6. When applied to a `UIView` or `NSView` subclass, the `@IBDesignable` designation lets Interface Builder know that it should render the view directly in the canvas. This allows seeing how your custom views will appear without building and running your app after each change.

To mark a custom view as `IBDesignable`, prefix the class name with `@IBDesignable` (or the `IB_DESIGNABLE` macro in Objective-C). Your initializers, layout, and drawing methods will be used to render your custom view right on the canvas:

```
@IBDesignable
class MyCustomView: UIView {
    ...
}
```

![IBDesignable Live Preview](https://nshipster.com/assets/IBInspectable-designable-a705ffb98119bfcf9bb2680a7f77620babd4f429c595a42be6b9b3678a1fc44abf87acda8458e56ba62ecd1982aebb5612fb905c97fd3d19ae1515ac48f5c372.png)

The time-savings from this feature can’t be overstated. Combined with `IBInspectable` properties, a designer or developer can easily tweak the rendering of a custom control to get the exact result she wants. Any changes, whether made in code or the attribute inspector, are immediately rendered on the canvas.

Moreover, any problems can be debugged without compiling and running the whole project. To kick off a debugging session right in place, simply set a breakpoint in your code, select the view in Interface Builder, and choose **Editor** ➔ **Debug Selected Views**.

Since the custom view won’t have the full context of your app when rendered in Interface Builder, you may need to generate mock data for display, such as a default user profile image or generic weather data. There are two ways to add code for this special context:

> - `prepareForInterfaceBuilder()`: This method compiles with the rest of your code but is only executed when your view is being prepared for display in Interface Builder.

> - `TARGET_INTERFACE_BUILDER`: The `#if TARGET_INTERFACE_BUILDER` preprocessor macro will work in either Objective-C or Swift to conditionally compile the right code for the situation:

> ```
> #if !TARGET_INTERFACE_BUILDER
>     // this code will run in the app itself
> #else
>     // this code will execute only in IB
> #endif
> ```

## IBCalculatorConstructorSet

What can you create with a combination of `IBInspectable` attributes in your `IBDesignable` custom view? As an example, let’s update an old classic from [Apple folklore](http://www.folklore.org/StoryView.py?story=Calculator_Construction_Set.txt): the “Steve Jobs Roll Your Own Calculator Construction Set,” Xcode 6-style ([gist](https://gist.github.com/natecook1000/4269059121ec247fbb90)):

![Calculator Construction Set](https://nshipster.com/assets/IBInspectable-CCS-3a46c2bb95a2da2f4f96ae756b2b1afecb8a9705c2d38e85c4ce5d0fd286bb7293636b41463eb42600b0ce15af5c16da6df8a6d210053c2ee8ffc33463746199.gif)

---

That was almost a thousand words—let’s see some more pictures. What are _you_ creating with these powerful new tools? [Tweet an image](https://twitter.com/share?hashtags=IBInspectable) of your `IBInspectable` or `IBDesignable` creations with the hashtag `#IBInspectable`—we can all learn from seeing what’s possible.
