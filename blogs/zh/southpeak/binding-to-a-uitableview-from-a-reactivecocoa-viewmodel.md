---
title: Binding To A UITableView From A ReactiveCocoa ViewModel
source: 南峰子 (southpeak)
source_key: southpeak
source_url: 'https://southpeak.github.io/2014/09/21/binding-to-a-uitableview-from-a-reactivecocoa-viewmodel/'
original_language: zh
published: 2016-08-27
status: frozen
license: © 2017 南峰子（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5cb8453c0406c871'
translated: n/a
---

> 原文：[Binding To A UITableView From A ReactiveCocoa ViewModel](https://southpeak.github.io/2014/09/21/binding-to-a-uitableview-from-a-reactivecocoa-viewmodel/)　·　南峰子 (southpeak)

英文作者Colin Eberhardt，原文可查看[BINDING TO A UITABLEVIEW FROM A REACTIVECOCOA VIEWMODEL](http://www.scottlogic.com/blog/2014/05/11/reactivecocoa-tableview-binding.html)

这篇博客介绍了一个工具类，这个类将`ReactiveCocoa`中的`ViewModels`绑定到`UITableView`，而不需要通常的datasource和delegate。下面是这个辅助类的使用方法：

```objc
// 创建一个cell
UINib *nib = [UINib nibWithNibName:@"CETweetTableViewCell" bundle:nil];

// 将ViewModels的searchResults属性绑定到table view
[CETableViewBindingHelper bindingHelperForTableView:self.searchResultsTable
                        sourceSignal:RACObserve(self.viewModel, searchResults)
                        templateCell:nib];
```

## 介绍

我总是在不断的编写代码：在工作中，在家里，在火车上…如果我不写代码，我就会觉得不快乐！(注：这才是真正的程序员啊)

在过去的几个月中，我开始在我的工程中越来越多地使用ReactiveCocoa了。这个框架可以用来创建一些非常优雅的解决方案，但同时它非常具有挑战性，因为对于任何一个问题，都有许多可用的解决方案。对于像我这样的编码狂人来说，这再好不过了。

几个月之前，我在Ray Wenderlich的网站上发表了两篇关于ReactiveCocoa的文章([第一部分](http://www.raywenderlich.com/62699/reactivecocoa-tutorial-pt1)、[第二部分](http://www.raywenderlich.com/62796/reactivecocoa-tutorial-pt2))，以及一个[Tech Talk](http://www.raywenderlich.com/70598/reactivecocoa-tech-talk-video)视频。这些覆盖了ReactiveCocoa的基本用法，希望能让广大读者熟悉ReactiveCocoa。不过，我收到不少请求，希望能讨论一些使用ReactiveCocoa实现MVVM模式的高级话题。

正因此，我开始写这篇文章。不过，在我发布之前，我想先分享一个已纠缠我很久的问题…

如果将一个`UITableView`绑定到一个`ReactiveCocoa`的`ViewModel`中？

## 视图模式

我以一个简单的例子开头–一个允许我们搜索Twitter的`ViewModel`：

```objc
/// A view model which provides a mechanism for searching twitter
@interface CETwitterSearchViewModel : NSObject

/// The current search text
@property NSString *searchText;

/// An array of CETweetViewModel instances which indicate
/// the current search results
@property NSArray *searchResults;

/// A command which when executed searches twitter using the current searchText
@property RACCommand *searchCommand;

@end
```

这个`ViewModel`的实现重用了我在`ReactiveCocoa`指南第二部分所创建的信号，所以我不在此重复。如果想要看详细的代码，可以在github上查找。

将`ViewModel`绑定到一个带有`UITextField`和`UIButton`的UI是使用`ReactiveCocoa`最普通不过工作了

```objc
// bind the UITextField text updates to the view model
RAC(self.viewModel, searchText) = self.searchTextField.rac_textSignal;

// bind a button to the search command
self.searchButton.rac_command = self.viewModel.searchCommand;

// when the search executes hide the keyboard
[self.viewModel.searchCommand.executing subscribeNext:^(id x) {
  [self.searchTextField resignFirstResponder];
}];

// show a network activity indicator when the search is being executed
RAC([UIApplication sharedApplication], networkActivityIndicatorVisible) =
  self.viewModel.searchCommand.executing;
```

在上面的代码中，当点击go按钮时，我们处理了诸如隐藏键盘这样的操作，并将网络连接的`activity indicator`绑定到了`searchCommand.executing`信号。

![image](http://www.scottlogic.com/blog/ceberhardt/assets/mvvm/UIBinding.png)

这样就将`ViewModel`三个属性中的两个绑定到了UI，到目前为止，一切都还不错！

最后一个属性是`searchResults`；这个属性是一个数组，包含了搜索结果。我们可以通过`RACObserve`来观察这个属性的修改，`RACObserve`创建了一个信号，该信号会在每次更新时发出一个next事件。但不幸的是，我们不能只给`UITableView`一个对象的数组，并告诉它去渲染自己。

如果我们在StackOverflow上搜索相关帖子，或者查看别人的`ReactiveCocoa`实例，可以看到传统的方式似乎是我们需要自己去实现`table view`的代理和数据源。换句话说，我们之前优雅的只需要几行绑定代码的视图类代码会由于需要实现`table view`的各种逻辑而显示异常丑陋。

不过，我们有更好的方法。

## 一个Table View绑定辅助类

在MVVM模式中，每一个View都由一个`ViewModel`支撑着。一个视图可能占据整个屏幕(此时我们将一个视图控制器绑定到一个`ViewModel`)，或者只占据屏幕的一部分。

我们的顶层`ViewModel`的`searchResults`属性包含了一个对象数组，其中每一个元素都是一个`ViewModel`。为了解决这个问题，我们需要的是一个通用的机制来为每个视图创建一个`ViewModel`，并将这两者绑定在一起。

Nib提供了一种便捷的机制来定义可重用的视图。可以方便地使用nib来定义一个table view的单元格。

一个合理的table view绑定辅助类的接口如下：

```objc
/// A helper class for binding view models with NSArray properties
/// to a UITableView.
@interface CETableViewBindingHelper : NSObject

- (instancetype) initWithTableView:(UITableView *)tableView
                      sourceSignal:(RACSignal *)source
                      templateCell:(UINib *)templateCellNib;

@end
```

这个绑定类使用提供的table view来渲染由源信号所提供的view model，另外templeteCell定义了视图。让我们来看看这个辅助类的实现：

```objc
＠interface CETableViewBindingHelper () <UITableViewDataSource>

＠end

＠implementation CETableViewBindingHelper {
  UITableView *_tableView;
  NSArray *_data;
  UITableViewCell *_templateCell;
}

- (instancetype)initWithTableView:(UITableView *)tableView
                     sourceSignal:(RACSignal *)source
                     templateCell:(UINib *)templateCellNib {

  if (self = [super init]) {
    _tableView = tableView;
    _data = [NSArray array];

    // each time the view model updates the array property, store the latest
    // value and reload the table view
    [source subscribeNext:^(id x) {
      _data = x;
      [_tableView reloadData];
    }];

    // create an instance of the template cell and register
    // with the table view
    _templateCell = [[templateCellNib instantiateWithOwner:nil
                                          options:nil] firstObject];
    [_tableView registerNib:templateCellNib
              forCellReuseIdentifier:_templateCell.reuseIdentifier];

    // use the template cell to set the row height
    _tableView.rowHeight = _templateCell.bounds.size.height;

    _tableView.dataSource = self;
  }
  return self;
}

#pragma mark - UITableViewDataSource implementation

- (NSInteger)tableView:(UITableView *)tableView
                       numberOfRowsInSection:(NSInteger)section {
  return _data.count;
}

- (UITableViewCell *)tableView:(UITableView *)tableView
                        cellForRowAtIndexPath:(NSIndexPath *)indexPath {
  id<CEReactiveView> cell = [tableView
      dequeueReusableCellWithIdentifier:_templateCell.reuseIdentifier];
  [cell bindViewModel:_data[indexPath.row]];
  return (UITableViewCell *)cell;
}

＠end
```

注意，初始化方法是内在逻辑所在。在这里，`sourceSignal`添加了一个`subscriber`，这样每次`ViewModel`的数组属性变化时，当前属性值的引用都会被保存，而table view也会重新加载。同样，也会创建`templeteCell`实例，来确定单元格的高度。

最后，这个类实现了table view的数据源方法，并通过信号来获取数据。

其中，单元格Cell必须实现以下协议，该协议提供了一个信号方法来将Cell绑定到相应的`ViewModel`上。

```objc
/// A protocol which is adopted by views which are backed by view models.
@protocol CEReactiveView <NSObject>

/// Binds the given view model to the view
- (void)bindViewModel:(id)viewModel;

@end
```

将这个用于实际当中，现在只需要几行代码就可以将一个数组属性绑定到一个table view上了。

```objc
// create a cell template
UINib *nib = [UINib nibWithNibName:@"CETweetTableViewCell" bundle:nil];

// bind the view models 'searchResults' property to a table view
[[CETableViewBindingHelper alloc]
      initWithTableView:self.searchResultsTable
           sourceSignal:RACObserve(self.viewModel, searchResults)
           templateCell:nib];
```

注意，源信号是通过`RACObserver`宏来创建的。这个信号在每次属性通过setter来改变都会发出一个next事件。

cell的实现类似于视图控制器；它们的UI控件定义在一个nib文件中并连接到相应的outlet属性。下图是该示例程序中定义cell的nib：

![image](http://www.scottlogic.com/blog/ceberhardt/assets/mvvm/CellNib.png)

定义在`CEReactiveView`协议中的`ViewModel`绑定方法实现如下：

```objc
- (void)bindViewModel:(id)viewModel {

  CETweetViewModel *tweet = (CETweetViewModel *)viewModel;

  // set the tweet 'status' label, sizing it to fit the text
  self.titleTextField.frame =
                 CGRectInset(self.titleBackgroundView.frame, 5.0f, 5.0f) ;
  self.titleTextField.text = tweet.status;
  [self.titleTextField sizeToFit];

  // set the username
  self.usernameTextField.text = tweet.username;

  // use signals to fetch the images for each image view
  self.profileImage.image = nil;
  [[self signalForImage:[NSURL URLWithString:tweet.profileBannerUrl]]
    subscribeNext:^(id x) {
      self.ghostImageView.image = x;
    }];

  self.ghostImageView.image = nil;
  [[self signalForImage:[NSURL URLWithString:tweet.profileImageUrl]]
    subscribeNext:^(id x) {
      self.profileImage.image = x;
    }];
}
```

注意，由于`CETweetViewModel`的属性不会发生变化，因此它们的值直接被拷贝到相应的UI控件上。当然，如果它们的值会改变，我们也可以使用`ReactiveCocoa`来将两者绑定到一起。

cell的实现同样使用了`ReactiveCocoa`在后台加载图片：

```objc
// creates a signal that fetches an image in the background, delivering
// it on the UI thread. This signal 'cancels' itself if the cell is re-used before the
// image is downloaded.
-(RACSignal *)signalForImage:(NSURL *)imageUrl {

  RACScheduler *scheduler = [RACScheduler
                 schedulerWithPriority:RACSchedulerPriorityBackground];

  RACSignal *imageDownloadSignal = [[RACSignal
    createSignal:^RACDisposable *(id<RACSubscriber> subscriber) {
      NSData *data = [NSData dataWithContentsOfURL:imageUrl];
      UIImage *image = [UIImage imageWithData:data];
      [subscriber sendNext:image];
      [subscriber sendCompleted];
      return nil;
    }] subscribeOn:scheduler];

  return [[imageDownloadSignal
          takeUntil:self.rac_prepareForReuseSignal]
          deliverOn:[RACScheduler mainThreadScheduler]];
}
```

通过这种方式，我们就可以让我们的视图控制器保持少量的代码。看，是不是很整洁。

下面是完整的程序的实现效果：

![image](http://www.scottlogic.com/blog/ceberhardt/assets/mvvm/CellBinding.png)

## 处理选中事件

当前的绑定辅助类允许我们在一个table view中渲染`ViewModel`的数组，但如果我们需要处理选中事件呢？传统的方法是在视图控制器的手动处理，实现table view的代理方法，并执行相关的`ViewModel`的命令。

不过，这部分逻辑代码也可以放入到绑定辅助类中。

首先，我们在初始化方法中添加一个选择命令：

```objc
- (instancetype) initWithTableView:(UITableView *)tableView
                      sourceSignal:(RACSignal *)source
                  selectionCommand:(RACCommand *)selection
                      templateCell:(UINib *)templateCellNib;
```

这个初始化方法的实现现在存储了这个命令的引用。辅助类同样也实现了table view的代理，即`tableView:didSelectRowAtIndexPath:`方法的实现如下：

```objc
- (void)tableView:(UITableView *)tableView
               didSelectRowAtIndexPath:(NSIndexPath *)indexPath {
  [_selection execute:_data[indexPath.row]];
}
```

即当命令被调用时，会将选择的`ViewModel`作为执行参数传入。

在顶层`ViewModel`中，我已经添加了一个命令，这个操作只是简单地记录一下日志：

```objc
// create the tweet selected command, that simply logs
self.tweetSelectedCommand = [[RACCommand alloc]
        initWithSignalBlock:^RACSignal *(CETweetViewModel *selected) {
	 NSLog(selected.status);
	 return [RACSignal empty];
}];
```

## 结论

希望这个table view绑定辅助类能够帮助那些使用`MVVM`和`ReactiveCocoa`来开发iOS应用的开发者们。所有的代码都在github上。如果您有任何意见、想法或建议，请让我知道。
