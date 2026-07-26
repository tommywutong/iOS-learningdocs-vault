---
title: Debugging Dyld - Low Level Bits 🇺🇦
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/debugging-dyld/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:abbf0a55b653c36f'
translated: false
---

> 原文：[Debugging Dyld - Low Level Bits 🇺🇦](https://lowlevelbits.org/debugging-dyld/)　·　Low Level Bits (Alex Denisov)

# Debugging Dyld

_Published on Nov 13, 2018_

Recently, I was debugging an interesting issue: a program crashes whenever it tries to call a particular function from a dynamic library. It was not clear how to debug this issue. Eventually, I did resolve the problem: the key was in the dynamic linker, dyld.

In this article, I want to make a short intro on where to start if you have a similar issue. It is by no means an exhaustive guide, but rather a starting point that could have saved me a few hours would I have known this information before.

## Inspect the dyld from inside

The source code of dyld is generally available but is outdated. At the time of writing, you can get the source code for macOS High Sierra, 10.13.6, from [here](https://opensource.apple.com). If you are running the latest version of macOS, 10.14, Mojave, then your last resort is binaries shipped with the OS. Though, the source code from previous versions is still helpful. So to get the full picture, I recommend doing the following:

1. https://opensource.apple.com/
2. Hopper

  ftw) to inspect dyld binaries:

  ,

  , and

  .
3. SIP

  (optional) and run you binary under

  . You can set breakpoints on all dyld related functions:

  or

  for dyld3 only.

During debugging, please be ready to jump a lot between the source code and the three libraries mentioned in step two.

## Inspect the dyld from the outside

There are a few other options to observe the behavior of dyld without looking at the code, source or binary. You will also need to disable [SIP](https://en.wikipedia.org/wiki/System_Integrity_Protection) if you want to exercise it on systems apps. All the options are controlled via environment variables. These are the ones I found the most useful:

- : documented, prints a nice trace of almost everything that is happening inside of dyld. Here is an example output:

```
_dyld_register_func_for_add_image(0x7fff7696ab92)
_dyld_get_image_slide(0x1000f1000)
_dyld_register_func_for_add_image(0x7fff7689cd98)
_dyld_get_image_slide(0x1000f1000)
_dyld_register_func_for_add_image(0x7fff76be67cb)
dyld_image_path_containing_address(0x7fff75221000)
...
```

It looks cryptic, but it greatly helps to understand the program execution flow.

- , documented, prints all the dynamic libraries that are being loaded during the app startup. Here is an example output:

```
dyld: loaded: /usr/lib/libiconv.2.dylib
dyld: loaded: /System/Library/Frameworks/Security.framework/Versions/A/Security
dyld: loaded: /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
dyld: loaded: /usr/lib/libz.1.dylib
dyld: loaded: /usr/lib/libSystem.B.dylib
dyld: loaded: /usr/lib/libresolv.9.dylib
dyld: loaded: /usr/lib/system/libcache.dylib
dyld: loaded: /usr/lib/system/libcommonCrypto.dylib
dyld: loaded: /usr/lib/system/libcompiler_rt.dylib
```

- , undocumented, may print some useful information. Currently, it definitely prints some info about

  dyld3 closures

  . An example output:

```
dyld: found closure 0x7ffff48ae9ac (size=844) in dyld shared cache
dyld: closure 0x7ffff48ae9ac not used because DYLD_FRAMEWORK_PATH changed
```

- , documented, changes the order of directories where dyld will search for dynamic libraries. The nice side effect of using these variables is that their presence disables the dyld3 closure cache. So if your suspect is dyld3 closures, then export any of the

  variables to disable them. Some examples:

```
export DYLD_FRAMEWORK_PATH=
export DYLD_LIBRARY_PATH=
```

For more info, please consult the dyld man page (`man dyld`) or dig through the code, source or binary.

## Summary

Debugging such thing as dyld is a nontrivial task, but it is indeed possible. If you know any other hints or tricks, please share them.

Happy debugging!
