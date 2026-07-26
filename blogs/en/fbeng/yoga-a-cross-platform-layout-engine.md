---
title: 'Yoga: A cross-platform layout engine'
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2016/12/07/android/yoga-a-cross-platform-layout-engine/'
original_language: en
published: 2016-12-07
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:175f37002600668f'
translated: false
---

> 原文：[Yoga: A cross-platform layout engine](https://engineering.fb.com/2016/12/07/android/yoga-a-cross-platform-layout-engine/)　·　Meta Engineering — iOS

Layout is an important part of building user interfaces for any mobile, desktop, or web application, because it describes the size and position of views on the screen and their relationship to one another.

Today, layout is handled differently on each platform, through systems like Auto Layout on iOS, composable containers on Android, and various CSS-based approaches on the web. Having such a diverse set of layout systems makes it hard for teams building products to share solutions across platforms and increases the amount of time developers spend fixing platform-specific layout bugs.

At Facebook, we want engineers to be able to build products across multiple platforms without needing to learn a new layout system for each. With React Native, we introduced a solution to this problem in the form of css-layout, a cross-platform implementation of the [Flexbox spec](https://www.w3.org/TR/css-flexbox-1/). Since then, several teams have come together to help fix bugs, improve performance, and make css-layout more spec-compliant.

Today we are excited to officially relaunch css-layout as Yoga, a stand-alone layout engine that extends beyond React Native and allows product engineers to build layouts quickly for multiple platforms.

We chose to implement Yoga in C to better optimize its performance, and we saw a 33 percent improvement to layout times on Android compared with the previous Java implementation. C also gives us the ability to easily integrate Yoga into more platforms and frameworks. To date, Yoga has bindings for Java (Android), Objective-C (UIKit), and C# (.NET), and is being used in projects such as [React Native](https://facebook.github.io/react-native), [Components for Android](https://engineering.fb.com/posts/531104390396423/components-for-android-a-declarative-framework-for-efficient-uis), and [Oculus](https://www.oculus.com). We are also in the process of migrating some views in Instagram to Yoga via the UIKit bindings, and we’re integrating Yoga into [ComponentKit](http://componentkit.org) as well.

## Complex layouts made simple

Let’s dive into a code sample using the UIKit bindings. (Examples in other languages can be found [here](https://facebook.github.io/yoga/).) We’ll cover just the layout portion of the below image, as styling (applying colors, etc.) is left to the platform’s UI framework.

![](https://engineering.fb.com/wp-content/uploads/2016/12/GK9o6gBJg0GIL24EAAAAAADPDXQobj0JAAAB.jpg)

As with any layout, we start with a root. In this case, we know the size we want and pass it to the view’s initializer. The UIKit bindings are implemented as a category on UIView to easily migrate existing layouts. We have to tell the view to use Yoga for layout.

```
UIView *root = [[UIView alloc] initWithFrame:CGRectMake(0, 0, 500, 300)];
[root yg_setUsesYoga:YES];
```

Next, we create the large hero image. We won’t give the image an explicit size, as we want this to be determined by Yoga. By default, views will stretch to fill their parent’s width, and by using `flexGrow` we can make the image take up any height not occupied by the text.

```clike
UIImageView *image = [UIImageView new];
[image yg_setUsesYoga:YES];
[image yg_setFlexGrow:1];
[root addSubview:image];
```

Finally, we create a label to hold our text and give it some margin. Notice that we don’t give this label an explicit height, since Yoga will measure the label to ensure it gets the amount of space it needs.

```clike
UILabel *text = [UILabel new];
[text yg_setUsesYoga:YES];
[text yg_setMargin:20 forEdge:YGEdgeAll];
[root addSubview:text];
```

Once we’ve set up our view hierarchy we tell Yoga to calculate the layout and apply the results to the frames of the views in the hierarchy. We are now ready to display our UI.

```clike
[root yg_applyLayout];
```

We also thought a lot about performance with Yoga. When calculating a layout, Yoga ensures that labels and text views, which typically take a long time to measure, are measured as few times as possible, ideally just once. Yoga also ensures that subsequent calls to `yg_applyLayout` calculate layout only for the views that have changed.

## Open source

For something to be truly cross-platform, it requires expert knowledge from engineers working on a wide variety of platforms and frameworks. Microsoft has been an important contributor to Yoga, contributing fixes as well as features. Huge thanks to them and to everyone else who has contributed to making Yoga what it is today.

Yoga fosters collaboration by allowing developers on all platforms to discuss and come up with the optimal layout for a given UI element together. Sharing a layout implementation across platforms has also enabled us to optimize performance once and see the gains across many product and platforms.

With Yoga we intend to be fully compatible with the web implementation of Flexbox. Over time, however, we have plans to add functionality and properties to Yoga, with the goal of better supporting scenarios not easily described within Flexbox.

Yoga is now available on [GitHub](http://facebook.github.io/yoga). We look forward to hearing your feedback.
