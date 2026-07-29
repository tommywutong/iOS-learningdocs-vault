---
title: 'Friday Q&A 2009-10-30：Objective-C 中的生成器'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-10-30-generators-in-objective-c.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1f260c8c670a7160'
translated: true
---

> 原文：[Friday Q&A 2009-10-30: Generators in Objective-C](https://www.mikeash.com/pyblog/friday-qa-2009-10-30-generators-in-objective-c.html)　·　mikeash.com Friday Q&A

发布于 2009-10-30 16:59 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Friday Q&A 2009-11-06：链接和 Install Names](https://www.mikeash.com/pyblog/friday-qa-2009-11-06-linking-and-install-names.html)  
上一篇文章：[Friday Q&A 2009-10-23：即将到来的预览](https://www.mikeash.com/pyblog/friday-qa-2009-10-23-a-preview-of-coming-attractions.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [generators](https://www.mikeash.com/pyblog/?tag=generators)

Friday Q&A 2009-10-30：Objective-C 中的生成器

作者：[Mike Ash](https://www.mikeash.com/)

**生成器**  
 [生成器（generator）](http://en.wikipedia.org/wiki/Generator_(computer_science))本质上是一种能在调用之间记住自身状态的函数。在普通函数中，第二次调用与第一次完全相同。执行从头开始，局部变量重置其值，等等。而对于生成器，执行会从上次中断的地方继续，局部变量也会记住它们的值。

在 Python 中，一个简单的生成器看起来像这样：

```
    def countfrom(n):
        while True:
            yield n
            n += 1
```

`yield` 语句取代了普通函数中的 `return` 语句。当执行到 `yield` 时，值被返回，但函数的状态也被保存。最终结果是，连续调用会返回递增的数字。

实际上，在 Python 中事情并没有这么简单。调用 `countfrom` 并不会立即开始返回数字，而是返回一个对象。调用该对象返回值的 `next` 方法会依次返回递增的数字。

使用我的 [MAGenerator](http://www.mikeash.com/svn/MAGenerator/)，情况类似。生成器的写法要冗长和丑陋得多，但考虑到这是 C 语言，并且基本上是 hack 上去的支持而非语言特性，这并不令人意外。使用 `MAGenerator` 的计数器生成器示例如下：

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

与 Python 类似，调用 `CountFrom` 并不会立即开始返回数字。相反，它返回一个 block（块）。调用该 block 就会开始返回数字。以下是你实际使用此生成器的示例：

```
    int (^counter)(void) = CountFrom(42);
    for(int i = 0; i < 10; i++)
        NSLog(@"%d", counter());
```

这将输出 42、43、44、45、46、47、48、49、50、51。

**基本实现**  
 `MAGenerator` 工作方式背后的基本概念灵感来源于 [Simon Tatham 的 C 语言协程](http://www.chiark.greenend.org.uk/~sgtatham/coroutines.html)。他的协程要受限得多，因为不包含 block 的 C 语言实际上无法处理所需的功能，但实现中包含了大量巧妙之处。

需要解决两个主要问题。第一个是如何从上次中断的地方恢复执行。这通过使用 `switch` 语句解决。各个 `case` 标签提供了恢复执行的位置。在 C 语言中，`case` 标签几乎可以放在任何地方，甚至在其他控制结构内部，跳转可以顺利进行，一切都不会出现任何问题。

第二个问题是保存状态。Tatham 通过简单地使用 `static` 变量代替局部变量解决了这个问题。虽然这可行，但它有一个严重的限制：只允许该函数的一个实例处于活跃状态。通过使用 block，我们可以利用从封闭作用域捕获的变量来更优雅地解决这个问题。因此，下面是我们 `CountFrom` 函数的基本思路，如果我们直接实现而不使用宏：

```
    // 这个奇怪的东西是声明一个返回 block 的函数的方法
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

如你所见，对 `CountFrom` 的调用返回一个 block，该 block 捕获了 `start` 参数以及 `state` 和 `n` 局部变量。这些变量使用 `__block` 限定，以便可以在 block 内部改变它们。

`state` 变量是魔法发生的地方。当你调用 block 时，执行总是从顶部开始，就像函数一样。然而，它首先遇到的是一个 `switch` 语句。通过将 `state` 变量设置为对应于 `return` 语句的位置，这个 `switch` 语句使得执行立即在它之后恢复。由于我们所有的变量都是从封闭作用域捕获的，它们在调用之间记住它们的内容。

**清理**  
 让我们考虑一个小的字符串构建器生成器。这个生成器将获取路径组件并从中构建完整的路径。这是初步尝试：

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

这可行，但很危险。危险源于 `__block` 变量不会 retain 它们所指向的对象。我们的 `path` 变量指向一个非拥有的字符串。如果调用者在两次调用路径构建器生成器之间恰好弹出了自动释放池（autorelease pool），那将销毁字符串，在 `path` 中留下一个悬垂指针，并在下一次调用时导致崩溃。

我们可以通过复制字符串来修复这个问题，如下所示：

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

但这有一个新问题，即它会泄漏分配给 `path` 的最后一个字符串。

正确的解决方案是创建一个在主要 block 被销毁时执行的清理 block。这可以通过利用 block 确实会自动管理捕获的非 `__block` 对象指针变量的内存来实现。我们可以创建一个对象：

```
    NSString *(^PathBuilder(void))(NSString *component)
    {
        id cleanupObj = ...;
```

以无意义的方式引用它，以便它被 block 捕获：

```
        ...
        NSString *(^block)(NSString *component) = ^{
           [cleanupObj path];
           ...
```

然后让该对象在销毁时调用清理 block：

```
        [cleanupObj callBlockWhenDeallocated: ^{ ... }];
```

这可以通过使用自定义类来完成，但为了简单起见，我选择使用带有自定义回调的 `CFMutableArray`，设置回调使得 retain 回调会复制对象，而 release 回调会将其转换为适当的 block 指针，调用它，然后释放它。通过将清理 block 添加到数组中，当数组（和生成器 block）销毁时，它将自动被调用。

如果你假设 `MAGeneratorMakeCleanupArray` 负责设置适当的 `CFMutableArray`（并将其转换为 `NSMutableArray`），那么最终的带有清理功能的代码如下所示：

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

现在一切都按预期工作了。

**宏化**  
 上述内容虽然可行，但写起来非常烦人。为方便起见，我将所有样板部分都做成了宏（macro）。

首先，`GENERATOR` 宏负责函数声明以及一个用于保存清理 block 的变量。它还声明了一个 `GENERATOR_zeroReturnValue` 变量，用于消除编译器关于在 block 末尾未能返回值的警告。不幸的是，这个技巧意味着你不能使用这些宏来创建返回 `void` 的生成器。然而，由于你可以声明另一个类型（如 `int`）并在调用方忽略该值，因此这不是一个大问题。它看起来像这样：

```
    #define GENERATOR(returnType, nameAndCreationParams, perCallParams) \
        returnType (^nameAndCreationParams) perCallParams \
        { \
            returnType GENERATOR_zeroReturnValue; \
            bzero(&GENERATOR;_zeroReturnValue, sizeof(GENERATOR_zeroReturnValue)); \
            returnType (^GENERATOR_cleanupBlock)(void) = nil;
```

局部变量可以紧跟在 `GENERATOR` 之后声明。

`GENERATOR_DECL` 的工作方式与 `GENERATOR` 宏相同，但只产生原型，适用于头文件中的声明。

```
    #define GENERATOR_DECL(returnType, nameAndCreationParams, perCallParams) \
        returnType (^nameAndCreationParams) perCallParams
```

接下来是 `GENERATOR_BEGIN`，它再次接受生成器的参数。这声明了状态变量（称为 `GENERATOR_where`）、清理数组，并开始 block：

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

生成器代码可以跟在这个宏之后。在生成器代码中，你想要返回值，因此使用 `GENERATOR_YIELD` 宏来实现。这个宏的作用与我们上面手动编写的序列完全相同。这里的一个技巧是，我们需要一个唯一的数字来标识此次 yield 的状态值。之前我们可以在代码中简单地写入 1、2、3、4 等。我们可以让这个宏再接受一个参数作为状态值，但跟踪所有这些值很烦人。相反，像 Tatham 所做的那样，我选择使用 `__LINE__` 宏，它会被当前代码行的行号替换。

```
    #define GENERATOR_YIELD(...) \
                        do { \
                            GENERATOR_where = __LINE__; \
                            return __VA_ARGS__; \
                    case __LINE__: ; \
                        } while(0)
```

这工作得很好，但有一个注意事项，即你绝不能在同一条行上放置两个 `GENERATOR_YIELD`。

接下来，我们希望有能力定义一个清理 block，我们将通过 `GENERATOR_CLEANUP` 宏来实现。这个宏有点奇怪，因为宏的设计使得无论是否存在 `GENERATOR_CLEANUP`，它们都能工作。`GENERATOR_END` 将结束生成器的定义，它需要无论跟在 `GENERATOR_CLEANUP` 还是 `GENERATOR_BEGIN` 之后都能正常工作。这是通过向清理 block 添加一组多余的尖括号来实现的：

```
    #define GENERATOR_CLEANUP \
                } \
                GENERATOR_where = -1; \
                return GENERATOR_zeroReturnValue; \
            }; \
            GENERATOR_cleanupBlock = ^{{
```

返回语句让编译器不再抱怨缺少返回语句，并且在你让执行流落到末尾时提供了一个安全网。最后我们来到结束部分。同样，这个宏必须无论是否存在 `GENERATOR_CLEANUP` 都能工作。因此，它以相同的返回语句结束，这在两种上下文中都有效。最后它检查是否设置了清理 block，如果是则将其添加到清理数组中，然后返回新创建的生成器 block。

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

请注意，为了在清理 block 中容纳 `return GENERATOR_zeroReturnValue;` 语句，清理 block 需要具有与生成器 block 相同的返回类型。由于数组无法确定要调用的正确 block 类型，我们将清理 block 包装在一个它可以处理的简单的 `void`/`void` block 中。

**结果**  
 这些宏相当可怕，但结果非常好。这是我开头展示的同一个示例：

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

更复杂的生成器看起来也不错。这是我上面用作示例的 `PathBuilder` 生成器（未使用宏时）以宏形式呈现：

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

当然，这并非 100% 自然，但考虑到语言本身不支持这类功能，总体来说它惊人地合理且可读。

**注意事项**  
 如同所有对自然的亵渎罪行一样，MAGenerator 也有一些注意事项。

1. **局部变量必须在 `GENERATOR_BEGIN` 之前，在顶部声明。** 在生成器 block 内部声明的局部变量在调用之间不会记住它们的状态。在精心构建的代码中你或许可以侥幸成功，但最好不要尝试。
2. **这包括使用 `for`/`in` 循环产生的隐式局部变量。** 你不能安全地使用 `for`/`in` 循环（其他循环结构没问题），除非循环体内不包含 `GENERATOR_YIELD` 的调用。
3. **你不能在同一条行上放置两个 `GENERATOR_YIELD`。** 这不是什么大问题：用回车分隔它们即可。值得庆幸的是，这会产生编译器错误，而不是难以调试的运行时错误。
4. **生成器内部使用的 `switch` 语句不得包含任何 `GENERATOR_YIELD` 调用。** 因为生成器的执行状态是通过 `switch` 语句恢复的，并且因为 `GENERATOR_YIELD` 会创建 `case` 标签，所以在你自己的 `switch` 语句内部使用 `GENERATOR_YIELD` 会引起混淆，因为生成的 case 标签将属于内部 `switch`，而不是宏生成的执行分发 `switch`。
5. **如果对象生命周期跨越 `GENERATOR_YIELD`，则必须小心管理。** 你不能假设调用者会为你保持一个自动释放池（autorelease pool）直到你完成。`GENERATOR_CLEANUP` 会处理这个问题，但它仍然比在普通代码中更难。

这些都是不幸的，我希望它们不存在，但总的来说，它们绝不是什么致命问题。

**潜在用途**  
 我对生成器领域相当陌生，当然每个人对 Objective-C 中的生成器领域都是陌生的，但我有一些关于如何有效使用它们的想法。

**惰性求值**  
 生成器在 Python 中的一个主要用途是惰性求值枚举值。生成器按需创建新值，而不是要求所有值都被预计算。MAGenerator 包含一个便捷函数 `MAGeneratorEnumerator`，它接受一个没有每次调用参数的生成器，返回类型为 `id`，并返回一个符合 `NSFastEnumeration` 的对象，该对象通过连续调用生成器进行枚举。

作为一个示例，这里是一个生成器，它将在指定路径中找到具有特定扩展名的文件：

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

你可以编写一个返回数组的函数，但这需要枚举整个目录的内容，如果调用者实际上并不需要所有这些内容，这会很慢。你可以编写一个包装 `NSDirectoryEnumerator` 的 `NSEnumerator` 子类（subclass），但这需要更多的代码。你可以编写一个代码，它接受一个 block 作为参数，并为找到的每个文件调用它，但这不太自然。以下是使用此生成器的方式：

```
    for(NSString *path in MAGeneratorEnumerator(FileFinder(@"/Applications", @"app")))
        NSLog(@"%@", path);
```

没有比这更简单的了。

**替代状态机**  
 代码经常需要状态机（state machine）。想象一下类似于网络协议解析器的东西。编写这种代码的自然方式是编写从上到下的代码。读取一个字符，对其执行操作。读取下一个字符，对其执行操作。使用循环读取字符串，读取单个字符以跳过分隔符，等等。

然后异步编程出现了，突然间这似乎不是一个好主意。每一个读取调用都可能阻塞。你可以将其放在一个单独的线程（thread）中，但这有其自身的问题。你研究使用 `NSStream` 或 GCD 进行基于回调的网络编程，但突然间你必须处理缓冲区，保留一堆关于你在协议解析中所在位置的显式状态，等等。

得益于其由内而外的编程方法，生成器允许你反转控制流（control），同时保留从同步方法中获得的美观线性代码。

作为一个示例，考虑一个非常简单的 RLE 解码器，它读取 `{ count, value }` 字节对。通常，解码器如果是异步的，则必须跟踪它处于什么状态，以便知道它接收的下一个字节是 count 还是 value。然而，使用生成器，这些状态信息消失了，被隐式的生成器状态所取代：

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

这段代码比非生成器的异步版本更直接、更容易理解。

对于更复杂的示例，这里是一个写为生成器的 HTTP 响应解析器。它接受几个 block 作为参数，用作解析完响应各个部分时的回调。

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
            // 读取响应行
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
            
            // 读取标头
            while(1)
            {
                currentHeaderData = [[NSMutableData alloc] init];
                while(byte != ':' && byte != '\r')
                {
                    AppendByte(currentHeaderData, byte);
                    GENERATOR_YIELD(0);
                }
                
                // 空行表示标头处理完毕
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
            
            // 读取正文
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

要使用它，代码只需像这样创建一个新的解析器：

```
    int (^httpParser)(int) = HTTPParser( /* callbacks go here */ );
```

然后将其存储在某处。每当从远程端有新的数据可用时，就调用它：

```
    httpParser(newByte);
```

当连接关闭时，它发出流结束的信号：

```
    httpParser(-1);
```

其他一切都会自动发生。每当 `newByte` 提供了足够的信息，使得解析器可以解析出响应的一个新组件时，相应的回调 block 就会被调用。

这个生成器被声明为返回 `int`，因为 MAGenerator 不支持 `void` 生成器。在这种情况下，返回值被简单地忽略。执行从顶部开始，数据流的第一个字符存储在 `byte` 中。每次它调用 `GENERATOR_YIELD` 时，效果是从调用者那里获得一个新的 `byte`。因此，解析自然地从上到下进行，即使这段代码实际上是高度异步的。

应该注意的是，这些解析器效率不是很高，因为它们需要对每个字节进行一次 block 调用（一次函数调用加上额外开销）。如果必要，这可以很容易地补救。修改生成器以接受一个缓冲区而不是单个字节。然后，不是盲目地调用 `GENERATOR_YIELD`，代码会在缓冲区中推进一个光标，并且仅在缓冲区为空并需要重新填充时才调用 `GENERATOR_YIELD`。这将使每次调用处理一个缓冲区，而不是每个字节一次调用。

**总结**  
 现在你知道如何使用 block 在 Objective-C 中构建生成器，并且至少有一些关于如何有效使用它们的想法。当然，你不应该手动构建它们，而应该使用我的 MAGenerator 库！MAGenerator 是开源的。你可以通过从我的 Subversion 仓库检出获取源码：

```
    svn co http://www.mikeash.com/svn/MAGenerator/
```

或者通过点击上面的 URL 来浏览它。它可以根据 MIT 许可证使用，因此你几乎可以在任何项目中使用它。该项目包含编写生成器所需的一切，以及大量的示例/测试用例。

我相信还有很多可以改进的地方，欢迎提交补丁。根据你所做的更改，我不能保证一定会接受，但当然，如果我不接受，你随时可以 fork。

本周就到这里。看起来这是我迄今为止最长的 Friday Q&A，所以我希望它能弥补上周只是代码转储的不足。下周回来会带来另一个惊悚版。像往常一样（除了本周），Friday Q&A 是由你们的投稿驱动的。如果你有希望在这里看到的话题，[请发邮件给我！](mailto:mike@mikeash.com)

你喜欢这篇文章吗？我正在出售包含全部文章的书！第二卷和第三卷现在已经上市！它们以 ePub、PDF、印刷版以及 iBooks 和 Kindle 格式提供。[点击这里了解更多信息](https://www.mikeash.com/book.html).

---

评论：

---

[此页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-10-30-generators-in-objective-c.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
