---
title: 'iOS 5 Tech Talk: Allan Schaffer on OpenGL ES with GLKit'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/11/ios5-tech-talk-allan-schaffer-opengl-es-glkit/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2eadacfb04ca052b'
translated: false
---

> 原文：[iOS 5 Tech Talk: Allan Schaffer on OpenGL ES with GLKit](https://oleb.net/blog/2011/11/ios5-tech-talk-allan-schaffer-opengl-es-glkit/)　·　Ole Begemann

# iOS 5 Tech Talk: Allan Schaffer on OpenGL ES with GLKit

The third Tech Talk session I saw was [Allan Schaffer](https://twitter.com/funnest)’s talk titled **Harnessing OpenGL ES and GLKit**. Allan is Apple’s Graphics and Game Technologies Evangelist. The abstract:

> GLKit is a high-level framework that combines the best practices for high-performance games with the rich capabilities of OpenGL ES 2.0. See how GLKit makes it easy to take advantage of the latest iOS hardware, and learn how you can tap into the advances in OpenGL ES in iOS 5.

iOS started out with [OpenGL ES 1.1](https://en.wikipedia.org/wiki/OpenGL_ES#OpenGL_ES_1.1) support and its fixed-function (in other words: limited) rendering pipeline. From the iPhone 3Gs onwards, all iOS devices have a GPU that is capable of [OpenGL ES 2.0](https://en.wikipedia.org/wiki/OpenGL_ES#OpenGL_ES_2.0) and its programmable (in other words: limited only by your imagination) rendering pipeline. Unfortunately, OpenGL 2.0 is not backwards compatible, which means many developers are still working with 1.1.

With iOS 5, Apple introduced the [GLKit](https://developer.apple.com/reference/glkit) framework. It is meant to lower the barriers of entry to work with OpenGL ES significantly. Specifically, Allan mentioned two goals behind the development of GLKit:

1. Easy creation of 2.0-based apps. No more hundreds of lines of boilerplate code to get OpenGL ES going!
2. Provide an easy-to-use environment that is based on Open GL ES 2.0 but provides the features of the fixed-function pipeline of OpenGL ES 1.1 out of the box. This should make it easy to port your existing 1.1 code to GLKit and then act as a gateway to more complex effects, giving you the additional artistic headroom that OpenGL ES 2.0 provides.

GLKit consists of four parts, which Allan discussed one by one. I am going to concentrate on the first section of the talk because that’s what I found most interesting and what I have the best notes for.

# 1. GLKView and GLKViewController

> **With GLKView and GLKViewController, we made OpenGL a true first-class citizen in the view hierarchy.**

Before iOS 5, creating an OpenGL surface inside the world of UIKit involved a lot of work. Until you arrived at a working `CAEAGLLayer` that was ready to accept your OpenGL draw calls, you had already subclassed `UIView`, overridden a fairly obscure class method, added several dozen lines of boilerplate code, and created a timer or display link to establish your render loop. Additionally, you had to take device rotation into your own hands for optimum performance, despite all the automatic handling in `UIViewController`.

GLKit fixes this by offering two new classes: [`GLKView`](https://developer.apple.com/reference/glkit/glkview) and [`GLKViewController`](https://developer.apple.com/reference/glkit/glkviewcontroller). Together, they make OpenGL views true first-class citizens in the view hierarchy and relieve you of writing almost all boilerplate code.

## GLKView

`GLKView` handles all of the previously required setup of the OpenGL subsystem for you automatically. It manages a framebuffer on your behalf that can be configured by simply settting some properties (`drawableColorFormat`, `drawableDepthFormat`, `drawableStencilFormat`, `drawableMultisample`) and calls its delegate ([`GLKViewDelegate`](https://developer.apple.com/reference/glkit/glkviewdelegate)) whenever it is time to draw your OpenGL scene. It is this delegate in which you place your OpenGL draw calls. `GLKView` even has a convenience method to make a snapshot of the current scene and return it as a `UIImage`!

To set up the view, all you have to do is manually create an [`EAGLContext`](https://developer.apple.com/reference/opengles/eaglcontext), pass it to your `GLKView` instance and assign a delegate. It couldn’t be much easier.

## GLKViewController

The `GLKViewController` class provides all of the standard `UIViewController` functionality. First and foremost, this includes interface rotation between portrait and landscape. According to Allan, the old recommendation to handle landscape rotation directly in your OpenGL matrix stack for best performance is no longer valid. All current devices can natively deal with the view controller-based UI rotation without a negative impact on performance.

`GLKViewController` also provides an integrated OpenGL ES rendering loop. For you, that means you no longer have to set up your own timer or display link. Just tell the view controller your preferred fps rate (via the `preferredFramesPerSecond` property) and it will automatically call its delegate’s ([`GLKViewControllerDelegate`](https://developer.apple.com/reference/glkit/glkviewcontrollerdelegate)) update method (or an overridden `- (void)update;` method) before the next frame is rendered. You just place the code that updates your model in that method and you’re done.

The view controller will also do the right thing when your app moves between foreground and background by automatically pausing and resuming the rendering loop.

# 2. GLKTextureLoader

Another task that every OpenGL-based app has to deal with repeatedly is loading textures. The [`GLKTextureLoader`](https://developer.apple.com/reference/glkit/glktextureloader) class makes it really easy to load both standard 2D textures and cubemaps in more or less every image format the iOS devices understand.

To use it, just instantiate a texture loader and connect it to an OpenGL context’s sharegroup (the object that is used to manage textures and other shared data for one or multiple `EAGLContext` instances). You can then create an OpenGL texture from a file or URL, a section in memory or a `CGImageRef`. Both synchronous and asynchronous methods are available. The documentation on `GLKTextureLoader` has all the details.

# 3. GLKMath

> **These math functions really excite me.**

This part of the talk got Allan most excited (he confessed to be a huge math nerd). The GLKit Math Functions are a set of almost 200 highly optimized functions that should cover most of your matrix and vector math needs. The library includes functions for two- to four-dimensional vectors, 3D and 4D matrices, quaternions and even 4×4 matrix stacks that are so often used in hierarchical animation systems. All of these functions are optimized to run as efficiently as possible on ARM-based CPUs.

See the [GLKit](https://developer.apple.com/reference/glkit) reference for a coverage of all available functions. There should be no more need for you to write your own vector math library.

# 4. GLKEffects

The final part of GLKit is a set of pre-defined effects, namely [`GLKBaseEffect`](https://developer.apple.com/reference/glkit/glkbaseeffect), [`GLKReflectionMapEffect`](https://developer.apple.com/reference/glkit/glkreflectionmapeffect) and [`GLKSkyboxEffect`](https://developer.apple.com/reference/glkit/glkskyboxeffect). These serve mainly as a starting point for your 3D scene to quickly get a 3D scene rendered with some standard effects without having to write your own vertex and/or fragment shaders, which requires knowledge of [GLSL](https://en.wikipedia.org/wiki/GLSL).

`GLKBaseEffect` in particular provides shaders that mimic the lighting model employed by OpenGL ES 1.1, which makes it the ideal starting point if you are porting an OpenGL ES 1.1-based app to 2.0. With the base effect you can apply up to 3 lights and 2 textures to a scene.

To use any of the effects, you create a new effect object at startup, configure its properties (such as lights and textures) and call its `prepareToDraw` method. This causes the effect’s shaders to be compiled and binds them to the current GL context. The documentation contains more information on how to use each effect.

The pre-defined effects work seamlessly together with your own shaders. This should make it easy to extend and improve your app’s rendering quality once you are more familiar with OpenGL ES 2.0 and the capabilities of custom shaders.
