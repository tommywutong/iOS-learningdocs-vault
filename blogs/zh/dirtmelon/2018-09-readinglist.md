---
title: 2018-09-ReadingList
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/2018-09-ReadingList/'
original_language: zh
published: 2018-10-05
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0d9a3c8fb7ea1c09'
translated: n/a
---

> 原文：[2018-09-ReadingList](https://dirtmelon.github.io/posts/2018-09-ReadingList/)　·　dirtmelon

[Swift 4 泛型：如何在你的代码或App里应用泛型](https://swift.gg/2018/08/28/swift-generics/) 如何在 Swift 中应用泛型，比较基础。

[Swift 中的属性](https://swift.gg/2018/09/18/properties-in-swift/) Swift 属性相关说明，一些属性相关的基础用法。

[Defer usage in Swift](https://www.avanderlee.com/swift/defer-usage-swift/) defer 在 swift 中的运行机制，defer 的执行顺序是按照声明顺序倒序执行，介绍了几个在 swift 中使用 defer 的场景，可以预先设定在函数完成后需要执行的方法。我大部分用到 defer 的场景就是取消 tableView/collectionView 的选中效果。

[CompactMap vs flatMap: The differences explained](https://www.avanderlee.com/swift/compactmap-flatmap-differences-explained/) compactmap 与 flatmap 的不同之处，如果数组为 optional ，想转换为 nonoptional，则使用 compactmap ，flatmap 则是将多维数组降为一维。

[Never](https://swift.gg/2018/08/30/never/) 介绍了 `Never` 这个无实例类型，以及如何使用 `Never` 来优化代码中的不可能情况。

[Private properties in protocols](http://alisoftware.github.io/swift/protocols/2018/09/02/protocols-private-properties/) 在 Swift 中，protocols 不支持定义属性的访问控制权，但是有时候你不想暴露这些属性。这篇文章介绍了如何使用一个嵌套类型和 `fileprivate` 来使得属性私有化。

[Switching with Associated Values](https://www.objc.io/blog/2018/09/04/switching-with-associated-values/) 如何在多重 `switch` 中优化代码。

[Design Patterns in Swift #1: Factory Method and Singleton](https://www.appcoda.com/design-pattern-creational/) [Design Patterns in Swift #2: Observer and Memento](https://www.appcoda.com/design-pattern-behavorial/) [Design Patterns in Swift #3: Facade and Adapter](https://www.appcoda.com/design-pattern-structural) 设计模式三连发。 第一篇为工厂模式和单例模式，工厂模式结合 `protocol` 对类进行抽象。 第二篇为观察者模式和备忘录模式，观察者模式结合了 `protocol` 和 `enum` 来讲述如何实现在 Swift 中实现观察者模式，备忘录模式则是 `protocol` 和 `UserDefaults` 相结合来实现数据持久化。 第三篇为外观模式和适配器模式，外观模式还是通过 `protocol` 进行封装成统一的接口。适配器模式也是结合 `protocol` 来说明如何对接口进行调整。
