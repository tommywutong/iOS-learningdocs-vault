---
title: 'Friday Q&A 2009-11-06: Linking and Install Names'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-11-06-linking-and-install-names.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5a532e2cef965e9d'
translated: false
---

> 原文：[Friday Q&A 2009-11-06: Linking and Install Names](https://www.mikeash.com/pyblog/friday-qa-2009-11-06-linking-and-install-names.html)　·　mikeash.com Friday Q&A

Posted at 2009-11-07 00:18 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-11-13: Dangerous Cocoa Calls](https://www.mikeash.com/pyblog/friday-qa-2009-11-13-dangerous-cocoa-calls.html)  
Previous article: [Friday Q&A 2009-10-30: Generators in Objective-C](https://www.mikeash.com/pyblog/friday-qa-2009-10-30-generators-in-objective-c.html)  
Tags: [frameworks](https://www.mikeash.com/pyblog/?tag=frameworks) [libraries](https://www.mikeash.com/pyblog/?tag=libraries) [linking](https://www.mikeash.com/pyblog/?tag=linking)

Friday Q&A 2009-11-06: Linking and Install Names

by [Mike Ash](https://www.mikeash.com/)

**Static Libraries**  
 These are so simple they barely need discussion. When you link against a static library, the contents of that library are copied into your application when you build. From that point on, the code acts just like the code you wrote yourself.

**Dynamic Libraries**  
 When you link against a dynamic library, things are less straightforward. The linker basically makes a note that your references to various symbols are to be found in this library, and that your binary depends on that library. Then at runtime, when your application is loaded, the dynamic linker also loads that library.

The big question for today is, how does the dynamic linker know where to find it?

**Install name**  
 The answer to that question varies greatly from one OS to another, but on the Mac, the answer is install names.

An install name is just a pathname embedded within a dynamic library which tells the linker where that library can be found at runtime. For example, `libfoo.dylib` might have an install name of `/usr/lib/libfoo.dylib`. This install name gets copied into the application at link time. When the dynamic linker goes looking for `libfoo.dylib` at runtime, it will fetch the install name out of the application and know to look for the library in `/usr/lib`.

Frameworks are just dynamic libraries with a funny wrapper, so they work the same way. `Foo.framework` might have an install name of `/Library/Frameworks/Foo.framework/Versions/A/Foo`, and that's where the dynamic linker will search for it.

**`@executable_path`**  
 Absolute paths are annoying. Sometimes you want to embed a framework into an application instead of having to install the framework into `/Library` or a similar location.

The Mac's solution to this is `@executable_path`. This is a magic token that, when placed at the beginning of a library's install name, gets expanded to the path of the executable that's loading it, minus the last component. For example, let's say that `Bar.app` links against `Foo.framework`. If `Bar.app` is installed in `/Applications`, `@executable_path` will expand to `/Applications/Bar.app/Contents/MacOS`. If you intend to embed the framework in `Contents/Frameworks`, then you can just set `Foo.framework`'s install name to `@executable_path/../Frameworks/Foo.framework/Versions/A/Foo`. The dynamic linker will expand that to `/Applications/Bar.app/Contents/MacOS/../Frameworks/Foo.framework/Versions/A/Foo` and will find the framework there.

**`@loader_path`**  
 Finding the executable isn't always good enough. Imagine that you ship a plugin or a framework which embeds another framework. Say, `Foo.framework` embeds `Baz.framework`. Even though `Foo.framework` is the one requesting the load, the dynamic linker will still go off of `Bar.app`'s location when figuring out what `@executable_path` refers to, and this won't work right.

Starting in 10.4, Apple provided `@loader_path` which does what you want here. It expands to the full path, minus the last component, of whatever is actually causing the target library to be loaded. If it's an application, then it's the same as `@executable_path`. If it's a framework or plugin, though, then it's relative to that framework or plugin, which is much more useful.

**`@rpath`**  
 While the above is sufficient for anything in theory, it can be troublesome in practice. The problem is that a single copy of a library can only be used in one way. If you want `Foo.framework` to work when embedded in an application or when installed to `/Library/Frameworks`, you have to provide two separate copies with two different install names. (Or manually tweak install names later on using `install_name_tool`.) This is doable, but annoying.

Starting in 10.5, Apple provides `@rpath`, which is a solution to this. When placed at the front of an install name, this asks the dynamic linker to search a list of locations for the library. That list is embedded in the application, and can therefore be controlled by the application's build process, not the framework's. A single copy of a framework can thus work for multiple purposes.

To make this work, `Foo.framework`'s install name would be set to `@rpath/Foo.framework/Versions/A/Foo`. An application that intends to embed `Foo.framework` would then pass `-rpath @executable_path/../Frameworks` to the linker at build time, which tells the dynamic linker to search for `@rpath` frameworks there. An application that intends to install the framework would pass `-rpath /Library/Frameworks`, telling the dynamic linker to search there. An application that for some reason doesn't want to commit to one or the other at build time can just pass both sets of parameters, which will cause the dynamic linker to try both locations.

**Conclusion**  
 Now you hopefully know a little bit more about how dynamic linking works on Mac OS X and how the dynamic linker finds your libraries, including how to embed frameworks in applications, in plugins, and in other frameworks.

Come back next week for another exciting edition. Friday Q&A is driven by your submissions, so if you have an idea for a topic that you would like to see covered here, please [send it in!](mailto:mike@mikeash.com)

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
