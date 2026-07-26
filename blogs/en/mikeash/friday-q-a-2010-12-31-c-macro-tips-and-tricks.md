---
title: 'Friday Q&A 2010-12-31: C Macro Tips and Tricks'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-12-31-c-macro-tips-and-tricks.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4aff6eb70d1a7fb5'
translated: false
---

> 原文：[Friday Q&A 2010-12-31: C Macro Tips and Tricks](https://www.mikeash.com/pyblog/friday-qa-2010-12-31-c-macro-tips-and-tricks.html)　·　mikeash.com Friday Q&A

Posted at 2010-12-31 22:43 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Rogue Amoeba Is Hiring Again](https://www.mikeash.com/pyblog/rogue-amoeba-is-hiring-again.html)  
Previous article: [Friday Q&A 2010-12-17: Custom Object Allocators in Objective-C](https://www.mikeash.com/pyblog/friday-qa-2010-12-17-custom-object-allocators-in-objective-c.html)  
Tags: [c](https://www.mikeash.com/pyblog/?tag=c) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [macros](https://www.mikeash.com/pyblog/?tag=macros)

Friday Q&A 2010-12-31: C Macro Tips and Tricks

by [Mike Ash](https://www.mikeash.com/)

**Preprocessor vs Compiler**  
 To properly understand C macros, you must understand how a C program is compiled. In particular, you must understand the different things that happen in the preprocessor and in the compiler.

The preprocessor runs first, as the name implies. It performs some simple textual manipulations, such as:

- Stripping comments.
- Resolving `#include` directives and replacing them with the contents of the included file.
- Evaluating `#if` and `#ifdef` directives.
- Evaluating `#define`s.
- Expading the macros found in the rest of the code according to those `#define`s.

It is, of course, these last two which are most relevant to today's discussion.

Note that the preprocessor largely has no understanding of the text that it processes. There are some exceptions to this. For example, it knows that this is a string, and so does not expand the macro inside it:

```
    #define SOMETHING hello
    
    char *str = "SOMETHING, world!" // nope
```

And it can count parentheses, so it knows that this comma does not result in two arguments to the macro:

```
    #define ONEARG(x) NSLog x
    
    ONEARG((@"hello, %@", @"world"));
```

But in general, it does not have any concept of what it processes. For example, you can't use `#if` to check whether a type is defined or not:

```
    // makes no sense
    #ifndef MyInteger
    typedef int MyInteger
    #endif
```

The `#ifndef` always comes out true even if the `MyInteger` type is already defined. Type definitions are evaluated as part of the compilation phase, which hasn't even happened yet.

Likewise, there is no need for the contents of a `#define` to be syntactically correct on their own. It is completely legal, although a poor idea, to create macros like this:

```
    #define STARTLOG NSLog(@
    #define ENDLOG , @"testing");
    STARTLOG "just %@" ENDLOG
```

The preprocessor just blindly replaces `STARTLOG` and `ENDLOG` with their definitions. By the time the compiler comes along to try to make sense of this code, it actually _does_ make sense, and so it compiles as valid code.

**A Word of Warning**  
 C macros are at the same time too powerful and not powerful enough. Their somewhat ad-hoc nature makes them dangerous, so treat them with care.

The C preprocessor is [nearly Turing-complete](http://www.ioccc.org/2001/herrmann1.hint). With a simple driver, you can compute any computable function using the preprocessor. However, the contortions required to do this are so bizarre and difficult that they make Turing-complete C++ templates look simple by comparison.

While powerful, they are also very simple. Since macro expansion is a simple textual process, there are pitfalls. For example, operator precedence can be dangerous:

```
    #define ADD(x, y) x+y
    
    // produces 14, not 20
    ADD(2, 3) * 4;
    
    #define MULT(x, y) x*y
    
    // produces 14, not 20
    MULT(2 + 3, 4);
```

Be very careful to parenthesize everything that could possibly need it, considering both any possible arguments passed to the macro, and any possible context that the macro could be used in.

Evaluating a macro argument multiple times can also lead to unexpected results:

```
    #define MAX(x, y) ((x) > (y) ? (x) : (y))
    
    int a = 0;
    int b = 1;
    int c = MAX(a++, b++);
    // now a = 1, c = 1, and b = 3!
    // (a++ > b++ ? a++ : b++)
    // b++ gets evaluated twice
```

The syntax for using a parameterized macro looks just like the the syntax for calling a function, but don't be fooled. Macros require a great deal of care.

**Macro Debugging**  
 Macros are code, and like any code, they will have bugs. Macro bugs tend to manifest as weird compiler errors at the site where the macro is used. This can be incredibly confusing.

To reduce confusion, you'll want to look at the file as it appears after preprocessing. This means all of your macros are expanded, and you can see the raw C code that the compiler sees, rather than trying to expand the macro in your head. In Xcode you can do this by selecting Build-\>Preprocess. The resulting file will generally be very large due to all of the `#include` directives, but you'll find your code near the end. Find the site where the macro is used, figure out how the code has gone wrong, then modify your macro to make it right.

**Multi-Statement Macros**  
 It's common to write a macro that consists of multiple statements. For example, a timing macro:

```
    #define TIME(name, lastTimeVariable) NSTimeInterval now = [[NSProcessInfo processInfo] systemUptime]; if(lastTimeVariable) NSLog(@"%s: %f seconds", name, now - lastTimeVariable); lastTimeVariable = now
```

You would use this macro in some frequently called method to measure just how frequently it's called:

```
    - (void)calledALot
    {
        // do some work
        
        // time it
        TIME("calledALot", _calledALotLastTimeIvar);
    }
```

This definition works well enough here, but it's unbelievably ugly sitting all on one line like this. Let's split it up onto multiple lines. Normally a `#define` is terminated at the end of the line, but by putting `\` at the end of the line, you can make the preprocessor continue the definition on the next line:

```
    #define TIME(name, lastTimeVariable) \
        NSTimeInterval now = [[NSProcessInfo processInfo] systemUptime]; \
        if(lastTimeVariable) \
            NSLog(@"%s: %f seconds", name, now - lastTimeVariable); \
        lastTimeVariable = now
```

This is easier to work with. However, the macro is flawed. Consider this use:

```
    - (void)calledALot
    {
        if(...) // only time some calls
            TIME("calledALot", _calledALotLastTimeIvar);
    }
```

The macro will expand like this:

```
    - (void)calledALot
    {
        if(...) // only time some calls
            NSTimeInterval now = [[NSProcessInfo processInfo] systemUptime];
        if(_calledALotLastTimeIvar)
            NSLog(@"%s: %f seconds", name, now - _calledALotLastTimeIvar);
        _calledALotLastTimeIvar = now;
    }
```

This won't compile. Declaring `NSTimeInterval now` in the `if` statement is illegal. Even if that worked, only the first statement is subject to the `if`, and the following lines would run regardless. Not what we wanted!

This can be solved by putting brackets around the macro definition:

```
    #define TIME(name, lastTimeVariable) \
    { \
        NSTimeInterval now = [[NSProcessInfo processInfo] systemUptime]; \
        if(_calledALotLastTimeIvar) \
            NSLog(@"%s: %f seconds", name, now - _calledALotLastTimeIvar); \
        _calledALotLastTimeIvar = now; \
    }
```

Now the expansion looks like this:

```
    - (void)calledALot
    {
        if(...) // only time some calls
        {
            NSTimeInterval now = [[NSProcessInfo processInfo] systemUptime];
            if(lastTimeVariable)
                NSLog(@"%s: %f seconds", name, now - lastTimeVariable);
            lastTimeVariable = now;
        };
    }
```

Pretty good, except for that surplus semicolon at the end. Not a problem, though... right?

In fact, this is a problem. Consider this code:

```
    - (void)calledALot
    {
        if(...) // only time some calls
            TIME("calledALot", _calledALotLastTimeIvar);
        else // otherwise do something else
            // stuff
    }
```

The expansion then looks like this:

```
    - (void)calledALot
    {
        if(...) // only time some calls
        {
            NSTimeInterval now = [[NSProcessInfo processInfo] systemUptime];
            if(_calledALotLastTimeIvar)
                NSLog(@"%s: %f seconds", name, now - _calledALotLastTimeIvar);
            _calledALotLastTimeIvar = now;
        };
        else // otherwise do something else
            // stuff
    }
```

That semicolon now causes a syntax error. Whoops.

You could work around this by requiring the user of the macro not to put a semicolon at the end. However, this is highly unnatural and tends to mess with things like automatic code indenting.

A better way to fix it is to wrap the function in a `do ... while(0)` construct. This construct requires a semicolon at the end, which is exactly what we want. Using `while(0)` ensures that the loop never really loops, and its contents are only executed once.

```
    #define TIME(name, lastTimeVariable) \
        do { \
            NSTimeInterval now = [[NSProcessInfo processInfo] systemUptime]; \
            if(lastTimeVariable) \
                NSLog(@"%s: %f seconds", name, now - lastTimeVariable); \
            lastTimeVariable = now; \
        } while(0)
```

This works correctly with the `if` statement and in all other situations. A multi-statement macro should always be wrapped in `do ... while(0)` for this reason.

This macro defines a variable called `now`. This is a poor choice of names for a macro variable, because it could conflict with a variable from outside. Imagine the following code, with somewhat poor variable naming:

```
    NSTimeInterval now; // ivar
    
    TIME("whatever", now);
```

This will not work as expected. Debugging it will not be easy, because the failure is subtle. It's best to avoid it up-front, even if it looks unlikely.

Unfortunately, C does not have a good way to generate unique variable names for this use. The best thing to do is to add a prefix, like you do with Objective-C class names:

```
    #define TIME(name, lastTimeVariable) \
        do { \
            NSTimeInterval MA_now = [[NSProcessInfo processInfo] systemUptime]; \
            if(lastTimeVariable) \
                NSLog(@"%s: %f seconds", name, MA_now - lastTimeVariable); \
            lastTimeVariable = MA_now; \
        } while(0)
```

This macro is now safe against accidental conflicts, and is good to go.

**String Concatenation**  
 This feature is not strictly part of macros, but it's useful for building macros, so it deserves mention. It's a little-known feature of C that if you put two string literals next to each other in the source code, they get concatenated:

```
    char *helloworld = "hello, " "world!";
    // equivalent to "hello, world!"
```

It works for Objective-C strings too:

```
    NSString *helloworld = @"hello, " @"world!";
```

Even better, if you take an Objective-C string and follow it with a C string, it still works, and produces an Objective-C string result:

```
    NSString *helloworld = @"hello, " "world!";
```

You can use this to combine a macro parameter with a constant string within the macro definition:

```
    #define COM_URL(domain) [NSURL URLWithString: @"http://www." domain ".com"];
```

```
    COM_URL("google"); // gives http://www.google.com
    COM_URL("apple"); // gives http://www.apple.com
```

**Stringification**  
 By placing a `#` in front of a parameter name, the preprocessor will turn the contents of that parameter into a C string. For example:

```
    #define TEST(condition) \
        do { \
            if(!(condition)) \
                NSLog(@"Failed test: %s", #condition); \
        } while(0)
    
    TEST(1 == 2);
    // logs: Failed test: 1 == 2
```

However, you have to be careful with this. If the parameter contains a macro, it will _not_ be expanded. For example:

```
    #define WITHIN(x, y, delta) (fabs((x) - (y)) < delta)
    
    TEST(WITHIN(1.1, 1.2, 0.05));
    // logs: Failed test: WITHIN(1.1, 1.2, 0.05)
```

Sometimes this is desirable, but sometimes it's not. To avoid it, you can add an extra level of indirection:

```
    #define STRINGIFY(x) #x
    
    #define TEST(condition) \
        do { \
            if(!(condition)) \
                NSLog(@"Failed test: %s", STRINGIFY(condition)); \
        } while(0)
    
    TEST(WITHIN(1.1, 1.2, 0.05));
    // logs: Failed test: (fabs(1.1 - 1.2) < 0.05)
```

For this particular case, the desired behavior is pretty much a matter of opinion. In other cases, it may be obvious that you only want one or the other.

**Token Pasting**  
 The preprocessor provides a `##` operator to concatenate tokens together. This allows you to build multiple related items in a macro to eliminate redundancy. Writing `a ## b` produces the single token `ab`. If `a` or `b` is a macro parameter, its content will be used instead. A useless example:

```
    #define NSify(x) NS ## x
    
    NSify(String) *s; // gives NSString
```

For example, you might use this to generate method combinations. This macro will automatically generate indexed accessors for key-value compliance for a property backed by an `NSMutableArray`:

```
    #define ARRAY_ACCESSORS(capsname, lowername) \
        - (NSUInteger)countOf ## capsname { \
            return [lowername count]; \
        } \
        \
        - (id)objectIn ## capsname ## AtIndex: (NSUInteger)index { \
            return [lowername objectAtIndex: index]; \
        } \
        \
        - (void)insertObject: (id)obj in ## capsname ## AtIndex: (NSUInteger)index { \
            [lowername insertObject: obj atIndex: index]; \
        } \
        \
        - (void)removeObjectFrom ## capsname ## AtIndex: (NSUInteger)index { \
            [lowername removeObjectAtIndex: index]; \
        }
```

You could then use it like this:

```
    // instance variable
    NSMutableArray *thingies;
    
    // in @implementation
    ARRAY_ACCESSORS(Thingies, thingies)
```

Notice how the macro takes two parameters which are nearly identical. This is because it's convential to name the instance variable using all lowercase, but the method names require the key name to begin with a capital letter. In order to be able to refer to both cases, the macro has to take them both as parameters. (Unfortunately, there is no C preprocessor operator that will capitalize or lowercase a token!)

Like the stringify operator, the concatenation operator won't evaluate macros passed to it without an extra level of indirection:

```
    #define ARRAY_NAME thingies
    #define ARRAY_NAME_CAPS Thingies
    
    // incorrectly creates accessors for "ARRAY_NAME_CAPS"
    ARRAY_ACCESSORS(ARRAY_NAME_CAPS, ARRAY_NAME)
    
    #define CONCAT(x, y) x ## y
    
    // define ARRAY_ACCESSORS using CONCAT, and the above works
```

And as with stringify, which behavior is most desirable will depend on the individual situation.

**Variable Argument Lists**  
 Imagine that you want to write a logging macro that only logs if a variable is set:

```
    #define LOG(string) \
        do { \
            if(gLoggingEnabled) \
                NSLog(@"Conditional log: %s", string); \
        } while(0)
```

You can call it like this:

```
    LOG("hello");
```

If logging is enabled, then it will print output like this:

```
    Conditional log: hello
```

This is handy, but it could be handier. `NSLog` takes a format string and variable arguments. It would be really useful if `LOG` could do the same:

```
    LOG("count: %d  name: %s", count, name);
```

With the original definition of the macro, this will produce an error. The macro only takes one argument, you're providing three, and that's not allowed.

If you place the magic `...` parameter at the end of the macro's parameter list, the macro will accept a variable number of arguments. If you then use the magic `__VA_ARGS__` identifier in the macro body, that will be replaced by all of the variable arguments, commas and all. Thus the `LOG` macro can be made to accept variable arguments like this:

```
    #define LOG(...) \
        do { \
            if(gLoggingEnabled) \
                NSLog(@"Conditional log: " __VA_ARGS__); \
        } while(0)
```

While this works well, it can be useful to have fixed arguments before the variable part. For example, you might want to place some boilerplate text after the custom logging as well as before:

```
    #define LOG(fmt, ...) \
        do { \
            if(gLoggingEnabled) \
                NSLog(@"Conditional log: --- " fmt " ---", __VA_ARGS__); \
        } while(0)
```

This works well, except for one problem: you can't provide just a string for simple logs. If you do something like `LOG("hello")`, the `NSLog` line expands to:

```
    NSLog(@"Conditional log: --- " "hello" " ---", );
```

That trailing comma is a syntax error.

To avoid this problem in a completely portable way, you have to go back to taking one parameter, and do fancier tricks. For example, you might construct the user-provided string separately, then combine it into the log:

```
    NSString *MA_logString = [NSString stringWithFormat: __VA_ARGS__]; \
    NSLog(@"Conditional log: --- %@ ---", MA_logString);
```

This works, but it ugly and a bit less efficient. Fortunately, gcc provides an extension which allows the more natural definition. By placing the magic `##` operator between the trailing comma and `__VA_ARGS__`, the preprocessor will eliminate the trailing comma in the case that no variable arguments are provided:

```
    #define LOG(fmt, ...) \
        do { \
            if(gLoggingEnabled) \
                NSLog(@"Conditional log: --- " fmt " ---", ## __VA_ARGS__); \
        } while(0)
```

This works just as we'd expect, both with extra arguments and without. (Naturally, this extension is also supported in Clang.)

**Magic Identifiers**  
 C provides several built-in identifiers which can be extremely useful when building macros:

- `__LINE__`: a built-in macro that expands to the current line number.
- `__FILE__`: another built-in macro that expands to a string literal containing the name of the current source file.
- `__func__`: this is an implicit variable which contains the name of the current function as a C string.

Note that when used in a macro definition, these will all refer to the place where your macro is _used_, not where it is defined, which is really useful.

As an example, consider this logging macro:

```
    #define LOG(fmt, ...) NSLog(fmt, ## __VA_ARGS__)
```

This is not too exciting. Let's use these built-in identifiers to make it more interesting:

```
    #define LOG(fmt, ...) NSLog(@"%s:%d (%s): " fmt, __FILE__, __LINE__, __func__, ## __VA_ARGS__)
```

This is much more interesting. You can write a log like this:

```
    LOG("something happened");
```

The output will look like this:

```
    MyFile.m:42 (MyFunction): something happened
```

This is an extremely valuable debugging aid. You can sprinkle `LOG` statements throughout your code and the log output will automatically contain the file name, line number, and function name of where each log statement was placed.

**Compound Literals**  
 This is another item that's not really part of macros, but is really useful for building macros. Compound literals are a new feature in C99. They allow you to to create literals (that is, a constant expression of a given value, like `42` or `"hello"`) of any type, not just built-in types.

The syntax for compound literals is a bit odd, but not hard. It looks like this:

```
    (type){ initializer }
```

As an example, these are equivalent:

```
    // regular variable and initializer
    NSPoint p = { 1, 100 };
    DoSomething(p);
    
    // compound literal
    DoSomething((NSPoint){ 1, 100 });
```

As a more useful example, you can create an array inline in code:

```
    NSArray *array = [NSArray arrayWithObjects: (id []){ @"one", @"two", @"three" } count: 3];
```

This is useful enough to make a macro out of:

```
    #define ARRAY(num, ...) [NSArray arrayWithObjects: (id []){ __VA_ARGS__ } count: num]
```

Then we can use it like this:

```
    NSArray *array = ARRAY(3, @"one", @"two", @"three");
```

Of course, having to manually enter the number of items is annoying. It would be better to avoid that. The good news is that this is pretty easy to do.

As you probably know, the `sizeof` operator gives you the size of a particular object or type in bytes. When given an array, it reports the size of the entire array. By dividing this size by the size of a single element, you get the number of elements in the array:

```
    #define ARRAY(...) [NSArray
                         arrayWithObjects: (id []){ __VA_ARGS__ }
                         count: sizeof((id []){ __VA_ARGS__ }) / sizeof(id)]
```

We can then use this as you'd expect:

```
    NSArray *array = ARRAY(@"one", @"two", @"three");
```

This is good, but could use some refinement. The macro definition is wordy and redundant. Better to factor out the common pieces:

```
    #define IDARRAY(...) (id []){ __VA_ARGS__ }
    #define IDCOUNT(...) (sizeof(IDARRAY(__VA_ARGS__)) / sizeof(id))
    
    #define ARRAY(...) [NSArray arrayWithObjects: IDARRAY(__VA_ARGS__) count: IDCOUNT(__VA_ARGS__)]
```

These macros are nice, short, easy to use, and almost comprehensible.

Let's make a similar one for dictionaries. `NSDictionary` doesn't have a method that exactly corresponds to what I want, so I'll make this macro call a small helper fuction that does some more work:

```
    #define DICT(...) DictionaryWithIDArray(IDARRAY(__VA_ARGS__), IDCOUNT(__VA_ARGS__) / 2)
```

The helper function unpacks the object array and then calls through to `NSDictionary` to create the dictionary:

```
    NSDictionary *DictionaryWithIDArray(id *array, NSUInteger count)
    {
        id keys[count];
        id objs[count];
        
        for(NSUInteger i = 0; i < count; i++)
        {
            keys[i] = array[i * 2];
            objs[i] = array[i * 2 + 1];
        }
        
        return [NSDictionary dictionaryWithObjects: objs forKeys: keys count: count];
    }
```

Now you can write:

```
    NSDictionary *d = DICT(@"key", @"value", @"key2", @"value2");
```

**`typeof`**  
 This is a `gcc` extension, not part of standard C, but it's extremely useful. It works like `sizeof`, except instead of providing the size, it provides the type. If you give it an expression, it evaluates to the type of that expression. If you give it a type, it just regurgitates that type.

Note that for maximum compatibility, it's best to write it as `__typeof__`. The plain `typeof` keyword is disabled in some `gcc` modes to avoid conflicts.

Let's take a look at that faulty `MAX` macro from the beginning of this article:

```
    #define MAX(x, y) ((x) > (y) ? (x) : (y))
```

As you'll recall, this is faulty because it evaluates one of its parameters twice. We can try to fix this, using some local variables, and a block to contain them:

```
    #define MAX(x, y) (^{ \
        int my_localx = (x); \
        int my_localy = (y); \
        return my_localx > my_localy ? (my_localx) : (my_localy); \
    }())
```

This works, sort of. The trouble is that by hard-coding `int`, the macro doesn't work correctly for `float`, `long long`, or other types that don't quite fit.

Using `__typeof__`, this macro can be built to be completely generic:

```
    #define MAX(x, y) (^{ \
        __typeof__(x) my_localx = (x); \
        __typeof__(y) my_localy = (y); \
        return my_localx > my_localy ? (my_localx) : (my_localy); \
    }())
```

This version behaves as expected. Note that because `__typeof__` is a purely compile-time construct, the extra use of the macro parameters does _not_ cause them to be evaluated twice. You can use a similar trick to create a pointer to any value you want:

```
    #define POINTERIZE(x) ((__typeof__(x) []){ x })
```

While this isn't very useful by itself, it can be a good building block to have. For example, here's a macro which will automatically box any value into an `NSValue` object:

```
    #define BOX(x) [NSValue valueWithBytes: POINTERIZE(x) objCType: @encode(__typeof__(x))]
```

**Built-in Functions**  
`gcc` provides two built-in functions which can be useful for building macros.

The first is `__builtin_types_compatible_p`. You pass two types to this function (`__typeof__` comes in handy here) and it produces `1` if the two types are "compatible" (roughly, if they're equal) and `0` if they aren't.

The second is `__builtin_choose_expr`. This works like the C standard `?:` operator, except that the predicate must be a compile-time constant, and the type of the entire `__builtin_choose_expr` expression is the type of whichever branch gets chosen; the two branches are not required to be similar types.

This allows you to write macros which do different things depending on the type of the argument. As an example, here's a macro which turns an expression into an `NSString`, and tries to make the output as useful as possible:

```
    // make the compiler treat x as the given type no matter what
    #define FORCETYPE(x, type) *(type *)(__typeof__(x) []){ x }
    
    #define STRINGIFY(x) \
        __builtin_choose_expr( \
            __builtin_types_compatible_p(__typeof__(x), NSRect), \
                NSStringFromRect(FORCETYPE(x, NSRect)), \
            \
        __builtin_choose_expr( \
            __builtin_types_compatible_p(__typeof__(x), NSSize), \
                NSStringFromSize(FORCETYPE(x, NSSize)), \
            \
        __builtin_choose_expr( \
            __builtin_types_compatible_p(__typeof__(x), NSPoint), \
                NSStringFromPoint(FORCETYPE(x, NSPoint)), \
            \
        __builtin_choose_expr( \
            __builtin_types_compatible_p(__typeof__(x), SEL), \
                NSStringFromSelector(FORCETYPE(x, SEL)), \
            \
        __builtin_choose_expr( \
            __builtin_types_compatible_p(__typeof__(x), NSRange), \
                NSStringFromRange(FORCETYPE(x, NSRange)), \
            \
            [NSValue valueWithBytes: (__typeof__(x) []){ x } objCType: @encode(__typeof__(x))] \
        )))))
```

Note the `FORCETYPE` macro. Even though the code branch to follow is chosen at compile time, unused branches still have to be valid code. The compiler won't accept `NSStringFromRect(42)` even though that branch will never be chosen. By pointerizing the value and then casting it before dereferencing it, it ensures that the code will compile. The cast is invalid for everything but the one branch that is taken, but it doesn't need to be valid for any of the others anyway.

**X-Macros**  
 This is something I've never used, but is interesting enough that it deserves mention. X-macros are a way of defining a macro in terms of another macro, which are then redefined multiple times to give that macro new meaning. This is confusing, so here's an example:

```
    #define MY_ENUM \
        MY_ENUM_MEMBER(kStop) \
        MY_ENUM_MEMBER(kGo) \
        MY_ENUM_MEMBER(kYield)
    
    // create the actual enum
    enum MyEnum {
        #define MY_ENUM_MEMBER(x) x,
        MY_ENUM
        #undef MY_ENUM_MEMBER
    };
    
    // stringification
    const char *MyEnumToString(enum MyEnum value)
    {
        #define MY_ENUM_MEMBER(x) if(value == (x)) return #x;
        MY_ENUM
        #undef MY_ENUM_MEMBER
    }
    
    // destringification
    enum MyEnum MyEnumFromString(const char *str)
    {
        #define MY_ENUM_MEMBER(x) if(strcmp(str, #x) == 0) return x;
        MY_ENUM
        #undef MY_ENUM_MEMBER
        
        // default value
        return -1;
    }
```

This is an advanced and frightening technique, but it could help eliminate a lot of boring repetition in certain specialized cases. For more information about X-macros, consult [the Wikipedia article](http://en.wikipedia.org/wiki/C_preprocessor#X-Macros).

**Conclusion**  
 C macros are complicated and powerful. If you use them, you must be extremely careful not to abuse them. However, in some situations they can be incredibly useful, and, when used correctly, these tips and tricks can help you create macros which make your code easier to write and easier to read.

That's it for 2010. Come back next year (in two weeks) for the next Friday Q&A. As always, if you have a topic that you would like to see covered here, [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-12-31-c-macro-tips-and-tricks.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
