---
title: UIStoryboardViewControllerCreator
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistoryboardviewcontrollercreator
source_url: 'https://developer.apple.com/documentation/uikit/uistoryboardviewcontrollercreator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistoryboardviewcontrollercreator.json'
content_hash: 'sha256:020fb3095879c65d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIStoryboardViewControllerCreator

<sub>Type Alias</sub>

A handler block that contains the custom initialization code for a view controller you instantiate from a storyboard.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
typedef __kindof UIViewController *(^)(NSCoder *) UIStoryboardViewControllerCreator;
```

## Parameters

- `coder` — The coder object containing the storyboard data to use when configuring the view controller. Pass this coder object to any methods you use to restore the state of the view controller and its views. For example, you might pass it to the view controller’s [- initWithCoder:](<uiviewcontroller/init(coder_).md>) method before initializing any other custom properties.

## See Also

### Storyboards

- [Customizing the behavior of segue-based presentations](customizing-the-behavior-of-segue-based-presentations.md) — Pass data between view controllers during a segue, and programmatically control when segues occur.
- [Dismissing a view controller with an unwind segue](dismissing-a-view-controller-with-an-unwind-segue.md) — Configure an unwind segue in your storyboard file that dynamically chooses the most appropriate view controller to display next.
- [UIStoryboard](uistoryboard.md) — An encapsulation of the design-time view controller graph represented in an Interface Builder storyboard resource file.
- [UIStoryboardSegue](uistoryboardsegue.md) — An object that prepares for and performs the visual transition between two view controllers.
- [UIStoryboardUnwindSegueSource](uistoryboardunwindseguesource.md) — An encapsulation of information about an unwind segue.
