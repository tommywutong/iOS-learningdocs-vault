---
title: 'Friday Q&A 2009-10-30: Generators in Objective-C'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-10-30-generators-in-objective-c.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1f260c8c670a7160'
translated: false
---

> 原文：[Friday Q&A 2009-10-30: Generators in Objective-C](https://www.mikeash.com/pyblog/friday-qa-2009-10-30-generators-in-objective-c.html)　·　mikeash.com Friday Q&A

Posted at 2009-10-30 16:59 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-11-06: Linking and Install Names](https://www.mikeash.com/pyblog/friday-qa-2009-11-06-linking-and-install-names.html)  
Previous article: [Friday Q&A 2009-10-23: A Preview of Coming Attractions](https://www.mikeash.com/pyblog/friday-qa-2009-10-23-a-preview-of-coming-attractions.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [generators](https://www.mikeash.com/pyblog/?tag=generators)

Friday Q&A 2009-10-30: Generators in Objective-C

by [Mike Ash](https://www.mikeash.com/)

**Generators**  
 A [generator](http://en.wikipedia.org/wiki/Generator_(computer_science)) is essentially a function which remembers its state between invocations. In a normal function, the second time you call it is just like the first. Execution starts over at the top, local variables reset their values, etc. With a generator, execution starts where it left off, and local variables remember their values.

In Python, a simple generator looks like this:

```
    def countfrom(n):
        while True:
            yield n
            n += 1
```

The `yield` statement takes the place of the `return` statement that you'd find in a normal function. When execution hits `yield`, the value is returned but the function's state is also saved. The net result is that successive calls return successively increasing numbers.

Things aren't actually quite this simple in Python. A call to `countfrom` doesn't start returning numbers, but rather returns an object. Calling the `next` method on the object it returns will return the successive numbers.

Using my [MAGenerator](http://www.mikeash.com/svn/MAGenerator/), things are much the same. The generator is considerably more wordy and uglier, but this should be so surprise considering that it's C, and that this is basically hacked on support rather than a language feature. The example counter generator using `MAGenerator` would look like this:

```
    GENERATOR(int, CountFrom(int start), (void))
    {
        __block int n;
        GENERATOR_BEGIN(void)
        {
            n = start;
            while(1)
            {
                GENERATOR_YIELD(n);
                n++;
            }
        }
        GENERATOR_END
    }
```

Much like in Python, calling `CountFrom` doesn't start returning numbers. Instead, it returns a block. Calling the block will then start returning numbers. Here's an example of how you'd actually use this generator:

```
    int (^counter)(void) = CountFrom(42);
    for(int i = 0; i < 10; i++)
        NSLog(@"%d", counter());
```

This will log 42, 43, 44, 45, 46, 47, 48, 49, 50, 51.

**Basic Implementation**  
 The basic concept behind how `MAGenerator` works was inspired by [Simon Tatham's Coroutines in C](http://www.chiark.greenend.org.uk/~sgtatham/coroutines.html). His coroutines are considerably more limited due to the fact that C without blocks can't really handle what's needed, but there's a great deal of cleverness in the implementation.

There are two major problems that need to be solved. The first problem is that of resuming execution where it left off. This is solved using a switch statement. The individual `case` labels give places to resume execution. In C, `case` labels can be put practically anywhere, even inside other control constructs, and the jump can be made and everything continues without any fuss.

The second problem is that of preserving state. Tatham solved this one by simply using `static` variables instead of locals. While this works, it has the severe limitation of only allowing one instance of the function to be active. Using blocks, we can work around this much more nicely by using variables captured from the enclosing scope. Thus, here is the basic idea of what our `CountFrom` function would look like if we implemented it directly instead of with the help of macros:

```
    // this crazy thing is how you declare a function that returns a block
    int (^CountFrom(int start))(void)
    {
        __block int state = 0;
        __block int n;
        int (^block)(void) = ^{
            switch(state)
            {
                case 0:
                    n = start;
                    while(1)
                    {
                        state = 1;
                        return n;
                case 1: ; // yes, this is legal!
                        n++;
                    }
            }
        };
        return [[block copy] autorelease];
    }
```

As you can see, the call to `CountFrom` returns a block, which captures the `start` parameter as well as the `state` and `n` local variables. Those are qualified with `__block` so that they can be mutated from within the block.

The `state` variable is where the magic happens. When you call the block, execution always begins at the top, just like with a function. However, the first thing it encounters is a switch statement. By setting the state variable to correspond to the location of the return statement, this switch statement causes execution to resume immediately after it. Since all of our variables are captured from the enclosing scope, they remember their contents across calls.

**Cleanup**  
 Let's consider a little string builder generator. This generator will take path components and build a complete path out of them. Here's a first stab at it:

```
    NSString *(^PathBuilder(void))(NSString *component)
    {
        __block int state = 0;
        __block NSString *path;
        NSString *(^block)(NSString *component) = ^{
            switch(state)
            {
                case 0:
                    path = @"/";
                    while(1)
                    {
                        path = [path stringByAppendingPathComponent: component];
                        state = 1;
                        return path;
                case 1: ;
                    }
            }
        };
        return [[block copy] autorelease];
    }
```

This works, but is dangerous. The danger comes because `__block` variables don't retain what they point to. Our `path` variable points to an un-owned string. If the caller happens to pop an autorelease pool in between calls to the path builder generator, that will destroy the string, leave a dangling pointer in `path`, and cause a crash at the next call.

We could fix this by copying the string, like so:

```
    NSString *(^PathBuilder(void))(NSString *component)
    {
        __block int state = 0;
        __block NSString *path;
        __block NSString *newPath;
        NSString *(^block)(NSString *component) = ^{
            switch(state)
            {
                case 0:
                    path = @"/";
                    while(1)
                    {
                        newPath = [path stringByAppendingPathComponent: component];
                        [path release];
                        path = [newPath copy];
                        state = 1;
                        return path;
                case 1: ;
                    }
            }
        };
        return [[block copy] autorelease];
    }
```

But this has a new problem, namely that it will leak the last string assigned to `path`.

The proper solution is to create a cleanup block which gets executed when the main block is destroyed. This can be accomplished by taking advantage of the fact that blocks _do_ automatically manage the memory of captured non-`__block` object pointer variables. We can create an object:

```
    NSString *(^PathBuilder(void))(NSString *component)
    {
        id cleanupObj = ...;
```

Reference it in a meaningless way so that it gets captured by the block:

```
        ...
        NSString *(^block)(NSString *component) = ^{
           [cleanupObj path];
           ...
```

And then have that object call the cleanup block when it's destroyed:

```
        [cleanupObj callBlockWhenDeallocated: ^{ ... }];
```

This could be done using a custom class, but for the sake of simplicity, I opted instead to use a `CFMutableArray` with custom callbacks set up so that the retain callback would copy the object, and the release callback would cast it to the appropriate block pointer, call it, and then release it. By adding the cleanup block to the array, it will be automatically invoked when the array (and the generator block) is destroyed.

If you assume that `MAGeneratorMakeCleanupArray` does the job of setting up the appropriate `CFMutableArray` (and casting it to an `NSMutableArray` then the final code, with cleanup, looks like this:

```
    NSString *(^PathBuilder(void))(NSString *component)
    {
        __block int state = 0;
        __block NSString *path;
        __block NSString *newPath;
        NSMutableArray *cleanupArray = MAGeneratorMakeCleanupArray();
        NSString *(^block)(NSString *component) = ^{
            [cleanupArray self]; // meaningless reference to capture it
            switch(state)
            {
                case 0:
                    path = @"/";
                    while(1)
                    {
                        newPath = [path stringByAppendingPathComponent: component];
                        [path release];
                        path = [newPath copy];
                        state = 1;
                        return path;
                case 1: ;
                    }
            }
        };
        [cleanupArray addObject: ^{ [path release]; }];
        return [[block copy] autorelease];
    }
```

Now everything works as expected.

**Macroization**  
 Much of the above, while workable, is tremendously annoying to write. To help, I turned all the boilerplate parts into macros.

To start with, the `GENERATOR` macro takes care of the function declaration as well as a variable to hold the cleanup block. It also declares a `GENERATOR_zeroReturnValue` variable, which is used to quiet compiler warnings about failing to return a value at the end of the block. Unfortunately, this trick means you can't use these macros to create a generator which returns `void`. However, since you can just declare another type (like `int`) and ignore the value in the caller, this is not a big problem. Here's what it looks like:

```
    #define GENERATOR(returnType, nameAndCreationParams, perCallParams) \
        returnType (^nameAndCreationParams) perCallParams \
        { \
            returnType GENERATOR_zeroReturnValue; \
            bzero(&GENERATOR;_zeroReturnValue, sizeof(GENERATOR_zeroReturnValue)); \
            returnType (^GENERATOR_cleanupBlock)(void) = nil;
```

Local variables can be declared immediately after `GENERATOR`.

The `GENERATOR_DECL` works the same as the `GENERATOR` macro, but only produces the prototype, making it suitable for a declaration in a header file.

```
    #define GENERATOR_DECL(returnType, nameAndCreationParams, perCallParams) \
        returnType (^nameAndCreationParams) perCallParams
```

Next comes `GENERATOR_BEGIN`, which takes the generator's parameters again. This declares the state variable (called `GENERATOR_where`, the cleanup array, and starts off the block:

```
    #define GENERATOR_BEGIN(...) \
        __block int GENERATOR_where = -1; \
        NSMutableArray *GENERATOR_cleanupArray = MAGeneratorMakeCleanupArray(); \
        id GENERATOR_mainBlock = ^ (__VA_ARGS__) { \
            [GENERATOR_cleanupArray self]; \
            switch(GENERATOR_where) \
            { \
                case -1:
```

The generator code can follow this macro. Within the generator code, you want to return values, so you do this using the `GENERATOR_YIELD` macro. This macro does exactly the same thing as the sequence we wrote manually above. The one trick here is that we need a unique number to identify the state value for this yield. Previously we could just write 1, 2, 3, 4, etc. in the code. We could make this macro take another parameter for the state value, but it's annoying to have to keep track of them all. Instead, as Tatham did, I chose to use the `__LINE__` macro, which gets replaced by the line number of the current line of code.

```
    #define GENERATOR_YIELD(...) \
                        do { \
                            GENERATOR_where = __LINE__; \
                            return __VA_ARGS__; \
                    case __LINE__: ; \
                        } while(0)
```

This works great, with one caveat, that you must never place two `GENERATOR_YIELD`s on the same line.

Next we want the ability to define a cleanup block, which we'll do with a `GENERATOR_CLEANUP` macro. This macro gets a little funky, because the macros are designed to work whether `GENERATOR_CLEANUP` is present or not. `GENERATOR_END`, which will end the definition of the generator, needs to work properly whether it follows `GENERATOR_CLEANUP` or `GENERATOR_BEGIN`. This is done in this macro by adding a superfluous set of curly braces to the cleanup block:

```
    #define GENERATOR_CLEANUP \
                } \
                GENERATOR_where = -1; \
                return GENERATOR_zeroReturnValue; \
            }; \
            GENERATOR_cleanupBlock = ^{{
```

The return statement shuts up the compiler about missing return statements, and also provides a safety net if you let execution fall off the end. Finally we come to the end. Again, this macro has to work whether `GENERATOR_CLEANUP` is present or not. Thus, it has the same ending with the return statement, which works in both contexts. Finally it checks to see if a cleanup block has been set, adds it to the cleanup array if so, and then returns the newly created generator block.

```
    #define GENERATOR_END \
                } \
                GENERATOR_where = -1; \
                return GENERATOR_zeroReturnValue; \
            }; \
            if(GENERATOR_cleanupBlock) \
                [GENERATOR_cleanupArray addObject: ^{ GENERATOR_cleanupBlock(); }]; \
            return [[GENERATOR_mainBlock copy] autorelease]; \
        }
```

Note that in order to accommodate the `return GENERATOR_zeroReturnValue;` statement in the cleanup block, the cleanup block needs to have the same return type as the generator block. Since the array has no way to figure out the proper block type to invoke, we wrap the cleanup block in a nice `void`/`void` block that it can deal with.

**Results**  
 These macros are pretty scary, but the results are quite nice. This is the same example that I showed at the beginning:

```
    GENERATOR(int, CountFrom(int start), (void))
    {
        __block int n;
        GENERATOR_BEGIN(void)
        {
            n = start;
            while(1)
            {
                GENERATOR_YIELD(n);
                n++;
            }
        }
        GENERATOR_END
    }
```

More complicated generators look nice too. Here's the `PathBuilder` generator that I used as an example above without the macros, put in macro form:

```
    GENERATOR(NSString *, PathBuilder(void), (NSString *component))
    {
        __block NSString *path;
        __block NSString *newPath;
        GENERATOR_BEGIN(NSString *component)
        {
            path = @"/";
            while(1)
            {
                newPath = [path stringByAppendingPathComponent: component];
                [path release];
                path = [newPath copy];
                GENERATOR_YIELD(path);
            }
        }
        GENERATOR_CLEANUP
        {
            [path release];
        }
        GENERATOR_END
    }
```

Certainly this is not 100% natural, but all in all it's amazingly reasonable and readable considering that the language has no support for this sort of thing.

**Caveats**  
 As with all blasphemous crimes against nature, MAGenerator has a few caveats.

1. **Local variables must be declared at the top, before `GENERATOR_BEGIN`.** Local variables declared within the generator block will not remember their state between invocation. You can get away with this with carefully structured code, but it's best not to try.
2. **This includes the implicit locals generated by using a `for`/`in` loop.** You cannot safely use `for`/`in` loops (other loop constructs are fine) unless the body contains no invocations of `GENERATOR_YIELD`.
3. **You can't put two invocations of `GENERATOR_YIELD` on the same line.** This is not a big hardship: just separate them with a carriage return. Thankfully, this one will generate a compiler error, not a difficult runtime error.
4. **`switch` statements used within the generator must not contain any invocations of `GENERATOR_YIELD`.** Because the generator's execution state is resumed using a `switch` statement, and because `GENERATOR_YIELD` creates `case` labels, using `GENERATOR_YIELD` inside your own `switch` statement will cause confusion, because the generated case labels will belong to the inner `switch` rather than the macro-generated execution dispatch one.
5. **Object lifetime must be managed carefully if it croses `GENERATOR_YIELD`.** You can't assume that the caller will keep an autorelease pool around for you until you're done. `GENERATOR_CLEANUP` takes care of this, but it's still harder than it is in normal code.

These are all unfortunate, and I wish they weren't there, but all in all they aren't dealbreakers by any stretch of the imagination.

**Potential Uses**  
 I'm fairly new to the world of generators, and of course everybody is new to the world of generators in Objective-C, but I have some ideas of how they could be productively used.

**Lazy Evaluation**  
 A major use of generations in Python is to lazily evaluate enumerated values. The generator creates new values on demand rather than requiring them all to be precomputed. MAGenerator includes a convenience function, `MAGeneratorEnumerator`, which takes a generator with no per-call parameters and an `id` return type, and returns an object conforming to `NSFastEnumeration` which enumerates by successively calling the generator.

As an example, here's a generator which will find files with a certain extension in a certain path:

```
    GENERATOR(id, FileFinder(NSString *path, NSString *extension), (void))
    {
        NSDirectoryEnumerator *enumerator = [[NSFileManager defaultManager] enumeratorAtPath: path];
        __block NSString *subpath;
        GENERATOR_BEGIN(void)
        {
            while((subpath = [enumerator nextObject]))
            {
                if([[subpath pathExtension] isEqualToString: extension])
                    GENERATOR_YIELD((id)[path stringByAppendingPathComponent: subpath]);
            }
        }
        GENERATOR_END
    }
```

You could just write a function that returns an array, but that requires enumerating over the entire contents of the directory, which is slow if the caller doesn't actually need them all. You could write an `NSEnumerator` subclass which wraps the `NSDirectoryEnumerator`, but that requires a lot more code. You could write code which takes a block as a parameter and invokes it for each one it finds, but that's less natural. Here's what it looks like to use this generator:

```
    for(NSString *path in MAGeneratorEnumerator(FileFinder(@"/Applications", @"app")))
        NSLog(@"%@", path);
```

It doesn't get any easier than that.

**Replacing State Machines**  
 Code frequently requires state machines. Imagine something like a network protocol parser. The natural way to write this is to write code that flows from top to bottom. Read a character, act on it. Read the next character, act on it. Have loops for reading strings, read individual characters to skip over separators, etc.

Then asynchronous programming appears and suddenly this doesn't seem like a good idea. Every one of those read calls could block. You could put it in a separate thread, but that has its own problems. You look into doing callback-based networking, using `NSStream` or GCD, but suddenly you have to deal with buffers, keep around a bunch of explicit state about where you are in the protocol parsing, etc.

By virtue of their inside-out approach to programming, generators allow you to invert the flow of control while preserving the nice linear code that you get from the synchronous approach.

As an example, consider a very simple RLE decoder, which reads pairs of `{ count, value }` bytes. Normally the decoder, if asynchronous, would have to keep track of what state it's in so that it knows whether the next byte it receives is a count or a value. However, using a generator, that state information disappears, replaced with the implicit generator state:

```
    GENERATOR(int, RLEDecoder(void (^emit)(char)), (unsigned char byte))
    {
        __block unsigned char count;
        GENERATOR_BEGIN(unsigned char byte)
        {
            while(1)
            {
                count = byte;
                GENERATOR_YIELD(0);
                
                while(count--)
                    emit(byte);
                GENERATOR_YIELD(0);
            }
        }
        GENERATOR_END
    }
```

This code is more straightforward and easier to understand than a non-generator asynchronous version would be.

For a much more complicated example, here's an HTTP response parser written as a generator. It takes several blocks as parameters to use as callbacks for when it finishes parsing the various components of the response.

```
    GENERATOR(int, HTTPParser(void (^responseCallback)(NSString *),
                              void (^headerCallback)(NSDictionary *),
                              void (^bodyCallback)(NSData *),
                              void (^errorCallback)(NSString *)),
                              (int byte))
    {
        NSMutableData *responseData = [NSMutableData data];
        
        NSMutableDictionary *headers = [NSMutableDictionary dictionary];
        __block NSMutableData *currentHeaderData = nil;
        __block NSString *currentHeaderKey = nil;
        
        NSMutableData *bodyData = [NSMutableData data];
        
        GENERATOR_BEGIN(char byte)
        {
            // read response line
            while(byte != '\r')
            {
                AppendByte(responseData, byte);
                GENERATOR_YIELD(0);
            }
            responseCallback(SafeUTF8String(responseData));
            GENERATOR_YIELD(0); // eat the \r
            if(byte != '\n')
                errorCallback(@"bad CRLF after response line");
            GENERATOR_YIELD(0); // eat the \n
            
            // read headers
            while(1)
            {
                currentHeaderData = [[NSMutableData alloc] init];
                while(byte != ':' && byte != '\r')
                {
                    AppendByte(currentHeaderData, byte);
                    GENERATOR_YIELD(0);
                }
                
                // empty line means we're done with headers
                if(byte == '\r' && [currentHeaderData length] == 0)
                    break;
                else if(byte == '\r')
                    errorCallback(@"No colon found in header line");
                else
                {
                    GENERATOR_YIELD(0);
                    if(byte == ' ')
                        GENERATOR_YIELD(0);
                    
                    currentHeaderKey = [SafeUTF8String(currentHeaderData) copy];
                    [currentHeaderData release];
                    
                    currentHeaderData = [[NSMutableData alloc] init];
                    while(byte != '\r')
                    {
                        AppendByte(currentHeaderData, byte);
                        GENERATOR_YIELD(0);
                    }
                    
                    NSString *currentHeaderValue = SafeUTF8String(currentHeaderData);
                    [currentHeaderData release];
                    
                    [headers setObject: currentHeaderValue forKey: currentHeaderKey];
                    [currentHeaderKey release];
                }
                GENERATOR_YIELD(0);
                if(byte != '\n')
                    errorCallback(@"bad CRLF after header line");
                GENERATOR_YIELD(0); // eat the \n
            }
            headerCallback(headers);
            
            // read body
            while(byte != -1)
            {
                AppendByte(bodyData, byte);
                GENERATOR_YIELD(0);
            }
            bodyCallback(bodyData);
        }
        GENERATOR_CLEANUP
        {
            [currentHeaderData release];
            [currentHeaderKey release];
        }
        GENERATOR_END
    }
```

To use it, code would simply create a new parser like so:

```
    int (^httpParser)(int) = HTTPParser( /* callbacks go here */ );
```

It would then store this object somewhere. Whenever new data became available from the remote end, it would just call it:

```
    httpParser(newByte);
```

When the connection is closed, it signals the end of the stream:

```
    httpParser(-1);
```

And everything else just happens automatically. Any time `newByte` provides enough information for the parser to have parsed a new component of the response, the appropriate callback block is invoked.

This generator is declared to return `int` since MAGenerator doesn't support `void` generators. The return value is simply ignored in this case. Execution begins at the top, with the first character from the data stream stored in `byte`. Each time it invokes `GENERATOR_YIELD`, the effect is to get a new `byte` from the caller. Parsing thus flows naturally from top to bottom, even though this code is in fact heavily asynchronous.

It should be noted that these parsers are not very efficient, because they require a block call (a function call plus additional overhead) for every single byte. This could be easily remedied if necessary, however. Modify the generator to take a buffer instead of a single byte. Then, instead of blind invocation of `GENERATOR_YIELD`, the code would advance a cursor in the buffer, and only invoke `GENERATOR_YIELD` when the buffer is empty and needs to be refilled. This would get you down to one call per buffer instead of one per byte.

**Wrapping Up**  
 Now you know how to build generators in Objective-C using blocks, and have at least some ideas of how to use them productively. Of course you shouldn't be building them manually, but rather you should use my MAGenerator library! MAGenerator is open source. You can get the source by checking it out from my subversion repository:

```
    svn co http://www.mikeash.com/svn/MAGenerator/
```

Or browse it by just clicking on the URL above. It's available under the MIT license, so you can use it in pretty much any project you like. The project includes everything needed to write generators, as well as a bunch of examples/test cases.

I'm sure there are improvements that could be made, and patches are welcome. Depending on the change you're making I can't guarantee that I'll accept it, but of course you're always welcome to fork it if I don't.

That's it for this week. It looks like this is my longest Friday Q&A to date, so I hope it makes up for just getting a code dump last week. Come back week for another frightening edition. As always (except this week) Friday Q&A is driven by your submissions. If you have a topic that you would like to see covered here, [send it in!](mailto:mike@mikeash.com)

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-10-30-generators-in-objective-c.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
