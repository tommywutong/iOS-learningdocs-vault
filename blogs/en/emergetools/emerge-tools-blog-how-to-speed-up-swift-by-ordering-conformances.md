---
title: 'Emerge Tools Blog | How To Speed Up Swift By Ordering Conformances'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/how-order-files-speed-up-protocols'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:84f5c9e18a0121d4'
translated: false
---

> 原文：[Emerge Tools Blog | How To Speed Up Swift By Ordering Conformances](https://www.emergetools.com/blog/posts/how-order-files-speed-up-protocols)　·　Emerge Tools Blog

# How To Speed Up Swift By Ordering Conformances

January 25, 2023 by

[Noah Martin](https://twitter.com/sond813)

SwiftiOSPerformance

![How To Speed Up Swift By Ordering Conformances](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fblog12.aa258e6c.jpg&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

The Swift runtime executes a protocol conformance check when you cast a type to a protocol, such as with `as?` or `as!`. This operation is surprisingly slow, as detailed in my [previous post](https://www.emergetools.com/blog/posts/SwiftProtocolConformance). In this article we’ll look at an easy way to speed this up by ~20%, without making any changes to your source code. First, a brief review of protocol conformance checks.

## [Review + iOS 16 improvements](https://www.emergetools.com/blog/posts/how-order-files-speed-up-protocols#pages)

Records of every conformance you write in source code get stored in the __TEXT/__const section of the binary in a form similar to this:

```swift
struct ProtocolConformanceDescriptor {
// Offset to the protocol definition
let protocolDescriptor: Int32
// Offset to the type that conforms to the protocol
var nominalTypeDescriptor: Int32
let protocolWitnessTable: Int32
let conformanceFlags: UInt32
}
```

A typical app can have tens of thousands of these. Many are conformances to common protocols such as `Equatable`, `Hashable`, `Decodable` or `Encodable`. When the Swift runtime encounters something like `myVar as? MyProtocol` (may not be directly in your code, common functions like `String(describing:)` internally do an `as?`) it loops over every `ProtocolConformanceDescriptor` in the binary plus any dynamically linked binaries. This operation is O(n). In the worst case if you need to lookup a protocol conformance record for every type that would be `O(n^2)`.

iOS 16 greatly improves on this. As I explained in a [previous post](https://www.emergetools.com/blog/posts/iOS16LaunchTime), iOS 16 precomputes protocol conformances in the [dyld](https://www.emergetools.com/glossary/dyld) closure, and the Swift runtime consults dyld before running the `O(n)` lookup. At the time of the previous blog post Apple had not released the iOS 16 dyld source code, but now that they have, we can see the actual implementation in the function [`_dyld_find_protocol_conformance_on_disk`](https://github.com/apple-oss-distributions/dyld/blob/c8a445f88f9fc1713db34674e79b00e30723e79d/dyld/DyldAPIs.cpp#L2424). This function is conceptually the same as the [zconform library](https://github.com/EmergeTools/zconform/tree/main) which speeds up these checks using a hash table that maps types to a list of protocols that they conform to.

Although this improvement is in iOS 16, it's difficult to measure in practice because this dyld behavior is disabled when running the app from Xcode or Instruments. Emerge has a [local performance debugging tool](https://docs.emergetools.com/docs/performance-debugging) that works around this and can be used to profile apps that do have access to the dyld closure.

Even with the improvements, there are still 3 cases where you might encounter the slow lookup:

- On the first launch after an app install/update. The dyld closure isn’t built yet, and all conformance lookups are still slow.
- When the conformance lookup results in `nil`. This could use

  `_dyld_protocol_conformance_result_kind_definitive_failure`

  , but a quick scan of the source code reveals this is not yet implemented.
- If you aren’t using iOS 16, such as a user on an older OS or using Swift on a non-apple platform including server side Swift.

With a simple order file, we can improve the runtime of all three of these cases.

## [Order files](https://www.emergetools.com/blog/posts/how-order-files-speed-up-protocols#order-files)

Order files are inputs to the linker which make apps faster by grouping code used together into the same region of the binary. With order files, your app accesses only the memory used by the app launch code rather than reading an entire 100+ MB binary into memory. **This principle relies on the concept of a memory page size. To access one byte of the binary, the entire 16kb page is loaded. It’s beneficial to have the data you need on as few pages as possible.** I previously wrote a [deep dive on order files](https://www.emergetools.com/blog/posts/FasterAppStartupOrderFiles).

Keeping used memory close together is also important to improve the cache hit rate. iPhones have multiple levels of memory caches, for example the iPhone 7/A10 has the following structure [1]

The specifics of speeds are not published by Apple and vary year to year, but some benchmarks show that moving up a level can increase latency by 5x [2].

## [Ordering conformances](https://www.emergetools.com/blog/posts/how-order-files-speed-up-protocols#ordering-conformances)

By default, protocol conformances end up spread throughout the `__TEXT/__const` section of the binary. This is because each module in an app generates their own static binary. When they are linked into the final app, the binaries are placed side by side. Data from different modules is not interleaved in the executable.

Let’s visualize this with the Uber app — the version we’re using has 102,800 conformance records (based on the size of the `__TEXT/__swift5_proto` section) and a 12.7mb `__TEXT/__const` section.

![Figure displaying the distribution of protocols in a binary.](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog12%2F1.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Conformances in each binary page of Uber’s __TEXT/__const section. The y-axis shown the number of conformances on each page. The top figure is a heatmap of conformance counts.

The above figure shows the number of conformances on each page of Uber’s app. A protocol conformance record can vary in size (depends on details like associated types), but the minimum size is 16 bytes. You can have a maximum of 1024 conformance records on a single page of memory.

Interestingly, Uber has a few spikes where a page contains nothing but the minimum sized conformances. This might be due to codegen, such as dependency injection or network models, which creates many simple protocols in one module. There are also a couple regions with no conformances, likely due to non-Swift code in the app. **The key takeaway is that conformances are spread throughout the binary, so almost all pages will be loaded from memory when conformances are enumerated.**

![Figure displaying the distribution of protocols in a binary.](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog12%2F2.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Conformances in each binary page of Lyft’s __TEXT/__const section

Similarly, the above figure shows conformances Lyft’s app. While there are no large spikes, there are about 250 conformances on every page with the exception of one region that is likely non-Swift code.

We can apply the idea of using order files to group data onto as few pages as possible to conformances, and generate an order file that moves all conformances onto their own pages.

![Figure displaying the distribution of protocols in a binary.](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog12%2F3.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Conformances ordered to the beginning of the __TEXT/__const section

The above figure shows the result of using an order file to group conformances. Each of the first ~250 pages now only contain protocol conformance descriptors, with about 500 per page. Conformance records vary in size, so the number of conformances on a page is not always the same. With this ordering, less than half of the section needs to be loaded when performing a protocol conformance lookup. In fact, the total memory used by 250 pages is \< 4MB so in this example they can all fit in the L3 cache of an iPhone 7. In our tests, co-locating the conformances like this resulted in an **over 20% decrease in protocol conformance lookup time on an iPhone 7 running iOS 15!**

You can generate an order file that has this result by parsing the [linkmap](https://docs.emergetools.com/docs/linkmaps) file. All protocol conformances end in Mc so you just need the Swift symbol names matching this pattern that are in the `__TEXT/__const` section. You could write a detailed parser for the structure of a linkmap, but a simple grep should also do the trick:

```shell
cat Binary-arm64-LinkMap.txt | grep -v '<<dead>>|non-lazy-pointer-to-local' | grep -o '_$.*Mc$' > order_file.txt
```

The first grep removes a few symbols that we don’t need, and the second grep filters for just the symbols that are protocol conformance records. All Swift symbols start with _$ and protocol conformance records end in Mc.

That's it! You now have your order file. You can set the Xcode "Order File" build setting to the path of this file, or check out our [docs](https://docs.emergetools.com/docs/launch-booster-ios#using-the-file) with instructions on third party build systems. For something this easy to make, it is definitely worth doing to speed up the app for iOS 15 users or the first launch after an app update on iOS 16. If you try out this improvement on your app I’d love to hear about it! Feel free to [get in touch](https://twitter.com/sond813).

## [Emerge Launch Booster](https://www.emergetools.com/blog/posts/how-order-files-speed-up-protocols#emerge-launch-booster)

Emerge's iOS [Launch Booster](https://www.emergetools.com/product/launchbooster) automates the process of generating an order file and can do all this for you. While the protocol conformance optimization mainly applies to iOS 15 and the first launch of iOS 16, Launch Booster also includes many other optimizations that make apps faster for all your users.

---

[1] https://en.wikipedia.org/wiki/Apple_A10

[2] https://www.anandtech.com/show/14892/the-apple-iphone-11-pro-and-max-review/3
