---
title: 'Last time on Friday Q&A'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-03-09-lets-build-nsmutablearray.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ca6d931b5607ab36'
translated: false
---

> 原文：[Last time on Friday Q&A](https://www.mikeash.com/pyblog/friday-qa-2012-03-09-lets-build-nsmutablearray.html)　·　mikeash.com Friday Q&A

Posted at 2012-03-09 13:44 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2012-03-16: Let's Build NSMutableDictionary](https://www.mikeash.com/pyblog/friday-qa-2012-03-16-lets-build-nsmutabledictionary.html)  
Previous article: [Friday Q&A 2012-03-02: Key-Value Observing Done Right: Take 2](https://www.mikeash.com/pyblog/friday-qa-2012-03-02-key-value-observing-done-right-take-2.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2012-03-09: Let's Build NSMutableArray

by [Mike Ash](https://www.mikeash.com/)

**Concepts**  
Since `NSMutableArray` is a class cluster, reimplementing it is fairly easy. By subclassing it and then implementing the primitive methods, you end up with a fully functional `NSMutableArray` that supports all of the functionality of any `NSMutableArray`. Here are the primitive methods:

```
    - (NSUInteger)count;
    - (id)objectAtIndex:(NSUInteger)index;
    - (void)addObject:(id)anObject;
    - (void)insertObject:(id)anObject atIndex:(NSUInteger)index;
    - (void)removeLastObject;
    - (void)removeObjectAtIndex:(NSUInteger)index;
    - (void)replaceObjectAtIndex:(NSUInteger)index withObject:(id)anObject;
```

It should be pretty clear how these primitive methods provide enough functionality for all the other `NSMutableArray` methods to be built on. In fact, these primitive methods are already a bit excessive. For example, `addObject:` can be implemented in terms of `insertObject:atIndex:`, and `removeLastObject` can be implemented in terms of `removeObjectAtIndex:`. I'm not entirely clear just why these extra primitive methods exist, but in any case, implementing this full set will give us a fully functional `NSMutableArray` subclass.

The question is then, _how_ do we implement these methods? The idea is to use a C array as the backing storage. Fundamentally, C arrays only support getting and setting values, whereas `NSMutableArray` allows for adding and removing values, which automatically shifts later values around. We'll handle this by copying array entries as necessary. `NSMutableArray` also allows for dynamic expansion of the array, which we'll handle by allocating a new C array and copying the old contents into it when necessary.

**Code**  
As usual, the code for today's escapades is available on GitHub if you want to see it all in one place:

[https://github.com/mikeash/MACollections](https://github.com/mikeash/MACollections)

**Implementation**  
The interface for this class is extremely simple:

```
    @interface MAMutableArray : NSMutableArray
    @end
```

This subclass doesn't add anything new to the interface, so it's just a direct `NSMutableArray` subclass.

Here are the instance variables that this class will use:

```
    @implementation MAMutableArray {
        NSUInteger _count;
        NSUInteger _capacity;
        id *_objs;
    }
```

The C array is `_objs`, and `_capacity` holds the number of elements allocated for the array. The number of elements actually used is stored in `_count`. The capacity and count are stored separately so that the array doesn't need to be reallocated every time an object is added or removed, which would be extremely inefficient.

Next up is the initializer. `NSMutableArray` requires an implementation of `initWithCapacity:` in order for the class to work with built-in convenience methods like `+array`. As far as I know, this is not documented anywhere. For this class, all instance variables can be left at zero, so this initializer doesn't really need to do anything but call `super`:

```
    - (id)initWithCapacity: (NSUInteger)capacity
    {
        return [super init];
    }
```

Note that the `capacity` argument is purely advisory, so it's safe to ignore like this.

Next comes the implementation of `dealloc`. When the array is destroyed, it needs to release all of the objects it contains. While there are faster ways to implement this, I'll implement this by simply removing all of the objects. Besides that, the C array itself needs to be freed, and that's it:

```
    - (void)dealloc
    {
        [self removeAllObjects];
        free(_objs);
        [super dealloc];
    }
```

Now we can move on to the implementation of the various primitive methods. The first one is `count`, which is really easy since it can just return the `_count` instance variable:

```
    - (NSUInteger)count
    {
        return _count;
    }
```

Next is `objectAtIndex:`, which is nearly as simple. It simply fetches the element out of the C array and returns it:

```
    - (id)objectAtIndex: (NSUInteger)index
    {
        return _objs[index];
    }
```

This code omits error checking in the interest of brevity and simplicity. A proper implementation of this method would first check `index` against `_count` and throw an exception if it's out of bounds. As it is here, a bad value for `index` will cause this method to return junk or crash.

**Insertion**  
As mentioned previously, the `addObject:` method can be implemented in terms of `insertObject:atIndex:`, so that is what I do:

```
    - (void)addObject:(id)anObject
    {
        [self insertObject: anObject atIndex: [self count]];
    }
```

With `insertObject:atIndex:`, we finally get to some interesting code. The first thing this method needs to do is resize the backing C array if the current one is full, in order to make room for the new object:

```
    - (void)insertObject: (id)anObject atIndex: (NSUInteger)index
    {
        if(_count >= _capacity)
        {
```

The code must calculate a new capacity to allocate. I use a minimum of `16` elements, which is used for the very first allocation, and then increase the capacity by a factor of `2` for each additional reallocation. Multiplying the capacity by a constant factor for each reallocation has some useful performance consequences which I'll discuss a little later. Here's the code that calculates the new capacity and then allocates the new array with this new capacity:

```
            NSUInteger newCapacity = MAX(_capacity * 2, 16);
            id *newObjs = malloc(newCapacity * sizeof(*newObjs));
```

Next, we need to copy the contents of the old array across. This is a simple `memcpy`:

```
            memcpy(newObjs, _objs, _count * sizeof(*_objs));
```

Finally, the old storage is freed, and the instance variables reassigned to the new storage:

```
            free(_objs);
            _objs = newObjs;
            _capacity = newCapacity;
        }
```

At this point, the array is guaranteed to have enough room for the new object. If the array was previously full, it has now been expanded. If it wasn't full, then it necessarily has room. With that condition satisfied, the next requirement is to move objects around to open up the slot at `index` for the new object. All of the objects in the array after `index` need to shift down by one. This is done with a call to `memmove`:

```
        memmove(_objs + index + 1, _objs + index, ([self count] - index) * sizeof(*_objs));
```

For the unfamiliar, `memmove` is a potentially slower variant of `memcpy` which allows its arguments to overlap. `memcpy` is allowed to assume that its arguments are distinct, and can misbehave if that's not true. This code will have overlapping arguments nearly always, and `memmove` allows that to work.

Let's unpack these arguments briefly. `_objs + index` is the source address for the `memmove`, and is the beginning of the objects that need to be moved. The number of objects that need to be moved is `[self count] - index`, and multiplying that by `sizeof(*_objs)` gives the total size of these pointers in bytes. Finally, they need to be moved down by one slot, so the destination pointer is `_objs + index + 1`.

With room made for the new object, all that remains is to put it into the C array and increase the `_count`:

```
        _objs[index] = [anObject retain];

        _count++;
    }
```

**Removal and Replacement**  
The `removeLastObject` primitive method is implemented by just calling `removeObjectAtIndex:` and passing the last index in the array:

```
    - (void)removeLastObject
    {
        [self removeObjectAtIndex: [self count] - 1];
    }
```

The implementation of `removeObjectAtIndex:` is also relatively simple. The first thing is to release the object being removed:

```
    - (void)removeObjectAtIndex: (NSUInteger)index
    {
        [_objs[index] release];
```

Next, shift all of the objects down with `memmove`. This is essentially the same as the object shifting from `insertObject:atIndex:`, but in the opposite direction:

```
        memmove(_objs + index, _objs + index + 1, ([self count] - index - 1) * sizeof(*_objs));
```

All that remains is to decrement the object count:

```
        _count--;
    }
```

This method should also have some error checking in a real implementation to ensure that `index` is valid, but once again we skip it for this example.

A real implementation of this method would probably also shrink the C array if the count falls under some threshold. If you add a million objects to an array and then remove all of them, you don't want the array still holding memory for a million objects. However, since this isn't strictly necessary and is really just a memory-usage optimization, I have omitted it. The code would look much like the reallocation code in `insertObject:atIndex:`.

The implementation of `replaceObjectAtIndex:withObject:` is also really simple. All it does is retain the new object, release the old object, and then place the new object into that index in the array:

```
    - (void)replaceObjectAtIndex: (NSUInteger)index withObject: (id)anObject
    {
        [anObject retain];
        [_objs[index] release];
        _objs[index] = anObject;
    }
```

And that's it! We now have a fully functional `NSMutableArray` built from scratch.

**Reallocation Cost**  
When reallocating the array, the code increases the capacity by a factor of two each time. This may be an unintuitive approach compared to, say, simply increasing the capacity by a fixed amount each time. Let's examine the performance consequences of these approaches to see why multiplying the capacity by a constant factor is generally better.

First, let's look at the cost incurred in performing a single array reallocation. We can assume that the allocation itself (and freeing the old array) take about the same amount of time no matter how big the array is. The only variable cost is copying the objects from the old array to the new array. Since copying doesn't do anything special, and just moves bytes around one by one, we can assume that if there are \\(\\mathrm{n}\\) objects in the array, the copy will take an amount of time that's approximately proportionate to \\(\\mathrm{n}\\), or in algorithmic complexity terms, this operation is \\(\\mathrm{O(n)}\\). Knowing that each allocation is \\(\\mathrm{O(n)}\\) in the size of the array so far, we can then figure out the complexity of different reallocation strategies.

Let's consider the case where we increase the array by a fixed amount each time. To make the analysis easy, let's say that the array's capacity is increased by \\(\\mathrm{1}\\) each time. This is a pathological case, but it's easy to analyze, and the results carry over to more sane cases. Given this, let's look at the total cost of adding \\(\\mathrm{1000}\\) elements to the array.

Every new element that's added requires a reallocation and incurs a cost proportional to the number of elements in the array so far. The first element costs approximately \\(\\mathrm{1}\\), the second one approximately \\(\\mathrm{2}\\), and so on. The total cost is then \\(\\mathrm{1 + 2 + 3 + \\cdots + 999 + 1000}\\), or \\(\\mathrm{500500}\\).

More generally, the cost to add \\(\\mathrm{m}\\) elements will be \\(\\mathrm{1 + 2 + 3 + \\cdots + m}\\), or: $$\\frac{m * (m + 1)}{2}$$ In algorithmic complexity terms, this can be expressed simply as \\(\\mathrm{O(m^2)}\\). In other words, the total cost to add `m` elements is proportional to the square of `m`. Double the number of elements, and the time to add them will roughly quadruple. Adding a million elements will take roughly a trillion times longer than adding one element, which is not a very happy number.

Let's take a more realistic case, like increasing the capacity by \\(\\mathrm{1024}\\) for each reallocation. In this case, adding \\(\\mathrm{m}\\) elements will cost \\(\\mathrm{1024 + 2048 + 3076 + 4096 + \\cdots + m}\\). If you work it all out, this still turns out to be `O(m``2``)`, although it's still much faster than before. The cost is still proportional to the square of the number of elements, but the cost is smaller by a large constant factor. This is a much more practical way to implement growing the array, but it still has poor asymptotic behavior.

Finally, let's look at the strategy implemented here of doubling the capacity for each reallocation. In this case, the total cost for `m` elements will be approximately \\(\\mathrm{1 + 2 + 4 + 8 + 16 + \\cdots + m}\\), which is just \\(\\mathrm{2m - 1}\\), or \\(\\mathrm{O(m)}\\). In short, the cost to add elements is proportional to the total number of elements added. Add twice as many elements, and it takes about twice as much time.

Interestingly, this holds for other factors as well. For example, let's say that we increase the capacity by 10% each time. This is a little bit harder to work with, since the capacity can only be whole numbers. But if we put that aside for a moment and assume we can deal with fractions, then adding \\(\\mathrm{m}\\) elements costs \\(\\mathrm{1 + 1.1 + 1.21 + \\cdots + m}\\), which works out to about \\(\\mathrm{11m}\\), which is still \\(\\mathrm{O(m)}\\), just with a larger constant factor. In general, _any_ factor \\(\\mathrm{\>1}\\) will result in a net \\(\\mathrm{O(m)}\\) cost to insert \\(\\mathrm{m}\\) elements. However, the larger the factor, the lower the constant multiplier in front, so the faster the allocation will perform.

We end up with an interesting tradeoff. Using larger factors makes the array perform better, but wastes more space. When doubling the allocation, if the array holds \\(\\mathrm{m}\\) elements, there may be space allocated for up to \\(\\mathrm{m - 2}\\) additional elements that isn't being used. If the array continues to grow then it will eventually be used, but if it stops at that point, that space is perpetually wasted. With a 10% allocation increase, at most about \\(\\mathrm{\\frac{m}{10}}\\) space can be wasted, but the time spent in copying and reallocating becomes considerably greater.

**Conclusion**  
The real implementation of `NSMutableArray` is [considerably more complicated that what's presented here](http://ridiculousfish.com/blog/posts/array.html), but the basic principles remain. Now that you see one simple implementation, I hope that this makes the whole concept more clear.

Next time, I'll take this a step further and show an implementation of `NSMutableDictionary` based on a hash table. Until then, your ideas are always welcome for future articles, so [send them in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
