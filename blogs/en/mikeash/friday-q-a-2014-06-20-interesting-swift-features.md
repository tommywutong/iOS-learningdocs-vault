---
title: 'Friday Q&A 2014-06-20: Interesting Swift Features'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2014-06-20-interesting-swift-features.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:368a3d40475a4741'
translated: false
---

> 原文：[Friday Q&A 2014-06-20: Interesting Swift Features](https://www.mikeash.com/pyblog/friday-qa-2014-06-20-interesting-swift-features.html)　·　mikeash.com Friday Q&A

Posted at 2014-06-20 13:17 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2014-07-04: Secrets of Swift's Speed](https://www.mikeash.com/pyblog/friday-qa-2014-07-04-secrets-of-swifts-speed.html)  
Previous article: [Friday Q&A 2014-06-06: Secrets of dispatch_once](https://www.mikeash.com/pyblog/friday-qa-2014-06-06-secrets-of-dispatch_once.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [swift](https://www.mikeash.com/pyblog/?tag=swift)

Friday Q&A 2014-06-20: Interesting Swift Features

by [Mike Ash](https://www.mikeash.com/)

**Explicit Optionals**  
Swift makes optional values a first-class language construct, and requires that any optional type be explicitly marked as such. For example:

```
    var a: Int
    var b: Int?
```

Here, `a` is a plain `Int` and it always contains some integer value. `b` is an optional `Int` and it either contains an integer value, or it contains nothing.

That example is not so special, but it gets more interesting with other types:

```
    var c: String
    var d: String?
```

Just like above, `c` is a plain `String` and it always contains some string value. `d` is an optional `String` and it can either contain a string value or it can contain nothing.

Let's look at the equivalent Objective-C declarations:

```
    int e;
    NSString *f;
```

Here, `e` is a plain `int`, and it always contains some integer value. `f` is an `NSString *`, which means it can either contain a pointer to an `NSString`, or it can contain `nil`, which generally means "nothing".

Note how `e` is a non-optional type, while `f` is effectively optional. The existence of `NULL` in C (which is the same as `nil` in Objective-C) means that all pointer types in the language are implicitly optional types. If you have a `NSString *`, it means "pointer to `NSString`, or `nil`". If you have a `char *`, it means "pointer to `char`, or `NULL`".

The existence of `NULL` in C blows apart the entire static type system when it comes to pointers. Every pointer type is a half truth. Whenever you see a type "pointer to X", there's always an implied "...or `NULL`."

`NULL` behaves totally differently. You can dereference a pointer, but you can't dereference `NULL`. You can send it messages in Objective-C, but the return value is always `0`, even when that makes no sense:

```
    [nil isEqual: nil] // returns NO!
```

Log a `nil` string, and you get `(null)`. `[nil arrayByAppendingArray: obj]` does not produce a one-element array containing `obj`, but rather `nil`. Everything has two different behaviors: the regular one, and the `nil` or `NULL` one.

This is a major problem because our _code_ doesn't behave that way. Sometimes we write our code for "pointer to X or `NULL`," but sometimes we just write it for "pointer to X." But there is no way to express this latter type in the language.

To illustrate the problem this poses, consider the following two questions:

1. Is `nil` a legal argument to pass to `isEqual:`?
2. is `nil` a legal argument to pass to `isEqualToString:`?

I'll give you a moment while you check the documentation.

The answer to the first question is "yes". The docs say: "May be `nil`, in which case this method returns `NO`."

The answer to the second question is... no? Maybe? The docs don't say. It's generally best to assume that if `nil` isn't explicitly allowed, then it's not legal.

Method parameters can sometimes be `nil`, and sometimes not. Return values are the same way. Some methods never return `nil`, and some do. If a method returns `nil` and you pass the return value to a method that doesn't accept `nil`, trouble ensues. You have to add checks, and the compiler can't help you with this because, as far as it knows, _everything_ accepts `nil`. Even if you can keep on top of everything, the documentation often glosses over the handling of `nil`.

Here's another illustrative question: is this code legal?

```
    free(NULL);
```

In my experience, about 99% of C and Objective-C programmers will say "no". Checks like these are extremely common:

```
    if(ptr)
        free(ptr);
```

But if you check the man page, it turns out to be fine. "The `free()` function deallocates the memory allocation pointed to by `ptr`. If `ptr` is a `NULL` pointer, no operation is performed."

If people frequently get something as simple as this wrong, what hope do we have in more complex situations?

Swift approaches this in a consistent manner by making all types non-optional, and allowing any type to be made optional with an additional annotation.

For types that would be pointers in Objective-C, this solves the inconsistencies caused by `nil` and `NULL`. If a parameter can accept `nil`, then it will be declared as an optional type. If it can't, it won't. The compiler can easily check your code to make sure it's doing the right thing. Likewise, if a return value can be `nil`, it will be an optional type, making it obvious. In the common case, your types will be non-optional, making it clear that they always hold _something_.

Because _any_ type can be made optional, it solves some other problems as well. A lot of methods in the frameworks return special sentinel values to indicate the absence of a return value. For example, `indexOfObject:` returns `NSNotFound`, which is just an alias for `NSIntegerMax`. It's easy to forget about this:

```
    NSUInteger index = [array indexOfObject: obj];
    [array removeObjectAtIndex: index]; // oops
```

The equivalent in Swift would return an optional type:

```
    func indexOfObject(obj: T) -> Int?
```

Not finding the object would be indicated by not returning an integer at all, and the fact that optionals are a different type means the compiler can check everything for you.

**Multiple Return Values**  
Swift allows a function to return multiple values. Or if you look at it in a different way, Swift functions always return one value, but that value can be a tuple which is easily unpacked at the call site.

C and Objective-C support this in two ways, neither of which is great. Functions/methods can return a `struct` or a class containing multiple values, or they can use out parameters. Returning a `struct` is so unwieldy that it's basically never used except in cases where the `struct` is conceptually a single unit, like `frame` returning a `NSRect` or `CGRect`. Out parameters get a lot of use in Cocoa, though, especially for error handling.

The `NSError` class and the corresponding `NSError **` pattern showed up late in the 10.2 era and quickly became pervasive. Where some languages would throw an exception, Cocoa indicates errors by returning an `NSError *` to the caller through a parameter. Code like this is common:

```
    NSError *error;
    NSData *data = [NSData dataWithContentsOfFile: file options: 0 error: &error];
    if(data == nil) {
        // handle error
    }
```

This can get annoying, and since the error is always optional, a lot of code ends up looking like this instead:

```
    NSData *data = [NSData dataWithContentsOfFile: file options: 0 error: NULL];
```

This is bad, but temptation strikes us all.

Multiple return values present another option besides exceptions and out pointers. In Python with PyObjC, for example, this code would look like:

```
    data, error = NSData.dataWithContentsOfFile_options_error_(file, 0, None)
    if not data:
        # handle error
```

It's a bit odd due to the bridging, where you still have to pass `None` for the out parameter even though it's being translated into a second return value. A native Python call might look like:

```
    data, error = Data.dataWithContentsOfFile(file, 0)
```

A Swift version would look almost identical:

```
    let (data, error) = Data.dataWithContentsOfFile(file, 0)
```

This is ultimately a small thing, but `NSError` returns are so common in Cocoa that anything which makes it nicer is welcome. The problem has bothered me enough that I've committed [preprocessor crimes against humanity](https://gist.github.com/mikeash/1355671) trying to build multiple return values in Objective-C, and I'm glad I don't have to anymore.

(I think a good case could be made that an even better way to handle error returns would be with an [either type](http://www.scala-lang.org/api/2.9.3/scala/Either.html). In any case, I look forward to exploring the options.)

**Generics**  
This is a huge one. Swift supports generic classes and functions.

This opens up a lot of possibilities. A big one is that container classes can now have a static type which declares, at compile time, what kind of objects they contain. In Objective-C, you lose static type information as soon as objects go into a container:

```
    NSArray *array = @[ @"a", @"b", @"c" ];
```

We can deal with this, but it's not the best. For one thing, it completely breaks dot syntax:

```
    NSLog(@"%@", array[0].uppercaseString);
```

This fails to compile because the type of `array[0]` is `id` and that doesn't work with dot syntax.

For another, it takes some effort to keep track of what's in the thing. This isn't a big deal for local variables where you set up and use it right away. It can be a bit more of a pain for instance variables, and can be really annoying for parameters and return values. When you fail and get the type wrong, the result is a runtime error.

It gets worse for dictionaries, where there are two types to worry about. I have a lot of instance variables with names like `_idStringToHamSandwichMap` to help me remember that the keys are `NSString` instances and the values are `HamSandwich` instances.

In Swift, the types are not `Array` and `Dictionary`, but `Array<String>` and `Dictionary<String, HamSandwich>`. When you extract an element from the array, the result is not `id` (or `Any`/`AnyObject` in Swift) but `String`. It chains nicely too, so if you ask `Dictionary<String, HamSandwich>` for a list of all of its values, the result is a collection type that knows it contains `HamSandwich` instances.

Functions can be generic as well. This lets you write functions that operate on any type without losing type information when you go through them. For example, you might write a small helper function in Objective-C to provide a default value for a value when the value is `nil`:

```
    id DefaultNil(id first, id fallback) {
        if(first) return first;
        return fallback;
    }
```

(Let's ignore for a moment the nonstandard `?:` operator which provides this exact behavior.)

This works great, but loses type information, so that this doesn't work:

```
    NSLog(@"%@", DefaultNil(myName, genericName).uppercaseString);
```

It's possible to make this better by using macros and the nonstandard `__typeof__` operator, but it gets frightening fast.

The rough equivalent in Swift would look like:

```
    func DefaultNil(first: AnyObject?, fallback: AnyObject) -> AnyObject {
        if first { return first! }
        return fallback
    }
```

Swift's stricter static typing would make this a pain to use, much more so than Objective-C, which loses the type info but basically trusts us when we tell it what it is. However, with generics we can solve the problem easily:

```
    func DefaultNil<T>(first: T?, fallback: T) -> T {
        if first { return first! }
        return fallback
    }
```

This preserves the type so that the return value has the same type of the arguments. Type inference means that you don't even have to tell it which type to use, it just knows from looking at the type of the arguments.

Generics are another example of my [preprocessor crimes against humanity](https://gist.github.com/mikeash/4fa887db918cd8c16ca1) trying to hack them into Objective-C, and I'm really glad to have them for real.

**Type Inference**  
Static typing is nice, but it can lead to painful redundancy in code:

```
    NSString *string = @"hello";
    UIAlertView *alert = [[UIAlertView alloc] initWithTitle...];
```

The compiler knows the type of these expressions, so why do we have to repeat the information every time? With Swift, we don't:

```
    let string = "hello"
    let alert = UIAlertView(...)
```

Despite the superficial appearances to languages like JavaScript, don't be fooled: these are statically typed variables, the type just isn't written out as part of the declaration. If there's ever a case where you really want to make sure that a variable is a certain type (and generate a compiler error if the initializer doesn't match), you can still declare it:

```
    let string: String = ThisMustReturnAString()
```

Verbosity in programming can be good to an extent, to help readability. But Objective-C and Cocoa can take it to an absurd extreme in many cases, and it will be great to have the option to cut down on that.

**Class-like Structs**  
Like Objective-C, Swift has both classes and `struct`s. Unlike Objective-C, Swift `struct`s can contain methods. Instead of a massive crowd of functions for operating on a `struct`, a Swift `struct` can just contain that code as methods. `CGRectGetMaxX(rect)` could turn into `rect.maxX`.

The language also provides a default initializer method if you don't provide one, which saves you the trouble of writing any code for that purpose, and gets rid of ugly functions like `CGRectMake`.

Furthermore, `struct`s are better integrated into the language. In Objective-C, there's an ugly divide between them. The declaration syntax is different, you can't use them with Cocoa collections without boxing them, and with ARC it becomes extremely inconvenient to have Objective-C objects as `struct` members.

In Swift, the declaration syntax is the same. Because the collections use generic types, they have no problem containing `struct`s. Object members work without difficulty. They basically become pass-by-value objects rather than a totally different entity.

The result is that small model classes become a lot nicer in Swift. How many times have you used an `NSMutableDictionary` with a few fixed keys to represent a bag of related data that really should have been a class? If you're like me, the answer is "too many". That's because making a simple Objective-C class is a bit of a pain. This was especially true pre-ARC, but even with ARC it's annoying to make it nice. You _can_ just toss properties into a class and call it a day, of course:

```
    @interface Person : NSObject
    @property (copy) NSString *name;
    @property NSUInteger age;
    @property (copy) NSString *phoneNumber;
    @end
    @implementation Person
    @end
```

But now it's mutable, so you have to hope nobody decides to start changing them. And there's no initializer, so you have to set up instances over several lines of code and hope you didn't forget any. If you want a nice immutable model class, you have to manually write out an initializer and keep it in sync with the properties.

With Swift, it's easy:

```
    struct Person {
        let name: String
        let age: Int
        let phoneNumber: String
    }
```

This automatically produces an initializer and instances are all immutable. As a bonus, it should be more efficient as well, since `struct`s can potentially be allocated inline rather than requiring allocation on the heap.

**Trailing Closures**  
This is a nifty feature that's simultaneously pointless and really nice.

When the last parameter of a function or method is a closure (i.e. a block), Swift allows you to write the block after the call, outside the parentheses. These two calls are equivalent:

```
    dispatch_async(queue, {
        println("dispatch!")
    })

    dispatch_async(queue) {
        println("dispatch!")
    }
```

If the closure is the only parameter, then you don't even need the parentheses:

```
    func MainThread(block: Void -> Void) {
        dispatch_async(dispatch_get_main_queue(), block)
    }

    MainThread {
        println("hello from the main thread")
    }
```

This is interesting because it knocks down a visual barrier separating language constructs from library calls. As I [discussed way back in 2008](https://www.mikeash.com/pyblog/friday-qa-2008-12-26.html), blocks are a great addition to Objective-C because they allow you to write your own control constructs. This showed up in a huge way with GCD, which could provide a ton of useful asynchronous calls that worked a lot like language constructs, but were implemented as library calls. However, with Objective-C, there's still a _syntactic_ difference in how you write calls with blocks compared to how you use built-in language constructs.

For example, Swift (currently, at least) lacks anything like Objective-C's `@synchronized` statement. Trailing closures mean that you could implement your own and make it look exactly the way it would look if it were built in:

```
    synchronized(object) {
        ...
    }
```

If you were doing this in Objective-C, the parentheses couldn't go in the right place and you'd end up with something a little more awkward:

```
    synchronized(object, ^{
        ...
    });
```

This is ultimately a really small thing, because this still works just fine and isn't difficult to read at all. But at the same time, it's great to be able to arrange the code in a more natural way.

**Operator Overloading**  
I imagine this one will be controversial. Unfortunately, there's a huge group of programmers who have been scarred for life by being exposed to C++'s terrible and terrifying operator overloading culture. When the language designer thinks it's a fine idea to overload the `<<` and `>>` bitshifting operators for IO, then you know you're in real trouble. I can't blame people for being scared away.

However, I think that if you look beyond C++, the situation is much better. Operator overloading exists in a lot of other languages and doesn't see the kind of crazy abuse that's so common in C++.

Operator overloading is terrible when people use it just so they can have arbitrary symbols instead of words. It's great when people use it so that the traditional operators can be used for their traditional purposes on new types.

Take a simple Objective-C example:

```
    NSNumber *count = ...;
    count = @([count intValue] + 1);
```

You might write code like this if `count` is being stored in a dictionary or an array somewhere. Dealing with boxing/unboxing just to increment the number is a real pain. It's also somewhat dangerous, since the `NSNumber` value could potentially be beyond what could be stored in an `int`. You could write a method to handle that, but it's still not great:

```
    count = [count add: @(1)];
```

With operator overloading, you can implement `+`, `+=`, and `++` to do the same thing they would do with a regular `int`. The code would then become:

```
    NSNumber *count = ...;
    count++;
```

Of course, generics in Swift mean that `NSNumber` itself is much less commonly needed, but there are many other potential _good_ uses for operator overloading. A big (pun intended) one would be a bignum type. Swift has no built-in type for integers of arbitrary size, but you could implement one yourself that handles all the standard arithmetic operators.

One really interesting example is creating autolayout constraints, as demonstrated by [SwiftAutoLayout](https://github.com/indragiek/SwiftAutoLayout). This uses operator overloading to turn expressions like `view1.al_left() == view2.al_right() * 2.0 + 10.0` into `NSLayoutConstraint` instances. This is _way_ better than Apple's cool but crazy visual format language.

In addition to overloading existing operators, Swift allows you to define entirely new operators from a limited character set. If you really want to, you can create an operator called `<~^~>` and make it do what you want. It will be interesting to see what people do with this, and we'll all have to be really careful not to let this power go to our heads.

**Conclusion**  
Swift is an interesting new language that I'm looking forward to using for real work. It has a lot of features that may seem foreign to someone coming from Objective-C, but I think they ultimately make a lot of sense and will be nice to use.

That's it for today. Come back next time for more goodies. I plan to continue talking about Swift for a while, but topic suggestions are always welcome. If you have something about Swift you'd like to see, great! If it's about something else, I can keep it on file for an appropriate time. Either way, if you have a topic you'd like to see covered, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2014-06-20-interesting-swift-features.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
