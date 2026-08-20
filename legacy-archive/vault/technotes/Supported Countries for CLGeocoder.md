---
title: Supported Countries for CLGeocoder
apple_id: DTS40011305
resource_type: Technical Note
platform: watchOS|iOS
topic: null
technology: CoreLocation
published: '2011-10-12'
source_url: https://developer.apple.com/library/archive/technotes/tn2289/_index.html
archived_at: '2026-07-26T19:54:10.114590Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2289

# Supported Countries for CLGeocoder

Support for reverse geocoding a location and geocoding an address using the `CLGeocoder` class varies depending on the availability and granularity of map data by region around the globe. This document describes the regions that are currently supported by CLGecocoder. Inclusion of a region on the lists indicates that address lookup is generally supported. In some cases regions or specific addresses in a supported region may be unavailable.

[Supported Regions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzqguwugsbrfvke4vcbi4za)[Partially Supported Regions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzqguwugsbrfvke4vcbi4zq)[References](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzqguwugsbrfvke4vcbi42a)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmzqguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Supported Regions

Worldwide coverage is continually improving for `CLGeocoder`. The following regions currently have full support:

- Australia
- Austria
- Belgium
- Canada
- Croatia
- Denmark
- Estonia
- Finland
- France
- Germany
- Greece
- Hungary
- Italy
- Japan
- Latvia
- Liechtenstein
- Lithuania
- Luxembourg
- Netherlands
- New Zealand
- Norway
- Poland
- Singapore
- Slovakia
- Slovenia
- Spain
- Sweden
- Switzerland
- United Kingdom
- United States

[Back to Top](#)

## Partially Supported Regions

The following are territories are not fully supported, either because coverage is more limited or for other reasons. For example a location may only be able to be geocoded to road level as opposed to a specific address point on that road.

- Andorra
- Argentina
- Bulgaria
- Chile
- China
- Czech Republic
- Hong Kong
- Indonesia
- Ireland
- Macau
- Mexico
- Morocco
- Portugal
- Romania
- Taiwan
- Thailand
- Turkey

[Back to Top](#)

## References

`CLGeocoder` Class Reference

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-10-04 | New document that describes the regions that are currently supported by CLGecocoder. |

