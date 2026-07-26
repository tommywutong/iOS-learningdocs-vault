---
title: Xcode 11 与 iOS 13 适配
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/xcode-11-adapts-to-ios-13/'
original_language: zh
published: 2019-10-13
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:9b72ddbe1360f7b0'
translated: n/a
---

> 原文：[Xcode 11 与 iOS 13 适配](https://dirtmelon.github.io/posts/xcode-11-adapts-to-ios-13/)　·　dirtmelon

## 启动白屏

在 iOS 13 以下的版本中，如果你在 App 中替换了 `window.rootViewController` 那么会有一个 `UITransitionView` 的界面遗留在 `window` 上无法释放，苹果并不推荐我们在 App 运行时替换 `window.rootViewController` 。但是有时业务确实需要我们怎么做，比如只有登录后可以使用 App ，我们可以在登录后替换 `window.rootViewController` 。但是到了 iOS 13 情况变得不一样了，iOS 13 可能调整了流程，如果移除了 `UITransitionView` 应用就会白屏，所以需要调整下代码逻辑，添加判断是否为 iOS 13。

```swift
func setRootViewController(_ newRootViewController: UIViewController,
                             withTransition transition: CATransition? = nil) {
    rootViewController?.dismiss(animated: false, completion: { [weak self] in
      self?.rootViewController?.view.removeFromSuperview()
    })
    if let transition = transition {
      layer.add(transition, forKey: kCATransition)
    }
    rootViewController = newRootViewController
    if UIView.areAnimationsEnabled {
      UIView.animate(withDuration: CATransaction.animationDuration()) {
        newRootViewController.setNeedsStatusBarAppearanceUpdate()
      }
    } else {
      newRootViewController.setNeedsStatusBarAppearanceUpdate()
    }
    if #available(iOS 13.0, *) {
    } else {
      if let transitionViewClass = NSClassFromString("UITransitionView") {
        for subview in subviews where subview.isKind(of: transitionViewClass) {
          subview.removeFromSuperview()
        }
      }
    }
  }
}
```

## UIModalPresentationStyle

在 iOS 13 上，使用 `presentViewController` 弹出 `ViewController` 时，默认样式如下：

![1*Dne8HWkv4CzYDcTN1d79gw](https://raw.githubusercontent.com/dirtmelon/blog-images/main/1*Dne8HWkv4CzYDcTN1d79gw.jpeg)

大部分情况下我们需要的还是原来的样式，需要将 `viewController` 的 `modalPresentationStyle` 改为 `overFullScreen` ，但是一个个手动去改，工作量也比较大，此时就需要用到 `method swizzle` 了，[Referencing the Objective-C selector of property getters and setters](https://github.com/apple/swift-evolution/blob/7fcba970b88a5de3d302d291dc7bc9dfba0f9399/proposals/0064-property-selectors.md) 这份提案有说到 `Swift` 是支持获取 `getter` 和 `setter` 对应的 `selector` ，然后我们需要替换 `modalPresentationStyle` 的默认值，改为 `overFullScreen` ，这样可以在需要的时候设置为 `autoMatic` 。首先，需要在 `UIViewController` 的 `extension` 中新增 `swizzledModalPresentationStyle` 属性，默认值为 `.overFullScreen` ：

```swift
// MARK: - ModalPresentationStyle
private var modalPresentationStyleKey: UInt8 = 0

extension UIViewController {
  var swizzledModalPresentationStyle: UIModalPresentationStyle {
    set {
      objc_setAssociatedObject(self,
      &modalPresentationStyleKey,
      newValue,
      .OBJC_ASSOCIATION_RETAIN_NONATOMIC)
    }
    get {
      if let presentationStyle =
        (objc_getAssociatedObject(self,
                                  &modalPresentationStyleKey)) as? UIModalPresentationStyle {
        return presentationStyle
      } else {
        return .overFullScreen
      }
    }
  }
}
```

然后再对 `modalPresentationStyle` 的 `setter` 和 `getter` 方法进行 `swizzle`：

```swift
private static var hasSwizzled = false
static func swizzleMethods() {
  guard !hasSwizzled else { return }
  hasSwizzled = true
  [
    (#selector(self.viewDidLoad), #selector(cbViewDidLoad)),
    (#selector(self.viewDidAppear(_:)), #selector(cbViewDidAppear(_:))),
    (#selector(self.viewWillAppear(_:)), #selector(cbViewWillAppear(_:))),
    (#selector(getter: self.preferredStatusBarStyle), #selector(getter: cbPreferredStatusBarStyle)),
    (#selector(getter: self.modalPresentationStyle), #selector(getter: swizzledModalPresentationStyle)),
    (#selector(setter: self.modalPresentationStyle), #selector(setter: swizzledModalPresentationStyle))
    ].forEach { (original, swizzled) in
      guard let originalMethod = class_getInstanceMethod(self, original),
        let swizzledMethod = class_getInstanceMethod(self, swizzled) else { return }
      if class_addMethod(self,
                         original,
                         method_getImplementation(swizzledMethod),
                         method_getTypeEncoding(swizzledMethod)) {
        class_replaceMethod(self,
                            swizzled,
                            method_getImplementation(originalMethod),
                            method_getTypeEncoding(originalMethod))
      } else {
        method_exchangeImplementations(originalMethod, swizzledMethod)
      }
  }
}
```

## Cocoapods 与 Xcode New Build System

如果你有至少一个 Pods 包含 `Assets.xcassets` ，那么在打包的时候就会生成重复的图片到 App 的根路径下的 `Assets.car` 中，在使用 Xcode 11 build 时，那么就会报错，显示你有 duplicate output file 。 如果你的 Pods 包含 `Assets.xcassets` ，那么应该在 `Input File` 列表中，具体讨论可以看这里 [Xcode 10 new build system makes asset catalog invalid specified by podspec’s`resource(s)`](https://github.com/CocoaPods/CocoaPods/issues/8122)，里面也有说到具体的解决方案。
