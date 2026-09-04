---
title: 'Friday Q&A 2012-07-06：让我们构建 NSNumber'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-07-06-lets-build-nsnumber.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:75715e668c01132a'
translated: true
---

> 原文：[Last time](https://www.mikeash.com/pyblog/friday-qa-2012-07-06-lets-build-nsnumber.html)　·　mikeash.com Friday Q&A

发表于 2012-07-06 15:08 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2012-07-27：构建 Tagged Pointer](https://www.mikeash.com/pyblog/friday-qa-2012-07-27-lets-build-tagged-pointers.html)  
上一篇：[Friday Q&A 2012-06-22：Objective-C 字面量](https://www.mikeash.com/pyblog/friday-qa-2012-06-22-objective-c-literals.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2012-07-06：让我们构建 NSNumber

作者：[Mike Ash](https://www.mikeash.com/)

**总览**  
与许多（但并非全部）面向对象语言一样，Objective-C 在对象与非对象之间划了一道界线。对象响应消息，可以在运行时不问其确切类型地加以查询、放进集合、比较相等性，并共享一整套共同行为。非对象则基本是编译期构造物，它们的类型信息在运行时几乎荡然无存。在 Objective-C 中，这些非对象就是一切来自 C 的东西：从整数 `42` 到字符串 `"Hello, world"`，再到复杂的结构体。

装箱（boxing）就是把这些非对象装进一个对象的过程，让它们能像其他对象一样使用，典型目的是放进集合。`NSNumber` 就是 Cocoa 中用来给 C 数字装箱的类。你可以有装 `NSNumber` 的 `NSArray`，却不能有装 `int` 的 `NSArray`。`NSNumber` 在 Cocoa 编程里出场率极高：凡是 Cocoa 集合要存一个数字的地方，几乎都有 `NSNumber`。除此之外，当你让 `NSUserDefaults` 保存一个数字时，它存取的也正是 `NSNumber` 对象。

**接口**  
我们的替身版 `NSNumber` 将被称作 `MANumber`。Cocoa 版本是更通用的装箱类 `NSValue` 的子类，与它不同，这个类直接继承 `NSObject`：

```
    @interface MANumber : NSObject
```

初始化实例的方法有_一大堆_。每种 C 数值类型各有一个初始化方法，外加一些 Cocoa 特有类型的方法：

```
    - (id)initWithChar:(char)value;
    - (id)initWithUnsignedChar:(unsigned char)value;
    - (id)initWithShort:(short)value;
    - (id)initWithUnsignedShort:(unsigned short)value;
    - (id)initWithInt:(int)value;
    - (id)initWithUnsignedInt:(unsigned int)value;
    - (id)initWithLong:(long)value;
    - (id)initWithUnsignedLong:(unsigned long)value;
    - (id)initWithLongLong:(long long)value;
    - (id)initWithUnsignedLongLong:(unsigned long long)value;
    - (id)initWithFloat:(float)value;
    - (id)initWithDouble:(double)value;
    - (id)initWithBool:(BOOL)value;
    - (id)initWithInteger:(NSInteger)value;
    - (id)initWithUnsignedInteger:(NSUInteger)value;
```

这些类型也各有取值方法：

```
    - (char)charValue;
    - (unsigned char)unsignedCharValue;
    - (short)shortValue;
    - (unsigned short)unsignedShortValue;
    - (int)intValue;
    - (unsigned int)unsignedIntValue;
    - (long)longValue;
    - (unsigned long)unsignedLongValue;
    - (long long)longLongValue;
    - (unsigned long long)unsignedLongLongValue;
    - (float)floatValue;
    - (double)doubleValue;
    - (BOOL)boolValue;
    - (NSInteger)integerValue;
    - (NSUInteger)unsignedIntegerValue;
```

注意，无论当初用的是哪个初始化方法，这些取值方法都可用。`MANumber` 必须自行完成相应的转换。

最后，还有几个用于字符串转换和比较的方法：

```
    - (NSString *)stringValue;
    - (NSComparisonResult)compare:(MANumber *)otherNumber;
    - (BOOL)isEqualToNumber:(MANumber *)number;
    - (NSString *)descriptionWithLocale:(id)locale;
```

**实现策略**  
`MANumber` 将用一个 `union` 来存放底层数值。`union` 是标准 C 中少见的特性。它看上去和 `struct` 一模一样，工作方式却不同。`struct` 把多个值一起存在一处；`union` 也这样存，但你只能访问最后一次存入的那个。当你向 `union` 存入一个值时，其余所有字段的值都变成未定义。

以 C 典型的「帮不上忙但很高效」的风格，编译器不强制这条规则，也不会帮你遵守它——比如说，它不会让你查询最后设置的是哪个字段。你得自己记着这件事，通常靠一个配套的 `enum`。

`union` 可以用来装下每一种 C 数值类型，再配一个大 `enum` 标明当前用的是哪个。然而这就过于复杂了。我们真正需要的只有三个字段：最大的整数类型、最大的无符号整数类型、最大的浮点类型。在必须处理的类型中，它们分别是 `long long`、`unsigned long long` 和 `double`。其他一切类型都能与这三者无损互转。

这一实现与 `NSNumber` 的实现并不完全一致——后者会记住创建时用的具体类型。不过，用这三种类型已经足够接近，还省掉了大量重复代码。`NSNumber` 精确追踪原始类型这一点，多数时候根本看不出来，只有在使用 `-descriptionWithLocale:` 或 `-objCType` 这类方法时才会露馅。

**存储**  
实例变量如下：

```
    @implementation MANumber {
        enum { INT, UINT, DOUBLE } _type;
        union {
            long long i;
            unsigned long long u;
            double d;
        } _value;
    }
```

`_type` 变量持有一个匿名 `enum`，说明值是 `INT`（`long long`）、`UINT`（`unsigned long long`）还是 `DOUBLE`（猜猜看）。`_value` 变量则持有真正的数字，用的是 `union`，所以最终只存下一个。

代码会在各个初始化方法里设置 `_type` 和相应的 `_value`。取值方法随后检查 `_type`，按需取出值。

**初始化方法**  
为应付所有不同类型，有一大堆样板代码。所有有符号整数类型都直接转发到 `initWithLongLong:`，无符号类型则转发到 `initWithUnsignedLongLong:`

```
    - (id)initWithChar:(char)value
    {
        return [self initWithLongLong: value];
    }

    - (id)initWithUnsignedChar:(unsigned char)value
    {
        return [self initWithUnsignedLongLong: value];
    }

    - (id)initWithShort:(short)value
    {
        return [self initWithLongLong: value];
    }

    - (id)initWithUnsignedShort:(unsigned short)value
    {
        return [self initWithUnsignedLongLong: value];
    }

    - (id)initWithInt:(int)value
    {
        return [self initWithLongLong: value];
    }

    - (id)initWithUnsignedInt:(unsigned int)value
    {
        return [self initWithUnsignedLongLong: value];
    }

    - (id)initWithLong:(long)value
    {
        return [self initWithLongLong: value];
    }

    - (id)initWithUnsignedLong:(unsigned long)value
    {
        return [self initWithUnsignedLongLong: value];
    }

    - (id)initWithBool:(BOOL)value
    {
        return [self initWithLongLong: value];
    }

    - (id)initWithInteger:(NSInteger)value
    {
        return [self initWithLongLong: value];
    }

    - (id)initWithUnsignedInteger:(NSUInteger)value
    {
        return [self initWithUnsignedLongLong: value];
    }
```

这些初始化方法随后只需设置 `_type`、`_value` 并返回 `self`。（注意，为简短起见我省略了对 `[super init]` 的传统调用——超类是 `NSObject` 时它并非严格必需，虽然仍是好习惯。）

```
    - (id)initWithLongLong:(long long)value
    {
        _type = INT;
        _value.i = value;
        return self;
    }

    - (id)initWithUnsignedLongLong:(unsigned long long)value
    {
        _type = UINT;
        _value.u = value;
        return self;
    }
```

浮点初始化方法类似。`float` 那个直接转发到 `initWithDouble:`，后者只需恰当地设置 `_type` 和 `_value`：

```
    - (id)initWithFloat:(float)value
    {
        return [self initWithDouble: value];
    }

    - (id)initWithDouble:(double)value
    {
        _type = DOUBLE;
        _value.d = value;
        return self;
    }
```

**取值方法**  
取值方法比初始化方法还要相似。它们都检查 `_type`，然后返回 `_value` 中当前生效的字段。从 `_value` 的活动字段到请求的返回类型之间的最后一道转换，编译器会替你完成。

既然这些方法都包含相同的代码，那就是用宏封装相同部分的最佳候选。下面这个宏检查 `_type`，然后返回 `_value` 中相应的字段：

```
    #define RETURN() do { \
            if(_type == INT) \
                return _value.i; \
            else if(_type == UINT) \
                return _value.u; \
            else \
                return _value.d; \
        } while(0)
```

有了这个宏，取值方法几乎是自己写自己：

```
    - (char)charValue
    {
        RETURN();
    }

    - (unsigned char)unsignedCharValue
    {
        RETURN();
    }

    - (short)shortValue
    {
        RETURN();
    }

    - (unsigned short)unsignedShortValue
    {
        RETURN();
    }

    - (int)intValue
    {
        RETURN();
    }

    - (unsigned int)unsignedIntValue
    {
        RETURN();
    }

    - (long)longValue
    {
        RETURN();
    }

    - (unsigned long)unsignedLongValue
    {
        RETURN();
    }

    - (long long)longLongValue
    {
        RETURN();
    }

    - (unsigned long long)unsignedLongLongValue
    {
        RETURN();
    }

    - (float)floatValue
    {
        RETURN();
    }

    - (double)doubleValue
    {
        RETURN();
    }

    - (NSInteger)integerValue
    {
        RETURN();
    }

    - (NSUInteger)unsignedIntegerValue
    {
        RETURN();
    }
```

真是又多又无聊又丑的代码。

这片整齐划一的宏调用海洋中唯一的例外是 `-boolValue` 方法。既然 `BOOL` 冒充真正的布尔值，这个方法对存进 `MANumber` 对象的任何非零值都应返回 `YES`。编译器的内建转换做不到这一点。比如整数 `256` 转换成 `BOOL` 会返回 NO，因为 `BOOL` 只是个 `signed char`，一个 8 位整数。正因如此，`-boolValue` 复刻了宏的逻辑，但带上了对零的显式检查：

```
    - (BOOL)boolValue
    {
        if(_type == INT)
            return _value.i != 0;
        else if(_type == UINT)
            return _value.u != 0;
        else
            return _value.d != 0;
    }
```

**字符串转换**  
有两个字符串转换方法：`-stringValue` 和 `-descriptionWithLocale:`。`-stringValue` 只是带着 `nil` 参数调用 `-descriptionWithLocale:`：

```
    - (NSString *)stringValue
    {
        return [self descriptionWithLocale: nil];
    }
```

`-descriptionWithLocale:` 再用 `-[NSString initWithFormat:locale:]` 构建字符串。这里没有什么花哨的办法应对不同数值类型，只能检查 `_type`，每种情况用不同的格式串：

```
    - (NSString *)descriptionWithLocale:(id)locale
    {
        if(_type == INT)
            return [[NSString alloc] initWithFormat: @"%lld" locale: locale, _value.i];
        else if(_type == UINT)
            return [[NSString alloc] initWithFormat: @"%llu" locale: locale, _value.u];
        else
            return [[NSString alloc] initWithFormat: @"%f" locale: locale, _value.d];
    }
```

注意我用的是 ARC，所以这里没有 `autorelease` 调用。

**比较**  
比较方法开始有意思了，因为它们要在不同类型的 `MANumber` 对象之间工作。比如，`double` 值 `-1.1` 应当比较为小于无符号整数值 `99999`。

类型有九种排列，所以要处理九种不同情形。通过强制一个顺序，可以把它缩减为六种。如果两个对象的类型是 `INT` 和 `UINT`，本来两种情形可以合并成一种：只处理 `self` 为 `INT`、对方为 `UINT` 的情形，若出现相反的顺序就把两个对象对调。

为了帮忙在不同类型之间做比较，我写了一个简单的宏，接受两个数字并返回相应的 `NSComparisonResult`。它所做的只是接受两个参数、存进临时变量以避免多次求值，然后按二者的大小关系返回相应的常量。这里还有一点浮点戏法。对浮点数来说，`NAN`（非数字，not a number）与任何东西比较都不相等，与它的一切比较都是假。`NSComparisonResult` 无法表示一种意为「这个数不等于任何数，连它自己也不等于」的排序关系，所以我武断地规定：就 `MANumber` 的比较而言，`NAN` 等于它自身、小于任何其他数：

```
    #define COMPARE(a, b) do { \
            __typeof__(a) __a_local = a; \
            __typeof__(b) __b_local = b; \
            BOOL __a_isnan = isnan(__a_local); \
            BOOL __b_isnan = isnan(__b_local); \
            if(__a_isnan && __b_isnan) \
                return NSOrderedSame; \
            else if(__a_isnan) \
                return NSOrderedAscending; \
            else if(__b_isnan) \
                return NSOrderedDescending; \
            else if(__a_local > __b_local) \
                return NSOrderedDescending; \
            else if(__a_local < __b_local) \
                return NSOrderedAscending; \
            else \
                return NSOrderedSame; \
        } while(0)
```

比较方法本身做的第一件事，是取出待比较两个对象的类型：

```
    - (NSComparisonResult)compare:(MANumber *)otherNumber
    {
        int selfType = _type;
        int otherType = otherNumber->_type;
```

如果两个类型的顺序不对，我们就反转比较：把参数倒过来再调用一次 `compare:`，并返回结果的反值。既然 `NSComparisonResult` 无非是 `-1`、`0` 或 `1`，取负就能反转它的含义：

```
        if(selfType > otherType)
            return -[otherNumber compare: self];
```

现在剩下的是排好序的类型，共六种情形。如果 `selfType` 是 INT，`otherType` 可为任何值。如果 `selfType` 是 `UINT`，`otherType` 只能是 `UINT` 或 `DOUBLE`。如果 `selfType` 是 `DOUBLE`，`otherType` 必然也是 `DOUBLE`。

来看 `selfType` 为 `INT` 的情形。若两个值都是 `INT`，代码很简单：

```
        if(selfType == INT)
        {
            if(otherType == INT)
            {
                COMPARE([self longLongValue], [otherNumber longLongValue]);
            }
```

如果 `otherType` 是 `UINT`，要多费点事。直接与 `[otherNumber unsignedLongLongValue]` 比较行不通。C 会在比较前把 `[self longLongValue]` 提升为无符号，把负数变成正数，毁掉整个比较。正因如此，`-1` 会比较为大于 `1`。为了避免这一点，我们对负数做专门检查，确认双方都为正之后再比较它们的无符号值：

```
            else if(otherType == UINT)
            {
                if([self longLongValue] < 0)
                    return NSOrderedAscending;
                else
                    COMPARE([self unsignedLongLongValue], [otherNumber unsignedLongLongValue]);
            }
```

接下来是 `DOUBLE` 的情形。这就相当复杂了，因为浮点数的工作方式与整数差别很大。这里有几个不同的子情形，我逐个来讲。不过它做的第一件事是从对方取 `doubleValue`，方便后续处理：

```
            else
            {
                double other = [otherNumber doubleValue];
```

`double` 的表示范围比 `long long` 大得多。第一个子情形是找出 `long long` 能容纳的最大数，看看 `other` 是否超出。若超出，它显然大于 `self`，因为 self 是个 `long long`。

内建宏 `LLONG_MAX` 给出 `long long` 能容纳的最大数。但我们不能把它直接转换成 `double`。那个数等于 2^63-1，在 `double` 中无法表示。由于 `double` 的内部格式，一旦超过 2^54，它就只能表示偶数。为了准确完成比较，我们算出比最大 `long long` 再多一的数——加法时小心使用 `unsigned` 类型——然后与它比较：

```
                double longLongMaxPlusOne = LLONG_MAX + 1ULL;
                if(other >= longLongMaxPlusOne)
                    return NSOrderedAscending;
```

负方向也要检查。这稍微容易些，因为最小的 `long long` 可以直接用 `double` 表示：

```
                if(other < LLONG_MIN)
                    return NSOrderedDescending;
```

如果程序还能走到这里，说明这个 `double` 落在 `long long` 的范围内，二者需要直接比较。但我们不能直接掏出 `>` 运算符了事，因为有许多 `double` 无法用 `long long` 表示（比如 `1.5`），也有许多 `long long` 无法用 `double` 表示（比如超过某个阈值后的任何奇数，如前所述）。

超过某个阈值后，`double` 只能表示整数值，因为数值的大小超出了表示格式的精度。在阈值之上、且低于 `long long` 最大值时，`double` 可以安全地转换成 `long long` 而不损失精度，两个值就可以按 `long long` 比较。在阈值之下，`double` 能表示任何整数，因此 `long long` 可以安全地转换成 `double` 而不损失精度，两个值按 `double` 比较。

这个阈值的位置其实不难确定。C 提供宏 `DBL_MANT_DIG`，给出 `double` 类型的精度。以它为指数计算 2 的幂（`double` 是二进制表示），就得到了阈值：

```
                double pureIntegerStart = 1LL << DBL_MANT_DIG;
```

然后根据 `other` 相对阈值的位置做简单比较。注意该阈值对负数同样适用，所以必须双向检查：

```
                if(other >= pureIntegerStart || other <= -pureIntegerStart)
                    COMPARE([self longLongValue], (long long)other);
                else
                    COMPARE([self doubleValue], other);
            }
        }
```

接下来是 `selfType` 为 `UINT` 的情形。与前面一样，当 `otherType` 也是 `UINT` 时，代码很简单：

```
        else if(selfType == UINT)
        {
            if(otherType == UINT)
            {
                COMPARE([self unsignedLongLongValue], [otherNumber unsignedLongLongValue]);
            }
```

由于上面做了类型排序，这里不必处理 `INT`。继续看 `DOUBLE`，它又一次复杂起来。与前面一样，把 `otherNumber` 的值取进一个局部变量：

```
            else
            {
                double other = [otherNumber doubleValue];
```

我们做的第一件事是看 `other` 是否为负。若是，顺序就已确定，因为 `self` 是无符号的（因此要么为零，要么为正）：

```
                if(other < 0)
                    return NSOrderedDescending;
```

否则，做与之前相同的基本阈值计算。这次要把 `other` 与最大的 `unsigned long long` 比较。这有点棘手。与 `long long` 一样，必须加 `1` 才能得到一个能当 `double` 用的数。然而，比最大 `unsigned long long` 更大的任何数我们都无法用整数表示，因为 `unsigned long long` 已经是最大的整数类型。于是改为计算 `(LLONG_MAX + 1) * 2`，它比最大的 `unsigned long long` 大一，同时小心使用全部正确的类型，避免溢出或精度损失：

```
                double unsignedLongLongMaxPlusOne = (double)(LLONG_MAX + 1ULL) * 2.0;
                if(other >= unsignedLongLongMaxPlusOne)
                    return NSOrderedAscending;
```

此时可以确定两个数都在各自类型的范围内，于是沿用与之前相同的 `pureIntegerStart` 策略直接比较：

```
                double pureIntegerStart = 1LL << DBL_MANT_DIG;
                if(other >= pureIntegerStart)
                    COMPARE([self unsignedLongLongValue], (unsigned long long)other);
                else
                    COMPARE([self doubleValue], other);
            }
        }
```

最后剩下的是 `DOUBLE` 情形，其实非常容易。由于类型排序，这里唯一可能的情形是双方都是 `DOUBLE`，直接比较即可：

```
        else
        {
            COMPARE([self doubleValue], [otherNumber doubleValue]);
        }
    }
```

`compare:` 实现完毕，相等性检查就是小菜一碟：

```
    - (BOOL)isEqualToNumber:(MANumber *)number
    {
        return [self compare: number] == NSOrderedSame;
    }
```

我们还需要来自 `NSObject` 的 `isEqual:`。它可以先检查对方的类，再借力 `isEqualToNumber:`

```
    - (BOOL)isEqual: (id)other
    {
        if(![other isKindOfClass: [MANumber class]])
            return NO;

        return [self isEqualToNumber: other];
    }
```

最后，既然重写了 `isEqual:`，就必须一并重写 `hash`。由于浮点数的语义，`hash` 的实现略有些棘手。对非浮点值，直接返回整数值作为哈希即可：

```
    - (NSUInteger)hash
    {
        if(_type != DOUBLE)
            return [self unsignedIntegerValue];
```

对恰为整数值的浮点数，我们想做同样的事。既然我们的 `isEqual:` 把整数值的 `DOUBLE` 视为与同值的 `INT` 或 `UINT` 相等，我们就_必须_返回与等价 `INT`/`UINT` 相同的哈希。为此，检查这个 `DOUBLE` 值是否真为整数，是则返回整数值：

```
        if(_value.d == floor(_value.d))
            return [self unsignedIntegerValue];
```

再往下就是非整数值了。终极目标是直接返回 `double` 的位模式（bit pattern），它能给出很好的哈希。然而这只对「位模式相等即意味着 `isEqual:`」的数成立，而并非所有 `double` 都如此。首先是 `NAN`：我们让它与自身比较相等，但它有许多种不同的位表示。为处理它，显式检查 `NAN` 并为它返回一个常量哈希：

```
        if(isnan(_value.d))
            return 0;
```

另一个特殊情况更怪一点。IEEE 754 浮点数（如今几乎任何 CPU 用的都是这种）的零有两个可能的值：正零与负零。它们通常无法区分——比较相等，对多数计算也给出相同结果。但它们的位模式不同，所以必须为它们做特殊处理。我利用负零与正零比较相等这一点做了一个简单检查，为两种零返回同一个常量哈希：

```
        if(_value.d == 0.0)
            return 0;
```

排除掉所有特殊情况之后，代码若能走到这里，这个数必然满足「数值相等即位模式相等」。于是直接返回位模式作为哈希。做法是返回 `union` 的 `u` 字段：

```
        return _value.u;
    }
```

且慢！我前面说过，`union` 中除最后设置的字段外，其他字段都不许访问，所以这里明显违规。虽然按语言规范这确实不允许，但各家 C 编译器早已达成默契：允许这种访问，只是把现存的值重新解释一遍。这段代码取出 `union` 里存的 `double`，把它的位按 `unsigned long long` 重新解释——这正是我们想要的。严格说这依赖未定义行为（undefined behavior），但我们实际在用的编译器都正式认可这种写法。

**结语**  
`NSNumber` 是一个概念上很简单的类，它存在的主要意义就是让我们能把数值塞进 Cocoa 集合，但它的灵活性意味着底层有相当的复杂度。通过实现一个功能等效的 `MANumber` 类，我们可以看清 `NSNumber` 内部都得干些什么。向不同整数类型的自动转换需要大量样板代码，而不同类型数字之间可靠的相互转换也会变得相当复杂。

今天就到这里。下次再见，届时又是一期 Friday Q&A。一如既往，Friday Q&A 由读者的建议驱动，如果你有想看的主题，请[发给我](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我还在销售整本整本的文章合集！第二卷和第三卷已经出版，提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里了解详情](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论的 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-07-06-lets-build-nsnumber.html)

发表你的想法，发一条评论：

垃圾内容和离题帖子将被无通知删除。发帖者可能会按我的个人判断被公开羞辱。

代码语法高亮由 [Pygments](http://pygments.org/) 提供。
