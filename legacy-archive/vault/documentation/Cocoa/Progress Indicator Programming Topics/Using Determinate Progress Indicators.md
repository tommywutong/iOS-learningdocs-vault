---
title: Progress Indicator Programming Topics
apple_id: 10000024i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2002-11-12'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgIndic/Tasks/DeterProgIndic.html
archived_at: '2026-07-15T07:17:50.541213Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Progress Indicator Programming Topics](Introduction%20to%20Progress%20Indicators.md)


[Next](Using%20Indeterminate%20Progress%20Indicators.md)[Previous](About%20Progress%20Indicators.md)

# Using Determinate Progress Indicators

By default, a progress indicator is indeterminate. Your can specify a determinate progress indicator when you set up the view with Interface Builder, or you can use code like the following example to change the default value programmatically:

```
[myProgressIndicatorView setIndeterminate:FALSE];
```

For a determinate progress indicator, invoke the `incrementBy:` method to advance the progress bar. By default, a determinate progress indicator goes from 0.0 to 100.0. You can increment by any amount, but if you vary the increment too widely, progress may appear uneven or jerky. You typically choose an increment value that evenly divides 100.0. For example, you might invoke `incrementBy:` 50 times, incrementing by 2.0 each time, to draw the complete progress bar. To set the value directly, use `setDoubleValue:`. To modify the default range of 0.0 to 100.0, you can invoke `setMinValue:` to modify the minimum value and `setMaxValue:` to modify the maximum value.

After each invocation of `incrementBy:`, you can invoke the `displayIfNeeded` method to ensure immediate redrawing.

[Next](Using%20Indeterminate%20Progress%20Indicators.md)[Previous](About%20Progress%20Indicators.md)

