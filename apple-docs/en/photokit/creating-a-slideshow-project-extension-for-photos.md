---
title: Creating a Slideshow Project Extension for Photos
framework: PhotosUI
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [macOS 11.0+, Xcode 13.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photokit/creating-a-slideshow-project-extension-for-photos
source_url: 'https://developer.apple.com/documentation/photokit/creating-a-slideshow-project-extension-for-photos'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photokit/creating-a-slideshow-project-extension-for-photos.json'
content_hash: 'sha256:92deb72ddad2ede4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotoKit](../photokit.md)

# Creating a Slideshow Project Extension for Photos

<sub>Sample Code</sub>

Augment the macOS Photos app with extensions that support project creation.

## Overview

Starting in macOS 10.13, you can create Photos project extensions. This sample app shows you how to implement a slideshow extension that transitions between photos by zooming in on a region of interest (ROI) with significant meaning in an asset, for example, faces that are relevant to a user, as opposed to faces in a crowd. The app demonstrates the computation of saliency based on an ROI’s weight and quality and the process of subscribing to change notifications so your extension can respond to asset modifications.

### Configure the Sample Code Project

In the extension’s `Info.plist` file, choose the extension type by entering `slideshow` in the field at `NSExtension` \> `NSExtensionAttributes` \> [PHProjectCategory](../photosui/phprojectcategory.md). Add more categories to the information property list for your extension to appear in other categories in the Create menu.

Build and run the Photos Project Slideshow scheme in Xcode once to run the sample app and install the extension in the macOS Photos app. To use the extension, build and run the Slideshow Sample scheme in Xcode, which prompts you to open the macOS Photos app to use the extension.

From within the Photos app, access the Create categories by choosing File \> Create or right-clicking any group of assets. Under the Slideshow category, you’ll see the app extension and can create a project to run in it.

Because the project extension runs inside the Photos app, the sample emulates the grid layout of the user’s photo assets. Pressing the play button in the upper-right corner of the extension starts the slideshow.

### Customize the Focus Rectangle of the Zoom Transition

The sample code project contains custom `Animator` and `AssetModel` classes.

The `Animator` class handles transitions between photos in the slideshow. This sample’s `Animator` asks an `AssetModel` object for a rectangle to zoom in on. Photos identifies each ROI it finds as a possible ROI, and the sample uses the bounding box of the most salient one as the preferred zoom rectangle. The code defines saliency of a [PHProjectRegionOfInterest](../photosui/phprojectregionofinterest.md) as the sum of its [weight](../photosui/phprojectregionofinterest/weight.md) and [quality](../photosui/phprojectregionofinterest/quality.md) values, and then sorts the array of the photo’s regions by that value.

```swift
let sortedRois = assetProjectElement.regionsOfInterest.sorted { (roi1, roi2) -> Bool in
    return roi1.weight + roi1.quality < roi2.weight + roi2.quality
}
return sortedRois.last?.rect
```

The `weight` of an ROI represents the pervasiveness of the ROI in the project as a whole. The `quality` score represents the quality of the ROI in the individual asset, based on factors such as sharpness, visibility, and prominence in the photo. Adding these two values is a heuristic for determining the ROI’s relative importance throughout a photo project.

### Respond to Asset Changes in the Project

To respond to asset changes in the Photos Library, your app extension needs to monitor change notifications. Register for change observation as soon as the project begins or resumes. In the [PHProjectExtensionController](../photosui/phprojectextensioncontroller.md) protocol, the [- beginProjectWithExtensionContext:projectInfo:completion:](<../photosui/phprojectextensioncontroller/beginproject(with_projectinfo_completion_).md>) and [- resumeProjectWithExtensionContext:completion:](<../photosui/phprojectextensioncontroller/resumeproject(with_completion_).md>) methods provide points for your extension to begin monitoring changes.

```swift
self.projectAssets = PHAsset.fetchAssets(in: extensionContext.project, options: nil)
extensionContext.photoLibrary.register(self)
```

When the project is complete, use the [- finishProjectWithCompletionHandler:](<../photosui/phprojectextensioncontroller/finishproject(completionhandler_).md>) protocol method to unregister from change observation.

```swift
library.unregisterChangeObserver(self)
```

Whenever something changes in the Photos library, the system calls the [- photoLibraryDidChange:](<../photos/phphotolibrarychangeobserver/photolibrarydidchange(__).md>) method. When implementing this method, ask the [PHChange](../photos/phchange.md) instance for details about changes to any of the objects. When assets are added or removed, the sample project calls [- updatedProjectInfoFromProjectInfo:completion:](<../photosui/phprojectextensioncontext/updatedprojectinfo(from_completion_).md>) to get an updated [PHProjectInfo](../photosui/phprojectinfo.md) instance that you use to refresh your UI.

```swift
func photoLibraryDidChange(_ changeInstance: PHChange) {
    guard let fetchResult = projectAssets,
        let changeDetails = changeInstance.changeDetails(for: fetchResult)
        else { return }
    projectAssets = changeDetails.fetchResultAfterChanges

    guard let projectExtensionContext = projectExtensionContext else { return }
    projectExtensionContext.updatedProjectInfo(from: projectModel?.projectInfo) { (updatedProjectInfo) in
        guard let projectInfo = updatedProjectInfo else { return }
        DispatchQueue.main.async {
            self.setupProjectModel(with: projectInfo, extensionContext: projectExtensionContext)
        }
    }
}
```

### Support Copy and Paste

If your extension handles the paste action, implement the [validateMenuItem:](../objectivec/nsobject-swift.class/validatemenuitem_.md) delegate method to handle pasteboard contents.

```
func validateMenuItem(_ menuItem: NSMenuItem) -> Bool {
    var canHandlePaste = false
    if menuItem.action == #selector(paste(_:)) {
        canHandlePaste = canHandleCurrentPasteboardContent()
    }
    return canHandlePaste
}
```

## See Also

### Sample code

- [Browsing and Modifying Photo Albums](browsing-and-modifying-photo-albums.md) — Help users organize their photos into albums and browse photo collections in a grid-based layout using PhotoKit.
- [Selecting Photos and Videos in iOS](selecting-photos-and-videos-in-ios.md) — Improve the user experience of finding and selecting assets by using the Photos picker.
- [Bringing Photos picker to your SwiftUI app](bringing-photos-picker-to-your-swiftui-app.md) — Select media assets by using a Photos picker view that SwiftUI provides.
- [Implementing an inline Photos picker](implementing-an-inline-photos-picker.md) — Embed a system-provided, half-height Photos picker into your app’s view.

## Download

- [CreatingASlideshowProjectExtensionForPhotos.zip](https://docs-assets.developer.apple.com/published/47b788a396e5/CreatingASlideshowProjectExtensionForPhotos.zip)
