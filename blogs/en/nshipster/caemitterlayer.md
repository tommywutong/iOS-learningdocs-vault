---
title: CAEmitterLayer
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/caemitterlayer/'
original_language: en
published: 2019-07-08
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:b74be6a95be6c82d'
translated: false
---

> 原文：[CAEmitterLayer](https://nshipster.com/caemitterlayer/)　·　NSHipster (Mattt)

# [CAEmitter​Layer](https://nshipster.com/caemitterlayer/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  July 8^th, 2019

Etymologically, confetti comes from the Italian word for the sugar-coated almond sweet thrown at celebrations, which, in turn, get their name from the Latin conficio: con- (“with, together”) + facio (“do, make”); in another sense, _“to celebrate”_.

Confetti gets tossed around a lot these days, but not nearly as in the 20^th century with its iconic ticker-tape parades down the streets of New York City, like the one [welcoming home the Apollo 11 astronauts](https://en.wikipedia.org/wiki/Ticker_tape_parade#/media/File:Apollo_11_ticker_tape_parade_1.jpg) 50 years ago. Alas, the rise of digital technology made obsolete the stock tickers whose waste paper tape comprised the substrate of those spectacles. And as a result, the tradition has become much less commonplace today.

This week mark’s NSHipster’s 7^th anniversary! And what better way to celebrate the occasion than to implement a fun and flexible confetti view on iOS?

---

Let’s dive right in with a quick refresher on the difference between views and layers:

## Views and Layers

On iOS, each view is backed by a layer …or perhaps it’s more accurate to say that layers are _fronted_ by view.

Because despite their reputation as the workhorse of UIKit, `UIView` delegates the vast majority of its functionality to `CALayer`. Sure, views handle touch events and autoresizing, but beyond that, nearly everything else between your code and the pixels on screen is the responsibility of layers.

Among the available `CALayer` subclasses in the Quartz Core / Core Animation framework there are APIs for displaying large amounts of content by [scrolling](https://developer.apple.com/documentation/quartzcore/cascrolllayer?language=objc) and [tiling](https://developer.apple.com/documentation/quartzcore/catiledlayer?language=objc), there are APIs for doing [advanced](https://developer.apple.com/documentation/quartzcore/careplicatorlayer?language=objc) [transformations](https://developer.apple.com/documentation/quartzcore/catransformlayer?language=objc), and there are APIs that let you get at the bare [metal](https://developer.apple.com/documentation/quartzcore/cametallayer?language=objc). But our focus today is a special class called [`CAEmitterLayer`](https://developer.apple.com/documentation/quartzcore/caemitterlayer?language=objc).

## Particle Emitters

Indeed, particle systems are frequently used to generate fire, smoke, sparks, fireworks, and explosions. But they’re also capable of modeling… less destructive phenomena like rain, snow, sand, and — most importantly — confetti.

`CAEmitterLayer` configures the position and shape of where particles are emitted. As to the specific behavior and appearance of those particles, that’s determined by the `CAEmitterCell` objects seeded to the emitter layer.

By analogy:

- `CAEmitterLayer` controls the size, position, and intensity of a confetti cannon,
- `CAEmitterCell` controls the size, shape, color, and movement of each type of confetti loaded into the hopper.

If you wanted confetti with black mustaches, orange birds, and [purple aardvarks](https://nshipster.com/bug-reporting/), then you’d load a `CAEmitterLayer` with three different `CAEmitterCell` objects, each specifying its `color`, `contents`, and other behaviors.

## Particle Emitter Cells

The secret to `CAEmitterLayer`’s high performance is that it doesn’t track each particle individually. Unlike views or even layers, emitted particles can’t be altered once they’re created. _(Also, they don’t interact with one another, which makes it easy for them to be rendered in parallel)_

Instead, `CAEmitterCell` has an enormous API surface area to configure every aspect of particle appearance and behavior before they’re generated, including birth rate, lifetime, emission angles, velocity, acceleration, scale, magnification filter, color — too many to cover in any depth here.

In general, most emitter cell behavior is defined by either a single property or a group of related properties that specify a base value along with a corresponding range and/or speed.

A _range_ property specifies the maximum amount that can be randomly added or subtracted from the base value. For example, the `scale` property determines the size of each particle, and the `scaleRange` property specifies the upper and lower bounds of possible sizes relative to that base value; a `scale` of `1.0` and a `scaleRange` of `0.2` generates particles sized between 0.8× and 1.2× the original `contents` size.

Cell emitter behavior may also have a corresponding _speed_ property, which specify the rate of growth or decay over the lifetime of the particle. For example, with the `scaleSpeed` property, positive values cause particles to grow over time whereas negative values cause particles to shrink.

---

Loaded up with a solid understanding of the ins and outs of `CAEmitterLayer`, now’s the time for us to let that knowledge spew forth in a flurry of code!

## Implementing a Confetti View for iOS

First, let’s define an abstraction for the bits of confetti that we’d like to shoot from our confetti cannon. An enumeration offers the perfect balance of constraints and flexibility for our purposes here.

```
enum Content {
    enum Shape {
        case circle
        case triangle
        case square
        case custom(CGPath)
    }

    case shape(Shape, UIColor?)
    case image(UIImage, UIColor?)
    case emoji(Character)
}
```

Here’s how we would configure our confetti cannon to shoot out a colorful variety of shapes and images:

```
let contents: [Content] = [
    .shape(.circle, .purple),
    .shape(.triangle, .lightGray),
    .image(UIImage(named: "swift")!, .orange),
    .emoji("👨🏻"),
    .emoji("📱")
]
```

### Creating a CAEmitterLayer Subclass

The next step is to implement the emitter layer itself.

The primary responsibility of `CAEmitterLayer` is to configure its cells. Confetti rains down from above with just enough variation in its size, speed, and spin to make it interesting. We use the passed array of `Content` values to set the `contents` of the cell (a `CGImage`) and a fill color (a `CGColor`).

```
private final class Layer: CAEmitterLayer {
    func configure(with contents: [Content]) {
        emitterCells = contents.map { content in
            let cell = CAEmitterCell()

            cell.birthRate = 50.0
            cell.lifetime = 10.0
            cell.velocity = CGFloat(cell.birthRate * cell.lifetime)
            cell.velocityRange = cell.velocity / 2
            cell.emissionLongitude = .pi
            cell.emissionRange = .pi / 4
            cell.spinRange = .pi * 6
            cell.scaleRange = 0.25
            cell.scale = 1.0 - cell.scaleRange
            cell.contents = content.image.cgImage
            if let color = content.color {
                cell.color = color.cgColor
            }

            return cell
        }
    }

    …
}
```

We’ll call this `configure(with:)` method from our confetti view, which will be our next and final step.

### Implementing ConfettiView

We want our confetti view to emit confetti for a certain amount of time and then stop. However, accomplishing this is surprisingly difficult, as evidenced by the questions floating around on [Stack Overflow](https://stackoverflow.com/questions/18913484/ios-7-caemitterlayer-spawning-particles-inappropriately).

The central problem is that Core Animation operates on its own timeline, which doesn’t always comport with our own understanding of time.

For instance, if you neglect to initialize the `beginTime` of the emitter layer with `CACurrentMediaTime()` right before it’s displayed, it’ll render with the wrong time space.

As far as stopping goes: you can tell the layer to stop emitting particles by setting its `birthRate` property to `0`. But if you start it again up by resetting that property to `1`, you get a flurry of particles filling the screen instead of the nice initial burst on the first launch.

Suffice to say that there are myriad different approaches to making this behave as expected. But here’s the best solution we’ve found for handling starting and stopping, as well as having more than one emitter at the same time:

---

Going back to our original explanation for a moment, each instance of `UIView` (or one of its subclasses) is backed by a single, corresponding instance of `CALayer` (or one of its subclasses). A view may also host one or more additional layers, either as siblings or children to the backing layer.

Taking advantage of this fact, we can create a new emitter layer each time we fire our confetti cannon. We can add that layer as a hosted sublayer for our view, and let the view handle animation and disposal of each layer in a nice, self-contained way.

```
private let kAnimationLayerKey = "com.nshipster.animationLayer"

final class ConfettiView: UIView {
    func emit(with contents: [Content],
              for duration: TimeInterval = 3.0)
    {
    ❶ let layer = Layer()
        layer.configure(with: contents)
        layer.frame = self.bounds
        layer.needsDisplayOnBoundsChange = true
        self.layer.addSublayer(layer)

        guard duration.isFinite else { return }

    ❷ let animation = CAKeyframeAnimation(keyPath: #keyPath(CAEmitterLayer.birthRate))
        animation.duration = duration
        animation.timingFunction = CAMediaTimingFunction(name: .easeIn)
        animation.values = [1, 0, 0]
        animation.keyTimes = [0, 0.5, 1]
        animation.fillMode = .forwards
        animation.isRemovedOnCompletion = false

        layer.beginTime = CACurrentMediaTime()
        layer.birthRate = 1.0

    ❸ CATransaction.begin()
        CATransaction.setCompletionBlock {
            let transition = CATransition()
            transition.delegate = self
            transition.type = .fade
            transition.duration = 1
            transition.timingFunction = CAMediaTimingFunction(name: .easeOut)
            transition.setValue(layer, forKey: kAnimationLayerKey) ❹
            transition.isRemovedOnCompletion = false

            layer.add(transition, forKey: nil)

            layer.opacity = 0
        }
        layer.add(animation, forKey: nil)
        CATransaction.commit()
    }

    …
```

There’s a lot of code to unpack here, so let’s focus on its distinct parts:

❶ First, we create an instance of our custom `CAEmitterLayer` subclass (creatively named `Layer` here, because it’s a private, nested type). It’s set up with our `configure(with:)` method from before and added as a sublayer. The `needsDisplayOnBoundsChange` property defaults to `false` for whatever reason; setting it to `true` here allows us to better handle device trait changes (like rotation or moving to a new window). ❷ Next, we create a keyframe animation to taper the `birthRate` property down to `0` over the specified duration. ❸ Then we add that animation in a transaction and use the completion block to set up a fade-out transition. (We set the view as the transition’s animation delegate, as described in the next session) ❹ Finally, we use key-value coding to create a reference between the emitter layer and the transition so that it can be referenced and cleaned up later on.

### Adopting the CAAnimationDelegate Protocol

To extend our overarching metaphor, `CAAnimationDelegate` is [that little cartoon janitor from _Rocky and Bullwinkle_](https://nshipster.com/assets/caemitterlayer-janitor-b82cefff441178add0447a42234bb422f435bfc1b1fb042c0be48b45ccff3e8f4bbff149b78952d0dcfbea6208820b3846be229972c593735b036759a5647749.jpg) with a push broom at the end of the ticker-tape parade.

The `animationDidStop(_:)` delegate method is called when our `CATransition` finishes. We then get the reference to the calling layer in order to remove all animations and remove it from its superlayer.

```
// MARK: - CAAnimationDelegate

extension ConfettiView: CAAnimationDelegate {
    func animationDidStop(_ animation: CAAnimation, finished flag: Bool) {
        if let layer = animation.value(forKey: kAnimationLayerKey) as? CALayer {
            layer.removeAllAnimations()
            layer.removeFromSuperlayer()
        }
    }
}
```

The end result: it’s as if NSHipster.com were parading down the streets of New York City (or rather, Brooklyn, if you really wanted to lean into the hipster thing)

---

The full `ConfettiView` source [is available on GitHub](https://github.com/NSHipster/ConfettiView), and can be easily integrated into your project using [CocoaPods](https://cocoapods.org).

But ending on such a practical note doesn’t make for a particularly snazzy conclusion. So instead, how about a quick bonus round detailing seven other ways that you could implement confetti instead:

---

## ✨Bonus ✨ 7 Alternative Approaches to Confetti

### SpriteKit Particle System

SpriteKit is the cooler, younger cousin to UIKit, providing nodes to games rather than views to apps. On their surface, they couldn’t look more different from one another. And yet both share a common, deep reliance on layers, which makes for familiar lower-level APIs.

The comparison between these two frameworks goes even deeper, as you’ll find if you open File \> New, scroll down to “Resource” and create a new SpriteKit Particle System file. Open it up, and Xcode provides a specialized editor reminiscent of Interface Builder.

![Xcode SpriteKit Particle Editor](https://nshipster.com/assets/caemitterlayer-spritekit-particle-emitter--light-777adf26d045c657af16c9ad258cf28612aaeb57f2d96e51d868f6851e0ffd6b391d16b342254578eb2fbda69c1662dbe0fcc4dfbcff53982a8c3d00a1a84236.png)

Call up your designed `SKEmitterNode` by name or reimplement in code _(if you’re the type to hand-roll all of your `UIView`s)_ for a bespoke confetti experience.

### SceneKit Particle System

Again with the metaphors, SceneKit is to 3D what SpriteKit is to 2D.

In Xcode 11, open File \> New, select SceneKit Scene File under the “Resource” heading, and you’ll find an entire 3D scene editor — right there in your Xcode window.

![Xcode SceneKit Scene Editor](https://nshipster.com/assets/caemitterlayer-scenekit-scene-editor--light-a304fe5eeb4b28ebcee98029eca998e0acf7f9ee27cdb68d6302432417b2e686046e80834acfeab3fdc29a56bc631b23df4e70f8a17f37cd60ee0accc32bf24a.png)

Add in a dynamic physics body and a turbulence effect, and you can whip up an astonishingly capable simulation in no time at all (though if you’re like me, you may find yourself spending hours just playing around with everything)

### UIKit Dynamics

At the same time that SpriteKit entered the scene, you might imagine that UIKit started to get self-conscious about the “business only” vibe it was putting out.

So in iOS 7, in a desperate attempt to prove itself cool to its “fellow kids” UIKit added `UIDynamicAnimator` as part of a set of APIs known as “UIKit Dynamics”.

Feel free to [read our article on `UIFieldBehavior`](https://nshipster.com/uifieldbehavior/) and make confetti out of your app, if you like.

### HEVC Video with Alpha Channel

Good news! Later this year, AVFoundation adds support for alpha channels in HEVC video! So if, say, you already had a snazzy After Effects composition of confetti, you could export that with a transparent background and composite it directly to your app or on the web.

For more details, check out [WWDC 2019 Session 506](https://developer.apple.com/videos/play/wwdc2019/506/).

### Animated PNGs

Of course, this time next year, we’ll still be sending animated GIFs around to each other, despite all of their shortcomings.

Animated GIFs are especially awful for transparency. Without a proper alpha channel, GIFs are limited to a single, transparent matte color, which causes unsightly artifacts around edges.

We all know to use PNGs on the web for transparent images, but only a fraction of us are even aware that [APNG](https://en.wikipedia.org/wiki/APNG) is even a thing.

Well even fewer of us know that iOS 13 adds native support for APNG (as well as animated GIFs — finally!). Not only were there no announcements at WWDC this year, but the only clue of this new feature’s existence is an API diff between Xcode 11 Beta 2 and 3. Here’s the documentation stub for the function, [`CGAnimateImageAtURLWithBlock`](https://developer.apple.com/documentation/imageio/3333271-cganimateimageaturlwithblock)

And if you think that’s (unfortunately) par for the course these days, it gets worse. Because for whatever reason, the relevant header file (`ImageIO/CGImageAnimation.h`) is inaccessible in Swift!

Now, we don’t really know how this is supposed to work, but here’s our best guess:

```
// ⚠️ Expected Usage
let imageView = UIImageView()

let imageURL = URL(fileURLWithPath: "path/to/animated.png")
let options: [String: Any] = [kCGImageAnimationLoopCount: 42]
CGAnimateImageAtURLWithBlock(imageURL, options) { (index, cgimage, stop) in
    imageView.image = UIImage(cgImage: cg)
}
```

---

Meanwhile, animated PNGs have been supported in Safari for ages, and with a far simpler API:

```
<img src="animated.png" />
```

![](https://nshipster.com/assets/caemitterlayer-confetti-e51c32fcb954c0b207462437b17b098568f9c5d4c86e9381c4d3ac9447cc519e5abb6e900835dd93c232804512f76af753c138741e36f3cd54a8d2ed2b14f2bc.png)

### WebGL

Speaking of the web, let’s talk about a shiny, new(-ish) web standard called [WebGL](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API).

With just [a few hundred lines of JavaScript and GL shader language](https://nshipster.com/assets/articles/caemitterlayer-5c5fbf96b6f05830f90497cdd5a840daed7fdce6c6dc35a2300c844d1b03f8f2276cdcd204681c8421ff5c97bf4e8f66dcc60044b98ab6cc86e892e97d061aae.js), you too can render confetti to your very own blog about ~~web development~~ Objective-C, Swift, and Cocoa.

![](https://nshipster.com/assets/logo-d66465b1836b0b9dc11cd5cd8f61aab1a377aedd4c7086ce5ba73cc2ad08f37342aea6c125ad3a9fc7d5a77f2ec7c1d6f4bea939c14d9ecc618ea3e5f512ebc9.png)

### Emoji

But really, we could do away with all of this confetti and express ourselves much more simply:

```
let mood = "🥳"
```

---

It’s hard to believe that it’s been seven years since I started this site. We’ve been through a lot together, dear reader, so know that your ongoing support means the world to me. Thanks for learning with me over the years.

Until next week: _May your code continue to compile and inspire._
