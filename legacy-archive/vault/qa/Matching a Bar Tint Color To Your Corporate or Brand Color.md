---
title: Matching a Bar Tint Color To Your Corporate or Brand Color
apple_id: DTS40014219
resource_type: QA
platform: iOS
topic: User Experience
technology: UIKit
published: '2014-03-20'
source_url: https://developer.apple.com/library/archive/qa/qa1808/_index.html
archived_at: '2026-07-18T02:34:53.279119Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1808

# Matching a Bar Tint Color To Your Corporate or Brand Color

## Q:  How do I select a bar tint color which will match my corporate or brand color?

A: Beginning with iOS 7, navigation bars, tab bars, and tool bars (henceforth referred to as 'bars') are configured to be translucent by default. A translucent bar mixes its `barTintColor` with gray before combining it with a system-defined alpha value to produce the final background color that is used to composite the bar with the content it overlies. This presents a challenge for developers who want to maintain a consistent color scheme in their apps because they must account for the color of the content passing underneath a translucent bar when selecting a bar tint color. Recent updates to iOS 7 have helped alleviate this problem by increasing the system-defined alpha value mentioned previously. The result is that bars with a custom bar tint color appear more opaque, giving developers better control over the final color produced by compositing the bar with the content underneath it.

To compute a bar tint color to match a given color (e.g. for a corporate or brand identity), the color you pass to the -setBarTintColor: method will need to account for the translucency iOS maintains for the bar. Also note that the alpha channel for the color you pass will be ignored, since iOS controls for that to achieve the overall translucency effect.

Arriving at the correct color for tinted bars may require some experimentation. You may also need to take into account the app content which passes under the bar (e.g. photos or text).

A starting point is to darken each of the RGB channels in your bar color by 0.12. For example:

__Listing 1__  Computing a bar tint color from a given color.

```
UIColor *corporateColor = [UIColor colorWithRed:0.20 green:0.40 blue:0.20 alpha:1.0];
UIColor *barTintColor = [UIColor colorWithRed:0.08 green:0.28 blue:0.08 alpha:1.0];
```

If the starting color in a channel is already less than 0.12, you may need to darken the other channels by more than 0.12, like so:

__Listing 2__  Computing a bar tint color from a given color with one or more channels that are close to zero.

```
UIColor *corporateColor = [UIColor colorWithRed:0.04 green:0.40 blue:0.20 alpha:1.0];
UIColor *barTintColor = [UIColor colorWithRed:0.00 green:0.24 blue:0.04 alpha:1.0];
```

Again, you may need to experiment with more or less darkening to get the exact effect you're trying to achieve.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-03-20 | New document that describes how to select an appropriate bar tint color to match your corporate or brand color. |

