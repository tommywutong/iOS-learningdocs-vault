---
title: Parallelize Your for Loops With GCD
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2013/07/parallelize-for-loops-gcd-dispatch_apply/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:07b4315bf3c50f1e'
translated: false
---

> 原文：[Parallelize Your for Loops With GCD](https://oleb.net/blog/2013/07/parallelize-for-loops-gcd-dispatch_apply/)　·　Ole Begemann

# Parallelize Your for Loops With GCD

# Concurrent Iteration over Cocoa Collections

Foundation comes with a set of handy methods to enumerate the items in a collection, such as [`enumerateObjectsUsingBlock:`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSArray_Class/NSArray.html#//apple_ref/doc/uid/20000137-SW19). By passing the [`NSEnumerationConcurrent`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Miscellaneous/Foundation_Constants/Reference/reference.html#//apple_ref/doc/uid/TP40003793-CH3g-SW193) flag to the more elaborate version of the same method, [`enumerateObjectsWithOptions:usingBlock:`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSArray_Class/NSArray.html#//apple_ref/doc/uid/20000137-SW18), you can easily parallelize the execution of the blocks that are performed for each element in the collection.

# Concurrent Iteration in Grand Central Dispatch

From reading the excellent [second issue of objc.io](http://www.objc.io/issue-2/), I recently learned that [Grand Central Dispatch](http://developer.apple.com/library/ios/#documentation/Performance/Reference/GCD_libdispatch_Ref/) includes a very similar pattern on a lower level, for those cases where the thing you’re iterating over is not a Cocoa collection: the [`dispatch_apply()`](http://developer.apple.com/library/ios/documentation/Performance/Reference/GCD_libdispatch_Ref/Reference/reference.html#//apple_ref/doc/uid/TP40008079-CH2-SW5) function.

`dispatch_apply()` executes a given block on a given dispatch queue _n_ times, passing the current index of the iteration to the block. The function then waits for all iterations to complete before returning. If you pass a concurrent queue to `dispatch_apply()`, you can basically think of the construct as a parallel (and efficient, as the documentation notes) `for` loop.

Using `dispatch_apply()` in the right places can potentially provide a huge performance boost. If your code processes images on a per-pixel basis or iterates over other memory areas byte by byte, you should definitely look into this. However, as Daniel Eggert stresses in [his article](http://www.objc.io/issue-2/low-level-concurrency-apis.html#iterative_execution), you should measure the performance impact of the parallelization carefully. It could even turn out to be negative:

> How well this works depends a lot on exactly what you’re doing inside that loop.
> 
> The work done by the block must be non trivial, otherwise the overhead is too big. Unless the code is bound by computational bandwidth, it is critical that the memory that each work unit needs to read from and write to fits nicely into the cache size. This can have dramatic effects on performance. Code bound by critical sections may not perform well at all.
