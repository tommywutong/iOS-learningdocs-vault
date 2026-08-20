---
title: Image Capture Applications Programming Guide
apple_id: TP40005196
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: ImageCaptureCore
published: '2009-08-29'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ImageCaptureServicesProgrammingGuide/CreatinganApplicationUsingImageCaptureCore/CreatinganApplicationUsingImageCaptureCore.html
archived_at: '2026-07-15T05:23:12.611552Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Image Capture Applications Programming Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Creating%20an%20Application%20Using%20ImageKit.md)

# Creating an Application Using ImageCaptureCore

Use the `ImageCaptureCore` framework to create headless applications, applications that require a custom UI for the device browser, camera view, or scanner view, or to add features or controls not available in `ImageKit`.

This section uses the `SimpleCameraBrowser` example, which you can download from Apple Developer Connection sample code.

The example instantiates a device browser and displays an array of cameras in a table view. The cameras are properties of the device browser, stored as key/value pairs. The user selects a camera and clicks an “Open” button, which opens a session with the selected camera. The camera’s contents are displayed in a second table view, wrapped in a scroll view. If the camera contains any downloadable image files, they are listed by thumbnail, name, and date, and a “Download” button is activated. The thumbnails are returned as core graphics image refs, so a utility function converts them to `NSImages` for display in the table view.

Even though the `ImageCaptureCore` uses a programmatic interface, it includes Cocoa bindings, so you can build your custom UI using Interface Builder, as this example illustrates. The delegate methods and array controllers are written in code, but the table views, scrolling lists, and buttons are created in Interface Builder, and they are tied together using Cocoa bindings.

You can open the `SimpleCameraBrowser` sample and read along, or you can create an equivalent program from scratch. Here’s how to create it yourself:

Open Xcode, choose New Xcode project, then choose Cocoa Application. Give your application a name and save it. Then add `QuartzCore.framework` to your project. If you opened the `SimpleCameraBrowser` project, set the SDK to Mac OS 10.6.

Open `appController.h` in the sample, or create it yourself by following these directions.

Create a new class file named appController (choose New from the File menu). Xcode automatically creates the .h and .m files and adds them to the project.

The application controller is your delegate for the device browser.

Type the following into the application controller’s `.h` file:

```objc
// Import the Cocoa and ImageCaptureCore headers
#import <Cocoa/Cocoa.h>
#import <ImageCaptureCore/ImageCaptureCore.h>

// Create a public interface for the controller
@interface appController : NSObject

// Create delegates for the device browser and camera device classes.
<ICDeviceBrowserDelegate, ICCameraDeviceDelegate> {

// Create an instance variable for the device browser
// and an array for the cameras the browser finds
ICDeviceBrowser * mDeviceBrowser;
NSMutableArray * mCameras;

// Define Interface Builder outlets for two
// array controllers -- one for cameras,
// one for the chosen camera's files
IBOutlet  NSArrayController *  mCamerasController;
IBOutlet  NSArrayController *  mMediaFilesController;

// Define IB outlets for the tableviews used to
// display the cameras and the chosen camera's contents
IBOutlet  NSTableView * mCameraContentTableView;
IBOutlet  NSTableView * mCamerasTableView;
}

 // Cameras are properties of the device browser stored in an array
@property(retain)   NSMutableArray* cameras;

 // Create a boolean to indicate whether the camera has images to download
@property(readonly) BOOL            canDownload;
@end
```


Now let’s look at how to construct the application controller’s `.m` file.

```objc
#import "appController.h"

// The camera device returns core graphics image refs,
// convert them to NSImages for table view
 @interface NSImageFromCGImageRef: NSValueTransformer {}
@end
 @implementation NSImageFromCGImageRef
+ (Class)transformedValueClass      { return [NSImage class]; }
+ (BOOL)allowsReverseTransformation { return NO; }
- (id)transformedValue:(id)item
{
    if ( item )
        return  [[[NSImage alloc] initWithCGImage:(CGImageRef)item size:NSZeroSize] autorelease];     else         return nil; } @end  @implementation appController

// synthesize the getters and setters for camera properties
@synthesize cameras = mCameras;

// Main task -- on launch
- (void)applicationDidFinishLaunching:(NSNotification*)notification {     mCameras = [[NSMutableArray alloc] initWithCapacity:0];          // Get an instance of ICDeviceBrowser     mDeviceBrowser = [[ICDeviceBrowser alloc] init];     // Assign a delegate     mDeviceBrowser.delegate = self;     // Look for cameras in all available locations     mDeviceBrowser.browsedDeviceTypeMask = mDeviceBrowser.browsedDeviceTypeMask                                                  | ICDeviceTypeMaskCamera                                         | ICDeviceLocationTypeMaskLocal                                         | ICDeviceLocationTypeMaskShared                                         | ICDeviceLocationTypeMaskBonjour                                         | ICDeviceLocationTypeMaskBluetooth                                         | ICDeviceLocationTypeMaskRemote;     // Start browsing for cameras     [mDeviceBrowser start];  }

// Stop browser and release it when done
- (void)applicationWillTerminate:(NSNotification*)notification {     mDeviceBrowser.delegate = NULL;          [mDeviceBrowser stop];     [mDeviceBrowser release];          [mCameras release]; }

// Method delegates for device added and removed
//
// Device browser maintains list of cameras as key-value pairs, so delegate
// must call willChangeValueForKey to modify list
- (void)deviceBrowser:(ICDeviceBrowser*)browser didAddDevice:(ICDevice*)addedDevice moreComing:(BOOL)moreComing {         if ( addedDevice.type & ICDeviceTypeCamera )     {          addedDevice.delegate = self;         // implement manual observer notification for the cameras property         [self willChangeValueForKey:@"cameras"];             [mCameras addObject:addedDevice];         [self didChangeValueForKey:@"cameras"];     } }

- (void)deviceBrowser:(ICDeviceBrowser*)browser didRemoveDevice:(ICDevice*)device moreGoing:(BOOL)moreGoing {     device.delegate = NULL;          // implement manual observer notification for the cameras property     [self willChangeValueForKey:@"cameras"];         [mCameras removeObject:device];     [self didChangeValueForKey:@"cameras"]; }  - (void)didRemoveDevice:(ICDevice*)removedDevice {     [mCamerasController removeObject:removedDevice]; }  // Check to see if the camera has image files to download
- (void)observeValueForKeyPath:(NSString*)keyPath ofObject:(id)object change:(NSDictionary*)change context:(void*)context {     if ( [keyPath isEqualToString:@"selectedObjects"] && (object == mMediaFilesController) )     {         [self willChangeValueForKey:@"canDownload"];         [self didChangeValueForKey:@"canDownload"];     } }  - (BOOL)canDownload {     if ( [[mMediaFilesController selectedObjects] count] )         return YES;     else         return NO; }

// Download images
// (Add a download button in interface builder -- use boolean to enable button)
- (void)downloadFiles:(NSArray*)files {     NSDictionary* options = [NSDictionary dictionaryWithObject:[NSURL fileURLWithPath:[@"~/Pictures" stringByExpandingTildeInPath]] forKey:ICDownloadsDirectoryURL];          for ( ICCameraFile* f in files )     {         [f.device requestDownloadFile:f options:options downloadDelegate:self didDownloadSelector:@selector(didDownloadFile:error:options:contextInfo:) contextInfo:NULL];     } }

// Done downloading -- log results to console for debugging
- (void)didDownloadFile:(ICCameraFile*)file error:(NSError*)error options:(NSDictionary*)options contextInfo:(void*)contextInfo {     NSLog( @"didDownloadFile called with:\n" );     NSLog( @"  file:        %@\n", file );     NSLog( @"  error:       %@\n", error );     NSLog( @"  options:     %@\n", options );     NSLog( @"  contextInfo: %p\n", contextInfo ); }
```

That’s all the code you’ll need for a camera browser. The rest of this section shows you how to construct a user interface using Interface Builder.

Because `ImageCaptureCore` supports Cocoa bindings, you can construct the user interface entirely in Interface Builder, without writing any more code. Your interface will consist of an object (the application controller), a pair of table views to show the cameras and images, and two buttons—one to select a camera from the list, and the other to download images from the camera.

Creating the UI in interface builder involves a lot of dragging, dropping, control-clicking, and clicking checkboxes. This is easy to show and easy to do, but the description is necessarily somewhat tedious. The easiest way to understand the interface is to open the `MainMenu` Interface Builder file in `SimpleCameraBrowser` and inspect it.

A description of how to construct the interface yourself follows.

1. Double click the `MainMenu` file in the project window’s Interface Builder folder.
2. Choose File > Read Class Files and navigate to the `appController.h` file that you created. Click Open.
3. Drag an Object (`NSObject`) from the Library panel into the document window.
4. Type appController in the Name field of the Identity Inspector window and press Return.

1. In the document window, control-click the File's Owner icon and drag to the appController object. Release. Choose delegate in the pop-up menu.
2. Control-click the Window icon and drag to the appController object. Release. Choose delegate in the pop-up menu.

   This makes your application controller object responsible for events sent to the window and the file owner.

1. Double-click the Window icon. Drag an `NSTableView` from the Library panel into the window. Position and size it as desired.
2. If you want to make it a scrollable list, enter a value in the Attribute pane’s Line Scroll Vertical box, then click inside the scroll view object to select the contained `NSTableView` and enter the same value in the Row Height box of the Inspector window’s Size pane.
3. Drag an `NSImageCell` from the Library panel into the `NSTableView`.
4. Create a title for the list by dragging in an `NSTextField` from the Library pane. Double-click it and type “Cameras”. Drag it into position above the list.

1. Drag an `NSTableView` from the Library panel into the window. Position and size it as desired.
2. You want this list to be scrollable, so enter a value in the Attribute pane’s Line Scroll Vertical box, then click inside the scroll view object to select the contained `NSTableView` and enter the same value in the Row Height box of the Inspector window’s Size pane.
3. Enter a value of 3 in the Columns box of the Inspector window’s Attributes pane.
4. Drag an `NSImageCell` from the Library panel into the first column of the`NSTableView`.
5. Label the second and third columns “Name” and “Date” by clicking in the column title bar.

1. Drag an `NSArrayController` from the Library panel onto the MainMenu window.
2. Type “Cameras Controller" in the Name field of the Identity inspector window and press Return.
3. Click the Attributes Inspector.

   Using the plus (+) button, add the following keys for the Object Controller:

   - name
   - contents
   - icon
   - mediaFiles

   Deselect Avoid Empty Selection and Select Inserted Objects.
4. Click the Bindings tab in the Attributes Inspector.

   In the Controller Content section, for the Content Array bindings, click Bind To and select appController from the pop-up menu.

   Type “cameras” in the Model Key Path box.

1. Drag an `NSArrayController` from the Library panel onto the MainMenu window.
2. Type “MediaFiles Controller" in the Name field of the Identity inspector window and press Return.
3. Click the Attributes Inspector.

   Using the plus (+) button, add the following keys for the Object Controller:

   - thumbnailIfAvailable
   - name
   - size
   - creationDate

   Deselect Avoid Empty Selection and Select Inserted Objects.
4. Click the Bindings tab in the Attributes Inspector.

   In the Controller Content section, for the Content Array bindings, click Bind To and select Cameras Controller from the pop-up menu.

   Select mediaFiles in the Model Key Path pop-up menu.

1. Control-click the appController object in the MainMenu window. Drag to the cameras table view. Release. Select mCameraTableView in the Outlets window.
2. If you have made the camera table view scrollable, repeat step 1 for the scroll view.
3. Control-click the appController object in the MainMenu window again. Drag to the media files table view. Release. Select mCameraContentTableView in the Outlets window.
4. Repeat step 3 for the camera content scroll view.
5. Control-click the App Controller again. This time drag to the Cameras Controller in the same window. Release. Select mCameraController in the Outlets window.
6. Control-click the App Controller again. This time drag to the Media Files Controller in the same window. Release. Select mMediaFilesController in the Outlets window.

You need a way for the user to select a device from the list. An “Open” button works.

1. Drag an NSButton from the Library pane into the window. Position it below the camera table view, double-click it, and type “Open”.
2. With the button selected, open the Target in the Bindings Inspector. Click the Bind to checkbox and choose Cameras Controller from the pop-up menu.
3. In the Selector Name box, enter requestOpenSession.

   This causes the “Open” button to issue a requestOpenSession to the device browser from the Camera Controller.
4. In the Model Key Path box, enter hasOpenSession. in the Value Transformer box, enter NSNegateBoolean.

   This tells the device browser to toggle to boolean value hasOpenSession for the selected device.

1. Click the first column of the camera table view. Open the Bindings Inspector. Click Value, then Bind To: and choose Cameras Controller from the pop-up menu.
2. Click Model Key Path and enter icon.
3. Click Value Transformer and enter `NSImageFromCGRef`.
4. Deselect allowing multiple value selections.
5. Click the second column in the camera table view. Click Value in the Bindings Inspector and choose Cameras Controller again.
6. In the Model Key Path field, enter name.

1. Click the first column of the media files table view. Open the Bindings Inspector. Click Value, then Bind To: and choose MediaFiles Controller from the pop-up menu.
2. Click Model Key Path and enter thumbnailIfAvailable.
3. Click Value Transformer and enter `NSImageFromCGRef`.
4. Click the second column in the camera table view. Click Value in the Bindings Inspector and choose MediaFiles Controller again.
5. In the Model Key Path field, enter name.
6. Click the third column in the camera table view. Click Value in the Bindings Inspector and choose MediaFiles Controller yet again.
7. In the Controller Key field, enter arrangedObjects
8. In the Model Key Path field, enter creationDate.

The user interface is now complete. You should be able to build and run the application.

[Next](Document%20Revision%20History.md)[Previous](Creating%20an%20Application%20Using%20ImageKit.md)

