---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.14.html
archived_at: '2026-07-15T07:59:25.020081Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.13.md) | [Back Up One Level](CSJ_Tutorial.13.md) | [Next](CSJ_Tutorial.15.md)

###  Formatting Currency Values and Dates

When an attribute is defined in your model as having the internal type Number, a currency formatter is automatically added to any control with which the attribute is associated. Likewise, when an attribute has an NSGregorianDate type, date formatters are added to controls associated with it.

Not all adaptors map, say, the __budget__
attribute to the Number data type. In that case, you won't automatically get currency formatting in the column. You can fix this problem either by setting __budget__
's internal type to be Number in the model, or you can add a currency formatter to the column (as described in [Writing Derived Methods](CSJ_Tutorial.23.md#apple-ge4dgmzq)
).

Once a control has a formatter, you can use the Inspector to change it.

__6. Set field formatting.__

> Select the __Budget__
> column head in the table view, and display the Formatter view of the NSTableColumn Inspector.
>
> 
>
> Change the format to a standard currency format.
>
> ###### 
>
> !
>
> 
>
> Do not set the format to show negative values in red. The JFC currently does not implement colored text.
>
> ---
>
> \xA9 1999 Apple Computer, Inc.
>
> [Previous](CSJ_Tutorial.13.md) | [Back Up One Level](CSJ_Tutorial.13.md) | [Next](CSJ_Tutorial.15.md)
>
> 
>
> Copyright © 2016 Apple Inc. All rights reserved.
>
> - [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
> - [Privacy Policy](http://www.apple.com/privacy/)
