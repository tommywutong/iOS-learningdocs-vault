---
title: Core Image Programming Guide
apple_id: TP30001185
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: CoreImage
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_concepts/ci_concepts.html
archived_at: '2026-07-15T07:35:30.261886Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Image Programming Guide](About%20Core%20Image.md)


[Next](Subclassing%20CIFilter-%20Recipes%20for%20Custom%20Effects.md)[Previous](Auto%20Enhancing%20Images.md)

# Querying the System for Filters

Core Image provides methods that let you query the system for the available built-in filters and the associated information about each filter—display name, input parameters, parameter types, defaults values, and so on. Querying the system provides you with the most up-to-date information about available filters. If your app supports letting users choose and set filters, you can use this information when creating a user interface for a filter.

Use the [filterNamesInCategory:](https://developer.apple.com/documentation/coreimage/cifilter/1438145-filternames) and [filterNamesInCategories:](https://developer.apple.com/documentation/coreimage/cifilter/1437595-filternamesincategories) methods to discover exactly which filters are available. Filters are categorized to make the list more manageable. If you know a filter category, you can find out the filters available for that category by calling the method [filterNamesInCategory:](https://developer.apple.com/documentation/coreimage/cifilter/1438145-filternames) and supplying one of the category constants listed in Table 4-1, [Table 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqmrnknltk), or [Table 4-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqmrnknltm).

If you want to find all available filters for a list of categories, you can call the method [filterNamesInCategories:](https://developer.apple.com/documentation/coreimage/cifilter/1437595-filternamesincategories), supplying an array of category constants from those listed in the tables. The method returns an `NSArray` object populated with the filter names for each category. You can obtain a list of all filters for all categories by supplying `nil` instead of an array of category constants.

A filter can be a member of more than one category. A category can specify:

- The type of effect produced by the filter (color adjustment, distortion, and so forth). See Table 4-1.
- The usage of the filter (still image, video, high dynamic range, and so forth). See [Table 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqmrnknltk).
- Whether the filter is provided by Core Image (built-in). See [Table 4-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqmrnknltm).

__Table 4-1__  Filter category constants for effect types

| Effect type | Indicates |
| `kCICategoryDistortionEffect` | Distortion effects, such as bump, twirl, hole |
| `kCICategoryGeometryAdjustment` | Geometry adjustment, such as affine transform, crop, perspective transform |
| `kCICategoryCompositeOperation` | Compositing, such as source over, minimum, source atop, color dodge blend mode |
| `kCICategoryHalftoneEffect` | Halftone effects, such as screen, line screen, hatched |
| `kCICategoryColorAdjustment` | Color adjustment, such as gamma adjust, white point adjust, exposure |
| `kCICategoryColorEffect` | Color effect, such as hue adjust, posterize |
| `kCICategoryTransition` | Transitions between images, such as dissolve, disintegrate with mask, swipe |
| `kCICategoryTileEffect` | Tile effect, such as parallelogram, triangle |
| `kCICategoryGenerator` | Image generator, such as stripes, constant color, checkerboard |
| `kCICategoryGradient` | Gradient, such as axial, radial, Gaussian |
| `kCICategoryStylize` | Stylize, such as pixellate, crystallize |
| `kCICategorySharpen` | Sharpen, luminance |
| `kCICategoryBlur` | Blur, such as Gaussian, zoom, motion |

__Table 4-2__  Filter category constants for filter usage

| Use | Indicates |
| `kCICategoryStillImage` | Can be used for still images |
| `kCICategoryVideo` | Can be used for video |
| `kCICategoryInterlaced` | Can be used for interlaced images |
| `kCICategoryNonSquarePixels` | Can be used for nonsquare pixels |
| `kCICategoryHighDynamicRange` | Can be used for high-dynamic range pixels |

__Table 4-3__  Filter category constants for filter origin

| Filter origin | Indicates |
| `kCICategoryBuiltIn` | A filter provided by Core Image |

After you obtain a list of filter names, you can retrieve the attributes for a filter by creating a `CIFilter` object and calling the method [attributes](https://developer.apple.com/documentation/coreimage/cifilter/1437661-attributes) as follows:

```
CIFilter *myFilter = [CIFilter filterWithName:@"<# Filter Name Here #>"];
NSDictionary *myFilterAttributes = [myFilter attributes];
```

You replace the string "`<# Filter Name Here #>`" with the name of the filter you are interested in. Attributes include such things as name, categories, class, minimum, and maximum. See _[CIFilter Class Reference](https://developer.apple.com/documentation/coreimage/cifilter)_ for the complete list of attributes that can be returned.

If your app provides a user interface, it can consult a filter dictionary to create and update the user interface. For example, filter attributes that are Boolean would require a checkbox or similar user interface element, and attributes that vary continuously over a range could use a slider. You can use the maximum and minimum values as the basis for text labels. The default attribute setting would dictate the initial setting in the user interface.

Filter names and attributes provide all the information you need to build a user interface that allows users to choose a filter and control its input parameters. The attributes for a filter tell you how many input parameters the filter has, the parameter names, the data type, and the minimum, maximum, and default values.

Listing 4-1 shows code that gets filter names and builds a dictionary of filters by functional categories. The code retrieves filters in these categories—`kCICategoryGeometryAdjustment`, `kCICategoryDistortionEffect`, `kCICategorySharpen`, and `kCICategoryBlur`—but builds the dictionary based on app-defined functional categories, such as Distortion and Focus. Functional categories are useful for organizing filter names in a menu that makes sense for the user. The code does not iterate through all possible Core Image filter categories, but you can easily extend this code by following the same process.

__Listing 4-1__  Code that builds a dictionary of filters by functional categories

```
NSMutableDictionary *filtersByCategory = [NSMutableDictionary dictionary];

NSMutableArray *filterNames = [NSMutableArray array];
[filterNames addObjectsFromArray:
    [CIFilter filterNamesInCategory:kCICategoryGeometryAdjustment]];
[filterNames addObjectsFromArray:
    [CIFilter filterNamesInCategory:kCICategoryDistortionEffect]];
filtersByCategory[@"Distortion"] = [self buildFilterDictionary: filterNames];

[filterNames removeAllObjects];
[filterNames addObjectsFromArray:
    [CIFilter filterNamesInCategory:kCICategorySharpen]];
[filterNames addObjectsFromArray:
    [CIFilter filterNamesInCategory:kCICategoryBlur]];
filtersByCategory[@"Focus"] = [self buildFilterDictionary: filterNames];
```

Listing 4-2 shows the `buildFilterDictionary` routine called in Listing 4-1. This routine builds a dictionary of attributes for each of the filters in a functional category. A detailed explanation for each numbered line of code follows the listing.

__Listing 4-2__  Building a dictionary of filters by functional name

```objc
- (NSMutableDictionary *)buildFilterDictionary:(NSArray *)filterClassNames  // 1
{
    NSMutableDictionary *filters = [NSMutableDictionary dictionary];
    for (NSString *className in filterClassNames) {                         // 2
        CIFilter *filter = [CIFilter filterWithName:className];             // 3

        if (filter) {
            filters[className] = [filter attributes];                       // 4
        } else {
            NSLog(@"could not create '%@' filter", className);
        }
    }
    return filters;
}
```

Here’s what the code does:

1. Takes an array of filter names as an input parameter. Recall from [Listing 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobvfvbuqmrnknlto) that this array can be a concatenation of filter names from more than one Core Image filter category. In this example, the array is based upon functional categories set up by the app (Distortion or Focus).
2. Iterates through the array of filter names.
3. Retrieves the filter object for the filter name.
4. Retrieves the attributes dictionary for a filter and adds it to the dictionary returned by the routine.

[Next](Subclassing%20CIFilter-%20Recipes%20for%20Custom%20Effects.md)[Previous](Auto%20Enhancing%20Images.md)

