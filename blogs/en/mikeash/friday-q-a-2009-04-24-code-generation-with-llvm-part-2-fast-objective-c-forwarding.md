---
title: 'Friday Q&A 2009-04-24: Code Generation with LLVM, Part 2: Fast Objective-C Forwarding'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-04-24-code-generation-with-llvm-part-2-fast-objective-c-forwarding.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0a34033051ea1c9e'
translated: false
---

> 原文：[Friday Q&A 2009-04-24: Code Generation with LLVM, Part 2: Fast Objective-C Forwarding](https://www.mikeash.com/pyblog/friday-qa-2009-04-24-code-generation-with-llvm-part-2-fast-objective-c-forwarding.html)　·　mikeash.com Friday Q&A

Posted at 2009-04-24 01:35 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-05-01: On Hold](https://www.mikeash.com/pyblog/friday-qa-2009-05-01-on-hold.html)  
Previous article: [Friday Q&A 2009-04-17: Code Generation with LLVM, Part 1: Basics](https://www.mikeash.com/pyblog/friday-qa-2009-04-17-code-generation-with-llvm-part-1-basics.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [llvm](https://www.mikeash.com/pyblog/?tag=llvm)

Friday Q&A 2009-04-24: Code Generation with LLVM, Part 2: Fast Objective-C Forwarding

by [Mike Ash](https://www.mikeash.com/)

**Forwarding?**  
 If you aren't familiar with forwarding, then you'll want to read over [my post from a few weeks ago](http://www.mikeash.com/?page=pyblog/friday-qa-2009-03-27-objective-c-message-forwarding.html) that talks about it. Quickie version: forwarding lets you capture a method invocation and then bend it to your will.

Forwarding is really cool and powerful. Trouble is that it's also slow. A forwarded message send is about a thousand times slower than a direct one.

This should come as no surprise. After all, you perform forwarding by implementing `-(void)forwardInvocation:(NSInvocation *)invocation` That's an object parameter, one which has to be freshly created. The arguments have to be parsed from the method signature, then marshalled and loaded into the invocation object. Then to make the call, the arguments have to be marshalled out of the invocation object and into the right places to make the call. All of this takes a significant amount of time.

**Higher-Order Messaging**  
 My LLVM demonstration will involve implementing higher-order messaging, so you'd better know what that is. Cocoadev.com has [a thorough explanation](http://cocoadev.com/index.pl?HigherOrderMessaging). The short version is that it's a technique for nested messaging which uses the outer message as an argument to the inner one. Consider this code:

```
   NSArray *result = [[array map] stringByAppendingString:@"suffix"];
```

What this code will do is iterate through the array, invoke `stringByAppendingString:@"suffix"` on every element, and return a new array containing the results. The `map` call is the higher-order message, and `stringByAppendingString:@"suffix"` serves as its argument. This is pretty neat stuff and is an interesting demonstration of the power of Objective-C.

How does it work? It's actually quite straightforward. `map` is defined in a category on NSArray and returns an instance of an `NSProxy` subclass. That proxy then implemets `-forwardInvocation:` to do the work of iterating and returning the new array. Here's the full source code for my minimal proxy that implements this:

```
    @interface ArrayMapProxyNormal : NSProxy
    {
        NSArray *_array;
    }
    - (id)initWithArray:(NSArray *)array;
    @end
    @implementation ArrayMapProxyNormal
    - (id)initWithArray:(NSArray *)array
    {
        _array = array;
        return self;
    }
    - (NSMethodSignature *)methodSignatureForSelector:(SEL)sel
    {
        return [[_array lastObject] methodSignatureForSelector:sel];
    }
    - (void)forwardInvocation:(NSInvocation *)inv
    {
        NSMutableArray *newArray = [NSMutableArray array];
        for(id obj in _array)
        {
            id retval;
            [inv invokeWithTarget:obj];
            [inv getReturnValue:&retval;];
            [newArray addObject:retval];
        }
        [inv setReturnValue:&newArray;];
    }
    @end
```

"Normal" here in contrast to the fancy LLVM solution that's coming up. For completeness, here's the `mapNormal` method on NSArray:

```
    - (id)mapNormal
    {
        return [[[ArrayMapProxyNormal alloc] initWithArray:self] autorelease];
    }
```

Not too much to it.

But, as mentioned, forwarding is slow. How can we make it faster?

**Dynamic Methods**  
 This technique gets kind of slow because it has to go through the forwarding path, which as mentioned, is very slow by itself. `NSInvocation` is expensive to build and expensive to invoke.

For the `stringByAppendingString:` example, we could special case that and speed it up by implementing it directly:

```
    - (id)stringByAppendingString:(NSString *)string
    {
        NSMutableArary *newArray = [NSMutableArary array];
        for(id obj in _array)
            [newArray addObject:[obj stringByAppendingString:string]];
        return newArray;
    }
```

That gets rid of the forwarding and invocation overhead. Trouble is, of course, that we'd have to anticipate and reimplement every possible method in advance. That's just not practical.

LLVM to the rescue! Using LLVM we can implement nothing, and see what gets used at runtime. The forwarding mechanism will get the first message. The proxy can then generate the appropriate method dynamically, add it to the class, and "forward" the invocation to itself. Subsequent messages will go straight through. This is what the `forwardImplementation:` implementation looks like from the LLVM proxy:

```
    - (void)forwardInvocation:(NSInvocation *)inv
    {
        SEL sel = [inv selector];
        id obj = [_array lastObject];
        Method method = class_getInstanceMethod(object_getClass(obj), sel);
        NSParameterAssert(method);
        
        const char *types = method_getTypeEncoding(method);
        NSMethodSignature *sig = [NSMethodSignature signatureWithObjCTypes:types];
        NSParameterAssert([sig methodReturnType][0] == '@');
        
        class_addMethod([self class],
                        sel,
                        [[self class] _trampolineMethodForSignature:sig selector:sel],
                        types);
        [inv invoke];
    }
```

Mostly straightforward stuff there. We get the metadata for the method from an object in the array, and then add a new method to our class. At the end we re-invoke the invocation, which causes it to go back to `self` and hit the newly-added method. The one tricky bit is the `_trampolineMethodForSignature:selector:` call. And that is a _very_ tricky bit indeed!

**Building the Code**  
 If you'd like to see the entire program at once instead of bit by bit, you can [get it here](https://www.mikeash.com/pyblog/llvmhom.mm).

In order to simplify the LLVM-generated method, I'm going to push most of the iteration into Objective-C. Using fast enumeration would make things go even faster, but I'm not up to building that in LLVM intermediate code.

As such, the generated method will do the equivalent of this:

```
    - (id)trampoline
    {
        NSMutableArray *array = [NSMutableArray array];
        id obj;
        while((obj = [self _nextObject]))
            [array addObject:[obj trampoline]];
        return array;
    }
```

Except that the generated method will take and pass parameters depending on what we tell it to use. By using this template, the `_nextObject` method can be written in Objective-C, simplifying the job.

There's a lot of support structure that's needed before we can actually start building methods. First, we need to create an LLVM module and execution engine:

```
    static ExecutionEngine *ArrayMapProxyLLVMEngine;
    
    // requires explicit namespace due to conflict with objc header Module type
    static llvm::Module *ArrayMapProxyLLVMModule;
    
    + (void)initialize
    {
        ArrayMapProxyLLVMModule = new llvm::Module("ArrayMapProxyLLVMDynamic");
        ArrayMapProxyLLVMEngine = ExecutionEngine::create(ArrayMapProxyLLVMModule);
    }
```

We'll also define a method for printing the module, handy for debugging:

```
    + (void)printModule
    {
        PassManager PM;
        ModulePass *pmp = createPrintModulePass(&outs;());
        PM.add(pmp);
        PM.run(*ArrayMapProxyLLVMModule);
    }
```

Next, I define a bunch of convenience functions for creating LLVM types corresponding to `int`, `char`, and various pointer types. For `id` and `SEL` I cheated a bit and defined them as `char *`. Since they're never dereferenced it doesn't really matter.

```
    static const IntegerType *intType(void)
    {
        return IntegerType::get(sizeof(int) * CHAR_BIT);
    }
    
    static const IntegerType *charType(void)
    {
        return IntegerType::get(CHAR_BIT);
    }
    
    static const IntegerType *intptrType(void)
    {
        return IntegerType::get(sizeof(void *) * CHAR_BIT);
    }
    
    static const PointerType *idType(void)
    {
        return PointerType::getUnqual(charType());
    }
    
    static const PointerType *selType(void)
    {
        return PointerType::getUnqual(charType());
    }
```

Another important piece of infrastructure is code to go from an Objective-C type string to an LLVM type. We get the method argument types as C strings that conform to the `@encode` directive, but LLVM obviously expects values of its own `Type` class. This function maps from the one to the other:

```
    static const Type *LLVMTypeForObjCType(const char *type)
    {
    #define IF_ISTYPE(t) if(strcmp(@encode(t), type) == 0)
    #define INT_TYPE(t) IF_ISTYPE(t) return IntegerType::get(sizeof(t) * CHAR_BIT)
    #define PTR_TYPE(t) IF_ISTYPE(t) return PointerType::getUnqual(charType())
        INT_TYPE(char);
        INT_TYPE(short);
        INT_TYPE(int);
        INT_TYPE(long);
        INT_TYPE(long long);
        INT_TYPE(unsigned char);
        INT_TYPE(unsigned short);
        INT_TYPE(unsigned int);
        INT_TYPE(unsigned long);
        INT_TYPE(unsigned long long);
        IF_ISTYPE(float) return Type::FloatTy;
        IF_ISTYPE(double) return Type::DoubleTy;
        IF_ISTYPE(void) return Type::VoidTy;
        PTR_TYPE(char *);
        PTR_TYPE(id);
        PTR_TYPE(SEL);
        PTR_TYPE(Class);
        if(type[0] == '^') return PointerType::getUnqual(charType());
        
        return NULL;
    }
```

You'll note that there is absolutely no handling of any `struct` types. That was simply too involved and I didn't bother trying to implement it. It certainly could be done, but it would require considerably greater sophistication.

I need to refer to selectors and classes within the generated function, so here are convenience functions that take a `SEL` or a `Class` and generate an LLVM constant with that value:

```
    static Value *PtrValue(void *ptr, IRBuilder<> &builder, const Type *type, const char *name)
    {
        Value *intv = ConstantInt::get(intptrType(), (int64_t)ptr, 0);
        return builder.CreateIntToPtr(intv, type, name);
    }
    
    static Value *SELValue(SEL sel, IRBuilder<> &builder)
    {
        return PtrValue(sel, builder, selType(), sel_getName(sel));
    }
    
    static Value *ClassValue(Class c, IRBuilder<> &builder)
    {
        return PtrValue(c, builder, idType(), class_getName(c));
    }
```

This would never fly in a "real" code generator, because those pointers aren't guaranteed to remain fixed from one run to the next. But even though we're ultimately generating real machine code, we're still operating at runtime. Since those values can't change during the lifetime of the process there's no harm in embedding those values right into the code.

One more convenience function, this one for getting an LLVM `Function *` corresponding to `objc_msgSend`. This is actually pretty simple. By creating a function with that name, LLVM will automatically look it up as a C function within the process if no function with that name exists in the LLVM module. All we have to do is declare its parameter and return types correctly, and LLVM will call out to it.

```
    static Function *ObjcMsgSendFunction(void)
    {
        static Function *f;
        if(!f)
        {
            std::vector<const Type *> msgSendArgTypes;
            msgSendArgTypes.push_back(idType());
            msgSendArgTypes.push_back(selType());
            FunctionType *msgSendType = FunctionType::get(idType(), msgSendArgTypes, true);
            f = Function::Create(msgSendType,
                                 Function::ExternalLinkage,
                                 "objc_msgSend",
                                 ArrayMapProxyLLVMModule);
        }
        return f;
    }
```

That's all the infrastructure needed, now let's actually build the method.

**Building the Method**  
 So again, the generated method is supposed to look like this:

```
    - (id)trampoline
    {
        NSMutableArray *array = [NSMutableArray array];
        id obj;
        while((obj = [self _nextObject]))
            [array addObject:[obj trampoline]];
        return array;
    }
```

Except that arguments will be added as needed to fit the method signature of the target. And of course [we all know](https://www.mikeash.com/pyblog/friday-qa-2009-03-20-objective-c-messaging.html) that this really is a function that looks like this:

```
    id Trampoline(id self, SEL _cmd, ...)
    {
        NSMutableArray *array = [NSMutableArray array];
        id obj;
        while((obj = [self _nextObject]))
            [array addObject:objc_msgSend(obj, _cmd, ...)];
        return array;
    }
```

With the `...` replaced by the arguments in question. With our target in mind, let's code.

We'll need method which generates the LLVM `Function *` for this function:

```
    + (Function *)_trampolineFunctionForSignature:(NSMethodSignature *)sig selector:(SEL)sel
    {
```

The first thing this method does is build a vector of argument types, using the helper function I showed earlier to translate the `NSMethodSignature` into LLVM types:

```
        std::vector<const Type *> methodArgTypes;
        for(unsigned i = 0; i < [sig numberOfArguments]; i++)
            methodArgTypes.push_back(LLVMTypeForObjCType([sig getArgumentTypeAtIndex:i]));
```

Then we'll create the `Function` object and extract the arguments, just like last week:

```
        const Type *methodReturnType = LLVMTypeForObjCType([sig methodReturnType]);
        FunctionType *trampolineType = FunctionType::get(methodReturnType, methodArgTypes, false);
        Function *trampoline = (Function *)ArrayMapProxyLLVMModule->getOrInsertFunction(
            [NSStringFromSelector(sel) UTF8String],
            trampolineType);
        trampoline->setCallingConv(CallingConv::C);
        
        // get the 'self' and '_cmd' args as values, and name them
        // the rest we don't care about except to pass them along
        Function::arg_iterator args = trampoline->arg_begin();
        Value *selfarg = args++;
        selfarg->setName("self");
        Value *_cmdarg = args++;
        _cmdarg->setName("_cmd");
```

The next thing to do is to set up the `BasicBlock` objects that this function will contain. That means breaking down the model C code into something a little more low level. Essentially, the function should look like this:

```
    entry:
     set up selectors
     array = [NSMutableArray array];
     go to loopstart
    loopstart:
     obj = [self _nextObject]
     if obj == nil then go to return
     else go to loopbody
    loopbody:
     result = [obj trampoline]
     [array addObject:result];
     goto loopstart
    return:
     return array
```

Thus we can see that we'll need four basic blocks:

```
        BasicBlock *entry = BasicBlock::Create("entry", trampoline);
        BasicBlock *loopstart = BasicBlock::Create("loopstart", trampoline);
        BasicBlock *loopbody = BasicBlock::Create("loopbody", trampoline);
        BasicBlock *ret = BasicBlock::Create("return", trampoline);
```

We'll also take the opportunity to do some more setup here. We need the `Function` object for `objc_msgSend` since we'll be doing several of those, and we'll also get the selectors for messaging set up:

```
        Function *msgsend = ObjcMsgSendFunction();
        
        IRBuilder<> builder(entry);
        Value *arraySEL = SELValue(@selector(array), builder);
        Value *addObjectSEL = SELValue(@selector(addObject:), builder);
        Value *nextObjectSEL = SELValue(@selector(_nextObject), builder);
```

Now we can actually start making calls. We already know how to call functions from last week. We know how an Objective-C message translates into a C function call. We have a helper function to push an Objective-C `Class` pointer into LLVM code. All the pieces are therefore set to make the call to `[NSMutableArray array]`:

```
        Value *nsmutablearray = ClassValue([NSMutableArray class], builder);
        Value *array = builder.CreateCall2(msgsend, nsmutablearray, arraySEL, "array");
```

Easier than I made it sound, huh? Last step, unconditionally branch to the `loopstart` block:

```
        builder.CreateBr(loopstart);
```

Next, fill in `loopstart`. This is just a message send and then an if statement, nothing we don't already know how to do. The one tricky thing here is casting the pointer to an integer before comparing it with zero. There may be a better way to do this, but this way works....

```
        builder.SetInsertPoint(loopstart);
        Value *nextObject = builder.CreateCall2(msgsend, selfarg, nextObjectSEL, "nextObject");
        
        Value *nextObjectInt = builder.CreatePtrToInt(nextObject, intptrType(), "nextObjectInt");
        Constant *zero = ConstantInt::get(intType(), 0, 1);
        Value *nextObjectIsNil = builder.CreateICmpEQ(nextObjectInt, zero, "nextObjectIsNil");
        builder.CreateCondBr(nextObjectIsNil, ret, loopbody);
```

Next, `loopbody`. Everything is straightforward here. The only tricky bit is dynamically generating the arguments for the trampoline call. This isn't particularly hard: we just copy the original arguments vector, but put `nextObject` in place of `self`. After that, a standard call to `objc_msgSend`, then a branch back to `loopstart`:

```
        builder.SetInsertPoint(loopbody);
        Function::arg_iterator methodArgs = trampoline->arg_begin();
        std::vector<Value *> msgsendArgs;
        msgsendArgs.push_back(nextObject); methodArgs++;
        while(methodArgs != trampoline->arg_end())
            msgsendArgs.push_back(methodArgs++);
        Value *result = builder.CreateCall(msgsend,
                                           msgsendArgs.begin(),
                                           msgsendArgs.end(),
                                           "result");
        builder.CreateCall3(msgsend, array, addObjectSEL, result);
        builder.CreateBr(loopstart);
```

That's pretty much the whole function. Only the return block is left, and all that has to do is return the array we've built:

```
        builder.SetInsertPoint(ret);
        builder.CreateRet(array);
```

Then just return the `Function`:

```
        return trampoline;
    }
```

In addition to this, I'm also going to introduce something else new: optimization. Turns out that running optimizations in LLVM is, like most of the rest, surprisingly easy. A `FunctionPassManager` object manages passes. Add some optimization passes, then run the pass manager on the function, and it's optimized:

```
    + (void)_optimizeFunction:(Function *)f
    {
        static FunctionPassManager *fpm;
        if(!fpm)
        {
            ExistingModuleProvider *moduleProvider = new ExistingModuleProvider(ArrayMapProxyLLVMModule);
            fpm = new FunctionPassManager(moduleProvider);
            
            fpm->add(new TargetData(*ArrayMapProxyLLVMEngine->getTargetData()));
            fpm->add(createInstructionCombiningPass());
            fpm->add(createReassociatePass());
            fpm->add(createGVNPass());
            fpm->add(createCFGSimplificationPass());
        }
        
        fpm->run(*f);
    }
```

Now all the pieces are in place for the really short `+_trampolineMethodForSignature:selector:`method:

```
    + (IMP)_trampolineMethodForSignature:(NSMethodSignature *)sig selector:(SEL)sel
    {
        Function *f = [self _trampolineFunctionForSignature:sig selector:sel];
        [self _optimizeFunction:f];
        return (IMP)ArrayMapProxyLLVMEngine->getPointerToFunction(f);
    }
```

And for completeness, the implementation of `-_nextObject`:

```
    - (id)_nextObject
    {
        return (_index < _count
                ? (id)CFArrayGetValueAtIndex((CFArrayRef)_array, _index++)
                : nil);
    }
```

**Performance Testing**  
 In order to see how fast the LLVM version went (and make sure that it actually worked!) I built a little test harness:

```
    @interface NSString (NOP)
    - (id)nop;
    - (id)nop:(int)x :(int)y :(int)z;
    @end
    @implementation NSString (Logging)
    - (id)nop { return self; }
    - (id)nop:(int)x :(int)y :(int)z
    {
        NSParameterAssert(x == 1 && y == 2 && z == 3);
        return self;
    }
    @end
    
    
    #define TIME(expr) do { \
        fprintf(stderr, "testing %s...", #expr); \
        /* let stuff happen a few times first for caching etc. */ \
        for(int i = 0; i < 10; i++) expr; \
        \
        NSTimeInterval totalTime = 0; \
        int iterations = 1; \
        while(totalTime < 5 && iterations < 2000000000) \
        { \
            iterations *= 5; \
            NSTimeInterval start = [NSDate timeIntervalSinceReferenceDate]; \
            NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init]; \
            for(int i = 0; i < iterations; i++) \
            { \
                expr; \
                if(!(i & 0xFF)) \
                { \
                    [pool release]; \
                    pool = [[NSAutoreleasePool alloc] init]; \
                } \
            } \
            [pool release]; \
            NSTimeInterval end = [NSDate timeIntervalSinceReferenceDate]; \
            totalTime = end - start; \
        } \
        fprintf(stderr, " %fus/call\n", totalTime * 1000000.0 / iterations); \
    } while(0)
    
    int main(int argc, char **argv)
    {
        NSAutoreleasePool *pool = [NSAutoreleasePool new];
        
        NSArray *reallySmallTimeTestArray = [NSArray arrayWithObject: @"0"];
        NSMutableArray *smallTimeTestArray = [NSMutableArray array];
        for(int i = 0; i < 10; i++)
            [smallTimeTestArray addObject:[NSString stringWithFormat:@"%d", i]];
            
        NSMutableArray *largeTimeTestArray = [NSMutableArray array];
        for(int i = 0; i < 10000; i++)
            [largeTimeTestArray addObject:[NSString stringWithFormat:@"%d", i]];
        
        TIME([[reallySmallTimeTestArray mapLLVM] nop]);
        TIME([[reallySmallTimeTestArray mapNormal] nop]);
        TIME([[reallySmallTimeTestArray mapLLVM] nop:1 :2 :3]);
        TIME([[reallySmallTimeTestArray mapNormal] nop:1 :2 :3]);
        
        TIME([[smallTimeTestArray mapLLVM] nop]);
        TIME([[smallTimeTestArray mapNormal] nop]);
        TIME([[smallTimeTestArray mapLLVM] nop:1 :2 :3]);
        TIME([[smallTimeTestArray mapNormal] nop:1 :2 :3]);
        
        TIME([[largeTimeTestArray mapLLVM] nop]);
        TIME([[largeTimeTestArray mapNormal] nop]);
        TIME([[largeTimeTestArray mapLLVM] nop:1 :2 :3]);
        TIME([[largeTimeTestArray mapNormal] nop:1 :2 :3]);
        
        [pool release];
        return 0;
    }
```

**Results**  
 So how did it do? Here are the results from my Mac Pro:

```
    testing [[reallySmallTimeTestArray mapLLVM] nop]... 1.450171us/call
    testing [[reallySmallTimeTestArray mapNormal] nop]... 8.171945us/call
    testing [[reallySmallTimeTestArray mapLLVM] nop:1 :2 :3]... 1.496475us/call
    testing [[reallySmallTimeTestArray mapNormal] nop:1 :2 :3]... 9.091927us/call
    testing [[smallTimeTestArray mapLLVM] nop]... 3.219738us/call
    testing [[smallTimeTestArray mapNormal] nop]... 15.972872us/call
    testing [[smallTimeTestArray mapLLVM] nop:1 :2 :3]... 3.471767us/call
    testing [[smallTimeTestArray mapNormal] nop:1 :2 :3]... 17.267069us/call
    testing [[largeTimeTestArray mapLLVM] nop]... 2263.705921us/call
    testing [[largeTimeTestArray mapNormal] nop]... 8524.912024us/call
    testing [[largeTimeTestArray mapLLVM] nop:1 :2 :3]... 2592.695684us/call
    testing [[largeTimeTestArray mapNormal] nop:1 :2 :3]... 8722.084808us/call
```

In short, it ranges from about 6 times faster for the one-element array case to a bit over 3 times faster for really long arrays. The difference is not surprising: much of the cost of standard forwarding is in building the invocation object, something that only happens once for the entire array. For long arrays, that cost is amortized into nonexistence, and we only pay the cost of invoking the `NSInvocation`, which is expensive but not as much.

Both techniques also pay a cost for allocating a proxy, allocating an array, and filling that array. While this hurts both equally, it reduces the relative advantage of the LLVM solution.

Finally, the forwarding solution has the advantage of using fast enumeration. This is unimportant for the small array but hurts for the big one. Redoing the LLVM code to use fast enumeration is entirely doable, of course, but would make the code more complicated.

It's also interesting to watch how the argument marshalling cost hits traditional forwarding with the really short array. An method with 3 arguments takes over 10% longer to map onto a 1-element array than a method with no arguments. Meanwhile LLVM map pays only about 3% for the extra arguments, since they're essentially hardcoded.

Conclusion: up to a 6x speedup, pretty cool!

**Limitations and Improvements**  
 This LLVM forwarding stuff is neat, but it could be better. Here are some areas where it could use work, if you feel like tinkering:

1. **Fast enumeration:** I've probably mentioned this about sixteen times already, but it would definitely help with speed.
2. **Caching functions:** Right now, the implementation generates a new function for every selector. This is wasteful, because many selectors will have the same signature, and can reuse the same function. A cache that allows reusing functions for different selectors with the same method signature would cut down on overhead.
3. **Zero-size arrays:** This implementation simply explodes on empty arrays if the selector has never been seen before, because there's no object to get a method signature from to generate the function, but `map` shouldn't break just because it's used on an empty array.
4. **Struct support:** This one is a little scary, but writing some code that can properly generate an LLVM struct definition from an Objective-C type string would be nifty.

**Conclusion**  
 That wraps up my two week series on runtime code generation with LLVM. In [the first week](http://www.mikeash.com/?page=pyblog/friday-qa-2009-04-17-code-generation-with-llvm-part-1-basics.html) I showed how to get basic code generation up and running with LLVM, then this week you saw how to take that and actually make it do something useful within an Objective-C program.

LLVM is a tremendously cool project and this kind of runtime code generation is extremely powerful. This dynamic fast forwarding implementation barely scratches the surface of the kinds of interesting things you can do.

Questions? Comments? Dares? Post them all below.

Don't forget that Friday Q&A is driven by your suggestions. Do you have a topic you'd like to see discussed here? If so, [e-mail](mailto:mike@mikeash.com), [tweet](http://twitter.com/mikeash), or post it in the comments. (And be sure to tell me explicitly if you want to remain anonymous.)

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-04-24-code-generation-with-llvm-part-2-fast-objective-c-forwarding.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
