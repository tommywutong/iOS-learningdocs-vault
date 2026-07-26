---
title: '[objc explain]: Selector uniquing in the dyld shared cache'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2009/09/01/objc_explain_Selector_uniquing_in_the_dyld_shared_cache.html'
original_language: en
published: 2009-09-01
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1f9de33b42489426'
translated: false
---

> 原文：[[objc explain]: Selector uniquing in the dyld shared cache](http://sealiesoftware.com/blog/archive/2009/09/01/objc_explain_Selector_uniquing_in_the_dyld_shared_cache.html)　·　Hamster Emporium (Greg Parker)

[![](http://sealiesoftware.com/hamster.jpg)](http://sealiesoftware.com/blog/index.html)  
  
 **blog**  
 [recent](http://sealiesoftware.com/blog/index.html)  
 [archive](http://sealiesoftware.com/blog/archive/index.html)  
 [twitter](http://twitter.com/gparker)  
   
 **projects**  
 [Mac OS X](http://www.apple.com/macosx/)  
 [Keyboard](http://sealiesoftware.com/keyboard/index.html)  
 [backlight](http://sealiesoftware.com/keyboard/index.html)  
 [CSC Menu](http://sealiesoftware.com/cscmenu/index.html)  
 [Valgrind](http://sealiesoftware.com/valgrind/index.html)  
 [Fringe Player](http://sealiesoftware.com/fringe/index.html)  
 [pssh](http://sealiesoftware.com/pssh/index.html)  
 [Peal](http://sealiesoftware.com/peal/index.html)  
 [Frankenmouse](http://sealiesoftware.com/frankenmouse/index.html)

## Hamster Emporium archive

\<\< [Colorized keyboard backlight](http://sealiesoftware.com/blog/archive/2009/09/05/Colorized_keyboard_backlight.html) | [archive](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]: Thread-local garbage collection](http://sealiesoftware.com/blog/archive/2009/08/28/objc_explain_Thread-local_garbage_collection.html) \>\>

[![(link)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2009/09/01/objc_explain_Selector_uniquing_in_the_dyld_shared_cache.html)

**[objc explain]: Selector uniquing in the dyld shared cache** ([2009-09-01 2:10 AM](http://sealiesoftware.com/blog/archive/2009/09/01/objc_explain_Selector_uniquing_in_the_dyld_shared_cache.html))

Mac OS X Snow Leopard cuts in half the launch-time overhead of starting the Objective-C runtime, and simultaneously saves a few hundred KB of memory per app. This comes for free to every app, courtesy of one of the few pieces of Mac OS X that lives below even the Objective-C runtime: dyld.

#### dyld and the shared cache

dyld is the dynamic loader and linker. When your process starts, dyld loads your executable and its shared libraries into memory, links the cross-library C function and variable references together, and starts execution on its way towards `main()`.

In theory a shared library could be different every time your program is run. In practice, you get the same version of the shared libraries almost every time you run, and so does every other process on the system. The system takes advantage of this by building the dyld shared cache. The shared cache contains a copy of many system libraries, with most of dyld's linking and loading work done in advance. Every process can then share that shared cache, saving memory and launch time.

(Incidentally, the shared cache beats the pants off the pre-Leopard prebinding system that was supposed to achieve the same optimizations. Remember the post-install "Optimizing System Performance" step that often took longer than the install itself? That was prebinding being updated. Rebuilding the shared cache is so blazingly fast that the installer doesn't bother to report it anymore.)

#### Objective-C selector uniquing

Leopard's dyld shared cache is great for C code, but it didn't do anything to help Objective-C's startup overhead. The single biggest launch cost for Objective-C is selector uniquing. The app and every shared library contain their own copies of selector names like "alloc" and "init". The runtime needs to choose a single canonical SEL pointer value for each selector name, and then update the metadata for every call site and method list to use the blessed unique value. This means building a big hash table (memory), calling `strcmp()` a lot (time), and modifying copy-on-write metadata (more memory).

There are tens of thousands of unique selectors present in a typical process. If you run ``strings
	/usr/lib/libobjc.dylib`` on Leopard you can see the thirty-thousand-line [built-in selector table](http://www.opensource.apple.com/source/objc4/objc4-371/runtime/objc-sel-table.h) that was a previous attempt to reduce the memory cost. Even so the cost goes up with every new class and method added to Cocoa.framework; left unchecked, an identical app would take longer to launch and use more memory after every OS upgrade.

The obvious solution? Do the work of selector uniquing in the dyld shared cache. Build a selector table into the shared cache itself, and update the selector references in the cached copy of the shared libraries. Then you save memory because every process shares the same selector table, and save time because the runtime does not need to rebuild it during every app launch. The runtime only needs to fix the selector references from the app itself. The catch? Selectors are too dynamic to be implemented as C symbols, so the shared cache construction tool needed to be taught how to read and write Objective-C's metadata.

#### Optimization WIN

Snow Leopard's dyld shared cache uniques Objective-C selectors, and Snow Leopard's Objective-C runtime recognizes when the selectors in a shared library are already uniqued courtesy of the shared cache. About half of the runtime's initialization time is eliminated, making warm app launch several tenths of a second faster. Typical memory savings is 200-500 KB per process, adding up to a few megabytes system-wide. When this optimization ships on the iPhone OS side, it's estimated to save 1 MB on a 128 MB device. The iPhone performance team would pay any number of arms and legs for that kind of gain.

You can watch the system in action with various debugging flags.

```
$ sudo /usr/bin/update_dyld_shared_cache -debug -verify

[...]

update_dyld_shared_cache: for x86_64, uniquing objc selectors

update_dyld_shared_cache: for x86_64, found 68761 unique objc selectors

update_dyld_shared_cache: for x86_64, 541736/590908 bytes (91%) used in	libobjc unique selector section

update_dyld_shared_cache: for x86_64, updated 205230 selector references
```

```
$ OBJC_PRINT_PREOPTIMIZATION=YES /usr/bin/defaults

objc[424]: PREOPTIMIZATION: selector preoptimization ENABLED (version 3)

objc[424]: PREOPTIMIZATION: honoring preoptimized selectors in /usr/lib/libobjc.A.dylib

objc[424]: PREOPTIMIZATION: honoring preoptimized selectors in /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

objc[424]: PREOPTIMIZATION: honoring preoptimized selectors in /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Metadata

objc[424]: PREOPTIMIZATION: honoring preoptimized selectors in /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
```

You can estimate the memory savings with the `allmemory` tool. Record post-launch memory usage of an app run with and without environment variable `OBJC_DISABLE_PREOPTIMIZATION=YES`. Look for the count of dirty pages; each dirty page is 4 KB eaten by that process. With 64-bit TextEdit I see the dirty page count jump from 725 to 1069 after disabling the optimization. This is an overestimate - many of those pages would have been not-dirty in Leopard because of the old built-in selector table - but it does show the magnitude of the win.

The Objective-C runtime does more than just selector uniquing during launch. Future improvements to the dyld shared cache may precompute some of that other work, to further improve launch time, save memory, and reduce the cost of linking to Objective-C code that you don't actually use. But selector uniquing as seen in Snow Leopard is by far the biggest bang for the buck.

[Sealie Software](http://sealiesoftware.com/index.html)
