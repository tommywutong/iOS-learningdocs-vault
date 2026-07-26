---
title: NSArray Binary Search
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2013/07/nsarray-binary-search/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:890103f0b8555f48'
translated: false
---

> 原文：[NSArray Binary Search](https://oleb.net/blog/2013/07/nsarray-binary-search/)　·　Ole Begemann

# NSArray Binary Search

The other day I learned that [`NSArray`](https://developer.apple.com/library/ios/#documentation/Cocoa/Reference/Foundation/Classes/NSArray_Class/NSArray.html) comes with a binary search method named [`indexOfObject:inSortedRange:options:usingComparator:`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSArray_Class/NSArray.html#//apple_ref/doc/uid/20000137-SW31). Using this method can greatly speed up searching but requires the array to be sorted.

# containsObject: and indexOfObject:

You are probably familiar with the most common methods for searching NSArrays: [`containsObject:`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSArray_Class/NSArray.html#//apple_ref/doc/uid/20000137-BABCEJDI) tells you if its argument is present in the array at all and [`indexOfObject:`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSArray_Class/NSArray.html#//apple_ref/doc/uid/20000137-BABDHGFB) returns the index where the object can be found. Both of these methods iterate over all elements in the array, starting at index 0, until they find a match. In the worst case (there is no match), they have to iterate over the entire array. In [big O notation](https://en.wikipedia.org/wiki/Big_O_notation), the methods’ performance characteristic is O(n).

This is usually not a problem for small arrays with only a few dozen elements. But if your code regularly needs to find objects in arrays with thousands of elements, you may want to look for a faster search algorithm.

**Update July 11, 2013:** [Bavarious](https://objectivistc.tumblr.com) reminded me that despite its name, `NSArray` is [not necessarily implemented with array-like characteristics](https://twitter.com/bavarious/status/355252119542042624). In fact, the [header file for `CFArray`](http://www.opensource.apple.com/source/CF/CF-744/CFArray.h) (on which `NSArray` is based), has this to say on the topic of computational complexity:

> The access time for a value in the array is guaranteed to be at worst O(lg N) for any implementation, current and future, but will often be O(1) (constant time). Linear search operations similarly have a worst case complexity of O(N*lg N), though typically the bounds will be tighter, and so on.

In other words: because random access is not guaranteed to have constant time performance characteristics, linear search can in practice be even slower than O(n). Since binary search is also based on random element access (see below), it will have a similar worst-case performance degradation as linear search compared to pure arrays. Comparing the two algorithms against each other, binary search still comes out way ahead.

In you want to learn more about the surprising performance characteristics of `CFArray`/`NSArray`, I recommend [this article from 2005](http://ridiculousfish.com/blog/posts/array.html).

# Binary Search

If the array is sorted by the search key, [binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm) can give you a huge boost in performance. By comparing the middle element in the array to the search item, the algorithm effectively halves the number of elements it has to search trough with each iteration. Binary search has O(log n) performance. What does this mean in practice? Searching a sorted array of 100,000 elements using binary search would require at most 17 comparisons compared to the 50,000 comparisons a naive linear search would take on average.

This is all you have to do to perform a binary search:

```
NSArray *sortedArray = ... // must be sorted
id searchObject = ...
NSRange searchRange = NSMakeRange(0, [sortedArray count]);
NSUInteger findIndex = [sortedArray indexOfObject:searchObject
                                    inSortedRange:searchRange
                                          options:NSBinarySearchingFirstEqual
                                  usingComparator:^(id obj1, id obj2)
                                  {
                                      return [obj1 compare:obj2];
                                  }];
```

Note that [sorting an array](https://en.wikipedia.org/wiki/Sort_algorithms#Comparison_of_algorithms) is at least an O(n) operation, more likely on the order of O(n log n). Therefore, it does not make sense to sort an array first (using [`sortedArrayUsingComparator:`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSArray_Class/NSArray.html#//apple_ref/doc/uid/20000137-SW28) or a similar method) if all you need to do is a one-time search.

# Keeping Arrays Sorted When Inserting New Objects

You can also use the `indexOfObject:inSortedRange:options:usingComparator:` method to keep a sorted array sorted when you insert a new object. When you call the method with the `NSBinarySearchingInsertionIndex` option, it will return the index at which you should insert the new object in order to keep the array sorted.
