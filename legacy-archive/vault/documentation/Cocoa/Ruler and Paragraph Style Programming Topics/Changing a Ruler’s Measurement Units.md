---
title: Ruler and Paragraph Style Programming Topics
apple_id: 10000089i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2007-09-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Rulers/Tasks/ChangingUnits.html
archived_at: '2026-07-15T07:18:45.344408Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Ruler and Paragraph Style Programming Topics](Introduction%20to%20Rulers%20and%20Paragraph%20Styles.md)


[Next](Using%20a%20Ruler%20View%E2%80%99s%20Client.md)[Previous](Setting%20Up%20a%20Ruler%20View.md)

# Changing a Ruler’s Measurement Units

A new ruler view automatically uses the user’s preferred measurement units for drawing hash marks and labels, as stored in the user defaults system under the key `NSMeasurementUni`t. If your application allows the user to change his preferred measurement units, you can change them at runtime using `setMeasurementUnits:`, which takes the name of the units to use, such as `Inches` or `Centimeters`, and causes the ruler view to use that unit definition in spacing its hash marks and labels.

NSRulerView supports the units `Inches`, `Centimeters`, `Points`, and `Picas` by default. If your application uses other measurement units, your application should define and register them before creating any ruler views. To register a unit, use the class method `registerUnitWithName:abbreviation:unitToPointsConversionsFactor:stepUpCycle:stepDownCycle:`. Your application can register these wherever it’s most convenient, such as in the NSApplication delegate method `applicationDidFinishLaunching:`.

This Objective-C code fragment registers a new unit called `Grummets`, with the abbreviation `gt`:

```
NSArray *upArray;
NSArray *downArray;

upArray = [NSArray arrayWithObjects:[NSNumber numberWithFloat:2.0], nil];
downArray = [NSArray arrayWithObjects:[NSNumber numberWithFloat:0.5],
    [NSNumber numberWithFloat:0.2], nil];
[NSRulerView registerUnitWithName:@"Grummets"
    abbreviation:NSLocalizedString(@"gt", @"Grummets abbreviation string")
    unitToPointsConversionFactor:100.0
    stepUpCycle:upArray stepDownCycle:downArray];
```

A `Grummet` is 100.0 PostScript units (points) in length, so a ruler view using it draws a major hash mark every 100.0 points when its document view is unscaled. If the document view is scaled, the ruler view spaces its hash marks accordingly.

The arguments `stepUpCycle` and `stepDownCycle` control how hash marks are drawn for fractions and multiples of units. NSRulerView attempts to place hash marks so that they’re neither too crowded nor too sparse based on the current scale of the document view. It does so by drawing smaller hash marks for fractions of units where possible and by removing hash marks for whole units where necessary.

The value of `stepDownCycle` determines the fractional units checked by the ruler view. For example, with the unit `Grummets` defined above, the step down cycle is 0.5, then 0.2. With this cycle, the ruler view first checks to see if there’s room for marks every half `Grummet`, placing them if there is. Then, it checks every fifth of the remaining space, or a tenth of a full `Grummet`, placing further hash marks if there’s room. Then it returns to the first step in the cycle to further subdivide the ruler, and so on.

The value of `stepUpCycle` determines how many full unit marks get dropped when there isn’t room for each one. The example uses a single-step cycle of 2.0, which means that each second `Grummet` hash mark is displayed if there isn’t room for every one, then every fourth if there still isn’t room, and so on.

[Next](Using%20a%20Ruler%20View%E2%80%99s%20Client.md)[Previous](Setting%20Up%20a%20Ruler%20View.md)

