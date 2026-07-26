---
title: nibName
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontroller/nibname
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/nibname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/nibname.json'
content_hash: 'sha256:060be73aab817b60'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# nibName

<sub>Instance Property</sub>

The name of the view controller’s nib file, if one was specified.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var nibName: String? { get }
```

## Discussion

This property contains the value specified at initialization time to the [- initWithNibName:bundle:](<init(nibname_bundle_).md>) method. The value of this property may be `nil`.

If you use a nib file to store your view controller’s view, it is recommended that you specify that nib file explicitly when initializing your view controller. However, if you do not specify a nib name, and do not override the [- loadView](<loadview().md>) method in your custom subclass, the view controller searches for a nib file using other means. Specifically, it looks for a nib file with an appropriate name (without the `.nib` extension) and loads that nib file whenever its view is requested. Specifically, it looks (in order) for a nib file with one of the following names:

1. If the view controller class name ends with the word ‘Controller’, as in `MyViewController`, it looks for a nib file whose name matches the class name without the word ‘Controller’, as in `MyView.nib`.
2. It looks for a nib file whose name matches the name of the view controller class. For example, if the class name is `MyViewController`, it looks for a `MyViewController.nib` file.

> [!note] Note
> Nib names that include a platform-specific identifier such as `~iphone` or `~ipad` are loaded only on a device of the corresponding type. For example, a nib name of `MyViewController~ipad.nib` is loaded only on iPad. If your app supports both platform types, you must provide versions of your nib files for each platform.

## See Also

### Related Documentation

- [- initWithNibName:bundle:](<init(nibname_bundle_).md>) — Creates a view controller with the nib file in the specified bundle.

### Getting the storyboard and nib information

- [storyboard](storyboard.md) — The storyboard from which the view controller originated.
- [nibBundle](nibbundle.md) — The view controller’s nib bundle if it exists.
