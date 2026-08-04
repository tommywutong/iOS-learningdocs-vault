---
title: 'Friday 问答 2013-02-08：构建键值编码'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-02-08-lets-build-key-value-coding.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2455c810cad34765'
translated: true
---

> 原文：[Friday Q&A 2013-02-08: Let's Build Key-Value Coding](https://www.mikeash.com/pyblog/friday-qa-2013-02-08-lets-build-key-value-coding.html)　·　mikeash.com Friday Q&A

发表于 2013-02-08 14:17 | [RSS feed](https://www.mikeash.com/pyblog/rss.py)（[全文 feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)
下一篇：[Friday Q&A 2013-02-22：构建 UITableView](https://www.mikeash.com/pyblog/friday-qa-2013-02-22-lets-build-uitableview.html)
上一篇：[Friday Q&A 2013-01-25：构建 NSObject](https://www.mikeash.com/pyblog/friday-qa-2013-01-25-lets-build-nsobject.html)
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday 问答 2013-02-08：构建键值编码

作者：[Mike Ash](https://www.mikeash.com/)

**基础**
键值编码（KVC）是一组通过字符串访问对象属性的 API。`NSObject` 实现了根据键名查找访问器方法或实例变量、并使用它们读取或设置值的方法。

KVC 的基础由两个基本方法构成。

`valueForKey:` 方法会先查找与键同名的 getter 方法。找到后调用该方法并返回结果。如果没有找到，它会查找与键同名的实例变量。若仍然失败，则查找名称相同但带下划线前缀的实例变量。找到实例变量后，返回它当前保存的值。

`setValue:forKey:` 方法执行相同的搜索，只是它查找的是 setter 方法而非 getter。随后，它要么调用 setter，要么直接设置实例变量。

这两个方法都有一个有趣的特性：它们会自动将基本类型值封装（boxing）为 `NSNumber` 或 `NSValue` 实例，也会自动解封装（unboxing），因此可以直接处理基本类型。你可以用 `valueForKey:` 调用一个返回 `int` 的方法，结果会是一个包含返回值的 `NSNumber` 对象。同样，也可以用 `setValue:forKey:` 调用一个接受 `int` 的方法，传入 `NSNumber`，它会自动取出其中的整数值。

KVC 还有键路径的概念：用句点连接一串键，例如：

```
    foo.bar.baz
```

对应地，有 `valueForKeyPath:` 和 `setValue:forKeyPath:` 方法处理键路径。这两个方法只是递归调用前面更基础的方法。

KVC 还有许多用于管理集合的特性，但它们没那么有意思，本文就略过了。

**代码**
今天的代码作为 `MAObject` 项目的一部分发布在 GitHub 上：

[https://github.com/mikeash/MAObject](https://github.com/mikeash/MAObject)

开始吧。

**valueForKey:**
`valueForKey:` 做的第一件事，是查找一个与键同名的 getter 方法。

```
    - (id)valueForKey: (NSString *)key
    {
        SEL getterSEL = NSSelectorFromString(key);
        if([self respondsToSelector: getterSEL])
        {
```

如果对象响应这个 selector，它就会使用访问器获取值。具体做法取决于访问器的返回类型。首先获取返回类型和该方法的 `IMP`：

```
            NSMethodSignature *sig = [self methodSignatureForSelector: getterSEL];
            char type = [sig methodReturnType][0];
            IMP imp = [self methodForSelector: getterSEL];
```

如果返回类型是对象或类，代码很简单：将 `IMP` 转换为正确的函数指针类型，调用它，然后返回结果：

```
            if(type == @encode(id)[0] || type == @encode(Class)[0])
            {
                return ((id (*)(id, SEL))imp)(self, getterSEL);
            }
```

否则，方法返回的是基本类型，事情就变得有意思了。

没有一种方便的方式可以接收任意类型的函数指针、调用它并封装返回值。我们只能用蛮力：逐一枚举所有可能性，为每种类型编写处理代码。为此我定义了一个小宏：

```
            else
            {
                #define CASE(ctype, selectorpart) \
                    if(type == @encode(ctype)[0]) \
                        return [NSNumber numberWith ## selectorpart: ((ctype (*)(id, SEL))imp)(self, getterSEL)];
```

这个想法是让每种类型只占一行。一个参数传入类型名，另一个参数传入可与 `[NSNumber numberWithType:]` 拼接的 selector 部分。宏会据此生成代码：检查类型是否匹配，匹配时用正确的函数指针类型调用 `IMP`。有了这个宏，只需写出所有支持的基本类型：

```
                CASE(char, Char);
                CASE(unsigned char, UnsignedChar);
                CASE(short, Short);
                CASE(unsigned short, UnsignedShort);
                CASE(int, Int);
                CASE(unsigned int, UnsignedInt);
                CASE(long, Long);
                CASE(unsigned long, UnsignedLong);
                CASE(long long, LongLong);
                CASE(unsigned long long, UnsignedLongLong);
                CASE(float, Float);
                CASE(double, Double);
```

别忘了取消定义 `CASE` 宏，这样稍后才能再次使用这个名字：

```
                #undef CASE
```

如果找到匹配的分支，方法会立即返回。如果执行到这里方法仍未返回，说明类型未知。方法不会尝试优雅地处理这种情况，而是直接抛出异常：

```
                [NSException raise: NSInternalInconsistencyException format: @"Class %@ key %@ don't know how to interpret method return type from getter, signature is %@", [isa description], key, sig];
            }
        }
```

以上处理了 getter 方法存在的情况。如果没有 getter，KVC 就退回到实例变量。首先，它尝试获取一个与键同名的实例变量：

```
        Ivar ivar = class_getInstanceVariable(isa, [key UTF8String]);
```

如果失败，再尝试加上下划线前缀：

```
        if(!ivar)
            ivar = class_getInstanceVariable(isa, [[@"_" stringByAppendingString: key] UTF8String]);
```

如果其中任何一次找到了实例变量，就继续读取它的值。要取出变量内容，首先要知道它存储在哪里：获取变量偏移量，再将它加到 `self` 的值上：

```
        if(ivar)
        {
            ptrdiff_t offset = ivar_getOffset(ivar);
            char *ptr = (char *)self;
            ptr += offset;
```

`self` 先转换为 `char *`，因为偏移量以字节为单位，对 `char *` 做 `+=` 才能得到需要的效果。

还需要知道变量的类型：

```
            const char *type = ivar_getTypeEncoding(ivar);
```

如果类型是对象或类，就直接取出并返回：

```
            const char *type = ivar_getTypeEncoding(ivar);
            if(type[0] == @encode(id)[0] || type[0] == @encode(Class)[0])
            {
                return *(id *)ptr;
            }
```

否则，再次退回到特殊情况处理。这次使用略有不同的 `CASE` 宏：它检查类型，匹配时从 `ptr` 取出值：

```
            else
            {
                #define CASE(ctype, selectorpart) \
                    if(strcmp(type, @encode(ctype)) == 0) \
                        return [NSNumber numberWith ## selectorpart: *(ctype *)ptr];
```

同样，这里有一长串支持的类型：

```
                CASE(char, Char);
                CASE(unsigned char, UnsignedChar);
                CASE(short, Short);
                CASE(unsigned short, UnsignedShort);
                CASE(int, Int);
                CASE(unsigned int, UnsignedInt);
                CASE(long, Long);
                CASE(unsigned long, UnsignedLong);
                CASE(long long, LongLong);
                CASE(unsigned long long, UnsignedLongLong);
                CASE(float, Float);
                CASE(double, Double);
```

然后清理宏：

```
                #undef CASE
```

如果没有匹配项，代码会用 `ptr` 中的内容创建一个通用的 `NSValue`。由于数据已经按原样排布在内存中，这里可以轻松提供回退方案，而不必像 getter 代码那样抛出异常：

```
                return [NSValue valueWithBytes: ptr objCType: type];
            }
        }
```

最后，如果既没有找到 getter，也没有找到实例变量，方法会抛出异常。末尾的虚拟 return 语句只是为了避免编译器抱怨没有返回值：

```
        [NSException raise: NSInternalInconsistencyException format: @"Class %@ is not key-value compliant for key %@", [isa description], key];
        return nil;
    }
```

`valueForKey:` 就处理完了。

**setValue:forKey:**
`setValue:forKey:` 方法的工作方式类似，但由于它需要设置值，存在一些差异。

它做的第一件事是构造要查找的 setter 方法名称。`valueForKey:` 可以直接把键转换为 selector，但这个方法需要多做一些工作。setter 方法由以下规则生成：将键的首字母大写，在开头加上“set”，末尾加冒号：

```
    - (void)setValue: (id)value forKey: (NSString *)key
    {
        NSString *setterName = [NSString stringWithFormat: @"set%@:", [key capitalizedString]];
```

然后将它转换成 selector，并检查对象是否响应：

```
        SEL setterSEL = NSSelectorFromString(setterName);
        if([self respondsToSelector: setterSEL])
        {
```

如果响应，就像 getter 代码那样获取方法参数类型和 `IMP`：

```
            NSMethodSignature *sig = [self methodSignatureForSelector: setterSEL];
            char type = [sig getArgumentTypeAtIndex: 2][0];
            IMP imp = [self methodForSelector: setterSEL];
```

如果类型是对象或类，就直接调用 setter，传入 `value`，然后返回：

```
            if(type == @encode(id)[0] || type == @encode(Class)[0])
            {
                ((void (*)(id, SEL, id))imp)(self, setterSEL, value);
                return;
            }
```

否则，再次需要使用 `CASE` 宏。找到匹配项时，它会调用 `IMP`，并将 `[value typeValue]` 作为参数传入：

```
            else
            {
                #define CASE(ctype, selectorpart) \
                    if(type == @encode(ctype)[0]) { \
                        ((void (*)(id, SEL, ctype))imp)(self, setterSEL, [value selectorpart ## Value]); \
                        return; \
                    }
```

下面是完整的分支列表：

```
                CASE(char, char);
                CASE(unsigned char, unsignedChar);
                CASE(short, short);
                CASE(unsigned short, unsignedShort);
                CASE(int, int);
                CASE(unsigned int, unsignedInt);
                CASE(long, long);
                CASE(unsigned long, unsignedLong);
                CASE(long long, longLong);
                CASE(unsigned long long, unsignedLongLong);
                CASE(float, float);
                CASE(double, double);
```

然后清理宏：

```
                #undef CASE
```

最后，如果类型未知，就抛出异常：

```
                [NSException raise: NSInternalInconsistencyException format: @"Class %@ key %@ set from incompatible object %@", [isa description], key, value];
            }
        }
```

如果没有找到 setter 方法，它就搜索实例变量。不需要进行字符串处理，因为实例变量的名称不像 setter 名称那样需要变化。下面的代码同样会检查带下划线前缀的实例变量：

```
        Ivar ivar = class_getInstanceVariable(isa, [key UTF8String]);
        if(!ivar)
            ivar = class_getInstanceVariable(isa, [[@"_" stringByAppendingString: key] UTF8String]);
```

如果实例变量存在，就像 `valueForKey:` 一样创建指向它的指针并获取类型：

```
        if(ivar)
        {
            ptrdiff_t offset = ivar_getOffset(ivar);
            char *ptr = (char *)self;
            ptr += offset;

            const char *type = ivar_getTypeEncoding(ivar);
```

如果变量是对象或类指针，代码可以直接设置它。不过严格来说并非完全直接：为了保证内存管理正确，需要进行一次小型的 `retain`/`release` 配对：

```
            if(type[0] == @encode(id)[0] || type[0] == @encode(Class)[0])
            {
                value = [value retain];
                [*(id *)ptr release];
                *(id *)ptr = value;
                return;
            }
```

否则，`value` 是一个封装对象，需要取出其中的基本类型值。如果 `value` 是 `NSValue`，并且类型与实例变量**完全**相同，就可以使用 `getValue:` 直接把值复制过去：

```
            else if(strcmp([value objCType], type) == 0)
            {
                [value getValue: ptr];
                return;
            }
```

如果这也不行，就轮到最后一长串分支了。这个版本的 `CASE` 宏会把经过适当转换的 `[value typeValue]` 设置到 `ptr`：

```
            else
            {
                #define CASE(ctype, selectorpart) \
                    if(strcmp(type, @encode(ctype)) == 0) { \
                        *(ctype *)ptr = [value selectorpart ## Value]; \
                        return; \
                    }
```

接下来是传统的基本类型穷举：

```
                CASE(char, char);
                CASE(unsigned char, unsignedChar);
                CASE(short, short);
                CASE(unsigned short, unsignedShort);
                CASE(int, int);
                CASE(unsigned int, unsignedInt);
                CASE(long, long);
                CASE(unsigned long, unsignedLong);
                CASE(long long, longLong);
                CASE(unsigned long long, unsignedLongLong);
                CASE(float, float);
                CASE(double, double);
```

清理宏：

```
                #undef CASE
```

最后，如果没有任何分支命中，就抛出异常：

```
                [NSException raise: NSInternalInconsistencyException format: @"Class %@ key %@ set from incompatible object %@", [isa description], key, value];
            }
        }
```

如果既没有找到 setter 方法，也没有找到实例变量，就抛出异常：

```
        [NSException raise: NSInternalInconsistencyException format: @"Class %@ is not key-value compliant for key %@", [isa description], key];
    }
```

**键路径**
为了完成 KVC 的实现，我也会实现 `valueForKeyPath:` 和 `setValue:forKeyPath:`。

`valueForKeyPath:` 做的第一件事，是在键路径中查找 `.`。如果不存在，就把它当作普通键，传给 `valueForKey:`：

```
    - (id)valueForKeyPath: (NSString *)keyPath
    {
        NSRange range = [keyPath rangeOfString: @"."];
        if(range.location == NSNotFound)
            return [self valueForKey: keyPath];
```

否则，键会被拆成两部分。`.` 之前的部分是本地键，后面的部分是键路径的剩余部分：

```
        NSString *key = [keyPath substringToIndex: range.location];
        NSString *rest = [keyPath substringFromIndex: NSMaxRange(range)];
```

将键传给 `valueForKey:`：

```
        id next = [self valueForKey: key];
```

然后对 `next` 对象递归调用 `valueForKeyPath:`：

```
        return [next valueForKeyPath: rest];
    }
```

它的实现会继续拆分 `rest`，直到消耗掉每一个 `.`。最终结果就是一串 `valueForKey:` 调用，并返回最后一次调用的结果。

`setValue:forKeyPath:` 的工作方式类似。如果键路径中没有 `.`，就调用 `setValue:forKey:` 并返回：

```
    - (void)setValue: (id)value forKeyPath: (NSString *)keyPath
    {
        NSRange range = [keyPath rangeOfString: @"."];
        if(range.location == NSNotFound)
        {
            [self setValue: value forKey: keyPath];
            return;
        }
```

否则，取出键和剩余部分：

```
        NSString *key = [keyPath substringToIndex: range.location];
        NSString *rest = [keyPath substringFromIndex: NSMaxRange(range)];
```

使用 `valueForKey:` 获取下一个对象：

```
        id next = [self valueForKey: key];
```

然后以 `rest` 作为键路径，递归向 `next` 发送 `setValue:forKeyPath:`：

```
        [next setValue: value forKeyPath: rest];
    }
```

最终结果是一串 `valueForKey:` 调用，最后在链末对象上调用 `setValue:forKey:`。

**结论**
现在你可以看到键值编码的内部工作方式了。它并不特别复杂，本质上只是依次尝试一长串不同的可能性。Cocoa 的实现更聪明一些，可以利用 `NSInvocation` 等机制覆盖更多情况，但基本思路就是这样。`NSInvocation` 的很大一部分，也只是内置了对所有需要处理的不同情况的了解。

今天就到这里。愿你平静地编码你的键和值。下次见。由于 Friday Q&A 的主题由读者建议驱动，请[提交你的主题想法](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我正在出售装满这类文章的整套书！第二卷和第三卷现已出版！它们提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论 RSS feed](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2013-02-08-lets-build-key-value-coding.html)

发表想法，发表评论：

垃圾评论和无关内容将被删除，恕不另行通知。违规者可能会被我自行决定公开羞辱。

代码语法高亮由 [Pygments](http://pygments.org/) 提供。
