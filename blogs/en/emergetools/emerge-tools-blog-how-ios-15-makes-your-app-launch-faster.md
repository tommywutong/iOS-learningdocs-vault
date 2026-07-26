---
title: 'Emerge Tools Blog | How iOS 15 makes your app launch faster'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/iOS15LaunchTime'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:2e5a448c17337870'
translated: false
---

> 原文：[Emerge Tools Blog | How iOS 15 makes your app launch faster](https://www.emergetools.com/blog/posts/iOS15LaunchTime)　·　Emerge Tools Blog

# How iOS 15 makes your app launch faster

June 23, 2021 by

[Noah Martin](https://twitter.com/sond813)

iOSPerformanceStartup time

![Graphic with text "iOS 15 Startup Time Discoveries"](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fblog3.39576561.png&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

The most intriguing feature from WWDC21 was buried deep in the [Xcode 13 release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-13-beta-release-notes):

> All programs and `dylibs` built with a deployment target of macOS 12 or iOS 15 or later now use the chained fixups format. This uses different load commands and LINKEDIT data, and won't run or load on older OS versions.

There isn't any documentation or sessions to learn more about this change, but we can reverse engineer it to see what Apple is doing differently on the new OSes and if it will help your apps. First, a bit of background on the program that controls app startup.

## [Meet dyld](https://www.emergetools.com/blog/posts/iOS15LaunchTime#meet-dyld)

The dynamic linker ([dyld](https://www.emergetools.com/glossary/dyld)) is the entry point of every app. It's responsible for getting your code ready to run, so it would make sense that any improvement to dyld would result in improved app launch time. Before calling main, running static initializers, or setting up the Objective-C runtime, dyld performs fixups. These consist of rebase and bind operations which modify pointers in the app binary to contain addresses that will be valid at runtime. To see what these look like, you can use the `dyldinfo` command line tool.

```shell
% xcrun dyldinfo -rebase -bind Snapchat.app/Snapchat
rebase information (from compressed dyld info):
segment section          address     type
__DATA  __got            0x10748C0C8  pointer
...
bind information:
segment section address     type    addend dylib        symbol
__DATA  __const 0x107595A70 pointer 0      libswiftCore _$sSHMp
```

This means address `0x10748C0C8` is located in `__DATA/__got` and needs to be shifted by a constant value (known as the slide). While address `0x107595A70` is in `__DATA/__const` and should point to the protocol descriptor for Hashable[1] found in `libswiftCore.dylib`

dyld uses the `LC_DYLD_INFO` load command and [`dyld_info_command`](https://developer.apple.com/documentation/kernel/dyld_info_command) struct to determine the location and size of rebases, binds and [exported symbols](https://github.com/qyang-nj/llios/blob/main/exported_symbol/README.md)[2] in a binary. [Emerge](https://www.emergetools.com), parses this data to let you visualize their contribution to binary size as well as suggest linker flags to make them smaller:

![Treemap chart of dynamic linker content.](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog3%2F1.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

## [A new format](https://www.emergetools.com/blog/posts/iOS15LaunchTime#a-new-format)

When I first uploaded an app built for iOS 15 to [Emerge](https://www.emergetools.com) there was no visualization of dyld fixups. This was because the `LC_DYLD_INFO_ONLY` load command was missing, it had been replaced by `LC_DYLD_CHAINED_FIXUPS` and `LC_DYLD_EXPORTS_TRIE`.

```shell
% otool -l iOS14Example.app/iOS14Example | grep LC_DYLD
  cmd LC_DYLD_INFO_ONLY 

% otool -l iOS15Example.app/iOS15Example | grep LC_DYLD
  cmd LC_DYLD_CHAINED_FIXUPS
  cmd LC_DYLD_EXPORTS_TRIE
```

The export data is exactly the same as before, a trie where each node represents part of a symbol name.

![Diagram displaying a portion of the exports trie for Wikipedia](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog3%2F2.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Portion of the exports trie for Wikipedia

The only change in iOS 15 is the data is now referenced by a [`linkedit_data_command`](https://developer.apple.com/documentation/kernel/linkedit_data_command) which contains the offset of the first node. To validate this, I wrote a short Swift app to parse the iOS 15 binary and print each symbol:

## [Chaining](https://www.emergetools.com/blog/posts/iOS15LaunchTime#chaining)

The real change is in `LC_DYLD_CHAINED_FIXUPS`. Before iOS 15, rebases, binds and lazy binds were each stored in a separate table. Now they have been combined into chains, with pointers to the starts of the chains contained in this new load command:

![Diagram displaying chains.](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog3%2F3.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

The app binary is broken into segments which each contain a chain of fixups that can be either binds or rebases (there are no more lazy binds). Each 64 bit rebase[3] location in the binary now encodes the offset it points to as well as the offset to the next fixup, as seen in this struct:

[dyld_chained_ptr_64_rebase](https://developer.apple.com/documentation/kernel/dyld_chained_ptr_64_rebase)

```swift
struct dyld_chained_ptr_64_rebase
{
uint64_t    target    : 36,
          high8     :  8,
          reserved  :  7,    // 0s
          next      : 12,
          bind      :  1;    // Always 0 for a rebase
};
```

36 bits are used for the pointer target, enough for a 2³⁶ = 64GB binary, and 12 bits are used to provide the offset of the next fixup (stride=4). Therefore it can point anywhere within 2¹² * 4 = 16kb — exactly the page size on iOS.

This very compact encoding means the entire process of walking the chain can be contained within the existing size of the binary. **In my tests over 50% of dyld data's contribution to binary size is saved since only a small amount of metadata is reserved to indicate the first fixup on each page**. The end result was an over 1mb size reduction for large Swift apps.

The source code for this process is in [MachOLoaded.cpp](https://opensource.apple.com/source/dyld/dyld-851.27/dyld3/MachOLoaded.cpp.auto.html) with the binary layout in `/usr/include/macho-o/fixup-chains.h`

## [Order matters](https://www.emergetools.com/blog/posts/iOS15LaunchTime#order-matters)

To understand the motivation behind this change we have to pay attention to one of the most expensive operations during app startup, a page fault. When code on the filesystem is accessed during app launch, it needs to be brought from the file to memory through a page fault. Each 16kb range in an app binary is mapped to a page in memory. Once the page is modified it needs to stay in RAM for as long as the app is running (known as a dirty page). iOS optimizes this by compressing pages that haven't been used recently.

![Diagram displaying a simplified view of virtual memory mappings for segments in an app binary](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog3%2F4.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Simplified view of virtual memory mappings for segments in an app binary

A fixup at app launch requires changing the address in the app binary, so the entire page is marked dirty. Let's look at how many pages are used by fixups during an app launch:

```shell
% xcrun dyldinfo -rebase Snapchat.app/Snapchat > rebases
% ruby -e 'puts IO.read("rebases").split("
").drop(2).map { |a| a.split(" ")[2].to_i(16) / 16384 }.uniq.count'
1554 

% xcrun dyldinfo -bind Snapchat.app/Snapchat > binds
450
```

With the table format, rebases are resolved first, followed by binds. This means rebasing requires many page faults and ends up being mostly IO bound[4]. Binding on the other hand accesses 30% of the pages that rebasing used, effectively doing a second pass through memory.

Now in iOS 15, the chained fixups group all changes for each memory page together. **Dyld can now process them faster with one pass through memory, completing rebases and binds at the same time.** This allows OS features like the memory compressor to take advantage of the well known ordering, not needing to go back and decompress old pages during binding. Because of these changes, the rebase function in dyld becomes a no-op:

![Code snippet from iOS](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog3%2F5.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

[ImageLoaderMachOCompressed.cpp.auto](https://opensource.apple.com/source/dyld/dyld-851.27/src/ImageLoaderMachOCompressed.cpp.auto.html)

Overall this change mostly impacts anyone reverse engineering iOS apps and exploring the details of the dynamic linker, but it's a good reminder of the low level memory management that impacts performance of your apps. While this change only takes effect if you're targeting iOS 15, remember there's still plenty you can do to optimize app startup time:

- Reduce number of [dynamic frameworks](https://www.emergetools.com/glossary/dynamic-frameworks)
- Reduce app size so less memory pages are used
- Move code out of +load and static initializers
- Use [fewer classes](https://medium.com/codestory/why-swift-reference-types-are-bad-for-app-startup-time-90fbb25237fc)
- Defer work to after drawing the first frame

---

[1] The symbol from `dyldinfo` is mangled, you can get the human readable name with `xcrun swift-demangle '_$sSHMp'`.

[2] Exports are the second piece of a bind. One binary binds to symbols exported from its dependencies.

[3] The same goes for binds, a pointer is actually a union of rebase and bind ([dyld_chained_ptr_64_bind](https://developer.apple.com/documentation/kernel/dyld_chained_ptr_64_bind)) with a single bit used to differentiate the two. Binds also require the imported symbol name which isn't discussed here.

[4] https://asciiwwdc.com/2016/sessions/406
