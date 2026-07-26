---
title: 'Friday Q&A 2015-03-20: Preprocessor Abuse and Optional Parentheses'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2015-03-20-preprocessor-abuse-and-optional-parentheses.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b4ee1b4f3de3ce44'
translated: false
---

> 原文：[Friday Q&A 2015-03-20: Preprocessor Abuse and Optional Parentheses](https://www.mikeash.com/pyblog/friday-qa-2015-03-20-preprocessor-abuse-and-optional-parentheses.html)　·　mikeash.com Friday Q&A

Posted at 2015-03-20 14:23 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2015-04-17: Let's Build Swift.Array](https://www.mikeash.com/pyblog/friday-qa-2015-04-17-lets-build-swiftarray.html)  
Previous article: [Friday Q&A 2015-02-20: Let's Build @synchronized](https://www.mikeash.com/pyblog/friday-qa-2015-02-20-lets-build-synchronized.html)  
Tags: [c](https://www.mikeash.com/pyblog/?tag=c) [evil](https://www.mikeash.com/pyblog/?tag=evil) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [preprocessor](https://www.mikeash.com/pyblog/?tag=preprocessor)

Friday Q&A 2015-03-20: Preprocessor Abuse and Optional Parentheses

by [Mike Ash](https://www.mikeash.com/)

**Motivation**  
The C preprocessor is a fairly blind textual replacement engine that doesn't really understand C code, let alone Objective-C. It works well enough for common situations, but occasionally it gets confused.

Here's a typical example:

```
    XCTAssertEqualObjects(someArray, @[ @"one", @"two" ], @"Array is not as expected");
```

This will fail to compile, and produce some really weird errors. The preprocessor looks for commas separating the macro arguments, and it doesn't understand that the stuff in `@[...]` should be considered a single argument. Thus, this code tries to compare `someArray` with `@[ @"one"`. The assertion failure message is `@"two" ]` and `@"Array is not as expected"` is an additional argument. These half-formed components are inserted into the macro expansion of `XCTAssertEqualObjects` and the resulting code is nothing remotely legal.

Fixing this is easy: add parentheses. The preprocessor doesn't know about `[]`, but it _does_ know about `()` and is smart enough to ignore commas inside. This works:

```
    XCTAssertEqualObjects(someArray, (@[ @"one", @"two" ]), @"Array is not as expected");
```

In many parts of C, you can add superfluous parentheses without any penalty. After the macro is expanded, the resulting code still has the parentheses around the array literal, but they do no harm. You can write ludicrous expressions and the compiler happily digs to the bottom for you:

```
    NSLog(@"%d", ((((((((((42)))))))))));
```

You can even subject the `NSLog` to this:

```
    ((((((((((NSLog))))))))))(@"%d", 42);
```

There's one place in C where you can't just add random parentheses: types. For example:

```
    int f(void); // legal
    (int) f(void); // not legal
```

When would this matter? It's uncommon, but it comes up if you have a macro that uses a type, and you have a type that contains a comma that isn't inside parentheses. The macro could do any number of things, and types with un-parenthesized commas can occur in Objective-C when a type conforms to multiple protocols, and in C++ when using templated types with multiple template arguments. For example, here's a simple macro that creates getters that provide statically-typed values from a dictionary:

```
    #define GETTER(type, name) \
        - (type)name { \
            return [_dictionary objectForKey: @#name]; \
        }
```

You could use it like this:

```
    @implementation SomeClass {
        NSDictionary *_dictionary;
    }

    GETTER(NSView *, view)
    GETTER(NSString *, name)
    GETTER(id<NSCopying>, someCopyableThing)
```

No problem so far. Now imagine we want to make one that conforms to _two_ protocols:

```
    GETTER(id<NSCopying, NSCoding>, someCopyableAndCodeableThing)
```

Oops! The macro doesn't work anymore. Adding parentheses won't help:

```
    GETTER((id<NSCopying, NSCoding>), someCopyableAndCodeableThing)
```

This produces invalid code. What we'd like to have is an UNPAREN macro that removes optional parentheses. The `GETTER` macro would be written:

```
    #define GETTER(type, name) \
        - (UNPAREN(type))name { \
            return [_dictionary objectForKey: @#name]; \
        }
```

How do we do it?

**Requring Parentheses**  
It's easy to remove parentheses:

```
    #define UNPAREN(...) __VA_ARGS__
    #define GETTER(type, name) \
        - (UNPAREN type)name { \
            return [_dictionary objectForKey: @#name]; \
        }
```

This looks crazy, but it actually works. The preprocessor will expand `type` to `(id<NSCopying, NSCoding>)`, producing `UNPAREN (id<NSCopying, NSCoding>)`. It will then expand the `UNPAREN` macro to `id<NSCopying, NSCoding>`. Parentheses, begone!

However, the previous uses of `GETTER` now fail. For example, `GETTER(NSView *, view)` produces `UNPAREN NSView *` in the macro expansion. This is not expanded further, and is given to the compiler. The result is, naturally, a compiler error, since `UNPAREN NSView *` is nonsensical. This can be worked around by writing `GETTER((NSView *), view)`, but it's annoying to be forced to add these parentheses. This is not what we want.

**Macros Can't Be Overloaded**  
I immediately thought about how to get rid of the surplus `UNPAREN`. When you want an identifier to disappear, you can use an empty `#define`, like so:

```
    #define UNPAREN
```

With this present, the sequence `a UNPAREN b` turns into `a b`. Perfect! However, the preprocessor rejects this if another definition with arguments is already present. Even though the preprocessor could potentially choose one or the other, it won't allow both forms to be present simultaneously. This would work great if it could be done, but it's not allowed:

```
    #define UNPAREN(...) __VA_ARGS__
    #define UNPAREN
    #define GETTER(type, name) \
        - (UNPAREN type)name { \
            return [_dictionary objectForKey: @#name]; \
        }
```

This will fail to make it through the preprocessor, as it will complain about a duplicate `#define` for `UNPAREN`. It does puts us on the path to victory, though. The trick is to figure out a way to achieve the same effect without making both macros have the same name.

**Bottleneck**  
The ultimate goal is for `UNPAREN(x)` and `UNPAREN((x))` to both produce `x`. A step towards that goal is to make some macro where passing `x` and `(x)` produce the same output, even if it's not exactly `x`. This can be achieved by putting the macro name in the macro expansion, like so:

```
    #define EXTRACT(...) EXTRACT __VA_ARGS__
```

Now if you write `EXTRACT(x)` the result is `EXTRACT x`. And naturally, if you write `EXTRACT x` the result is also `EXTRACT x`, since no macro expansion takes place for that case. This still leaves us with a leftover `EXTRACT`. We can't simply `#define` it away, but it's progress.

**Token Pasting**  
The preprocessor has an operator `##` which pastes two tokens together. For example, `a ## b` becomes `ab`. This can be useful to construct identifiers from pieces, but it can also be used invoke macros. For example:

```
    #define AA 1
    #define AB 2
    #define A(x) A ## x
```

Given this, `A(A)` produces `1` and `A(B)` produces `2`.

Let's combine this operator with the `EXTRACT` macro above to try to produce an `UNPAREN` macro. Since `EXTRACT(...)` produces the argument with a leading `EXTRACT`, we can use token pasting to produce some other token that ends in `EXTRACT`. If we `#define` that new token to nothing, we'll be all set.

Here's a macro ending in `EXTRACT` that produces nothing:

```
    #define NOTHING_EXTRACT
```

Here's an attempt at an `UNPAREN` macro that puts it all together:

```
    #define UNPAREN(x) NOTHING_ ## EXTRACT x
```

Unfortunately, this doesn't get the job done. The problem is order of operations. If we write `UNPAREN((int))`, we get:

```
    UNPAREN((int))
    NOTHING_ ## EXTRACT (int)
    NOTHING_EXTRACT (int)
    (int)
```

The token pasting happens too early, and the `EXTRACT` macro never gets expanded.

You can force the preprocessor to evaluate things in a different order by using indirection. Instead of using `##` directly, let's make a `PASTE` macro:

```
    #define PASTE(x, ...) x ## __VA_ARGS__
```

Then we'll write `UNPAREN` in terms of it:

```
    #define UNPAREN(x) PASTE(NOTHING_, EXTRACT x)
```

This _still_ doesn't work. Here's what happens:

```
    UNPAREN((int))
    PASTE(NOTHING_, EXTRACT (int))
    NOTHING_ ## EXTRACT (int)
    NOTHING_EXTRACT (int)
    (int)
```

It's closer, though. The sequence `EXTRACT (int)` shows up without a token pasting operator present. We just have to get the preprocessor to actually evaluate that before it sees the `##`. Another layer of indirection will force it to behave. Let's define an `EVALUATING_PASTE` macro that just wraps `PASTE`:

```
    #define EVALUATING_PASTE(x, ...) PASTE(x, __VA_ARGS__)
```

Now let's use _this_ one to write `UNPAREN`:

```
    #define UNPAREN(x) EVALUATING_PASTE(NOTHING_, EXTRACT x)
```

Here's the expansion:

```
    UNPAREN((int))
    EVALUATING_PASTE(NOTHING_, EXTRACT (int))
    PASTE(NOTHING_, EXTRACT int)
    NOTHING_ ## EXTRACT int
    NOTHING_EXTRACT int
    int
```

It still works without the surplus parentheses, as the extra evaluation is harmless there:

```
    UNPAREN(int)
    EVALUATING_PASTE(NOTHING_, EXTRACT int)
    PASTE(NOTHING_, EXTRACT int)
    NOTHING_ ## EXTRACT int
    NOTHING_EXTRACT int
    int
```

Success! We can now write `GETTER` to allow but not require parentheses around the type:

```
    #define GETTER(type, name) \
        - (UNPAREN(type))name { \
            return [_dictionary objectForKey: @#name]; \
        }
```

**Bonus Macro**  
While coming up with macros that would justify this construct, I built a nice `dispatch_once` macro for making lazily-initialized constants. Here it is:

```
    #define ONCE(type, name, ...) \
        UNPAREN(type) name() { \
            static UNPAREN(type) static_ ## name; \
            static dispatch_once_t predicate; \
            dispatch_once(&predicate, ^{ \
                static_ ## name = ({ __VA_ARGS__; }); \
            }); \
            return static_ ## name; \
        }
```

Here's an example use:

```
    ONCE(NSSet *, AllowedFileTypes, [NSSet setWithArray: @[ @"mp3", @"m4a", @"aiff" ]])
```

Then you can call `AllowedFileTypes()` to obtain the set, and it's efficiently created on demand. In the unlikely event that the type contains a comma, you can add parentheses and it will still work.

**Conclusion**  
By merely writing this macro, I am a horrible person who deserves terrible things. I hope that exposure to this terror does not warp your mind too much. Use this knowledge with care.

That's it for today. Come back next time for more exciting adventures, probably something less terrifying than this. Until then, if you have any suggestions for topics to cover here, please [send them in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
