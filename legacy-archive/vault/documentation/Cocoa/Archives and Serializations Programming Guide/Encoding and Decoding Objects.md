---
title: 归档与序列化编程指南
apple_id: 10000047i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2012-07-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Articles/codingobjects.html
archived_at: '2026-07-15T05:25:42.003741Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [归档与序列化编程指南](Introduction.md)


[下一页](Encoding%20and%20Decoding%20C%20Data%20Types.md)[上一页](Creating%20and%20Extracting%20Archives.md)

# 编码和解码对象

要支持实例的编码和解码，一个类必须采纳 `NSCoding` [协议](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45) 并实现其方法。该协议声明了两个方法，它们会被发送给正在被编码或解码的对象。

按照面向对象设计原则，被编码或解码的对象负责编码和解码自身的状态。编码器通过调用 `encodeWithCoder:` 或 `initWithCoder:` 来指示对象执行该操作。`encodeWithCoder:` 方法指示对象使用给定的编码器编码自身的状态；一个对象可以任意次数地收到这个方法。`initWithCoder:` 消息指示对象根据给定编码器中的数据初始化自身；因此，它会取代其他任何初始化方法，并且每个对象只会收到一次该消息。

当一个对象收到 `encodeWithCoder:` 消息时，它应该在将消息转发给其超类（如果超类也符合 `NSCoding` 协议）之后，编码其所有重要状态（通常由其属性或实例变量表示）。对象不必编码它的全部状态。有些值可能没有必要重新建立，另一些则可以在解码时从相关状态推导出来。其他状态则应仅在特定条件下才被编码（例如使用 `encodeConditionalObject:`，如 [Conditional Objects](Archives.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2dmljrgqzdemby) 中所述）。

你可以使用诸如 `encodeObject:forKey:` 之类的编码方法，来编码 id、标量、C 数组、结构体、字符串，以及指向这些类型的指针。有关方法的完整列表，请参阅 [NSKeyedArchiver](https://developer.apple.com/documentation/foundation/nskeyedarchiver) 类规范。例如，假设你创建了一个 Person 类，它具有名字、姓氏和身高的属性；你可能会像下面这样实现 `encodeWithCoder:`

```objc
- (void)encodeWithCoder:(NSCoder *)coder {
    [coder encodeObject:self.firstName forKey:ASCPersonFirstName];
    [coder encodeObject:self.lastName forKey:ASCPersonLastName];
    [coder encodeFloat:self.height forKey:ASCPersonHeight];
}
```

这个示例假设 Person 的超类没有采纳 `NSCoding` 协议。如果你的类的超类采纳了 `NSCoding`，你应该在调用其他任何编码方法之前，先调用超类的 `encodeWithCoder:` 方法：

```objc
- (void)encodeWithCoder:(NSCoder *)coder {
    [super encodeWithCoder:coder];
    // Implementation continues.
```

`@encode()` 编译器指令会根据类型表达式生成一个 Objective-C 类型编码，该编码可以用作 `encodeValueOfObjCType:at:` 的第一个参数。更多信息请参阅 _[The Objective-C Programming Language](../The%20Objective-C%20Programming%20Language/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrt)_ 中的 "Type Encodings"。

在 `initWithCoder:` 方法的实现中，对象应先调用其超类的指定初始化方法来初始化继承的状态，然后再解码并初始化自己的状态。这些键可以按任意顺序解码。Person 的 `initWithCoder:` 实现可能如下所示：

```objc
- (id)initWithCoder:(NSCoder *)coder {
    self = [super init];
    if (self) {
        _firstName = [coder decodeObjectForKey:ASCPersonFirstName];
        _lastName = [coder decodeObjectForKey:ASCPersonLastName];
        _height = [coder decodeFloatForKey:ASCPersonHeight];
    }
    return self;
}
```

如果超类采纳了 `NSCoding` 协议，你应先将 `initWithCoder:` 的返回值赋给 `self`：

```objc
- (id)initWithCoder:(NSCoder *)coder {
    self = [super initWithCoder:coder];
    if (self) {
        // Implementation continues.
```

之所以要在子类中这样做，是因为超类在其 `initWithCoder:` 的实现中，可能会决定返回一个不是自身的其他对象。

你为一个对象编码的内容越少，需要解码的内容也就越少，读写归档的速度也就越快。停止写出那些对该类已不再重要的项（尽管在非键控编码下你可能不得不继续写出它们）。

编码和解码布尔值比将单个 1 位位域作为整数编码和解码更快、开销更低。不过，将多个位域编码为单个整数值的开销可能比逐个编码更低，但这也可能给日后的兼容性工作带来更多复杂性（参见 [Structures and Bit Fields](Encoding%20and%20Decoding%20C%20Data%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4tiljzgy4timi)）。

不要读取你不需要的键。你不像非键控编码那样，被要求读取归档中特定对象的全部信息，而且不这样做的成本要低得多。不过，未读取的数据仍然会增加归档的大小，因此如果你不需要读取某些数据，也应停止写出它们。

直接解码某个键对应的值，要比先检查该值是否存在再解码更快。只有当你需要区分（由于不存在而产生的）默认返回值与恰好与默认值相同的真实值时，才应调用 `containsValueForKey:`。

通常来说，解码速度比编码速度更重要。如果存在某种权衡，能以降低编码性能为代价提升解码性能，通常这种权衡是合理的。

避免使用 “$” 作为键的前缀。键控归档器和解档器使用以 “$” 为前缀的键来存储内部值。虽然它们会检测并处理带有 “$” 前缀的用户自定义键，但这种额外开销会使归档速度变慢。

在编码或解码期间，编码器对象会调用一些方法，允许被编码的对象用一个替代类或替代实例来替换自身。这使得归档可以在具有不同类层次结构、或者仅仅是同一个类不同版本的多种实现之间共享。例如，类簇（class cluster）就利用了这一特性。这个特性还允许那些需要维护唯一实例的类，在解码时强制执行这一策略。例如，对于给定的字体和字号，应该只存在一个 `NSFont` 实例。

替换方法由 `NSObject` 声明，分为通用和专用两类。以下是通用方法：

| 方法 | 典型用途 |
| --- | --- |
| `classForCoder` | 允许对象在被编码之前，用另一个类替换自身所属的类。例如，类簇的私有子类在被归档时会用其公共超类的名称替换自身。 |
| `replacementObjectForCoder:` | 允许对象在被编码之前，用另一个实例替换自身。 |
| `awakeAfterUsingCoder:` | 允许对象在被解码之后，用另一个对象替换自身。例如，表示字体的对象在解码后，可能会返回一个与自身具有相同字体描述的已存在对象。这样，冗余的对象就可以被消除。 |

专用替换方法与 `classForCoder` 和 `replacementObjectForCoder:` 类似，但它们是为特定的具体编码器子类设计（并由其调用）的。例如，`classForArchiver` 和 `replacementObjectForPortCoder:` 分别由 `NSArchiver` 和 `NSPortCoder` 使用。通过实现这些专用方法，你的类可以根据所使用的具体编码器类来调整其编码行为。有关这些方法的更多信息，请参阅 `NSObject` 类规范中相应的方法说明。

除了刚才讨论的方法之外，`NSKeyedArchiver` 和 `NSKeyedUnarchiver` 还允许委托对象在编码之前和解码之后执行最终的替换操作。`NSKeyedArchiver` 对象的委托可以实现 `archiver:willEncodeObject:`，`NSKeyedUnarchiver` 对象的委托可以实现 `unarchiver:didDecodeObject:` 来执行替换。

在某些情况下，一个类可能实现了 `NSCoding` 协议，但不支持一种或多种编码器类型。例如，`NSDistantObject`、`NSInvocation`、`NSPort` 及其子类采纳 `NSCoding` 仅是为了在分布式对象系统中供 `NSPortCoder` 使用；它们不能被编码进归档中。在这种情况下，一个类可以测试编码器是否属于特定类型，如果不受支持则抛出异常。如果限制仅仅是将某个类限定为只能用于顺序归档或键控归档，你可以向编码器发送 `allowsKeyedCoding` 消息；否则，你可以像下面的示例那样测试编码器的类身份。

```objc
- (void)encodeWithCoder:(NSCoder *)coder {
    if ([coder isKindOfClass:[NSKeyedArchiver class]]) {
        // encode object
    }
    else {
        [NSException raise:NSInvalidArchiveOperationException
                    format:@"Only supports NSKeyedArchiver coders"];
    }
}
```

在其他情况下，一个类可能从超类继承了 `NSCoding`，但子类并不想支持编码。例如，`NSWindow` 从 `NSResponder` 继承了 `NSCoding`，但它并不支持编码。在这种情况下，该类应该重写 `initWithCoder:` 和 `encodeWithCoder:` 方法，使它们在被调用时抛出异常。

[下一页](Encoding%20and%20Decoding%20C%20Data%20Types.md)[上一页](Creating%20and%20Extracting%20Archives.md)
