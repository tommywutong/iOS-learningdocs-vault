---
title: Dynamic Loader Release Notes
apple_id: TP40001695
resource_type: Release Note
platform: macOS
topic: Xcode
technology: null
published: '2009-07-01'
source_url: https://developer.apple.com/library/archive/releasenotes/DeveloperTools/RN-dyld/index.html
archived_at: '2026-07-18T02:50:29.045541Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Dynamic Loader Release Notes

The dynamic loader for Darwin/OS X is called `dyld`, and it is responsible for loading all frameworks, dynamic libraries, and bundles (plug-ins) needed by a process.

#### Contents:

- [New Features in OS X v10.6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmojvfvjvomq)
- [Bug Fixes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmojvfvjvomy)
- [Deprecated APIs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmojvfvjvona)
- [Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmojvfvjvoni)

### New Features in OS X v10.6

This section contains the dynamic-loader features OS X v10.6 introduces.

### New compressed `LINKEDIT` Segment Format

The traditional format of the `LINKEDIT` segment is modeled on the symbol table entries and relocations created by the assembler when making object files. This format is not ideal for the dynamic loader to process at runtime: It is large and has little locality. OS X v10.6 introduces a new format for the data the dynamic loader needs from the `LINKEDIT` segment. A process can contain Mach-O images in both the new format or traditional format. The dynamic loader allows intermixing of the formats, but uses the new format when available.

The new format is described by the `LC_DYLD_INFO` load command. It has five chunks: rebasing, binding, weak binding, lazy binding, and exported symbols. The format is described in `<mach-o/loader.h>`. The command-line tool `dyldinfo(1)` can be used to display that information.

When building a product targeted at OS X v10.6, the linker, `ld`, creates Macho-O images that contain only the new `LINKEDIT` format; these programs do not run on OS X v10.5 and earlier. When targeting OS X v10.5, the linker creates images that contain both the new and traditional `LINKEDIT` segment format; this practice allows programs to run on OS X v10.5 and run very efficiently on OS X v10.6. (When targeting OS X v10.4 or earlier, the linker produces only the traditional format.)

### Faster Weak-symbol Coalescing

C++ uses weak definitions to solve a number of issues. But if weak symbols are not hidden, the dynamic loader needs to make them unique at runtime. The previous algorithm for doing that was expensive. For every weak symbol in each image, the dynamic loader would look up that symbol in every other image. In OS X v10.6 the algorithm is more efficient: It assumes that weak-symbol duplicates are rare. First, all symbols are bound by their normal two-level namespace binding. Then there is as a separate pass that takes an alphabetized list of weak symbols from each image and iterates through just those weak symbols looking for duplicates. The dynamic loader updates only the duplicates. The new `LINKEDIT` segment format is optimized for this algorithm.

### New `dlsym` Handle

There is a new pseudo handle you can pass to `dlsym` called `RTLD_MAIN_ONLY`. It tells the dynamic loader to search for the symbol only in the main executable.

### Change to `update_dyld_shared_cache` Command-line Tool

This tool creates the dynamic loader shared cache, which improves launch performance. In OS X v10.5, the dynamic loader would automatically start it if it appeared that the shared cache was outdated. In OS X v10.6, `update_dyld_shared_cache(1)` is not automatically run. The Installer runs it when you first install the operating system; Software Update runs it when it updates the operating system. If for some reason you swap out an system dynamic library, you should manually run `update_dyld_shared_cache`.

Restarting the computer in Safe Boot mode deletes the dynamic-loader shared cache.

If you suspect the shared cache is somehow corrupt, you can run:

```
sudo update_dyld_shared_cache -verify
```

which re-creates the cache and compares the result with your actual cache file.

The launch time of Cocoa programs has been improved by caching some Objective-C runtime fix ups in the shared cache. Thus the Objective-C runtime has less work to do during launch.

### Bug Fixes

- `dladdr` now returns information on local (non-global) symbols
- `dyld(1)` has better error messages.

### Deprecated APIs

- Most API in `<mach-o/loader.h>` has been deprecated in OS X v10.5. The cross-platform API in `<dlfcn.h>` is the preferred replacement.

### Known Issues

- Safe Boot deletes the dynamic-loader shared cache, and it is never automatically re-created.

  The shared cache is be re-created the next time a Software Update is done, or you can update it manually, as described in [Change to update_dyld_shared_cache Command-line Tool](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmojvfvjvonq).
- No fast thread local storage.

  [pthread_getspecific(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/pthread_getspecific.3.html#//apple_ref/doc/man/3/pthread_getspecific) is currently the only option.
- No `dl*` way to load memory based Mach-O images.

  `NSCreateObjectFileFromMemory` is deprecated. Some programs decrypt or synthesize Mach-O files in memory. There should be a `dl*` based API that can use a Mach-O file that exists only in memory and not on disk.
- `MH_BINDATLOAD` ignored

  At build time the `ld` option `-bind_at_load` sets the `MH_BINDATLOAD` bit in the [mach_header](https://developer.apple.com/documentation/kernel/mach_header) and [mach_header_64](https://developer.apple.com/documentation/kernel/mach_header_64) flags. But at runtime the dynamic loader does not check for the `MH_BINDATLOAD` bit. (In OS X v10.3 and earlier, this flag was usually used as a workaround to run initializers correctly, which is not necessary in OS X v10.4 and later.)
