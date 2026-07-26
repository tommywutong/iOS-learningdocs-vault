---
title: Objective-C Literals
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-06-22-objective-c-literals.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6f12c1aef344d269'
translated: false
---

> 原文：[Objective-C Literals](https://www.mikeash.com/pyblog/friday-qa-2012-06-22-objective-c-literals.html)　·　mikeash.com Friday Q&A

Posted at 2012-06-22 14:17 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2012-07-06: Let's Build NSNumber](https://www.mikeash.com/pyblog/friday-qa-2012-07-06-lets-build-nsnumber.html)  
Previous article: [Friday Q&A 2012-06-01: A Tour of PLWeakCompatibility: Part II](https://www.mikeash.com/pyblog/friday-qa-2012-06-01-a-tour-of-plweakcompatibility-part-ii.html)  
Tags: [clang](https://www.mikeash.com/pyblog/?tag=clang) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2012-06-22: Objective-C Literals

by [Mike Ash](https://www.mikeash.com/)

This article is also available in [Hindi (translation by Priti Agarwal)](http://moviehustle.com/objective-c-literals/) and [Hungarian (translation by Szabolcs Csintalan)](http://fertlond.com/objective-c-allandok/).

**Literals**  
For anyone unfamiliar with the term in the context of programming languages, a "literal" refers to any value which can be written out directly in source code. For example, `42` is a literal in C (and, of course, a lot of other languages). It's common to refer to what kind of value they produce, so `42` is an integer literal, `"hello"` is a string literal, and `'x'` is a character literal.

Literals are a foundational building block of most programming languages, since there needs to be _some_ way of writing constant values in code. They aren't strictly necessary, as you can construct any desired value at runtime, but they generally make code a lot nicer to write. For example, we can construct `42` without using any literals:

```
    int fortytwo(void)
    {
        static int zero; // statics are initialized to 0
        static int fortytwo;
        if(!fortytwo)
        {
            int one = ++zero;
            int two = one + one;
            int four = two * two;
            int eight = four * two;
            int thirtytwo = eight * four;
            fortytwo = thirtytwo + eight + two;
        }
        return fortytwo;
    }
```

However, if we had to do this for every integer we used, we'd probably all give up computer programming and go into some profession where the tools don't hate us so much. Likewise, we could construct C strings by hand out of characters, but strings are used so commonly that the language has a concise way to write them.

Collections are pretty commonly used as well. C originally had no facilities for collection literals, but the ability to initialize variables of a compound data type came pretty close:

```
    int array[] = { 1, 2, 3, 4, 5 };
    struct foo = { 99, "string" };
```

This isn't always entirely convenient, and so C99 added _compound literals_, which allow writing such things directly in code anywhere:

```
    DoWorkOnArray((int[]){ 1, 2, 3, 4, 5 });
    DoWorkOnStruct((struct foo){ 99, "string" });
```

Collection literals are pretty common in other languages too. For example, the popular JSON serialization format is just a codification of JavaScript's literal syntax. This JSON code is also valid syntax to create an array of dictionaries in JavaScript, Python, and probably some other languages:

```
    [{ "key": "obj" }, { "key": "obj2" }]
```

Until recently, Objective-C didn't have any syntax for Objective-C collections. The equivalent to the above was:

```
    [NSArray arrayWithObjects:
        [NSDictionary dictionaryWithObjectsAndKeys:
            @"obj", @"key", nil],
        [NSDictionary dictionaryWithObjectsAndKeys:
            @"obj2", @"key", nil],
        nil];
```

This is really verbose, to the extent that it's painful to type and obscures what's going on. The limitations of C variable argument passing also require a `nil` sentinel value at the end of each container creation call, which can fail in extremely odd ways when forgotten. All in all, not a good situation.

**Container Literals**  
The latest clang now has support for container literals in Objective-C. The syntax is similar to that of JSON and modern scripting languages, but with the traditional Objective-C `@` thrown in. Our example array/dictionary looks like this:

```
    @[@{ @"key" : @"obj" }, @{ @"key" : @"obj2" }]
```

There's definitely a bit of `@` overload happening here, but it's a vast improvement over the previous state of things. The `@[]` syntax creates an array from the contents, which must all be objects. The `@{}` syntax creates a dictionary from the contents, which are written as `key : value` instead of the completely ludicrous `value, key` syntax found in the `NSDictionary` method.

Because it's built into the language, there's no need for a terminating `nil`. In fact, using `nil` anywhere in these literals will throw an error at runtime, since Cocoa collections refuse to contain `nil`. As always, use `[NSNull null]` to represent `nil` in collections.

There is no equivalent syntax for `NSSet`. The array literal syntax makes the job a bit nicer, since you can do something like `[NSSet setWithArray: @[ contents ]]`, but there's nothing quite like the concise literal syntax.

Everything you put into such an array or dictionary still has to be an object. You can't fill out an object array with numbers by writing `@[ 1, 2, 3 ]`. However, this is made much easier by the introduction of....

**Boxed Expressions**  
Boxed expressions essentially allow for literals corresponding to primitive types. The syntax is `@(contents)`, which produces an object boxing the result of the expression within the parentheses.

The type of object depends on the type of the expression. Numeric types are converted to `NSNumber` objects. For example, `@(3)` produces an `NSNumber` containing `3`, just like if you wrote `[NSNumber numberWithInt: 3]`. C strings are converted to `NSString` objects using the UTF-8 encoding, so `@("stuff goes here")` produces an `NSString` with those contents.

These can contain arbitrary expressions, not just constants, so they go beyond simple literals. For example, `@(sqrt(2))` will produce an `NSNumber` containing the square root of `2`. The expression `@(getenv("FOO"))` is equivalent to `[NSString stringWithUTF8String: getenv("FOO")]`.

As a shortcut, number literals can be boxed without using the parentheses. Rather than `@(3)`, you can just write `@3`. Applied to strings, this gives us the familiar and ancient construct `@"object string"`. Note that expressions _do not_ work like this. `@2+2` and `@sqrt(2)` will produce an error, and must be parenthesized as `@(2+2)` and `@(sqrt(2))`.

Using this, we can easily create an object array containing numbers:

```
    @[ @1, @2, @3 ]
```

Once again, a bit of `@` overload, but much nicer than the equivalent without the new syntax.

Note that boxed expressions only work for numeric types and `char *`, and don't work with other pointers or structures. You still have to resort to longhand to box up your `NSRect`s or `SEL`s.

**Object Subscripting**  
But wait, there's more! There's now concise syntax for fetching and setting the elements of an array and dictionary. This isn't strictly related to object literals, but arrived in clang at the same time, and continues the theme of making it easier to work with containers.

The familiar `[]` syntax for array access now works for `NSArray` objects as well:

```
    int carray[] = { 12, 99, 42 };
    NSArray *nsarray = @[ @12, @99, @42 ];

    carray[1]; // 99
    nsarray[1]; // @99
```

It works for setting elements in mutable arrays as well:

```
    NSMutableArray *nsarray = [@[ @12, @99, @42 ] mutableCopy];
    nsarray[1] = @33; // now contains 12, 33, 42
```

Note, however, that it's not possible to add elements to an array this way, only replace existing elements. If the array index is beyond the end of the array, the array will not grow to match, and instead it throws an error.

It works the same for dictionaries, except the subscript is an object key instead of an index. Since dictionaries don't have any indexing restrictions, it also works for setting new entries:

```
    NSMutableDictionary *dict = [NSMutableDictionary dictionary];
    dict[@"suspect"] = @"Colonel Mustard";
    dict[@"weapon"] = @"Candlestick";
    dict[@"room"] = @"Library";

    dict[@"weapon"]; // Candlestick
```

As with literals, there is no equivalent notation for `NSSet`, probably because it doesn't make much sense to subscript sets.

**Custom Subscripting Methods**  
In a really cool move, the clang developers made the object subscripting operators completely generic. They're not actually tied into `NSArray` or `NSDictionary` in any way. They simply translate to simple methods which any class can implement.

There are four methods in total: one setter and one getter for integer subscripts, and one setter/getter for object subscripts. The integer subscript getter has this prototype:

```
    - (id)objectAtIndexedSubscript: (NSUInteger)index;
```

You can then implement this to do whatever you want to support the semantics you want. The code simply gets translated mechanically:

```
    NSLog(@"%@", yourobj[99]);
    // becomes
    NSLog(@"%@", [yourobj objectAtIndexedSubscript: 99]);
```

Your code can fetch the index from an internal array, build a new object based on the index, log an error, `abort()`, start a game of pong, or whatever you want.

The corresponding setter has this prototype:

```
    - (void)setObject: (id)obj atIndexedSubscript: (NSUInteger)index;
```

You get the index and the object that's being set there, and then you do whatever you need to do with them to implement the semantics you want. Again, this is just a simple mechanical translation:

```
    yourobj[12] = @"hello";
    // becomes
    [yourobj setObject: @"hello" atIndexedSubscript: 12];
```

The two methods for object subscripts are similar. Their prototypes are:

```
    - (id)objectForKeyedSubscript: (id)key;
    - (void)setObject: (id)obj forKeyedSubscript: (id)key;
```

It's possible to implement all four methods on the same class. The compiler decides which one to call by examining the type of the subscript. Integer subscripts call the indexed variants, and objects call the keyed variants.

This is actually a small chunk of operator overloading now available in Objective-C, which traditionally has completely avoided it. As always, be careful with it to ensure that your custom implementations remain true to the spirit of the subscripting operator. Don't implement the subscripting syntax to append objects or send messages across the network. If you keep it restricted to fetching and getting elements of your object, the usage of the syntax remains consistent and you can more easily understand what code is doing without needing to know all the details.

**Initializers**  
C has an odd quirk in that any initializer of a global variable must be a compile-time constant. This includes simple expressions, but not function calls. For example, the following global variable declaration is legal:

```
    int x = 2 + 2;
```

But this is not:

```
    float y = sin(M_PI);
```

C string literals are compile-time constants, so this is legal:

```
    char *cstring = "hello, world";
```

`NSString` literals are also compile-time constants, so the Cocoa equivalent is legal:

```
    NSString *nsstring = @"hello, world";
```

It's important to note that none of the new literal syntax qualifies as a compile-time constant. Assuming that the array is a global variable, the following is _not_ legal:

```
    NSArray *array = @[ @"one", @"two" ];
```

This is because the `@[]` syntax literally translates into a call to an `NSArray` method. The compiler can't compute the result of that method at compile time, so it's not a legal initializer in this context.

It's interesting to explore exactly why this would be the case. The compiler lays out global variables in your binary, and they are loaded directly into memory. A global variable initialized with `2 + 2` results in a literal `4` being written into memory. A C string initializer results in the string contents being written out in the program's data, and then a pointer to those contents being written out as the global variable's value.

Note that C++, and therefore Objective-C++, _does_ allow non-constant initializers for global variables. When the C++ compiler encounters such an expression, it packages into a function and arranges for that function to be called when the binary loads. Because the initializer code runs so early, it can be a bit dangerous to use, as other code like `NSArray` might not be ready to go yet. In any case, if you've seen a non-constant initializer compile and are wondering why, it was probably being compiled as C++.

`NSString` literals are also compile-time constants, because of a tight coupling between the compiler and the libraries. There's a special `NSString` subclass called `NSConstantString` with a fixed ivar layout:

```
    @interface NSSimpleCString : NSString {
    @package
        char *bytes;
        int numBytes;
    #if __LP64__
        int _unused;
    #endif
    }
    @end

    @interface NSConstantString : NSSimpleCString
    @end
```

It just contains an `isa` (inherited from `NSObject`), a pointer to bytes, and a length. When such a literal is used as a global variable initializer, the compiler simply writes out the string contents, then writes out this simple object structure, and finally initializes the global variable with a pointer to that structure.

You may have noticed that you don't need to retain and release `NSString` literals like you do other objects (although it's still a good idea to do so just out of habit). In fact, you can release them as many times as you want and it won't do anything. This is because `NSString` literals aren't dynamically allocated like most Objective-C objects. Instead, they're allocated at compile time as a part of your binary, and live for the lifetime of your process.

This tight coupling has advantages, like producing legal global variable initializers, and requiring no extra code to run to build the object at runtime. However, there are big disadvantages as well. The `NSConstantString` layout is set forever. That class must be maintained with exactly that data layout, because that data layout is baked into thousands of third-party apps. If Apple changed the layout, those third-party apps would break, because they contain `NSConstantString` objects with the old layout.

If `NSArray` literals were compile-time constants, there would need to be a similar `NSConstantArray` class with a fixed layout that the compiler could generate, and that would have to be maintained separately from other `NSArray` implementations. Such code could not run on older OSes which didn't have this `NSConstantArray` class. The same problem exists for the other classes that the new literals can produce.

This is particularly interesting in the case of `NSNumber` literals. Lion introduced tagged pointers, which allow an `NSNumber`'s contents to be embedded directly in the pointer, eliminating the need for a separate dynamically-allocated object. If the compiler emitted tagged pointers, their format could never change, and compatibility with old OS releases would be lost. If the compiler emitted constant `NSNumber` objects, then `NSNumber` literals would be substantially different from other `NSNumber`s, with a possible significant performance hit.

Instead, the compiler simply emits calls into the framework, constructing the objects exactly like you would have done manually. This results in a bit of a runtime hit, but no worse than building them yourself without the new syntax, and makes for a much cleaner design.

**Compatibility**  
When can we start using this new syntax? Xcode 4.3.3 is the latest shipping version and does not yet include these additions. We can reasonably expect that the next release, presumably coming with Mountain Lion, will incorporate these changes in its version of clang.

For OS compatibility, the literals simply generate code that calls standard Cocoa initializers. The result is indistinguishable from writing the code by hand.

The story for subscripting is a bit more complex. These require new methods that don't exist in Cocoa at the moment. However, the subscripting methods map directly to existing `NSArray` and `NSDictionary` methods, so we can expect a compatibility shim to be made available along the lines of the `ARCLite` shim that allows using `ARC` on OSes that predate it.

**Conclusion**  
The new object literals and subscripting syntax in Objective-C can significantly reduce the verbosity of code that deals heavily with arrays and dictionaries. The syntax is similar to that found in common scripting languages, and makes code much easier to read and write, aside from a minor surplus of `@` symbols.

That's it for today. Come back next time for another friendly exploration of the world of programming. Friday Q&A is as always driven by reader suggestions, so until then, if you have a topic that you'd like to see covered here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-06-22-objective-c-literals.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
