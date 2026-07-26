---
title: 在基于 Intel 的 Mac 上查找多个 GPU
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/finding-multiple-gpus-on-an-intel-based-mac
source_url: 'https://developer.apple.com/documentation/metal/finding-multiple-gpus-on-an-intel-based-mac'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/finding-multiple-gpus-on-an-intel-based-mac.json'
content_hash: 'sha256:2bd648d98d2a742e'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md) · [GPU devices and work submission](gpu-devices-and-work-submission.md) · [Multi-GPU systems](multi-gpu-systems.md)

# 在基于 Intel 的 Mac 上查找多个 GPU

<sub>文章</sub>

定位、识别并为你的 App 选择合适的 GPU。

## 概述

在基于 Intel 的 Mac 上，你的 App 可以使用多个 GPU，包括任何内置和外接 GPU。首先获取系统中所有可用 GPU 的列表，然后将工作负载提交给适合你 App 任务的那些 GPU。

> [!note] 注意
> 搭载 Apple 芯片的 Mac 电脑只有一个高性能、高能效的 GPU。

### 获取 GPU 设备列表

你的 App 可以通过调用 [MTLCopyAllDevices](<mtlcopyalldevices().md>) 函数，获取一个 [MTLDevice](mtldevice.md) 实例数组，其中每个实例都代表一个可用的 GPU。

**Swift**

```swift
let devices = MTLCopyAllDevices()
```

**Objective-C**

```objective-c
NSArray<id<MTLDevice>> *devices = MTLCopyAllDevices();
```

不过，该函数提供的是那一时刻可用 GPU 的列表。要获取当前列表并注册设备更新通知，可以通过调用 [MTLCopyAllDevicesWithObserver](mtlcopyalldeviceswithobserver.md) 函数，向 Metal 提供一个处理程序。

**Swift**

```swift
let (devices, observer) = MTLCopyAllDevicesWithObserver() { (device, notification) in
    self.device(device, issued: notification)
}
```

**Objective-C**

```objective-c
id<NSObject> deviceObserver = nil;
NSArray<id<MTLDevice>> *devices = nil;

devices = MTLCopyAllDevicesWithObserver(&deviceObserver,
                                        ^(id<MTLDevice> device,
                                          MTLDeviceNotificationName name) {
    [self device:device hasNotification:name];
});
```

当系统在系统中添加或移除某个 [MTLDevice](mtldevice.md) 时，Metal 会调用你的处理程序来通知你的 App。

> [!note] 注意
> 当某个设备将来可能改变其状态时（例如某人发起了安全断开请求），Metal 会调用你 App 的处理程序。更多信息请参阅[处理外接 GPU 的添加和移除](handling-external-gpu-additions-and-removals.md)。

当你的 App 不再需要来自系统的 GPU 设备更新时，可以通过调用 [MTLRemoveDeviceObserver](<mtlremovedeviceobserver(__).md>) 函数注销其观察者。

**Swift**

```swift
MTLRemoveDeviceObserver(observer)
```

**Objective-C**

```objective-c
MTLRemoveDeviceObserver(deviceObserver);
```

### 按类型识别每个 GPU

Mac 电脑系统中的每个 GPU 可以是以下三种类型之一：集成、独立或外接。你可以通过检查每个 [MTLDevice](mtldevice.md) 实例的 [lowPower](mtldevice/islowpower.md) 和 [removable](mtldevice/isremovable.md) 属性来识别其类型。

| GPU 类型 | [lowPower](mtldevice/islowpower.md) | [removable](mtldevice/isremovable.md) |
|---|---|---|
| 集成 | [true](../swift/true.md) | [false](../swift/false.md) |
| 独立 | [false](../swift/false.md) | [false](../swift/false.md) |
| 外接 | [false](../swift/false.md) | [true](../swift/true.md) |

举例来说，你可以使用这些属性为每种 GPU 类型构建一个设备列表。

**Swift**

```swift
var externalGPUs = [MTLDevice]()
var discreteGPUs = [MTLDevice]()
var integratedGPUs = [MTLDevice]()

for device in devices {
    if device.isRemovable { externalGPUs.append(device) } else
    if device.isLowPower { integratedGPUs.append(device) } else {
        discreteGPUs.append(device)
    }
}
```

**Objective-C**

```objective-c
NSMutableArray<id<MTLDevice>> *externalGPUs = [[NSMutableArray alloc] init];
NSMutableArray<id<MTLDevice>> *discreteGPUs = [[NSMutableArray alloc] init];
NSMutableArray<id<MTLDevice>> *integratedGPUs = [[NSMutableArray alloc] init];

for (id<MTLDevice> device in devices) {
    if (device.isRemovable) { [externalGPUs addObject:device]; }
    else if (device.isLowPower) { [integratedGPUs addObject:device]; }
    else { [discreteGPUs addObject:device]; }
}
```

某些外接或独立 GPU 也可能是_无头（headless）_的，也就是说它们没有连接显示器。你的 App 可以通过检查某个设备实例的 [headless](mtldevice/isheadless.md) 属性，来判断某个 GPU 是否无头。

**Swift**

```swift
if device.isHeadless {
    // This GPU device isn't connected to any displays.
    ...
}
```

**Objective-C**

```objective-c
if (device.isHeadless) {
    // This GPU device isn't connected to any displays.
    ...
}
```

### 为你的工作负载选择合适的 GPU

在拥有多个 GPU 的系统中，每种 GPU 类型对于特定的任务或工作负载都有各自的优势，供你参考。

| GPU 类型 | 功耗 | 内存带宽 |
|---|---|---|
| 集成 | 低 | 高 |
| 独立 | 中 | 高 |
| 外接 | 高 | 低 |

一般来说，先从集成 GPU 开始（如果系统有的话），以节省电力并延长设备的电池续航。如果你的 App 需要额外的图形或计算处理能力，可以考虑将部分工作负载转移到独立 GPU 上（如果系统有的话）。

> [!tip] 提示
> 你的 App 可以让用户选择使用哪个 GPU 来处理其工作负载，尤其是在他们的系统上连接了外接 GPU 的情况下。

与内部 GPU 相比，外接 GPU 通常具备强大的处理能力，但带宽较低，这使它们非常适合每帧不需要大量内存带宽的任务，包括：

- 渲染高复杂度的图形场景
- 渲染高分辨率的图形内容
- 在渲染图形的同时处理计算工作负载
- 处理算术逻辑单元（ALU）复杂度较高的计算工作负载

有关 GPU 内存带宽的更多信息，请参阅[针对 GPU 内存带宽权衡进行调整](adjusting-for-gpu-memory-bandwidth-tradeoffs.md)。

> [!note] 注意
> 由于无头 GPU 没有连接显示器，它比起为显示器渲染图形，更适合用于计算处理。

## 另请参阅

### Locating GPUs

- [获取驱动某个视图显示的 GPU](getting-the-gpu-that-drives-a-views-display.md) — 让你的显示始终使用最优的设备。
- [MTLCopyAllDevices](<mtlcopyalldevices().md>) — 返回系统中所有 Metal 设备实例的数组。
- [MTLCopyAllDevicesWithObserver(handler:)](<mtlcopyalldeviceswithobserver(handler_).md>) — 返回系统中所有 Metal GPU 设备的数组，并注册一个通知处理程序，供 Metal 在设备列表发生变化时调用。
- [MTLRemoveDeviceObserver](<mtlremovedeviceobserver(__).md>) — 移除一个已注册的设备通知观察者。_(已废弃)_
- [CGDirectDisplayCopyCurrentMetalDevice(_:)](<../coregraphics/cgdirectdisplaycopycurrentmetaldevice(__).md>) — 返回当前正在驱动某个显示器的 GPU 设备实例。
- [MTLDeviceNotificationHandler](mtldevicenotificationhandler.md) — 一个 Swift 闭包或 Objective-C block，供系统添加或移除 GPU 设备时由 Metal 调用。_(已废弃)_
- [MTLDeviceNotificationName](mtldevicenotificationname.md) — 代表系统中某个 GPU 设备发生变化的通知。_(已废弃)_
