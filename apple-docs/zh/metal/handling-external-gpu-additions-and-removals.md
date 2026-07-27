---
title: 处理外接 GPU 的增加与移除
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/handling-external-gpu-additions-and-removals
source_url: 'https://developer.apple.com/documentation/metal/handling-external-gpu-additions-and-removals'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/handling-external-gpu-additions-and-removals.json'
content_hash: 'sha256:917d34adefa7916d'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md) · [GPU devices and work submission](gpu-devices-and-work-submission.md) · [Multi-GPU systems](multi-gpu-systems.md)

# 处理外接 GPU 的增加与移除

<sub>文章</sub>

注册并响应由用户发起的外接 GPU 通知。

## 概述

用户可以随时从 Mac 上连接或断开外接 GPU。当用户正确地向系统添加和移除外接 GPU 时，会发生以下事件序列：

1. 用户物理连接一个外接 GPU，macOS 将其添加到系统中，Metal 使该 GPU 可供你的 App 使用。
2. 当系统连接有一个或多个外接 GPU 时，macOS 会在菜单栏中显示一个图标，让用户可以安全地断开任意外接 GPU。
3. 用户安全地断开一个外接 GPU。
4. Metal 将该请求通知你的 App，你的 App 将当前及未来的所有工作从该外接 GPU 上迁移出去。
5. 在所有 App（包括你的 App）都已停止使用该外接 GPU 后，macOS 通知用户可以安全断开该 GPU。
6. 系统移除该外接 GPU，以便用户可以将其从 Mac 上物理断开。

你的 App 可以通过恰当地响应这些事件来有效地支持外接 GPU。

> [!warning] 警告
> 用户可以随时从 Mac 上断开外接 GPU，而无需请求或遵循安全断开流程。为你的 App 应对这种可能性做好准备，并对意外移除采取相应措施。

### 设置 GPU 弹出策略

你可以通过配置 App 的 `Info.plist` 中的 `GPUEjectPolicy` 键，来控制你的 App 如何响应对外接 GPU 的安全断开请求。你可以将该键赋值为以下字符串值之一：

- **`"wait"`** — 告知系统你的 App 会手动响应安全断开请求。你的 App 需要注册并响应 Metal 发布的 [MTLDeviceRemovalRequestedNotification](mtldevicenotificationname/removalrequested.md) 通知。系统会等待你的 App 移除对该外接 GPU 的所有引用后，才通知用户可以安全断开该 GPU。
- **`“relaunch”`** — 允许 macOS 退出并使用另一个 GPU 重新启动你的 App。你的 App 可以在退出前通过实现 [application(_:willEncodeRestorableState:)](<../appkit/nsapplicationdelegate/application(__willencoderestorablestate_).md>) 方法保存任何状态，并在启动时通过实现 [application(_:didDecodeRestorableState:)](<../appkit/nsapplicationdelegate/application(__diddecoderestorablestate_).md>) 方法恢复该状态。
- **`“kill”`** — 允许 macOS 强制退出你的 App。

> [!tip] 提示
> 通过将 App 的 `Info.plist` 中的 `GPUEjectPolicy` 键设为 `“wait”`，并恰当地响应安全断开（[MTLDeviceRemovalRequestedNotification](mtldevicenotificationname/removalrequested.md)）通知，来有效地支持外接 GPU。

### 设置 GPU 选择策略

你可以通过配置 App 的 `Info.plist` 中的 `GPUSelectionPolicy` 键，来控制 Metal 是倾向于使用还是避免使用外接 GPU。你可以将该键赋值为以下字符串值之一：

- **`“avoidRemovable”`** — Metal 会尽量避免在外接 GPU 上创建上下文。对于使用旧版 OpenGL 的 App，OpenGL 也会尽量避免为外接 GPU 创建上下文。仅当你的 App 在外接 GPU 上运行不佳时才设置此选项。
- **`“preferRemovable”`** — 如果外接 GPU 对系统可见，Metal 会优先使用它们而非其他 GPU。同样地，对于使用旧版 OpenGL 的 App，OpenGL 也会优先为外接 GPU 创建上下文。

### 注册外接 GPU 通知

调用 [MTLCopyAllDevicesWithObserver](mtlcopyalldeviceswithobserver.md) 函数来获取系统中所有可用 Metal 设备的列表，并注册一个观察者，每当该列表发生变化（或因安全断开请求而可能发生变化）时都会调用它。

**Swift**

```swift
let devicesWithObserver = MTLCopyAllDevicesWithObserver(handler: { (device, name) in
    self.handleExternalGPUEvents(device: device, notification: name)
})
deviceList = devicesWithObserver.devices
deviceObserver = devicesWithObserver.observer
```

**Objective-C**

```objective-c
id <NSObject> deviceObserver  = nil;
NSArray<id<MTLDevice>> *deviceList = nil;
deviceList = MTLCopyAllDevicesWithObserver(&deviceObserver,
                                           ^(id<MTLDevice> device, MTLDeviceNotificationName name) {
                                               [self handleExternalGPUEventsForDevice:device notification:name];
                                           });
_deviceObserver = deviceObserver;
_deviceList = deviceList;
```

要取消注册该观察者，调用 [MTLRemoveDeviceObserver](<mtlremovedeviceobserver(__).md>) 函数。

### 响应外接 GPU 通知

Metal 会就以下外接 GPU 事件通知你的 App：

- **[MTLDeviceWasAddedNotification](mtldevicenotificationname/wasadded.md)** — 当 macOS 向系统添加一个外接 GPU 时，Metal 会发布此通知。评估更新后的设备列表，并考虑使用新增的设备。
- **[MTLDeviceRemovalRequestedNotification](mtldevicenotificationname/removalrequested.md)** — 当用户对某个外接 GPU 发起安全断开请求时，Metal 会发布此通知。你的 App 大约有一秒钟的时间将工作从该设备迁移出去并移除对它的所有引用。如果你的 App 未能做到这一点，macOS 会通知用户，你的 App 正在阻塞安全断开请求。
- **[MTLDeviceWasRemovedNotification](mtldevicenotificationname/wasremoved.md)** — 当 macOS 从系统中移除一个外接 GPU、而你的 App 仍持有对该设备的引用时，Metal 会发布此通知。如果用户安全地断开了一个外接 GPU，Metal 会在发布 [MTLDeviceRemovalRequestedNotification](mtldevicenotificationname/removalrequested.md) 通知之后发布此通知。如果用户意外断开了一个外接 GPU，Metal 会在不先发布 [MTLDeviceRemovalRequestedNotification](mtldevicenotificationname/removalrequested.md) 通知的情况下直接发布此通知。在 macOS 移除一个外接 GPU 后，Metal 会以错误的方式完成该设备排队等待的所有命令缓冲区，并且任何引用该设备的新 API 调用都会以错误告终。

设置一个方法来响应这些通知，并将该方法传递给 [MTLCopyAllDevicesWithObserver](mtlcopyalldeviceswithobserver.md) 函数的 `handler` 参数。

**Swift**

```swift
func handleExternalGPUEvents(device: MTLDevice, notification: MTLDeviceNotificationName) {
    switch notification {
    case .wasAdded:
        // 处理新增
        break
    case .removalRequested:
        // 处理安全断开
        break
    case .wasRemoved:
        // 处理移除
        break
    default:
        break
    }
}
```

**Objective-C**

```objective-c
- (void)handleExternalGPUEventsForDevice:(id<MTLDevice>)device notification:(MTLDeviceNotificationName)notification
{
    if (notification == MTLDeviceWasAddedNotification) {  }
    else if (notification == MTLDeviceRemovalRequestedNotification) {  }
    else if (notification == MTLDeviceWasRemovedNotification) {  }
}
```

## 另请参阅

### 使用外接 GPU

- [Transferring data between connected GPUs](transferring-data-between-connected-gpus.md) — 使用 GPU 之间的高速连接快速传输数据。
