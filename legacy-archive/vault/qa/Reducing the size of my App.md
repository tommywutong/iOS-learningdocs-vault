---
title: Reducing the size of my App
apple_id: DTS40014195
resource_type: QA
platform: watchOS|tvOS|iOS
topic: General
technology: null
published: '2017-04-25'
source_url: https://developer.apple.com/library/archive/qa/qa1795/_index.html
archived_at: '2026-07-27T06:57:05.372001Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1795

# Reducing the size of my App

## Q:  How can I make my app smaller, so that it is faster to download and install?

A: This document is a collection of techniques to reduce the size of your app when it is downloaded and installed for the first time. See "[Reducing Download Size for iOS App Updates](https://developer.apple.com/library/ios/qa/qa1779/)" for information specific to app updates — they work differently.

## Measure Your App

Before trying any optimizations, you should measure. Some of the techniques in this document are tradeoffs with downsides that must be considered. You must measure their impact to be sure you're making the right tradeoff. Without measuring, you can't know what kind of change you're making.

The app distribution process produces a number of different artifacts, each with its own purpose and size. It's important to understand what each artifact represents and which artifacts to use when measuring your app's size.

- An __app bundle__ is the `.app` bundle containing all of the binaries in your app, plus all of your app's resources, such as images. This bundle contains everything needed for your app to run on every supported device. For the purposes of this document, an app bundle only refers to the `.app` produced by archiving your app.
- An __App Store submission .ipa__ is created from an Xcode archive when uploading to the App Store or by exporting the archive for iOS App Store Deployment. This `.ipa` is a compressed directory containing the app bundle and additional resources needed for App Store services, such as `.dSYM` files for crash reporting and asset packs for On Demand Resources.
- A __universal .ipa__ is a compressed app bundle that contains all of the resources to run the app on any device. Bitcode has been recompiled, and additional resources needed by the App Store, such as `.dSYM` files and On Demand Resources, are removed. For App Store apps, this `.ipa` is downloaded to devices running iOS 8 or earlier.
- A __thinned .ipa__ is a compressed app bundle that contains only the resources needed to run the app on a specific device. Bitcode has been recompiled, and additional resources needed by the App Store, such as `.dSYM` files and On Demand Resources, are removed. For App Store apps, this `.ipa` is downloaded to devices running iOS 9 or later.
- A __universal app bundle__ is the decompressed universal `.ipa`. The installation process decompresses the universal `.ipa` and installs the universal app bundle.
- A __thinned app bundle__ is the decompressed thinned `.ipa`. The installation process decompresses the thinned `.ipa` and installs the thinned app bundle.

### Getting an App Size Report

Xcode provides reporting tools to help you understand the size of your app. To generate the size report:

1. [Archive your app](http://help.apple.com/xcode/mac/current/#/devf37a1db04).
2. [Export your archive for testing outside the store](http://help.apple.com/xcode/mac/current/#/dev23ea8b877).
3. Select “Export for specific devices” and choose “All compatible device variants” from the pop-up menu.
4. Select "Rebuild from bitcode."

In the output folder, you will find `App Thinning Size Report.txt`, which breaks down the compressed and uncompressed file sizes, plus the size of any On Demand Resources, for each device type. An example of this file is in Listing 1.

You can also [use xcodebuild from the command line to export an Ad-Hoc archive](https://developer.apple.com/library/ios/technotes/tn2339/_index.html) with options to create the thinned `.ipa` files and get the app size report.

__Note:__ This report does not factor in encryption for App Store apps. See [iOS App Store Specific Considerations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimjzguwugsbrfvavauc7knke6usfl5bu6tstjfcekusbkreu6tst) for more information.

__Listing 1__  Sample App Thinning Size Report for the Lister sample code project

```
App Thinning Size Report for All Variants of Lister

Variant: Lister-iPad 2-etc.ipa
Supported devices: iPad (3rd generation), iPad (4th generation), iPad 2, iPad mini, iPhone 4S, iPhone 5, iPhone 5c, and iPod touch
App + On Demand Resources size: 3.3 MB compressed, 9.6 MB uncompressed
App size: 3.3 MB compressed, 9.6 MB uncompressed
On Demand Resources size: Zero KB compressed, Zero KB uncompressed

Variant: Lister-iPod touch (6th generation)-etc.ipa
Supported devices: iPad Air, iPad Air 2, iPad Pro (12.9-inch), iPad Pro (9.7-inch), iPad mini 2, iPad mini 3, iPad mini 4, iPhone 5s, iPhone 6, iPhone 6 Plus, iPhone 6s, iPhone 6s Plus, iPhone SE, and iPod touch (6th generation)
App + On Demand Resources size: 3.2 MB compressed, 9.6 MB uncompressed
App size: 3.2 MB compressed, 9.6 MB uncompressed
On Demand Resources size: Zero KB compressed, Zero KB uncompressed

Variant: Lister.ipa
Supported devices: Universal
App + On Demand Resources size: 5.1 MB compressed, 16.6 MB uncompressed
App size: 5.1 MB compressed, 16.6 MB uncompressed
On Demand Resources size: Zero KB compressed, Zero KB uncompressed
```

### iOS App Store Specific Considerations

The App Thinning Size Report is an estimate of the final size of your app on the App Store. As part of the App Store distribution process, all of the binaries inside the App Store submission `.ipa` are encrypted when the App Store produces the universal `.ipa` and the thinned `.ipa` files. The encryption does not change the size of the binary, but the encrypted binary will have different compression characteristics, resulting in `.ipa` files from the App Store being larger than the size listed in the App Thinning Size Report.

__Note:__ The size change above is not unique to App Store's encryption algorithm, but is instead one of the normal consequences of any strong encryption algorithm. By design, strong encryption algorithms produce output that cannot be efficiently compressed.

The size of your app on the App Store is available in the [App File Size information provided by iTunes Connect](http://help.apple.com/itunes-connect/developer/#/dev3b56ce97c). If you are concerned about your app being over the cellular download limit, your build on iTunes Connect will indicate if the build is over the cellular download limit.

__Note:__ Apps distributed for testing with TestFlight contain additional data, adding to the size of the app reported by iTunes Connect. This data will not be present after the app is released to the App Store.

Until the app is approved by App Review, the sizes displayed on iTunes Connect are only estimates of what the final App Store size will be. After the app has been approved, the sizes will be updated to reflect the final values.

### Inspecting an .ipa File

If the universal `.ipa` or any of the thinned `.ipa` files are larger than expected, the next step is to look at the thinned app bundle and see what files inside it are taking up the most space. The `.ipa` files are just a `.zip` archive that has a particular structure when unzipped.

Simply change the extension of an `.ipa` file to `.zip`, then open it with Finder to decompress it. Right-click on the unzipped `.app` bundle and choose "Show Package Contents" to see the resources inside. This can give you an idea of what is using the most space.

You can examine the compressed size of each item in the `.ipa` by opening Terminal and executing the following command:

`unzip -lv /path/to/your/thinned_app.ipa`

__Important:__ App Store submission `.ipa` files are not representative of the actual size of an app on a device, and should not be used for this examination. Only measure using `.ipa` files produced by following the steps in [Getting an App Size Report](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimjzguwugsbrfvdukvc7knevurk7kjcvat2skq).

The size column has the compressed size of each file within your `.ipa` file. You should evaluate this size as you work to reduce the size of resources in your app. You may reduce the size of a resource by a lot, but after producing an `.ipa` file, you may discover the compressed size of that resource has not changed as dramatically. The most effective technique for reducing the size of an `.ipa` file is to remove unnecessary resources.

[Back to Top](#)

## Optimization Tips

### Analyze Your Code

#### Keep Data out of Code

Moving any resources, such as long strings, or tables, out of code and into external files will make the final download smaller, because external files compress more efficiently than when the data is compiled into a binary. See [iOS App Store Specific Considerations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimjzguwugsbrfvavauc7knke6usfl5bu6tstjfcekusbkreu6tst) for full technical background.

#### Compiler Options

Setting the `Optimization Level` build setting to `Fastest, Smallest [-Os]` can dramatically lower the size of your compiled binary. This setting is the default for the "Release" configuration in Xcode projects.

__Note:__ Only enable `Optimization Level` for your Release builds.

If you have a watchOS app written in Swift, use the procedure described in [Inspecting an .ipa File](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimjzguwugsbrfvevaqk7kvhfuskq) to verify that only one copy of `libSwiftCore.dylib` is present in the subdirectories of the `Watch` folder. If you see multiple copies, ensure the `Always Embed Swift Standard Libraries` build setting is set to `Yes` for the watchOS app target, and set to `No` for the watchOS app extension target.

### Analyze Your Assets

#### Sanity Check Your App

Use the procedure described in [Inspecting an .ipa File](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimjzguwugsbrfvevaqk7kvhfuskq) to check what is actually shipping in your app bundle. Apps often contain extra files, like headers or a readme, that are never used.

#### Leverage Asset Catalogs

[Use asset catalogs](https://help.apple.com/xcode/mac/current/index.html?localePath=en.lproj#/dev10510b1f7) for images, textures, and data assets, tagging each asset with relevant metadata to indicate which devices the asset is for. Asset Catalogs help maximize the size reduction provided by App Slicing, which can be significant for apps with assets not needed by every device. For an introduction to App Slicing, watch the [App Thinning WWDC Session](https://developer.apple.com/videos/wwdc/2015/?id=404).

Asset catalogs have configurable levels of compression for each asset type. In particular, apps using wide color images or using textures with Metal should consider the ASTC compression options. For more information on these compression options, watch the WWDC session [Working With Wide Color](https://developer.apple.com/videos/play/wwdc2016/712/).

Asset catalogs also provide the ability to [define a resizable center area](http://help.apple.com/xcode/mac/current/#/deve65bd8d0d) of an image with optional end caps, reducing the overall size of an image.

#### Use 8-bit Images Where Possible

Using an 8-bit PNG instead of a 32-bit PNG can decrease your image size by 4x, so use them whenever you can. However, 8-bit images can only have 256 different colors and photographs or other detailed color images might not be suitable in an 8-bit format. Greyscale images are a perfect candidate for 8-bit images, and images with a small set of colors may work well in an 8-bit format.

#### Use Compression for Images Where Possible

For 32 bit images, using Adobe Photoshop’s “Save For Web” feature can reduce the size of JPEG and PNG images considerably. By default, `.png` images not in an asset catalog will be [compressed with pngcrush](https://developer.apple.com/library/ios/qa/qa1681/) by Xcode automatically when the app is built.

#### Compress Audio

See the [Audio Development for Games](https://developer.apple.com/videos/wwdc/2011/?id=404) WWDC session for information on handling audio efficiently. As a general rule, you should compress audio using AAC or MP3, and experiment with a reduced bitrate. Quite often a 44.1khz sample is overkill and a lower-bitrate clip won't have a perceptible drop in quality.

### Analyze Your Architecture

The following optimization tips may require you to alter your app's architecture in order to implement the tip.

#### Adopt On-Demand Resources

Analyze all of the assets your app uses, and determine which resources are used infrequently or only by some users, and group these resources in to asset packs that are delivered with On Demand Resources. See the [On-Demand Resources Guide](https://developer.apple.com/library/ios/documentation/FileManagement/Conceptual/On_Demand_Resources_Guide/index.html) for more information.

#### Adopt Background Downloads

Apps with assets in the app bundle that could be downloaded from a web service instead should move those assets to the web service and [download them with a background session provided by NSURLSession](https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/URLLoadingSystem/Articles/UsingNSURLSession.html).

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-04-25 | Updated links |
| 2017-01-20 | Added instructions for getting an app thinning size report and expanded the optimization suggestions |
| 2015-09-29 | Updated section about encryption |
| 2015-09-08 | Updated to include App Thinning. |
| 2014-03-06 | New document that explains techniques for reducing the size of your app |
