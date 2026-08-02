---
title: Camera Programming Topics for iOS
apple_id: TP40010400
resource_type: Guide
platform: tvOS|iOS
topic: Audio, Video, & Visual Effects
technology: UIKit
published: '2012-07-17'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/CameraAndPhotoLib_TopicsForIOS/Articles/TakingPicturesAndMovies.html
archived_at: '2026-07-15T05:21:02.037051Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Camera Programming Topics for iOS](About%20the%20Camera%20and%20Photo%20Library.md)


[Next](Picking%20an%20Item%20from%20the%20Photo%20Library.md)[Previous](About%20the%20Camera%20and%20Photo%20Library.md)

# Taking Pictures and Movies

Taking a picture or movie with an image picker controller is a three part process that proceeds as an interplay between your code and the system:

1. You instantiate and modally present a camera interface—an instance of the `UIImagePickerController` class.
2. The system manages the camera interface and the user’s interaction with it. In typical use, the user either takes a picture or movie, or cancels the operation.
3. The system invokes your image picker controller delegate object’s methods, which in turn handle the results of the user’s interaction—for example, by saving a new picture to the Camera Roll album. The delegate is also responsible for dismissing the camera interface.

A default image picker controller includes a variety of features, as shown in Figure 1.

__Figure 1__  An image picker controller

!

This chapter explains how to use a default image picker [controller](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11) and [delegate](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) for taking pictures and movies. (Movie recording is available starting in iOS 3.0 on supported devices).

To learn how to instead use the AV Foundation framework for fully-customized media capture, see [Media Capture and Access to Camera](../AVFoundation%20Programming%20Guide/About%20AVFoundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcobyfvbuqmjnknltcma) in _[AVFoundation Programming Guide](../AVFoundation%20Programming%20Guide/About%20AVFoundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcoby)_.

To present a camera interface, you must first ensure that three things are in place:

1. The device your app is running on must have a camera.

   If taking pictures or movies is essential to your app, specify that by configuring the `UIRequiredDeviceCapabilities` key in your app’s `Info.plist` [property list](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44) file. See [UIRequiredDeviceCapabilities](../../General/Information%20Property%20List%20Key%20Reference/iOS%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjsfvjvomy) in _[Information Property List Key Reference](../../General/Information%20Property%20List%20Key%20Reference/About%20Info.plist%20Keys%20and%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbx)_ for the various camera characteristics you can specify as required.

   If capturing media is incidental to your app—that is, if your app remains useful even if the device doesn’t have a camera—then your code should follow an alternate path when running on a device without a camera.
2. The device’s camera must be available for you to use, which you can test by way of the [isSourceTypeAvailable:](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619144-issourcetypeavailable) [class method](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassMethod.html#//apple_ref/doc/uid/TP40008195-CH8) of the `UIImagePickerController` class.
3. You must have implemented a delegate object to respond to the user’s interaction with the image picker controller. (See [Implementing a Delegate for the Camera Interface](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydimbwfvjvonq).)

With those prerequisites satisfied, [create](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39) and then configure an image picker controller by specifying the following options:

- _Source type_ To configure the picker for media capture as opposed to browsing saved media, set its [sourceType](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619167-sourcetype) property to [UIImagePickerControllerSourceTypeCamera](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/sourcetype/camera).
- _Media types_ To specify whether the user can take still images, movies, or both, set the [mediaTypes](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619173-mediatypes) property to an array containing identifiers for the desired types. The valid values for elements of the array are [kUTTypeImage](https://developer.apple.com/documentation/coreservices/kuttypeimage) and [kUTTypeMovie](https://developer.apple.com/documentation/coreservices/kuttypemovie).

  However, before setting this property, check which media types are available by calling the [availableMediaTypesForSourceType:](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619169-availablemediatypesforsourcetype) class method. If you set the [mediaTypes](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619173-mediatypes) property to an empty array, or to an array in which none of the media types is available for the current source, the system throws an exception.
- _Editing controls_ To specify whether the camera interface should offer the user controls for moving and scaling the captured picture, or for trimming the captured movie, set the [allowsEditing](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619137-allowsediting) property to `YES` (to provide editing controls) or to `NO`.

  When using built-in editing controls, the image picker controller enforces certain options. For still images, the picker enforces a square cropping as well as a maximum pixel dimension. For movies, the picker enforces a maximum movie length and resolution. If you want to let the user edit full-size media, or specify custom cropping, you must provide your own editing UI.
- _Delegate object_ Finally, assign your [delegate object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) to the image picker controller’s [delegate](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619145-delegate) property.

Listing 1 verifies the prerequisites are satisfied by way of its method signature and a conditional test, and goes on to instantiate, configure, and asynchronously present the camera user interface full screen.

__Listing 1__  Presenting the camera interface full screen

```objc
- (BOOL) startCameraControllerFromViewController: (UIViewController*) controller
               usingDelegate: (id <UIImagePickerControllerDelegate,
                                   UINavigationControllerDelegate>) delegate {

    if (([UIImagePickerController isSourceTypeAvailable:
                 UIImagePickerControllerSourceTypeCamera] == NO)
            || (delegate == nil)
            || (controller == nil))
        return NO;


    UIImagePickerController *cameraUI = [[UIImagePickerController alloc] init];
    cameraUI.sourceType = UIImagePickerControllerSourceTypeCamera;

    // Displays a control that allows the user to choose picture or
    // movie capture, if both are available:
    cameraUI.mediaTypes =
        [UIImagePickerController availableMediaTypesForSourceType:
            UIImagePickerControllerSourceTypeCamera];

    // Hides the controls for moving & scaling pictures, or for
    // trimming movies. To instead show the controls, use YES.
    cameraUI.allowsEditing = NO;

    cameraUI.delegate = delegate;

    [controller presentModalViewController: cameraUI animated: YES];
    return YES;
}
```

Listing 1 provides a picker that lets the user capture still images and movies, if both are available on the device. To instead present a picker that captures only movies, for example, ensure that movie capture is available and then set the [mediaTypes](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619173-mediatypes) property as follows:

```
cameraUI.mediaTypes = [[NSArray alloc] initWithObjects: (NSString *) kUTTypeMovie, nil];
```

(To ensure that movie capture is available, call the [availableMediaTypesForSourceType:](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619169-availablemediatypesforsourcetype) class method.)

For a picker that captures only still images, replace the [kUTTypeMovie](https://developer.apple.com/documentation/coreservices/kuttypemovie) identifier here with [kUTTypeImage](https://developer.apple.com/documentation/coreservices/kuttypeimage), or rely on the default value of the `mediaTypes` property, which is `kUTTypeImage`.

The `startCameraControllerFromViewController:usingDelegate:` example method from Listing 1 is designed to be invoked by an action method such as this:

```objc
- (IBAction) showCameraUI {
    [self startCameraControllerFromViewController: self
                                    usingDelegate: self];
}
```

Notice, as specified in the method signature in [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydimbwfvjvona), that the delegate object must conform to the [UIImagePickerControllerDelegate](https://developer.apple.com/documentation/uikit/uiimagepickercontrollerdelegate) and [UINavigationControllerDelegate](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate) [protocols](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45).

The result of the `startCameraControllerFromViewController:usingDelegate:` example method is that the system modally displays the standard camera interface, including controls for capturing media or canceling, as shown in [Figure 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydimbwfvjvooa).

When the user taps a button in the camera interface to accept a newly captured picture or movie, or to just cancel the operation, the system notifies the delegate of the user’s choice. The system does not, however, dismiss the camera interface. The delegate must dismiss it by calling the [dismissModalViewControllerAnimated:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621369-dismissmodalviewcontrolleranimat) method and must release the interface as well. It is for this reason that, typically, you make the view controller that presents the camera interface serve double-duty as the delegate.

Listing 2 shows example implementations of delegate methods for an image picker controller. The [imagePickerController:didFinishPickingMediaWithInfo:](https://developer.apple.com/documentation/uikit/uiimagepickercontrollerdelegate/1619126-imagepickercontroller) implementation includes code for saving a still image or a movie, depending on what the user captured.

__Listing 2__  Delegate methods for a camera interface

```objc
@implementation CameraViewController (CameraDelegateMethods)

// For responding to the user tapping Cancel.
- (void) imagePickerControllerDidCancel: (UIImagePickerController *) picker {

    [[picker parentViewController] dismissModalViewControllerAnimated: YES];
    [picker release];
}

// For responding to the user accepting a newly-captured picture or movie
- (void) imagePickerController: (UIImagePickerController *) picker
            didFinishPickingMediaWithInfo: (NSDictionary *) info {

    NSString *mediaType = [info objectForKey: UIImagePickerControllerMediaType];
    UIImage *originalImage, *editedImage, *imageToSave;

    // Handle a still image capture
    if (CFStringCompare ((CFStringRef) mediaType, kUTTypeImage, 0)
            == kCFCompareEqualTo) {

        editedImage = (UIImage *) [info objectForKey:
                    UIImagePickerControllerEditedImage];
        originalImage = (UIImage *) [info objectForKey:
                    UIImagePickerControllerOriginalImage];

        if (editedImage) {
            imageToSave = editedImage;
        } else {
            imageToSave = originalImage;
        }

    // Save the new image (original or edited) to the Camera Roll
        UIImageWriteToSavedPhotosAlbum (imageToSave, nil, nil , nil);
    }

    // Handle a movie capture
    if (CFStringCompare ((CFStringRef) mediaType, kUTTypeMovie, 0)
            == kCFCompareEqualTo) {

        NSString *moviePath = [[info objectForKey:
                    UIImagePickerControllerMediaURL] path];

        if (UIVideoAtPathIsCompatibleWithSavedPhotosAlbum (moviePath)) {
            UISaveVideoAtPathToSavedPhotosAlbum (
                    moviePath, nil, nil, nil);
        }
    }

    [[picker parentViewController] dismissModalViewControllerAnimated: YES];
    [picker release];
}

@end
```

If image editing is enabled and the user successfully accepts a newly captured picture, the _info_ parameter of the [imagePickerController:didFinishPickingMediaWithInfo:](https://developer.apple.com/documentation/uikit/uiimagepickercontrollerdelegate/1619126-imagepickercontroller) method contains a dictionary that includes the edited image. Treat this image as the selected image, as done in Listing 2. If you want to store the original image, you can get it from the dictionary, also as shown in the code listing.

Instead of immediately saving the new media item to the user’s Camera Roll as shown in this example, you could instead call custom code to work with the media.

[Next](Picking%20an%20Item%20from%20the%20Photo%20Library.md)[Previous](About%20the%20Camera%20and%20Photo%20Library.md)

