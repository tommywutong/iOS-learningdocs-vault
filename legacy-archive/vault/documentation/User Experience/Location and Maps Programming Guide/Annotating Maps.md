---
title: Location and Maps Programming Guide
apple_id: TP40009497
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: User Experience
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/AnnotatingMaps/AnnotatingMaps.html
archived_at: '2026-07-18T02:11:51.929837Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Location and Maps Programming Guide](About%20Location%20Services%20and%20Maps.md)


[Next](Providing%20Directions.md)[Previous](Displaying%20Maps.md)

# Annotating Maps

_Annotations_ display content that can be defined by a single coordinate point; _overlays_ display content that is defined by any number of points and may constitute one or more contiguous or noncontiguous shapes. For example, you use annotations to represent information such as the user’s current location, a specific address, or a single point of interest. You use overlays to present more complex information such as routes or traffic information, or the boundaries of areas such as parks, lakes, cities, states, or countries.

Unlike generic subviews, annotations and overlays remain fixed to the map so that they move appropriately when the user zooms, pans, or scrolls. In a 3D map, annotations maintain their position, size, and orientation regardless of how the map rotates or pitches.

Map Kit separates the data associated with an annotation or overlay from its visual presentation on the map. This separation allows the map to manage visible annotations and overlays much more efficiently: You can add hundreds of annotations and overlays to a map and still expect reasonable performance.

Annotations offer a way to highlight specific coordinates on the map and provide additional information about them. You can use annotations to call out particular addresses, points of interest, and other types of destinations. When displayed on a map, annotations typically have some sort of image to identify their location and may also have a callout bubble providing information and links to more content. Figure 6-1 shows an annotation that uses a standard pin annotation view to mark a particular location and provides a callout bubble that displays additional information including a disclosure indicator that leads to more details.

__Figure 6-1__  Displaying an annotation in a map

!

To display an annotation on a map, your app must provide two distinct objects:

- An _annotation object_, which is an object that conforms to the [MKAnnotation](https://developer.apple.com/documentation/mapkit/mkannotation) protocol and manages the data for the annotation.
- An _annotation view_, which is a view (derived from the [MKAnnotationView](https://developer.apple.com/documentation/mapkit/mkannotationview) class) used to draw the visual representation of the annotation on the map surface.

Annotation objects are typically small data objects that store the map coordinate data and any other relevant information about the annotation, such as a title string. Because annotations are defined using a protocol, you can turn any class in your app into an annotation object. In practice, it’s good to keep annotation objects lightweight, especially if you intend to add large numbers of them to the map. The map view keeps a reference to the annotation objects you add to it and uses the data in those objects to determine when to display the corresponding view.

Map Kit provides some standard annotation views, such as the pin annotation, and you can also define custom annotation views. Whether you use standard or custom annotation views, you don’t add them directly to the map surface. Instead, the map delegate provides an annotation view when the map view asks for one and the map view incorporates the annotation into its view hierarchy.

The annotations you create are typically anchored to a single map coordinate that doesn’t change, but you can modify an annotation’s coordinate programmatically if needed. In addition, you can implement support to allow users to drag annotations around the map.

The steps for implementing and using annotations in your map-based app are shown below. It’s assumed that your app incorporates an `MKMapView` object somewhere in its interface.

1. Define an appropriate annotation object using one of the following options:

   - Use the [MKPointAnnotation](https://developer.apple.com/documentation/mapkit/mkpointannotation) class to implement a simple annotation. This type of annotation contains properties for specifying the title and subtitle strings to display in the annotation’s callout bubble.
   - Define a custom object that conforms to the [MKAnnotation](https://developer.apple.com/documentation/mapkit/mkannotation) protocol, as described in [Defining a Custom Annotation Object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqnrnknlte). A custom annotation can store any type of data you want.
2. Define an annotation view to present the annotation data on screen. How you define your annotation view depends on your needs and may be one of the following:

   - If you want to use a standard pin annotation, create an instance of the [MKPinAnnotationView](https://developer.apple.com/documentation/mapkit/mkpinannotationview) class; see [Using the Standard Annotation Views](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqnrnknltm).
   - If the annotation can be represented by a custom static image, create an instance of the [MKAnnotationView](https://developer.apple.com/documentation/mapkit/mkannotationview) class and assign the image to its [image](https://developer.apple.com/documentation/mapkit/mkannotationview/1452094-image) property; see [Using the Standard Annotation Views](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqnrnknltm).
   - If a static image is insufficient for representing your annotation, subclass `MKAnnotationView` and implement the custom drawing code needed to present it. For information about how to implement custom annotation views, see [Defining a Custom Annotation View](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqnrnknltinq).
3. Implement the [mapView:viewForAnnotation:](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452045-mapview) method in your map view delegate.

   In your implementation of this method, dequeue an existing annotation view if one exists; if not, create a new annotation view. If your app supports multiple types of annotations, include logic in this method to create a view of the appropriate type for the provided annotation object. For more information about implementing the `mapView:viewForAnnotation:` method, see [Creating Annotation Views from Your Delegate Object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqnrnknltiny).
4. Add your annotation object to the map view using the [addAnnotation:](https://developer.apple.com/documentation/mapkit/mkmapview/1452069-addannotation) (or [addAnnotations:](https://developer.apple.com/documentation/mapkit/mkmapview/1451889-addannotations)) method.

When you add an annotation to a map view, the map view displays the corresponding annotation view whenever the coordinate for the annotation is in the visible map rectangle. If you want to hide annotations selectively, you must manually remove them from the map view yourself. You can add and remove annotations at any time.

All annotations are drawn at the same scale every time, regardless of the map’s current zoom level. If your map contains many annotations, your annotation views could overlap each other as the user zooms out. To counter this behavior, you can add and remove annotations based on the map’s current zoom level. For example, a weather app might display information only for major cities when the map is zoomed out to show the entire state. As the user zooms in, the app could then add new annotations containing weather information for smaller cities and regions. Implementing the logic necessary to add and remove annotations is your responsibility.

For more information about how to manage the annotations of a map view effectively, see [Displaying Multiple Annotation Objects](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqnrnknltini).

If all you want to do is associate a title with a map coordinate, you can use the [MKPointAnnotation](https://developer.apple.com/documentation/mapkit/mkpointannotation) class for your annotation object. However, if you want to represent additional information with the annotation, you need to define a custom annotation object. All annotation objects must conform to the [MKAnnotation](https://developer.apple.com/documentation/mapkit/mkannotation) protocol.

A custom annotation object consists of a map coordinate and whatever other data you want to associate with the annotation. Listing 6-1 shows the minimal code needed to declare a custom annotation class. The [coordinate](https://developer.apple.com/documentation/mapkit/mkannotation/1429524-coordinate) property declaration is from the `MKAnnotation` protocol and must be included in all annotation classes. Because this is a simple annotation, it also includes an initializer method, which is used to set the value of the read-only `coordinate` property. Your own declaration would likely also include methods and properties that define additional annotation data.

__Listing 6-1__  Creating a simple annotation object

```objc
@interface MyCustomAnnotation : NSObject <MKAnnotation> {
    CLLocationCoordinate2D coordinate;
}
@property (nonatomic, readonly) CLLocationCoordinate2D coordinate;
- (id)initWithLocation:(CLLocationCoordinate2D)coord;

// Other methods and properties.
@end
```

Your custom class must implement the coordinate property and a way to set its value. (It’s recommended that you synthesize `coordinate` because it ensures that Map Kit can automatically update the map based on changes to the property.) All that remains is to implement the custom `initWithLocation:` method, which is shown in Listing 6-2.

__Listing 6-2__  Implementing the MyCustomAnnotation class

```objc
@implementation MyCustomAnnotation
@synthesize coordinate;

- (id)initWithLocation:(CLLocationCoordinate2D)coord {
    self = [super init];
    if (self) {
        coordinate = coord;
    }
    return self;
}
@end
```

For more examples of annotation objects, see the sample code project _[MapCallouts: Using MapKit Annotations](https://developer.apple.com/library/archive/samplecode/MapCallouts/Introduction/Intro.html#//apple_ref/doc/uid/DTS40009746)_.

The standard annotation views make it easy to present annotations on your map. The [MKAnnotationView](https://developer.apple.com/documentation/mapkit/mkannotationview) class defines the basic behavior for all annotation views. For example, the [MKPinAnnotationView](https://developer.apple.com/documentation/mapkit/mkpinannotationview) subclass of `MKAnnotationView` displays one of the standard system pin images at the associated annotation’s coordinate point. You can also use `MKAnnotationView` to display a custom static image without subclassing.

To display a custom image as an annotation, create an instance of `MKAnnotationView` and assign the custom image to the object’s [image](https://developer.apple.com/documentation/mapkit/mkannotationview/1452094-image) property. When the annotation is displayed, your custom image appears, centered over the target map coordinate. If you don’t want the image to be centered on the map coordinate, you can use the [centerOffset](https://developer.apple.com/documentation/mapkit/mkannotationview/1452144-centeroffset) property to move the center point in any direction. Listing 6-3 shows an example of creating an annotation view with a custom image that should be offset to the right and above the annotation coordinate.

__Listing 6-3__  Creating a standard annotation view with a custom image

```
MKAnnotationView* aView = [[MKAnnotationView alloc] initWithAnnotation:annotation
                                  reuseIdentifier:@"MyCustomAnnotation"];
aView.image = [UIImage imageNamed:@"myimage.png"];
aView.centerOffset = CGPointMake(10, -20);
```

You create the standard annotation views in your delegate’s [mapView:viewForAnnotation:](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452045-mapview) method. For more information about how to implement this method, see [Creating Annotation Views from Your Delegate Object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqnrnknltiny).

If a static image is insufficient for representing your annotation, you can subclass [MKAnnotationView](https://developer.apple.com/documentation/mapkit/mkannotationview) and draw content dynamically in one of the following two ways:

- Continue to use the [image](https://developer.apple.com/documentation/mapkit/mkannotationview/1452094-image) property of `MKAnnotationView`, but change the image at regular intervals.
- Override the annotation view’s [drawRect:](https://developer.apple.com/documentation/uikit/uiview/1622529-draw) method and draw your content dynamically every time.

As with any custom drawing you do in a view, always consider performance before choosing an approach. Although custom drawing gives you the most flexibility, using images can be faster, especially if most of your content is fixed.

When you use the `drawRect:` method to draw content, specify a nonzero frame size for the annotation view shortly after initialization to ensure that your rendered content becomes visible. Specifying a nonzero frame size is necessary because the default [initialization method](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21) for annotation views uses the image specified in the `image` property to set the frame size later. If you draw the image instead of setting the property, you must set the [frame](https://developer.apple.com/documentation/uikit/uiview/1622621-frame) property of the view explicitly or your rendered content won’t be visible. And because the view draws in only part of its frame, set its `opaque` property to `NO` so that the remaining map content shows through. If you don’t set the `opaque` property, the drawing system fills your view with the current background color before calling the `drawRect:` method. Listing 6-4 shows an example initialization method that sets the frame size and opacity of a custom annotation view.

__Listing 6-4__  Initializing a custom annotation view

```objc
- (id)initWithAnnotation:(id <MKAnnotation>)annotation reuseIdentifier:(NSString *)reuseIdentifier
{
    self = [super initWithAnnotation:annotation reuseIdentifier:reuseIdentifier];
    if (self)
    {
        // Set the frame size to the appropriate values.
        CGRect  myFrame = self.frame;
        myFrame.size.width = 40;
        myFrame.size.height = 40;
        self.frame = myFrame;

        // The opaque property is YES by default. Setting it to
        // NO allows map content to show through any unrendered parts of your view.
        self.opaque = NO;
    }
    return self;
}
```

In most respects, drawing custom content in an annotation view is the same as it is in any view. The system calls your view’s `drawRect:` method to redraw portions of the view that need it, and you can force a redraw operation by calling the [setNeedsDisplay](https://developer.apple.com/documentation/uikit/uiview/1622437-setneedsdisplay) or [setNeedsDisplayInRect:](https://developer.apple.com/documentation/uikit/uiview/1622587-setneedsdisplayinrect) method of your view at any time. If you want to animate the contents of your view, set up a timer to fire at periodic intervals and update your view. To set up timers, see _[Timer Programming Topics](../../Cocoa/Timer%20Programming%20Topics/Introduction%20to%20Timers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3dc2i)_. To learn more about how views draw content, see _[View Programming Guide for iOS](../../Windows%20Views/View%20Programming%20Guide%20for%20iOS/About%20Windows%20and%20Views.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbt)_ or _[Cocoa Drawing Guide](../../Cocoa/Cocoa%20Drawing%20Guide/Introduction%20to%20Cocoa%20Drawing%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojq)_ (for OS X information).

When the map view needs an annotation view, it calls the [mapView:viewForAnnotation:](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452045-mapview) method of its [delegate object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14). If you don’t implement this method—or if you implement it and always return `nil`—the map view uses a default annotation view, which is typically a pin annotation view. If you want to return annotation views other than the default ones, you need to override [mapView:viewForAnnotation:](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452045-mapview) and create your views there.

Before creating a new view in the `mapView:viewForAnnotation:` method, always check to see if a similar annotation view already exists. The map view has the option of caching unused annotation views that it isn’t using, so an unused view may be available from the [dequeueReusableAnnotationViewWithIdentifier:](https://developer.apple.com/documentation/mapkit/mkmapview/1452672-dequeuereusableannotationviewwit) method. If the dequeuing method returns a value other than `nil`, update the view’s attributes and return it; if the method returns `nil`, create a new instance of the appropriate annotation view class. In both cases, it’s your responsibility to take the annotation passed to this method and assign it to your annotation view. Also use `mapView:viewForAnnotation:` to update the view before returning it.

Listing 6-5 shows an example implementation of the `mapView:viewForAnnotation:` method that provides pin annotation views for custom annotation objects. If an existing pin annotation view already exists, this method associates the annotation object with that view. If no view is in the reuse queue, this method creates a new one and sets up its basic properties. If the map is currently showing the user’s location, this method returns `nil` for any [MKUserLocation](https://developer.apple.com/documentation/mapkit/mkuserlocation) objects so that the map uses the default annotation view. (You would also customize the callout in the `mapView:viewForAnnotation:` method; see [Creating Callouts](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqnrnknlteoa).)

__Listing 6-5__  Creating annotation views

```objc
- (MKAnnotationView *)mapView:(MKMapView *)mapView
                      viewForAnnotation:(id <MKAnnotation>)annotation
{
    // If the annotation is the user location, just return nil.
    if ([annotation isKindOfClass:[MKUserLocation class]])
        return nil;

    // Handle any custom annotations.
    if ([annotation isKindOfClass:[MyCustomAnnotation class]])
    {
        // Try to dequeue an existing pin view first.
        MKPinAnnotationView*    pinView = (MKPinAnnotationView*)[mapView
        dequeueReusableAnnotationViewWithIdentifier:@"CustomPinAnnotationView"];

        if (!pinView)
        {
            // If an existing pin view was not available, create one.
            pinView = [[MKPinAnnotationView alloc] initWithAnnotation:annotation
                       reuseIdentifier:@"CustomPinAnnotationView"];
            pinView.pinColor = MKPinAnnotationColorRed;
            pinView.animatesDrop = YES;
            pinView.canShowCallout = YES;

            // If appropriate, customize the callout by adding accessory views (code not shown).
        }
        else
            pinView.annotation = annotation;

        return pinView;
    }

    return nil;
}
```


A callout is a standard or custom view that can appear with an annotation view. A standard callout displays the annotation’s title, and it can display additional content such as a subtitle, images, and a control. If you want to display a custom view that behaves like a callout, add a custom subview to the annotation view and update the annotation view’s hit testing method to handle user interaction with the subview.

Using a standard callout is the easiest way to display custom content without creating a custom subview. For example, Figure 6-2 shows a standard callout that’s been modified to display a custom image and a detail disclosure button (Listing 6-6 shows the code that creates this modified callout).

__Figure 6-2__  A standard callout modified to include a custom image and disclosure button

!

__Listing 6-6__  Customizing a standard callout

```objc
// This code snippet assumes that an annotation for the Golden Gate Bridge has already been added to the map view.

- (MKAnnotationView *)mapView:(MKMapView *)theMapView viewForAnnotation:(id <MKAnnotation>)annotation
{
// Try to dequeue an existing pin view first (code not shown).

// If no pin view already exists, create a new one.
MKPinAnnotationView *customPinView = [[MKPinAnnotationView alloc]
                                             initWithAnnotation:annotation reuseIdentifier:BridgeAnnotationIdentifier];
customPinView.pinColor = MKPinAnnotationColorPurple;
customPinView.animatesDrop = YES;
customPinView.canShowCallout = YES;

// Because this is an iOS app, add the detail disclosure button to display details about the annotation in another view.
UIButton *rightButton = [UIButton buttonWithType:UIButtonTypeDetailDisclosure];
[rightButton addTarget:nil action:nil forControlEvents:UIControlEventTouchUpInside];
customPinView.rightCalloutAccessoryView = rightButton;

      // Add a custom image to the left side of the callout.
UIImageView *myCustomImage = [[UIImageView alloc] initWithImage:[UIImage imageNamed:@"MyCustomImage.png"]];
customPinView.leftCalloutAccessoryView = myCustomImage;

return customPinView;
}
```

In an iOS app, it’s good practice to use the [mapView:annotationView:calloutAccessoryControlTapped:](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1616211-mapview) delegate method to respond when users tap a callout view’s control (as long as the control is a descendant of `UIControl`). In your implementation of this method you can discover the identity of the callout view’s annotation view so that you know which annotation the user tapped. In a Mac app, the callout view’s view controller can implement an action method that responds when a user clicks the control in a callout view.

When you use a custom view instead of a standard callout, you need to do extra work to make sure your callout shows and hides appropriately when users interact with it. The steps below outline the process for creating a custom callout that contains a button:

1. Design an `NSView` or `UIView` subclass that represents the custom callout. It’s likely that the subclass needs to implement the `drawRect:` method to draw your custom content.
2. Create a view controller that initializes the callout view and performs the action related to the button.
3. In the annotation view, implement `hitTest:` to respond to hits that are outside the annotation view’s bounds but inside the callout view’s bounds, as shown in [Listing 6-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqnrnknltgma).
4. In the annotation view, implement [setSelected:animated:](https://developer.apple.com/documentation/mapkit/mkannotationview/1452381-setselected) to add your callout view as a subview of the annotation view when the user clicks or taps it. If the callout view is already visible when the user selects it, the `setSelected:` method should remove the callout subview from the annotation view (see [Listing 6-8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqnrnknltgmi)).
5. In the annotation view’s `initWithAnnotation:` method, set the `canShowCallout` property to `NO` to prevent the map from displaying the standard callout when the user selects the annotation.

Listing 6-7 shows an example of implementing `hitTest:` to handle hits in the callout view that might be outside the bounds of the annotation view.

__Listing 6-7__  Responding to hits within a custom callout

```objc
- (NSView *)hitTest:(NSPoint)point
{
    NSView *hitView = [super hitTest:point];
    if (hitView == nil && self.selected) {
        NSView *calloutView = self.calloutViewController.view;
        NSPoint pointInCalloutView = [self convertPoint:point toView:calloutView];
        hitView = [calloutView hitTest:pointInCalloutView];
    }
    return hitView;
}
```

Listing 6-8 shows an example of implementing `setSelected:animated:` to animate the arrival and dismissal of a custom callout view when the user selects the annotation view.

__Listing 6-8__  Adding and removing a custom callout view

```objc
- (void)setSelected:(BOOL)selected
{
    [super setSelected:selected];

    // Get the custom callout view.
    NSView *calloutView = self.calloutViewController.view;
    if (selected) {
        NSRect annotationViewBounds = self.bounds;
        NSRect calloutViewFrame = calloutView.frame;
      // Center the callout view above and to the right of the annotation view.
        calloutViewFrame.origin.x = -(NSWidth(calloutViewFrame) - NSWidth(annotationViewBounds)) * 0.5;
        calloutViewFrame.origin.y = -NSHeight(calloutViewFrame) + 15.0;
        calloutView.frame = calloutViewFrame;

        [self addSubview:calloutView];
    } else {
        [calloutView.animator removeFromSuperview];
    }
}
```


If your app works with more than a few annotations, you might need to think about how you display them. The map view considers all annotation objects it knows about to be active and as a result, it always tries to display a corresponding annotation view when the given coordinate point is on the screen. If the coordinates for two annotations are close together, this could lead to overlap between the corresponding annotation views. If your map includes hundreds of annotations, zooming out far enough could lead to a visually unappealing mass of annotation views. Even worse, the annotations may be so close together that the user can’t access some of them.

The only way to eliminate annotation overcrowding is to remove some of the annotation objects from the map view. This typically involves implementing the [mapView:regionWillChangeAnimated:](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452571-mapview) and [mapView:regionDidChangeAnimated:](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452345-mapview) methods to detect changes in the map zoom level. During a zoom change, you can add or remove annotations as needed based on their proximity to one another. You might also consider other criteria (such as the user’s current location) to eliminate some annotations.

Map Kit includes numerous functions that make determining the proximity of map points easier. If you convert the map coordinate of your annotation to the map point coordinate space, you can use the [MKMetersBetweenMapPoints](https://developer.apple.com/documentation/mapkit/mkmappoint/1452729-distance) method to get the absolute distance between two points. You can also use each coordinate as the center of a map rectangle and use the [MKMapRectIntersectsRect](https://developer.apple.com/documentation/mapkit/1452221-mkmaprectintersectsrect) function to find any intersections. For a complete list of functions, see _Map Kit Functions Reference_.

Annotation views provide built-in dragging support, which makes it very easy to drag annotations around the map and to ensure that the annotation data is updated accordingly. To implement minimal support for dragging:

- In your annotation objects, implement the [setCoordinate:](https://developer.apple.com/documentation/mapkit/mkannotation/1429528-setcoordinate) method to allow the map view to update the annotation’s coordinate point.
- When creating your annotation view, set its [draggable](https://developer.apple.com/documentation/mapkit/mkannotationview/1452401-isdraggable) property to `YES`.

When the user touches and holds a draggable annotation view, the map view begins a drag operation for it. As the drag operation progresses, the map view calls the [mapView:annotationView:didChangeDragState:fromOldState:](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452229-mapview) method of its delegate to notify it of changes to the drag state of your view. You can use this method to affect or respond to the drag operation.

To animate your view during a drag operation, implement a custom [dragState](https://developer.apple.com/documentation/mapkit/mkannotationview/1451941-dragstate) method in your annotation view. As the map view processes drag-related touch events, it updates the [dragState](https://developer.apple.com/documentation/mapkit/mkannotationview/1451941-dragstate) property of the affected annotation view. Implementing a custom `dragState` method gives you a chance to intercept these changes and perform additional actions, such as animating the appearance of your view. For example, the [MKPinAnnotationView](https://developer.apple.com/documentation/mapkit/mkpinannotationview) class raises the pin off the map when a drag operation starts and drops the pin back down on the map when it ends.

Overlays offer a way to layer content over an arbitrary region of the map. Whereas annotations are always defined by a single map coordinate, overlays are typically defined by multiple coordinates. You can use these coordinates to create contiguous or noncontiguous sets of lines, rectangles, circles, and other shapes, which can then be filled or stroked with color. For example, you might use overlays to layer traffic information on top of roadways, highlight the boundaries of a park, or show city, state, and national borders. Figure 6-3 shows a filled and stroked overlay covering the state of Colorado.

__Figure 6-3__  Displaying an overlay on a map

!

To display an overlay on a map, your app must provide two distinct objects:

- An _overlay object_, which is an object that conforms to the [MKOverlay](https://developer.apple.com/documentation/mapkit/mkoverlay) protocol and manages the data points for the overlay.
- An _overlay renderer_, which is a class (derived from [MKOverlayRenderer](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer)) used to draw the visual representation of the overlay on the map surface.

Overlay objects are generally small data objects that store the points that define the overlay and any other relevant information, such as a title string. Because overlays are defined using a protocol, you can turn any class in your app into an overlay object. In addition, Map Kit defines several concrete overlay objects for specifying different types of standard shapes. The map view keeps a reference to the overlay objects you add to it and uses the data in those objects to determine when to display a corresponding view.

Map Kit provides standard overlay renderers that can draw any shapes represented by the concrete overlay objects. As with annotations, you don’t add overlay renderers directly to the map surface. Instead, the delegate object provides an overlay renderer when the map view asks for one, and the map view incorporates the overlay into its opaque view hierarchy.

Typically, the coordinates of an overlay on the map never change. Although it’s possible to create draggable overlays, doing so is rare. You would need to implement the code to track the dragging operation, and you must update the overlay coordinate points yourself.

Here are the steps for implementing and using overlays in your map-based app. It’s assumed that your app incorporates an `MKMapView` object somewhere in its interface.

1. Define an appropriate overlay data object using one of the following options:

   - Use the [MKCircle](https://developer.apple.com/documentation/mapkit/mkcircle), [MKPolygon](https://developer.apple.com/documentation/mapkit/mkpolygon), or [MKPolyline](https://developer.apple.com/documentation/mapkit/mkpolyline) class as-is.
   - Use the [MKTileOverlay](https://developer.apple.com/documentation/mapkit/mktileoverlay) class if your overlay is represented by collection of custom bitmap tiles.
   - Subclass [MKShape](https://developer.apple.com/documentation/mapkit/mkshape) or [MKMultiPoint](https://developer.apple.com/documentation/mapkit/mkmultipoint) to create overlays that provide app-specific behaviors or use custom shapes.
   - Use an existing class from your app and make it conform to the [MKOverlay](https://developer.apple.com/documentation/mapkit/mkoverlay) protocol.
2. Define an overlay renderer to present the overlay onscreen using one of the following options:

   - For standard shapes, use the [MKCircleRenderer](https://developer.apple.com/documentation/mapkit/mkcirclerenderer), [MKPolygonRenderer](https://developer.apple.com/documentation/mapkit/mkpolygonrenderer), or [MKPolylineRenderer](https://developer.apple.com/documentation/mapkit/mkpolylinerenderer) class to represent the overlay. You can customize many of the drawing attributes of the final shape using these classes.
   - For a tiled overlay, use the [MKTileOverlayRenderer](https://developer.apple.com/documentation/mapkit/mktileoverlayrenderer) class to handle the drawing of tiles on the map.
   - For custom shapes descended from [MKShape](https://developer.apple.com/documentation/mapkit/mkshape), define an appropriate subclass of [MKOverlayPathRenderer](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer) to render the shape.
   - For all other custom shapes and overlays, subclass [MKOverlayRenderer](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer) and implement your custom drawing code.
3. Implement the [mapView:rendererForOverlay:](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452203-mapview) method in your map view delegate.
4. Add your overlay data object to the map view using the [addOverlay:](https://developer.apple.com/documentation/mapkit/mkmapview/1451964-addoverlay) method or one of many others.

Unlike annotations, rendered overlays are automatically scaled to match the current zoom level of the map. Scaling the overlay is necessary because overlays generally highlight boundaries, roads, and other content that also scales during zooming.

You can rearrange the Z-ordering of overlays in a map to ensure that specific overlays are always displayed on top of others. And, to specify the level of an overlay with respect to other map content, such as roads, labels, and annotation views, use one of the [MKOverlayLevel](https://developer.apple.com/documentation/mapkit/mkoverlaylevel) constants:

- `MKOverlayLevelAboveRoads`
- `MKOverlayLevelAboveLabels`

Overlays can supplement or replace system-provided map content. If your overlay is opaque, use the [canReplaceMapContent](https://developer.apple.com/documentation/mapkit/mkoverlay/1452399-canreplacemapcontent) property to prevent the system from unnecessarily loading and drawing map content that users won’t see behind the overlay.

If all you want to do is highlight a specific map region, using the standard overlay classes is the easiest way to do it. The standard overlay classes include [MKCircle](https://developer.apple.com/documentation/mapkit/mkcircle), [MKPolygon](https://developer.apple.com/documentation/mapkit/mkpolygon), and [MKPolyline](https://developer.apple.com/documentation/mapkit/mkpolyline). These classes define the basic shape of the overlay and are used in conjunction with the [MKCircleRenderer](https://developer.apple.com/documentation/mapkit/mkcirclerenderer), [MKPolygonRenderer](https://developer.apple.com/documentation/mapkit/mkpolygonrenderer), or [MKPolylineRenderer](https://developer.apple.com/documentation/mapkit/mkpolylinerenderer) classes, which handle the rendering of that shape on the map surface.

Listing 6-9 shows an example of how you would create the rectangular polygon shown in [Figure 6-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqnrnknltcma). This polygon consists of four map coordinates that correspond to the four corners of the state of Colorado. After creating the polygon, all you have to do is add it to the map using the [addOverlay:](https://developer.apple.com/documentation/mapkit/mkmapview/1451964-addoverlay) method.

__Listing 6-9__  Creating a polygon overlay object

```
    // Define an overlay that covers Colorado.
    CLLocationCoordinate2D  points[4];

    points[0] = CLLocationCoordinate2DMake(41.000512, -109.050116);
    points[1] = CLLocationCoordinate2DMake(41.002371, -102.052066);
    points[2] = CLLocationCoordinate2DMake(36.993076, -102.041981);
    points[3] = CLLocationCoordinate2DMake(36.99892, -109.045267);

    MKPolygon* poly = [MKPolygon polygonWithCoordinates:points count:4];
    poly.title = @"Colorado";

    [map addOverlay:poly];
```

For an overlay to be shown on the map, the [mapView:viewForOverlay:](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1616210-mapview) method of your map view delegate needs to provide an appropriate overlay renderer. For the standard overlay shapes, you can do this by creating a renderer that matches the type of shape you want to display. Listing 6-10 shows an implementation of this method that creates the polygon renderer used to cover the state of Colorado. In this example, the method sets the colors to use for rendering the shape and the border width.

__Listing 6-10__  Creating a polygon renderer for rendering a shape

```objc
- (MKOverlayRenderer *)mapView:(MKMapView *)mapView viewForOverlay:(id <MKOverlay>)overlay
{
    if ([overlay isKindOfClass:[MKPolygon class]])
    {
        MKPolygonRenderer*    aRenderer = [[MKPolygonRenderer alloc] initWithPolygon:(MKPolygon*)overlay];

        aRenderer.fillColor = [[UIColor cyanColor] colorWithAlphaComponent:0.2];
        aRenderer.strokeColor = [[UIColor blueColor] colorWithAlphaComponent:0.7];
        aRenderer.lineWidth = 3;

        return aRenderer;
    }

    return nil;
}
```

It’s important to remember that the standard overlay renderers simply fill and stroke the shape represented by the overlay. If you want to display additional information, you need to create a custom overlay renderer to do the necessary drawing. You should avoid adding subviews to an existing overlay in an attempt to render any extra content. Any subviews you add to an overlay are scaled along with the overlay itself and made to fit the zoom level of the map. Unless your subviews contain content that also scales well, the results would probably not look very good.

If you use custom bitmap tiles to provide an overlay, you can use [MKTileOverlay](https://developer.apple.com/documentation/mapkit/mktileoverlay) to manage the tiles and [MKTileOverlayRenderer](https://developer.apple.com/documentation/mapkit/mktileoverlayrenderer) to present them. A single `MKTileOverlay` object can handle the tiles for multiple zoom levels, because the class's URL template lets you specify a tile’s map position, zoom level, and scale factor, in addition to its location within the app bundle or on a server.

By default, the upper-left corner of the map is the origin for the tile’s x and y values. (You can use the [geometryFlipped](https://developer.apple.com/documentation/mapkit/mktileoverlay/1452251-isgeometryflipped) property to move the origin to the lower-left corner, but if you want to use a custom indexing scheme, you need to subclass `MKTileOverlay`.) Each zoom level increases or decreases the number of tiles by a power of two. For example, a zoom level of three means that there are eight tiles in both the x and y directions.

To create tiles that match the curvature of the map, use the EPSG:3857 spherical Mercator projection coordinate system.

The job of an overlay object is to manage the coordinate data and any additional information associated with the overlay. Map Kit provides the following options for defining custom overlays:

- Adopting the [MKOverlay](https://developer.apple.com/documentation/mapkit/mkoverlay) protocol in one of your app’s existing classes
- Subclassing [MKShape](https://developer.apple.com/documentation/mapkit/mkshape) or [MKMultiPoint](https://developer.apple.com/documentation/mapkit/mkmultipoint) to define new types of shape-based overlays
- Subclassing [MKTileOverlay](https://developer.apple.com/documentation/mapkit/mktileoverlay) to manage tiles that use a custom indexing scheme

Whether you subclass or adopt the `MKOverlay` protocol, the work you have to do in a custom overlay object is the largely same. The main job of an overlay object is to vend two key pieces of information:

- A coordinate that defines the center point of the overlay
- A bounding rectangle that completely encompasses the overlay’s content

The bounding rectangle is the most important piece of information to the overlay itself. The map view uses the bounding rectangle specified by an overlay object as its cue for when to add the corresponding overlay renderer to the map. (If you add the overlay to the map as an annotation as well, the coordinate value similarly determines when the corresponding annotation view should be added to the map.) The bounding rectangle itself must be specified using map points, not map coordinates. You can convert between the two coordinate systems using the Map Kit functions.

Most of the work involved with displaying an overlay is done by the corresponding overlay renderer object. The overlay object simply defines where on the map the overlay should be placed, whereas the overlay renderer defines the final appearance of the overlay, including what information (if any) is displayed for the overlay. The creation of custom overlay renderers is described further in [Defining a Custom Overlay Renderer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqnrnknltcmy).

If you want to do more than draw the boundaries or fill the content of your overlay shape, you need to create a custom overlay renderer. For example, if you’re drawing a traffic overlay, you could use a custom overlay renderer to color-code each roadway based on its conditions. You can also use custom drawing code to animate your overlay’s appearance.

To create a custom overlay renderer, you must subclass [MKOverlayRenderer](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer). (If you simply want to modify the drawing behavior of an existing shape-based overlay, you can subclass [MKOverlayPathRenderer](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer) instead.)

In your custom implementation of `MKOverlayRenderer`, you should implement the following methods:

- [drawMapRect:zoomScale:inContext:](https://developer.apple.com/documentation/mapkit/mkoverlayview/1613868-drawmaprect) to draw your custom content
- [canDrawMapRect:zoomScale:](https://developer.apple.com/documentation/mapkit/mkoverlayview/1613864-candrawmaprect) if your drawing code depends on content that might not always be available

The `canDrawMapRect:zoomScale:` method is for situations where your content may not always be ready to draw. For example, a traffic overlay would need to download the needed traffic data from the network before it could draw. If you return `NO` from this method, the map view refrains from drawing your overlay until you signal that you are ready. You can do this by marking your view as dirty using either the [setNeedsDisplayInMapRect:](https://developer.apple.com/documentation/mapkit/mkoverlayview/1613866-setneedsdisplayinmaprect) or [setNeedsDisplayInMapRect:zoomScale:](https://developer.apple.com/documentation/mapkit/mkoverlayview/1613876-setneedsdisplayinmaprect) method.

When your view is ready to draw, the map view calls the `drawMapRect:zoomScale:inContext:` method to do the actual drawing. (Note that if you need to perform image processing on tiles as they are being drawn, you should subclass [MKTileOverlayRenderer](https://developer.apple.com/documentation/mapkit/mktileoverlayrenderer).) Unlike drawing in a normal view, drawing in an overlay view requires special considerations:

- In your drawing code, never use the view’s bounds or frame as reference points for drawing. Instead, use the map points associated with the overlay object to define shapes. Immediately before drawing, the code should convert those map points to points ([CGPoint](https://developer.apple.com/documentation/coregraphics/cgpoint) and so on) using the conversion routines found in the [MKOverlayRenderer](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer) class.

  Also, you typically don’t apply the zoom scale value passed to this method directly to your content. Instead, you provide it only when a Map Kit function or method specifically requires it. As long as you specify content using map points and convert to points, your content should be scaled to the correct size automatically.
- If you use UIKit classes and functions to draw, explicitly set up and clean up the drawing environment. Before issuing any calls, call the [UIGraphicsPushContext](https://developer.apple.com/documentation/uikit/1623921-uigraphicspushcontext) function to make the context passed to your method the current context. When you finish drawing, call [UIGraphicsPopContext](https://developer.apple.com/documentation/uikit/1623914-uigraphicspopcontext) to remove that context.
- Remember that the map view may tile large overlays and render each tile on a separate thread. Your drawing code should therefore not attempt to modify variables or other data unless it can do so in a thread-safe manner.

Listing 6-11 shows the drawing code used to fill the bounding rectangle of an overlay using a gradient. When drawing gradients, it is especially important to contain the drawing operation by applying a clipping rectangle to the desired drawing area. The view’s frame is actually larger than the overlay’s bounding rectangle, so without a clipping rectangle, the gradient would render outside the expected area. Because the bounding rectangle of the overlay defines the actual shape in this case, this method simply clips to the bounding rectangle. For more complex overlays, you would want to clip to the path representing your overlay. The results of this drawing code are shown in [Figure 6-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqnrnknltena).

__Listing 6-11__  Drawing a gradient in a custom overlay

```objc
- (void)drawMapRect:(MKMapRect)mapRect zoomScale:(MKZoomScale)zoomScale inContext:(CGContextRef)context
{
   // Get the overlay bounding rectangle.
   MKMapRect  theMapRect = [self.overlay boundingMapRect];
   CGRect theRect = [self rectForMapRect:theMapRect];

   // Clip the context to the bounding rectangle.
   CGContextAddRect(context, theRect);
   CGContextClip(context);

   // Set up the gradient color and location information.
   CGColorSpaceRef myColorSpace = CGColorSpaceCreateDeviceRGB();
   CGFloat locations[4] = {0.0, 0.33, 0.66, 1.0};
   CGFloat components[16] = {0.0, 0.0, 1.0, 0.5,
                             1.0, 1.0, 1.0, 0.8,
                             1.0, 1.0, 1.0, 0.8,
                             0.0, 0.0, 1.0, 0.5};

   // Create the gradient.
   CGGradientRef myGradient = CGGradientCreateWithColorComponents(myColorSpace, components, locations, 4);
   CGPoint start, end;
   start = CGPointMake(CGRectGetMidX(theRect), CGRectGetMinY(theRect));
   end = CGPointMake(CGRectGetMidX(theRect), CGRectGetMaxY(theRect));

   // Draw.
   CGContextDrawLinearGradient(context, myGradient, start, end, 0);

   // Clean up.
   CGColorSpaceRelease(myColorSpace);
   CGGradientRelease(myGradient);
}
```

Figure 6-4 shows the results of drawing custom content over the overlay for the state of Colorado. In this case, the overlay renderer fills its content with a custom gradient.

__Figure 6-4__  Using a custom overlay renderer to draw

!

When it needs an overlay renderer, the map view calls the [mapView:rendererForOverlay:](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452203-mapview) method of its [delegate object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14). If you don’t implement this method—or if you implement it and always return `nil`—the map view doesn’t display anything for the specified overlay. Therefore, you must implement this method and return a valid overlay renderer for any overlays you want displayed on the map.

For the most part, every overlay is different. Although you should always create overlay renderers in your [mapView:rendererForOverlay:](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452203-mapview) method, you may need to be a little more creative in how you configure those objects. If all of your renderers share the same drawing attributes, you can implement this method in a way similar to the one shown in [Listing 6-10](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiojxfvbuqnrnknltcmq). However, if each overlay uses different colors or drawing attributes, you should find a way to initialize that information using the annotation object, rather than having a large decision tree in `mapView:rendererForOverlay:`.

Because overlays are typically different from one another, the map view doesn’t recycle those objects when they are removed from the map. Instead of dequeueing an existing overlay renderer, you must create a new one every time.

If your app works with more than one overlay, you might need to think about how to manage those objects. Like annotations, the overlays associated with a map are always displayed when any portion of the overlay intersects the visible portion of the map. Unlike annotations, overlays scale proportionally with the map and therefore don’t automatically overlap one another. This means that you are less likely to have to remove overlays and add them later to prevent overcrowding. In cases where the bounding rectangles of two overlays do overlap, you can either remove one of the overlays or arrange their Z-order to control which one appears on top.

The [overlays](https://developer.apple.com/documentation/mapkit/mkmapview/1452784-overlays) property of the `MKMapView` class stores the registered overlays in an ordered array. The order of the objects in this array matches the Z-order of the objects at render time, with the first object in the array representing the bottom of the Z-order. To place an overlay on top of all other overlays, you add it to the end of this array. You can also insert objects at different points in the array and exchange the position of two objects in the array using the map view’s methods.

If you decide to implement some type of overlap-detection algorithm for overlays, one place to do so is in the [mapView:didAddOverlayRenderers:](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452609-mapview) method of your map view delegate. When this method is called, use the [MKMapRectIntersectsRect](https://developer.apple.com/documentation/mapkit/1452221-mkmaprectintersectsrect) function to see if the added overlay intersects the bounds of any other overlays. If there is an overlap, use custom logic to choose which one should be placed on top in the rendering tree and exchange their positions as needed. (The comparison logic can occur on any thread, but because the map view is an interface item, any modifications to the `overlays` array should be synchronized and performed on the app’s main thread.)

The [MKOverlay](https://developer.apple.com/documentation/mapkit/mkoverlay) protocol conforms to the [MKAnnotation](https://developer.apple.com/documentation/mapkit/mkannotation) protocol. As a result, all overlay objects are also annotation objects and can be treated as one or both in your code. If you opt to treat an overlay object as both an overlay and an annotation, you are responsible for managing that object in two places. If you want to display both an overlay renderer and annotation view for the object, you must implement both the [mapView:rendererForOverlay:](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452203-mapview) and [mapView:viewForAnnotation:](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452045-mapview) methods in your app delegate. You must also add and remove the object from both the [overlays](https://developer.apple.com/documentation/mapkit/mkmapview/1452784-overlays) and [annotations](https://developer.apple.com/documentation/mapkit/mkmapview/1452593-annotations) arrays of your map.

[Next](Providing%20Directions.md)[Previous](Displaying%20Maps.md)

