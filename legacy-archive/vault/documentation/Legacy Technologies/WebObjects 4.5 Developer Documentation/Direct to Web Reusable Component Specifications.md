---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/ReusableComponents/Introduction.html
archived_at: '2026-07-15T08:11:31.425884Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

[![Table of Contents](attachments/images/up.gif)](../DirectToWebTOC.md)

# Direct to Web Reusable Component Specifications

## Introduction

The Direct to Web reusable components perform the basic tasks
provided by the Direct to Web framework: editing objects, inspecting
objects, listing objects, querying for objects, and selecting objects from
a list. You can embed a Direct to Web reusable component within
your WebObjects component to perform these tasks. The "Customizing
a Direct to Web Application" chapter of _Developing WebObjects Applications
With Direct to Web_ shows you how.

The Direct to Web framework defines five Direct to Web reusable
components:

: [D2WEdit](D2WEdit.md#apple-ijaucq2eineei)
: [D2WInspect](D2WInspect.md#apple-ijaucq2eineei)
: [D2WList](D2WList.md#apple-ijaucq2eineei)
: [D2WQuery](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/ReusableComponents/D2WQuery.html#BAACDCHD)
: [D2WSelect](D2WSelect.md#apple-ijaucq2eineei)

## How to Use These Specifications

Each component specification that follows is divided into
three sections: a synopsis, a description, and a set of bindings.
The synopsis is designed to give you ready reference to the element's
attributes, showing which ones are mandatory and which ones optional.
The description explains the purpose of the element. Finally, the
bindings describe in detail each of the component's attributes.

The synopses use several conventions that you should be aware
of. For example:

> ```
> WOSubmitButton { action=submitForm; value=aString; [disabled=YES|NO;] [name=aName;] };
> ```

- _Italic_ denotes
  words that represent something else or that can be varied. For example, _submitForm_ represents
  a method in your script-the exact name of the method is your choice.
- Square brackets ([ ]) mean that the enclosed attribute or
  attributes are optional. The name attribute and its value are optional
  in the synopsis above.
- A vertical bar (|) separates two options that are mutually
  exclusive, as in `disabled=YES|NO` where the
  attribute's value must be either `YES` or `NO`.
- The remaining words or characters are to be taken literally
  (that is, they should be typed as they appear). For example, the __action__ and __value__ attributes
  are to be taken literally in the synopsis above.

[![Table of Contents](attachments/images/up.gif)](../DirectToWebTOC.md)
