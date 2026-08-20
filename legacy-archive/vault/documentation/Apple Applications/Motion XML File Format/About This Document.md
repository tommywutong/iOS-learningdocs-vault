---
title: Motion XML File Format
apple_id: TP40007455
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2010-06-24'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/motion_XML_guide/About/About.html
archived_at: '2026-07-15T05:18:59.166009Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Motion%20XML%20Overview.md)

# About This Document

This document describes components of the Motion XML file format. In particular, it provides information about XML elements of the Motion scene graph. (A Motion scene graph specifies the objects in a Motion project, their attributes, the media files they incorporate, and their dependencies on other Motion objects.)

You can use the information in this document to directly edit the XML specification of a Motion scene graph and thus modify a Motion project offline. Possible modifications include changing scene object parameters, replacing media files, and editing text objects. You might also develop a utility that lets you automate modifications to Motion projects.

This document describes aspects of version 3 of the Motion XML file format. In particular it discusses:

- the Motion scene graph.
- the Motion scene objects.
- related parameter settings.

It does _not_ describe:

- filter parameters.
- behavior parameters.
- canvas and viewer details.
- Motion UI state.
- curve interpolation formulae.
- scene object and parameter flags.

This document assumes that you are familiar with general XML conventions and the Motion application.

This document contains the following chapters:

- [Motion XML Overview](Motion%20XML%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqnbnknlte)
- [Elements, Subelements, and Attributes](Elements%2C%20Subelements%2C%20and%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqnrnknltc)
- [The Properties Parameter](The%20Properties%20Parameter.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqnznknltc)
- [The Object Parameter](The%20Object%20Parameter.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqobnknltc)
- [Channel Folders and Related Elements](Channel%20Folders%20and%20Related%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqojnknltc)
- [Customizing a Motion XML Project File](Customizing%20a%20Motion%20XML%20Project%20File.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjvfvbuqmjqfvjvomi)

Elements appear in computer voice and initial lower case: `scenenode`, `layer`, and so on.

Names of attributes of elements appear in computer voice and initial lower case, and are followed by the = symbol: `uuid=`, `factoryID=`, and so on.

Values for attributes appear in computer voice and initial uppercase: `Properties`, `Position`, and so on.

An asterisk (\*) following an element indicates there may be 0 or more instances of the element.

A plus sign (+) following an element indicates there must be at least 1 or more instances of the element.

An ellipses (. . .) in a code listing indicates that some lines of code are not displayed.

[Next](Motion%20XML%20Overview.md)

