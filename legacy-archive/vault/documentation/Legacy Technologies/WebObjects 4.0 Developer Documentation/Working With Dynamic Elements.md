---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DynamicElements1.html
archived_at: '2026-07-15T08:01:43.159593Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](Palettes.md)

# Working With Dynamic Elements

---

## Introduction to Dynamic Elements

A _dynamic element_ is an element whose exact HTML representation isn't determined until run time. Dynamic elements are represented in the HTML template by the tag <WEBOBJECT>.
There are several types of dynamic elements that you can use in your WebObjects applications. Some of them (such as dynamic forms or images) have counterparts in standard HTML (<FORM> and <IMG>) and are always translated into those counterparts at run time. Others (such as conditionals and repetitions) are _abstract_ dynamic elements, which don't translate directly into HTML but control the generation of other elements.
This chapter describes the techniques you use to add dynamic elements to your components and to bind them to variables and methods in your code. For more information on programming with dynamic elements, see "Dynamic Elements"in the [_WebObjects Developer's Guide_](The%20WebObjects%20Developer%27s%20Guide.md). For details about specific dynamic elements, see the [_Dynamic Elements Reference_](Dynamic%20Element%20Specifications.md).

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](Attributes.md)
