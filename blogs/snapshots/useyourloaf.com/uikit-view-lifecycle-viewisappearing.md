---
title: UIKit View Lifecycle - viewIsAppearing
source_url: 'https://useyourloaf.com/blog/uikit-view-lifecycle-viewisappearing/'
source_domain: useyourloaf.com
source_group: single-site
original_language: en
published: 2023-09-25
archived_at: 2026-07-27
content_hash: 'sha256:5771218ce7a25ca9'
plan_ref: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 5｜生命周期必须按场景观测（对应 W5-06）
plan_week: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期
plan_day: Day 5｜生命周期必须按场景观测（对应 W5-06）
container: '//*[contains(@class,''article-content'')]'
container_source: guess
---

> 原文：[UIKit View Lifecycle - viewIsAppearing](https://useyourloaf.com/blog/uikit-view-lifecycle-viewisappearing/)

Apple added a new view controller lifecycle callback in iOS 17 that’s back-deployable to iOS 13. Here’s a quick guide to viewIsAppearing.

### View Controller Lifecycle

A `UIViewController` has a number of methods that UIKit calls as it moves the view controller’s view on and off screen:

- **viewDidLoad**: Called after the view controller has loaded its view but not yet added it to the view hierarchy. Called only **once** in the life of the view controller.
- **viewWillAppear**: Called when the view controller’s view is about to be added to the view hierarchy. Unlike viewDidLoad this method can be called **multiple times** in the life of a view controller as the view is moved on and off screen. There’s a corresponding ****viewWillDisappear** called when the view is about to be removed from the view hierarchy.
- **viewDidAppear**: Called after view controller’s view is added to the view hierarchy and displayed on-screen. Like viewWillAppear this method is called each time the view appears on-screen and has a corresponding method, viewDidDisappear, called after removing the view.

The important point to remember about these methods is that the views frame (size and position) and traits, like the horizontal/vertical size class, are not updated until after the view has been added to the view hierarchy.

This leads to a problem if you want to update the view based on its size or traits. It’s too early in viewDidLoad or viewWillAppear as the view is not yet added to the view hierarchy, and if you wait until viewDidAppear the view is already onscreen and visible.

### Predicting Trait Changes?

I should add a caveat at this point. In iOS 13, Apple made a change where UIKit predicts the initial traits for a view when you create it. See [predicting size classes in iOS 13](https://useyourloaf.com/blog/predicting-size-classes-in-ios-13/). That means you can update views/layout in viewDidLoad based on the predicted traits:

```swift
override func viewDidLoad() {
  super.viewDidLoad()
  enableConstraintsForWidth(traitCollection.horizontalSizeClass)
}
```

If the system gets the predicted traits wrong you still get a call to `traitCollectionDidChange` where you can make the necessary changes:

```swift
override func traitCollectionDidChange(previousTraitCollection: UITraitCollection?) {
  super.traitCollectionDidChange(previousTraitCollection)
  if traitCollection.horizontalSizeClass != previousTraitCollection?.horizontalSizeClass {
    enableConstraintsForWidth(traitCollection.horizontalSizeClass)
  }
}
```

That works, but is somewhat confusing and easy to get wrong.

Note: **`traitCollectionDidChange` is deprecated in iOS 17**, replaced with a more flexible API where you register for specific trait changes. I’ll cover that in a future post.

### viewIsAppearing

Apple added a new method **viewIsAppearing** in iOS 17 that clears up the confusion. Even better this new method is **back-deployable to iOS 13**. There’s no need to wait until you can require iOS 17 to adopt the new API.

The **viewIsAppearing** method is called after **viewWillAppear** but before **viewDidAppear**. The key difference is that it’s called after the view has been added to the hierarchy but is not yet onscreen. The view controller’s view has been laid out so you can rely on its size and traits.

**This make it a great place to update any UI just before the view appears onscreen**.

```swift
override func viewIsAppearing(_ animated: Bool) {
  super.viewIsAppearing(animated)
  enableConstraintsForWidth(traitCollection.horizontalSizeClass)
}
```

### What Should You Do?

If you’ve been relying on the predicated traits to update UI in **viewDidLoad** you might want to move that code to **viewIsAppearing**. Be aware that this new callback can be called **multiple times** if the view appears more than once (for example as a result of navigation).

### Learn More

- [WWDC23 What’s new in UIKit](https://developer.apple.com/videos/play/wwdc2023/10055/)
