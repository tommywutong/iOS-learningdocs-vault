---
title: Accessing Image Metadata in iOS
apple_id: DTS40009180
resource_type: QA
platform: watchOS|iOS
topic: null
technology: UIKit
published: '2011-08-22'
source_url: https://developer.apple.com/library/archive/qa/qa1622/_index.html
archived_at: '2026-07-18T02:32:58.167651Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1622

# Accessing Image Metadata in iOS

## Q:  How do I get image metadata in iOS?

A: The _[UIImagePickerController](https://developer.apple.com/documentation/uikit/uiimagepickercontroller)_ allows a developer to prompt the user to take a picture from the camera, or to choose an existing picture from the photo library. Beginning in iOS 4.1 the `NSDictionary` object that the _[UIImagePickerControllerDelegate](https://developer.apple.com/documentation/uikit/uiimagepickercontrollerdelegate)_ returns contains an `NSDictionary` that contains the metadata of the photo that was just captured in addition to the `UImage`. To access the metadata dictionary use the `UIImagePickerControllerMediaMetadata` key of the `NSDictionary` returned by the `UIImagePickerControllerDelegate`. To store the metadata along with the image in the Camera Roll, use the _[writeImageToSavedPhotosAlbum:metadata:completionBlock:](https://developer.apple.com/documentation/assetslibrary/alassetslibrary)_ method of the _[Assets Library framework](https://developer.apple.com/documentation/assetslibrary)_.

__Listing 1__  Example of accessing and saving the image metadata with the `UIImagePickerController`.

```
// Respond to the user accepting a newly-captured picture - (void) imagePickerController: (UIImagePickerController *) picker  didFinishPickingMediaWithInfo: (NSDictionary *) info {      NSString *mediaType = [info objectForKey: UIImagePickerControllerMediaType];     UIImage *originalImage, *editedImage, *imageToSave;      // Handle a still image capture     if (CFStringCompare ((CFStringRef) mediaType, kUTTypeImage, 0)         == kCFCompareEqualTo) {          editedImage = (UIImage *) [info objectForKey:                                    UIImagePickerControllerEditedImage];         originalImage = (UIImage *) [info objectForKey:                                      UIImagePickerControllerOriginalImage];          if (editedImage) {             imageToSave = editedImage;         } else {             imageToSave = originalImage;         }          // Get the image metadata         UIImagePickerControllerSourceType pickerType = picker.sourceType;         if(pickerType == UIImagePickerControllerSourceTypeCamera)         {             NSDictionary *imageMetadata = [info objectForKey:                                            UIImagePickerControllerMediaMetadata];             // Get the assets library             ALAssetsLibrary *library = [[ALAssetsLibrary alloc] init];             ALAssetsLibraryWriteImageCompletionBlock imageWriteCompletionBlock =             ^(NSURL *newURL, NSError *error) {                 if (error) {                     NSLog( @"Error writing image with metadata to Photo Library: %@", error );                 } else {                     NSLog( @"Wrote image with metadata to Photo Library");                 }             };              // Save the new image (original or edited) to the Camera Roll             [library writeImageToSavedPhotosAlbum:[imageToSave CGImage]                                           metadata:imageMetadata                                    completionBlock:imageWriteCompletionBlock];         }     }       [[picker parentViewController] dismissModalViewControllerAnimated: YES];     [picker release]; }
```

To access the metadata of existing pictures in the photo library you need to use the _[Assets Library framework](https://developer.apple.com/documentation/assetslibrary)_ which can be used to access the pictures and videos managed by the Photos application including their metadata.

__Listing 2__  Example of accessing the image metadata with the Assets Library framework.

```
// Get the assets library ALAssetsLibrary *library = [[ALAssetsLibrary alloc] init];  // Enumerate just the photos and videos group by using ALAssetsGroupSavedPhotos. [library enumerateGroupsWithTypes:ALAssetsGroupSavedPhotos                        usingBlock:^(ALAssetsGroup *group, BOOL *stop)  {       // Within the group enumeration block, filter to enumerate just photos.      [group setAssetsFilter:[ALAssetsFilter allPhotos]];       // For this example, we're only interested in the first item.      [group enumerateAssetsAtIndexes:[NSIndexSet indexSetWithIndex:0]                              options:0                           usingBlock:^(ALAsset *alAsset, NSUInteger index, BOOL *innerStop)       {            // The end of the enumeration is signaled by asset == nil.           if (alAsset) {               ALAssetRepresentation *representation = [alAsset defaultRepresentation];               NSDictionary *imageMetadata = [representation metadata];               // Do something interesting with the metadata.           }       }];  }                      failureBlock: ^(NSError *error)  {      // Typically you should handle an error more gracefully than this.      NSLog(@"No groups");  }];  [library release];
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-08-22 | Discusses the new APIs available in iOS 4 to access the metadata of an image. |
| 2009-08-25 | New document that describes how to access image metadata using the UIImagePickerController and the Assets Library Framework. |

