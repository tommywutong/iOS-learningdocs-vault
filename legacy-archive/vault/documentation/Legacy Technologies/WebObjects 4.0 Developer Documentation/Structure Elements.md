---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/Editing10.html
archived_at: '2026-07-18T01:26:35.395413Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](The%20Inspector.md)

# Structure Elements

By default, the switchable toolbar displays the Structure elements.

!

The following sections describe the elements you can create with these buttons.

## Paragraphs

Click ! to create a new paragraph. If there is a text selection, the entire selection becomes a paragraph.
You can use the Inspector to set the paragraph to one of the following tags:

- Plain (<P>)
- Preformatted (<PRE>)
- Address (<ADDRESS>)
- Block quote (<BLOCKQUOTE>)
- Division (<DIV>)

## Lists

Click ! to create a new list. If there is a selection, each line in the selection becomes a list item (<LI>). By default the list is an unordered (bulleted) list (<UL>). You can use the Inspector to change the list to an ordered list (<OL>). You can also change the way in which lists appear; for example, displaying an ordered list in Roman numerals (on browsers that support this feature).
When typing in a list:

- Press Shift-Enter to create a second list item. (If you simply press Enter, you will create a line break but no new list item.)
- Press Tab to create a new list nested inside the original list.
- Press Shift-Tab to move the nesting back one level.

## Headings

Click ! to create a heading. By default, an <H3> element is created. You can use the Inspector to change the level of the heading to between <H1> and <H6>.

## Horizontal Rule

Click ! to create horizontal rule (<HR>) element. You can use the Inspector to vary its height and width, and whether it is displayed in as a flat or shaded line.

## Images

Click ! to add a static image (<IMG>). A Select Image panel appears, allowing you to select an image file to display at the insertion point. The Inspector allows you to change the image's properties, including its size, file path, and whether it uses an absolute or relative reference.
With static images, you must specify a known file path. You can also create a _dynamic image_, which refers to an image file that lives in your project or in a framework. See ["Dynamic Images"](DynamicElements19.md#apple-g4ztiny) for more information.

To set an image for the page background, see ["Setting Page Attributes"](Setting%20Page%20Attributes.md#apple-gu4dsni).

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](Editing11.md)
