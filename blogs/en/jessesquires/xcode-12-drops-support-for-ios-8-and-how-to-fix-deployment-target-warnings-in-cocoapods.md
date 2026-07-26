---
title: Xcode 12 drops support for iOS 8 and how to fix deployment target warnings in CocoaPods
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2020/07/20/xcode-12-drops-support-for-ios-8-fix-for-cocoapods/'
original_language: en
published: 2020-07-20
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d2d9af026e9dd2ef'
translated: false
---

> 原文：[Xcode 12 drops support for iOS 8 and how to fix deployment target warnings in CocoaPods](https://www.jessesquires.com/blog/2020/07/20/xcode-12-drops-support-for-ios-8-fix-for-cocoapods/)　·　Jesse Squires

The [release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-12-beta-release-notes) for Xcode 12 beta state that the release “supports on-device debugging for iOS 9 and later, tvOS 9 and later, and watchOS 2 and later.” I am not sure if that means support for building and deploying for iOS 8 is **completely** removed, but it sounds like it. Who is still deploying to iOS 8, anyway?

If you are using CocoaPods with Xcode 12 beta, then you have probably seen this error:

```
The iOS Simulator deployment target 'IPHONEOS_DEPLOYMENT_TARGET' is set to 8.0, but the range of supported deployment target versions is 9.0 to 14.0.99.
```

This is happening because support for iOS 8 has been dropped, but the minimum deployment target for the pod is iOS 8. [This older GitHub issue](https://github.com/CocoaPods/CocoaPods/issues/7314) on CocoaPods discusses this a bit, as well as [this recently opened issue](https://github.com/CocoaPods/CocoaPods/issues/9884). Note that even if your minimum deployment target is greater than iOS 8, you will still see this error.

Until this is fixed in CocoaPods, you can add the following to your `Podfile` as a workaround:

```
post_install do |installer|
  installer.pods_project.targets.each do |target|
    target.build_configurations.each do |config|
      config.build_settings.delete 'IPHONEOS_DEPLOYMENT_TARGET'
    end
  end
end
```

This will remove all deployment target settings from all of the pods in your project, which allows them to simply inherit the project/workspace deployment target that you have specified at the top of your `Podfile`.
