---
title: 'Friday Q&A 2015-04-17: Let''s Build Swift.Array'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2015-04-17-lets-build-swiftarray.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4c71585b854cd57e'
translated: false
---

> 原文：[Friday Q&A 2015-04-17: Let's Build Swift.Array](https://www.mikeash.com/pyblog/friday-qa-2015-04-17-lets-build-swiftarray.html)　·　mikeash.com Friday Q&A

Posted at 2015-04-17 13:42 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2015-05-01: Fuzzing with afl-fuzz](https://www.mikeash.com/pyblog/friday-qa-2015-05-01-fuzzing-with-afl-fuzz.html)  
Previous article: [Friday Q&A 2015-03-20: Preprocessor Abuse and Optional Parentheses](https://www.mikeash.com/pyblog/friday-qa-2015-03-20-preprocessor-abuse-and-optional-parentheses.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [swift](https://www.mikeash.com/pyblog/?tag=swift)

Friday Q&A 2015-04-17: Let's Build Swift.Array

by [Mike Ash](https://www.mikeash.com/)

**Value and Reference Semantics**  
Before we get started, let's have a quick refresher on value and reference semantics. Reference semantics are what we're used to from Objective-C and most other object-oriented languages when we use object pointers or references. You might put a reference to an object into a variable:

```
    MyClass *a = ...;
```

Then you copy that variable into another variable:

```
    MyClass *b = a;
```

Now both `a` and `b` refer to the same object. If that object is mutable, then changes made to one will be visible to the other.

Value semantics are how things like `int` behave in Objective-C. With value semantics, the variable contains the actual value, not a reference to the value. When you use `=` you get a new copy of the value. For example:

```
    int a = 42;
    int b = a;
    b++;
```

At this point, `b` contains `43` but `a` still contains `42`.

In Swift, `class` types have reference semantics, and `struct` types have value semantics. If you use `=` on a `class` type, you get a new reference to the same instance. Modifications to that instance are visible to all references. If you use `=` on a `struct` type then you get a copy of that value, independent of the original.

Swift made the unusual move of making arrays and dictionaries have value semantics. For example:

```
    var a = [1, 2, 3]
    var b = a
    b.append(4)
```

In most language, this code (or the equivalent) would result in both `a` and `b` containing a reference to an array containing `[1, 2, 3, 4]`. In Swift, `a` contains `[1, 2, 3]` and `b` contains `[1, 2, 3, 4]`.

**Implementing Value Semantics**  
If your object contains a fixed amount of data, implementing value semantics in Swift is easy: put all of your data into a `struct` and you're done. For example, if you wanted a 2D `Point` type to have value semantics, you can just make a `struct` containing a `x` and `y` values:

```
    struct Point {
        var x: Int
        var y: Int
    }
```

Presto, you have value semantics. But how do you accomplish it for something like `Array`? You can't put all of the array elements in the `struct`, since you don't know how many there are when you write the code. You could create a pointer to the elements:

```
    struct Array<T> {
        var ptr: UnsafeMutablePointer<T>
    }
```

However, you need to take special action any time this `struct` is assigned or destroyed. When the `struct` is assigned, you need to copy the contents to a new pointer so that the new `struct` doesn't share data with the old one. When it's destroyed, the pointer needs to be destroyed as well. Swift does not allow any customization of `struct` assignment or destruction.

Destruction can be solved by using a `class`, which provides `deinit`. The pointer can be destroyed there. `class` doesn't have value semantics, but we can solve this by using `class` for the implementation of the `struct`, and exposing the `struct` as the external interface to the array. This looks something like:

```
    class ArrayImpl<T> {
        var ptr: UnsafeMutablePointer<T>

        deinit {
            ptr.destroy(...)
            ptr.dealloc(...)
        }
    }

    struct Array<T> {
        var impl: ArrayImpl<T>
    }
```

You then write methods on `Array` that forward to implementations on `ArrayImpl`, where the real work is done.

If we just leave it like this, then we still have reference semantics despite using a `struct`. If you make a copy of the `struct`, you'll get a new `struct` that still refers to the old `ArrayImpl`. And we can't customize `struct` assignment, so there's no way to copy the `ArrayImpl` too. The solution to this is not to copy on assignment, but rather copy on mutation. The key is that you still have value semantics if a copy shares a reference with the original as long as that reference points to the _exact same data_ with no changes. It's only when shared data is _changed_ that reference semantics become visibly different from value semantics.

For example, you might implement `append` to first copy the `ArrayImpl` (presuming that there is a `copy` method implemented on `ArrayImpl`, then mutate the copy:

```
    mutating func append(value: T) {
        impl = impl.copy()
        impl.append(value)
    }
```

This gives value semantics for `Array`. Although `a` and `b` will still share a reference to the same underlying data after assignment, any mutation will work on a copy, thus preserving the illusion of not sharing data.

This works fine, but it's terribly inefficient. For example:

```
    var a: [Int] = []
    for i in 0..<1000 {
        a.append(i)
    }
```

This will copy the underlying data storage on every iteration of the loop, and then immediately destroy the previous storage, even though nothing else can see it. How do we fix this?

**`isUniquelyReferenced`**  
This is the new API introduced in Swift 1.2. It does pretty much what it says. Give it a reference to an object and it tells you whether or not it's uniquely referenced. Specifically, it returns `true` if and only if the object has a single strong reference.

Presumably, the implementation checks the object's reference count and returns `true` if the reference count is `1`. Why not just provide a way to query the reference count and call it a day? It could be that this is impractical for some reason, but it's also information that would be really easy to abuse, and providing a wrapper for this single case is safer.

Using this call, the example implementation of `append` can be modified to copy the underlying storage only when necessary:

```
    mutating func append(value: T) {
        if !isUniquelyReferencedNonObjC(&impl) {
            impl = impl.copy()
        }
        impl.append(value)
    }
```

This API is actually a family of three functions. From the Swift module in Xcode:

```
    func isUniquelyReferenced<T : NonObjectiveCBase>(inout object: T) -> Bool
    func isUniquelyReferencedNonObjC<T>(inout object: T?) -> Bool
    func isUniquelyReferencedNonObjC<T>(inout object: T) -> Bool
```

These calls only work on pure Swift classes, not `@objc` types. The first one requires that the type explicitly declare this by subclassing the special `NonObjectiveCBase` class. The other two don't require that, and simply return `false` for all `@objc` types.

I was unable to get my code to compile with `NonObjectiveCBase` and so resorted to `isUniquelyReferencedNonObjC` instead. Functionally, there should be no difference.

**`ArrayImpl`**  
Let's get started with the implementation. I'll begin with `ArrayImpl`, then move on to `Array`.

This will not be a full reimplementation of the entire `Array` API. Instead, I'll implement just enough to make it reasonably functional, and demonstrate the principles involved.

The array contains three pieces of data: a pointer, the count of items in the array, and the total amount of space available in the current memory allocation. Only the pointer and count are required, but by allocating more memory than required and keeping track of the extra space, we can avoid a lot of expensive reallocations. Here's the beginning of the class:

```
    class ArrayImpl<T> {
        var space: Int
        var count: Int
        var ptr: UnsafeMutablePointer<T>
```

The `init` method takes a count and a pointer, and copies the contents of the pointer into the new object. Default values of `0` and `nil` are provided so the `init` can be called without any parameters to create an empty array implementation:

```
        init(count: Int = 0, ptr: UnsafeMutablePointer<T> = nil) {
            self.count = count
            self.space = count

            self.ptr = UnsafeMutablePointer<T>.alloc(count)
            self.ptr.initializeFrom(ptr, count: count)
        }
```

The `initializeFrom` call copies the data into the new pointer. Note that `UnsafeMutablePointer` distinguishes between different kinds of assignments, and it's important to get them all right to avoid crashes. The differences are due to whether the underlying memory is treated as initialized or uninitialized. Upon calling `alloc`, the resulting pointer is uninitialized and potentially filled with garbage. A normal assignment, such as `ptr.memory = ...`, is not legal here, because assignment will deinitialize the existing value before copying the new value. This doesn't matter for something like `Int`, but if you're working with a more complex data type it will crash. Here, `initializeFrom` treats the destination pointer as uninitialized memory, which is exactly what it is.

Next, there's a mutating `append` method. The first thing it does is check to see if the pointer needs to be reallocated. If there's no extra space left, we need a new chunk of memory:

```
        func append(obj: T) {
            if space == count {
```

We'll double the amount of space in the new allocation, with a floor at `16`:

```
                let newSpace = max(space * 2, 16)
                let newPtr = UnsafeMutablePointer<T>.alloc(newSpace)
```

Now copy the data from the old allocation:

```
                newPtr.moveInitializeFrom(ptr, count: count)
```

This is another kind of assignment, which not only treats the destination as uninitialized, but also destroys the source. This saves us the effort of writing code to destroy the contents of the old memory, and might be more efficient too. With the data moved over, the old pointer can be deallocated, and the new data placed into the class's properties:

```
                ptr.dealloc(space)
                ptr = newPtr
                space = newSpace
            }
```

Now we're assured of having enough space, so we can copy the new value into the end of the memory and increment `count`:

```
            (ptr + count).initialize(obj)
            count++
        }
```

The mutating `remove` method is simpler, since there's no need to reallocate memory. First, it destroys the value being removed:

```
        func remove(# index: Int) {
            (ptr + index).destroy()
```

The `moveInitializeFrom` function takes care of shuffling all remaining items down by one:

```
            (ptr + index).moveInitializeFrom(ptr + index + 1, count: count - index - 1)
```

And decrement the `count` to reflect the removal:

```
            count--
        }
```

We also need a `copy` method so the `struct` can make copies of the underlying storage when needed. The actual copying code lives in `init`, so this just creates a new instance and has it perform the copy:

```
        func copy() -> ArrayImpl<T> {
            return ArrayImpl<T>(count: count, ptr: ptr)
        }
```

That's nearly everything. We just have to ensure that the class cleans up after itself when it's destroyed by using `deinit` to destroy the values in the array and deallocate the pointer:

```
        deinit {
            ptr.destroy(count)
            ptr.dealloc(space)
        }
    }
```

Let's move on to the `Array` `struct`. Its only property is an `ArrayImpl`:

```
    struct Array<T>: SequenceType {
        var impl: ArrayImpl<T> = ArrayImpl<T>()
```

All `mutating` functions will start by checking to see if `impl` is uniquely referenced, and copying it if it's not. This is wrapped up in a function that they will all call:

```
       mutating func ensureUnique() {
            if !isUniquelyReferencedNonObjC(&impl) {
                impl = impl.copy()
            }
        }
```

`append` is then just a matter of calling `ensureUnique` and then calling the `append` method of `ArrayImpl`:

```
        mutating func append(value: T) {
            ensureUnique()
            impl.append(value)
        }
```

The same goes for `remove`:

```
        mutating func remove(# index: Int) {
            ensureUnique()
            impl.remove(index: index)
        }
```

The `count` property just passes through to `ArrayImpl`'s:

```
        var count: Int {
            return impl.count
        }
```

Subscripting reaches directly into the underlying pointer. If we were writing this code for real, we'd want a range check here (and in `remove`), but I omitted it from the example:

```
        subscript(index: Int) -> T {
            get {
                return impl.ptr[index]
            }
            mutating set {
                ensureUnique()
                impl.ptr[index] = newValue
            }
        }
```

Finally, `Array` implements `SequenceType` so it can be used in a `for in` statement. This requires a `Generator` `typealias` and a `generate` function. The built-in `GeneratorOf` type makes it easy to implement. `GeneratorOf` takes a block that returns the next element in the collection each time it's called, or `nil` when it reaches the end, and produces a `GeneratorType` that wraps that block:

```
        typealias Generator = GeneratorOf<T>
```

The `generate` function starts at index `0` and increments until it runs off the end, then starts returning `nil`:

```
        func generate() -> Generator {
            var index = 0
            return GeneratorOf<T>({
                if index < self.count {
                    return self[index++]
                } else {
                    return nil
                }
            })
        }
    }
```

And that's it!

**`Array`**  
Our `Array` is a generic `struct` that conforms to `CollectionType`:

```
    struct Array<T>: CollectionType {
```

The only data it contains is a reference to an underlying `ArrayImpl`:

```
        private var impl: ArrayImpl<T> = ArrayImpl<T>()
```

Any method that mutates the array must first check to see if `impl` is uniquely referenced, and copy it if it's not. That functionality is wrapped up in a private method that the others can call:

```
        private mutating func ensureUnique() {
            if !isUniquelyReferencedNonObjC(&impl) {
                impl = impl.copy()
            }
        }
```

The `append` method calls `ensureUnique` and then invokes `append` on the `impl`:

```
        mutating func append(value: T) {
            ensureUnique()
            impl.append(value)
        }
```

The implementation for `remove` is nearly identical:

```
        mutating func remove(# index: Int) {
            ensureUnique()
            impl.remove(index: index)
        }
```

The `count` property is a computed property that just calls through to the `impl`:

```
        var count: Int {
            return impl.count
        }
```

The subscript implementation directly modifies the underlying data within the `impl`. Normally this sort of direct access from outside a class would be a bad idea, but `Array` and `ArrayImpl` are so closely tied together that it doesn't seem too harmful. The `set` side of `subscript` mutates the array and so calls `ensureUnique` to preserve value semantics:

```
        subscript(index: Int) -> T {
            get {
                return impl.ptr[index]
            }
            mutating set {
                ensureUnique()
                impl.ptr[index] = newValue
            }
        }
```

The `CollectionType` protocol requires an `Index` `typealias`. For `Array`, the index type is just `Int`:

```
        typealias Index = Int
```

It also requires properties that provide a start and end index. For `Array`, the start index is `0` and the end index is the number of items in the array:

```
        var startIndex: Index {
            return 0
        }

        var endIndex: Index {
            return count
        }
```

The `CollectionType` protocol includes `SequenceType`, which is what allows objects to be used in a `for`/`in` loop. It works by having the sequence provide a generator, which is an object that can return successive elements of the sequence. The generator type is defined by the type that adopts the protocol. `Array` just uses `GeneratorOf`, which is a handy wrapper that allows creating a generator with a closure:

```
        typealias Generator = GeneratorOf<T>
```

The `generate` method has to return a generator. It uses `GeneratorOf` and provides a closure that increments an index until it hits the end of the array. By declaring `index` outside of the closure, it gets captured and its value persists across calls:

```
        func generate() -> Generator {
            var index = 0
            return GeneratorOf<T>{
                if index < self.count {
                    return self[index++]
                } else {
                    return nil
                }
            }
        }
    }
```

That completes the implementation of `Array`.

**Full Implementation and Test Code**  
The full implementation presented here, plus some tests that make sure everything works properly, is available on GitHub:

[https://gist.github.com/mikeash/63a791f2aec3318c7c5c](https://gist.github.com/mikeash/63a791f2aec3318c7c5c)

**Conclusion**  
The addition of `isUniquelyReferenced` to Swift 1.2 is a welcome change that allows implementing some pretty interesting data structures, including replicating the value semantics of the standard library's collections.

That's it for today. Come back next time for more fun, action, and fun and action. Until then, if you have a topic you'd like to see covered here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2015-04-17-lets-build-swiftarray.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
