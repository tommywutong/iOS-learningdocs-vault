---
title: 'Friday Q&A 2011-05-06: A Tour of MABlockClosure'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-05-06-a-tour-of-mablockclosure.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1300bcf592773945'
translated: false
---

> 原文：[Friday Q&A 2011-05-06: A Tour of MABlockClosure](https://www.mikeash.com/pyblog/friday-qa-2011-05-06-a-tour-of-mablockclosure.html)　·　mikeash.com Friday Q&A

Posted at 2011-05-06 17:34 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2011-05-20: The Inner Life of Zombies](https://www.mikeash.com/pyblog/friday-qa-2011-05-20-the-inner-life-of-zombies.html)  
Previous article: [Friday Q&A Falls Behind](https://www.mikeash.com/pyblog/friday-qa-falls-behind.html)  
Tags: [blocks](https://www.mikeash.com/pyblog/?tag=blocks) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [libffi](https://www.mikeash.com/pyblog/?tag=libffi) [trampoline](https://www.mikeash.com/pyblog/?tag=trampoline)

Friday Q&A 2011-05-06: A Tour of MABlockClosure

by [Mike Ash](https://www.mikeash.com/)

**Recap**  
 Blocks are an extremely useful language feature for two reasons: they allow writing anonymous functions inlined in other code, and they can capture context from the enclosing scope by referring to local variables from that scope. Among other things, this makes callback patterns much simpler. Instead of this:

```
    struct CallbackContext
    {
        NSString *title;
        int value;
    };
    
    static void MyCallback(id result, void *contextVoid)
    {
        struct CallbackContext *context = contextVoid;
        // use result, context->title, and context->value
    }
    
    struct CallbackContext ctx;
    ctx.title = [self title];
    ctx.value = [self value];
    CallAPIWithCallback(workToDo, MyCallback, &ctx;);
```

You can just do this:

```
    CallAPIWithCallbackBlock(workToDo, ^(id result) {
        // use result, [self title], [self value]
    });
```

As you can see, the convenience factor is enormous. While blocks don't fundamentally allow anything new, the removal of so much boilerplate code makes life much easier and makes it much nicer to use callbacks-based APIs frequently.

The problem is that not all callbacks-based APIs have versions that take blocks. What `MABlockClosure` and my older experimental trampoline code allow is converting a block to a function pointer that can be passed to one of these APIs. For example, if `CallAPIWithCallbackBlock` didn't exist, `MABlockClosure` allows writing code that's nearly as nice:

```
    CallAPIWithCallback(workToDo, BlockFptrAuto(^(id result) {
        // use result, [self title], [self value]
    }));
```

This is done by generating a trampoline function which captures its arguments, massages them as needed, then calls through to the block.

**Blocks ABI**  
 Blocks compile down to a function and a couple of structs. The function holds the code, and the structs hold information about the block, including the captured context. The function contains an implicit argument, much like the `self` argument to Objective-C methods, which points to the block structure. The block above translates to something like this:

```
    void BlockImpl(struct BlockStruct *block, id info)
    {
        // code goes here
    }
```

The important thing here is that calling a block is the same as calling a function, except with an extra argument at the front pointing to the block structure.

My original attempt used a small bit of assembly code for the trampoline. This code tried to shift the arguments in a general fashion, and then insert the pointer at the front. Unfortunately, this really can't be done by the same code for all cases, so it ended up with a lot of irritating restrictions.

At the time, this was about the best that could be done. Fortunately, Apple later added type metadata to blocks. As long as you're using a compiler that's recent enough to generate this metadata (any recent `clang` will do), this can be used to generate intelligent trampolines which do the appropriate argument manipulation.

**`libffi`**  
 Although the block type metadata provides all of the necessary information needed to perform the necessary argument transformation, it's still an extremely complicated undertaking. The exact nature of what needs to be done depends heavily on the function call ABI of the particular architecture the code is running on, and the particular argument types present.

If I had to do all of this myself, I never would have been able to put in the enormous effort required. The good news is that there is a library already built which knows how to handle all of this for a whole bunch of different architectures: [`libffi`](https://github.com/atgreen/libffi).

`libffi` provides two major facilities. It's best known for the ability to call into an arbitrary function with arbitrary arguments whose types aren't known until runtime. A lesser-known facility provides what is essentially the opposite: it allows creating "closures" which are runtime-generated functions which capture arbitrary arguments whose types aren't known until runtime.

The latter is what we need to generate the trampoline function for the block. This captures the arguments in a form that can be manipulated from C code. That code can then manipulate the arguments as needed and use the former facility to call the block's implementation pointer.

**Support Structures**  
 The layout of a block structure is not in any published header. However, since these structures are baked into executables when they're compiled, we can safely extract them from [the specification](http://clang.llvm.org/docs/Block-ABI-Apple.txt) and rely on that to match.

These are the structures in question:

```
    struct BlockDescriptor
    {
        unsigned long reserved;
        unsigned long size;
        void *rest[1];
    };
    
    struct Block
    {
        void *isa;
        int flags;
        int reserved;
        void *invoke;
        struct BlockDescriptor *descriptor;
    };
```

I also built a couple of wrapper functions for retrieving the implementation pointer and the type signature. The implementation pointer is easy, and this function just exists to make code a bit cleaner elsewhere:

```
    static void *BlockImpl(id block)
    {
        return ((struct Block *)block)->invoke;
    }
```

The function for extracting the type signature is a little more complicated. Blocks have a `flags` field which indicates various properties about the block. One of the flags indicates whether the type signature is present, which we check to ensure that the code fails early and obviously if it's not there. Another flag indicates whether the block contains a copy and dispose callback. If it does, then the location of the type signature information moves within the block descriptor struct. Here's the code for properly extracting the type signature:

```
    static const char *BlockSig(id blockObj)
    {
        struct Block *block = (void *)blockObj;
        struct BlockDescriptor *descriptor = block->descriptor;
        
        int copyDisposeFlag = 1 << 25;
        int signatureFlag = 1 << 30;
        
        assert(block->flags & signatureFlag);
        
        int index = 0;
        if(block->flags & copyDisposeFlag)
            index += 2;
        
        return descriptor->rest[index];
    }
```

**The Class**  
 Most of the code and data structures are encapsulated in a class called `MABlockClosure`.

A lot of the necessary `libffi` data structures have to be created dynamically depending on the type signature. Manually managing that memory gets irritating. Since their lifetime is tied to the life of the closure object itself, the simplest way to deal with this is to track allocations in the object. To do this, I have an `NSMutableArray`. When I need to allocate memory, I create an `NSMutableData` of the appropriate size, add it to this array, and then return its `mutableBytes` pointer. This array is the class's first instance variable:

```
    @interface MABlockClosure : NSObject
    {
        NSMutableArray *_allocations;
```

Next comes some type information. `libffi` stores function types in a struct called `ffi_cif`. I don't know what the `cif` part stands for, but this struct basically just holds an array of argument types, plus a return type. The class needs two of these: one for the function and one for the block. Although these two are similar, they aren't identical, and it's easier to just have two than try to reuse one. It's also useful to know how many arguments there are in total when doing the argument shifting, so that is also stored in an instance variable:

```
        ffi_cif _closureCIF;
        ffi_cif _innerCIF;
        int _closureArgCount;
```

Finally come the `ffi_closure` structure, a pointer to the actual function pointer that this provides, and a pointer to the block that this whole thing is intended for:

```
        ffi_closure *_closure;
        void *_closureFptr;
        id _block;
    }
```

The class has only two public methods: an initializer, which takes a block, and an accessor which returns the function pointer:

```
    - (id)initWithBlock: (id)block;
    
    - (void *)fptr;
    
    @end
```

The `-fptr` method is just an accessor:

```
    - (void *)fptr
    {
        return _closureFptr;
    }
```

All of the real work happens in the initializer. First, it sets up the `_allocations` ivar, assigns the block, and allocates a closure. It then fills out the `ffi_cif` structures to match the block's type signature. Finally, it initializes the `libffi` closure:

```
    - (id)initWithBlock: (id)block
    {
        if((self = [self init]))
        {
            _allocations = [[NSMutableArray alloc] init];
            _block = block;
            _closure = AllocateClosure(&_closureFptr);
            [self _prepClosureCIF];
            [self _prepInnerCIF];
            [self _prepClosure];
        }
        return self;
    }
```

**Closure Allocation**  
`libffi` has changed how it deals with closures over time. Originally, closures had to be allocated by the calling code. This chunk of memory was then passed to `libffi` which did its thing. Afterwards, the client had to mark that code as executable. The version of `libffi` which ships with Mac OS X works this way.

Newer versions of `libffi` encapsulate all of this in calls to allocate, prepare, and deallocate closures. This is what you'll get if you build `libffi` from source, and it's what you can get on iOS. `MABlockClosure` is built to handle both ways.

The `AllocateClosure` function uses conditional compilation to decide which technique to use. If `USE_LIBFFI_CLOSURE_ALLOC` is set, it just calls through to libffi. Otherwise, it allocates the memory using `mmap`, which ensures that the memory is properly aligned and can later be marked executable. Here's what that function looks like:

```
    static void *AllocateClosure(void **codePtr)
    {
    #if USE_LIBFFI_CLOSURE_ALLOC
        return ffi_closure_alloc(sizeof(ffi_closure), codePtr);
    #else
        ffi_closure *closure = mmap(NULL, sizeof(ffi_closure), PROT_READ | PROT_WRITE, MAP_ANON | MAP_PRIVATE, -1, 0);
        if(closure == (void *)-1)
        {
            perror("mmap");
            return NULL;
        }
        *codePtr = closure;
        return closure;
    #endif
    }
```

There's also a matching function to deallocate the closure. This just calls into `libffi` or `munmap` depending on which mode it's operating in:

```
    static void DeallocateClosure(void *closure)
    {
    #if USE_LIBFFI_CLOSURE_ALLOC
        ffi_closure_free(closure);
    #else
        munmap(closure, sizeof(ffi_closure));
    #endif
    }
```

**CIF Preparation**  
 After allocating the closure, `-initWithBlock:` then prepares the CIF structs which hold the type information for `libffi`. The type information can be obtained from the block using the `BlockSig` helper function shown earlier. However, this type information is in Objective-C `@encode` format. Converting from one to the other is not entirely trivial.

The two `prep` methods called by `-initWithBlock:` just call through to a single common method with slightly different arguments:

```
    - (void)_prepClosureCIF
    {
        _closureArgCount = [self _prepCIF: &_closureCIF withEncodeString: BlockSig(_block) skipArg: YES];
    }
    
    - (void)_prepInnerCIF
    {
        [self _prepCIF: &_innerCIF withEncodeString: BlockSig(_block) skipArg: NO];
    }
```

The main difference here is the `skipArg` argument. This tells the method whether to skip over the first argument to the function. When generating the block's type signature, all arguments are included. When generating the closure's type signature, the first argument is skipped, and the rest are included.

The `-_prepCIF:withEncodeString:skipArg:` method in turn calls through to another method which does the real work of the conversion of the `@encode` string to an array of `ffi_type`. It then skips over the first argument if needed, and calls `ffi_prep_cif` to fill out the `ffi_cif` struct:

```
    - (int)_prepCIF: (ffi_cif *)cif withEncodeString: (const char *)str skipArg: (BOOL)skip
    {
        int argCount;
        ffi_type **argTypes = [self _argsWithEncodeString: str getCount: &argCount;];
        
        if(skip)
        {
            argTypes++;
            argCount--;
        }
        
        ffi_status status = ffi_prep_cif(cif, FFI_DEFAULT_ABI, argCount, [self _ffiArgForEncode: str], argTypes);
        if(status != FFI_OK)
        {
            NSLog(@"Got result %ld from ffi_prep_cif", (long)status);
            abort();
        }
        
        return argCount;
    }
```

**`@encode` Parsing**  
 Objective-C `@encode` strings are not very fun to work with. They are essentially a single character which indicates a primitive, or some special notation to indicate structs. In the case of method signatures, the signature string is basically just a sequence of these `@encode` types concatenated together. The first one indicates the return type, and the rest indicate the arguments. Block signatures follow this same format.

Foundation provides a handy function called `NSGetSizeAndAlignment` which helps a great deal when parsing these strings. When passed an `@encode` string, it returns the size and alignment of the first type in the string, and returns a pointer to the next type. In theory, we can iterate through the types in a block signature by just calling this function in a loop.

In practice, there's a complication. For reasons I have never discovered, method signatures (and thus block signatures) have numbers in between the individual type encodings. `NSGetSizeAndAlignment` is clueless about these, so it needs a bit of help to correctly parse one of these strings. I wrote a small helper function which calls `NSGetSizeAndAlignment` and then skips over any digits it finds after the type string:

```
    static const char *SizeAndAlignment(const char *str, NSUInteger *sizep, NSUInteger *alignp, int *len)
    {
        const char *out = NSGetSizeAndAlignment(str, sizep, alignp);
        if(len)
            *len = out - str;
        while(isdigit(*out))
            out++;
        return out;
    }
```

I also wrote a quick helper function to count the number of arguments in a signature, which is handy when building the `libffi` structures:

```
    static int ArgCount(const char *str)
    {
        int argcount = -1; // return type is the first one
        while(str && *str)
        {
            str = SizeAndAlignment(str, NULL, NULL, NULL);
            argcount++;
        }
        return argcount;
    }
```

**Creating Argument Structures**  
 The `-_argsWithEncodeString:getCount:` method parses an `@encode` string and returns an array of `ffi_type *`. It uses another method, `-_ffiArgForEncode:`, to do the final conversion of a single `@encode` type to an `ffi_type *`. The first thing it does is use the `ArgCount` helper function to figure out how many types will be present, and then allocates an array of the appropriate size:

```
    - (ffi_type **)_argsWithEncodeString: (const char *)str getCount: (int *)outCount
    {
        int argCount = ArgCount(str);
        ffi_type **argTypes = [self _allocate: argCount * sizeof(*argTypes)];
```

Next, it enters a loop, calling `SizeAndAlignment` to iterate through all of the types in the string. For all of the argument types, it uses the `-_ffiArgForEncode:` method, the final piece in our puzzle, to create an individual `ffi_type *` and put it in the array:

```
        int i = -1;
        while(str && *str)
        {
            const char *next = SizeAndAlignment(str, NULL, NULL, NULL);
            if(i >= 0)
                argTypes[i] = [self _ffiArgForEncode: str];
            i++;
            str = next;
        }
```

Once this is done, it stores the count in `outCount` and returns the argument types:

```
        *outCount = argCount;
        
        return argTypes;
    }
```

Now we are left with `-_ffiArgForEncode:`, the final piece of the puzzle. Here is the very beginning of it:

```
    - (ffi_type *)_ffiArgForEncode: (const char *)str
    {
```

There is no generalized way to convert from an `@encode` string to an `ffi_type *`. To convert primitives, I use a simple lookup table approach. I build a table of every C primitive type I can think of, and the corresponding `ffi_type *`.

`libffi` differentiates integer types by size, and has no direct equivalent to `int` or `long`. To help me convert between the two, I built some macros. (It turns out that `libffi` built some macros for this as well. There are `#define`s like `ffi_type_sint` which map to the correct base `ffi_type`. I didn't know about these when I wrote the code, so my method is _slightly_ more roundabout than it needs to be.)

As I mentioned earlier, primitives are represented as single characters in an `@encode`. To avoid hardcoding any of those character values, I use an expression like `@encode(type)[0]` to get that single character. If this equals `str[0]`, then that's the primitive type encoded by the string.

My macro for signed integers first performs this check to see if the types match. If they do, it then uses `sizeof(type)` to figure out how big the integer type in question is and return the appropriate `ffi_type *` to match. Here's what the macro looks like:

```
        #define SINT(type) do { \
            if(str[0] == @encode(type)[0]) \
            { \
               if(sizeof(type) == 1) \
                   return &ffi;_type_sint8; \
               else if(sizeof(type) == 2) \
                   return &ffi;_type_sint16; \
               else if(sizeof(type) == 4) \
                   return &ffi;_type_sint32; \
               else if(sizeof(type) == 8) \
                   return &ffi;_type_sint64; \
               else \
               { \
                   NSLog(@"Unknown size for type %s", #type); \
                   abort(); \
               } \
            } \
        } while(0)
```

A second macro does the same thing but for unsigned types:

```
        #define UINT(type) do { \
            if(str[0] == @encode(type)[0]) \
            { \
               if(sizeof(type) == 1) \
                   return &ffi;_type_uint8; \
               else if(sizeof(type) == 2) \
                   return &ffi;_type_uint16; \
               else if(sizeof(type) == 4) \
                   return &ffi;_type_uint32; \
               else if(sizeof(type) == 8) \
                   return &ffi;_type_uint64; \
               else \
               { \
                   NSLog(@"Unknown size for type %s", #type); \
                   abort(); \
               } \
            } \
        } while(0)
```

This one probably isn't strictly necessary, as it's unlikely to matter if the signed and unsigned variants of the `ffi_type`s are mixed, but better safe than sorry in this case.

To round out the integer macros, I have a quick one which takes an integer type and then generates code to check for both signed and unsigned variants:

```
        #define INT(type) do { \
            SINT(type); \
            UINT(unsigned type); \
        } while(0)
```

Other pre-made `ffi_type`s are named in the form `ffi_type_TYPE`, where `TYPE` is something close to the name in C. To aid in mapping other primitives, I made a macro to do the `@encode` check and then return the specified pre-made `ffi_type`:

```
        #define COND(type, name) do { \
            if(str[0] == @encode(type)[0]) \
                return &ffi_type_ ## name; \
        } while(0)
```

There are a lot of pointer types which get different `@encode` strings but which are all represented and passed in exactly the same way at the machine level. To make this a bit shorter, I wrote a short macro to check for all of the various pointer types:

```
        #define PTR(type) COND(type, pointer)
```

That takes care of all of the necessary primitives, including all types of pointers. However, it does not cover any structs.

In theory, it would be possible to support arbitrary structs by parsing the struct in the `@encode` string and building up the appropriate `ffi_type` to match. In practice, this is difficult and error-prone. The `@encode` format is not very friendly at all. To handle most cases, there are only a small number of structs that need to be translated. These structs can be detected with a simple string compare without parsing the `@encode` string, and then a simple hardcoded list of types provided to `libffi`. While this won't handle all cases, by bailing out early if an unknown struct is discovered and making it easy to add new ones, this enables the programmer to quickly fix any deficiences which may be encountered.

One last macro handles structs. It takes a struct type and a list of corresponding `ffi_type`s. If the `@encode` matches, it creates an `ffi_type` for the struct, fills out the elements from the arguments given, and returns it:

```
        #define STRUCT(structType, ...) do { \
            if(strncmp(str, @encode(structType), strlen(@encode(structType))) == 0) \
            { \
               ffi_type *elementsLocal[] = { __VA_ARGS__, NULL }; \
               ffi_type **elements = [self _allocate: sizeof(elementsLocal)]; \
               memcpy(elements, elementsLocal, sizeof(elementsLocal)); \
                \
               ffi_type *structType = [self _allocate: sizeof(*structType)]; \
               structType->type = FFI_TYPE_STRUCT; \
               structType->elements = elements; \
               return structType; \
            } \
        } while(0)
```

Now that all of the macros are in place, all that remains is to build the table. First we start with integers. In addition to the usual kinds, I also include the C99 `_Bool` type. Also note the special handling for `char`, since a plain, unqualified `char` can be either signed or unsigned:

```
        SINT(_Bool);
        SINT(signed char);
        UINT(unsigned char);
        INT(short);
        INT(int);
        INT(long);
        INT(long long);
```

Next, the various pointer types. Note that for the most part, `@encode` does not discriminate between pointer types other than a few different kinds. The `void *` case handles almost everything, and the other cases pick up the special ones:

```
        PTR(id);
        PTR(Class);
        PTR(SEL);
        PTR(void *);
        PTR(char *);
        PTR(void (*)(void));
```

Next come floating-point types and `void`, all of which have corresponding `libffi` types:

```
        COND(float, float);
        COND(double, double);
        
        COND(void, void);
```

This function is used to translate return types, not just argument types, thus the need to handle `void`.

That takes care of primitives. Now it's time for structs. I only handle `CGRect`, `CGPoint`, `CGSize`, and their NS equivalents. Others could easily be added if necessary.

These structs all have elements of type `CGFloat`. The type of `CGFloat` can either be `float` or `double` depending on the platform. The first thing to do, then, is to figure out which one it is, and grab the corresponding `ffi_type`:

```
        ffi_type *CGFloatFFI = sizeof(CGFloat) == sizeof(float) ? &ffi;_type_float : &ffi;_type_double;
```

Now that this is ready, generate code to check for the various CG types:

```
        STRUCT(CGRect, CGFloatFFI, CGFloatFFI, CGFloatFFI, CGFloatFFI);
        STRUCT(CGPoint, CGFloatFFI, CGFloatFFI);
        STRUCT(CGSize, CGFloatFFI, CGFloatFFI);
```

Then do the same for the NS versions. Since these only exist on the Mac, don't try to compile this code for iOS:

```
    #if !TARGET_OS_IPHONE
        STRUCT(NSRect, CGFloatFFI, CGFloatFFI, CGFloatFFI, CGFloatFFI);
        STRUCT(NSPoint, CGFloatFFI, CGFloatFFI);
        STRUCT(NSSize, CGFloatFFI, CGFloatFFI);
    #endif
```

That takes care of building the table of types. Each macro returns the appropriate `ffi_type *` in the event of a match. If execution reaches this far, then there were no matches. Since it's best to find out about an omission as quickly as possible, the end of the code simply logs an error and aborts:

```
        NSLog(@"Unknown encode string %s", str);
        abort();
    }
```

**Building the Closure**  
 If you're still with me, then good news: the hard parts are done! All that remains is to use these `libffi` type structures to build the closure.

When a closure is prepared, it takes three important pieces of data. One is the type information that all of the previous code worked so hard to build. One is a C function which receives the arguments in `libffi` format. The last one is a context pointer which is passed into that C function. This context pointer is what allows all of the magic to happen. It allows the function to determine which instance of `MABlockClosure` the call is associated with, and call through to the associated block.

Like with closure allocation and deallocation, how the closure is prepared depends on which mode `libffi` is operating in. If `libffi` is managing its own closure allocation, then it's just a single call to prepare the closure. Otherwise, there's a different call to set it up, and then a call to `mprotect` is required to mark the memory as executable. Here's what the `-_prepClosure` method looks like:

```
    - (void)_prepClosure
    {
    #if USE_LIBFFI_CLOSURE_ALLOC
        ffi_status status = ffi_prep_closure_loc(_closure, &_closureCIF, BlockClosure, self, _closureFptr);
        if(status != FFI_OK)
        {
            NSLog(@"ffi_prep_closure returned %d", (int)status);
            abort();
        }
    #else
        ffi_status status = ffi_prep_closure(_closure, &_closureCIF, BlockClosure, self);
        if(status != FFI_OK)
        {
            NSLog(@"ffi_prep_closure returned %d", (int)status);
            abort();
        }
        
        if(mprotect(_closure, sizeof(_closure), PROT_READ | PROT_EXEC) == -1)
        {
            perror("mprotect");
            abort();
        }
    #endif
    }
```

The `BlockClosure` function is what handles calls to the closure. It receives the `ffi_cif *` associated with the closure, a place to put a return value, an array of arguments, and a context pointer:

```
    static void BlockClosure(ffi_cif *cif, void *ret, void **args, void *userdata)
    {
        MABlockClosure *self = userdata;
```

Once it has the `MABlockClosure` instance, it can take advantage of all of the data that was previously constructed for the block. The first thing to do is to construct a new arguments array that can hold one more argument. The block goes into the first argument, and then the other arguments are copied in, shifted down by one:

```
        int count = self->_closureArgCount;
        void **innerArgs = malloc((count + 1) * sizeof(*innerArgs));
        innerArgs[0] = &self-;>_block;
        memcpy(innerArgs + 1, args, count * sizeof(*args));
```

Next, `ffi_call` is used to call the block's implementation pointer. It requires a type signature, which we already generated previously. It requires a function pointer, which the `BlockImpl` helper function can provide. It requires a place to put the return value, for which we can just pass `ret`, since the return value should simply pass through. Finally, it requires an array of arguments, which we just built up:

```
        ffi_call(&self-;>_innerCIF, BlockImpl(self->_block), ret, innerArgs);
```

The block has now been called! All that remains is to clean up the new arguments array:

```
        free(innerArgs);
    }
```

`MABlockClosure` is now fully functional.

**Convenience Functions**  
 Using `MABlockClosure` directly is slightly inconvenient. I built two convenience functions to make this a bit easier. The `BlockFptr` function creates an `MABlockClosure` instance as an associated object on the block itself. This ensures that the function pointer remains valid for as long as the block is valid:

```
    void *BlockFptr(id block)
    {
        @synchronized(block)
        {
            MABlockClosure *closure = objc_getAssociatedObject(block, BlockFptr);
            if(!closure)
            {
                closure = [[MABlockClosure alloc] initWithBlock: block];
                objc_setAssociatedObject(block, BlockFptr, closure, OBJC_ASSOCIATION_RETAIN);
                [closure release]; // retained by the associated object assignment
            }
            return [closure fptr];
        }
    }
```

This only works with blocks which are on the heap, not stack blocks, so I also built a quick `BlockFptrAuto` function which copies the block onto the heap, then returns the appropriate function pointer for that:

```
    void *BlockFptrAuto(id block)
    {
        return BlockFptr([[block copy] autorelease]);
    }
```

Finally, after all of this work, we can simply build a function pointer from a block:

```
    int x = 42;
    void (*fptr)(void) = BlockFptrAuto(^{ NSLog(@"%d", x); });
    fptr(); // prints 42!
```

**Conclusion**  
`libffi` is an extremely useful library when dealing with low-level function calls where you don't know everything about them in advance. It's especially useful when coupled with Objective-C's runtime type information. The biggest hurdle is converting between the two ways of representing type information. The code presented here shows how that can be done without too much pain, and also demonstrates how to use the facilities provided by `libffi` to get work done.

That wraps up this week's (late) Friday Q&A. Come back in two weeks for the next installment. Until then, as always, keep [sending me your ideas](mailto:mike@mikeash.com) for topics to cover here.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2011-05-06-a-tour-of-mablockclosure.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
