---
title: Safari CSS Reference
apple_id: TP40002050
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: User Experience
technology: WebKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariCSSRef/Articles/ExplanationofTerms.html
archived_at: '2026-07-15T05:19:01.148977Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari CSS Reference](Introduction%20to%20Safari%20CSS%20Reference.md)


[Next](Supported%20CSS%20Properties.md)[Previous](Introduction%20to%20Safari%20CSS%20Reference.md)

# Explanation of Terms

This reference uses CSS-specific terminology in its headings within a property description. This article describes these terms and explains their meanings and possible values.

__Syntax__ describes the syntax of a CSS property. If a property can have multiple forms, each form appears in its own line.

__Types Allowed__ contains information about what numeric types are allowed in a given property. This field is omitted from properties that do not have a single numeric type, such as properties that take multiple values or use nonnumeric constants exclusively.

The Types Allowed field does not present the complete story, however, because a property may also take additional types specific to its subproperties.

__Constants__ contains a list of special nonnumeric values that you can assign to a specific property. For example, the `border-width` property can take the value `caption`.

The Constants field does not present the complete story, however, because a property may also take additional values specific to its subproperties.

__Subproperties__ provides a list of properties that make up a larger property.

There are three basic types of properties: simple properties, convenience properties, and composite properties.

- Simple properties take a single value of a single type (or a single named constant, such as `thin`).
- Convenience properties (`border-width`, for example) combine multiple properties of the same type into a single value. Many also allow you to optionally set distinct values for each of the included properties.
- Composite properties (`border`, for example) take multiple values of different types.

Convenience properties, such as `border-width`, have related subproperties with finer granularity. For example, instead of setting the `border-width` property, you could set the `border-bottom-width`, `border-top-width`, `border-left-width`, and `border-right-width` properties to the same value and achieve the same result.

Because these convenience properties can be broken down into subproperties of the same basic type, any value that is legal for all of the subproperties is also legal for the convenience property as a whole if the property has a single-value form, and for the individual parts if the property has a multiple-value form. For example, the `border-width` property can accept the value `thin` even though it is listed only in related subproperties such as `border-bottom-width`. Similarly, you could use a multiple-value form, such as `border-width: thin thin thin thin`.

Composite properties also have related subproperties. For example, the second parameter in the `border` property is equivalent to the `border-width` property. Thus, any value that is appropriate for the `border-width` property is also appropriate for the width portion of the `border` composite property.

Similarly, the types allowed for a subproperty are also allowed for convenience properties and the appropriate portions of composite properties that contain them.

__Availability__ gives the version of Safari in which the property first appeared. If no availability is listed you can assume the property has been supported for both Safari and iOS for several releases.

__Support Level__ specifies the revision of the W3C standard in which a given property is defined, where applicable, and provides the overall status of the property for properties that are not part of a W3C standard. The possible values are:

- CSS 2.1—properties in CSS 2.1 and earlier revisions. These properties are fully supported across most major browsers, including Safari and other applications that use WebKit.
- Stable CSS 3—properties new in CSS version 3 but believed to be stable. Apple is committed to supporting these properties going forward and does not expect their syntax or names to change. Unlike more experimental CSS 3 properties, these properties are not prefixed by `-webkit-`, and many are supported by other browsers such as Internet Explorer or Firefox.
- Apple extension—properties defined by Apple. These properties are fully supported by WebKit and Safari. A few of these extensions, where noted, are specific to Dashboard widgets or Safari on iOS. Some of these extensions may have been submitted to the W3C CSS working group for standardization, but are not currently part of the latest draft standard.
- Experimental CSS 3—properties new in CSS 3. The syntax for these properties may change, but because they are prefixed by `-webkit-`, Apple believes that the current syntax can be supported going forward. You still need to update these properties to the final CSS 3 syntax (as needed) and remove the `-webkit-` prefix if you need to use them on other browsers.
- Under development—new CSS 3 or Apple extension properties that are likely to change in syntax. Although it is OK to use these, support for these properties may change in incompatible ways in the future.

Properties may be upgraded to more stable categories as time passes, particularly as tags are added to relevant standards. Go to [http://webkit.org/specs](http://webkit.org/specs) for current W3C proposals.

[Next](Supported%20CSS%20Properties.md)[Previous](Introduction%20to%20Safari%20CSS%20Reference.md)

