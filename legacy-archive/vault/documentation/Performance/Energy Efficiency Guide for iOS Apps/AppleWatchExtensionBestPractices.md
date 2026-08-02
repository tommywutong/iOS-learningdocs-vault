---
title: Energy Efficiency Guide for iOS Apps
apple_id: TP40015243
resource_type: Guide
platform: watchOS|iOS
topic: Performance
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/AppleWatchExtensionBestPractices.html
archived_at: '2026-07-18T01:47:16.343685Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Energy Efficiency Guide for iOS Apps](index.md)



## Apple Watch Best Practices

Many of the features of Apple Watch, such as turning off the screen when the user lowers their wrist, were designed with energy conservation in mind. The watchOS API is also very efficient. All Apple Watch apps gain the benefits of the API, but should still adhere to the same general guidelines as any energy-conscious iOS app.

### Minimize Networking

Data transfers on Apple Watch require system resources, such as radios, to power up and use significant energy.

- Minimize traffic between the watch and the phone. Be aware that interaction between an iPhone and an Apple Watch impacts battery on both devices. Use the Watch Connectivity framework APIs for optimized data transfer methods. See [Communicating with Your Companion iOS App](https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/SharingData.html#//apple_ref/doc/uid/TP40014969-CH29-SW3) in _[App Programming Guide for watchOS](https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)_.
- Reduce network activity. Batch transactions together to the extent possible, rather than sending and receiving information bit by bit. Use `NSURLSession` background sessions to defer nonessential network activity until energy efficient times. See [Delay Deferrable Network Operations](DeferNetworking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqmjyfvjvomy).

### Optimize Graphics and Media

Every time your app updates content on the display, the CPU, GPU, and screen are active.

- Eliminate unnecessary content updates. See [Avoid Extraneous Graphics and Animations](AvoidExtraneousGraphicsAndAnimations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqmjzfvjvomi).
- Use darker colors. Brighter colors require significantly more energy to display. Whenever possible, use black for your app’s background. Aside from saving energy, this also has a side benefit of blending seamlessly with the Apple Watch bezel to create the illusion of an edgeless screen.
- Keep media sizes small. If your app downloads images from a server, for example, provide images that are appropriately sized for viewing on a watch-sized screen. Don’t download larger images and attempt to scale them down on the device—this uses both excess network and CPU resources.

### Reduce Work

Although the watchOS API is pretty efficient, doing lots of heavy work can still drain the battery.

- Do less work. If your app requires complex or lengthy operations, consider offloading it the iPhone for processing. First, there may not be enough time to complete the work before user interaction completes and your app is suspended.

[Bluetooth Best Practices](BluetoothBestPractices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqmryfvjvomi)

[Observe Signs of Energy Leaks](SignsofEnergyLeaks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqmzsfvjvomi)
