---
title: Swift 属性观察器
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/swift-property-observers/'
original_language: en
published: 2018-08-20
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:83c1defe842c053b'
translated: true
---

> 原文：[Swift Property Observers](https://nshipster.com/swift-property-observers/)　·　NSHipster (Mattt)

# [Swift 属性观察器](https://nshipster.com/swift-property-observers/)

作者：[Mattt](https://nshipster.com/authors/mattt/)　2018 年 8 月 20 日

到了 20 世纪 30 年代，鲁布·戈德堡已经家喻户晓；他的名字成了《[自动餐巾](https://upload.wikimedia.org/wikipedia/commons/a/a9/Rube_Goldberg%27s_%22Self-Operating_Napkin%22_%28cropped%29.gif)》这类连环画中那些极其复杂又异想天开的发明的代名词。大约在同一时期，阿尔伯特·爱因斯坦在对尼尔斯·玻尔量子力学主流诠释的[批评](https://en.wikipedia.org/wiki/EPR_paradox)中，推广了“鬼魅般的超距作用”这一说法。

近一个世纪后，现代软件开发也成了可被视作戈德堡装置精髓的东西，并借量子计算机日益逼近那个诡异的领域。

作为软件开发者，我们被鼓励在代码中尽可能减少超距作用。这种要求被写进了听上去很有分量的准则，例如[单一职责原则](https://en.wikipedia.org/wiki/Single_responsibility_principle)、[最小惊讶原则](https://en.wikipedia.org/wiki/Principle_of_least_astonishment)和[迪米特法则](https://en.wikipedia.org/wiki/Law_of_Demeter)。不过，尽管它们都担心产生副作用的代码，有些时候这类技术反而能澄清问题，而非制造困惑。

本周讨论的重点正是 Swift 的属性观察器。它为更正式的方案，例如模型-视图-视图模型（MVVM）和函数式响应式编程（FRP），提供了内建且轻量的替代选择。

---

Swift 有两类属性：将状态关联到对象的存储属性，以及基于该状态执行计算的计算属性。例如：

```
struct S {
    // Stored Property
    var stored: String = "stored"

    // Computed Property
    var computed: String {
        return "computed"
    }
}
```

声明存储属性时，可以定义属性被设置时执行的代码块，即属性观察器。新值存储前运行 `willSet` 观察器，之后运行 `didSet` 观察器。无论旧值与新值是否相等，它们都会运行。

```
struct S {
    var stored: String {
        willSet {
            print("willSet was called")
            print("stored is now equal to \(self.stored)")
            print("stored will be set to \(newValue)")
        }

        didSet {
            print("didSet was called")
            print("stored is now equal to \(self.stored)")
            print("stored was previously set to \(oldValue)")
        }
    }
}
```

例如，运行以下代码会在控制台输出：

```
var s = S(stored: "first")
s.stored = "second"
```

- willSet was called
- stored is now equal to first
- stored will be set to second
- didSet was called
- stored is now equal to second
- stored was previously set to first

---

Swift 属性观察器从语言诞生之初就是其中一部分。为了更好地理解原因，先快速看看 Objective-C 的做法：

## Objective-C 中的属性

从某种意义上说，Objective-C 的所有属性都是计算属性。每次通过点语法访问属性时，调用都会转换成等价的 getter 或 setter 方法调用，继而编译成一条消息发送，执行读取或写入实例变量的函数。

```
// Dot accessor
person.name = @"Johnny";

// ...is equivalent to
[person setName:@"Johnny"];

// ...which gets compiled to
objc_msgSend(person, @selector(setName:), @"Johnny");

// ...whose synthesized implementation yields
person->_name = @"Johnny";
```

编程时通常应避免副作用，因为它们会使程序行为难以推理。但很多 Objective-C 开发者已经习惯在需要时向 getter 或 setter 方法注入附加行为。

Swift 对属性的设计将这些模式形式化，并区分了两种副作用：装饰状态访问的副作用（存储属性），以及重定向状态访问的副作用（计算属性）。对于存储属性，`willSet` 和 `didSet` 观察器取代了原本会与 ivar 访问并列的代码。对于计算属性，`get` 和 `set` 访问器取代了你可能在 Objective-C 中为 `@dynamic` 属性实现的代码。

因此，我们获得了更一致的语义，也能对 Key-Value Observing（KVO）与 Key-Value Coding（KVC）这类和属性交互的机制作出更好的保证。

---

那么，Swift 中的属性观察器能做什么？下面给出几个可供考虑的想法：

---

## 验证与规范化值

有时你希望为某个类型可接受的值施加额外约束。

例如，若你正在开发一个要与政府官僚机构交互的 App，就需要确保用户不能提交缺少必填字段或包含无效值的表单。

假设表单要求姓名使用不带变音符号的大写字母，可以用 `didSet` 属性观察器自动移除变音符号并将新值转为大写：

```
var name: String? {
    didSet {
        self.name = self.name?
                        .applyingTransform(.stripDiacritics,
                                            reverse: false)?
                        .uppercased()
    }
}
```

在观察器主体中设置属性（幸运的是）不会触发额外回调，因此这里不会形成无限循环。这也是它不能作为 `willSet` 观察器工作的原因：回调中设置的任何值，都会在属性被设置为 `newValue` 时立即被覆盖。

这种方式可以解决一次性的问题；但若反复使用，强烈说明这里存在可以封装进类型的业务逻辑。

更好的设计是创建 `NormalizedText` 类型，封装此类表单文本的要求：

```
struct NormalizedText {
    enum Error: Swift.Error {
        case empty
        case excessiveLength
        case unsupportedCharacters
    }

    static let maximumLength = 32

    private(set) var value: String

    init(_ string: String) throws {
        if string.isEmpty {
            throw Error.empty
        }

        guard let value = string.applyingTransform(.stripDiacritics,
                                                   reverse: false)?
                                .uppercased(),
              value.canBeConverted(to: .ascii)
        else {
             throw Error.unsupportedCharacters
        }

        guard value.count < NormalizedText.maximumLength else {
            throw Error.excessiveLength
        }

        self.value = value
    }
}
```

可失败或抛错的初始化方法能以 `didSet` 观察器无法做到的方式向调用方暴露错误。现在，像来自_[兰费尔普尔古因吉尔戈格里赫维恩德罗布尔兰蒂西利奥戈戈戈赫](https://en.wikipedia.org/wiki/Llanfairpwllgwyngyll)_的捣蛋鬼 _Jøhnny_ 上门时，我们就可以好好招待他！也就是说，以合理的方式向他传达错误，而不是静默失败或允许无效数据通过。

## 传播依赖状态

属性观察器的另一个潜在用例，是在视图控制器中向依赖组件传播状态。

考虑下面的 `Track` 模型，以及展示它的 `TrackViewController`：

```
struct Track {
    var title: String
    var audioURL: URL
}

class TrackViewController: UIViewController {
    var player: AVPlayer?

    var track: Track? {
        willSet {
            self.player?.pause()
        }

        didSet {
            guard let track = self.track else {
                return
            }

            self.title = track.title

            let item = AVPlayerItem(url: track.audioURL)
            self.player = AVPlayer(playerItem: item)
            self.player?.play()
        }
    }
}
```

设置视图控制器的 `track` 属性时，会自动发生以下事情：

1. 暂停上一首曲目的音频
2. 将视图控制器的 `title` 设为新曲目的标题
3. 加载并播放新曲目的音频

*很酷，对吧？*

你甚至可以像[_捕鼠记_的那一幕](https://www.youtube.com/watch?v=TVAhhVrpkwM)那样，让多个被观察属性层层触发这种行为。

---

一般而言，编程时应避免副作用，因为它们会使复杂行为难以推理。下次想使用这个新工具时，请记住这一点。

但站在这座摇摇欲坠的抽象高塔最顶端，拥抱系统的混乱有时会很诱人，或许也值得。总是遵守规则，实在太 *Bohr* 了。
