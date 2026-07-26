---
title: 'Friday Q&A 2015-08-14: An Xcode Plugin for Unsmoothed Text'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2015-08-14-an-xcode-plugin-for-unsmoothed-text.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:954439bb9a288724'
translated: false
---

> 原文：[Friday Q&A 2015-08-14: An Xcode Plugin for Unsmoothed Text](https://www.mikeash.com/pyblog/friday-qa-2015-08-14-an-xcode-plugin-for-unsmoothed-text.html)　·　mikeash.com Friday Q&A

Posted at 2015-08-14 14:11 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2015-09-04: Let's Build dispatch_queue](https://www.mikeash.com/pyblog/friday-qa-2015-09-04-lets-build-dispatch_queue.html)  
Previous article: [Friday Q&A 2015-07-31: Tagged Pointer Strings](https://www.mikeash.com/pyblog/friday-qa-2015-07-31-tagged-pointer-strings.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [hack](https://www.mikeash.com/pyblog/?tag=hack) [xcode](https://www.mikeash.com/pyblog/?tag=xcode)

Friday Q&A 2015-08-14: An Xcode Plugin for Unsmoothed Text

by [Mike Ash](https://www.mikeash.com/)

**Background**  
I worship at the church of Monaco 9. It is, in my opinion, the One True Font for all monospaced tasks. This is especially true on old-fashioned non-retina screens, where its carefully designed pixels provide maximum readability in minimal space.

Those carefully designed pixels make it critically important that the text _not_ be antialiased. Font smoothing defeats the entire purpose of Monaco 9.

It was a bit distressing when, a couple of OS versions ago, Xcode started to insist on smoothing Monaco 9 despite my best efforts, because of changes made for retina support. This was annoying when not using a retina display. Fortunately, [it was possible to disable font smoothing with a defaults command](http://stackoverflow.com/questions/11660895/disable-anti-aliasing-fonts-in-xcode-4-4-in-mountain-lion).

Major trouble started when I got a retina display for my Mac Pro. I use it side by side with a normal non-retina display. Stuff that benefits from font smoothing, like web pages, e-mail, documentation, and cat pictures go on the retina display. Code goes on the regular display. However, the mere presence of the retina display made Xcode insist on font smoothing all over again, and the usual remedies were powerless.

I decided I'd have to get some code into Xcode and hack it from within. I thought about code injection using something like `mach_inject` or simply abusing `lldb`, but it turns out that Xcode has a built-in plugin mechanism that works well for this. It's undocumented and not officially supported, but it's not too hard to use.

**Getting Started**  
If you want to make your own Xcode plugin, create a new "Bundle" project in Xcode. This sets up a project that builds a loadable bundle, which is what plugins usually are. Tell it to use `.xcplugin` as the bundle's extension, and you're on your way to creating something Xcode can load.

Of course, it's not _quite_ so simple. Xcode is very particular about which plugins it will load, and requires some `Info.plist` keys.

The `XC4Compatible` key must be set to `YES`, otherwise Xcode will assume your plugin is utterly ancient and will refuse to load it.

The `XCPluginHasUI` key should be set to `NO` for our purposes. This causes Xcode to load the plugin's code immediately, allowing us to start causing trouble. If set to `YES`, there's presumably some sort of UI that allows it to be engaged manually, but I didn't explore this side of things since it wasn't necessary for my purposes.

The final and most annoying required key is `DVTPlugInCompatibilityUUIDs`. This is set to an array of strings. Each string is the UUID of an Xcode version that the plugin is compatible with. Each Xcode version has its own compatibilty UUID. If your plugin doesn't have the right UUID in its list, Xcode will refuse to load it.

Every single new version of Xcode gets a new UUID. These UUIDs can't be predicted in advance, so there's no way to preload the list in the plugin. This means that every new Xcode release breaks all plugins, and you have to manually go in and put the new UUID into the array. How annoying! If you're lucky, Xcode will dump an error to the Console stating the UUID it expects. Otherwise, you can extract the UUID from Xcode's own `Info.plist`.

Once you've made those changes, your project will build a plugin that Xcode actually wants to load. You still need to put the plugin in the right place for Xcode to actually find it, of course. That right place is `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins`. You could copy it manually every time you build, but that would be extremely annoying. It's much nicer to set up a Copy Files build phase to copy the plugin every time you build.

One more thing is needed for build nirvana, and that's to have your project actually start Xcode when you tell it to run. By default, plugin projects can't run, they can only build, because plugins are inert on their own. If you edit the scheme (option-click the run button in the toolbar) you can set a custom executable. Set this to Xcode, and Xcode will run Xcode when you tell Xcode to run your project. (Are you confused yet?)

For reasons completely unknown to me, Xcode will crash on launch with the default scheme settings. To fix this, make sure to go into Options, go to the very bottom, and disable "View Debugging ☑️ Enable user interface debugging." I do not know why this fix works.

To make sure everything is working, add a class to the plugin and implement `+load` to log some sort of "Hello, world" output. When you run the project, Xcode will launch and display your log output. You have full debugging available, with one copy of Xcode pointing at another. Try not to get confused about which is which.

**Hacking**  
Looking at the view hierarchy in the debugger, it's apparent that Xcode's code view is a custom subclass of `NSTextView`. This is great, because `NSTextView` is a public, documented class with lots of knobs to turn, and surely one of those knobs would solve the problem. (Not to be confused with the knobs who created the problem in the first place.)

How do we get ahold of the code view instances, though? We're just hanging out in `+load` with no pointers to anything. We could try to start from `NSApp` and work our way down, but that's pretty painful. Fortunately this code doesn't need to be production-worthy and we can use big hammers. Instead of trying to find individual instances, why not just modify the `NSTextView` class itself to do our bidding?

How to modify the class? I could override `init`, but that might be too early. I could try to make modifications in `viewDidMoveToWindow`, but even that might be too early. Without knowing exactly which knobs to turn yet, I want to make sure I can experiment without worrying about whether my experiments are being overridden later. I finally decided to use another big hammer and override `drawRect:`. This means my code will run every time the view is drawn. This is probably _way_ more often than necessary for this tweak. But as long as the tweak can run many times without hurting anything, why not? It'll be a tiny slowdown, and that's it.

How do we override `drawRect:` for the entire `NSTextView` class? Import `objc/runtime.h` and get cracking.

First, we want a convenient reference to the class and selector we're working with:

```
    Class nstv = [NSTextView class];
    SEL drawRect = @selector(drawRect:);
```

Then we can get a reference to the method in question:

```
    Method m = class_getInstanceMethod(nstv, drawRect);
```

We're going to provide a new implementation for the method. That implementation will call through to the original implementation, the moral equivalent of a call to `super`, so that the text still gets drawn. To make this happen, we need to save the pointer to the original implementation in a variable:

```
    IMP oldImplementation = method_getImplementation(m);
```

For convenience, I'll use the nifty `imp_implementationWithBlock` API to create the new implementation using a block. This call takes a block whose first argument is `self` and whose subsequent arguments are the method arguments, and turns it into an `IMP` which can be used as a method implementation. The runtime takes care of translating between the `IMP` function pointer and the block:

```
    IMP newImplementation = imp_implementationWithBlock(^(NSTextView *self, NSRect rect) {
```

Some sort of magic code is going to go it here to make everything better and destroy font smoothing for eternity, or at least until the next Xcode update:

```
        // MAGIC GOES HERE
```

After doing whatever magic, we want to call the original implementation. We do this by casting `oldImplementation` to a function pointer of the correct type, and then calling it:

```
        ((void (*)(id, SEL, NSRect))oldImplementation)(self, drawRect, rect);
    });
```

Now we have an `IMP` for the new implementation, and we can set it on the method:

```
    method_setImplementation(m, newImplementation);
```

That's it! Put this code in `+load` and our override now runs every time an `NSTextView` is drawn in Xcode.

What magic code goes in the override, though? With the surrounding code in place, it provides an excellent environment for experimentation. I tried CoreGraphics calls to disable font smoothing, I messed about with fonts, and various other things. I finally discovered that the magic incantation was to enable the use of screen fonts:

```
        [[self layoutManager] setUsesScreenFonts: YES];
```

I don't understand why, but apparently Xcode disables this. Re-enabling it in `drawRect:` fixes the problem. My perfectly pixelated Monaco 9 characters are back!

**Conclusion**  
Building an Xcode plugin is easier than it looked at first glance, and provides a good way to get code into Xcode to fix problems that just can't be fixed in any other way. If you'd like to see the complete project I made with the above code, you can get it on GitHub here:

[https://github.com/mikeash/DemoXcodePlugin](https://github.com/mikeash/DemoXcodePlugin)

That's it for today. Use this knowledge wisely and go in peace, or war, or whatever it is that you do. Come back next time for more entertainment and occasional knowledge. Friday Q&A is driven by reader suggestions, so as always, if you have an idea you'd like to see covered next time or some other time, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2015-08-14-an-xcode-plugin-for-unsmoothed-text.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
