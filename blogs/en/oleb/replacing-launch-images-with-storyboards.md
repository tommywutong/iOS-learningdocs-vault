---
title: Replacing Launch Images With Storyboards
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/08/replacing-launch-images-with-storyboards/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:0094b6b05b63ed2c'
translated: false
---

> 原文：[Replacing Launch Images With Storyboards](https://oleb.net/blog/2014/08/replacing-launch-images-with-storyboards/)　·　Ole Begemann

# Replacing Launch Images With Storyboards

![The new Launch Screen File option in Xcode 6](https://oleb.net/media/xcode6-launch-screen-file.png)

<sub>The new _Launch Screen File_ option in Xcode 6.</sub>

Earlier this week, tweets [from Nick Lockwood](https://twitter.com/nicklockwood/status/503848057017221120) and [James Thomson](https://twitter.com/jamesthomson/status/503829990245695488) alerted me to an as yet undocumented new feature in the iOS 8 SDK: you can now use a storyboard scene in place of your app’s launch images.

# Launch Images

iOS uses [launch images](https://developer.apple.com/library/ios/documentation/userexperience/conceptual/mobilehig/LaunchImages.html) to give users the impression that apps launch instantly. While an app is busy loading its initial screen, the OS displays a static image provided by the app developer. For best effect, the launch image should resemble the static parts of the app’s user interface.

> Design a launch image that is identical to the first screen of the app, except for: [1] Text. … [2] UI elements that might change. … If you think that following these guidelines will result in a plain, boring launch image, you’re right. Remember, the launch image doesn’t provide you with an opportunity for artistic expression. It’s solely intended to enhance the user’s perception of your app as quick to launch and immediately ready for use.
> 
> — [iOS Human Interface Guidelines](https://developer.apple.com/library/ios/documentation/userexperience/conceptual/mobilehig/LaunchImages.html)

For iOS 7 and earlier, app developers had to provide separate launch images for all screen sizes, resolutions and orientations their app supported. For universal apps, up to seven images were required: retina and non-retina versions for 3.5-inch iPhones in portrait and for iPads in portrait and landscape; and another retina image for 4-inch iPhones (the iPhone requires no landscape version because apps are always launched from the portrait-only Home screen).

Creating these images is a nuisance. And the new screen sizes that are likely coming next month will make the process even more annoying.

# An Interface Builder-Based Launch Screen

In Xcode 6, there is another option. You can specify a storyboard whose initial view controller will then be used as the app’s launch screen. This is how:

1. Create a blank storyboard file named `LaunchScreen.storyboard`.
2. Go to your target settings and, on the General tab, select the storyboard as your _Launch Screen File_. Xcode will add a corresponding `UILaunchStoryboardName` key to your app’s `Info.plist`. When this key is present, Xcode will prioritize it over any launch images you might have set.
3. Add a view controller scene to the storyboard. Add some subviews to the scene and position them with constraints. When you launch the app on a device, the OS should use the scene as the launch screen.

## One Storyboard for All Screen Sizes

You can use the new adaptive UI features in Interface Builder to fit your layout to different screen sizes. If your scene requires screen-size-specific images, use asset catalogs to define different images per size class. Note that you can not only adjust constraints for different size classes, you can also remove selected views from a specific size class entirely by deselecting the Installed check box. See [WWDC session 411](https://asciiwwdc.com/2014/sessions/411) for details.

## Also Works with NIBs

Despite the name of the `UILaunchStoryboardName` key, this also seems to work with NIB/XIB files containing a single view. When you open such a XIB file in Xcode, the File Inspector displays a check box named _Use as Launch Screen_, which is not there for storyboards. In my tests with Xcode 6 beta 6, checking it seemed to have no effect, however. You still have to set the _Launch Screen File_ in your target settings.

![The Use as Launch Screen check box for NIB files in Interface Builder](https://oleb.net/media/xcode6-nib-file-use-as-launch-screen.png)

<sub>The _Use as Launch Screen_ check box for NIB files in Interface Builder seems to have no effect.</sub>

## Caveats

Note that the launch screen is is not a fully customizable view controller. You cannot specify a custom class name in the storyboard and expect the system to give you the option to execute code at this stage by calling `viewDidLoad`. Remember, the app hasn’t launched yet.

The storyboard is not limited to a single view controller scene, however. You can set up a more complex scene, for example a navigation controller and an embedded content view controller.

The launch screen storyboard is not localizable at the moment. Neither using a separate `.strings` file under Base Internationalization nor a localized copy of the storyboard worked in my tests. I hope Apple will add this feature in a future version.

Ideally, your launch screen would use the same storyboard scene you have already built for your app’s initial screen. That way, you would only have to design it once. Since the storyboard can contain an arbitrary number of other scenes, it sounds possible in theory to just use your app’s main storyboard as the launch screen file. The OS would then load and display the initial view controller and seamlessly switch over to the fully initialized instance of the same view controller once the launch is complete. In my tests, this did not work if the scene used as the launch screen contained any outlets (which your app’s initial screen most likely does). As soon as I connected a control from the launch scene to an outlet in the view controller, the OS would simply skip the launch screen entirely. I’m not really sure why.

In practice, there are probably many reasons why you would not want to use your initial screen as your launch scene, especially as long as localization is not supported.

~~Remember, the purpose of the launch screen is make the app launch seem faster than it is. Take care not to overdo your launch scene with too many subviews and images. If it takes the OS a significant amount of time to load and compose the scene, it would defeat the entire purpose of the launch screen. I have not made any performance comparisons of launch screens vs. launch images. The old method with static images should still be faster, but I have no idea if the difference is large enough to matter, especially on modern devices.~~

**Update September 1, 2014:** Morten Bek Ditlevsen pointed out to me that Apple actually did mention the feature in the [WWDC Platforms State of the Union session](https://asciiwwdc.com/2014/sessions/102):

> With iOS 8, you can now provide an Interface Builder document and, at runtime, have the OS generate all of the necessary Launch Images for you.

Assuming these generated images are cached (and why wouldn’t they?), using storyboards [should have no impact on performance](https://twitter.com/joshshaffer/status/505114971315781632).
