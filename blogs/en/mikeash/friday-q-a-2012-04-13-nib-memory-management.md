---
title: 'Friday Q&A 2012-04-13: Nib Memory Management'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-04-13-nib-memory-management.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7985bb049eb54373'
translated: false
---

> 原文：[Friday Q&A 2012-04-13: Nib Memory Management](https://www.mikeash.com/pyblog/friday-qa-2012-04-13-nib-memory-management.html)　·　mikeash.com Friday Q&A

Posted at 2012-04-13 14:14 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2012-04-27: PLCrashReporter and Unwinding the Stack With DWARF](https://www.mikeash.com/pyblog/friday-qa-2012-04-27-plcrashreporter-and-unwinding-the-stack-with-dwarf.html)  
Previous article: [Introducing PLWeakCompatibility](https://www.mikeash.com/pyblog/introducing-plweakcompatibility.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [memory](https://www.mikeash.com/pyblog/?tag=memory) [nib](https://www.mikeash.com/pyblog/?tag=nib)

Friday Q&A 2012-04-13: Nib Memory Management

by [Mike Ash](https://www.mikeash.com/)

**Nib Loading Overview**  
When you load a nib, two important steps happen in sequence. First, the loader instantiates all of the objects in the nib. Second, it connects all of the outlets specified in the nib.

When it comes to memory management, there are two relevant areas. The first is how to properly manage outlets. The second is how to manage the top-level objects in the nib. A nib contains a hierarchy of objects, where each object is owned by its parent, but the objects at the top level of that hierarchy are a special case.

**Mac Nib Loading**  
Let's talk about how nib loading works on the Mac, with respect to the two relevant memory management areas.

Top level objects are instantiated using `alloc` and `init` (or a class-specific initializer like `-initWithContentRect:styleMask:backing:defer:` for `NSWindow` instances. They are then left like this, with responsibility for finally releasing them implicitly transferred to the File's Owner object. If you use `NSWindowController` or `NSViewController` to load the nib, it automatically takes ownership of these objects and will release them when the controller is destroyed.

To set an outlet, the nib loader first searches for a setter method. If the outlet is called `foo`, the loader searches for a method called `setFoo:`. If such a method exists, the loader calls it, passing the value of the outlet as the parameter.

If no such method exists, the loader searches for an instance variable with the same name as the outlet. If it finds such an instance variable, the loader sets its value directly to the outlet value without performing any memory management.

Finally, if no method and no instance variable can be found, the outlet connection fails and the outlet is not set.

**iOS Nib Loading**  
Now let's talk about how nib loading works on iOS. Overall it's very similar, but there are subtle differences. Don't worry about trying to find all of the differences, as I'll point them out and analyze them afterwards.

Top level objects are instantiated using `alloc` and `init` (or a class-specific initializer), and then autoreleased. In the absence of anything else retaining them, these objects will be automatically destroyed.

To set an outlet, the nib loader calls `-setValue:forKey:` with the outlet value and outlet name. The Key-Value Coding machinery then takes over and searches for a way to set that particular key. For an outlet called `foo`, it will first search for a method called `setFoo:`. If such a method exists, it calls that method, passing the value of the outlet as the parameter.

If no such method exists, the KVC machinery searches for an instance variable called `_foo`, `_isFoo`, `foo`, or `isFoo`. If any of those exists, it sets the first one it finds to the value of the outlet, releasing the old value in the instance variable (if any) and retaining the new value.

If no method and no instance variable are found, KVC calls `setValue:forUndefinedKey:`. By default, this raises an execption, and it can be overridden to implement custom behavior for unknown keys.

**The Differences**  
These two systems are similar but not quite the same. The differences are due to the more modern nature of iOS. Without exception, where the two systems differ, the iOS way is more sensible. Unfortunately, the Mac way can't be changed without severely breaking backwards compatibility. These differences are:

- Top level objects must be explicitly released on the Mac, unless you use an `NSWindowController` or `NSViewController` to load the nib. On iOS, they are autoreleased.
- Directly setting the ivar on iOS retains the outlet due to how KVC works. On the Mac, the outlet is not retained.
- Because directly setting the ivar results in a retain on iOS, such outlets must be released in `dealloc`. On the Mac, they can just be ignored there.
- Directly setting the ivar on iOS has a more thorough search pattern than on the Mac, due to KVC.

**The Similarities**  
Keeping track of these differences is mentally taxing and error-prone, especially if you switch between the two platforms. Getting it wrong can cause a leak or a crash (or both). The best way to handle the differences is to stick to areas where the two platforms are the same. Fortunately, those areas are also the most convenient and best ways to approach nibs anyway.

When loading nibs with a Cocoa controller class (`NSWindowController` and `NSViewController` on the Mac, `UIViewController` on iOS), top-level objects in the nib are automatically handled for you, and thus the behavior becomes the same on both platforms in this case. It's extremely rare to need to load a nib directly, and if you find yourself doing it, you should probably stop and use one of these controllers instead.

When using `@property` for outlets, memory management is consistent across both platforms, since they both use the setter if one exists. The memory management for the property can be set as you like, although `strong` or `retain` is generally preferred. In that case, you must `release` the property value in `dealloc`, just as you would with any other strong property, unless you're using ARC. `weak` can be a good choice for outlets to subviews on iOS, where the views may be unloaded and you don't want a strong reference to keep them alive behind your back.

**A Convenient Table**  
Here's a full summary of the various situations in convenient table form:

| **Outlet Type** | **Mac** | **iOS** |
|---|---|---|
| Directly setting the ivar | Unretained reference, do not release | Retained reference, must release in dealloc |
| Strong/retain setter | Release in dealloc (or let ARC handle it) | Release in dealloc (or let ARC handle it) |
| Assign/weak setter | Don't need to do anything | Don't need to do anything |
|  |  |  |
| Top-level objects | Use `NSWindowController` or `NSViewController` to load nibs, silly | Use `UIViewController` to load nibs, silly |
| No seriously, what about top-level objects? | Release each top-level object to balance the `alloc` sent when loading the nib | Don't do anything |

**Conclusion**  
Nib memory management is similar between Mac and iOS but just different enough to be annoyingly confusing. Fortunately, it's easy to mitigate the confusion by sticking to areas where the two platforms behave identically, which results in best practices anyway. Always use a Cocoa controller to load nibs rather than loading the nib directly yourself. Always declare properties for your outlets. As with any property, if your outlet properties are strong, then you must release the backing instance variable in `dealloc` (or let ARC do it for you).

That's it for today. Come back next time for another exciting and tittilating edition of Friday Q&A. Until then, since Friday Q&A is driven by reader suggestions, please [send in](mailto:mike@mikeash.com) your ideas for topics to cover.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-04-13-nib-memory-management.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
