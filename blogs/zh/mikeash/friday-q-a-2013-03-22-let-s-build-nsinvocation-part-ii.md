---
title: 'Friday Q&A 2013-03-22：让我们构建 NSInvocation，第二部分'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-03-22-lets-build-nsinvocation-part-ii.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:65bbee0f0739fc04'
translated: true
---

> 原文：[Friday Q&A 2013-03-22: Let's Build NSInvocation, Part II](https://www.mikeash.com/pyblog/friday-qa-2013-03-22-lets-build-nsinvocation-part-ii.html)　·　mikeash.com Friday Q&A

发表于 2013-03-22 14:57 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Objective-C Literals 在塞尔维亚-克罗地亚语中](https://www.mikeash.com/pyblog/objective-c-literals-in-serbo-croatian.html)  
上一篇：[Friday Q&A 2013-03-08：让我们构建 NSInvocation，第一部分](https://www.mikeash.com/pyblog/friday-qa-2013-03-08-lets-build-nsinvocation-part-i.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2013-03-22：让我们构建 NSInvocation，第二部分

作者：[Mike Ash](https://www.mikeash.com/)

**回顾**  
`MAInvocation` 是我对 `NSInvocation` 大部分功能的重新实现。为简单起见，它不支持浮点参数和浮点返回值，也不支持 `struct` 参数。它只支持 `x86-64` 架构。代码在 GitHub 上：

[https://github.com/mikeash/MAInvocation](https://github.com/mikeash/MAInvocation)

函数的前六个参数通过六个寄存器传递：`rdi`、`rsi`、`rdx`、`rcx`、`r8` 和 `r9`。后续参数（如果有的话）通过栈传递。返回值放在 `rax` 中返回。对于双元素 `struct` 这一特殊情况，第二个元素在 `rdx` 中返回。更大的 `struct` 通过让调用方分配内存来返回，然后一个指向那块内存的指针会被隐式地作为第一个参数传入 `rdi`，所有显式参数相应后移。这些在 Objective-C 世界里被称为 `stret` 调用。

汇编语言胶水（assembly glue）用于在 `struct` 中保存的值与真实函数调用之间做转换。这个 `struct` 保存了所有相关寄存器，外加一个指向栈参数的指针，以及一些附加数据：

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

`MAInvocationCall` 函数用汇编编写，[上一篇文章](https://www.mikeash.com/pyblog/friday-qa-2013-03-08-lets-build-nsinvocation-part-i.html)已经探讨过它。它的原型是：

```
    void MAInvocationCall(struct RawArguments *);
```

Objective-C 代码可以填充一个带有函数指针和相应寄存器值的 `struct RawArguments`，然后调用这个函数。它会执行函数调用，返回时，`struct` 中的两个返回值寄存器字段会被填上该函数返回的内容。

另外还有两个转发处理器：

```
    void MAInvocationForward(void);
    void MAInvocationForwardStret(void);
```

它们被设计为可由任意 Objective-C 方法调用触发。两者都会新建一个 `struct RawArguments`，填好参数寄存器和栈参数指针，然后调用一个名为 `MAInvocationForwardC` 的 C 函数。当它返回时，处理器再把 `rax_ret` 和 `rdx_ret` 的值传回给调用方。这两个处理器的唯一区别，是把 `isStretCall` 设为 `0` 还是 `1`。

至此，`MAInvocation` 的 Objective-C 实现已经万事俱备。

**接口**  
`MAInvocation` 的接口与 `NSInvocation` 相同：

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

**实例变量**  
方法签名（method signature）是 invocation 对象的核心。方法签名描述了方法接受多少个参数以及它们的类型。这是弄清如何处理方法参数和返回类型的关键信息。正因如此，创建 `MAInvocation` 的唯一途径是传入一个 `NSMethodSignature`，而这个签名会保存在一个实例变量里：

```
    @implementation MAInvocation {
        NSMethodSignature *_sig;
```

invocation 自己持有一个局部的 `struct RawArguments`。在设置或读取参数与返回值时，会直接操作这个 `struct`。当 invocation 被调用时，指向这个实例变量的指针可以直接传给汇编胶水：

```
        struct RawArguments _raw;
```

invocation 可以保留（retain）自己的参数。这会向所有对象参数发送 `retain`，同时复制 C 字符串参数。参数当前是否已被保留需要被记录下来，以便正确释放它们，也让新设置的参数能被保留，所以有一个标志位：

```
        BOOL _argumentsRetained;
```

最后，还需要一个缓冲区来存放 `stret` 调用的返回值：

```
        void *_stretBuffer;
    }
```

**初始化**  
工厂方法只是调用一个 `init` 方法：

```
    + (NSInvocation *)invocationWithMethodSignature: (NSMethodSignature *)sig
    {
        return [[[self alloc] initWithMethodSignature: sig] autorelease];
    }
```

`init` 方法保存方法签名：

```
    - (id)initWithMethodSignature: (NSMethodSignature *)sig
    {
        if((self = [super init]))
        {
            _sig = [sig retain];
```

然后，它通过检查方法签名来判断返回值是否满足 `stret` 调用的条件，从而填充 `struct RawArguments` 的 `isStretCall`。这一步通过调用另一个方法完成，那个方法的代码相当繁琐，稍后会讲到：

```
            _raw.isStretCall = [self isStretReturn];
```

接下来设置栈参数。第一件事是从方法签名中取得参数总数：

```
            NSUInteger argsCount = [sig numberOfArguments];
```

注意这个计数包含 `self` 和 `_cmd` 两个隐式参数，所以这个数字恰好等于正在传递的函数参数个数。

如果是 `stret` 调用，那么实际上还多一个参数，因为有一个用于返回值的隐式指针要传进 `rdi`：

```
            if(_raw.isStretCall)
                argsCount++;
```

如果参数超过六个（可能包含隐式的 `stret` 参数），就存在栈参数。`stackArgsCount` 被设为剩余参数的数量，并分配内存让 `stackArgs` 能容纳它们：

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

**包装方法**  
API 里有几个方法只是对其他方法的小型包装。在进入正题之前，先在这里讲掉它们。

`target` 方法只是用稍微方便一点的方式取第一个参数的值。它就是对 `getArgument:atIndex:` 方法的一个小包装：

```
    - (id)target
    {
        id target;
        [self getArgument: &target atIndex: 0];
        return target;
    }
```

`setTarget:` 方法是对 `setArgument:atIndex:` 方法更简单的一层包装：

```
    - (void)setTarget: (id)target
    {
        [self setArgument: &target atIndex: 0];
    }
```

`selector` 和 `setSelector:` 方法几乎一样，只是操作第二个参数：

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

最后，`invoke` 方法调用 `invokeWithTarget:`，传入 `[self target]`：

```
    - (void)invoke
    {
        [self invokeWithTarget: [self target]];
    }
```

**获取参数**  
要从 invocation 中取出一个参数，代码首先得知道参数存放在_哪里_。这个小包装方法负责这件事：

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

这个方法接受一个_原始_参数索引，也就是说这个索引已经过调整，考虑了这是不是一次 `stret` 调用。然后它把这个索引映射到相应的寄存器或栈槽。

能够取得某个参数的大小也很方便，这样对小于 8 字节的参数就能复制正确数量的字节。这个方法包装了 Foundation 函数 `NSGetSizeAndAlignment`，它接受一个 Objective-C 类型字符串，返回相应类型的大小（和对齐值！）：

```
    - (NSUInteger)sizeOfType: (const char *)type
    {
        NSUInteger size;
        NSGetSizeAndAlignment(type, &size, NULL);
        return size;
    }
```

再对_这个_方法做一层小包装，就能得到给定参数的大小：

```
    - (NSUInteger)sizeAtIndex: (NSInteger)idx
    {
        return [self sizeOfType: [_sig getArgumentTypeAtIndex: idx]];
    }
```

要真正取出一个参数，方法先调整请求的索引，把可能的 `stret` 返回考虑进去：

```
    - (void)getArgument: (void *)argumentLocation atIndex: (NSInteger)idx
    {
        NSInteger rawArgumentIndex = idx;
        if(_raw.isStretCall)
            rawArgumentIndex++;
```

接着，它用上面的方法取得指针，并做合理性检查：

```
        uint64_t *src = [self argumentPointerAtIndex: rawArgumentIndex];
        assert(src);
```

然后取得参数大小，从参数位置复制相应数量的字节：

```
        NSUInteger size = [self sizeAtIndex: idx];
        memcpy(argumentLocation, src, size);
    }
```

**获取与设置返回值**  
要获取和设置返回值，需要知道值的大小。这很容易：只要取得方法签名中返回类型的大小即可：

```
    - (NSUInteger)returnValueSize
    {
        return [self sizeOfType: [_sig methodReturnType]];
    }
```

还需要取得指向返回值存放位置的指针。如果这个 invocation 对应一次 `stret` 调用，就返回 `_stretBuffer`。如果缓冲区还没分配，就分配它：

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

对于普通调用，它只返回原始参数 `struct` 中 `rax_ret` 字段的地址：

```
        else
        {
            return &_raw.rax_ret;
        }
    }
```

这同时照顾到了返回值占用两个返回寄存器的情况。由于它们在 `struct` 中是连续的，向这个地址复制一个足够大的值就会同时写到 `struct` 中的两个寄存器字段。

有了这些方法，编写获取和设置返回值的方法就简单了。它们要做的只是用算好的大小和指针调用 `memcpy`：

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

**类型分类**  
判断一个方法的返回类型是否需要 `stret` 调用，需要按照 `x86-64` 调用约定对类型进行分类。`NSInvocation` API 允许保留 invocation 的参数，这同样需要对参数类型分类，以便找出所有对象类型。

各种分类结果放进一个 `enum`，它把 `x86-64` ABI 的相关部分与保留参数所需的区分结合起来。归纳起来就是：对象、block、C 字符串、其他整数类型（包括非对象指针）、包含_两个_整数的 `struct`、空 `struct`、任何其他 `struct`，以及任何未被覆盖的其他类型：

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

分类过程本身由两个相互递归的方法组成：一个分类任意类型，另一个专门分类 `struct` 类型。

通用方法先利用 `@encode` 指令创建 'id'、block 和 C 字符串的类型字符串：

```
    - (enum TypeClassification)classifyType: (const char *)type
    {
        const char *idType = @encode(id);
        const char *blockType = @encode(void (^)(void));
        const char *charPtrType = @encode(char *);
```

注意，对 `@encode` 而言所有 block 的类型字符串都相同，所以这里选哪种 block 类型完全是任意的。

有了这些，它将 `type` 与它们比较，匹配则返回相应的 `enum` 值：

```
        if(strcmp(type, idType) == 0)
            return TypeObject;
        if(strcmp(type, blockType) == 0)
            return TypeBlock;
        if(strcmp(type, charPtrType) == 0)
            return TypeCString;
```

接着检查整数类型。这段疯狂的代码构造了一个 C 字符串，其中包含每个整数类型对应的字符，外加函数指针（就是 `?`），以及任何其他指针（它们都以 `^` 开头）：

```
        char intTypes[] = { @encode(signed char)[0], @encode(unsigned char)[0], @encode(short)[0], @encode(unsigned short)[0], @encode(int)[0], @encode(unsigned int)[0], @encode(long)[0], @encode(unsigned long)[0], @encode(long long)[0], @encode(unsigned long long)[0], '?', '^', 0 };
```

有了这个 C 字符串，就可以用 `strchr` 函数把 `type` 的第一个字符与所有这些字符对照。有匹配就说明该类型是整数类型：

```
        if(strchr(intTypes, type[0]))
            return TypeInteger;
```

`struct` 类型以 `{` 字符开头。如果类型字符串以它开头，就调用 `struct` 分类器：

```
        if(type[0] == '{')
            return [self classifyStructType: type];
```

如果什么都不匹配，就返回「其他」类型：

```
        return TypeOther;
    }
```

`struct` 分类器使用一个辅助方法，该方法接受 `struct` 的类型字符串并枚举其全部内容。它随时跟踪这个 `struct` 的分类结果，并随 `struct` 中的每个新元素更新。它从一个空 `struct` 出发：

```
    - (enum TypeClassification)classifyStructType: (const char *)type
    {
        __block enum TypeClassification structClassification = TypeEmptyStruct;
```

然后枚举并分类其中的每个类型：

```
        [self enumerateStructElementTypes: type block: ^(const char *type) {
            enum TypeClassification elementClassification = [self classifyType: type];
```

如果当前分类是空 `struct`，那么新分类就与该元素的分类相同。只有一个元素的 `struct`，其分类与它包含的元素相同：

```
            if(structClassification == TypeEmptyStruct)
                structClassification = elementClassification;
```

如果当前分类是整数类型，且元素分类也是整数类型，那么这个 `struct` 获得特殊的「包含两个整数的 `struct`」分类：

```
            else if([self isIntegerClass: structClassification] && [self isIntegerClass: elementClassification])
                structClassification = TypeTwoIntegers;
```

任何其他情况（`struct` 含两个以上元素、`struct` 含浮点元素等等），分类就是普通的 `struct`：

```
            else
                structClassification = TypeStruct;
        }];
        return structClassification;
    }
```

枚举 `struct` 类型字符串元素的方法很短。`struct` 类型字符串由 `struct` 的名字、`=` 符号，以及之后逐个拼接的元素类型组成，整体包在一对 `{}` 中。例如 `NSRange` 会是：

```
    {NSRange=LL}
```

该方法做的第一件事是找到 `=`，并从它之后开始扫描：

```
    - (void)enumerateStructElementTypes: (const char *)type block: (void (^)(const char *type))block
    {
        const char *equals = strchr(type, '=');
        const char *cursor = equals + 1;
```

然后枚举其中包含的每个类型，借助 `NSGetSizeAndAlignment` 把光标移动到所遇类型的末尾，即使该类型不止一个字符。直到遇见右花括号为止：

```
        while(*cursor != '}')
        {
            block(cursor);
            cursor = NSGetSizeAndAlignment(cursor, NULL, NULL);
        }
    }
```

还有一个简短的辅助方法，用于判断某个类型分类是否算作整数。它只检查该分类是不是对象、block、C 字符串，或真正的整数或其他指针：

```
    - (BOOL)isIntegerClass: (enum TypeClassification)classification
    {
        return classification == TypeObject || classification == TypeBlock || classification == TypeCString || classification == TypeInteger;
    }
```

类型分类系统到此完成。与 `x86-64` 规范的完整复杂度相比，这有些简陋，但对 `MAInvocation` 的需求来说足够了。有了类型分类，我们终于可以实现初始化方法中用到的 `isStretReturn` 方法了：

```
    - (BOOL)isStretReturn
    {
        return [self classifyType: [_sig methodReturnType]] == TypeStruct;
    }
```

**设置参数**  
有了类型分类，终于可以实现设置参数了。`setArgument:atIndex:` 的基本形式与 `getArgument:atIndex:` 几乎一样，但对保留参数的支持让一切都复杂得多。

你可以创建一个 `NSInvocation`，配置好，然后把它在手里留一段时间。为了让 `NSInvocation` 保持有效，它需要能对包含的参数做恰当的内存管理。出于灵活性的考虑，这是可选的。新建的 `NSInvocation` 不会对参数做任何内存管理，但可以向它发送 `retainArguments` 消息来启用。

`MAInvocation` 模仿了这一功能。当它收到 `retainArguments` 时，会对参数执行以下操作：

```
    1. Block arguments are copied.
    2. Non-block object arguments are retained.
    3. C string arguments are copied.
    4. All others are left alone.
```

除了在 `retainArguments` 时这样做，`setArgument:atIndex:` 方法还需要对每个新设置的参数执行同样的操作。这正是它比 `getArgument:atIndex:` 复杂得多的原因。

方法先计算原始参数索引：

```
    - (void)setArgument: (void *)argumentLocation atIndex: (NSInteger)idx
    {
        NSInteger rawArgumentIndex = idx;
        if(_raw.isStretCall)
            rawArgumentIndex++;
```

接着取得该索引处的参数指针：

```
        uint64_t *dest = [self argumentPointerAtIndex: rawArgumentIndex];
        assert(dest);
```

然后对该索引处的参数分类：

```
        enum TypeClassification c = [self classifyArgumentAtIndex: idx];
```

如果参数已被保留，它会接着检查参数的分类，看它是 block、非 block 对象还是 C 字符串。如果是，就用相应的 `retain` 或 `copy` 语义，把 `dest` 直接设为 `argumentLocation` 处的值。如果参数是其他类型，或者参数未被保留，就做一次简单的 `memcpy`。

第一种情况是普通对象。这里做相当标准的 `retain`/`release` 组合，外加一堆类型转换，把两个指针都当作对象指针对待。`release` 放在最后、借助 `old` 变量完成，以避免「释放旧值导致新值失效」的问题：

```
        if(_argumentsRetained && c == TypeObject)
        {
            id old = *(id *)dest;
            *(id *)dest = [*(id *)argumentLocation retain];
            [old release];
        }
```

block 得到同样的待遇，只是用 `copy` 而不是 `retain`：

```
        else if(_argumentsRetained && c == TypeBlock)
        {
            id old = *(id *)dest;
            *(id *)dest = [*(id *)argumentLocation copy];
            [old release];
        }
```

C 字符串类似，但用的是 `strdup` 和 `free`：

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

其余所有情况，都用 `memcpy` 复制相应数量的字节：

```
        else
        {
            NSUInteger size = [self sizeAtIndex: idx];
            memcpy(dest, argumentLocation, size);
        }
    }
```

`classifyArgumentAtIndex:` 是 `classifyType:` 的小包装，从方法签名取参数类型并分类：

```
    - (enum TypeClassification)classifyArgumentAtIndex: (NSUInteger)idx
    {
        return [self classifyType: [_sig getArgumentTypeAtIndex: idx]];
    }
```

**保留参数**  
除了在参数进入 `setArgument:atIndex:` 时逐个保留，`MAInvocation` 还需要在 `retainArguments` 方法里保留所有既有参数。只有第一次调用会做事情，所以该方法的第一步是检查参数是否已被保留，是就直接返回：

```
    - (void)retainArguments
    {
        if(_argumentsRetained)
            return;
```

接着用一个辅助方法遍历所有可保留的参数。这个方法对每个可保留参数调用一次 block，传入参数索引和参数的值。block 有三个值参数，任何一次调用只会设置其中一个。

```
        [self iterateRetainableArguments: ^(NSUInteger idx, id obj, id block, char *cstr) {
```

如果是对象参数，就保留它：

```
            if(obj)
            {
                [obj retain];
            }
```

如果是 block 参数，就复制 block，并把新值设为参数值。注意 `_argumentsRetained` 此时还没有被设为 `YES`，所以 `setArgument:atIndex:` 不会尝试自己做内存管理，避免两者相互冲突：

```
            else if(block)
            {
                block = [block copy];
                [self setArgument: &block atIndex: idx];
            }
```

如果是 C 字符串参数，就用 `strdup`：

```
            else if(cstr)
            {
                if(cstr != NULL)
                    cstr = strdup(cstr);
                [self setArgument: &cstr atIndex: idx];
            }
        }];
```

最后，设置 `_argumentsRetained`：

```
        _argumentsRetained = YES;
    }
```

`iterateRetainableArguments:` 方法用类型分类系统判断每个参数是什么，然后调用 `getArgument:atIndex:` 取值。它先遍历每个参数并分类：

```
    - (void)iterateRetainableArguments: (void (^)(NSUInteger idx, id obj, id block, char *cstr))block
    {
        for(NSUInteger i = 0; i < [_sig numberOfArguments]; i++)
        {
            enum TypeClassification c = [self classifyArgumentAtIndex: i];
```

对象和 block 由同一个分支处理。它先把参数取到一个局部 `id` 变量里：

```
            if(c == TypeObject || c == TypeBlock)
            {
                id arg;
                [self getArgument: &arg atIndex: i];
```

然后根据类型是 block 还是普通对象，把 `arg` 移入另外两个局部变量之一：

```
                id o = c == TypeObject ? arg : nil;
                id b = c == TypeBlock ? arg : nil;
```

此时，如果参数是普通对象，`o` 中就是参数值；如果是 block，`b` 中就是参数值。随后即可用这些值调用迭代 block：

```
                block(i, o, b, NULL);
            }
```

C 字符串类似，但更简单，因为这里只有一种可能的类型：

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

顺手再写一个 `argumentsRetained` 的简单取值方法：

```
    - (BOOL)argumentsRetained
    {
        return _argumentsRetained;
    }
```

**dealloc**  
`dealloc` 中最难的部分是释放被保留的参数。`iterateRetainableArguments:` 方法替我们完成了大部分工作：

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

处理完这些，剩下的就是释放方法签名、`stackArgs` 指针，然后调用 `super`：

```
        [_sig release];
        free(_raw.stackArgs);

        [super dealloc];
    }
```

**调用**  
到目前为止，代码已经让 `struct RawArguments` 几乎完全保持最新。实现 `invokeWithTarget:` 只剩补齐最后几个细节，然后调用汇编胶水函数 `MAInvocationCall`。方法先设置 target 值：

```
    - (void)invokeWithTarget: (id)target
    {
        [self setTarget: target];
```

然后用 `methodForSelector:` 取得 invocation 选择器（selector）对应的函数指针，放进 `fptr` 字段。这就是胶水代码将要调用的东西：

```
        _raw.fptr = [target methodForSelector: [self selector]];
```

如果这是一次 `stret` 调用，那么需要把 `rdi` 设置为指向一块能容纳返回值的空间：

```
        if(_raw.isStretCall)
            _raw.rdi = (uint64_t)[self returnValuePtr];
```

最后，调用汇编胶水：

```
        MAInvocationCall(&_raw);
    }
```

有了全部寄存器字段和栈参数指针，加上设为目标 `IMP` 的函数指针字段，汇编胶水就能完成调用。返回时，汇编胶水把 `rax` 和 `rdx` 拷贝到 `struct RawArguments` 的返回值字段中。这意味着汇编胶水返回时返回值已经就位，Objective-C 代码无需任何额外动作就能从 `getReturnValue:` 取到它。

**转发**  
`MAInvocation` 的最后一块主要拼图是 `MAInvocationForwardC` 函数。汇编语言转发胶水拦截未知消息调用，然后基于这次函数调用在栈上构造一个 `struct RawArguments`，再调用 `MAInvocationForwardC`，把指向该 `struct RawArguments` 的指针传给它。剩余逻辑用 Objective-C 实现：

```
    void MAInvocationForwardC(struct RawArguments *r)
    {
```

头等大事是取到消息的接收对象和正在发送的选择器。对 `stret` 调用，对象在 `rsi`，选择器在 `rdx`。对普通调用，对象在 `rdi`，选择器在 `rsi`：

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

创建 invocation 对象离不开方法签名。有了对象和选择器，简单调用 `methodSignatureForSelector:` 即可获得：

```
        NSMethodSignature *sig = [obj methodSignatureForSelector: sel];
```

有了方法签名，转发函数现在可以创建一个 `MAInvocation`：

```
        MAInvocation *inv = [[MAInvocation alloc] initWithMethodSignature: sig];
```

接下来要做的，是把 `r into the invocation's`_raw` 实例变量中的所有相关信息都拷贝进去（原文此处反引号错位，意为把 `r` 的内容拷入 invocation 的 `_raw`）。首先是寄存器：

```
        inv->_raw.rdi = r->rdi;
        inv->_raw.rsi = r->rsi;
        inv->_raw.rdx = r->rdx;
        inv->_raw.rcx = r->rcx;
        inv->_raw.r8 = r->r8;
        inv->_raw.r9 = r->r9;
```

之后拷贝栈参数。虽然 `r` 中的 `stackArgsCount` 总是 `0`，但 invocation 此时已经算出了实际栈参数的数量，所以可以查它自己的 `_raw` 变量来取得计数：

```
        memcpy(inv->_raw.stackArgs, r->stackArgs, inv->_raw.stackArgsCount * sizeof(uint64_t));
```

invocation 现在已完全构建并填充完毕。向对象发送 `forwardInvocation:`，带上新构建的 invocation。

```
        [obj forwardInvocation: (id)inv];
```

该调用返回后，需要把 invocation 的返回值拷回 `r`。随后汇编胶水会把这个值传回给调用方。它先拷贝两个返回值寄存器：

```
        r->rax_ret = inv->_raw.rax_ret;
        r->rdx_ret = inv->_raw.rdx_ret;
```

如果这是一次 `stret` 调用，并且 invocation 确实有存放返回值的缓冲区，就把 invocation 返回值缓冲区中的值拷贝到 `r->rdi` 所指向的内存——调用方指定过它希望返回值被放在那里：

```
        if(r->isStretCall && inv->_stretBuffer)
        {
            memcpy((void *)r->rdi, inv->_stretBuffer, [inv returnValueSize]);
        }
```

至此一切完成，释放 invocation，控制权交回汇编语言胶水：

```
        [inv release];
    }
```

胶水代码现在会把 `rax` 和 `rdx` 字段拷回相应的 CPU 寄存器，然后把控制权交还给最初的方法调用方——后者将在这些寄存器里，或在它通过 `rdi` 传入的 `stret` 缓冲区里，看到返回值。

**结语**  
`MAInvocation` 的实现到此收尾。尽管它只支持 `x86-64`，并且忽略了 `struct` 参数和一切浮点类型——而这些是 `x86-64` 调用约定中相当大的一部分——它已经极其复杂繁琐。`NSInvocation` 不仅支持所有类型的参数和返回值（除了 `union` 参数等少数边角情况），还至少在三种不同架构上支持它们：`i386`、`x86-64` 和 `ARM`。

然而，尽管复杂，这一切都完全可行。覆盖所有情况需要大量时间和精力，但没有任何神秘或魔法可言。它需要为其他架构编写等价的汇编胶水函数，扩展胶水函数以覆盖浮点寄存器，并在 `MAInvocation` 的 Objective-C 代码里实现「哪个参数去哪里」的全部逻辑。

构建 `MAInvocation` 非常有趣，也让人得以深入理解 `NSInvocation` 究竟在做什么。应当显而易见的是：不要把 `MAInvocation` 用于任何真正的工作。`NSInvocation` 做着所有同样的事情甚至更多，而且毫无疑问做得更好。

今天就到这里。下次再见，届时又是一场惊心动魄的冒险。Friday Q&A 由读者的点子驱动，在那之前，请继续[把你想看的主题点子发给我](mailto:mike@mikeash.com)。

喜欢这篇文章吗？我还在销售整本整本的文章合集！第二卷和第三卷已经出版，提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里了解详情](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论的 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2013-03-22-lets-build-nsinvocation-part-ii.html)

发表你的想法，发一条评论：

垃圾内容和离题帖子将被无通知删除。发帖者可能会按我的个人判断被公开羞辱。

代码语法高亮由 [Pygments](http://pygments.org/) 提供。
