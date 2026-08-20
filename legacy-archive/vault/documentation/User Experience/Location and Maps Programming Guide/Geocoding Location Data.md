---
title: Location and Maps Programming Guide
apple_id: TP40009497
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: User Experience
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/UsingGeocoders/UsingGeocoders.html
archived_at: '2026-07-18T02:12:07.662495Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Location and Maps Programming Guide](About%20Location%20Services%20and%20Maps.md)


[Next](Displaying%20Maps.md)[Previous](Getting%20the%20Heading%20and%20Course%20of%20a%20Device.md)

# Geocoding Location Data

Location data is usually returned as a pair of numerical values that represent the latitude and longitude of the corresponding point on the globe. These coordinates offer a precise and easy way to specify location data in your code but they aren’t very intuitive for users. Instead of global coordinates, users are more likely to understand a location that is specified using information they are more familiar with such as street, city, state, and country information. For situations where you want to display a user friendly version of a location, you can use a geocoder object to get that information.

A _geocoder object_ uses a network service to convert between latitude and longitude values and a user-friendly _placemark_, which is a collection of data such as the street, city, state, and country information. _Reverse geocoding_ is the process of converting a latitude and longitude into a placemark; _forward geocoding_ is the process of converting place name information into latitude and longitude values. Reverse geocoding is supported in all versions of iOS, but forward geocoding is supported only in iOS 5.0 and later. Both reverse and forward geocoding are supported in OS X v10.8 and later.

Because geocoders rely on a network service, a live network connection must be present in order for a geocoding request to succeed. If a device is in Airplane mode or the network is currently not configured, the geocoder can’t connect to the service it needs and must therefore return an appropriate error. Here are some rules of thumb for creating geocoding requests:

- Send at most one geocoding request for any one user action.
- If the user performs multiple actions that involve geocoding the same location, reuse the results from the initial geocoding request instead of starting individual requests for each action.
- When you want to update the location automatically (such as when the user is moving), reissue the geocoding request only when the user's location has moved a significant distance and after a reasonable amount of time has passed. In general, you shouldn’t send more than one geocoding request per minute.
- Don’t start a geocoding request if the user won’t see the results immediately. For example, don’t start a request if your app is in the background or was interrupted and is currently in the inactive state.

To initiate a reverse-geocoding request using the `CLGeocoder` class, create an instance of the class and call the [reverseGeocodeLocation:completionHandler:](https://developer.apple.com/documentation/corelocation/clgeocoder/1423621-reversegeocodelocation) method. The geocoder object initiates the reverse geocoding request asynchronously and delivers the results to the [block object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3) you provide. The block object is executed whether the request succeeds or fails. In the event of a failure, an error object is passed to the block indicating the reason for the failure.

Listing 4-1 shows an example of how to reverse geocode a point on the map. The only code specific to the geocoding request are the first few lines, which allocate the geocoder object as needed and call the `reverseGeocodeLocation:completionHandler:` method to start the reverse-geocoding operation. (The `geocoder` variable represents a member variable used to store the geocoder object.) The rest of the code is specific to the sample app itself. In this case, the sample app stores the placemark with a custom annotation object (defined by the `MapLocation` class) and adds a button to the callout of the corresponding annotation view.

__Listing 4-1__  Geocoding a location using `CLGeocoder`

```objc
@implementation MyGeocoderViewController (CustomGeocodingAdditions)
- (void)geocodeLocation:(CLLocation*)location forAnnotation:(MapLocation*)annotation
{
    if (!geocoder)
        geocoder = [[CLGeocoder alloc] init];

    [geocoder reverseGeocodeLocation:location completionHandler:
        ^(NSArray* placemarks, NSError* error){
            if ([placemarks count] > 0)
            {
                annotation.placemark = [placemarks objectAtIndex:0];

                // Add a More Info button to the annotation's view.
                MKPinAnnotationView* view = (MKPinAnnotationView*)[map viewForAnnotation:annotation];
                if (view && (view.rightCalloutAccessoryView == nil))
                {
                    view.canShowCallout = YES;
                    view.rightCalloutAccessoryView = [UIButton buttonWithType:UIButtonTypeDetailDisclosure];
                }
            }
    }];
}
@end
```

The advantage of using a block object in a sample like this is that information (such as the annotation object) can be easily captured and used as part of the completion handler. Without blocks, the process of wrangling data variables becomes much more complicated.

Use the [CLGeocoder](https://developer.apple.com/documentation/corelocation/clgeocoder) class with a dictionary of Address Book information or a simple string to initiate forward-geocoding requests. There is no designated format for string-based requests: Delimiter characters are welcome, but not required, and the geocoder server treats the string as case-insensitive. For example, any of the following strings would yield results:

- "Apple Inc”
- "1 Infinite Loop”
- "1 Infinite Loop, Cupertino, CA USA”

The more information you can provide to the forward geocoder, the better the results returned to you. The geocoder object parses the information you give it and if it finds a match, returns some number of placemark objects. The number of returned placemark objects depends greatly on the specificity of the information you provide. For this reason, providing street, city, province, and country information is much more likely to return a single address than providing only street and city information. The completion handler block you pass to the geocoder should be prepared to handle multiple placemarks, as shown below.

```
[geocoder geocodeAddressString:@"1 Infinite Loop"
     completionHandler:^(NSArray* placemarks, NSError* error){
         for (CLPlacemark* aPlacemark in placemarks)
         {
             // Process the placemark.
         }
}];
```

[Next](Displaying%20Maps.md)[Previous](Getting%20the%20Heading%20and%20Course%20of%20a%20Device.md)

