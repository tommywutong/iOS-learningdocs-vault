---
title: 使用目标-动作模式响应基于控制的事件
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/responding-to-control-based-events-using-target-action
source_url: 'https://developer.apple.com/documentation/uikit/responding-to-control-based-events-using-target-action'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/responding-to-control-based-events-using-target-action.json'
content_hash: 'sha256:a035f6714eaea849'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [视图与控制](views-and-controls.md)

# 使用目标-动作模式响应基于控制的事件

<sub>文章</sub>

通过按钮、滑块和其他控制，使用目标-动作（target-action）设计模式将用户输入连接到你的 App 代码。

## 概述

用户交互为你的 App 生成成千上万的事件。例如，每一次手指的滑动或按钮的点击都会产生大量你的 App 需要处理的事件。

`Target-action` 是一种设计模式，帮助你高效地处理这些用户交互。仅针对控制上的特定事件注册动作，就能简化事件处理，同时让代码更易于维护和阅读。

使用 `target-action` 直接将 UI 中控制的事件连接到代码中的方法。

### 指定一个对象来处理与控制相关的事件

当用户与控制交互时，控制需要知道将事件发送到哪里。事件的发送目的地就是*目标*。视图控制器（View Controller）是很好的目标，因为它们擅长处理用户交互，同时也托管着 UI 控制。

![](../../../attachments/e4d1af298b6b4942ba4ae92e7b9142e1/media-4142878@2x.png)

<sub>一个示意图，描述控制与其相应目标和动作之间的关系。左侧的控制有一个箭头指向右侧的目标，即一个视图控制器。下方有一条平行的箭头，从左侧的控制指向右侧的动作方法，即名为 buttonTapped 的函数。</sub>

### 定义用于响应事件的动作方法

将控制分配给目标后，提供一个在事件发生时于该目标上调用的函数。这就是*动作*方法。

动作方法具有独特的方法签名：

**Swift**

```swift
// UIKit.
@IBAction func doSomething()
@IBAction func doSomething(sender: Any)
@IBAction func doSomething(sender: Any, forEvent event: UIEvent)
 
// AppKit.
@IBAction func doSomething()
@IBAction func doSomething(sender: Any)
```

**Objective-C**

```objc
    // UIKit.
    - (IBAction)doSomething;
    - (IBAction)doSomething:(id)sender;
    - (IBAction)doSomething:(id)sender forControlEvents:(UIControlEvents)controlEvents;

    // AppKit.
    - (IBAction)doSomething;
    - (IBAction)doSomething:(id)sender;
```

Xcode 使用 `@IBAction` 关键字将 Interface Builder 中的控制连接到代码中的函数。该关键字还桥接了 Swift 和 Objective-C 运行时，使 Swift 代码能够调用 Objective-C，而目标-动作（target-action）功能就位于其中。

`sender` 参数定义事件的来源；例如，一个按钮。使用通用类型 `Any` 允许任何控制调用该动作方法，或者当你需要更多关于控制的信息以进行事件处理时，指定 `sender` 的类型。例如，将 `sender` 类型设为 [UISlider](uislider.md) 以在有人向左或右移动滑块时读取滑块的值。

**Swift**

```swift
// UIKit.
@IBAction func adjustVolume(sender: UISlider) {
    print(sender.value)
}

// AppKit.
@IBAction func adjustVolume(sender: NSSlider) {
    NSLog("%@", sender.stringValue)
}
```

**Objective-C**

```objc
// UIKit.
- (IBAction)adjustVolume:(UISlider *)sender {
    NSLog(@"%f", sender.value);
}

// AppKit.
- (IBAction)adjustVolume:(NSSlider *)sender {
    NSLog(@"%@", [sender stringValue]);
}
```

UIKit 还支持将动作方法耦合到特定的事件类型（参见 [Event](uicontrol/event.md)）。例如，要为手指在控制边界内拖动的情况设置目标-动作，为事件类型 [UIControlEventTouchDragInside](uicontrol/event/touchdraginside.md) 注册。

### 在 Interface Builder 中将控制连接到动作方法

定义了 `target`（目标）和 `action`（动作）方法后，你就可以在 Interface Builder 中将它们可视化地连接到控制了。

1. 选择你想要连接到代码（`action`）的控制（`target`）。
2. 按住 Control 键并将控制拖拽至文稿大纲（document outline）中的视图控制器。
3. 选择控制所连接的动作方法。

![](../../../attachments/771651336f82f9f737bee724d8aacc30/responding-to-control-based-events-using-target-action-1@2x.png)

<sub>一张截图，展示如何在 Xcode 中使用 Interface Builder 将控制连接到动作。截图左侧是 Xcode 的文稿大纲视图，显示了一个连接到视图控制器的连线；右侧是 Interface Builder 画布，包含一个按钮。一个 Control-拖拽箭头将画布上的按钮连接到文稿大纲中的视图控制器。另一个箭头将画布上的按钮连接到 Interface Builder 画布中的视图控制器图标。</sub>

![](../../../attachments/f32f36a7eb6de15e414524562636015e/responding-to-control-based-events-using-target-action-2@2x.png)

<sub>一张 Xcode 截图，展示完成 Control-拖拽操作后显示连接选项的模态弹窗。该模态弹窗列出了几个动作 Segue 选项，包括 Show、Show Detail 和 Present Modally。一个箭头指向 signInButtonTapped 选项。</sub>

你可以通过将指针移动到动作方法左侧的圆形点上来验证控制与动作是否已连接。当你这样做时，Xcode 会高亮该控制。

![](../../../attachments/6d6f7bfd097d78c41bbcf1c506353ff2/responding-to-control-based-events-using-target-action-3@2x.png)

<sub>一张 Xcode 截图，展示将指针移动到代码编辑器中的动作方法上时，如何高亮它在 Interface Builder 中连接的控制。Interface Builder 在左侧，一个按钮处于高亮状态。右侧是助理代码编辑器（Assistant editor），鼠标指针悬停在函数定义左侧的灰色圆圈上。</sub>

另一种连接方式是将控制从 Interface Builder 按住 Control 键拖拽到视图控制器中。

![](../../../attachments/98bc3e6ad55e539a62a42c9aa23f1585/responding-to-control-based-events-using-target-action-4@2x.png)

<sub>一张 Xcode 截图，展示如何通过将控制从 Interface Builder 按住 Control 键拖拽到助理编辑器中来生成 target-action 方法。Interface Builder 在左侧。助理编辑器在其右侧打开。一个箭头从按钮指向代码编辑器，上方显示文字 Control-拖拽。</sub>

输入你希望控制调用的 `action` 方法名称，然后点按“连接（Connect）”。

![](../../../attachments/27137e08683ee7ab0d05fcb278d3c701/responding-to-control-based-events-using-target-action-5@2x.png)

<sub>一张 Xcode 截图，展示从 Interface Builder 与助理编辑器之间的 Control-拖拽操作所产生的模态弹窗。该模态弹窗显示以下字段：Connection、Object、Name、Type、Event 和 Arguments。底部有两个按钮：左侧的 Cancel（取消）按钮和右侧的 Connect（连接）按钮。</sub>

下表列出了可供配置的参数。

| 参数 | 描述 |
|---|---|
| Connection | 要建立的连接类型。选择 Action 以在控制与目标之间建立目标-动作（target-action）关系。 |
| Object | 你的控制所连接到的 `target` 或对象。 |
| Name | 事件发生时，你的控制所调用的函数或 `action` 的名称。 |
| Type | 发送事件的控制的类型。如果你不需要任何关于控制状态的进一步信息，选择 `Any`。如果你需要从控制获取更多信息以进行事件处理，指定控制类型。 |
| Event | 与该动作关联的 [UIEvent](uievent.md)。此功能仅在 UIKit 中可用。 |
| Arguments | 要包含在你的目标-动作方法签名中的参数。选择 None 则不包含任何参数。选择 Sender 则传入控制类型作为发送者。选择 Sender and Event 则同时传入控制类型和导致该动作的事件。此功能仅在 UIKit 中可用。 |

以这种方式连接目标-动作可确保方法签名和参数正确，因为 Xcode 会为你生成动作方法。

![](../../../attachments/8972599c7c584b335c8d4f9209cd742c/responding-to-control-based-events-using-target-action-6@2x.png)

<sub>一张 Xcode 截图，展示从 Interface Builder 到助理代码编辑器进行 Control-拖拽操作后生成的代码。Interface Builder 在左侧。助理编辑器在其右侧打开，编辑器内是生成的代码。一个带有 Generated 文字的箭头指向新生成的代码。</sub>

### 以编程方式将控制连接到代码

在 UIKit 中，使用 [- addTarget:action:forControlEvents:](<uicontrol/addtarget(__action_for_).md>) 方法在控制上以编程方式设置目标-动作（target-action）：

**Swift**

```swift
import UIKit

class ViewController: UIViewController {
    let signInButton = UIButton(type: .system)
    
    override func viewDidLoad() {
        super.viewDidLoad()

        signInButton.translatesAutoresizingMaskIntoConstraints = false
        signInButton.setTitle("Sign in", for: .normal)
        
        // Target-action.
        signInButton.addTarget(self, action: #selector(buttonTapped), for: .touchUpInside)
        
        view.addSubview(signInButton)
        signInButton.centerXAnchor.constraint(equalTo: view.centerXAnchor).isActive = true
        signInButton.centerYAnchor.constraint(equalTo: view.centerYAnchor).isActive = true
    }
    
    @IBAction func buttonTapped(sender: UIButton) {
        print("Sign in successful 🎉")
    }
}
```

**Objective-C**

```objc
#import "ViewController.h"

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    UIButton *signInButton = [UIButton buttonWithType:UIButtonTypeSystem];
    [signInButton setTitle:@"Sign in" forState:UIControlStateNormal];

    signInButton.translatesAutoresizingMaskIntoConstraints = false;

    // Target-action.
    [signInButton addTarget:self action:@selector(buttonTapped:) forControlEvents:UIControlEventTouchUpInside];
    
    [self.view addSubview:signInButton];
    [signInButton.centerXAnchor constraintEqualToAnchor:self.view.centerXAnchor].active = true;
    [signInButton.centerYAnchor constraintEqualToAnchor:self.view.centerYAnchor].active = true;
}

- (void)buttonTapped:(UIButton *)sender {
    NSLog(@"Sign in successful 🎉");
}
@end
```

在 AppKit 中，使用控制的 `target` 和 `action` 属性以编程方式设置目标-动作（target-action）：

**Swift**

```swift
import Cocoa

class ViewController: NSViewController {
    let signInButton = NSButton()
    
    override func viewDidLoad() {
        super.viewDidLoad()

        signInButton.translatesAutoresizingMaskIntoConstraints = false
        signInButton.title = "Sign in"
        
        // Target-action.
        signInButton.target = self
        signInButton.action = #selector(buttonTapped(sender:))
        
        view.addSubview(signInButton)
        signInButton.centerXAnchor.constraint(equalTo: view.centerXAnchor).isActive = true
        signInButton.centerYAnchor.constraint(equalTo: view.centerYAnchor).isActive = true
    }
    
    @IBAction func buttonTapped(sender: NSButton) {
        print("Sign in successful 🎉")
    }
}
```

**Objective-C**

```objc
#import "ViewController.h"

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    NSButton *signInButton = [[NSButton alloc] initWithFrame: NSMakeRect(20, 20, 100, 80)];
    signInButton.translatesAutoresizingMaskIntoConstraints = NO;
    signInButton.title = @"Sign in";
    signInButton.bezelStyle = NSBezelStyleRounded;
    
    // Target-action.
    signInButton.target = self;
    signInButton.action = @selector(buttonTapped:);
    
    [self.view addSubview:signInButton];
    [signInButton.centerXAnchor constraintEqualToAnchor:self.view.centerXAnchor].active = YES;
    [signInButton.centerYAnchor constraintEqualToAnchor:self.view.centerYAnchor].active = YES;
}

- (void)buttonTapped:(NSButton *)sender {
    NSLog(@"Sign in successful 🎉");
}

@end
```

### 让其他对象也能响应与控制相关的事件

当托管控制的对象不是你想要处理事件的对象时，通过传入 `nil` 作为目标来调用响应者链（responder chain）。这会让控制在响应者链中搜索指定的动作方法，并在找到时调用它。更多信息，请参见[使用响应者和响应者链处理事件](using-responders-and-the-responder-chain-to-handle-events.md)。

## 另请参阅

### 控制

- [UIControl](uicontrol.md) — 控制（control）的基类，控制是一种视觉元素，用于响应用户交互传达特定动作或意图。
- [UIButton](uibutton.md) — 一种控制，执行你的自定义代码以响应用户交互。
- [UIColorWell](uicolorwell.md) — 一种显示颜色选择器（color picker）的控制。
- [UIDatePicker](uidatepicker.md) — 用于输入日期和时间值的控制。
- [UIPageControl](uipagecontrol.md) — 一种显示水平圆点序列的控制，每个圆点对应 App 文稿或其他数据模型实体中的一页。
- [UISegmentedControl](uisegmentedcontrol.md) — 一种包含多个分段（segment）的水平控制，每个分段作为一个独立的按钮。
- [UISlider](uislider.md) — 用于从连续范围中选择单个值的控制。
- [UIStepper](uistepper.md) — 用于递增或递减值的控制。
- [UISwitch](uiswitch.md) — 提供二选一（如开/关）选择的控制。
