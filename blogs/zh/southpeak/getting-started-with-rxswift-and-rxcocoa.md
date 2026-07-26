---
title: Getting Started With RxSwift and RxCocoa
source: 南峰子 (southpeak)
source_key: southpeak
source_url: 'https://southpeak.github.io/2017/01/16/Getting-Started-With-RxSwift-and-RxCocoa/'
original_language: zh
published: 2017-01-16
status: frozen
license: © 2017 南峰子（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:eed96fb09f7d8bd4'
translated: n/a
---

> 原文：[Getting Started With RxSwift and RxCocoa](https://southpeak.github.io/2017/01/16/Getting-Started-With-RxSwift-and-RxCocoa/)　·　南峰子 (southpeak)

> 本文由Ellen Shapiro发表于raywenderlich，原文地址是[https://www.raywenderlich.com/138547/getting-started-with-rxswift-and-rxcocoa](https://www.raywenderlich.com/138547/getting-started-with-rxswift-and-rxcocoa)

---

代码能按你的意愿执行总是件很棒的事。在程序中改变一些东西，告诉代码，然后它就照做了。嗯，这是坨好代码！

在面向对象时代，大多数程序都像这样运行：你的代码告诉你的程序需要做什么，并且有很多方法来监听变化–但同时你又必须主动告诉系统什么时候发生的变化。

目前为止还是很不错，不过如果变化发生时，代码能自动响应更新，生活是不是会更美好呢？这就是响应式编程的基本思想：你的程序可以对底层数据的变化做出响应，而不需要你直接告诉它。这样，你可以更专注于所需要处理的业务逻辑，而不需要去维护特定的状态。

在Objective-C和Swift都可以实现这种操作，主要是通过`Key-value Observation`，在Swift中还可以使用`setter`或`didSet`方法。不过，有时这些方法并不那么好使。为了避免这些问题，现在市面上已经有一些Objective-C和Swift的框架，来实现响应式编程。

> 如果你想了解更多的信息，可以看看 ‘[ReactiveCocoa vs RxSwift](https://www.raywenderlich.com/126522/reactivecocoa-vs-rxswift)‘ 这篇文章。

今天我们将使用一个很棒的框架，RxSwift和它的小伙伴RxCocoa，来实现一个购买巧克力的App，并从那令人恼火的命令式编程过渡到相当awesome的响应式编程。

## RxSwift和RxCocoa是什么？

RxSwift和RxCocoa是ReactiveX工具套件的一部分，这个套件包含了多种编程语言和平台。ReactiveX起源于.Net/C#生态体系，不过现在已经非常受Rubyists、JavaScripers、尤其是Java和Android开发人员的欢迎了。

RxSwift是一个用于与Swift语言交互的框架，而RxCocoa是在响应式编程中让Cocoa APIs更容易使用的一个框架。

ReactiveX框架相当于提供了一个词汇表，以方便在不同的语言中描述相同的任务。这让你可以在多语言切换中，专注于语言本身的语法，而不是把时间浪费在将一个普通任务从一种语言转换为另一种新语言。

### Observables和Observers

这里有两个基本的概念：`Observable`和`Observer`。

- `Observable`是发出变化通知的对象；
- `Observer`是订阅`Observable`的对象，以便在`Observable`变化时接收通知

可以有多个`Observer`监听同一个`Observable`。这意味着当`Observable`发生变化时，会通知所有相关的`Observer`。

### DisposeBag

RxSwift和RxCocoa还有一个额外的工具来辅助处理ARC和内存管理：即`DisposeBag`。这是`Observer`对象的一个虚拟”包”，当它们的父对象被释放时，这个虚拟包会被丢弃。

当带有`DisposeBag`属性的对象调用`deinit()`时，虚拟包将被清空，且每一个一次性(disposable)`Observer`会自动取消订阅它所观察的内容。这允许ARC像通常一样回收内存。

如果没有`DisposeBag`，会有两种结果：或者`Observer`会产生一个`retain cycle`，被无限期的绑定到被观察对象上；或者意外地被释放，导致程序崩溃。

所以要成为一个ARC的良民，记得设置`Observable`对象时，将它们添加到`DisposeBag`中。这样，它们才能被很好地清理掉。

## 开始

让我们去买巧克力吧！本教程的初始工程**Chocotastic**可以在[这里](https://koenig-media.raywenderlich.com/uploads/2016/10/Chocotastic-starter-s3-rxs-3b1.zip)获取。下载zip文件并在Xcode中打开工程。

> 该项目使用CocoaPods，因此需要打开Chocotastic.xcworkspace文件。

构建并运行程序。你会看到以下效果，其中列出了你可以从欧洲购买的几种巧克力，以及各自的价格：

![](https://koenig-media.raywenderlich.com/uploads/2016/07/initial_landing.png)

点击单元格，可以将对应的巧克力添加到你的购物车中：

![](https://koenig-media.raywenderlich.com/uploads/2016/07/added_chocolate.png)

点击右上角的购物车就可以进入付款或重置购物车的界面：

![](https://koenig-media.raywenderlich.com/uploads/2016/07/checkout.png)

如果点击`Checkout`，将显示一个信用卡输入页面：

![](https://koenig-media.raywenderlich.com/uploads/2016/07/cc_form.png)

在本教程的后面，你将使用纯响应式来解决问题。点击`Cart`按钮将返回购物车清单，点击`Reset`按钮将返回主界面，并显示空购物车。

### 起点：非响应式

你现在已经知道了程序将做什么，现在该来看看是怎么做的了。打开`ChocolatesOfTheWorldViewController.swift`文件，在这里你可以看到一些标准的`UITableViewDelegate`和`UITableViewDataSource`方法。

还有一个`updateCartButton()`方法，它用购物车中现有的巧克力数量来更新购物车按钮。这个方法在两个地方被调用：

- 在`viewWillAppear(_:)`中，即视图控制器即将被显示时；
- 在`tableView(_:didSelectRowAt:)`中，即新添加一个巧克力到购物车后。

这些都是以命令式方法来修改计数：你必须显示调用方法来更新计数。

目前为止，你必须跟踪你要改变值的位置，不过我们要使用响应式技术来重写这些代码。这样，购物车按钮将自已更新，而不关心计数器在哪和怎样被更新。

## RxSwift：让购物车按钮响应

所有引用购物车中的项目的方法都使用`ShoppingCart.sharedCart`单例。打开`ShoppingCart.swift`文件，你将看到单例实例上一个变量的标准设置方式：

```swift
var chocolates = [Chocolate]()
```

现在，巧克力内容的变更不会被观察到。你可以在它的定义中添加一个`didSet`闭包，但它只有在整个数组被更新才会被调用，而不是它的元素被更新时。

幸运的是，RxSwift有一个解决方案。使用下面这行代码来替代变量的创建：

```swift
let chocolates: Variable<[Chocolate]> = Variable([])
```

> 这个更改暂时会导致一系列编译错误，不过很快会在下面解决这些问题。

这种语法可能稍微有点难理解，所以下面我们来慢慢了解到底发生了什么。

在这里我们不是将`chocolates`设置为`Chocolate`对象的数组，而将其定义为一个RxSwift的`Variable`对象，其中泛型类型指定为`Chocolate`数组。

`Variable`是一个类，所以它使用引用语义–即`chocolates`引用了一个`Variable`实例。

`Variable`对象有一个`value`属性。这是你的`Chocolate`对象数组的存储位置。

`Variable`的魔力来自于它的`asObservable()`方法。你可以添加一个`Observer`来观察这个值，而不是每次手动去确认这个值。当值发生变化时，`Observer`会通知你，以便你对任何更新做出响应。

这个设置有一个缺点，即当你需要访问或更新`Chocolates`数组中的元素时，你必须使用`value`属性，而不能直接使用它；这就是编译器提示错误的原因。是时候来解决它们了。

在`ShoppingCart.swift`中，找到`totalCost()`并修改下面这行：

```swift
return chocolates.reduce(0) {
```

为：

```swift
return chocolates.value.reduce(0) {
```

在`itemCountString()`，修改：

```swift
guard chocolates.count > 0 else {
```

为：

```swift
guard chocolates.value.count > 0 else {
```

并修改：

```swift
let setOfChocolates = Set<Chocolate>(chocolates)
```

为：

```swift
let setOfChocolates = Set<Chocolate>(chocolates.value)
```

最后，修改：

```swift
let count: Int = chocolates.reduce(0) {
```

为：

```swift
let count: Int = chocolates.value.reduce(0) {
```

在`CartViewController.swift`中，找到`reset()`并修改：

```swift
ShoppingCart.sharedCart.chocolates = []
```

为：

```swift
ShoppingCart.sharedCart.chocolates.value = []
```

回到`ChocolatesOfTheWorldViewController.swift`中，修改`updateCartButton()`的实现：

```swift
cartButton.title = "\(ShoppingCart.sharedCart.chocolates.value.count) \u{1f36b}"
```

及在`tableView(_:didSelectRowAt:)`中，修改下面这行：

```swift
ShoppingCart.sharedCart.chocolates.append(chocolate)
```

为：

```swift
ShoppingCart.sharedCart.chocolates.value.append(chocolate)
```

哇！这回Xcode高兴了，不再报错了。同时`chocolates`也可以被监听了。

打开`ChocolatesOfTheWorldViewController.swift`文件并添加以下属性：

```swift
let disposeBag = DisposeBag()
```

这里创建了一个`DisposeBag`对象，用于确保设置的`Observer`在`deinit()`中被清理掉。

在 **//MARK: Rx Setup** 注释下面添加以下代码：

```swift
//MARK: Rx Setup

private func setupCartObserver() {
  //1
  ShoppingCart.sharedCart.chocolates.asObservable()
    .subscribe(onNext: { //2
      chocolates in
      self.cartButton.title = "\(chocolates.count) \u{1f36b}"
    })
    .addDisposableTo(disposeBag) //3
}
```

这将设置一个响应式的`Observer`来自动更新购物车。如你所见，RxSwift大量使用链式函数，这意味着每一个函数都接受前一个函数的结果。

来解释一下发生的事情：

1. 首先，把购物车的`chocolates`变量作为一个`Observable`；
2. 在这个`Observable`上调用`subscribe(onNext:)`方法，以了解`Observable`的值的变化。`subscribe(onNext:)`接受一个闭包作为参数，在每次值改变时，会执行这个闭包。闭包的传入参数是`Observable`的新值。你将会接受到变更通知，直到你取消订阅或者你的订阅被丢弃。从这个方法得到的是一个实现了`Disposable`的`Observer`对象；
3. 将上一步得到的`Observer`对象添加到`disposeBag`中，以确保在订阅对象被释放时你的订阅被丢弃。

最后，删除命令式的`updateCartButton()`方法。这将导致在`viewWillAppear(_:)`和`tableView(_:didSelectRowAt:)`中报错。

要修复它们，可以删除整个`viewWillAppear(_:)`方法(因为这里除了调用super外，调用`updateCartButton()`方法是它唯一做的事情)，并删除`tableView(_:didSelectRowAt:)`中`updateCartButton()`方法的调用。

构建并运行。你将看到下面的列表：

![](https://koenig-media.raywenderlich.com/uploads/2016/07/Simulator-Screen-Shot-Jul-4-2016-9.26.45-PM.png)

但是注意，购物车的按钮只显示了`'Item'`。当你开始点击列表时，什么都没有发生。这是咋回事？

你创建了一个函数来设置你的`Rx Observers`，但是现在并没有实际调用它，所以也并没有设置`Observers`。要解决这个问题，可以在`viewDidLoad()`里面添加如下代码：

```swift
setupCartObserver()
```

编译并运行程序，可以看到下面的列表：

![](https://koenig-media.raywenderlich.com/uploads/2016/07/initial_landing.png)

点击单元格，购物车中的数量现在可以自动更新了！

![](https://koenig-media.raywenderlich.com/uploads/2016/07/added_chocolate.png)

哈哈，现在所有的巧克力都可以添加到购物车了。

![](https://koenig-media.raywenderlich.com/uploads/2016/07/rage_chocolate1-1.png)

## RxCocoa: 让TableView响应

现在，你已经使用RxSwift让购物车能响应了，现在将使用RxCocoa让`UITableView`也能响应。

RxCocoa扩展了UI元素以支持响应式API。这让你可以设置`UITableView`等视图，而不需要直接重写`delegate`或`data source`的方法。

为了演示如何工作，可以删除代码中所有的`UITableViewDataSource`和`UITableViewDelegate`协议及所有它们的方法。然后，在`viewDidLoad()`中删除对`tableView.dataSource`和`tableView.delegate`的设置。

编译并运行程序，你可以看到原本让人快乐的小列表没有了，巧克力也没有了：

![](https://koenig-media.raywenderlich.com/uploads/2016/07/no_chocolate_for_you.png)

一点都不好玩。现在来把巧克力找回来吧！

首先，为了获得一个响应式的`table view`，你需要一些让`table view`响应的东西。在`ChocolatesOfTheWorldViewController.swift`文件中，更新`europeanChocolates`属性，让其作为一个`Observable`对象：

```swift
let europeanChocolates = Observable.just(Chocolate.ofEurope)
```

`just(_:)`方法表示不会对`Observable`对象的底层值做任何修改，但你仍然需要以`Observable`值的方式来访问它。

> 有时，调用`just(_:)`可能是过度地使用响应式编程了 – 毕竟，如果一个值从不改变，为什么要使用响应式技术呢？在这个例子中，你将使用它来设置将要改变的单元格的响应，不过经常思考如何使用Rx总是件好事。因为虽然你有一个锤子，但不意味着每一个问题都是一个钉子。

现在你已经让`europeanChocolates`成为一个`Observable`，然后添加以下代码：

```swift
private func setupCellConfiguration() {
  //1
  europeanChocolates
    .bindTo(tableView
      .rx //2
      .items(cellIdentifier: ChocolateCell.Identifier,
             cellType: ChocolateCell.self)) { // 3
        row, chocolate, cell in
        cell.configureWithChocolate(chocolate: chocolate) //4
      }
      .addDisposableTo(disposeBag) //5
}
```

解释一下：

1. 调用`bindTo(_:)`将`europeanChocolates``observable`关联到应该为`table view`每一行执行的代码；
2. 调用`rx`，你可以访问任何类的RxCocoa扩展 – 在这里是UITableView；
3. 调用Rx的`items(cellIdentifier:cellType:)`方法，传入单元格标识符及要使用的单元格类型。这让Rx框架可以调用出列方法(`dequeuing methods`)，如果你的`table view`仍然有原始的代理，这些方法也会被正常调用；
4. 传入一个为每个单元格执行的闭包。闭包的参数包括行信息、行对应的`chocolate`及单元格对象，这样配置单元格就非常容易了；
5. 获取到`bindTo(_:)`返回的`Disposable`，然后添加到`disposeBag`。

通常由`tableView(_:numberOfRowsInSection:)`和`numberOfSections(in:)`生成的值，现在基于被观察的数据自动计算。`tableView(_:cellForRowAt:)`方法被闭包所取代。在`viewDidLoad()`方法中添加一行来调用新设置的方法：

```swift
setupCellConfiguration()
```

编译并运行程序，瞧，巧克力又回来了。

![](https://koenig-media.raywenderlich.com/uploads/2016/07/no_chocolate_for_you.png)

但是，当点击每一个巧克力时，他们并没有被添加到购物车。又是哪不对了？

也木有，之前只是删除了`tableView(_:didSelectRowAt:)`，这样就没办法识别单元格点击操作了。

为了解决这个问题，需要使用RxCocoa提供的另一个`UITableView`的扩展方法：`modelSelected(_:)`，它返回一个`Observable`，可以观察模型对象什么时候被选中了。

添加以下代码：

```swift
private func setupCellTapHandling() {
  tableView
    .rx
    .modelSelected(Chocolate.self) //1
    .subscribe(onNext: { //2
      chocolate in
      ShoppingCart.sharedCart.chocolates.value.append(chocolate) //3

      if let selectedRowIndexPath = self.tableView.indexPathForSelectedRow {
        self.tableView.deselectRow(at: selectedRowIndexPath, animated: true)
      } //4
    })
    .addDisposableTo(disposeBag) //5
}
```

再来解释一下：

1. 调用`table view`的响应式方法`modelSelected(_:)`，传入`Chocolate`模型以获取项目的正确类型。这个方法返回一个`Observable`；
2. 获取到`Observable`后，调用`subscribe(onNext:)`方法，传入一个尾随闭包，在模型被选中时会调用这个闭包；
3. 在尾随闭包中，将选中的巧克力添加到购物车中；
4. 同样在闭包中，确保当前被点击的单元格选中状态被取消；
5. `subscribe(onNext:)`返回一个`Disposable`，添加这个`Disposable`到`disposeBag`中。

最后，在`viewDidLoad()`中添加下面这行代码：

```swift
setupCellTapHandling()
```

编译并运行，可以看到熟悉的场景：

![](https://koenig-media.raywenderlich.com/uploads/2016/07/initial_landing.png)

不过现在你可以往购物车添加巧克力了！

![](https://koenig-media.raywenderlich.com/uploads/2016/07/added_chocolate.png)

## RxSwift和Direct Text Input

RxSwift另一个功能是能够获取并响应用户的直接文本输入(`Direct Text Input`)。

为了尝试一下响应式处理文本输入，你将在信用卡输入表单中添加一些简单的验证和卡类型检测。

非响应式的信用卡处理是由一串`UITextFieldDelegate`方法来实现的，通常每个方法包含一串的`if/else`语句，用于区分哪个`text field`正在被编辑，应该执行什么操作和逻辑处理。

响应式编程将处理操作和逻辑操作直接连接到每个`text field`。

在`BillingInfoViewController.swift`，在类的顶部添加以下代码：

```swift
private let disposeBag = DisposeBag()
```

和前面一样，这里定义了一个`DisposeBag`以确保在类的实例被释放时，你的`Observables`能被正确处理。

对于信用卡号的输入，一个体验比较好的方式是给用户显示信用卡的类型。

为了实现这一操作，可以在**//MARK: - Rx Setup**下面添加以下代码：

```swift
//MARK: - Rx Setup

private func setupCardImageDisplay() {
  cardType
    .asObservable()
    .subscribe(onNext: {
      cardType in
      self.creditCardImageView.image = cardType.image
    })
    .addDisposableTo(disposeBag)
}
```

稍后，你将依此根据卡类型的更改来更新卡图片。它为变量的值添加了一个`Observer`，并附加一个闭包在值改变时执行，同时确保`Observer`添加到`disposeBag`中以被正确处理。

现在到了最有趣的部分：文本变更处理。

由于用户可能会快速键入，因此你可能不希望每次按键都去验证。这样会导致昂贵的计算和UI卡顿。

一种更好的方式是限制验证的幅度，即只有一定的时间间隔后再去验证用户的输入，而不是每次改变时都去处理。这样，再快的打字速度也不会阻塞整个程序的运行。

`Throttling`是RxSwift的一个特性。因为在一些东西改变时，通常有大量的逻辑操作。而使用`Throttling`特性，不会产生大量的逻辑操作，而是以一个小的合理的幅度去执行。

首先，在`BillingInfoViewController`中的其它属性声明下面添加以下内容：

```swift
private let throttleInterval = 0.1
```

这里以秒为单位为抖动(`throttle`)幅度定义了一个常量。

然后添加以下代码：

```swift
private func setupTextChangeHandling() {
  let creditCardValid = creditCardNumberTextField
    .rx
    .text //1
    .throttle(throttleInterval, scheduler: MainScheduler.instance) //2
    .map { self.validate(cardText: $0) } //3

  creditCardValid
    .subscribe(onNext: { self.creditCardNumberTextField.valid = $0 }) //4
    .addDisposableTo(disposeBag) //5
}
```

> 如果在设置`creditCardValid`时得到一个”`Generic parameter R could not be inferred`“编译错误，通常可以显式的声明它的类型来解决问题，如`let creditCardValid: Observable`。理论上，编译器能推导出它的类型，但有时候还是需要一些帮助。

代码的描述如下：

1. `text`是另一个RxCocoa扩展(在使用之前必须先调用`rx`)，这一次是`UITextField`的扩展。它将`text field`的内容作为`Observable`值返回；
2. 限制输入，以便设置的验证基于设置的时间间隔才运行。`scheduler`参数是一个更高级的概念，它绑定到一个线程。因为你需要在主线程上执行，所以使用`MainScheduler`；
3. 将被限制的输入应用于`validate(cardText:)`来转换它，`validate(cardText:)`由当前类提供。如果输入的卡有效，则观察到的布尔值的最终值为true；
4. 接受所创建的`Observable`值并订阅它，根据传入的值来更新`text field`的验证；
5. 将生成的`Disposable`添加到`disposeBag`。

将以下代码添加到`setupTextChangeHandling()`方法下面，以创建有效期和卡安全代码(CVV)的`Observable`变量：

```swift
let expirationValid = expirationDateTextField
  .rx
  .text
  .throttle(throttleInterval, scheduler: MainScheduler.instance)
  .map { self.validate(expirationDateText: $0) }

expirationValid
  .subscribe(onNext: { self.expirationDateTextField.valid = $0 })
  .addDisposableTo(disposeBag)

let cvvValid = cvvTextField
  .rx
  .text
  .map { self.validate(cvvText: $0) }

cvvValid
  .subscribe(onNext: { self.cvvTextField.valid = $0 })
  .addDisposableTo(disposeBag)
```

现在你已经为三个`text field`的有效性设置了`Observable`值，接下来添加以下代码：

```swift
let everythingValid = Observable
  .combineLatest(creditCardValid, expirationValid, cvvValid) {
    $0 && $1 && $2 //All must be true
  }

everythingValid
  .bindTo(purchaseButton.rx.enabled)
  .addDisposableTo(disposeBag)
```

这里使用了`Observable`的`combineLatest(_:)`方法将前面创建的三个`Observable`组合成第四个变量，即`everythingValid`，其值是否为`true`取决于前面三个输入是否有效。

然后将`everythingValid`绑定到`UIButton`的响应扩展的`enabled`属性上，这样购买按钮的状态就由`everythingValid`的值来控制了。

如果所有的输入都有效，那么`everythingValid`的基础值就为`true`。如果不是，`rx.enabled`将会导致基础值被应用于购买按钮，该功能仅在信用卡详细信息有效时启用。

现在你已经创建了`setup`方法，在`viewDidLoad()`方法中添加以下代码来调用它：

```swift
setupCardImageDisplay()
setupTextChangeHandling()
```

编译并运行程序。要进入信用卡输入页面，需要选择一个巧克力将其添加到购物车，然后点击购物车按钮以进入购物车界面。只要购物车中至少有一个巧克力，`checkout`按钮就是可用的：

![](https://koenig-media.raywenderlich.com/uploads/2016/07/checkout.png)

点击`Checkout`按钮，将进入信用卡输入页面：

![](https://koenig-media.raywenderlich.com/uploads/2016/07/cc_form.png)

在卡号`text field`中输入`4`–你将看到卡图片显示了`Visa`的图标：

![](https://koenig-media.raywenderlich.com/uploads/2016/07/Simulator-Screen-Shot-Jul-4-2016-7.47.40-PM.png)

删除`4`，卡图片将恢复未知状态。输入`55`，图片将变成`MasterCard`：

![](https://koenig-media.raywenderlich.com/uploads/2016/07/Simulator-Screen-Shot-Jul-4-2016-7.47.36-PM.png)

这个应用涵盖了美国的四种主要信用卡(Visa, MasterCard, American Express, Discover)。如果有有其中一种卡，你可以输入卡号来看看图片是否正确以及卡号是否有效。

> 如果你没有这些信用卡，你可以使用Paypal用于测试其沙盒的测试卡卡号，这些应该可以通过程序的所有本地验证，即使卡号实际上是不可用的。

一旦输入有效的信用卡卡号，同时有效期和cvv也是有效的，那么`Buy Chocolate!`按钮将被启用：

![](https://koenig-media.raywenderlich.com/uploads/2016/07/enabled_checkout.png)

点击按钮查看购买的内容及如何付款的摘要：

![](https://koenig-media.raywenderlich.com/uploads/2016/07/success.png)

恭喜你！感谢RxSwift和RxCocoa，你可以买到你的巧克力，想要多少要多少，等你的牙医让你离开为止。

## 下一步做什么

最终的代码可以在[这里](https://koenig-media.raywenderlich.com/uploads/2016/10/Chocotastic-finished-s3-rxs-3b1.zip)找到。

如果你想挑战一下，可以尝试添加一些东西，使这个程序更具响应式：

- 更改`CartViewController`，以使用响应式`table view`来显示购物车的内容；
- 允许用户直接从购物车添加或删除巧克力，并自动更新价格。

现在你已经尝试了Rx编程，以下是一些资源，以帮助你继续你的旅程：

1. [RxSwift Slack](http://slack.rxswift.org/)
2. [RxSwift’s Getting Started guide](https://github.com/ReactiveX/RxSwift/blob/master/Documentation/GettingStarted.md)
3. [Max Alexander’s talk on Rx at Realm](https://www.raywenderlich.com/138547/getting-started-with-rxswift-and-rxcocoa)

最后，我们的[Marin Todorov](https://www.raywenderlich.com/u/icanzilb)有一个不错的博客，里面有他的[rx_marin](http://rx-marin.com/)响应式编程。
