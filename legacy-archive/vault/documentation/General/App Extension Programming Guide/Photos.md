---
title: App Extension Programming Guide
apple_id: TP40014214
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: General
technology: null
published: '2017-10-19'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/Photos.html
archived_at: '2026-07-15T07:34:01.651240Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [App Extension Programming Guide](index.md)



## Photo Editing

A Photo Editing extension lets users edit a photo or video within the Photos app. After users confirm the changes they make in a Photo Editing extension, the adjusted content is available in Photos. Photos always keeps the original version of the content, too, so that users can revert the changes they make in an extension.

> [!NOTE]
> 

### Understand How a Photo Editing Extension Works with Photos

To support a consistent editing experience, Photos keeps multiple versions of each media asset’s image or video data, in addition to adjustment data, which describes past edits made to the asset. For each asset, Photos stores the original version, the current version (which includes the most recent adjustments), and the set of adjustments that were applied to the original version to create the current version.

When a user chooses a Photo Editing extension, Photos asks the extension if it can read the adjustment data. If the app extension supports the adjustment data, Photos provides the original version of the asset as input to the editing session. After the extension reads the adjustment data and reconstructs the past edits, it can allow users to alter or revert past edits or add new edits. For example, if the adjustment data describes filters applied to a photo, the extension reapplies those filters to the original asset and can let users change filter parameters, add new filters, or remove filters.

If the extension doesn’t support an asset’s adjustment data, Photos provides the current version of the asset as input to the editing session. Because the current version contains the rendered output of all past edits, the extension can let users apply new edits to the asset but not alter or revert past edits.

> [!IMPORTANT]
> 

When a user finishes using a Photo Editing extension, the extension returns the edited asset and the adjustment data.

### Use the Xcode Photo Editing Template

The Xcode Photo Editing template provides default header and implementation files for the principal view controller class (called `PhotoEditingViewController`), an `Info.plist` file, and an interface file (that is, a storyboard file).

> [!IMPORTANT]
> 

By default, the Photo Editing template supplies the following `Info.plist` keys and values:

1. `<key>NSExtension</key>`
2. `<dict>`
3. `<key>NSExtensionAttributes</key>`
4. `<dict>`
5. `<key>PHSupportedMediaTypes</key>`
6. `<array>`
7. `<string>Image</string>`
8. `</array>`
9. `</dict>`
10. `<key>NSExtensionMainStoryboard</key>`
11. `<string>MainInterface</string>`
12. `<key>NSExtensionPointIdentifier</key>`
13. `<string>com.apple.photo-editing</string>`
14. `</dict>`

In particular, make sure that the `PHSupportedMediaTypes` array specifies the types of media assets your app extension can edit. The default value is `Image`, but you can also use `Video` and `LivePhoto`.

### Design the UI

> [!IMPORTANT]
> 

In iOS, your app extension’s view must support a full-screen presentation on devices of different sizes, as well as Slide Over and Split View presentations on iPad. In macOS, your app extension’s view occupies the entire Photos window, which is resizable and supports full-screen presentation.

The Photos app displays a Photo Editing extension with a navigation bar in iOS or a combined title bar and toolbar in macOS. Don’t create a navigation-based UI, and avoid stacking additional top-oriented toolbars in your app extension.

Photos automatically displays your app extension’s view so that it occupies the full height of the screen (iOS) or window (macOS), including the area behind the navigation bar or title bar. If you want your content view to appear below the bar, and not behind it, use the view’s top layout guide appropriately.

It’s best when a Photo Editing extension lets users preview the results of their edits. Giving users a preview while they’re still using your app extension means that they can get the effect they want without repeatedly exiting and reentering the extension.

Because users are likely to spend time editing a photo or movie in your app extension, you don’t want them to lose their work if they accidentally choose Cancel. To improve the user experience, be sure to implement the [shouldShowCancelConfirmation](https://developer.apple.com/documentation/photokit/phcontenteditingcontroller/1501734-shouldshowcancelconfirmation) method in your view controller, returning `YES``true` if there are unsaved changes. When this method returns `YES``true`, Photos displays confirmation UI so that users can confirm if they really want to cancel their changes.

### Implement Your Extension

Users get access to Photo Editing extensions in the Photos app. When a user chooses your app extension, display a view that provides a custom editing interface. To present this view, use a view controller that adopts the [PHContentEditingController](https://developer.apple.com/documentation/photokit/phcontenteditingcontroller) protocol.

When a user chooses your app extension, Photos provides the asset being edited to your extension’s view controller in the form of a [PHContentEditingInput](https://developer.apple.com/documentation/photokit/phcontenteditinginput) object. For photo and video assets, you use this object to access the asset’s image or video data to perform your editing. When the user chooses to end editing, Photos asks your app extension’s view controller for a [PHContentEditingOutput](https://developer.apple.com/documentation/photokit/phcontenteditingoutput) object, which you use to provide the edited asset data.

> [!NOTE]
> 

When your app extension works with Live Photo assets, it doesn’t access the asset’s underlying image and video resources directly. Instead, you create a [PHLivePhotoEditingContext](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext) object from the provided content editing input, and use the methods that class provides to perform and preview edits.

If your app extension edits video assets, see the [AVVideoComposition](https://developer.apple.com/documentation/avfoundation/avvideocomposition) [videoCompositionWithAsset:applyingCIFiltersWithHandler:](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1389556-init) method for an easy way to apply image-processing filters.

For example code illustrating how to edit all asset media types, download the _[Sample Photo Editing Extension](../../../samplecode/Sample%20Photo%20Editing%20Extension/Sample%20Photo%20Editing%20Extension.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dknzw)_ sample code project.

### Handling Memory Constraints

Because a Photo Editing extension often needs to work with large high-resolution images and videos, the extension is likely to experience memory pressures when running on a device. It’s recommended that you examine your existing image-processing code and make sure that it performs to a high standard before you use it in your app extension.

### Testing a Photo Editing Extension

Avoid making assumptions about the media formats that your app extension may receive. Be sure to test your filtering and other image-processing code with a wide range of media formats; don’t just test with content from the device camera.

To learn about debugging app extensions in general, see [Debug, Profile, and Test Your App Extension](ExtensionCreation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjufvbuqnjnknltq).

[Finder Sync](Finder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjufvbuqmjvfvjvomi)

[Share](Share.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjufvbuqmjsfvjvomi)
