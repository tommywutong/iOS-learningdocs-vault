---
title: ImageKit Programming Guide
apple_id: TP40004907
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/ImageKitProgrammingGuide/Slideshows/Sildeshows.html
archived_at: '2026-07-15T07:36:02.942157Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [ImageKit Programming Guide](Introduction%20to%20Image%20Kit%20Programming%20Guide.md)


[Next](Taking%20Snapshots%20and%20Setting%20Pictures.md)[Previous](Browsing%20Images.md)

# Showing Slides

Several applications provided with OS X have a slideshow feature built in, including Mail and Preview. Starting with OS X v10.5, any application can provide slideshow support by using the [IKSlideshow](https://developer.apple.com/documentation/quartz/ikslideshow) class. In addition to digital images, a slideshow can display pages from PDF documents, QuickTime movies, Quartz Composer compositions, and custom document formats supported through the Quick Look framework.

This chapter describes the user interface provided by the [IKSlideshow](https://developer.apple.com/documentation/quartz/ikslideshow) class and provides step-by-step instructions for creating a slideshow application.

When a slideshow runs, by default it opens to the first image provided by the slideshow data source. The slideshow uses the entire screen, as shown in Figure 4-1. The controls at the bottom of the screen allow the user to move forward and backward, pause and play, view an index layout of all items in the show, fit the images to the screen, and close the slideshow.

__Figure 4-1__  A slideshow with controls

![A slideshow with controls](attachments/Art/ikslideshow_01.jpg)![A slideshow with controls](attachments/Art/ikslideshow_01.jpg)

The user can override the automatic advance by clicking the pause control or by manually moving through the show using the onscreen controls or the arrow keys on the keyboard.

The index sheet (see Figure 4-2) lets the user see many slides at the same time and to move through them using the arrow keys or by clicking an image. If the user double-clicks an image or presses Return, the slideshow resumes, starting with the selected image.

__Figure 4-2__  The index sheet

![The index sheet](attachments/Art/ikslideshow_02.jpg)![The index sheet](attachments/Art/ikslideshow_02.jpg)

This section describes how to write an application that supports slideshows. First you’ll see what needs to be done to support slideshows in any application. Then you’ll take a look at a specific implementation of a simple slideshow application and the steps required to write the application.

A slideshow application requires a shared instance of the `IKSlideshow` class and a data source. You obtain the shared instance using the method `sharedSlideshow`. You run the slideshow using the method `runSlideshowWithDataSource:options:`.

You must implement two methods of the `IKSlideshowDataSource` protocol:

- `numberOfSlideshowItems` returns the number of items in the slideshow.
- `slideshowItemAtIndex:` returns the slideshow item at the given index. The item can be specified as an image object (`CGImage`, `NSImage`), a string that represents a path to a file, or as a URL (`NSURL`).

The `IKSlideshow` class defines a number of other methods that are useful depending on the nature of your application. For example, you can export slideshow items to an application, reload data, run or stop a slideshow, set a time interval that determines when the slideshow starts to play automatically, and get the index of the item that’s currently playing.

The `IKSlideshowDataSource` protocol defines several optional methods that you might want to implement, such as methods that allow your application to take action at certain points in the slideshow: `slideshowDidStop`, `slideshowWillStart`, and [slideshowDidChangeCurrentIndex:](https://developer.apple.com/documentation/quartz/ikslideshowdatasource/1504272-slideshowdidchangecurrentindex). See _[IKSlideshowDataSource Protocol Reference](https://developer.apple.com/documentation/quartz/ikslideshowdatasource)_ for a complete descriptions of the methods in this protocol.

The slideshow application that you’ll create in this section is quite simple. It implements the required methods of the the `IKSlideshowDataSource` protocol and allows the user to stop the slideshow and reload another set of images to view. It provides pathnames for each item in the slideshow. Although the paths could lead to any image file format supported by Quartz 2D and the Image I/O framework, including paths to PDF documents, for this application you’ll restrict the datasource mode to images. In this mode, Image Kit displays only the first page of any PDF documents that are mixed in with the images in a folder.

The most complicated part of this application is the code that fetches the pathnames for each item in the slideshow. The path-fetching code must be able to accept a folder path and resolve any folder path to the individual items in the path. The user should be able to provide a path to a folder that contains both individual items and other folders, but the resulting slideshow should show only individual files. In other words, the slideshow should not display folder icons, but rather, the items in the folder.

When launched, the simple slideshow application presents the user with an Open panel (dialog) for choosing a folder. The user closes the slideshow by clicking the Close icon provided by the slideshow controls shown in [Figure 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmbxfvbuqnrnknlte). The user can start another slideshow by choosing File > Choose Images, which presents the Open panel again. The slideshow application terminates when the user chooses Quit from the menu or presses Command-Q.

The user interface for this application is very simple—a Choose Images menu item, which you’ll create using Interface Builder. All other user interface elements are provided by the `IKSlideshow` class or other parts of the system.

To control the application, you’ll use the `NSWindowController` class. Your controller will have:

- A mutable array for holding the paths to each of the items in the slideshow
- An instance of the `IKSlideshow` class

Now that you have an overview of the slideshow application, it’s time to write the code. First you’ll set up the Xcode project, the project files, and the controller interface. Then you’ll add the necessary routines to the implementation file. Finally, you’ll create the user interface in Interface Builder.

Follow these steps to set up the project:

1. Create a Cocoa application and name it `Simple Slideshow`.
2. Add the Quartz framework to the project.

   For details, see [Using the Image Kit in Xcode](Basics%20of%20Using%20the%20Image%20Kit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmbxfvbuqmznknlti).
3. Choose File > New File.
4. Select “Objective-C NSWindowController subclass” and click Next.
5. Name the file `SlideshowController.m` and keep the option to create the header file. Then click Finish.
6. In the `SlideshowController.h` file, import the Quartz framework by adding this statement:

   `#import <Quartz/Quartz.h>`
7. Add an instance variable for the slideshow and a mutable array for image paths.

   The interface should look as follows:

```objc
@interface SlideshowController : NSWindowController {
    IKSlideshow        *mSlideshow;
    NSMutableArray *mImagePaths;
}
@end
```
8. Save the `SlideshowController.h` file.

Implement the slideshow routines by following these steps:

1. Open the `SlideshowController.m` file.
2. In the implementation file, add an `awakeFromNib` method.

   The method first obtains a shared instance of the slideshow. Next it loads images. You’ll write the `loadImages` method and its supporting methods later on. The `loadImages` method, if successful, will add image paths to the `mImagePaths` array. If paths are added, then the `awakeFromNib` method runs the slideshow, using the paths as the data source.

   The following `awakeFromNib` method sets the mode to images only. If there are PDF documents in any folders that you add, Image Kit renders only the first page.

   Note that the method does not set any options for the slideshow. However, you can set any of the options specified by the slideshow option key constants defined in _[IKSlideshow Class Reference](https://developer.apple.com/documentation/quartz/ikslideshow)_.

```objc
- (void)awakeFromNib
{
     mSlideshow = [IKSlideshow sharedSlideshow];
     [self loadImages];
     if ([mImagePaths count] > 0)
        [mSlideshow runSlideshowWithDataSource:(id<IKSlideshowDataSource>)self
                      inMode: IKSlideshowModeImages
                      options: NULL];
}
```
3. Next you need to implement the two required methods of the [IKSlideshowDataSource Protocol](https://developer.apple.com/documentation/quartz/ikslideshowdatasource) protocol.

   The `numberOfSlideshowItems` method simply returns a count the number of paths in the `mImagePaths` array. The `slideshowItemAtIndex:` method returns the index of the `mImagePaths` array for the item in question.

```objc
- (NSUInteger)numberOfSlideshowItems
{

    return [mImagePaths count];
}


- (id)slideshowItemAtIndex: (NSUInteger)index
{
   int i;
   i = index % [mImagePaths count];
    return [mImagePaths objectAtIndex: i];
}
```
4. Implement a `loadImages` method.

   This and the next few steps are where most of the work is done in the slideshow application. The `loadImages` method allocates and initializes the `mImagePaths` array, if necessary. Otherwise, the method removes all objects in preparation for adding new slideshow items.

   Next the method calls a function to open files. You’ll write this routine in the next step. The `openFiles` routine invokes the Open panel (`NSOpenPanel` class) and returns an array of paths or `NULL` if the user cancels the Open panel. If there is an array of paths, the `loadImages` method iterates through the paths and calls the method `addImagesFromPath:`, which you’ll write in a moment.

```objc
- (void)loadImages
{
    if (NULL == mImagePaths)
    {
        mImagePaths = [[NSMutableArray alloc] init];
    } else {
      [mImagePaths removeAllObjects];
    }
    NSArray * array = openFiles();
    if (array != NULL)
    {
        NSEnumerator *  enumerator;
        NSString *      path;

        enumerator = [array objectEnumerator];
        while (path = [enumerator nextObject])
        {
                [self addImagesFromPath: path];
        }
    }
}
```
5. Next you need to include an `openFiles` routine, which you’ll add in the `SlideshowController.m` file, but prior to the implementation statement.

   The `openFiles` routine creates an instance of the `NSOpenPanel` class, sets up options to allow the user to choose directories as well as files, runs the panel, and returns either an array of the file names chosen by the user, or `nil` if the user clicks the Cancel button.

```
static NSArray *openFiles()
{
    NSOpenPanel *panel;

    panel = [NSOpenPanel openPanel];
    [panel setFloatingPanel:YES];
    [panel setCanChooseDirectories:YES];
    [panel setCanChooseFiles:NO];
    int i = [panel runModal];
    if(i == NSOKButton){
        return [panel URLs];
    }
        return nil;
}
```
6. Write the `addImagesFromPath:` method called by the `loadImages` method.

   The first task for this method is to obtain an array of all the string objects contained in the given path. Then the method iterates through the string objects. If the string does not have a filename extension, then it represents a path. In this case the method calls itself to recursively resolve the path into individual items. If the string has an extension, then it represents an individual item that can be added to the image path array.

```objc
- (void)addImagesFromPath: (NSString *)path
{
   NSArray * array  = [[NSFileManager defaultManager]
                   directoryContentsAtPath: path];


    NSEnumerator *  enumerator;
    NSString *      imagePath;

    enumerator = [array objectEnumerator];
    while (imagePath = [enumerator nextObject])
    {
        if ([[[imagePath pathExtension] lowercaseString] isEqualToString: @""])
        {
             [self addImagesFromPath: [NSString stringWithFormat: @"%@/%@/",
                                       path, imagePath]];

      } else
        {
            [mImagePaths addObject: [NSString stringWithFormat: @"%@/%@",
                                     path, imagePath]];
        }
    }
}
```
7. You need to write a choose images method that is invoked when the user chooses that command.

   Recall that the user can stop a slideshow and start another by choosing File > Choose Images. You’ll add this menu item and connect to this action later on.

   This method first calls the `loadImages` method to fetch and add new slideshow items. If there are items to add (that is, the user did not click Cancel in the Open panel), the method reloads the slideshow data and then runs the slideshow.

```objc
- (IBAction) chooseImages:(id) sender
{

    [self loadImages];
    if ([mImagePaths count] > 0) {
        [mSlideshow reloadData];
        [mSlideshow  runSlideshowWithDataSource: (id<IKSlideshowDataSource>)self
            inMode: IKSlideshowModeImages
            options: NULL];
    }
}
```
8. Save the `SlideshowController.m` file.
9. Open the `SlideshowController.h` file and add these method declarations:

```objc
- (IBAction)chooseImages:(id)sender;

- (NSUInteger)numberOfSlideshowItems;
- (id)slideshowItemAtIndex: (NSUInteger)index;
- (void)loadImages;
```
10. Save the `SlideshowController.h` file.

Set up the user interface in Interface Builder by following these steps:

1. Double-click the `MainMenu.nib` file to open Interface Builder.
2. Choose File > Synchronize With Xcode.
3. Delete the window icon in the nib document window.
4. Double-click the MainMenu icon in the nib document window.
5. Drag a Menu Item (`NSMenuItem`) from the Library to the File menu and name the item Choose Images.
6. Drag an Object (`NSObject`) from the Library to the nib document window.
7. In the Identity inspector, type SlideshowController in the Name field. THen select `SlideshowController` from the Class pop-up menu.
8. Control-drag from the Choose Images menu item to the SlideshowController and in the connections panel choose `chooseImages:`.
9. Save the nib file.
10. In Xcode, click Build and Go. Then test your application to make sure it works.

    You might get warnings if you placed the methods into your file in the wrong order.

    Check to make sure that you can run a slideshow. Exit the slideshow, and then start another by choosing File > Choose Images.

[Next](Taking%20Snapshots%20and%20Setting%20Pictures.md)[Previous](Browsing%20Images.md)

