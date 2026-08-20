---
title: Apple URL Scheme Reference
apple_id: TP40007899
resource_type: Guide
platform: watchOS|Safari (Mobile)|Safari|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/MapLinks/MapLinks.html
archived_at: '2026-07-18T02:29:23.291318Z'
---
> 导航：[总目录](../../README.md) · [featuredarticles](../../_indexes/featuredarticles.md) · [Apple URL Scheme Reference](About%20Apple%20URL%20Schemes.md)


[Next](iTunes%20Links.md)[Previous](SMS%20Links.md)

# Map Links

The maps URL scheme is used to show geographical locations and to generate driving directions between two points. If your app includes address or location information, you can use map links to open that information in the Maps app in iOS or macOS.

Unlike some schemes, map URLs do not start with a “maps” scheme identifier. Instead, map links are specified as regular `http` links and are opened either in Safari or the Maps app on the target platform.

Table 5-1 lists the supported parameters along with a brief description of each.

__Table 5-1__  Supported Apple Maps parameters

| Parameter | Meaning | Values |
| `t` | The map type. If you don’t specify one of the documented values, the current map type is used. | - `m` (standard view) - `k` (satellite view) - `h` (hybrid view) - `r` (transit view) |
| `q` | The query. This parameter is treated as if its value had been typed into the Maps search field by the user. Note that `q=*` is not supported  The `q` parameter can also be used as a label if the location is explicitly defined in the `ll` or `address` parameters. | A URL-encoded string that describes the search object, such as “pizza,” or an address to be geocoded |
| `address` | The address. Using the address parameter simply displays the specified location, it does not perform a search for the location. | An address string that geolocation can understand. |
| `near` | A hint used during search. If the `sll` parameter is missing or its value is incomplete, the value of `near` is used instead. | A comma-separated pair of floating point values that represent latitude and longitude (in that order). |
| `ll` | The location around which the map should be centered.  The `ll` parameter can also represent a pin location when you use the `q` parameter to specify a name. | A comma-separated pair of floating point values that represent latitude and longitude (in that order). |
| `z` | The zoom level. You can use the `z` parameter only when you also use the `ll` parameter; in particular, you can’t use `z` in combination with the `spn` or `sspn` parameters. | A floating point value between `2` and `21` that defines the area around the center point that should be displayed. |
| `spn` | The area around the center point, or _span_. The center point is specified by the `ll` parameter.  You can’t use the `spn` parameter in combination with the `z` parameter. | A coordinate span (see [MKCoordinateSpan](https://developer.apple.com/documentation/mapkit/mkcoordinatespan)) denoting a latitudinal delta and a longitudinal delta. |
| `saddr` | The source address to be used as the starting point for directions.  A complete directions request includes the `saddr`, `daddr`, and `dirflg` parameters, but only the `daddr` parameter is required. If you don’t specify a value for `saddr`, the starting point is “here.” | An address string that geolocation can understand. |
| `daddr` | The destination address to be used as the destination point for directions.  A complete directions request includes the `saddr`, `daddr`, and `dirflg` parameters, but only the `daddr` parameter is required. | An address string that geolocation can understand. |
| `dirflg` | The transport type.  A complete directions request includes the `saddr`, `daddr`, and `dirflg` parameters, but only the `daddr` parameter is required. If you don’t specify one of the documented transport type values, the `dirflg` parameter is ignored; if you don’t specify any value, Maps uses the user’s preferred transport type or the previous setting. | - `d` (by car) - `w` (by foot) - `r` (by public transit) |
| `sll` | The search location. You can specify the `sll` parameter by itself or in combination with the `q` parameter. For example, `http://maps.apple.com/?sll=50.894967,4.341626&z=10&t=s` is a valid query. | A comma-separated pair of floating point values that represent latitude and longitude (in that order). |
| `sspn` | The screen span. Use the `sspn` parameter to specify a span around the search location specified by the `sll` parameter. | A coordinate span (see [MKCoordinateSpan](https://developer.apple.com/documentation/mapkit/mkcoordinatespan)) denoting a latitudinal delta and a longitudinal delta. |

You can use the maps URL scheme to help the user:

- Perform a search
- Get directions to a location
- View a specific location

To perform a search, supply a properly encoded URL string as the value of the `q` parameter. For example:

```
http://maps.apple.com/?q=Mexican+Restaurant
```

To specify a location for search, you can supply a value for the `near` parameter, or combine the `sll` parameter with either the `z` or `sspn` parameters. You can also set the map type using the `t` parameter, as shown here:

```
http://maps.apple.com/?q=Mexican+Restaurant&sll=50.894967,4.341626&z=10&t=s
```

To provide navigation directions from one location to another, supply the start and destination addresses in the `saddr` and `daddr` parameters as shown below. You can also supply much more detail for the start and destination addresses than is shown here.

```
http://maps.apple.com/?saddr=Cupertino&daddr=San+Francisco
```

To specify a transport type, you can use the `dirflg` parameter as shown here:

```
http://maps.apple.com/?saddr=San+Jose&daddr=San+Francisco&dirflg=r
```

You can omit the start address when you want to provide directions “from here.” The following example shows a search from here that provides driving directions in a hybrid map.

```
http://maps.apple.com/?daddr=San+Francisco&dirflg=d&t=h
```

To display a specific location, use the `ll` parameter to center the map at the specified position as shown here:

```
http://maps.apple.com/?ll=50.894967,4.341626
```

Another way to display a location is to specify an address, such as:

```
http://maps.apple.com/?address=1,Infinite+Loop,Cupertino,California
```

If you use both the `ll` and `address` parameters, `ll` takes precedence over `address`. If you include a name in the value of the `q` parameter, Maps tries to match the name at the specified location.

[Next](iTunes%20Links.md)[Previous](SMS%20Links.md)

