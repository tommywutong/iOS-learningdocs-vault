---
title: 'Friday Q&A 2009-04-24：使用 LLVM 生成代码，第 2 部分：快速的 Objective-C 转发'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-04-24-code-generation-with-llvm-part-2-fast-objective-c-forwarding.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0a34033051ea1c9e'
translated: true
---

> 原文：[Friday Q&A 2009-04-24: Code Generation with LLVM, Part 2: Fast Objective-C Forwarding](https://www.mikeash.com/pyblog/friday-qa-2009-04-24-code-generation-with-llvm-part-2-fast-objective-c-forwarding.html)　·　mikeash.com Friday Q&A

发表于 2009-04-24 01:35 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([全文 feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2009-05-01：暂停](https://www.mikeash.com/pyblog/friday-qa-2009-05-01-on-hold.html)  
上一篇：[Friday Q&A 2009-04-17：使用 LLVM 生成代码，第 1 部分：基础](https://www.mikeash.com/pyblog/friday-qa-2009-04-17-code-generation-with-llvm-part-1-basics.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [llvm](https://www.mikeash.com/pyblog/?tag=llvm)

Friday Q&A 2009-04-24：使用 LLVM 生成代码，第 2 部分：快速的 Objective-C 转发

作者：[Mike Ash](https://www.mikeash.com/)

**转发？**  
如果你不熟悉转发，那么你需要阅读一下[我几周前的文章](http://www.mikeash.com/?page=pyblog/friday-qa-2009-03-27-objective-c-message-forwarding.html)，其中对此进行了讨论。快速版本：转发让你能够捕获一个方法调用，然后按照你的意愿对其进行处理。

转发非常酷且强大。问题在于它也很慢。一次转发的消息发送比直接消息发送慢大约一千倍。

这并不令人惊讶。毕竟，你是通过实现 `-(void)forwardInvocation:(NSInvocation *)invocation` 来执行转发的。这是一个对象参数，而且必须被新创建出来。参数必须从方法签名中解析，然后被整理并加载到 invocation 对象中。然后，为了进行调用，参数又必须从 invocation 对象中取出并放到正确的位置。所有这些都需要花大量时间。

**高阶消息**  
我的 LLVM 演示将涉及实现高阶消息，所以你最好了解它是什么。Cocoadev.com 上有一个[详细的解释](http://cocoadev.com/index.pl?HigherOrderMessaging)。简而言之，它是一种用于嵌套消息的技术，它将外层消息作为内层消息的参数。考虑以下代码：

```
   NSArray *result = [[array map] stringByAppendingString:@"suffix"];
```

这段代码的作用是遍历该 array，对每个元素调用 `stringByAppendingString:@"suffix"`，并返回一个包含结果的新 array。`map` 调用就是高阶消息，而 `stringByAppendingString:@"suffix"` 作为它的参数。这非常巧妙，是 Objective-C 能力的一个有趣展示。

它是如何工作的？实际上非常简单。`map` 是在 NSArray 的一个分类（category）中定义的，并返回一个 `NSProxy` 子类（subclass）的实例。然后该代理实现 `-forwardInvocation:` 来完成遍历并返回新 array 的工作。以下是我实现此功能的最小代理的完整源代码：

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

这里的"Normal"是相对于接下来将要介绍的奇妙的 LLVM 解决方案而言的。为了完整性，这里是 NSArray 上的 `mapNormal` 方法：

```
    - (id)mapNormal
    {
        return [[[ArrayMapProxyNormal alloc] initWithArray:self] autorelease];
    }
```

没什么特别的。

但是，如前所述，转发很慢。我们怎样才能让它更快呢？

**动态方法**  
这种技术变慢是因为它必须经过转发路径，而如前所述，转发路径本身非常慢。构建和调用 `NSInvocation` 的代价很高。

对于 `stringByAppendingString:` 这个例子，我们可以特殊处理，通过直接实现它来加速：

```
    - (id)stringByAppendingString:(NSString *)string
    {
        NSMutableArary *newArray = [NSMutableArary array];
        for(id obj in _array)
            [newArray addObject:[obj stringByAppendingString:string]];
        return newArray;
    }
```

这消除了转发和 invocation 的开销。当然，问题在于我们必须事先预测并重新实现每一个可能的方法，这并不现实。

LLVM 来拯救！使用 LLVM，我们可以什么都不实现，然后在运行时查看哪些方法被使用了。转发机制会捕获第一条消息。然后代理可以动态生成适当的方法，将其添加到类中，并把这个"转发"调用重定向到自身。后续的消息就会直接通过。以下是 LLVM 代理中 `forwardImplementation:` 的实现：

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

这里大部分都很直接。我们从 array 中的一个对象获取方法的元数据，然后向我们的类添加一个新方法。最后，我们重新调用该 invocation，这会导致它回到 `self` 并命中刚刚添加的方法。一个棘手的地方是 `_trampolineMethodForSignature:selector:` 调用。而这确实是一个非常棘手的部分！

**构建代码**  
如果你想一次性看到整个程序，而不是一点一点地看，你可以[在这里获取](https://www.mikeash.com/pyblog/llvmhom.mm)。

为了简化 LLVM 生成的方法，我将把大部分迭代工作推入 Objective-C。使用快速枚举会让事情运行得更快，但我还没准备好在 LLVM 中间代码中构建它。

因此，生成的方法将执行相当于以下代码的功能：

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

只不过生成的方法会根据我们告诉它使用的参数来接收和传递参数。通过使用这个模板，`_nextObject` 方法可以用 Objective-C 编写，从而简化工作。

在我们可以真正开始构建方法之前，需要大量的支持结构。首先，我们需要创建一个 LLVM module 和一个执行引擎：

```
    static ExecutionEngine *ArrayMapProxyLLVMEngine;
    
    // 需要显式命名空间，因为与 objc 头文件中的 Module 类型冲突
    static llvm::Module *ArrayMapProxyLLVMModule;
    
    + (void)initialize
    {
        ArrayMapProxyLLVMModule = new llvm::Module("ArrayMapProxyLLVMDynamic");
        ArrayMapProxyLLVMEngine = ExecutionEngine::create(ArrayMapProxyLLVMModule);
    }
```

我们还将定义一个用于打印 module 的方法，方便调试：

```
    + (void)printModule
    {
        PassManager PM;
        ModulePass *pmp = createPrintModulePass(&outs;());
        PM.add(pmp);
        PM.run(*ArrayMapProxyLLVMModule);
    }
```

接下来，我定义了一堆方便函数，用于创建对应 `int`、`char` 和各种指针类型的 LLVM 类型。对于 `id` 和 `SEL`，我稍微偷了点懒，将它们定义为 `char *`。因为它们永远不会被解引用，所以这其实无所谓。

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

另一个重要的基础设施是，将 Objective-C 类型字符串转换为 LLVM 类型的代码。我们以符合 `@encode` 指令的 C 字符串形式获取方法参数类型，但 LLVM 显然期望的是它自己的 `Type` 类的值。这个函数负责两者之间的映射：

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

你会注意到，这里完全没有处理任何 `struct` 类型。那太复杂了，我不想费劲去实现它。当然可以做到，但这需要相当的复杂度。

我需要在生成的函数中引用选择器（selector）和类，所以这里有一些方便函数，它们接受一个 `SEL` 或 `Class`，并生成一个带有该值的 LLVM 常量：

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

这在"真正的"代码生成器中是行不通的，因为这些指针不能保证在每次运行之间保持不变。但是，即使我们最终生成的是真正的机器码，我们仍然是在运行时操作。因为这些值在进程的生命周期内不会改变，所以将这些值直接嵌入代码中是没有问题的。

还有一个方便函数，用于获取对应于 `objc_msgSend` 的 LLVM `Function *`。这实际上非常简单。通过创建具有该名称的函数，如果 LLVM module 中不存在同名函数，LLVM 会自动将其作为进程中的 C 函数进行查找。我们所要做的就是正确声明其参数和返回类型，然后 LLVM 就会调用它。

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

这就是所有需要的基础设施，现在让我们实际构建方法。

**构建方法**  
再次强调，生成的方法应该看起来像这样：

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

只不过会根据目标方法的签名按需添加参数。当然，[我们都知道](https://www.mikeash.com/pyblog/friday-qa-2009-03-20-objective-c-messaging.html)这实际上是一个看起来像这样的函数：

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

其中 `...` 被相关的参数替换。带着我们的目标，让我们开始编码。

我们将需要一个方法来为此函数生成 LLVM `Function *`：

```
    + (Function *)_trampolineFunctionForSignature:(NSMethodSignature *)sig selector:(SEL)sel
    {
```

此方法首先构建一个参数类型向量，使用我之前展示的辅助函数将 `NSMethodSignature` 转换为 LLVM 类型：

```
        std::vector<const Type *> methodArgTypes;
        for(unsigned i = 0; i < [sig numberOfArguments]; i++)
            methodArgTypes.push_back(LLVMTypeForObjCType([sig getArgumentTypeAtIndex:i]));
```

然后我们创建 `Function` 对象并提取参数，就像上周一样：

```
        const Type *methodReturnType = LLVMTypeForObjCType([sig methodReturnType]);
        FunctionType *trampolineType = FunctionType::get(methodReturnType, methodArgTypes, false);
        Function *trampoline = (Function *)ArrayMapProxyLLVMModule->getOrInsertFunction(
            [NSStringFromSelector(sel) UTF8String],
            trampolineType);
        trampoline->setCallingConv(CallingConv::C);
        
        // 获取 'self' 和 '_cmd' 参数作为值，并命名它们
        // 其余的我们不需要关心，除了要将它们传递下去
        Function::arg_iterator args = trampoline->arg_begin();
        Value *selfarg = args++;
        selfarg->setName("self");
        Value *_cmdarg = args++;
        _cmdarg->setName("_cmd");
```

接下来要做的是设置此函数将包含的 `BasicBlock` 对象。这意味着要将模型 C 代码分解成更底层的结构。本质上，函数应如下所示：

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

因此我们可以看到我们需要四个基本块：

```
        BasicBlock *entry = BasicBlock::Create("entry", trampoline);
        BasicBlock *loopstart = BasicBlock::Create("loopstart", trampoline);
        BasicBlock *loopbody = BasicBlock::Create("loopbody", trampoline);
        BasicBlock *ret = BasicBlock::Create("return", trampoline);
```

我们也将借此机会做更多设置。我们需要 `objc_msgSend` 的 `Function` 对象，因为我们会多次调用它，并且我们也会设置消息传递的选择器：

```
        Function *msgsend = ObjcMsgSendFunction();
        
        IRBuilder<> builder(entry);
        Value *arraySEL = SELValue(@selector(array), builder);
        Value *addObjectSEL = SELValue(@selector(addObject:), builder);
        Value *nextObjectSEL = SELValue(@selector(_nextObject), builder);
```

现在我们可以实际开始进行调用了。我们从上周已经知道如何调用函数。我们知道 Objective-C 消息如何转换为 C 函数调用。我们有一个辅助函数可以将 Objective-C `Class` 指针推入 LLVM 代码。因此，所有要素都已就绪，可以进行对 `[NSMutableArray array]` 的调用：

```
        Value *nsmutablearray = ClassValue([NSMutableArray class], builder);
        Value *array = builder.CreateCall2(msgsend, nsmutablearray, arraySEL, "array");
```

比我说得听起来要简单，对吧？最后一步，无条件分支到 `loopstart` 块：

```
        builder.CreateBr(loopstart);
```

接下来，填充 `loopstart`。这只是一个消息发送加上一个 if 语句，没有什么是我们不知道如何做的。这里唯一的棘手之处是在与零比较之前将指针转换为整数。可能有更好的方法，但这种方法有效……

```
        builder.SetInsertPoint(loopstart);
        Value *nextObject = builder.CreateCall2(msgsend, selfarg, nextObjectSEL, "nextObject");
        
        Value *nextObjectInt = builder.CreatePtrToInt(nextObject, intptrType(), "nextObjectInt");
        Constant *zero = ConstantInt::get(intType(), 0, 1);
        Value *nextObjectIsNil = builder.CreateICmpEQ(nextObjectInt, zero, "nextObjectIsNil");
        builder.CreateCondBr(nextObjectIsNil, ret, loopbody);
```

接下来，`loopbody`。这里的一切都很直接。唯一棘手的一点是动态生成 trampoline 调用的参数。这并不特别困难：我们只需复制原始参数向量，但将 `nextObject` 放在 `self` 的位置上。之后，是一个标准的 `objc_msgSend` 调用，然后分支回 `loopstart`：

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

函数主体基本就这些了。只剩下 return 块，它所需要做的就是返回我们构建的 array：

```
        builder.SetInsertPoint(ret);
        builder.CreateRet(array);
```

然后返回 `Function`：

```
        return trampoline;
    }
```

除此之外，我还要引入一些新东西：优化。事实证明，在 LLVM 中运行优化，就像其他大部分事情一样，出奇地简单。一个 `FunctionPassManager` 对象管理多个 pass。添加一些优化 pass，然后在该函数上运行 pass 管理器，它就被优化了：

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

现在所有部分都已就位，用于实现非常简短的 `+_trampolineMethodForSignature:selector:` 方法：

```
    + (IMP)_trampolineMethodForSignature:(NSMethodSignature *)sig selector:(SEL)sel
    {
        Function *f = [self _trampolineFunctionForSignature:sig selector:sel];
        [self _optimizeFunction:f];
        return (IMP)ArrayMapProxyLLVMEngine->getPointerToFunction(f);
    }
```

为了完整性，这里是 `-_nextObject` 的实现：

```
    - (id)_nextObject
    {
        return (_index < _count
                ? (id)CFArrayGetValueAtIndex((CFArrayRef)_array, _index++)
                : nil);
    }
```

**性能测试**  
为了查看 LLVM 版本有多快（并确保它确实有效！），我构建了一个小的测试工具：

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
        /* 先让事情发生几次以进行缓存等 */ \
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

**结果**  
那么它的表现如何？以下是我的 Mac Pro 上的结果：

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

简而言之，对于单元素 array 的情况，它快了大约 6 倍，而对于非常长的 array，则略高于 3 倍。这种差异并不令人惊讶：标准转发的大部分成本在于构建 invocation 对象，而这对于整个 array 只会发生一次。对于长 array 来说，这个成本可以被摊薄到几乎不存在，我们只需要支付调用 `NSInvocation` 的成本，这虽然昂贵但并非不可承受。

两种技术也都要为分配 proxy、分配 array 以及填充该 array 付出代价。虽然这对两者的影响相同，但它降低了 LLVM 解决方案的相对优势。

最后，转发解决方案具有使用快速枚举的优势。这对于小 array 来说无关紧要，但对于大 array 来说则不利。当然，重新编写 LLVM 代码以使用快速枚举完全是可行的，但这会使代码更复杂。

另外，观察参数整理成本对传统转发在非常短的 array 上的影响也很有趣。一个带有 3 个参数的方法映射到 1 个元素的 array 所需的时间比没有参数的方法要多 10% 以上。而 LLVM map 因额外参数增加的开销只有大约 3%，因为这些参数基本上是硬编码的。

结论：高达 6 倍的加速，相当酷！

**局限性与改进**  
这个 LLVM 转发的东西很巧妙，但它还可以更好。如果你有兴趣进行尝试，这里有一些可以改进的地方：

1. **快速枚举：** 我可能已经提到大约十六次了，但它肯定有助于提高速度。
2. **缓存函数：** 目前，该实现为每个选择器（selector）生成一个新函数。这是浪费的，因为许多选择器可能具有相同的签名，因此可以重用同一个函数。一个允许不同选择器重用具有相同方法签名的函数的缓存可以减少开销。
3. **零大小 array：** 如果之前从未见过该选择器，那么这个实现在空 array 上会直接崩溃，因为没有对象可以从中获取方法签名来生成函数，但 `map` 不应仅仅因为用于空 array 而崩溃。
4. **结构体支持：** 这个有点棘手，但编写一些代码，能够从 Objective-C 类型字符串正确生成 LLVM 结构体定义，那将是很棒的。

**结论**  
这结束了我关于使用 LLVM 进行运行时代码生成的两周系列。在[第一周](http://www.mikeash.com/?page=pyblog/friday-qa-2009-04-17-code-generation-with-llvm-part-1-basics.html)，我展示了如何启动并运行基本的代码生成，然后本周你看到了如何在此基础上，在 Objective-C 程序中实际做一些有用的事情。

LLVM 是一个非常酷的项目，这种运行时代码生成极其强大。这个动态快速转发的实现仅仅触及了你所能做的有趣事情的皮毛。

有疑问？评论？挑战？请将它们发布在下面。

别忘了 Friday Q&A 是由你的建议驱动的。是否有你希望在此处讨论的主题？如果有，请[发送电子邮件](mailto:mike@mikeash.com)、[发推文](http://twitter.com/mikeash)，或将其发布在评论中。（如果你想保持匿名，请务必明确告诉我。）

喜欢这篇文章吗？我有整本书出售！第二卷和第三卷现在已出版！它们提供 ePub、PDF、印刷版，以及在 iBooks 和 Kindle 上发售。[点击此处获取更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS feed](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-04-24-code-generation-with-llvm-part-2-fast-objective-c-forwarding.html)

添加你的想法，发表评论：

垃圾邮件和偏离主题的帖子将被删除，恕不另行通知。违规者可能会根据我的判断被公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
