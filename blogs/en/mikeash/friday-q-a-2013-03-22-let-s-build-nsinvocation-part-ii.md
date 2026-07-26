---
title: 'Friday Q&A 2013-03-22: Let''s Build NSInvocation, Part II'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-03-22-lets-build-nsinvocation-part-ii.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:65bbee0f0739fc04'
translated: false
---

> 原文：[Friday Q&A 2013-03-22: Let's Build NSInvocation, Part II](https://www.mikeash.com/pyblog/friday-qa-2013-03-22-lets-build-nsinvocation-part-ii.html)　·　mikeash.com Friday Q&A

Posted at 2013-03-22 14:57 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Objective-C Literals in Serbo-Croatian](https://www.mikeash.com/pyblog/objective-c-literals-in-serbo-croatian.html)  
Previous article: [Friday Q&A 2013-03-08: Let's Build NSInvocation, Part I](https://www.mikeash.com/pyblog/friday-qa-2013-03-08-lets-build-nsinvocation-part-i.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2013-03-22: Let's Build NSInvocation, Part II

by [Mike Ash](https://www.mikeash.com/)

**Recap**  
`MAInvocation` is my reimplementation of a large chunk of `NSInvocation`. For simplicity, it doesn't support floating point arguments or return values, and it also doesn't support `struct` arguments. It only supports the `x86-64` architecture. The code is on GitHub here:

[https://github.com/mikeash/MAInvocation](https://github.com/mikeash/MAInvocation)

The first six parameters to a function are passed in six registers: `rdi`, `rsi`, `rdx`, `rcx`, `r8`, and `r9`. Subsequent parameters, if any, are passed on the stack. Return values are returned in `rax`. For the special case of a two-element struct, the second element is returned in `rdx`. Larger structs are returned by having the caller allocate memory, and then a pointer to that memory is implicitly passed in as the first parameter in `rdi`, with all explicit parameters bumped down. These are called `stret` calls in the Objective-C world.

Assembly language glue is used to translate between values held in a `struct` and actual function calls. The `struct` holds all of the registers in question, plus a pointer to stack arguments, plus some additional data:

```
    struct RawArguments
    {
        void *fptr;

        uint64_t rdi;
        uint64_t rsi;
        uint64_t rdx;
        uint64_t rcx;
        uint64_t r8;
        uint64_t r9;

        uint64_t stackArgsCount;
        uint64_t *stackArgs;

        uint64_t rax_ret;
        uint64_t rdx_ret;

        uint64_t isStretCall;
    };
```

The `MAInvocationCall` function is written in assembly, and was explored [in the previous article](https://www.mikeash.com/pyblog/friday-qa-2013-03-08-lets-build-nsinvocation-part-i.html). It has this prototype:

```
    void MAInvocationCall(struct RawArguments *);
```

Objective-C code can fill out a `struct RawArguments` with a function pointer and the appropriate register values, then call this function. It will make the function call, and on return, the two return value register fields in the `struct` will be filled out with whatever the function returned.

There are also two forwarding handlers:

```
    void MAInvocationForward(void);
    void MAInvocationForwardStret(void);
```

These are designed to be invoked by an arbitrary Objective-C method call. They both create a new `struct RawArguments`, fill out the argument registers and stack arguments pointer, and then invoke a C function called `MAInvocationForwardC`. When that returns, the handlers pass the `rax_ret` and `rdx_ret` values back to the caller. The only difference between these two handlers is whether they set the `isStretCall` to `0` or `1`.

The stage is now set for the Objective-C implementation of `MAInvocation`.

**Interface**  
The interface to `MAInvocation` is the same as `NSInvocation`:

```
    @interface MAInvocation : NSObject

    + (MAInvocation *)invocationWithMethodSignature:(NSMethodSignature *)sig;

    - (NSMethodSignature *)methodSignature;

    - (void)retainArguments;
    - (BOOL)argumentsRetained;

    - (id)target;
    - (void)setTarget:(id)target;

    - (SEL)selector;
    - (void)setSelector:(SEL)selector;

    - (void)getReturnValue:(void *)retLoc;
    - (void)setReturnValue:(void *)retLoc;

    - (void)getArgument:(void *)argumentLocation atIndex:(NSInteger)idx;
    - (void)setArgument:(void *)argumentLocation atIndex:(NSInteger)idx;

    - (void)invoke;
    - (void)invokeWithTarget:(id)target;

    @end
```

**Instance Variables**  
The method signature is central to an invocation object. The method signature describes how many parameters the method takes, as well as what the types are. This is critical information to be able to figure out how to deal with method parameters and return types. This is why the only way to create an `MAInvocation` is with an `NSMethodSignature`, and that signature is stored in an instance variable:

```
    @implementation MAInvocation {
        NSMethodSignature *_sig;
```

The invocation keeps a local `struct RawArguments`. This `struct` is manipulated directly when setting or getting arguments and return values. When the invocation is invoked, a pointer to the instance variable can be passed directly to the assembly language glue:

```
        struct RawArguments _raw;
```

Invocations can retain their arguments. This sends `retain` to all object arguments, and it also copies C string arguments. Whether arguments are currently retained needs to be tracked, so that they can be properly freed, and so that newly-set arguments can be retained, so there's a flag for that:

```
        BOOL _argumentsRetained;
```

Finally, there needs to be a buffer to store the return value for `stret` calls:

```
        void *_stretBuffer;
    }
```

**Initialization**  
The factory method just calls an `init` method:

```
    + (NSInvocation *)invocationWithMethodSignature: (NSMethodSignature *)sig
    {
        return [[[self alloc] initWithMethodSignature: sig] autorelease];
    }
```

The `init` method saves the method signature:

```
    - (id)initWithMethodSignature: (NSMethodSignature *)sig
    {
        if((self = [super init]))
        {
            _sig = [sig retain];
```

It then populates the `isStretCall` of the `struct RawArguments` by examining the method signature to determine whether it fits the requirements for a `stret` call. This is done by calling another method. The code for that method is rather involved, and will come later:

```
            _raw.isStretCall = [self isStretReturn];
```

Next, the stack arguments are set up. The first thing to do here is to get the total number of arguments from the method signature:

```
            NSUInteger argsCount = [sig numberOfArguments];
```

Note that this count includes the two implicit arguments, `self` and `_cmd`, so this number is exactly equal to the number of function arguments being passed.

If it's a `stret` call, then there's effectively one more argument, because of the implicit pointer for the return value passed in `rdi`:

```
            if(_raw.isStretCall)
                argsCount++;
```

If there are more than six arguments (potentially including the implicit `stret` parameter), then there are stack arguments. `stackArgsCount` is set to the number of remaining arguments, and memory is allocated so that `stackArgs` can hold them:

```
            if(argsCount > 6)
            {
                _raw.stackArgsCount = argsCount - 6;
                _raw.stackArgs = calloc(argsCount - 6, sizeof(*_raw.stackArgs));
            }
        }
        return self;
    }
```

**Wrapper Methods**  
There are a few methods in the API that are simply small wrappers around other methods. I'll cover them here before we get to the real meat.

The `target` method just gets the value of the first argument in a slightly more convenient way. The method is just a small wrapper around the `getArgument:atIndex:` method:

```
    - (id)target
    {
        id target;
        [self getArgument: &target atIndex: 0];
        return target;
    }
```

The `setTarget:` method is an even simpler wrapper around the `setArgument:atIndex:` method:

```
    - (void)setTarget: (id)target
    {
        [self setArgument: &target atIndex: 0];
    }
```

The `selector` and `setSelector:` methods are virtually identical, but manipulate the second argument:

```
    - (SEL)selector
    {
        SEL sel;
        [self getArgument: &sel atIndex: 1];
        return sel;
    }

    - (void)setSelector: (SEL)selector
    {
        [self setArgument: &selector atIndex: 1];
    }
```

Finally, the `invoke` method calls `invokeWithTarget:`, passing `[self target]`:

```
    - (void)invoke
    {
        [self invokeWithTarget: [self target]];
    }
```

**Getting Arguments**  
In order to get an argument out of the invocation, the code first needs to know _where_ an argument is stored. This small wrapper method handles that:

```
    - (uint64_t *)argumentPointerAtIndex: (NSInteger)idx
    {
        uint64_t *ptr = NULL;
        if(idx == 0)
            ptr = &_raw.rdi;
        if(idx == 1)
            ptr = &_raw.rsi;
        if(idx == 2)
            ptr = &_raw.rdx;
        if(idx == 3)
            ptr = &_raw.rcx;
        if(idx == 4)
            ptr = &_raw.r8;
        if(idx == 5)
            ptr = &_raw.r9;
        if(idx >= 6)
            ptr = _raw.stackArgs + idx - 6;
        return ptr;
    }
```

This method takes a _raw_ argument index, which is to say that it's already been adjusted to take into account whether or not this is a `stret` call. It then maps that index onto the appropriate register or stack slot.

It's also handy to be able to get the size of a particular argument, so it can copy the right number of bytes for arguments that are smaller than 8 bytes. This method wraps the Foundation function `NSGetSizeAndAlignment`, which takes an Objective-C type string and returns the size (and alignment!) of the type in question:

```
    - (NSUInteger)sizeOfType: (const char *)type
    {
        NSUInteger size;
        NSGetSizeAndAlignment(type, &size, NULL);
        return size;
    }
```

Another small wrapper around _this_ method provides the size of a given argument:

```
    - (NSUInteger)sizeAtIndex: (NSInteger)idx
    {
        return [self sizeOfType: [_sig getArgumentTypeAtIndex: idx]];
    }
```

To actually fetch an argument, the method first adjusts the requested index to take into account the possible `stret` return:

```
    - (void)getArgument: (void *)argumentLocation atIndex: (NSInteger)idx
    {
        NSInteger rawArgumentIndex = idx;
        if(_raw.isStretCall)
            rawArgumentIndex++;
```

Next, it grabs the pointer from the above method, and checks it for sanity:

```
        uint64_t *src = [self argumentPointerAtIndex: rawArgumentIndex];
        assert(src);
```

Then it grabs the argument size and copies the appropriate number of bytes out of the argument location:

```
        NSUInteger size = [self sizeAtIndex: idx];
        memcpy(argumentLocation, src, size);
    }
```

**Getting and Setting Return Values**  
To get and set the return value, the value's size is needed. This is easy to obtain by just getting the size of the return type obtained from the method signature:

```
    - (NSUInteger)returnValueSize
    {
        return [self sizeOfType: [_sig methodReturnType]];
    }
```

It's also necessary to get a pointer to the location where the return value is stored. If the invocation is for a `stret` call, then it returns `_stretBuffer`. If the buffer isn't allocated yet, it allocates it:

```
    - (void *)returnValuePtr
    {
        if(_raw.isStretCall)
        {
            if(_stretBuffer == NULL)
                _stretBuffer = calloc(1, [self returnValueSize]);
            return _stretBuffer;
        }
```

For regular calls, it just returns the address of the `rax_ret` field in the raw arguments `struct`:

```
        else
        {
            return &_raw.rax_ret;
        }
    }
```

This takes care of the case where the return value uses both return registers. Since they're contiguous in the `struct`, copying a sufficiently large value into this address will write to both register fields in the `struct`.

With these methods available, writing the methods to get and set the return value is easy. All they have to do is call `memcpy` with the computed size and pointer:

```
    - (void)getReturnValue: (void *)retLoc
    {
        NSUInteger size = [self returnValueSize];
        memcpy(retLoc, [self returnValuePtr], size);
    }

    - (void)setReturnValue: (void *)retLoc
    {
        NSUInteger size = [self returnValueSize];
        memcpy([self returnValuePtr], retLoc, size);
    }
```

**Type Classification**  
Determining whether a method's return type requires a `stret` call requires classifying that type according to the `x86-64` calling conventions. The `NSInvocation` API allows for retaining the arguments to the invocation, which also requires classifying the argument types, so that all of the object types can be found.

The different classifications get put into an `enum` which combines the relevant parts of the `x86-64` ABI with the distinctions necessary for retaining arguments. This boils down to objects, blocks, C strings, other integer types (including non-object pointers), a `struct` containing _two_ integers, an empty `struct`, any other `struct`, and any other type not already covered:

```
    enum TypeClassification
    {
        TypeObject,
        TypeBlock,
        TypeCString,
        TypeInteger,
        TypeTwoIntegers,
        TypeEmptyStruct,
        TypeStruct,
        TypeOther
    };
```

The classification process itself consists of two mutually-recursive methods: one that classifies arbitrary types, and one specialized to classify `struct` types.

The general method starts by creating the type strings for 'id', blocks, and C strings by using the `@encode` directive:

```
    - (enum TypeClassification)classifyType: (const char *)type
    {
        const char *idType = @encode(id);
        const char *blockType = @encode(void (^)(void));
        const char *charPtrType = @encode(char *);
```

Note that all blocks have the same type string when it comes to `@encode`, so the choice of block type here is completely arbitrary.

With these in hand, it compares `type` against them, and returns the appropriate `enum` value if there's a match:

```
        if(strcmp(type, idType) == 0)
            return TypeObject;
        if(strcmp(type, blockType) == 0)
            return TypeBlock;
        if(strcmp(type, charPtrType) == 0)
            return TypeCString;
```

Next, it checks integer types. This crazy bit of code constructs a C string that contains every the character for every integer type, plus function pointers (which is just `?`), plus any other pointer (which all start with `^`):

```
        char intTypes[] = { @encode(signed char)[0], @encode(unsigned char)[0], @encode(short)[0], @encode(unsigned short)[0], @encode(int)[0], @encode(unsigned int)[0], @encode(long)[0], @encode(unsigned long)[0], @encode(long long)[0], @encode(unsigned long long)[0], '?', '^', 0 };
```

With that C string in hand, the `strchr` function can be used to check the first character in `type` aganist all of these characters. If there's a match, then the type is an integer type:

```
        if(strchr(intTypes, type[0]))
            return TypeInteger;
```

`struct` types begin with the `{` character. If the type string starts with that character, then call into the struct classifier:

```
        if(type[0] == '{')
            return [self classifyStructType: type];
```

If nothing matches, then return the "other" type:

```
        return TypeOther;
    }
```

The `struct` classifier uses a helper method that takes the type string for the `struct` and enumerates over all of its contents. It tracks the struct's classification at each point, and updates it with each new element in the `struct`. It starts out with an empty `struct`:

```
    - (enum TypeClassification)classifyStructType: (const char *)type
    {
        __block enum TypeClassification structClassification = TypeEmptyStruct;
```

Then it enumerates and classifies each type within:

```
        [self enumerateStructElementTypes: type block: ^(const char *type) {
            enum TypeClassification elementClassification = [self classifyType: type];
```

If the current classification is an empty `struct`, then the new classification is the same as the element classification. A struct with one element is classified the same as the element it contains:

```
            if(structClassification == TypeEmptyStruct)
                structClassification = elementClassification;
```

If the current classification is an integer type and the element classification is also an integer type, then the `struct` gets the special classification of a `struct` containing two integers:

```
            else if([self isIntegerClass: structClassification] && [self isIntegerClass: elementClassification])
                structClassification = TypeTwoIntegers;
```

In any other circumstance (`struct` contains more than two elements, `struct` contains floating-point elements, etc.) the classification is just a generic `struct`:

```
            else
                structClassification = TypeStruct;
        }];
        return structClassification;
    }
```

The method to enumerate over a `struct` type string's elements is short. A `struct` type string consists of the `struct`'s name, the `=` symbol, and then each element's type concatenated together, all contained within a pair of `{}`. For example, `NSRange` would look like:

```
    {NSRange=LL}
```

The first thing the method does is find the `=` and start scanning just beyond it:

```
    - (void)enumerateStructElementTypes: (const char *)type block: (void (^)(const char *type))block
    {
        const char *equals = strchr(type, '=');
        const char *cursor = equals + 1;
```

Then it enumerates over each type contained within, taking advantage of `NSGetSizeAndAlignment` to move the cursor to the end of each type encountered, even if the type contains more than one character. It does this until it encounters a closing brace:

```
        while(*cursor != '}')
        {
            block(cursor);
            cursor = NSGetSizeAndAlignment(cursor, NULL, NULL);
        }
    }
```

There's also a short helper method that determines whether a particular type classification is considered an integer. This just checks to see if the classification is an object, block, C string, or an actual integer or other pointer:

```
    - (BOOL)isIntegerClass: (enum TypeClassification)classification
    {
        return classification == TypeObject || classification == TypeBlock || classification == TypeCString || classification == TypeInteger;
    }
```

This finishes the type classification system. This is somewhat rudimentary compared to the full complexity of the `x86-64` spec, but it's enough for `MAInvocation`'s needs. With type classification available, we can finally implement the `isStretReturn` method used in the initializer:

```
    - (BOOL)isStretReturn
    {
        return [self classifyType: [_sig methodReturnType]] == TypeStruct;
    }
```

**Setting Arguments**  
With type classification in place, it's finally time to implement setting arguments. The basic form of `setArgument:atIndex:` is nearly identical to `getArgument:atIndex:`, but the need to support retained arguments makes everything far more complicated.

It's possible to create an `NSInvocation`, set it up, and then keep it around for a while. In order for the `NSInvocation` to remain valid, it needs to be able to do proper memory management on the arguments it contains. In a nod to flexibility, this is optional. A freshly-made `NSInvocation` doesn't do any memory management on its arguments, but it can be enabled by sending it a `retainArguments` message.

`MAInvocation` mimics this functionality. When it receives `retainArguments` it performs the following operations on its arguments:

```
    1. Block arguments are copied.
    2. Non-block object arguments are retained.
    3. C string arguments are copied.
    4. All others are left alone.
```

In addition to doing this for `retainArguments`, the `setArgument:atIndex:` method needs to do this for each newly set argument as well. This is what makes it so much more complex than `getArgument:atIndex:`.

The method starts off by computing the raw argument index:

```
    - (void)setArgument: (void *)argumentLocation atIndex: (NSInteger)idx
    {
        NSInteger rawArgumentIndex = idx;
        if(_raw.isStretCall)
            rawArgumentIndex++;
```

Next, it gets the argument pointer at that index:

```
        uint64_t *dest = [self argumentPointerAtIndex: rawArgumentIndex];
        assert(dest);
```

Then it classifies the argument at this index:

```
        enum TypeClassification c = [self classifyArgumentAtIndex: idx];
```

If arguments are retained, it will then check the classification of the arguments to see if it's a block, a non-block object, or a C string. If it is, then it directly sets `dest` to the value found at `argumentLocation` using the appropriate `retain` or `copy` semantics. If argument is of a different type, or if arguments aren't retained, it does a simple `memcpy`.

The first case is for plain objects. This just does a fairly standard `retain`/`release` combination, with a bunch of casting to treat both pointers as object pointers. The `release` is done at the end using the `old` variable to avoid problems where releasing the old value invalidates the new one:

```
        if(_argumentsRetained && c == TypeObject)
        {
            id old = *(id *)dest;
            *(id *)dest = [*(id *)argumentLocation retain];
            [old release];
        }
```

Blocks get the same treatment, except they get a `copy` rather than a `retain`:

```
        else if(_argumentsRetained && c == TypeBlock)
        {
            id old = *(id *)dest;
            *(id *)dest = [*(id *)argumentLocation copy];
            [old release];
        }
```

C strings are similar, but use `strdup` and `free`:

```
        else if(_argumentsRetained && c == TypeCString)
        {
            char *old = *(char **)dest;

            char *cstr = *(char **)argumentLocation;
            if(cstr != NULL)
                cstr = strdup(cstr);
            *(char **)dest = cstr;

            free(old);
        }
```

In all other cases, the appropriate number of bytes is copied over using `memcpy`:

```
        else
        {
            NSUInteger size = [self sizeAtIndex: idx];
            memcpy(dest, argumentLocation, size);
        }
    }
```

The `classifyArgumentAtIndex:` is a small wrapper around `classifyType:` that retrieves the argument type from the method signature and classifies it:

```
    - (enum TypeClassification)classifyArgumentAtIndex: (NSUInteger)idx
    {
        return [self classifyType: [_sig getArgumentTypeAtIndex: idx]];
    }
```

**Retaining Arguments**  
In addition to retaining each argument as it arrives in `setArgument:atIndex:`, `MAInvocation` also needs to retain all existing arguments in the `retainArguments` method. Only the first call does anything, so the first thing that method does is check to see if arguments are already retained, and bail out if so:

```
    - (void)retainArguments
    {
        if(_argumentsRetained)
            return;
```

Next, it iterates over all retainable arguments, using a helper method. This method invokes a block for each retainable argument that passes in the argument index as well as the argument's value. There are three value arguments in the block, and only one is set for any given call.

```
        [self iterateRetainableArguments: ^(NSUInteger idx, id obj, id block, char *cstr) {
```

If it's an object argument, then that argument is retained:

```
            if(obj)
            {
                [obj retain];
            }
```

If it's a block argument, the block is copied, and the new value set as the argument value. Note that `_argumentsRetained` has not yet been set to `YES`, so `setArgument:atIndex:` won't try to do its own memory management, avoiding any conflict between the two:

```
            else if(block)
            {
                block = [block copy];
                [self setArgument: &block atIndex: idx];
            }
```

If it's a C string argument, it uses `strdup`:

```
            else if(cstr)
            {
                if(cstr != NULL)
                    cstr = strdup(cstr);
                [self setArgument: &cstr atIndex: idx];
            }
        }];
```

Finally, it sets `_argumentsRetained`:

```
        _argumentsRetained = YES;
    }
```

The `iterateRetainableArguments:` method uses the type classification system to figure out what each argument is, then calls `getArgument:atIndex:` to fetch the value. It first iterates over each argument and classifies it:

```
    - (void)iterateRetainableArguments: (void (^)(NSUInteger idx, id obj, id block, char *cstr))block
    {
        for(NSUInteger i = 0; i < [_sig numberOfArguments]; i++)
        {
            enum TypeClassification c = [self classifyArgumentAtIndex: i];
```

Objects and blocks are both handled by the same branch. It first retrieves the argument into a local `id` variable:

```
            if(c == TypeObject || c == TypeBlock)
            {
                id arg;
                [self getArgument: &arg atIndex: i];
```

It then moves `arg` into one of two other local variables depending on whether the type is a block or a plain object:

```
                id o = c == TypeObject ? arg : nil;
                id b = c == TypeBlock ? arg : nil;
```

At this point, `o` contains the argument value if it's a plain argument, and `b` contains the argument value if it's a block. The iteration block can then be called with these values:

```
                block(i, o, b, NULL);
            }
```

C strings are similar, but less complex, because there's only one possible type here:

```
            else if(c == TypeCString)
            {
                char *arg;
                [self getArgument: &arg atIndex: i];

                block(i, nil, nil, arg);
            }
        }
    }
```

While we're at it, here's a quick getter method for `argumentsRetained`:

```
    - (BOOL)argumentsRetained
    {
        return _argumentsRetained;
    }
```

**Dealloc**  
The hardest part of `dealloc` is freeing the retained arguments. The `iterateRetainableArguments:` method takes care of most of the work:

```
    - (void)dealloc
    {
        if(_argumentsRetained)
        {
            [self iterateRetainableArguments: ^(NSUInteger idx, id obj, id block, char *cstr) {
                [obj release];
                [block release];
                free(cstr);
            }];
        }
```

With that taken care of, all that remains is freeing the method signature, the `stackArgs` pointer, and calling `super`:

```
        [_sig release];
        free(_raw.stackArgs);

        [super dealloc];
    }
```

**Invocation**  
The code so far has kept the `struct RawArguments` almost completely up to date. Implementing `invokeWithTarget:` is simply a matter of filling out the last details, then making a call to the `MAInvocationCall` assembly glue function. The method starts out by setting the target value:

```
    - (void)invokeWithTarget: (id)target
    {
        [self setTarget: target];
```

It then uses `methodForSelector:` to get the function pointer for the invocation's selector and places that into the `fptr` field. This is what the glue code will call:

```
        _raw.fptr = [target methodForSelector: [self selector]];
```

If this is a `stret` call, then `rdi` needs to be set up to point to space that can hold the return value:

```
        if(_raw.isStretCall)
            _raw.rdi = (uint64_t)[self returnValuePtr];
```

Finally, call the assembly glue:

```
        MAInvocationCall(&_raw);
    }
```

With all of the register fields and the stack arguments pointer set up, and the function pointer field set to the target `IMP`, the assembly glue is able to make the call. Upon return, the assembly glue copies `rax` and `rdx` into the return value fields of the `struct RawArguments`. This means that the return value is already set when the assembly glue returns, and will be available from `getReturnValue:` without any additional action in the Objective-C code.

**Forwarding**  
The last major piece of `MAInvocation` is the `MAInvocationForwardC` function. The assembly language forwarding glue intercepts unknown message calls. It then constructs a `struct RawArguments` on the stack from the function call, and then calls through to `MAInvocationForwardC`, passing it a pointer to the `struct RawArguments`. The remainder of the logic is implemented in Objective-C:

```
    void MAInvocationForwardC(struct RawArguments *r)
    {
```

The first order of business is to get the object that the message was sent to, and the selector being sent. For a `stret` call, the object is in `rsi` and the selector is in `rdx`. For a normal call, the object is in `rdi` and the selector is in `rsi`:

```
        id obj;
        SEL sel;

        if(r->isStretCall)
        {
            obj = (id)r->rsi;
            sel = (SEL)r->rdx;
        }
        else
        {
            obj = (id)r->rdi;
            sel = (SEL)r->rsi;
        }
```

A method signature is critical to creating an invocation object. With the object and selector available, a simple call to `methodSignatureForSelector:` obtains that:

```
        NSMethodSignature *sig = [obj methodSignatureForSelector: sel];
```

With the method signature in hand, the forwarding function can now create an `MAInvocation`:

```
        MAInvocation *inv = [[MAInvocation alloc] initWithMethodSignature: sig];
```

The next order of business is to copy all of the pertinent information from `r into the invocation's`_raw` instance variable. First come the registers:

```
        inv->_raw.rdi = r->rdi;
        inv->_raw.rsi = r->rsi;
        inv->_raw.rdx = r->rdx;
        inv->_raw.rcx = r->rcx;
        inv->_raw.r8 = r->r8;
        inv->_raw.r9 = r->r9;
```

After that, stack arguments are copied. Although `r` always contains `0` for `stackArgsCount`, the invocation has now computed the number of actual stack arguments, so its `_raw` variable can be consulted to get the count:

```
        memcpy(inv->_raw.stackArgs, r->stackArgs, inv->_raw.stackArgsCount * sizeof(uint64_t));
```

The invocation is now fully constructed and filled out. The object is sent `forwardInvocation:` with the newly constructed invocation.

```
        [obj forwardInvocation: (id)inv];
```

After that call returns, the return value from the invocation needs to be copied back into `r`. The assembly glue will then pass the value back to the caller. It first copies the two return value registers over:

```
        r->rax_ret = inv->_raw.rax_ret;
        r->rdx_ret = inv->_raw.rdx_ret;
```

If it's a `stret` call and the invocation actually has a buffer to hold the return value, the value in the invocation's return value buffer is copied into the memory pointed to by `r->rdi`, which is where the caller specified that it wanted the return value placed:

```
        if(r->isStretCall && inv->_stretBuffer)
        {
            memcpy((void *)r->rdi, inv->_stretBuffer, [inv returnValueSize]);
        }
```

Everything is now complete, so the invocation is released, and control is returned to the assembly language glue:

```
        [inv release];
    }
```

The glue code will now copy the `rax` and `rdx` fields back into the respective CPU registers, then return control to the original method caller, which will see the return value either in those registers or in the `stret` buffer that it passed in `rdi`.

**Conclusion**  
That wraps up the implementation of `MAInvocation`. It's enormously complicated and involved, despite only supporting `x86-64` and ignoring `struct` parameters and floating point of all kinds, which are a large part of the `x86-64` calling conventions. `NSInvocation` not only supports all types of parameters and return values (aside from a few corner cases like `union` parameters), it also supports them on at least three different architectures: `i386`, `x86-64`, and `ARM`.

However, despite the complication, it's all very much doable. Covering all of the cases requires a lot of time and effort, but there's nothing mysterious or magical. It would require equivalents of the assembly glue functions for the other architectures, expanding the glue functions to cover the floating-point registers, and implementing all of the logic for which arguments go where in the `MAInvocation` Objective-C code.

`MAInvocation` was a lot of fun to build and gives great insight on just what `NSInvocation` is doing. It should be obvious, but don't use `MAInvocation` for any real work. `NSInvocation` does all the same stuff and more, and no doubt does it better.

That's it for today. Come back next time for another breathtaking adventure. Friday Q&A is driven by reader ideas, so until then, please keep [sending in your ideas for topics to cover](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
