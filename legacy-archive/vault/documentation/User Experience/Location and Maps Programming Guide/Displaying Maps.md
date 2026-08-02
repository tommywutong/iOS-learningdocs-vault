---
title: Location and Maps Programming Guide
apple_id: TP40009497
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: User Experience
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/MapKit/MapKit.html
archived_at: '2026-07-18T02:12:05.175404Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Location and Maps Programming Guide](About%20Location%20Services%20and%20Maps.md)


[Next](Annotating%20Maps.md)[Previous](Geocoding%20Location%20Data.md)

# Displaying Maps

The Map Kit [framework](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56) lets you embed a fully functional map interface into your app. The map support provided by this framework includes many features of the Maps app in both iOS and OS X. You can display standard street-level map information, satellite imagery, or a combination of the two. You can zoom, pan, and pitch the map programmatically, display 3D buildings, and annotate the map with custom information. The Map Kit framework also provides automatic support for the touch events that let users zoom and pan the map.

To use the features of the Map Kit framework, turn on the Maps capability in your Xcode project (doing so also adds the appropriate entitlement to your App ID). Note that the only way to distribute a maps-based app is through the iOS App Store or Mac App Store. If you’re unfamiliar with entitlements, code signing, and provisioning, start learning about them in _App Distribution Quick Start_. For general information about the classes of the Map Kit framework, see _[Map Kit Framework Reference](https://developer.apple.com/documentation/mapkit)_.

A map view contains a flattened representation of a spherical object, namely the Earth. To use maps effectively, you need to understand how to specify points in a map view and how those points translate to points on the Earth’s surface. Understanding map coordinate systems is especially important if you plan to place custom content, such as overlays, on top of the map.

To understand the coordinate systems used by Map Kit, it helps to understand how the three-dimensional surface of the Earth is mapped to a two-dimensional map. Figure 5-1 shows how the surface of the Earth can be mapped to a two-dimensional surface.

__Figure 5-1__  Mapping spherical data to a flat surface

!

Map Kit uses a Mercator map projection, which is a specific type of cylindrical map projection like the one shown in Figure 5-1. In a cylindrical map projection, the coordinates of a sphere are mapped onto the surface of a cylinder, which is then unwrapped to generate a flat map. In such a projection, the longitude lines that normally converge at the poles become parallel instead, causing land masses to be distorted as you move away from the equator. The advantage of a Mercator projection is that the map content is scaled in a way that benefits general navigation. Specifically, on a Mercator map projection, a straight line drawn between any two points on the map yields a course heading that can be used in actual navigation on the surface of the Earth. The projection used by Map Kit uses the Prime Meridian as its central meridian.

How you specify data points on a map depends on how you intend to use them. Map Kit supports three basic coordinate systems for specifying map data points:

- A _map coordinate_ is a latitude and longitude on the spherical representation of the Earth. Map coordinates are the primary way of specifying locations on the globe. You specify individual map coordinate values using the [CLLocationCoordinate2D](https://developer.apple.com/documentation/corelocation/cllocationcoordinate2d) structure. You can specify areas using the [MKCoordinateSpan](https://developer.apple.com/documentation/mapkit/mkcoordinatespan) and [MKCoordinateRegion](https://developer.apple.com/documentation/mapkit/mkcoordinateregion) structures.
- A _map point_ is an x and y value on the Mercator map projection. Map points are used for many map-related calculations instead of map coordinates because they simplify the mathematics involved in the calculations. In your app, you use map points primarily when specifying the shape and position of custom map overlays. You specify individual map points using the [MKMapPoint](https://developer.apple.com/documentation/mapkit/mkmappoint) structure. You can specify areas using the [MKMapSize](https://developer.apple.com/documentation/mapkit/mkmapsize) and [MKMapRect](https://developer.apple.com/documentation/mapkit/mkmaprect) structures.
- A _point_ is a graphical unit associated with the coordinate system of a view object. Map points and map coordinates must be mapped to points before drawing custom content in a view. You specify individual points using the [CGPoint](https://developer.apple.com/documentation/coregraphics/cgpoint) structure. You can specify areas using the [CGSize](https://developer.apple.com/documentation/coregraphics/cgsize) and [CGRect](https://developer.apple.com/documentation/coregraphics/cgrect) structures.

In most situations, the coordinate system you should use is predetermined by the Map Kit interfaces you are using. When it comes to storing actual data in files or inside your app, map coordinates are precise, portable, and the best option for storing location data. Core Location also uses map coordinates when specifying location values.

Although you typically specify points on the map using latitude and longitude values, there may be times when you need to convert to and from other coordinate systems. For example, you usually use map points when specifying the shape of overlays. Table 5-1 lists the conversion routines you use to convert from one coordinate system to another. Most of these conversions require a view object because they involve converting to or from points.

__Table 5-1__  Map coordinate system conversion routines

| Convert from | Convert to | Conversion routines |
| Map coordinates | Points | [convertCoordinate:toPointToView:](https://developer.apple.com/documentation/mapkit/mkmapview/1452694-convertcoordinate) (`MKMapView`)  [convertRegion:toRectToView:](https://developer.apple.com/documentation/mapkit/mkmapview/1452055-convert) (`MKMapView`) |
| Map coordinates | Map points | [MKMapPointForCoordinate](https://developer.apple.com/documentation/mapkit/1452514-mkmappointforcoordinate) |
| Map points | Map coordinates | [MKCoordinateForMapPoint](https://developer.apple.com/documentation/mapkit/1452534-mkcoordinateformappoint)  [MKCoordinateRegionForMapRect](https://developer.apple.com/documentation/mapkit/mkcoordinateregion/1452357-init) |
| Map points | Points | [pointForMapPoint:](https://developer.apple.com/documentation/mapkit/mkoverlayview/1613874-pointformappoint) ([MKOverlayRenderer](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer))  [rectForMapRect:](https://developer.apple.com/documentation/mapkit/mkoverlayview/1613870-rectformaprect) ([MKOverlayRenderer](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer)) |
| Points | Map coordinates | [convertPoint:toCoordinateFromView:](https://developer.apple.com/documentation/mapkit/mkmapview/1452503-convert) ([MKMapView](https://developer.apple.com/documentation/mapkit/mkmapview))  [convertRect:toRegionFromView:](https://developer.apple.com/documentation/mapkit/mkmapview/1452305-convert) ([MKMapView](https://developer.apple.com/documentation/mapkit/mkmapview)) |
| Points | Map points | [mapPointForPoint:](https://developer.apple.com/documentation/mapkit/mkoverlayview/1613878-mappointforpoint) ([MKOverlayRenderer](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer))  [mapRectForRect:](https://developer.apple.com/documentation/mapkit/mkoverlayview/1613882-maprectforrect) ([MKOverlayRenderer](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer)) |

The [MKMapView](https://developer.apple.com/documentation/mapkit/mkmapview) class is a self-contained interface for presenting map data in your app: It provides support for displaying map data, managing user interactions, and hosting custom content provided by your app. Never subclass `MKMapView`. Instead, embed it as-is into your app’s view hierarchy.

Also assign a [delegate object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) to the map. The map view reports all relevant interactions to its delegate so that the delegate has a chance to respond appropriately.

You can add a map view to your app programmatically or using Interface Builder:

- To add a map using Interface Builder, drag a Map view object to the appropriate view or window.
- To add a map programmatically, [create an instance](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39) of the `MKMapView` class, [initialize](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21) it using the [initWithFrame:](https://developer.apple.com/documentation/uikit/uiview/1622488-init) method, and then add it as a subview to your window or view hierarchy.

Because a map view is a view, you can manipulate it the same way you manipulate other views. You can change its size and position in your view hierarchy, configure its autoresizing behaviors, and add subviews to it. The map view itself is an opaque container for a complex view hierarchy that handles the display of map-related data and all interactions with that data. Any subviews you add to the map view retain the position specified by their [frame](https://developer.apple.com/documentation/uikit/uiview/1622621-frame) property and don’t scroll with the map contents. If you want content to remain fixed relative to a specific map coordinate (and thus scroll with the map itself), you must use annotations or overlays as described in [Annotating Maps](Annotating%20Maps.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqnrnknltc). It’s best to avoid any modification of a map view’s hierarchy.

New maps are configured to accept user interactions and display map data only. By default, a standard map uses a 3D perspective by enabling pitch, which tilts the map, and rotation, which lets the map display a heading. You can specify pitch and rotation by creating an [MKMapCamera](https://developer.apple.com/documentation/mapkit/mkmapcamera) object. You can configure the map to display satellite imagery or a mixture of satellite and map data by changing the Type attribute of the map in Interface Builder or by changing the value in the [mapType](https://developer.apple.com/documentation/mapkit/mkmapview/1452742-maptype) property. If you want to limit user interactions, you can change the values in the [rotateEnabled](https://developer.apple.com/documentation/mapkit/mkmapview/1452274-rotateenabled), [pitchEnabled](https://developer.apple.com/documentation/mapkit/mkmapview/1452265-pitchenabled), [zoomEnabled](https://developer.apple.com/documentation/mapkit/mkmapview/1452577-iszoomenabled), and [scrollEnabled](https://developer.apple.com/documentation/mapkit/mkmapview/1451998-isscrollenabled) properties as well. If you want to respond to user interactions, use a delegate as described in [Using the Delegate to Respond to User Interactions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqmznknlti).

The `MKMapView` class has several properties that you can configure programmatically. These properties control important information such as which part of the map is currently visible, whether the content is displayed in 3D, and what user interactions are allowed.

The [region](https://developer.apple.com/documentation/mapkit/mkmapview/1452709-region) property of the `MKMapView` class controls the currently visible portion of the map. When a map is first created, its visible region is typically set to the entire world. In other words, the region encompasses the area that shows as much of the map as possible. You can change this region by assigning a new value to the [region](https://developer.apple.com/documentation/mapkit/mkmapview/1452709-region) property. This property contains an [MKCoordinateRegion](https://developer.apple.com/documentation/mapkit/mkcoordinateregion) structure, which has the definition shown below.

```
typedef struct {
   CLLocationCoordinate2D center;
   MKCoordinateSpan span;
} MKCoordinateRegion;
```

The interesting part of an `MKCoordinateRegion` structure is the span. The __span__ defines how much of the map at a given point should be visible. Although the span is analogous to the width and height values of a rectangle, it’s specified using map coordinates and thus is measured in degrees, minutes, and seconds. One degree of latitude is equivalent to approximately 111 kilometers, but longitudinal distances vary with the latitude. At the equator, one degree of longitude is equivalent to approximately 111 kilometers, but at the poles this value is zero. If you prefer to specify the span in meters, use the [MKCoordinateRegionMakeWithDistance](https://developer.apple.com/documentation/mapkit/mkcoordinateregion/1452245-init) to create a region data structure with meter values instead of degrees.

The value you assign to the `region` property (or set using the [setRegion:animated:](https://developer.apple.com/documentation/mapkit/mkmapview/1452768-setregion) method) is usually not the same value that is eventually stored by that property. Setting the span of a region nominally defines the rectangle you want to view but also implicitly sets the zoom level for the map view itself. The map view can’t display arbitrary zoom levels and must adjust any regions you specify to match the zoom levels it supports. It chooses the zoom level that allows your entire region to be visible while still filling as much of the screen as possible. It then adjusts the `region` property accordingly. To find out the resulting region without actually changing the value in the `region` property, use the [regionThatFits:](https://developer.apple.com/documentation/mapkit/mkmapview/1452371-regionthatfits) method of the map view.

A 3D map is a standard 2D map viewed at an angle from a vantage point above the map’s plane. The point’s altitude, combined with the angle from which the map is viewed, determine the span and tilt (also known as __pitch__) of the 2D map surface. Users can adjust the pitch and rotation of a map and, in iOS 7 and OS X v10.9 and later, you can use the [MKMapCamera](https://developer.apple.com/documentation/mapkit/mkmapcamera) class to programmatically adjust a 3D map.

A camera object uses the following properties to define the appearance of a 3D map:

- Altitude. The camera’s height (in meters) above the surface of the map.
- Pitch. The angle at which the camera tilts, relative to the ground. (Note that a pitch of 0 produces a standard 2D map because the camera is looking straight down.)
- Heading. The cardinal direction in which the camera is facing.
- Center. The point on the map surface that appears in the center of the screen or window.

In iOS 7 and OS X v10.9 and later, maps are 3D by default, which can affect your app in the following ways:

- Because a pitched map can expose the sky, users can see areas that are beyond the boundaries of the map. Be sure to check the validity of values returned by the map view’s conversion methods (such as [convertPoint:toCoordinateFromView:](https://developer.apple.com/documentation/mapkit/mkmapview/1452503-convert)) so your app doesn’t try to place annotations in the sky.
- If Map Kit detects a nonsensical pitch value, such as 180 degrees (that is, looking straight up at the sky), it clamps the pitch to a reasonable value.
- Often, the visible area of a 3D map is not rectangular when it’s viewed in two dimensions. In this scenario, the `region` and [visibleMapRect](https://developer.apple.com/documentation/mapkit/mkmapview/1452732-visiblemaprect) properties specify a rectangular area that contains a 2D approximation of the pitched map’s visible area.
- Annotations automatically maintain their size and orientation even as the map rotates or pitches, so your artwork won’t get distorted or resized. (Learn more about working with annotations in [Annotating Maps](Annotating%20Maps.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqnrnknltc).)

For the most part, 3D maps work the same in iOS and OS X apps. The few differences between the platforms are primarily in the user interface and in some underlying object types: A 3D map in an OS X app displays compass and zoom controls and a map data attribution label; a 3D map in an iOS app doesn’t display these items. In OS X, Map Kit defines objects that inherit from [NSView](https://developer.apple.com/documentation/appkit/nsview) and [NSImage](https://developer.apple.com/documentation/appkit/nsimage); in iOS, the analogous objects inherit from [UIView](https://developer.apple.com/documentation/uikit/uiview) and [UIImage](https://developer.apple.com/documentation/uikit/uiimage).

In iOS 7 and OS X v10.9 and later, the `MKMapView` class includes a [camera](https://developer.apple.com/documentation/mapkit/mkmapview/1452277-camera) property you can use to create and access a 3D map, save and restore map state, and programmatically zoom and pan. For example, you can easily create a 3D map of a location by specifying a position and altitude from which to view the location, asking Map Kit to create an appropriate camera object, and assigning the object to your map view’s `camera` property. Listing 5-1 shows how to do this.

__Listing 5-1__  Creating a 3D map

```
// Create a coordinate structure for the location.
CLLocationCoordinate2D ground = CLLocationCoordinate2DMake(myLatitude, myLongitude);

// Create a coordinate structure for the point on the ground from which to view the location.
CLLocationCoordinate2D eye = CLLocationCoordinate2DMake(eyeLatitude, eyeLongitude);

// Ask Map Kit for a camera that looks at the location from an altitude of 100 meters above the eye coordinates.
MKMapCamera *myCamera = [MKMapCamera cameraLookingAtCenterCoordinate:ground fromEyeCoordinate:eye eyeAltitude:100];

// Assign the camera to your map view.
mapView.camera = myCamera;
```

Because a camera object fully defines the appearance of a map, it’s a good idea to use it to save and restore your map’s state. The `MKMapCamera` class conforms to the [NSSecureCoding](https://developer.apple.com/documentation/foundation/nssecurecoding) protocol, so you can use a camera object with an archiver or, in an iOS app, the UIKit state restoration APIs. Listing 5-2 shows an example of saving and restoring a map’s state.

__Listing 5-2__  Archiving and unarchiving a map

```
MKMapCamera *camera = [map camera]; // Get the map's current camera.
[NSKeyedArchiver archiveRootObject:camera toFile:stateFile]; // Archive the camera.
…
MKMapCamera *camera = [NSKeyedUnarchiver unarchiveObjectWithFile:stateFile]; // Unarchive the camera.
[map setCamera:camera]; // Restore the map.
```


Zooming and panning allow you to change the visible portion of the map at any time:

- To pan the map (but keep the same zoom level, pitch, and rotation), change the value in the [centerCoordinate](https://developer.apple.com/documentation/mapkit/mkmapview/1451901-centercoordinate) property of the map view or the camera, or call the map view’s [setCenterCoordinate:animated:](https://developer.apple.com/documentation/mapkit/mkmapview/1451976-setcenter) or [setCamera:animated:](https://developer.apple.com/documentation/mapkit/mkmapview/1452476-setcamera) methods.
- To change the zoom level (and optionally pan the map), change the value in the [region](https://developer.apple.com/documentation/mapkit/mkmapview/1452709-region) property of the map view or call the [setRegion:animated:](https://developer.apple.com/documentation/mapkit/mkmapview/1452768-setregion) method. You can also vary the altitude of the camera in a 3D map (doubling or halving the altitude is approximately the same as zooming in or out by one level).

If you only want to pan the map, you should do so by modifying only the `centerCoordinate` property. Attempting to pan the map by changing the `region` property usually causes a change in the zoom level as well, because changing any part of the region causes the map view to evaluate the zoom level needed to display that region appropriately. Changes to the current latitude almost always cause the zoom level to change and other changes might cause a different zoom level to be chosen as well. Using the `centerCoordinate` property (or the [setCenterCoordinate:animated:](https://developer.apple.com/documentation/mapkit/mkmapview/1451976-setcenter) method) lets the map view know that it should leave the zoom level unchanged and update the span as needed. For example, this code pans the map to the left by half the current map width by finding the coordinate at the left edge of the map and using it as the new center point.

```
CLLocationCoordinate2D mapCenter = myMapView.centerCoordinate;
mapCenter = [myMapView convertPoint:
               CGPointMake(1, (myMapView.frame.size.height/2.0))
               toCoordinateFromView:myMapView];
[myMapView setCenterCoordinate:mapCenter animated:YES];
```

To zoom the map, modify the span of the visible map region. To zoom in, assign a smaller value to the span. To zoom out, assign a larger value. For example, as shown here, if the current span is one degree, specifying a span of two degrees zooms out by a factor of two.

```
MKCoordinateRegion theRegion = myMapView.region;

// Zoom out
theRegion.span.longitudeDelta *= 2.0;
theRegion.span.latitudeDelta *= 2.0;
[myMapView setRegion:theRegion animated:YES];
```


Map Kit includes built-in support for displaying the user’s current location on the map. To show this location, set the [showsUserLocation](https://developer.apple.com/documentation/mapkit/mkmapview/1452682-showsuserlocation) property of your map view object to `YES`. Doing so causes the map view to use Core Location to find the user’s location and add an annotation of type [MKUserLocation](https://developer.apple.com/documentation/mapkit/mkuserlocation) to the map.

The addition of the `MKUserLocation` annotation object to the map is reported by the delegate in the same way that custom annotations are. If you want to associate a custom annotation view with the user’s location, you should return that view from your delegate object’s [mapView:viewForAnnotation:](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452045-mapview) method. If you want to use the default annotation view, return `nil` from that method. To learn more about adding annotations to a map, see [Annotating Maps](Annotating%20Maps.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqnrnknltc).

In some cases, it doesn’t make sense to add a fully interactive map view to your app. For example, if your app lets users choose a location from a scrolling list of map images, enabling interaction with each map is unnecessary and may impair scrolling performance. Another reason to create a static image of a map is to implement a printing feature. In both situations, you can use a `MKMapSnapshotter` object to create a static map image asynchronously. The resulting snapshot contains an image view, to which you can apply all the effects that you apply to other images in your app.

In general, follow these steps to create a map snapshot:

1. Make sure you have a network connection and that your app is in the foreground.
2. Create and configure an [MKMapSnapshotOptions](https://developer.apple.com/documentation/mapkit/mkmapsnapshotoptions) object, which specifies the appearance of the map and the size of the output. (An iOS app can also specify a scale for the output.)
3. Create an [MKMapSnapshotter](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter) object and initialize it with the options you specified in step 1.
4. Call [startWithCompletionHandler:](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/1452479-start) to start the asynchronous snapshot-creation task.
5. When the task completes, retrieve the map snapshot from your completion handler block and draw any overlays or annotations that should appear in the final image.

In an iOS app, you often use [drawContentForPageAtIndex:inRect:](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/1621641-drawcontentforpageatindex) to implement printing. Because this method expects to receive the printable content synchronously, you have to modify the snapshot-creation steps to include the use of a dispatch semaphore and queue that help you block on the completion of the snapshot. (To learn more about dispatch semaphores and queues, see [Using Dispatch Semaphores to Regulate the Use of Finite Resources](../../General/Concurrency%20Programming%20Guide/Dispatch%20Queues.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojrfvbuqmjqgiwvgvzsgq).)

To create a map snapshot for printing in an iOS app:

1. Create and configure an [MKMapSnapshotOptions](https://developer.apple.com/documentation/mapkit/mkmapsnapshotoptions) object. (Note that iOS apps generally specify a scale of 2 because most printers are high-resolution.)
2. Create an [MKMapSnapshotter](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter) object and initialize it with the options you specified in step 1.
3. Create a dispatch semaphore that allows you to wait for a resource—in this case, the snapshot—to become available.
4. Choose a dispatch queue on which to receive a callback when the snapshot is ready.
5. Create variables to hold the results of the snapshot-creation task.
6. Call [startWithQueue:completionHandler:](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/1452419-start) to start generating the snapshot asynchronously.
7. When the task completes, pass the snapshot’s image to [drawContentForPageAtIndex:inRect:](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/1621641-drawcontentforpageatindex) for printing.

The code in Listing 5-3 implements most of the steps for printing a map snapshot. The code doesn’t show the creation of the `MKMapSnapshotOptions` object.

__Listing 5-3__  Creating a map snapshot for printing

```
// Initialize the semaphore to 0 because there are no resources yet.
dispatch_semaphore_t snapshotSem = dispatch_semaphore_create(0);

// Get a global queue (it doesn't matter which one).
dispatch_queue_t queue = dispatch_get_global_queue(myQueuePriorityLevel, 0);

// Create variables to hold return values. Use the __block modifier because these variables will be modified inside a block.
__block MKMapSnapshot *mapSnapshot = nil;
__block NSError *error = nil;

// Start the asynchronous snapshot-creation task.
[snapshotter startWithQueue:queue
          completionHandler:^(MKMapSnapshot *snapshot, NSError *e) {
    mapSnapshot = snapshot;
error = e;
    // The dispatch_semaphore_signal function tells the semaphore that the async task is finished, which unblocks the main thread.
    dispatch_semaphore_signal(snapshotSem);
}];

// On the main thread, use dispatch_semaphore_wait to wait for the snapshot task to complete.
dispatch_semaphore_wait(snapshotSem, DISPATCH_TIME_FOREVER);
if (error) { // Handle error. }

// Get the image from the newly created snapshot.
UIImage *image = mapSnapshot.image;
// Optionally, draw annotations on the image before displaying it.
```


The `MKMapView` class reports significant map-related events to its associated [delegate](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) object. The delegate object is an object that conforms to the [MKMapViewDelegate](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate) protocol. Providing a delegate object helps you respond to the following types of events:

- Changes to the visible region of the map
- The loading of map tiles from the network
- Changes in the user’s location
- Changes associated with annotations and overlays

For information about handling changes associated with annotations and overlays, see [Annotating Maps](Annotating%20Maps.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqnrnknltc).

If you would prefer to display map information in the Maps app as opposed to your own app, you can launch Maps programmatically using one of two techniques:

- In iOS 6 and and OS X v10.9 and later, use an [MKMapItem](https://developer.apple.com/documentation/mapkit/mkmapitem) object to open Maps.
- In iOS 5 and earlier, create and open a specially formatted map URL as described in _[Apple URL Scheme Reference](../../../featuredarticles/Apple%20URL%20Scheme%20Reference/About%20Apple%20URL%20Schemes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqojz)_.

The preferred way to open the Maps app is to use the `MKMapItem` class. This class offers both the [openMapsWithItems:launchOptions:](https://developer.apple.com/documentation/mapkit/mkmapitem/1452207-openmapswithitems) class method and the [openInMapsWithLaunchOptions:](https://developer.apple.com/documentation/mapkit/mkmapitem/1452239-openinmapswithlaunchoptions) instance method for opening the app and displaying locations or directions.

For an example showing how to open the Maps app, see [Asking the Maps App to Display Directions](Providing%20Directions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqobnknltm).

[Next](Annotating%20Maps.md)[Previous](Geocoding%20Location%20Data.md)

