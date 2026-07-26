---
title: 'Friday Q&A 2010-04-09: Comparison of Objective-C Enumeration Techniques'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-04-09-comparison-of-objective-c-enumeration-techniques.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:295fe50431c6835d'
translated: false
---

> 原文：[Friday Q&A 2010-04-09: Comparison of Objective-C Enumeration Techniques](https://www.mikeash.com/pyblog/friday-qa-2010-04-09-comparison-of-objective-c-enumeration-techniques.html)　·　mikeash.com Friday Q&A

Posted at 2010-04-09 11:17 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [An Objective-C Continuations Library](https://www.mikeash.com/pyblog/an-objective-c-continuations-library.html)  
Previous article: [Friday Q&A 2010-04-02: OpenCL Basics](https://www.mikeash.com/pyblog/friday-qa-2010-04-02-opencl-basics.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [nsfastenumeration](https://www.mikeash.com/pyblog/?tag=nsfastenumeration) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2010-04-09: Comparison of Objective-C Enumeration Techniques

by [Mike Ash](https://www.mikeash.com/)

**A Baseline**  
 To establishe a baseline for comparison, consider iterating over a C array of Objective-C objects:

```
    id *array = ...;
    NSUInteger length = ...;
    for(NSUInteger i = 0; i < length; i++)
        // do something with array[i]
```

The syntax is decent, but not great. It's somewhat redundant and a bit error prone.

For single-threaded code, this is about as fast as you're going to get for object enumeration. You have a small amount of overhead from the loop, and it's pretty much the minimum possible. (If you really want to get radical, you can try manually unrolling the loop, but that begins to get crazy, and could actually hurt performance.)

Of course, this sort of object enumeration is not usually practical in Cocoa apps. It's rare that we encounter a C array of objects. Much more common is an object that implements a collection.

**`NSEnumerator`**  
 In times past, the standard way of enumerating over a collection in Cocoa was to use `NSEnumerator`:

```
    NSEnumerator *enumerator = [collection objectEnumerator];
    id obj;
    while((obj = [enumerator nextObject]))
        // do something with obj
```

This is extremely verbose and annoying to write. It also has a fair amount of overhead compared to the baseline. First, it has to allocate a whole new object just to manage enumeration. Then, each iteration involves sending a message to the enumerator. The overhead here, while relatively small compared to most activities that would happen _inside_ the loop, is much larger than the baseline.

**`objectAtIndex:`**  
 For those who preferred something more traditional, or who disliked creating a whole new object just for enumeration, another way to enumerate over an array was to simply call `objectAtIndex:` on it repeatedly:

```
    NSUInteger length = [array count];
    for(NSUInteger i = 0; i < length; i++)
    {
        id obj = [array objectAtIndex: i];
        // do something with obj
    }
```

This still requires a message send per iteration, but avoids creating the `NSEnumerator` object so it can be a bit of a win, depending on just how fast `objectAtIndex:` is for that particular array. (The performance characteristics of `objectAtIndex:` compared to `objectEnumerator` aren't always completely obvious, especially on very large arrays, due to how `NSArray` is implemented internally.)

A big disadvantage, besides being verbose and error-prone, is that it simply doesn't work for enumerating `NSSet` or `NSDictionary`. Conversely, a big advantage is that, with careful management of the loop index, it's safe to mutate the array inside the loop, something that's not true of any other enumeration technique (unless you do something like enumerate over a copy instead).

**`NSFastEnumeration`**  
 In 10.5, Apple finally solved this problem. They solved the verbosity problem by introducing the `for`/`in` syntax. And they solved the speed problem by building `for`/`in` on top of a protocol called `NSFastEnumeration`.

```
    for(id obj in collection)
        // do something with obj
```

`NSFastEnumeration` works by fetching objects in bulk whenever possible. The compiler generates code that calls the collection and asks the collection to return as many objects as possible. For collections that store objects contiguously, the collection is able to return an interior pointer directly to those objects. If every object in the array is contiguous, the loop turns into something very much like the baseline, and with the same overall performance. If there are multiple contiguous object stores, `NSFastEnumeration` allows the collection to return interior pointers one after another, allowing for a quick loop implementation over each store, and requiring an Objective-C message only for getting the next interior pointer. For collections without contiguous storage, `NSFastEnumeration` allows the collection to copy objects out to temporary storage in bulk, reaping many of the same benefits. For collections where none of this works, `NSFastEnumeration` still allows a collection to efficiently return objects one by one.

Nice syntax, good performance, it's a great combination.

**Blocks-Based Enumeration**  
 With 10.6, Apple introduced blocks into Objective-C, and also introduced blocks-based enumeration. Blocks are a natural fit for creating new control constructs like enumeration, and Apple added blocks-based enumeration methods to their collections as well:

```
    [array enumerateObjectsUsingBlock: ^(id obj, NSUInteger index, BOOL *stop) {
        // do something with obj
    }];
```

For simple enumeration, the block syntax doesn't really offer any advantage over fast enumeration and the `for`/`in` syntax. The syntax is a bit clumsier, and iteration is a bit slower. The code has to call your block for every object. This overhead is less than that of a message send, as in the `NSEnumerator` case, but is more than the simple C `for` loop of `NSFastEnumeration`. There are two places where the block syntax is useful.

First is when you need something more than simple enumeration. Apple gives two enumeration options, to enumerate concurrently and to enumerate in reverse. Neither is directly supported by `for`/`in` syntax. Concurrent enumeration is very difficult to do any other way, so if your enumeration can take advantage of multithreading, this is extremely useful. Reverse enumeration can be done by sending `reverseObjectEnumerator` to an array and then using that as the target of a `for`/`in`, but this still has the overhead of creating an `NSEnumerator` and indirecting through it for enumeration, so the blocks-based method is probably a win.

Second is when you're enumerating over a dictionary and need both keys and objects. The `for`/`in` syntax can only give you one object at a time. This means that you have to enumerate over keys, then ask the dictionary for objects as a separate step:

```
    for(id key in dictionary)
    {
        id obj = [dictionary objectForKey: key];
        // do something with key and obj
    }
```

Not only is this much more verbose than a normal `for`/`in`, it's also much slower. The extra message send and dictionary lookup will kill the nice performance characteristics of `NSFastEnumeration`.

`NSDictionary` provides a blocks-based enumeration method that passes both key and object directly to the block:

```
    [dictionary enumerateKeysAndObjectsUsingBlock: ^(id key, id obj, BOOL *stop) {
        // do something with key and obj
    }];
```

This is somewhat nicer to write, and can be much faster. The dictionary is able to directly iterate over key/object pairs in its internal data structure, skipping the extra message send and key lookup required by the `for`/`in` loop.

**Conclusion**  
 With any code, you should always prefer the technique which is easiest to maintain and read unless you know for sure that there's a speed problem which would benefit from a more difficult approach. This is especially true with collection enumeration, where the work that you do inside the loop is virtually certain to dwarf the work that's done by the loop itself.

Fortunately, Apple has made it so that we don't have to make any tradeoffs in most cases. The `for`/`in` syntax is simultaneously the nicest and fastest code for enumerating over a collection in the majority of cases. For the rare cases where it's not the best, 10.6 provides blocks-based enumeration constructs which fill in the holes. You should pretty much never write an `NSEnumerator` loop unless you have to support 10.4. Manually fetching objects using `objectAtIndex:` can be handy if you need to mutate the array while enumerating, but besides that has no advantage over `for`/`in`.

That's it for this week. Come back next week, when I'll talk about how to build your own implementation of the `NSFastEnumeration` protocol. Until then, keep sending me your ideas for topics to talk about. Friday Q&A is driven by reader submissions, so if you have a topic you'd like to see discussed here, [send it in](mailto:mike@mikeash.com)! Next week is already booked, but after that, the future is wide open.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-04-09-comparison-of-objective-c-enumeration-techniques.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
