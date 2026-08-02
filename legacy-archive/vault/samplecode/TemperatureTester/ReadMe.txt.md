---
title: TemperatureTester
apple_id: DTS10003705
resource_type: Sample Code
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2010-07-09'
source_url: https://developer.apple.com/library/archive/samplecode/TemperatureTester/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:26:24.563163Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TemperatureTester](TemperatureTester.md)


[Next](main.m.md)[Previous](TemperatureTester.md)

# ReadMe.txt

```
Temperature Converter

An example using NSValueTransformer to automatically convert data between different representations. The purpose of this example is to show how to create and use custom NSValueTransformer subclasses. Otherwise it is possible to create a temperature converter using "regular glue code" with less lines of code.

Temperature Converter presents a simple user interface through which the user can enter temperature values in any of four different units and the application will automatically convert and display the temperature in the other three units.  The four units are Kelvin, Celsius, Fahrenheit, and-- the infrequently used-- Rankine temperature scale.

Internally, the application stores temperature values in Kelvin and uses value transformers to transform the entered temperature value to Kelvin and then from Kelvin to the other scales needed.



The Classes

The application uses value transformer classes to convert between Kelvin and the other three units. The RankineValueTransformer and CelsiusValueTransformer convert between Kelvin units and  Rankine and Celsius units respectively.

The FahrenheitValueTransformer converts uses the CelsiusValueTransformer to convert from Kelvin to Celsius before converting the Celsius value to the Fahrenheit temperature scale. It is intended to demonstrate that value transformers can be chained quite easily. Alternatively, the FahrenheitValueTransformer could have been implemented by subclassing CelsiusValueTransformer.

All three transformer classes implement reverse transformations.

An instance of the ApplicationDelegate can be found within the main interface file. It acts as the application delegate and implements the -applicationWillFinishLaunching: method to register the three value transformer classes with the runtime via class methods provided by NSValueTransformer.  The method also registers the boiling point of water as the default temperature to be displayed if the application has never been launched before.  Because it is more natural for most to think in Celsius than Kelvin, an instance of CelsiusValueTransformer is used directly to convert the boiling point of water from Celsius to Kelvin before pushing it into the user defaults as a registration default.

The ApplicationDelegate programmatically configures the value binding of the Rankine form cell to use the RankineValueTransformer.   The resulting binding is identical to the configuration of the other field's value binding configuration as done within the MainMenu nib file.



The Interface

The application presents the with four fields into which temperature values can be entered and the converted values will be displayed. Each field has a value binding that is connected to the LastTemperature key of the Shared Defaults controller. By using the Shared Defaults controller, the last value entered by the user will automatically be stored into the user defaults database and will be used the next time the application is launched.

The Celsius and Fahrenheit fields each have their value binding configured to use the appropriate value transformer. The Rankine field's value binding is programmatically configured in the -awakeFromNib method of ApplicationDelegate.


The Unit Tests
This modified version of Temperature Converted also contains a target for Unit Testing.


Using the Sample
Build the project using Xcode 3.2 and later. Select the ÒUnit TestsÓ as the active target for this project and run the project.
Enter a value in any of the fields and press return to view the conversions.



Change from Previous Versions
-Replaced all occurrences of Centigrade with Celsius. Updated the values of the Bundle Loader and Test Host build settings of the ÒUnit TestsÓ Target; replaced BUILT_PRODUCTS_DIR with CONFIGURATION_BUILD_DIR in these build settings. Updated for Mac OS X v10.6 or later.


Feedback and Bug Reports
Please send all feedback about this sample by using the Feedback form on the bottom of the sample's webpage.
Please submit any bug reports about this sample to the Bug Reporting <http://developer.apple.com/bugreporter> page.

Copyright © 2010-2003 Apple Inc. All rights reserved.
```

[Next](main.m.md)[Previous](TemperatureTester.md)

