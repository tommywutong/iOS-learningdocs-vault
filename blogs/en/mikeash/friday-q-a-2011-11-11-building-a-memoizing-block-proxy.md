---
title: 'Friday Q&A 2011-11-11: Building a Memoizing Block Proxy'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-11-11-building-a-memoizing-block-proxy.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e5aa00b665a47ea5'
translated: false
---

> 原文：[Friday Q&A 2011-11-11: Building a Memoizing Block Proxy](https://www.mikeash.com/pyblog/friday-qa-2011-11-11-building-a-memoizing-block-proxy.html)　·　mikeash.com Friday Q&A

Posted at 2011-11-11 16:06 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [No Article For you!](https://www.mikeash.com/pyblog/no-article-for-you.html)  
Previous article: [Friday Q&A 2011-10-28: Generic Block Proxying](https://www.mikeash.com/pyblog/friday-qa-2011-10-28-generic-block-proxying.html)  
Tags: [blocks](https://www.mikeash.com/pyblog/?tag=blocks) [evil](https://www.mikeash.com/pyblog/?tag=evil) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [hack](https://www.mikeash.com/pyblog/?tag=hack) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2011-11-11: Building a Memoizing Block Proxy

by [Mike Ash](https://www.mikeash.com/)

**What the Heck is Memoization?**  
In short, memoization is just a cache in front of a function. Imagine a pure function, which is to say, no side effects, and you always get the same result for the same arguments. Now imagine that this function is expensive to compute, and called multiple times with the same arguments. If the result is always the same with the same arguments, it's a waste to constantly recompute it.

The standard answer to this is a cache. Whenever the function computes a result, it can put that result into a dictionary that's keyed off the arguments. Whenever the function is called, it can check the dictionary first to see if the result is already in there. If it is, it can return the previously computed value.

Memoization is the process of performing this caching in a wrapper function. Instead of putting cache code into every function that fits this profile, you write the cache code once, as a wrapper around arbitrary functions. The wrapper has no idea how the function works, but it knows enough to cache return values and bypass the function if a particular set of arguments has already been computed.

**Code**  
As before, the code is available on GitHub here:

[https://github.com/mikeash/MABlockForwarding](https://github.com/mikeash/MABlockForwarding)

**Approach**  
The previous adventures eventually resulted in a `MAForwardingBlock` which takes a block and an interposer, and returns a new block. When the new block is called, the interposer is first called with an `NSInvocation` representing the call. The interposer can then manipulate the `NSInvocation` at will, optionally call through to the original block, and then give the `NSInvocation`'s return value back to the caller.

The goal here is to write an `MAMemoize` function. This function takes a block, and returns a new block which wraps the original. The new block memoizes the original, caching values based on the arguments passed in. `MAMemoize` will use `MAForwardingBlock` to interpose in front of the original block, and use an interposer block to perform the memoization.

In order to accomplish this, the interposer needs to unpack all of the arguments of the `NSInvocation` into an object which can be used as a dictionary key. It also needs to be able to translate the return value to and from an object that can be used as a dictionary value.

Once it's able to do this, the rest is simple. Keep a dictionary which contains the memory. Unpack the arguments, and check to see if the dictionary has an entry for them. If it does, grab the value for those arguments and return it. Otherwise, call through to the original block, then fetch the return value and stash it in the memory dictionary before returning.

**Implementation**  
To start out with, we'll define the `MAMemoize` function. It takes and return `id` because it deals with arbitrary blocks, not just a particular type:

```
    id MAMemoize(id block) {
```

Next up, create the memory dictionary. This is just a local variable, but it will be captured by the interposer block, so it ends up persisting. Blocks can be interesting like that. You can think of a block as being an object with just one method, where the captured variables are instance variables.

```
        NSMutableDictionary *memory = [NSMutableDictionary dictionary];
```

Now we call `MAForwardingBlock` and give it our interposer. The interposer block takes an `NSInvocation` and a block that calls through to the original block. Here's the beginning of the call:

```
        return MAForwardingBlock(^(NSInvocation *inv, void (^call)(void)) {
```

All of the code starting from here runs when the returned block is called. The `inv` argument contains the `NSInvocation` of that call, and the `call` block calls the original function.

The first thing to do is fetch the arguments into an object that can be used as a dictionary key. In this case, I chose to use an `NSArray`. Although this is probably not a very efficient dictionary key, this code isn't very efficient anyway and it does the job fine. The array will be filled out with objects representing each argument.

Fetching the arguments also requires knowing the invocation's method signature, so we grab that at the same time:

```
            NSMethodSignature *sig = [inv methodSignature];
            NSMutableArray *args = [NSMutableArray array];
```

Now, loop through the arguments and add them to the array. Note that the loop starts at argument `1`, because argument `0` is the implicit block pointer argument and doesn't need to be included in the cache:

```
            for(unsigned i = 1; i < [sig numberOfArguments]; i++)
            {
```

For the case where the argument is an object, the task is easy: fetch it using `getArgument:atIndex:` and then stash it in the array. For non-object arguments, life gets more complicated. In fact, it's not possible to handle every possible type, since things like pointer types simply can't be introspected well enough to understand how they're being used.

My approach is to special-case C strings, since they seem like a common parameter type. For all other parameter types, fetch the raw argument into an `NSData` and treat that as the argument, not even making an attempt to interpret the meaning. In practice, this means that all primitive values will work, as will some structs and the rare pointers, like `SEL` which can be compared using `==` and persist for the lifetime of the app.

To start with, I create an `arg` local variable which will hold the extracted object, whatever it is. I also grab the string describing the type of this argument:

```
                id arg = nil;
                const char *type = [sig getArgumentTypeAtIndex: i];
```

The first thing is to check to see if this argument is an object. We can do this by comparing the first character of 'type' with the first character of '@encode(id)':

```
                if(type[0] == @encode(id)[0])
                {
```

For this case, just grab the argument into `arg`. I add a small additional flourish where, if the argument conforms to `NSCopying`, it's copied before being placed into the array:

```
                    [inv getArgument: &arg atIndex: i];
                    if([arg conformsToProtocol: @protocol(NSCopying)])
                        arg = [arg copy];
                }
```

Next, check for a C string (any `char *` parameter is assumed to be a C string) using the same technique. If it is one, pull its contents into an `NSData`:

```
                else if(type[0] == @encode(char *)[0])
                {
                    char *str;
                    [inv getArgument: &str atIndex: i];
                    arg = [NSData dataWithBytes: str length: strlen(str)];
                }
```

Finally, for the fallback case, pull the argument directly into an `NSData`. The `NSGetSizeAndAlignment` function can tell us how large the argument is and thus how large the `NSData` needs to be:

```
                else
                {
                    NSUInteger size;
                    NSGetSizeAndAlignment(type, &size, NULL);
                    arg = [NSMutableData dataWithLength: size];
                    [inv getArgument: [arg mutableBytes] atIndex: i];
                }
```

Now we have this argument in `arg`. Before adding it to the array, since `NSArray` doesn't like `nil`, check for that and use `NSNull` instead:

```
                if(!arg)
                    arg = [NSNull null];
```

Now add the argument to the array and continue looping until all arguments are handled:

```
                [args addObject: arg];
            }
```

Next, we check `memory` to see if the arguments are in it. If they are, we extract the return value and put it into the `NSInvocation`. If they aren't, we call the original block, then extract the return value from the `NSInvocation. In both cases, we need the method's return type, and we need to know if it's an object, a C string, or something else, so we precompute those:

```
            const char *type = [sig methodReturnType];
            BOOL isObj = type[0] == @encode(id)[0];
            BOOL isCStr = type[0] == @encode(char *)[0];
```

Next up, check `memory`. This is done in a `@synchronized` block so that this code is thread safe:

```
            id result;
            @synchronized(memory)
            {
                result = [[[memory objectForKey: args] retain] autorelease];
            }
```

If the arguments exist in the dictionary, then `result` will contain the object representation of the return value. Otherwise, `result` will be `nil`. First, let's look at the case where there is no entry in `memory`:

```
            if(!result)
            {
```

Since there's no saved value, the first thing to do is call the original block to compute the return value:

```
                call();
```

Once this completes, the return value will be contained within the `NSInvocation`. We need to fetch it into an object so it can be stored in `memory`. If the return value is an object, this is really easy. Just use `getReturnValue:` and done:

```
                if(isObj)
                {
                    [inv getReturnValue: &result];
                }
```

If it's a C string, then we need to fetch the string pointer, then convert that to an `NSData`. Note that unlike the argument saving code, I add `1` to the length of the string in order to copy the string's terminating `NUL` byte as well. Since this pointer needs to be returned to the caller, and the caller will expect the terminating `NUL`, this saved additional redundant conversion:

```
                else if(isCStr)
                {
                    char *str;
                    [inv getReturnValue: &str];
                    result = str ? [NSData dataWithBytes: str length: strlen(str) + 1] : NULL;
                }
```

Finally, the fallback case. Like before, we fetch it into an `NSData`, using `NSGetSizeAndAlignment` to figure out the necessary length:

```
                else
                {
                    NSUInteger size;
                    NSGetSizeAndAlignment(type, &size, NULL);
                    result = [NSMutableData dataWithLength: size];
                    [inv getReturnValue: [result mutableBytes]];
                }
```

And again, if the object is `nil`, replace it with `NSNull`:

```
                if(!result)
                    result = [NSNull null];
```

Now that we have the result, store it in `memory`. At this point, we're done with this particular code path. The proper return value is already in the `NSInvocation` and will be returned to the caller:

```
                @synchronized(memory)
                {
                    [memory setObject: result forKey: args];
                }
            }
```

Now let's look at the case where a result was found in `memory`. In that case, all we have to do is stuff the contents of `result` into the `NSInvocation` using `setReturnValue:`. Here, we do the reverse transformation for `nil`, checking `result` for `NSNull` and changing it to `nil`:

```
            else
            {
                if(result == [NSNull null])
                    result = nil;
```

If the return type is an object, a direct call to `setReturnValue:` gets the job done:

```
                if(isObj)
                {
                    [inv setReturnValue: &result];
                }
```

If it's a C string, we have to fetch the string pointer into a local variable, then set that:

```
                else if(isCStr)
                {
                    const char *str = [result bytes];
                    [inv setReturnValue: &str];
                }
```

Otherwise, `result` is an `NSData` of the appropriate length containing the return value. We can just pass the pointer straight into the invocation, and that's all there is to it!

```
                else
                {
                    [inv setReturnValue: [result mutableBytes]];
                }
            }
        }, block);
    }
```

For those of you who have lost track, the `block` at the end of this is the original block which was passed into `MAMemoize`, and tells `MABlockForwarding` which block to wrap.

**Example**  
As an example of memoization, let's look at a simple, computationally-expensive block:

```
    __block uint64_t (^fib)(int) = ^uint64_t (int n) {
        if(n <= 1)
            return 1;
        else
            return fib(n - 1) + fib(n - 2);
    }
```

This `fib` block computes the well known Fibonacci function using recursion. This particular approach is extremely slow. The two recursive calls in the `else` clause result in an exponential growth of computation. Each of the two recursive calls spawns two more recursive calls, which in turn each spawn two more recursive calls, etc.

However, almost all of the calls are redundant. If you analyze it, you'll see that `fib(5)` calls `fib(4)` and `fib(3)`, but then `fib(4)` just calls `fib(3)` again. Memoizing `fib` will make it much faster, since subsequent calls to `fib(3)` will be cached rather than recomputed. There are, of course, much better ways compute the Fibonacci function altogether, but this still serves as an interesting example.

To memoize `fib`, we just call `MAMemoize` and assign the result back to `fib`:

```
    fib = MAMemoize(fib);
```

Since `fib` is declared as `__block`, the recursive calls pick up the memoized version, and the result is massively faster on large values than the original.

**Conclusion**  
This memoization wrapper is not entirely useful. For one thing, it's based on my colossal block proxying hack, which really can't be used in code you intend to ship. Even ignoring that, all of the games played with `NSInvocation` are slow and this is a big problem for code that is, essentially, an optimization.

Despite this, it's a great learning experience. Even if it's not practical, this memoization wrapper illustrates how to deal with `NSInvocation` in complicated situations and deal with some of the variety of argument and return types that you're likely to encounter in the wild. Beyond that, this kind of hacking is just good fun.

That wraps things up for today. Keep those suggestions coming. Friday Q&A is (usually) driven by reader-submitted topics, so if you have a subject you'd like to see covered, [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2011-11-11-building-a-memoizing-block-proxy.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
