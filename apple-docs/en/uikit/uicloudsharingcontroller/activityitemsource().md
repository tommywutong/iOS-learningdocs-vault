---
title: activityItemSource()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicloudsharingcontroller/activityitemsource()
source_url: 'https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/activityitemsource()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicloudsharingcontroller/activityitemsource%28%29.json'
content_hash: 'sha256:44009b38985f0109'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICloudSharingController](../uicloudsharingcontroller.md)

# activityItemSource()

<sub>Instance Method</sub>

The activity item object that can be used by an activity view controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func activityItemSource() -> any UIActivityItemSource
```

## Discussion

Use [- activityItemSource](<activityitemsource().md>), an object that conforms to the [UIActivityItemSource](../uiactivityitemsource.md) protocol, when you want to include the CloudKit Sharing action as one of the action items in an instance of [UIActivityViewController](../uiactivityviewcontroller.md).

Including [- activityItemSource](<activityitemsource().md>) in an activity view controller can be useful when your app’s user interface doesn’t have space to display a button dedicated to CloudKit Sharing. For instance, say your app already has an action button that lets the user share data with social media sites or other apps through an activity view controller. If you include [- activityItemSource](<activityitemsource().md>) as one of the activity view controller’s action items, the controller includes the action as a user-selectable option, thus eliminating the need for a second button in your app’s user interface.

**Swift**

```swift
let items = [cloudSharingController.activityItemSource()]
let activityController = UIActivityViewController(activityItems: items, applicationActivities: [])
present(activityController, animated: true, completion: {})
```

**Objective-C**

```objc
NSArray *items = @[[cloudSharingController activityItemSource]];
UIActivityViewController *activityController = [[UIActivityViewController alloc] initWithActivityItems:items applicationActivities:nil];
[self presentViewController:activityController animated:YES completion:^{}];
```
