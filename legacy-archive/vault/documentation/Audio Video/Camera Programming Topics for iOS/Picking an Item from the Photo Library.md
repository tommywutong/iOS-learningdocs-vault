---
title: Camera Programming Topics for iOS
apple_id: TP40010400
resource_type: Guide
platform: tvOS|iOS
topic: Audio, Video, & Visual Effects
technology: UIKit
published: '2012-07-17'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/CameraAndPhotoLib_TopicsForIOS/Articles/PickinganItemfromthePhotoLibrary.html
archived_at: '2026-07-15T05:21:02.025324Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Camera Programming Topics for iOS](About%20the%20Camera%20and%20Photo%20Library.md)


[Next](Document%20Revision%20History.md)[Previous](Taking%20Pictures%20and%20Movies.md)

# Picking an Item from the Photo Library

In addition to using a [UIImagePickerController](https://developer.apple.com/documentation/uikit/uiimagepickercontroller) instance to capture new pictures and movies, you can use it to present a media browser that lets a user choose an item from their saved photo albums. The steps you take are similar to those for capturing media, as described in [Taking Pictures and Movies](Taking%20Pictures%20and%20Movies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydimbwfvjvomi). The differences are:

- Instead of using the _camera_ as the media source, you use the Camera Roll album or Saved Photos album, or the entire photo library.
- Instead of capturing new media and (typically) saving it to an album, you let the user pick previously-saved media. You can then use the picked media in your app, perhaps displaying it full screen.

This chapter explains how to use an image picker [controller](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11) and [delegate](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) for browsing and choosing saved pictures and movies. If the standard media browsing UI does not suit your needs, you can create a fully custom solution with UIKit and the Assets Library framework. See _[Assets Library Framework Reference](https://developer.apple.com/documentation/assetslibrary)_.

Most iOS devices have a photo library. For such devices, whether or not the device has a camera, you can use an image picker controller to present a media browser. As for presenting a camera interface, you must have implemented a delegate object to respond to the user’s interaction with the browsing interface. You can then instantiate and configure an image picker controller by specifying the following options:

- _Source type_ To configure the picker for browsing saved media as opposed to capturing a new picture or movie, set its [sourceType](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619167-sourcetype) property to one of the saved photo sources:

  - Use [UIImagePickerControllerSourceTypePhotoLibrary](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/sourcetype/photolibrary) to present a browser that provides access to all the photo albums on the device, including the Camera Roll album on devices that have a camera.
  - Use [UIImagePickerControllerSourceTypeSavedPhotosAlbum](https://developer.apple.com/documentation/uikit/uiimagepickercontrollersourcetype/uiimagepickercontrollersourcetypesavedphotosalbum) to present a browser that restricts access to the Camera Roll album on devices that have a camera, or to the Saved Photos album on devices that don’t.
- _Media types_ To specify whether the image picker controller displays saved movies, still images, or both, set the [mediaTypes](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619173-mediatypes) property to an array containing identifiers for the desired types. The valid values for elements of the array are [kUTTypeImage](https://developer.apple.com/documentation/coreservices/kuttypeimage) and [kUTTypeMovie](https://developer.apple.com/documentation/coreservices/kuttypemovie).

  However, before setting this property, check which media types are available by calling the [availableMediaTypesForSourceType:](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619169-availablemediatypesforsourcetype) class method. If you set the [mediaTypes](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619173-mediatypes) property to an empty array, or to an array in which none of the media types is available for the current source, the system throws an exception.
- _Editing controls_ To specify whether or not the media picker offers the user controls for moving and scaling the picked saved image, or for trimming the picked saved movie, set the [allowsEditing](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619137-allowsediting) property to `YES` (to provide editing controls) or to `NO`.

  When using built-in editing controls, the image picker controller enforces certain options. For still images, the picker enforces a square cropping as well as a maximum pixel dimension. For movies, the picker enforces a maximum movie length and resolution. If you want to let the user edit full-size media, or specify custom cropping, you must provide your own editing UI.
- _Delegate object_ Finally, assign your delegate object to the image picker controller’s [delegate](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619145-delegate) property.

Listing 1 verifies the prerequisites are satisfied by way of its method signature and a conditional test, and goes on to instantiate, configure, and asynchronously present the media browser user interface full screen.

__Listing 1__  Presenting the media browser interface full screen on iPhone or iPod touch

```objc
- (BOOL) startMediaBrowserFromViewController: (UIViewController*) controller
               usingDelegate: (id <UIImagePickerControllerDelegate,
                                   UINavigationControllerDelegate>) delegate {

    if (([UIImagePickerController isSourceTypeAvailable:
                 UIImagePickerControllerSourceTypeSavedPhotosAlbum] == NO)
            || (delegate == nil)
            || (controller == nil))
        return NO;

    UIImagePickerController *mediaUI = [[UIImagePickerController alloc] init];
    mediaUI.sourceType = UIImagePickerControllerSourceTypeSavedPhotosAlbum;

    // Displays saved pictures and movies, if both are available, from the
    // Camera Roll album.
    mediaUI.mediaTypes =
        [UIImagePickerController availableMediaTypesForSourceType:
            UIImagePickerControllerSourceTypeSavedPhotosAlbum];

    // Hides the controls for moving & scaling pictures, or for
    // trimming movies. To instead show the controls, use YES.
    mediaUI.allowsEditing = NO;

    mediaUI.delegate = delegate;

    [controller presentModalViewController: mediaUI animated: YES];
    return YES;
}
```

On iPad, you must present the browser interface using a popover as described in [initWithContentViewController:](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624669-initwithcontentviewcontroller) and Presenting and Dismissing the Popover in _[UIPopoverController Class Reference](https://developer.apple.com/documentation/uikit/uipopovercontroller)_. If, on iPad, you attempt to present the browser interface modally (full-screen), the system raises an exception.

[Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydimbyfvjvomq) displays both still images and movies in the picker, if both are present in the Camera Roll album. To present a picker that displays only movies, for example, instead set the [mediaTypes](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619173-mediatypes) property as follows:

```
mediaUI.mediaTypes = [[NSArray alloc] initWithObjects: (NSString *) kUTTypeMovie, nil];
```

Using this option, you must first ensure that the device is capable of displaying movies. Do this by calling the [availableMediaTypesForSourceType:](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619169-availablemediatypesforsourcetype) class method. For a picker that displays only still images, replace the [kUTTypeMovie](https://developer.apple.com/documentation/coreservices/kuttypemovie) identifier here with [kUTTypeImage](https://developer.apple.com/documentation/coreservices/kuttypeimage), or rely on the default value of the `mediaTypes` property, which is `kUTTypeImage`.

The `startMediaBrowserFromViewController:usingDelegate:` example method from Listing 1 is designed to be invoked by an action method such as this:

```objc
- (IBAction) showSavedMediaBrowser {
    [self startMediaBrowserFromViewController: self
                                    usingDelegate: self];
}
```

Notice, as specified in the method signature in [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydimbyfvjvomq), that the delegate object must conform to the [UIImagePickerControllerDelegate](https://developer.apple.com/documentation/uikit/uiimagepickercontrollerdelegate) and [UINavigationControllerDelegate](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate)[protocols](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45).

When presented with the standard media browser display for an image picker controller, the user sees a scrolling grid of thumbnails representing the contents of the Camera Roll album. The user options are to cancel the operation or to tap on a thumbnail. If the user taps Cancel, your delegate implementation should simply dismiss the picker—just as you do when presenting the camera interface. Indeed, your imagePickerControllerDidCancel: implementation for an image picker controller is identical whether presenting a camera or a media browser interface. See [Listing 2](Taking%20Pictures%20and%20Movies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydimbwfvjvomq).

If the user taps a thumbnail, what happens next depends on whether the thumbnail represents a still image or a movie.

- For still images, tapping the thumbnail immediately calls the delegate with information about the image.
- For movies, tapping the thumbnail displays a preview with a scroller plus three buttons: play, Cancel, and Choose. If the user taps Choose, the system calls the delegate with information about the movie. If the user taps Cancel, the preview automatically dismisses and returns the user to the media browser.

To respond to the user tapping Choose in an image picker controller configured as a media browser, use code similar to that shown in LISTING.

__Listing 2__  Delegate method for picked media

```objc
- (void) imagePickerController: (UIImagePickerController *) picker
            didFinishPickingMediaWithInfo: (NSDictionary *) info {

    NSString *mediaType = [info objectForKey: UIImagePickerControllerMediaType];
    UIImage *originalImage, *editedImage, *imageToUse;

    // Handle a still image picked from a photo album
    if (CFStringCompare ((CFStringRef) mediaType, kUTTypeImage, 0)
            == kCFCompareEqualTo) {

        editedImage = (UIImage *) [info objectForKey:
                    UIImagePickerControllerEditedImage];
        originalImage = (UIImage *) [info objectForKey:
                    UIImagePickerControllerOriginalImage];

        if (editedImage) {
            imageToUse = editedImage;
        } else {
            imageToUse = originalImage;
        }
        // Do something with imageToUse
    }

    // Handle a movied picked from a photo album
    if (CFStringCompare ((CFStringRef) mediaType, kUTTypeMovie, 0)
            == kCFCompareEqualTo) {

        NSString *moviePath = [[info objectForKey:
                    UIImagePickerControllerMediaURL] path];

        // Do something with the picked movie available at moviePath
    }

    [[picker parentViewController] dismissModalViewControllerAnimated: YES];
    [picker release];
}
```

If image editing is enabled and the user successfully accepts a newly captured picture, the _info_ parameter of the [imagePickerController:didFinishPickingMediaWithInfo:](https://developer.apple.com/documentation/uikit/uiimagepickercontrollerdelegate/1619126-imagepickercontroller) method contains a dictionary that includes the edited image. Treat this image as the selected image, as done in Listing 2. If you want to store the original image, you can get it from the dictionary, also as shown in the code listing.

[Next](Document%20Revision%20History.md)[Previous](Taking%20Pictures%20and%20Movies.md)

