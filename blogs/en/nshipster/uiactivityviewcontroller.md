---
title: UIActivityViewController
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/uiactivityviewcontroller/'
original_language: en
published: 2014-04-21
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:e03c88a92be53ce3'
translated: false
---

> 原文：[UIActivityViewController](https://nshipster.com/uiactivityviewcontroller/)　·　NSHipster (Mattt)

# [UIActivity​View​Controller](https://nshipster.com/uiactivityviewcontroller/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  December 5^th, 2018 ([revised](https://github.com/nshipster/articles/commits/master/2014-04-21-uiactivityviewcontroller.md))

On iOS, `UIActivityViewController` provides a unified interface for users to share and perform actions on strings, images, URLs, and other items within an app.

You create a `UIActivityViewController` by passing in the items you want to share and any custom activities you want to support (we’ll show how to do that later on). You then present that view controller as you would any other modal or popover.

```
let string = "Hello, world!"
let url = URL(string: "https://nshipster.com")!
let image = UIImage(named: "mustache.jpg")
let pdf = Bundle.main.url(forResource: "Q4 Projections",
                            withExtension: "pdf")

let activityViewController =
    UIActivityViewController(activityItems: [string, url, image, pdf],
                             applicationActivities: nil)

present(activityViewController, animated: true) {
    …
}
```

When you run this code the following is presented on the screen:

![UIActivityViewController](https://nshipster.com/assets/uiactivityviewcontroller-a7b5cb0c237bc73fb43ca87c87d0c087954edf0e214c68978017411f65042d1feea8f49747005ade4bedc17d037b2cf55b41854d5682ad798fcc040dd73e7f73.png)

By default, `UIActivityViewController` shows all the activities available for the items provided, but you can exclude certain activity types via the `excludedActivityTypes` property.

```
activityViewController.excludedActivityTypes = [.postToFacebook]
```

Activity types are divided up into “action” and “share” types:

- **Action** (`UIActivityCategoryAction`) activity items take an action on selected content, such as copying text to the pasteboard or printing an image.
- **Share** (`UIActivityCategoryShare`) activity items share the selected content, such as composing a message containing a URL or posting an image to Twitter.

Each activity type supports certain kinds of items. For example, you can post a String, URL, and / or image to Twitter, but you can’t assign a string to be the photo for a contact.

The following tables show the available activity types for each category and their supported items:

### UIActivityCategoryAction

|  | ![](https://nshipster.com/assets/uiactivity-icon-string-55c9ded9ca09f0e5db733b4b3378e7482a249b29594e48b28617043e4dba51761020cc13676677d5fadec47e54002d4fb89c7af7435ac67f8cf6cd4042e9ab50.svg) | ![](https://nshipster.com/assets/uiactivity-icon-url-f87bd59f35af62cd2a7afedbe0a6b43e66f84d86df3db15bb5e61d664a8c2bde46c2a6eed08c5753192248c41f31874139ed04a93765e1640a9fe47baab27c8a.svg) | ![](https://nshipster.com/assets/uiactivity-icon-image-3b35917dcaa50934db09712deda347c760070179af8fa3399144ec26441eac151a058a82425a88d1628b0cd8c36390a01521a2fc14a741d7c2e980791401c0c5.svg) | ![](https://nshipster.com/assets/uiactivity-icon-file-61a5c19374369730d0ceac3c0ecf326c3019a154f3ac965842295b73449fb7c57543ee16e2701814e4ae8fce4de6153688ca01f122f1811694a47d863357d9cd.svg) |  |
|---|---|---|---|---|---|
| String | URL | Image | Files |  |  |
| ![](https://nshipster.com/assets/uiactivity-airDrop-0f475bc254bf525c3e021897820d9bcc7bd47a1f94a2056cbf74946d5ada81be659d3aaee4f07c30e012b6b66a8a12b8998ea45d7f8d7d6ad500c13aaddf28bd.png) | `airDrop` | ✓ | ✓ | ✓ | ✓ |
| ![](https://nshipster.com/assets/uiactivity-addToReadingList-a5094c0677caa80b1c5825daa74d50a48d6a5a0b1bb0490e7eb3bfa8bce822455e2304e170bc980370d339fd4c9804bdc48dfe5c07585156c9ea1433bb29ab39.png) | `addToReadingList` |  | ✓ |  |  |
| ![](https://nshipster.com/assets/uiactivity-assignToContact-a9928035511696c4d45cd5bba1df532fa94647ac93ce481411e88090e92713cd6e5b5bf5b7251dd130ddd7f6aeb4c7575376d353458a12984e8a722c8fe5f97c.png) | `assignToContact` |  |  | ✓ |  |
| ![](https://nshipster.com/assets/uiactivity-copyToPasteboard-3bfee55629fe439a4aa67fb76ae2817f4d0e9f6283bc7592241b1ac6e11fc60f76c807fff56008d4ff991888fff95c7e976bd951ec2149bb040a820955169aa2.png) | `copyToPasteboard` | ✓ | ✓ | ✓ | ✓ |
| ![](https://nshipster.com/assets/uiactivity-print-ebbf06eca8a4b5710251a5a85d07e2a56f74d86ac40e750a2b8e58346fbdf919661808bc46f451710a67c3cd83aac6de5c6cbff4d0566301d6787bbd0486ea05.png) | `print` |  |  | ✓ | ✓ |
| ![](https://nshipster.com/assets/uiactivity-saveToCameraRoll-5bc7e785d3ec57062328b37483e84243bac6219ca590eb5e3ffa444eab0d6fb1ce0fb8eb30dd9b1ab5a0aeda6d967a37711ab2bb559187b95246a6b0444a1d58.png) | `saveToCameraRoll` |  | ✓ | ✓ |  |

### UIActivityCategoryShare

|  | ![](https://nshipster.com/assets/uiactivity-icon-string-55c9ded9ca09f0e5db733b4b3378e7482a249b29594e48b28617043e4dba51761020cc13676677d5fadec47e54002d4fb89c7af7435ac67f8cf6cd4042e9ab50.svg) | ![](https://nshipster.com/assets/uiactivity-icon-url-f87bd59f35af62cd2a7afedbe0a6b43e66f84d86df3db15bb5e61d664a8c2bde46c2a6eed08c5753192248c41f31874139ed04a93765e1640a9fe47baab27c8a.svg) | ![](https://nshipster.com/assets/uiactivity-icon-image-3b35917dcaa50934db09712deda347c760070179af8fa3399144ec26441eac151a058a82425a88d1628b0cd8c36390a01521a2fc14a741d7c2e980791401c0c5.svg) | ![](https://nshipster.com/assets/uiactivity-icon-file-61a5c19374369730d0ceac3c0ecf326c3019a154f3ac965842295b73449fb7c57543ee16e2701814e4ae8fce4de6153688ca01f122f1811694a47d863357d9cd.svg) |  |
|---|---|---|---|---|---|
| String | URL | Image | Files |  |  |
| ![](https://nshipster.com/assets/uiactivity-mail-7f431d2600f303d10adea429b534d5e4f424382095f56869dfde6dcc8af6aa27a9194e755b9b2ab335197056a0e51855801feb34116da4591ee41c3c7342036a.png) | `mail` | ✓ | ✓ | ✓ | ✓ |
| ![](https://nshipster.com/assets/uiactivity-message-a295878c0985b7b4c651d9662e7c83df5a12bb1a81593eb3d798c7959a0edcb961a2b34cd2412797638b6d4ac31d85e6a1aa239be10704936ca00e007fa663fc.png) | `message` | ✓ | ✓ | ✓ | ✓ |
| ![](https://nshipster.com/assets/uiactivity-postToFacebook-f2ccc550c13e408a80a3e68c76968fdd7b6fd721bbc8538bc8f61390cedd5b6793f04c34dd88d00e8f6c45557d2ac0cab920e4df356da6d4914548efeb45b6a6.png) | `postToFacebook` | ✓ | ✓ | ✓ |  |
| ![](https://nshipster.com/assets/uiactivity-postToFlickr-5cd79c791edc24b3bedfbfff98d44c52c50af8f735ea24e1226adaff1253fed47defcaaecbe8ea64c9b8a430841a4b3f0a561ddc794c40689c2134cbb25e4480.png) | `postToFlickr` |  | ✓ | ✓ |  |
| ![](https://nshipster.com/assets/uiactivity-postToTencentWeibo-09e5c7fd6bf6b7d236c9d59ec13026aaaf33bf2fbb20ed39ed68b9f53d521683ef81fc6cb384230bef7e3cabc55ca4b911dfc9eea0a7e19786bceaac9147d35f.png) | `postToTencentWeibo` | ✓ | ✓ | ✓ |  |
| ![](https://nshipster.com/assets/uiactivity-postToTwitter-bc8d41db04b9941fa327ca3b98f18836531899d57cdde89b119260e0843c35868caece422c6f141d8ef99b6e60bc2b39f502d8e21ad2d5a2c8b2494011fcbd10.png) | `postToTwitter` | ✓ | ✓ | ✓ |  |
| ![](https://nshipster.com/assets/uiactivity-postToVimeo-5d2ea2d53583c2a3b0625dd5ac776441b56d116514eed00d88840c11633f38d0c218301b5eff2304a3140aa6206ecfd352e70263ddf669395c46d2072dd2800e.png) | `postToVimeo` |  | ✓ | ✓ |  |
| ![](https://nshipster.com/assets/uiactivity-postToWeibo-2d3b16f25b84e172a6e2e3c18b55d3601b0ddaf0ece66381c958aff760d839be3ebcdda703fc74fca13666e084ee9295f1039855c5154ab0fe9b32e23d0c275f.png) | `postToWeibo` | ✓ | ✓ | ✓ |  |

## Creating a Custom UIActivity

In addition to the system-provided activities, you can create your own activities.

As an example, let’s create a custom activity that takes an image and applies a mustache to it via a web application.

| ![Jony Ive Before](https://nshipster.com/assets/jony-ive-unstache-471d24859054e549fdcdb85074d36c0afc4c277e83cd82fc29afa5d0d1ecd5fb3638a0e9aec484dfbb38a8ffc724e117355d6bd068469f81bbfe770c84a67e52.png) | ![Jony Ive After](https://nshipster.com/assets/jony-ive-mustache-c52be213feccf807b5765bec739a345b1b9e7dbae856eea5fb417e34b8537fa686de5bc08344bc53dfaa56009200fc435f2506746630caad30144ac6aaafec88.png) |
|---|---|
| Before | After |

### Defining a Custom Activity Type

First, define a new activity type constant in an extension to `UIActivity.ActivityType`, initialized with a [reverse-DNS identifier](https://en.wikipedia.org/wiki/Reverse_domain_name_notation).

```
extension UIActivity.ActivityType {
    static let mustachify =
        UIActivity.ActivityType("com.nshipster.mustachify")
}
```

### Creating a UIActivity Subclass

Next, create a subclass of `UIActivity` and override the default implementations of the `activityCategory` type property and `activityType`, `activityTitle`, and `activityImage` instance properties.

```
class MustachifyActivity: UIActivity {
    override class var activityCategory: UIActivity.Category {
        return .action
    }

    override var activityType: UIActivity.ActivityType? {
        return .mustachify
    }

    override var activityTitle: String? {
        return NSLocalizedString("Mustachify", comment: "activity title")
    }

    override var activityImage: UIImage? {
        return UIImage(named: "mustachify-icon")
    }

    …
}
```

### Determining Which Items are Actionable

Activities are responsible for determining whether they can act on a given array of items by overriding the `canPerform(withActivityItems:)` method.

Our custom activity can work if any of the items is an image, which we identify with some fancy pattern matching on a for-in loop:

```
override func canPerform(withActivityItems activityItems: [Any]) -> Bool {
    for case is UIImage in activityItems {
        return true
    }

    return false
}
```

### Preparing for Action

Once an activity has determined that it can work with the specified items, it uses the `prepare(withActivityItems:)` to get ready to perform the activity.

In the case of our custom activity, we take the PNG representation of the first image in the array of items and stores that in an instance variable:

```
var sourceImageData: Data?

override func prepare(withActivityItems activityItems: [Any]) {
    for case let image as UIImage in activityItems {
        self.sourceImageData = image.pngData()
        return
    }
}
```

### Performing the Activity

The `perform()` method is the most important part of your activity. Because processing can take some time, this is an asynchronous method. However, for lack of a completion handler, you signal that work is done by calling the `activityDidFinish(_:)` method.

Our custom activity delegates the mustachification process to a web app using a data task sent from the shared `URLSession`. If all goes well, the `mustachioedImage` property is set and `activityDidFinish(_:)` is called with `true` to indicate that the activity finished successfully. If an error occurred in the request or we can’t create an image from the provided data, we call `activityDidFinish(_:)` with `false` to indicate failure.

```
var mustachioedImage: UIImage?

override func perform() {
    let url = URL(string: "https://mustachify.app/")!
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.httpBody = self.sourceImageData

    URLSession.shared.dataTask(with: request) { (data, _, error) in
        guard error == nil else {
            self.activityDidFinish(false)
            return
        }

        if let data = data,
            let image = UIImage(data: data)
        {
            self.mustachioedImage = image
            self.activityDidFinish(true)
        } else {
            self.activityDidFinish(false)
        }
    }
}
```

### Showing the Results

The final step is to provide a view controller to be presented with the result of our activity.

The QuickLook framework provides a simple, built-in way to display images. We’ll extend our activity to adopt `QLPreviewControllerDataSource` and return an instance of `QLPreviewController`, with `self` set as the `dataSource` for our override of the`activityViewController` method.

```
import QuickLook

extension MustachifyActivity: QLPreviewControllerDataSource {
    override var activityViewController: UIViewController? {
        guard let image = self.mustachioedImage else {
            return nil
        }

        let viewController = QLPreviewController()
        viewController.dataSource = self
        return viewController
    }

    // MARK: QLPreviewControllerDataSource

    func numberOfPreviewItems(in controller: QLPreviewController) -> Int {
        return self.mustachioedImage != nil ? 1 : 0
    }

    func previewController(_ controller: QLPreviewController, previewItemAt index: Int) -> QLPreviewItem {
        return self.mustachioedImage!
    }
}
```

### Providing a Custom Activity to Users

We can use our brand new mustache activity by passing it to the `applicationActivities` parameter in the `UIActivityViewController initializer`:

```
let activityViewController =
    UIActivityViewController(activityItems: [image],
                             applicationActivities: [Mustachify()])

present(activityViewController, animated: true) {
    …
}
```

![](https://nshipster.com/assets/uiactivityviewcontroller-custom-action-b73c64e62f751e063922c437a81027f5bd0a46f432cdf8b22e1e11afa793c6bd59a7a561f7dcf2cbe9038a220f42ff34965a0beaa3a1560b8e8d9a279857c040.png)

---

There is a strong argument to be made that the long-term viability of iOS as a platform depends on sharing mechanisms like `UIActivityViewController`.

As the saying goes, _“Information wants to be free.”_ Anything that stands in the way of federation is doomed to fail.
