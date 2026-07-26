---
title: 'JavaScriptCore Tutorial for iOS: Getting Started'
source: 南峰子 (southpeak)
source_key: southpeak
source_url: 'https://southpeak.github.io/2016/08/01/javascriptcore-tutorial-for-ios-getting-started/'
original_language: zh
published: 2016-08-28
status: frozen
license: © 2017 南峰子（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6d2aa03cc6d79bf0'
translated: n/a
---

> 原文：[JavaScriptCore Tutorial for iOS: Getting Started](https://southpeak.github.io/2016/08/01/javascriptcore-tutorial-for-ios-getting-started/)　·　南峰子 (southpeak)

> 本文由József Vesza发表于raywenderlich，原文地址是[https://www.raywenderlich.com/124075/javascriptcore-tutorial](https://www.raywenderlich.com/124075/javascriptcore-tutorial)

自从2014年Swift发布以来，其受欢迎程度直线上升：从TIOBE的数据来看，在2016年二月份，它的排名已经上升到第16位。不过，同时我们可以看到排名第9位的是Javascript，这门语言与Swift有许多不同之处：Swift在编译时安全性上做了很多努力，而Javascript是弱类型且动态的。

Swift与Javascript有很多不一样的地方，不过有一件事却将他们紧紧绑在一起：你可以使用他们来创建一个轻量级的iOS应用。

在这篇JavaScriptCore的教程中，你将构建一个用于显示类似web页面的iOS应用，并重用web页面现存的Javascript代码。特别是你将了解以下几点：

- JavaScriptCore框架的组件
- 如何在iOS代码中调用Javascript方法
- 如何在Javascript代码中访问本地代码

> 注：你不需要有JavaScript的经验。如果这篇JavaScriptCore教程已经激起你学习这门语言的兴趣，那么[Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/JavaScript)对于初学者来说是一个非常棒的资源 - 或者你也可以选择看[这里](http://blog.wix.engineering/wp-content/uploads/2015/04/mIuuwgx-1024x576.jpg)介绍的两本书。

## 入门

下载这篇教程的[初始工程](http://www.raywenderlich.com/wp-content/uploads/2016/02/Showtime-Starter.zip)并解压。你可以看到下面的目录结构：

- Web：包含将被转换为iOS应用的web页面的HTML和CSS文件。
- Native：iOS工程。文章中所有的修改都是在这里。
- js：包含用于工程的Javascript代码。

App名叫Showtime，用于搜索iTunes上的付费电影。为了查看它的效果，可以用浏览器打开Web/index.html页面，输入你要的价格，然后按下`return`按钮。

![image](https://cdn2.raywenderlich.com/wp-content/uploads/2016/01/5.jpg)

如果想在iOS上测试Showtime，则可以打开Native/Showtime中的工程。编译并运行App来看看效果：

![image](https://cdn2.raywenderlich.com/wp-content/uploads/2016/02/Simulator-Screen-Shot-20-Feb-2016-21.25.58-1.png)

正如你所看到的，手机中的App还未准备就绪，不过我们慢慢来补充它。工程已经包含了一些代码；我们会一步一步来完善。这个App的目的是提供一个类似web页面的体验：它将把搜索结果显示在一个Collection View中。

## JavaScriptCore是什么？

JavaScriptCore框架提供了访问WebKit的Javascript引擎的机制。最初这个框架只有一些支持Mac系统的C API，但到了iOS 7和OS X 10.9后，它提供了一个更加友好的Objective-C封装。这个框架为Swift/Objective-C和Javascript代码提供了更强大的互通性。

> 注：React Native演示了JavaScriptCore强大功能。如果你想了解如何使用Javascript构建本地应用，你可以看看本站的[Introducing React Native tutorial](http://www.raywenderlich.com/99473/introducing-react-native-building-apps-javascript)一文。

在这一节中，你将近距离于窥探一下JavaScriptCore的API。JavaScriptCore包含几个主要的组件：JSVirtualMachine、JSContext和JSValue。下面描述它们是如何整合在一起的。

### JSVirtualMachine

JavaScript代码是在由JSVirtualMachine类表示的一个虚拟机上执行的。通常情况下你不需要直接与这个类交互，但有一种情况例外：并发执行JavaScript代码。在一个独立的JSVirtualMachine中，是不可能同一时间执行多个线程的。为了支持并行，你必须使用多个虚拟机。

每一个JSVirtualMachine实例都有自己的堆和自己的垃圾回收器，这意味着你不能在虚拟机之间传递对象。一个虚拟机的垃圾收集器不知道如何去处理另一个堆上的值。

### JSContext

一个JSContext对象表示JavaScript代码的执行环境。它对应于一个单一的全局对象；它的web开发环境等同于一个窗口对象。不同于一个虚拟机，你可以在多个上下文之间传递对象(因为它们位于同一虚拟机)。

### JSValue

JSValue是我们需要处理的主要数据类型：它可以表示任何可能的Javascript值。一个JSValue被绑定到其存活的JSContext对象中。任何来源于上下文对象的值都是JSValue类型。

下图显示了这几个对象是如何一起工作的：

![image](https://cdn5.raywenderlich.com/wp-content/uploads/2016/02/javascriptcore.png)

现在你对JavaScriptCore框架有了一个更好的了解了，就让我们来写一些代码吧。

## 调用Javascript方法

回到Xcode，在project navigator中展开Data group，并打开MovieService.swift。这个类将获取并处理来源于iTunes的电影结果。不过现在它几乎是空的；接下来就由你来提供这些方法的具体实现。

MovieService的工作流程如下：

- `loadMoviesWithLimit(_:onComplete:)`将获取电影数据。
- `parseResponse(_:withLimit:)`将使用共享的JavaScript代码来处理响应数据。

第一步是获取电影列表。如果你熟悉JavaScript开发，你会知道一般是使用XMLHttpRequest对象来访问网络。这个对象并不是语言本身的一部分，所以你不能将它用于一个iOS App的上下文中。相反，你应该使用本地网络代码。

在MovieService类中，找到`loadMoviesWithLimit(_:onComplete:)`方法并按以下代码来修改：

```swift
func loadMoviesWithLimit(limit: Double, onComplete complete: [Movie] -> ()) {
  guard let url = NSURL(string: movieUrl) else {
    print("Invalid url format: \(movieUrl)")
    return
  }

  NSURLSession.sharedSession().dataTaskWithURL(url) { data, _, _ in
    guard let data = data,
        jsonString = String(data: data, encoding: NSUTF8StringEncoding) else {
      print("Error while parsing the response data.")
      return
    }

    let movies = self.parseResponse(jsonString, withLimit:limit)
    complete(movies)

  }.resume()
}
```

上面的代码片断使用默认的NSURLSession单例来获取电影列表。在你将响应数据传递给JavaScript代码之前，你需要提供一个执行上下文给响应数据。首先，在MovieService.swift文件顶部，在`import UIKit`下方添加下面这行代码来导入JavaScriptCore：

```swift
import JavaScriptCore
```

然后在MovieService中定义如下属性：

```swift
lazy var context: JSContext? = {
  let context = JSContext()

  // 1
  guard let
      commonJSPath = NSBundle.mainBundle().pathForResource("common", ofType: "js") else {
    print("Unable to read resource files.")
    return nil
  }

  // 2
  do {
    let common = try String(contentsOfFile: commonJSPath, encoding: NSUTF8StringEncoding)
    context.evaluateScript(common)
  } catch (let error) {
    print("Error while processing script file: \(error)")
  }

  return context
}()
```

这段代码将上下文定义为一个懒加载的JSContext属性：

1. 首先，你从应用的bundle中加载common.js文件，这个文件中包含你要访问的JavaScript代码。
2. 在加载文件后，上下文对象将调用`context.evaluateScript()`，并将文件内容作为其参数，以此来执行js代码。

现在可以调用Javascript方法了。仍然是在MovieService.swift文件中，找到`parseResponse(_:withLimit:)`方法，添加以下代码：

```swift
func parseResponse(response: String, withLimit limit: Double) -> [Movie] {
  // 1
  guard let context = context else {
    print("JSContext not found.")
    return []
  }

  // 2
  let parseFunction = context.objectForKeyedSubscript("parseJson")
  let parsed = parseFunction.callWithArguments([response]).toArray()

  // 3
  let filterFunction = context.objectForKeyedSubscript("filterByLimit")
  let filtered = filterFunction.callWithArguments([parsed, limit]).toArray()

  // 4
  return []
}
```

一步一步来看看这个流程：

1. 首先，确保上下文对象被正确的初始化。如果在设置的时候有任何错误(如：common.js文件不在bundle中)，则返回空数组。
2. 在上下文对象中查询`parseJSON()`方法。正如上面所提到的，查询的结果将被封装在一个JSValue对象中。接着，使用`callWithArguments(_:)`来调用方法，并将一个数组作为参数。最后，将返回的JavaScript值转换为一个数组。
3. `filterByLimit()`返回匹配给定价格限制的电影列表。
4. 现在你已经获取到了电影列表，但仍然忘了一点：`filtered`常量持有一个JSValue数组，你需要将其映射为本地Movie类型。

> 注：你可以发现`objectForKeyedSubscript()`方法的使用有点怪怪的。不幸的是，Swift只能用这种原始的下标方法，而不能将其转换成合适的下标方法。而Objective-C可以使用方括号的下标语法。

## 暴露本地代码

在JavaScript运行时运行本地代码的一种方式是使用block；它们会被自动桥接到JavaScript方法。这里有个小问题：这个方法只适用于Objective-C的block，而不适用于Swift的闭包。为了暴露一个闭包，你必须执行两个任务：

- 使用`@convention(block)`特性来修饰一个闭包，以将它桥接到一个Objective-C block。
- 在你可以将一个block映射到JavaScript方法调用前，你需要将其转换为一个AnyObject对象。

切换到Movie.swift文件，并添加以下方法：

```swift
static let movieBuilder: @convention(block) [[String : String]] -> [Movie] = { object in
  return object.map { dict in

    guard let
        title = dict["title"],
        price = dict["price"],
        imageUrl = dict["imageUrl"] else {
      print("unable to parse Movie objects.")
      fatalError()
    }

    return Movie(title: title, price: price, imageUrl: imageUrl)
  }
}
```

这个闭包维护一个JavaScript对象数组(元素为字典类型)，然后用它们构造Movie实例。

切换回MovieService.swift文件。在`parseResponse(_:withLimit:)`方法中，使用以下代码来替换的返回语句：

```swift
// 1
let builderBlock = unsafeBitCast(Movie.movieBuilder, AnyObject.self)

// 2
context.setObject(builderBlock, forKeyedSubscript: "movieBuilder")
let builder = context.evaluateScript("movieBuilder")

// 3
guard let unwrappedFiltered = filtered,
  let movies = builder.callWithArguments([unwrappedFiltered]).toArray() as? [Movie] else {
  print("Error while processing movies.")
  return []
}

return movies
```

1. 你使用Swift的`unsafeBitCast(_:_:)`方法来将block转换成AnyObject。
2. 在上下文中调用`setObject(_:forKeyedSubscript:)`，将block加载到JavaScript运行时。然后使用`evaluateScript()`方法获取JavaScript中block的一个引用。
3. 最后一步是使用`callWithArguments(_:)`从JavaScript中调用你的block，这个方法传入一个JSValue对象的数组作为参数。返回值可以被转换成Movie对象的数组。

最后来看看效果！编译并运行。在搜索框中输入一个价格，然后你可以看到将显示一些结果：

![image](https://cdn5.raywenderlich.com/wp-content/uploads/2016/02/Simulator-Screen-Shot-19-Feb-2016-21.51.48-1-281x500.png)

仅仅几行代码，你就构建了一个本地应用，并使用JavaScript来解析和过滤结果。

## 使用JSExport协议

在JavaScript使用自定义对象的另一种方式是JSExport协议。你必须创建一个继承自JSExport的协议，并声明想要暴露给Javascript的属性和方法。

对于你暴露的每一个本地类，JavaScriptCore都会在适当的JSContext实例中创建一个原型。JavaScriptCore框架这样做是基于这样一个选择基础：默认情况下，你的类的方法或属性自己并不会暴露给JavaScript。相反，你必须选择暴露谁。JSExport的规则如下：

- 对于被暴露的实例方法，JavaScriptCore创建一个对应的JavaScript函数作为原型对象的属性。
- 类的属性将作为原型的访问器属性。
- 对于类方法，JavaScriptCore将在构造器对象中创建一个JavaScript方法。

为了看看在实践中如何处理，我们切换到Movie.swift中，并在类声明前面定义如下一个新的协议：

```swift
import JavaScriptCore

@objc protocol MovieJSExports: JSExport {
  var title: String { get set }
  var price: String { get set }
  var imageUrl: String { get set }

  static func movieWithTitle(title: String, price: String, imageUrl: String) -> Movie
}
```

在这里，你指定所有想要暴露的属性并定义一个类方法来在Javascript中构造Movie对象。后者是必须的，因为JavaScriptCore不桥接初始化方法。

现在来修改Movie以实现JSExport协议。使用以下代码来替换整个类：

```swift
class Movie: NSObject, MovieJSExports {

  dynamic var title: String
  dynamic var price: String
  dynamic var imageUrl: String

  init(title: String, price: String, imageUrl: String) {
    self.title = title
    self.price = price
    self.imageUrl = imageUrl
  }

  class func movieWithTitle(title: String, price: String, imageUrl: String) -> Movie {
    return Movie(title: title, price: price, imageUrl: imageUrl)
  }
}
```

类方法只是简单地调用适当的初始化方法。

现在你的类已准备好用于JavaScript了。为了了解你可以怎么转换当前的实现，从Resources group中打开additions.js。它已经包含了以下代码：

```swift
var mapToNative = function(movies) {
  return movies.map(function (movie) {
    return Movie.movieWithTitlePriceImageUrl(movie.title, movie.price, movie.imageUrl);
  });
};
```

上面的方法从输入数组中获取每一个元素，并使用它来构造一个Movie实例。唯一值得指出的是方法签名是如何改变的：因为JavaScript没有命名参数，所以使用驼峰命名法将额外的参数附加到方法名后面。

打开MovieService.swift，使用以下代码替换懒加载上下文属性的闭包实现。

```swift
lazy var context: JSContext? = {

  let context = JSContext()

  guard let
      commonJSPath = NSBundle.mainBundle().pathForResource("common", ofType: "js"),
      additionsJSPath = NSBundle.mainBundle().pathForResource("additions", ofType: "js") else {
    print("Unable to read resource files.")
    return nil
  }

  do {
    let common = try String(contentsOfFile: commonJSPath, encoding: NSUTF8StringEncoding)
    let additions = try String(contentsOfFile: additionsJSPath, encoding: NSUTF8StringEncoding)

    context.setObject(Movie.self, forKeyedSubscript: "Movie")
    context.evaluateScript(common)
    context.evaluateScript(additions)
  } catch (let error) {
    print("Error while processing script file: \(error)")
  }

  return context
}()
```

没有太大的改变。加载additions.js的内容到上下文。使用JSContext的`setObject(_:forKeyedSubscript:)`方法，你同样可以让Movie原型在上下文中可用。

还剩下最后一件事：在MovieService.swift中，使用以下代码来替换`parseResponse(_:withLimit:)`的实现。

```swift
func parseResponse(response: String, withLimit limit: Double) -> [Movie] {
  guard let context = context else {
    print("JSContext not found.")
    return []
  }

  let parseFunction = context.objectForKeyedSubscript("parseJson")
  let parsed = parseFunction.callWithArguments([response]).toArray()

  let filterFunction = context.objectForKeyedSubscript("filterByLimit")
  let filtered = filterFunction.callWithArguments([parsed, limit]).toArray()

  let mapFunction = context.objectForKeyedSubscript("mapToNative")
  guard let unwrappedFiltered = filtered,
    movies = mapFunction.callWithArguments([unwrappedFiltered]).toArray() as? [Movie] else {
    return []
  }

  return movies
}
```

代码现在使用Javascript运行时的`mapToNative()`来创建Movie数组。如果现在编译并运行，你可以看到app仍然按预期的来运行：

![image](https://cdn1.raywenderlich.com/wp-content/uploads/2016/01/4.jpg)

恭喜你！不仅创建了一个浏览电影的很棒的App，同时也学会了通过重用完全由不同的语言实现的代码来创建它。

## 下一步去哪里？

你可以在[这里](https://developer.apple.com/videos/play/wwdc2013-615/)下载这篇教程完整的代码。

如果你想学习更多关于JavaScriptCore知识，可以看看WWDC 2013的[Session 615](https://developer.apple.com/videos/play/wwdc2013-615/)

我希望你喜欢这篇JavaScriptCore教程。如果有任何问题或评论，可以参考到下面的讨论中来！

---

欢迎关注我的微信公众号：iOS知识小集，扫扫左边**站点概览**里的二维码就OK了。对了，还有微博：[@南峰子_老驴](http://weibo.com/touristdiary)。
