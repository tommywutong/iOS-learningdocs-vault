---
title: Sketch+Accessibility
apple_id: DTS40008920
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: null
published: '2009-07-14'
source_url: https://developer.apple.com/library/archive/samplecode/Sketch+Accessibility/Listings/Sketch_scriptSuite.html
archived_at: '2026-07-18T03:24:42.930557Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Sketch+Accessibility](Sketch%2BAccessibility.md)


[Next](Sketch.sdef.md)[Previous](NSColorSKTScripting.m.md)

# Sketch.scriptSuite

```
// Sketch.scriptSuite
// Sketch Example
//

{
    "Name" = "Sketch";
    "AppleEventCode" = "sktc";

    "Classes" = {
        "NSApplication" = {
            "Superclass" = "NSCoreSuite.NSApplication";
            "ToManyRelationships" = {
                "orderedDocuments" = {
                    "Type" = "SKTDocument";
                    "AppleEventCode" = "docu";
                };
            };
            "AppleEventCode" = "capp";
        };
        "SKTGraphic" = {
            "Superclass" = "NSCoreSuite.AbstractObject";
            "AppleEventCode" = "grph";
            "Attributes" = {
                "xPosition" = {
                    "Type" = "NSNumber";
                    "AppleEventCode" = "xpos";
                };
                "yPosition" = {
                    "Type" = "NSNumber";
                    "AppleEventCode" = "ypos";
                };
                "width" = {
                    "Type" = "NSNumber";
                    "AppleEventCode" = "widt";
                };
                "height" = {
                    "Type" = "NSNumber";
                    "AppleEventCode" = "heig";
                };
                "scriptingStrokeColor" = {
                    "Type" = "NSColor";
                    "AppleEventCode" = "sclr";
                };
                "scriptingFillColor" = {
                    "Type" = "NSColor";
                    "AppleEventCode" = "fclr";
                };
        "scriptingStrokeWidth" = {
                    "Type" = "NSNumber";
                    "AppleEventCode" = "slwd";
        };
            };
    };
        "SKTRectangle" = {
            "Superclass" = "SKTGraphic";
            "AppleEventCode" = "d2rc";
    };
        "SKTCircle" = {
            "Superclass" = "SKTGraphic";
            "AppleEventCode" = "d2cr";
    };
        "SKTLine" = {
            "Superclass" = "SKTGraphic";
            "AppleEventCode" = "d2ln";
    };
        "SKTText" = {
            "Superclass" = "SKTGraphic";
            "AppleEventCode" = "d2ta";
            "ToOneRelationships" = {
                "scriptingContents" = {
                    "Type" = "NSTextStorage";
                    "AppleEventCode" = "tact";
                };
            };
    };
        "SKTImage" = {
            "Superclass" = "SKTGraphic";
            "AppleEventCode" = "d2im";
            "Attributes" = {
                "filePath" = {
                    "Type" = "NSString";
                    "AppleEventCode" = "imgf";
                };
            };
    };
        "SKTDocument" = {
            "Superclass" = "NSCoreSuite.NSDocument";
            "AppleEventCode" = "docu";
            "ToManyRelationships" = {
                "graphics" = {
                    "Type" = "SKTGraphic";
                    "AppleEventCode" = "grph";
                };
                "rectangles" = {
                    "Type" = "SKTRectangle";
                    "AppleEventCode" = "d2rc";
                };
                "circles" = {
                    "Type" = "SKTCircle";
                    "AppleEventCode" = "d2cr";
                };
                "lines" = {
                    "Type" = "SKTLine";
                    "AppleEventCode" = "d2ln";
                };
                "textAreas" = {
                    "Type" = "SKTText";
                    "AppleEventCode" = "d2ta";
                };
                "images" = {
                    "Type" = "SKTImage";
                    "AppleEventCode" = "d2im";
                };
            };
    };
    };
    "Synonyms" = {
        "tact" = "NSTextSuite.NSTextStorage";
    };
}
```

[Next](Sketch.sdef.md)[Previous](NSColorSKTScripting.m.md)

