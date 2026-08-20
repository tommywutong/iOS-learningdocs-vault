---
title: Location and Maps Programming Guide
apple_id: TP40009497
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: User Experience
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/EnablingSearch/EnablingSearch.html
archived_at: '2026-07-18T02:12:01.573803Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Location and Maps Programming Guide](About%20Location%20Services%20and%20Maps.md)


[Next](Document%20Revision%20History.md)[Previous](Providing%20Directions.md)

# Enabling Search

To support searches based on user-entered queries, Map Kit provides the [MKLocalSearch](https://developer.apple.com/documentation/mapkit/mklocalsearch) API. Apps can use this API to perform searches for locations that users describe by name, address, or type, such as coffee or theater.

Although local search and geocoding are similar, they support different use cases. Use geocoding when you want to convert between map coordinates and a structured address, such as an Address Book address. Use local search when you want to find a set of locations that match the user’s input.

To search for a location that matches the query a user types into a search field:

1. Create an [MKLocalSearchRequest](https://developer.apple.com/documentation/mapkit/mklocalsearch/request) object and specify a string that contains the user’s natural-language query.

   (Optional) Define a geographical region to narrow the search results. It’s recommended that you define a region to ensure that the user gets relevant results.
2. Create an [MKLocalSearch](https://developer.apple.com/documentation/mapkit/mklocalsearch) object and initialize it with the search request you created in step 1.
3. Start the search by calling [startWithCompletionHandler:](https://developer.apple.com/documentation/mapkit/mklocalsearch/1452652-startwithcompletionhandler) and specifying a completion handler block to process the results.

Each `MKLocalSearch` object performs only one search; if you want to perform multiple searches, you have to define multiple search requests and use them to create multiple search objects. Because the search is performed asynchronously, you can create and begin multiple searches in parallel and handle the results as they arrive.

The results of a local search are provided as a set of [MKMapItem](https://developer.apple.com/documentation/mapkit/mkmapitem) objects. Each map item object contains the following attributes:

- The map coordinates of the location
- A structured address that represents the location
- If the location is a business, the name, phone number, and URL associated with the business might be available

Listing 8-1 shows one way to create a search request, initiate a local search, and display the results as annotations on a map.

__Listing 8-1__  Searching for locations that match the user’s input

```
// Create and initialize a search request object.
MKLocalSearchRequest *request = [[MKLocalSearchRequest alloc] init];
request.naturalLanguageQuery = query;
request.region = self.map.region;

// Create and initialize a search object.
MKLocalSearch *search = [[MKLocalSearch alloc] initWithRequest:request];

// Start the search and display the results as annotations on the map.
[search startWithCompletionHandler:^(MKLocalSearchResponse *response, NSError *error)
{
   NSMutableArray *placemarks = [NSMutableArray array];
   for (MKMapItem *item in response.mapItems) {
      [placemarks addObject:item.placemark];
   }
   [self.map removeAnnotations:[self.map annotations]];
   [self.map showAnnotations:placemarks animated:NO];
}];
```

[Next](Document%20Revision%20History.md)[Previous](Providing%20Directions.md)

