---
title: 'Friday Q&A 2011-06-03: Objective-C Blocks vs. C++0x Lambdas: Fight!'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-06-03-objective-c-blocks-vs-c0x-lambdas-fight.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:8c7de33f54d030cc'
translated: false
---

> 原文：[Friday Q&A 2011-06-03: Objective-C Blocks vs. C++0x Lambdas: Fight!](https://www.mikeash.com/pyblog/friday-qa-2011-06-03-objective-c-blocks-vs-c0x-lambdas-fight.html)　·　mikeash.com Friday Q&A

Posted at 2011-06-03 15:11 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2011-06-17: gdb Tips and Tricks](https://www.mikeash.com/pyblog/friday-qa-2011-06-17-gdb-tips-and-tricks.html)  
Previous article: [Friday Q&A 2011-05-20: The Inner Life of Zombies](https://www.mikeash.com/pyblog/friday-qa-2011-05-20-the-inner-life-of-zombies.html)  
Tags: [blocks](https://www.mikeash.com/pyblog/?tag=blocks) [c++](https://www.mikeash.com/pyblog/?tag=c%2B%2B) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2011-06-03: Objective-C Blocks vs. C++0x Lambdas: Fight!

by [Mike Ash](https://www.mikeash.com/)

**Terminology**  
 I will refer to Apple's blocks extension as "Objective-C blocks" even though this is not entirely correct. They are actually an addition to C (and can even be used in C++), with some extra behaviors to make them more useful in Objective-C. However, they are deeply intertwined with Objective-C in their implementation, and "C blocks" is vague, so I think that "Objective-C blocks" is the best way to refer to them here.

C++0x lambdas are part of C++ only and can't be used from C. Presumably they can be used in Objective-C++ if the compiler supports C++0x.

For a generic term to refer to both Objective-C blocks and C++0x lambdas, I will use "anonymous function".

**Syntax**  
 Both Objective-C blocks and C++0x lambdas have the same basic goal: to allow writing anonymous inline functions. Called closures, blocks, lambdas, or just anonymous functions, these are a common feature in higher level languages. They are extremely useful for building convenient, succint libraries for things like array iteration, multithreading, delayed computation, and many others.

As lower level languages, C and C++ had no concept of anonymous functions. To add them, new syntax had to be created. Because of this, Objective-C blocks and C++0x lambdas ended up with somewhat different syntax. An empty Objective-C block looks like this:

```
    ^{}
```

Whereas an empty C++0x lambda looks like this:

```
    []{}
```

So far not much different. They both use the standard C `{}` symbols to separate a block of code, with a special symbol to indicate that this is a block or lambda, not a normal C block. In both cases, the `{}` section takes normal code.

The anonymous function can take arguments by writing them in parentheses, in the style of function arguments, after the leading bit:

```
    ^(int x, NSString *y){} // ObjC, take int and NSString*
    [](int x, std::string y){} // C++, take int and std::string
```

In both languages, a value can be returned, and the return type can be inferred from the return statement:

```
    ^{ return 42; } // ObjC, returns int
    []{ return 42; } // C++, returns int
```

Here, the two features begin to diverge. With C++0x lambdas, the return type can only be inferred if the lambda contains a single statement, and that statement is a return statement. So while the above is valid, this is not:

```
    []{ if(something) return 42; else return 43; }
```

In a more complicated lambda with an inferred return type, the return type is always inferred to be `void`. The code above will therefore produce an error, because it's invalid to return `42` from something with a return type of `void`.

In contrast, Objective-C blocks do return type inference no matter how complicated the code is inside of the block. If no return statements are present, the type is inferred as `void`. Otherwise, it examines all of the return statements in the block. If they all return the same type, then the return type of the block is inferred to be that same type. If they conflict, an error is generated. Thus, the equivalent Objective-C example to the invalid C++0x lambda example works fine:

```
    ^{ if(something) return 42; else return 43; }
```

Both features also allow the explicit declaration of a return type. This is essential with C++0x lambdas, where it's the only way to have a complicated lambda return a value. It's merely a convenience in Objective-C, but often useful to avoid having to cast in return statements.

With Objective-C blocks, the return type is declared immediately after the `^`. In C++0x, the return type is declared by placing `->type` after the lambda's argument list. Here are those two examples with explicit return types, which allows it to work in both languages:

```
    []()->int { if(something) return 42; else return 43; }
    ^int { if(something) return 42; else return 43; }
```

Note that an arguments declaration is required for C++0x lambdas, although it can be empty, if an explicit return type is declared. Objective-C blocks can declare either a return type or an argument list separately, or have both together. For completeness, here is the same example with an argument list:

```
    ^int (void) { if(something) return 42; else return 43; }
```

Finally, both Objective-C blocks and C++0x lambdas are called in the same way: use the standard `()` operator on an expression of the appropriate type. Pass arguments if they are required. This calls the anonymous function.

**Type**  
 Objective-C blocks introduce a new class of language-level types to represent block types. They match the standard (but tricky) syntax for C function pointer types, but with a `^` in place of the `*`:

```
    void (*)(int) // function pointer taking int and returning void
    void (^)(int) // block taking int and returning void
```

These types can be used for function/method parameters, return types, local variables, instance variables, etc.

C++0x takes a completely different approach. Lambdas have a unique anonymous type which implements `operator()`. In other words, you can call it, but otherwise you don't have an accessible type the way Objective-C blocks do. In order to store them in variables, pass them to functions, or return them from functions, C++ templates or the C++0x `auto` keyword (which infers the type of a variable from the type of its initializer) must be used.

**Captured Variables**  
 One of the most significant features of these anonymous functions is the ability to capture variables from the enclosing scope. For example:

```
    int x = 42;
    void (^block)(void) = ^{ printf("%d\n", x); };
    block(); // prints 42
```

The two constructs handle variable capture significantly differently, so I'll take them one at a time.

Objective-C blocks can capture variables from the enclosing scope by simply referring to them within the block, as seen above. By default, all captured variables are copied at the point where the block is created and cannot be modified from within the block.

If a block captures another block variable, that block's memory is automatically managed. It's copied and released as necessary. Objective-C object pointers are also automatically managed by retaining and releasing them as necessary. This deep, implicit integration with Objective-C memory management makes a lot of tasks significantly easier, because most of the time blocks automatically do the right thing with the variables they capture.

For cases where the block needs to be able to modify a captured variable, the variable must be declared with the special `__block` qualifier to mark it as being mutable:

```
    __block int x = 42;
    void (^block)(void) = ^{ x = 43; };
    block(); // x is now 43
```

It is important to note that the automatic memory management of block and object pointers does _not_ occur for variables qualified with `__block`, so the programmer needs to make sure that everything is built to tolerate that. For primitives like `x` above, there is no concern.

It should come as no surprise that C++0x lambdas offer considerably greater flexibility but also considerably greater complication in this area. The overall philosophy of C++ appears to be to give the programmer as many tools and choices as possible, which has its pros and cons.

The initial `[]` which begins a C++0x lambda controls how local variables are captured. If it's left empty like that, then no variables can be captured at all. In order to capture variables, it's necessary to tell the compiler what you want to do.

The most explicit way to do this is to list the variables to be captured inside the `[]`. Any variable listed directly by name is captured by value. Any variable listed with a leading `&` is captured by reference. For example:

```
    int x = 42;
    int y = 99;
    auto lambda = [x, &y]{ y = 100; };
    lambda(); // y is now 100
```

It's not possible to modify `x` in this case, as a lambda's `operator()` is `const` by default. However, this can be overridden by declaring it to be `mutable`:

```
    int x = 42;
    int y = 99;
    auto lambda = [x, &y]() mutable {
        x++, y++;
        printf("%d, %d\n", x, y);
    };
    lambda(); // prints 43, 100
    printf("%d, %d\n", x, y); // prints 42, 100
    lambda(); // prints 44, 101!
```

Because `x` is captured by value, changes made from within the lambda are not seen outside of it. There are essentially two copies of `x` at this point, and neither one affects the other.

It can be inconvenient to list every variable to be captured, so it is possible to specify a default capture behavior by putting either `=` or `&` within the `[]`. For example:

```
    int x = 42;
    int y = 99;
    auto lambda = [&] {
        x++, y++;
    };
    lambda(); // x, y are now 43, 100
```

It's even possible to combine the two, to have a default capture with exceptions:

```
    int x = 42;
    int y = 99;
    int z = 1001;
    auto lambda = [=, &z] {
        // can't modify x or y here, but we can read them
        z++;
        printf("%d, %d, %d\n", x, y, z);
    };
    lambda(); // prints 42, 99, 1002
    // z is now 1002
```

By allowing each lambda to specify how it captures things, the C++0x system allows more flexibility. With Objective-C blocks, a given variable is either `__block` or it's not. Every block which captures that variable must capture it in the same way. C++0x lambdas allow each lambda to make its own choice on how to capture. The `mutable` keyword even allows them to capture by value but retain the ability to change the copied value internally. The downside is considerably increased complexity.

**Memory Management**  
 Both Objective-C blocks and C++0x lambdas start their lives as stack objects. After that point, however, they diverge significantly.

Objective-C blocks are also Objective-C objects. Like all Objective-C objects, they are stored by reference, never by value. When a block literal is written, the block object is created on the stack, and the literal expression evaluates to the address of that block.

In order for a block to outlive its slot on the stack, it must be copied. Because the value is just a reference, simply assigning it with `=` is not enough:

```
    void (^block)(void);
    {
        block = ^{ printf("hello world"); };
    }
    block(); // bad!
```

Instead, it must be copied, either by using the Objective-C `copy` method, or the C `Block_copy` function:

```
    void (^block)(void);
    {
        block = ^{ printf("hello world"); };
        block = [block copy];
    }
    block(); // good!
```

Blocks follow standard Objective-C reference counting semantics. Each `copy` must be balanced with a `release` or `autorelease`, and each `Block_copy` must be balanced with a `Block_release`. The first copy gets the block onto the heap, subsequent ones simply increment the reference count. When the last live reference is released, the block is destroyed, and any captured objects or blocks are released.

C++0x lambdas are stored by value, not by reference. They can be copied onto the heap if needed, but the process is entirely manual. All captured variables are stored as member variables within the anonymous lambda object, so when the lambda is copied, those get copied as well, firing the appropriate constructors and destructors.

One extremely important aspect of this behavior is that variables which are captured by reference are stored as references within the lambda object. They get no special treatment in this respect. This means that a lambda which accesses one of those variables after the original enclosing scope has been destroyed is engaging in undefined behavior and will likely crash. Compare this to `__block` variables, where the storage is transparently moved to the heap and is guaranteed to live at least as long as the block does.

On the other hand, as long as nothing is captured by reference, a C++0x lambda can be returned without any extra work. The return will copy it and the copy will continue to function. With Objective-C blocks, they must be explicitly copied before returning, otherwise they become immediately invalid.

**Performance**  
 Objective-C blocks are objects which contain an embedded function pointer. A block call translates to a call to that function pointer, passing the block as an implicit parameter:

```
    block();
    // equivalent to:
    block->impl(block);
```

The cost of calling a block is therefore about the same as the cost of calling a C function. It's slightly higher due to the need to look up the implementation pointer first, but just slightly.

Opportunities for optimization are rare in most use cases. For example, this code calls a method to iterate over an array with a block:

```
    [array do: ^(id obj) {
        NSLog(@"Obj is %@", obj);
    }];
```

The implementation of `-do:` can't know anything about the block which is passed to it here, so it must perform the full dereference and call for each iteration of the loop.

The cases where blocks can be optimized are mostly cases where they're not needed in the first place, for example where they are defined and then called in the same scope. One place where useful optimizations could be made are inline functions which take block parameters, since the optimizer is able to improve the inlined code based on the calling code. However, as far as I know, no current blocks-capable compilers perform any of these optimizations, although I haven't investigated it thoroughly.

C++0x lambdas are objects with a `operator()`. There is no dynamic dispatch involved, so calling the lambda works out to be a simple function call, with no dereferencing ahead of time.

Because passing a lambda to another function involves templates, there are further opportunities for optimization. Consider this code to iterate over a vector:

```
    for_each(v.begin(), v.end(), [](int x) {
        printf("x is %d\n", x);
    });
```

`for_each` is a template function, which means that it gets specialized for this particular type. This makes it an excellent candidate for inlining, and it's likely that an optimizing compiler will end up generating code for the above which would be just as good as the equivalent for loop.

This is a typical tradeoff between C++ and Objective-C. C++ often favors the fastest possible generated code at the level of individual functions, sacrificing ease and speed of compilation and sometimes ease of programming to get it. Objective-C more often favors implementations which are simpler to create, compile, and use, at the cost of additional runtime overhead.

**Conclusion**  
 Objective-C blocks and C++0x lambdas are similar language features with similar goals but considerably different approaches. Objective-C blocks are somewhat simpler to write and to use, especially in the case of using them for asynchronous or background tasks where the block has to be copied and kept alive beyond the lifetime of the scope where it was created. C++0x lambdas ultimately provide more flexibility and potential speed, but at the cost of considerable added complexity. In comparing the two, I believe that Apple ultimately made the better set of tradeoffs, at least for the cases where I am likely to use blocks in my own programming.

That wraps things up for this week. Come back in another 14 days for the next baffling edition. As I say every time, Friday Q&A is driven by reader ideas. If you have a topic that you would like to see covered here, please [send it in](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2011-06-03-objective-c-blocks-vs-c0x-lambdas-fight.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
