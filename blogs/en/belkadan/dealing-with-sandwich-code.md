---
title: 'Dealing with "Sandwich Code"'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2011/06/Sandwich-Code/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:33a13913b6f62036'
translated: false
---

> 原文：[Dealing with "Sandwich Code"](https://belkadan.com/blog/2011/06/Sandwich-Code/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [gdba](https://belkadan.com/blog/2011/06/Gdba/)

[Automatic Reference Counting](https://belkadan.com/blog/2011/06/Automatic-Reference-Counting/) »

« [Garbage Collectors and Stack Drawers](https://belkadan.com/blog/2009/06/Garbage-Collectors-and-Stack-Drawers/?tag=programming-languages)

[Recommendations](https://belkadan.com/blog/2015/11/Recommendations/?tag=programming-languages) »

## [Dealing with "Sandwich Code"](#)

I came across the term “sandwich code” for the first time recently as part of the [Ruby Koans](http://rubykoans.com/) Ruby tutorial. It’s not a common term (yet?), but refers to a common resource management problem. Here’s how a lot of people are usually introduced to it:

```
// Top slice of bread
FILE *f = fopen("file.txt", "r");

// The meat (or other filling, if it's a vegetarian sandwich)
if (f) {
    processLinesInFile(f);
}

// Bottom slice of bread
fclose(f);
```

This is okay. In fact it’s completely correct code, and all of it is necessary. If you forget the call to `fclose`, you might (at some point) hit your OS’s limit on the number of files you can have open at once.

Here’s another example:

```
// Top slice of bread
mutex.acquire();

// The meat (or other filling)
char *buf = accessProtectedResource();
if (buf == NULL)
    return;
process(buf);

// Bottom slice of bread
mutex.release();
```

In this case, the consequences of not releasing the lock (mutex) are potentially much worse than simply forgetting to close a file: you could deadlock your entire program. But this code does exactly that if the protected resource is `NULL`: the early return skips the release of the mutex! An easy mistake to make, but a potentially deadly one.

We could fix this. But now suppose we’re using a language with exceptions, like Java. We’d have to do something like this:

```
mutex.acquire();

try {
    char *buf = accessProtectedResource();
    if (buf == null)
        return;
    process(buf);
} finally {
    mutex.release();
}
```

Java is “nice” enough to run the `finally` block whether we get an exception, use the early return, or just finish everything in the `try` block normally. But this code is pretty ugly. Imagine if we had _several_ resources we were trying to use.

Fortunately, there’s a better way. Actually, there are _two_ better ways. The first requires the use of _lexically-scoped functions_—not even full closures. It looks something like this (in pseudo-code):

```
function withMutex (mutex, sandwichMeat) {
    mutex.acquire()
    try {
        result = sandwichMeat()
    } finally {
        mutex.release()
    }
    result
}

// ...in the middle of some other function...
withMutex(mutex, function () {
    buf = accessProtectedResource()
    if (buf == null)
        return
    process(buf)
})
```

Suddenly, all the sandwich code is packaged up inside the `withMutex` procedure. If `withMutex` is the only way to use locks in this system, then you’ll never forget to release your locks again! And it’s already exception-safe.

Ruby has a nice syntax for this that lets you put the “meat” _after_ the function call, instead of inside it, using `do`/`end`:

```
mutex.acquire do
    buf = accessProtectedResource
    if (buf.nil?)
        return
    process(buf)
end
```

And a couple of other languages support similar ideas, though often with a bit more language support. Python’s [`with`](http://effbot.org/zone/python-with-statement.htm) and C#’s [`using`](http://msdn.microsoft.com/en-us/library/yh598w02(v=vs.80).aspx) come to mind; they’re a little clunkier since they don’t have convenient anonymous functions.

I’m a fan of this “scoping” style: it makes it clear that this is my critical section, this is where I’m using a file, whatever.

The alternative is RAII, which stands for Resource Acquisition Is Initialization. Most commonly found in C++, RAII takes advantage of deterministic destruction of stack-based objects when you leave a scope. (This isn’t true in all languages!) Here, you put the “top slice of bread” in the object’s constructor, and the “bottom slice” in the object’s destructor. Then you do something like this:

```
{
    // the CriticalSection constructor acquires the mutex
    CriticalSection cs(mutex);
    
    char *buf = accessProtectedResource();
    if (buf == NULL)
        return;
    process(buf);
    
    // cs destroyed here, releasing the mutex, at the end of the scope
}
```

Like the lexical scoping method, RAII guarantees (via language support) that the mutex will be released, whether you return early, throw an exception, or finish the block normally. An advantage is that you can have several resources with a shared scope without several levels of indent (or an unwieldy `using` list). And if you _want_ to clearly delineate the scope in which your resource is acquired, you can.

First-class functions are useful all over the place, but it looks like in terms of functionality, RAII ekes out a win here. I still like the “scoped blocks” style of _thinking_ better, though…RAII seems too easy to forget. And Apple’s new [Automatic Reference Counting](http://clang.llvm.org/docs/AutomaticReferenceCounting.html#autoreleasepool) syntax seems to agree with me:

```
@autoreleasepool {
    NSString *x = [input lastPathComponent];
    x = [self process:x];
    return [x capitalizedString];
}
```

Still, most languages don’t have first-class functions, `with`/`using`, _and_ deterministic destructors for RAII, so it’s probably best to be reasonably comfortable with all of these, and recognize that they’re just different solutions to the same problems.

This entry was posted on [June](https://belkadan.com/blog/2011/06) 16, [2011](https://belkadan.com/blog/2011) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Programming languages](https://belkadan.com/blog/tags/programming-languages)
