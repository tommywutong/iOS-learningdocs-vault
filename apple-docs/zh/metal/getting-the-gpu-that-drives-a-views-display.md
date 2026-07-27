---
title: 获取驱动视图显示的 GPU
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/getting-the-gpu-that-drives-a-views-display
source_url: 'https://developer.apple.com/documentation/metal/getting-the-gpu-that-drives-a-views-display'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/getting-the-gpu-that-drives-a-views-display.json'
content_hash: 'sha256:342f0a9dc9e88dd4'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md) · [GPU devices and work submission](gpu-devices-and-work-submission.md) · [Multi-GPU systems](multi-gpu-systems.md)

# 获取驱动视图显示的 GPU

<sub>文章</sub>

随时了解适合你显示器的最佳设备。

## 概述

用户可以将多台外接显示器直接连接到 Mac 或外接 GPU 上。你 App 中的每个视图都显示在单个显示器上，而每个显示器都由单个 GPU 驱动。你的视图所显示的显示器，以及驱动该显示器的 GPU，都可能动态变化；因此，你需要让 App 准备好处理这些变化。注册显示变化通知，获取驱动你视图所在显示器的设备，并决定你的 App 是否应使用该设备来呈现渲染后的图形。

### 处理显示变化通知

注册以下通知，以便系统在特定显示变化发生时通知你的 App：

- **[didChangeScreenNotification](../appkit/nswindow/didchangescreennotification.md)** — 当任意窗口（包括包含你视图的窗口）移动到另一台显示器时，系统会发布此通知。
- **[didChangeScreenParametersNotification](../appkit/nsapplication/didchangescreenparametersnotification.md)** — 当 Mac 系统的显示器配置发生变化时，系统会发布此通知；例如，当用户从系统连接或断开一台外接显示器时。另一个例子是驱动显示器的 GPU 发生变化时，例如系统启用了自动显卡切换，在独立 GPU 和集成 GPU 之间切换以驱动显示器。

当系统发布显示变化通知时，你可以决定是否需要获取并使用新设备。

**Swift**

```swift
@objc func handleDisplayChanges(notification: NSNotification) {
    // Handle display changes
}

func registerForDisplayChangeNotifications() {
    NotificationCenter.default.addObserver(self,
                                           selector: #selector(handleDisplayChanges(notification:)),
                                           name: NSNotification.Name(rawValue: "NSWindowDidChangeScreenNotification"),
                                           object: nil)
    
    NotificationCenter.default.addObserver(self,
                                           selector: #selector(handleDisplayChanges(notification:)),
                                           name: NSNotification.Name(rawValue: "NSApplicationDidChangeScreenParametersNotification"),
                                           object: nil)
}
```

**Objective-C**

```objective-c
- (void)handleDisplayChanges:(NSNotification *)notification
{
    // Handle display changes
}

- (void)registerForDisplayChangeNotifications
{
    [[NSNotificationCenter defaultCenter] addObserver:self
                                             selector:@selector(handleDisplayChanges:)
                                                 name:NSWindowDidChangeScreenNotification
                                               object:nil];
    
    [[NSNotificationCenter defaultCenter] addObserver:self
                                             selector:@selector(handleDisplayChanges:)
                                                 name:NSApplicationDidChangeScreenParametersNotification
                                               object:nil];
}
```

要取消注册前述通知，调用 [removeObserver(_:name:object:)](<../foundation/notificationcenter/removeobserver(__name_object_).md>) 方法。

### 识别驱动你视图显示的设备

获取你视图当前所显示的显示器的 [CGDirectDisplayID](../coregraphics/cgdirectdisplayid.md) 值。然后调用 [CGDirectDisplayCopyCurrentMetalDevice(_:)](<../coregraphics/cgdirectdisplaycopycurrentmetaldevice(__).md>) 函数来获取驱动该显示器的设备。

**Swift**

```swift
guard let viewDisplayID = mtkView.window?.screen?.deviceDescription[NSDeviceDescriptionKey("NSScreenNumber")] as? CGDirectDisplayID else { return }
let displayDevice = CGDirectDisplayCopyCurrentMetalDevice(viewDisplayID)
```

**Objective-C**

```objective-c
NSNumber           *screenNumber = _mtkView.window.screen.deviceDescription[@"NSScreenNumber"];
CGDirectDisplayID  viewDisplayID  = [screenNumber unsignedIntValue];
id <MTLDevice>     displayDevice  = CGDirectDisplayCopyCurrentMetalDevice(viewDisplayID);
```

## 另请参阅

### 定位 GPU

- [Finding multiple GPUs on an Intel-based Mac](finding-multiple-gpus-on-an-intel-based-mac.md) — 为你的 App 定位、识别并选择合适的 GPU。
- [MTLCopyAllDevices](<mtlcopyalldevices().md>) — 返回系统中所有 Metal 设备实例的数组。
- [MTLCopyAllDevicesWithObserver(handler:)](<mtlcopyalldeviceswithobserver(handler_).md>) — 返回系统中所有 Metal GPU 设备的数组，并注册一个通知处理程序，在设备列表发生变化时由 Metal 调用。
- [MTLRemoveDeviceObserver](<mtlremovedeviceobserver(__).md>) — 移除一个已注册的设备通知观察者。_(已废弃)_
- [CGDirectDisplayCopyCurrentMetalDevice(_:)](<../coregraphics/cgdirectdisplaycopycurrentmetaldevice(__).md>) — 返回当前驱动某个显示器的 GPU 设备实例。
- [MTLDeviceNotificationHandler](mtldevicenotificationhandler.md) — 一个 Swift 闭包或 Objective-C 代码块，在系统添加或移除 GPU 设备时由 Metal 调用。_(已废弃)_
- [MTLDeviceNotificationName](mtldevicenotificationname.md) — 表示系统中 GPU 设备发生变化的通知。_(已废弃)_
