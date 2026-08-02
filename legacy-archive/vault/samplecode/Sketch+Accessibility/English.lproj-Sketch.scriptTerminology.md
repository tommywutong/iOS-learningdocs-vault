---
title: Sketch+Accessibility
apple_id: DTS40008920
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: null
published: '2009-07-14'
source_url: https://developer.apple.com/library/archive/samplecode/Sketch+Accessibility/Listings/English_lproj_Sketch_scriptTerminology.html
archived_at: '2026-07-18T03:24:39.268802Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Sketch+Accessibility](Sketch%2BAccessibility.md)


[Next](NSColorSKTScripting.m.md)[Previous](Accessibility-SKTLine%2BAccessibility.m.md)

# English.lproj/Sketch.scriptTerminology

```
// Sketch.scriptTerminology
// Sketch Example
//

{
    "Name" = "Sketch suite";
    "Description" = "Sketch specific classes.";

    "Classes" = {
        "NSApplication" = {
            "Name" = "application";
            "PluralName" = "applications";
            "Description" = "Sketch's top level scripting object.";
        };
        "SKTGraphic" = {
            "Name" = "graphic";
            "PluralName" = "graphics";
            "Description" = "A graphic.  This abstract class represents the individual shapes in a Sketch document.  There are subclasses for each specific type of graphic.";
            "Attributes" = {
                "xPosition" = {
                    "Name" = "x position";
                    "Description" = "The x coordinate of the graphic's bounding rectangle.";
                };
                "yPosition" = {
                    "Name" = "y position";
                    "Description" = "The y coordinate of the graphic's bounding rectangle.";
                };
                "width" = {
                    "Name" = "width";
                    "Description" = "The width of the graphic's bounding rectangle.";
                };
                "height" = {
                    "Name" = "height";
                    "Description" = "The height of the graphic's bounding rectangle.";
                };
                "scriptingStrokeColor" = {
                    "Name" = "stroke color";
                    "Description" = "The stroke color.";
                };
                "scriptingFillColor" = {
                    "Name" = "fill color";
                    "Description" = "The fill color.";
                };
        "scriptingStrokeWidth" = {
                    "Name" = "stroke thickness";
                    "Description" = "The thickness of the stroke.";
        };
            };
    };
        "SKTRectangle" = {
            "Name" = "rectangle";
            "PluralName" = "rectangles";
            "Description" = "A rectangle graphic.";
    };
        "SKTCircle" = {
            "Name" = "circle";
            "PluralName" = "circles";
            "Description" = "A circle graphic.";
    };
        "SKTLine" = {
            "Name" = "line";
            "PluralName" = "lines";
            "Description" = "A line graphic.";
    };
        "SKTText" = {
            "Name" = "text area";
            "PluralName" = "text areas";
            "Description" = "A text graphic.";
    };
        "SKTImage" = {
            "Name" = "image";
            "PluralName" = "images";
            "Description" = "an image";
            "Attributes" = {
                "filePath" = {
                    "Name" = "imagefile";
                    "Description" = "The graphic file to use for the contents of the image.  This attribute should only be used for setting.";
                };
            };
    };
        "SKTDocument" = {
            "Name" = "document";
            "PluralName" = "documents";
            "Description" = "A Sketch document.";
    };
    };
    "Synonyms" = {
        "tact" = {
            "Name" = "text contents";
            "Description" = "The textual contents of a text area graphic.";
        };
    };
}
```

[Next](NSColorSKTScripting.m.md)[Previous](Accessibility-SKTLine%2BAccessibility.m.md)

