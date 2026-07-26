---
title: UIViewController.ViewLoading
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, tvOS 16.4+, visionOS, Swift 5.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/viewloading
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/viewloading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/viewloading.json'
content_hash: 'sha256:fd0600e964d65c1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# UIViewController.ViewLoading

<sub>Structure</sub>

A property wrapper that loads the view controller’s view before accessing the property.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@propertyWrapper struct ViewLoading<Value>
```

## Overview

Use this property wrapper on view controller properties that can be `nil` before the view controller’s view loads. Wrapping view controller properties this way eliminates crashes that can occur from implicitly defining properties as [Optional](../../swift/optional.md), and then referencing them before the view controller finishes loading.

The following example uses the [ViewLoading](viewloading.md) wrapper to ensure that `dateLabel` [UILabel](../uilabel.md) loads before referencing it in the `didSet` of the `date` property observer:

```swift
class DateViewController: UIViewController {
    @ViewLoading private var dateLabel: UILabel
    
    var date: Date? {
        didSet {
            let dateFormatter = DateFormatter()
            dateFormatter.dateStyle = .full
            let dateString = dateFormatter.string(from: self.date ?? Date())
            // If the view controller's view hasn't loaded yet,
            // accessing the dateLabel property here causes it to load.
            self.dateLabel.text = dateString
        }
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        let label = UILabel(frame: self.view.bounds)
        self.view.addSubview(label)
        self.dateLabel = label
    }
}
```

After loading [UILabel](../uilabel.md), the system can safely access and set the `date` property.

```swift
let dateViewController = DateViewController()
dateViewController.date = Date()
```

Use this property wrapper over implicitly unwrapped optionals for `IBOutlets` as well.

```swift
@IBOutlet @ViewLoading private var dateLabel: UILabel
```

## Topics

### Creating a ViewLoading property wrapper

- [init()](<viewloading/init().md>) — Creates an empty property wrapper that loads the view controller’s view before accessing the property.
- [init(wrappedValue:)](<viewloading/init(wrappedvalue_).md>) — Creates a property wrapper that loads the view controller’s view before accessing the property.

## See Also

### Managing the view’s properties

- [- updateProperties](<updateproperties().md>) — Configures the view controller’s content and styling properties.
- [- updatePropertiesIfNeeded](<updatepropertiesifneeded().md>) — Forces an immediate properties update for this view controller and its view, including any view controllers and views in this subtree.
- [- setNeedsUpdateProperties](<setneedsupdateproperties().md>) — Call to manually request a properties update for the view controller. Multiple requests may be coalesced into a single update alongside the next layout pass.
