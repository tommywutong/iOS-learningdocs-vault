---
title: QuickTime Vector Graphics
apple_id: TP40000943
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2000-11-04'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/RM/LegacyAPIs/Vectors/rmVectors/rmVectors.html
archived_at: '2026-07-18T02:05:04.067416Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)



# QuickTime Vector Graphics

This chapter discusses QuickTime vectors. QuickTime vectors are mathematical descriptions of images that are smaller in size than their equivalent bitmaps and can be scaled without loss of image quality.

This chapter also provides background information about QuickDraw GX objects that you will need to know in order to use QuickTime vectors in your software. Note, however, that you do not need QuickDraw GX on your computer to use QuickTime vectors.

Read this chapter if you need to create and manipulate QuickTime vectors.

[Inside Macintosh: QuickTime Reference](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.2.htm) describes the basic characteristics of QuickTime vectors, how they are constructed using QuickTime atoms, and how they are related to QuickDraw GX.

[Inside Macintosh: QuickTime Reference](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.4.htm) describes the QuickDraw GX concepts and data structures that you need to understand in order to work with QuickTime vectors.

A QuickTime vector corresponds to a QuickDraw GX path object, which is one of the geometric shapes supported by QuickDraw GX. Path objects are closely related to, and are in some cases defined by, other QuickDraw GX geometric shapes, such as points and curves.

- [Shape Objects](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.5.htm)
- [Supporting Objects](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.6.htm)
- [QuickDraw GX Coordinates](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.a.htm)
- [Geometry Space](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.b.htm)
- [Summary Table and Diagram of QuickDraw GX Objects](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.c.htm)
- [Shape Properties](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.d.htm)
- [Path Shapes](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.11.htm)
- [Creating and Drawing Paths](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.12.htm)
- [Geometric Properties of Style Objects](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.16.htm)
- [Color in QuickDraw GX](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.20.htm)
- [Transfer Modes](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.1d.htm)

[Inside Macintosh: QuickTime Reference](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.2c.htm) describes QuickTime vector data streams. In QuickTime, paths and their characteristics are represented by a series of atoms in a QT atom container. This ordered series of atoms is called a vector data stream. A vector data stream contains atoms for paths, atoms that specify attributes of paths, and a final atom that marks the end of the data stream. This section gives detailed instructions for creating and manipulating these atoms.

- [Contents of a Vector Data Stream](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.2d.htm)
- [Required Atoms](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.2e.htm)
- [Atoms that Specify Path Attributes](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.2f.htm)

[Inside Macintosh: QuickTime Reference](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.30.htm) describes two features of QuickTime vectors that are not based on QuickDraw GX: gradient fills and minimum bit depth.

- [Gradients for Path Fills](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.31.htm)
- [Specifying the Bit Depth for Paths](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.32.htm)

[Inside Macintosh: QuickTime Reference](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.33.htm) explains how to create and manipulate QuickTime vectors. The examples use utility functions provided by the vector codec, described in "Vector Codec Component Functions", that eliminate the need to work directly with the QuickTime atoms in a vector data stream. If your software edits or parses a great deal of vector data, it may be more efficient to work directly with the atoms. For descriptions of the atoms in a vector data stream, see "Vector QT Atom Container".

- [Opening the Vector Codec Component](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.34.htm)
- [Creating a Vector Data Stream](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.35.htm)
- [Creating a Path Using Only Off-Curve Points](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.36.htm)
- [Creating Paths With Multiple Contours and Fills](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.37.htm)
- [Specifying Joins](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.38.htm)
- [Adding Gradients](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.39.htm)
- [Specifying a Color for a Path](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.3a.htm)
- [Specifying a Transfer Mode](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.3b.htm)
- [Hit-Testing a Path](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.3c.htm)
- [Drawing Vectors](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.3d.htm)

[Inside Macintosh: QuickTime Reference](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.3e.htm) describes how to use the GX-to-vector transcoder included with QuickTime, which lets you convert QuickDraw GX data into equivalent QuickTime vectors. If your application already has QuickDraw GX data, or if you use a drawing program that can create QuickDraw GX data, the transcoder makes it easy to create vector graphics for your application

[Inside Macintosh: QuickTime Reference](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.40.htm) describes the constants that are specific to QuickTime vectors.

- [Vector Atom Types](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.41.htm)
- [Gradient Types](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.42.htm)
- [Fill Types](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.43.htm)
- [Join Constants](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.44.htm)
- [Selectors for Vector Codec Component Functions](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.45.htm)

[Inside Macintosh: QuickTime Reference](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.46.htm)defines the data structures used by QuickTime vectors.

- [Vector QT Atom Container](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.47.htm)
- [ARGB Color](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.48.htm)
- [Gradient Color Record](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.49.htm)
- [The Point Structure](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.4a.htm)
- [The Path Structure](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.4b.htm)
- [The Paths Structure](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.4c.htm)
- [Color Structure](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.4d.htm)
- [The Transfer Mode Structure](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.4e.htm)
- [Transfer Component Structure](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.4f.htm)
- [Transfer Component Flag Type](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.50.htm)
- [Transfer Component Mode Type](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.51.htm)
- [Color Value Type](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.52.htm)
- [Transfer Mode Flag Type](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.53.htm)
- [Color Space Type](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.54.htm)
- [Color Space Structures](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.55.htm)

[Inside Macintosh: QuickTime Reference](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.56.htm) defines the functions provided by vector codec components.

- `CurveAddAtomToVectorStream`
- `CurveAddPathAtomToVectorStream`
- `CurveAddZeroAtomToVectorStream`
- `CurveCountPointsInPath`
- `CurveCreateVectorStream`
- `CurveGetAtomDataFromVectorStream`
- `CurveGetLength`
- `CurveGetNearestPathPoint`
- `CurveGetPathPoint`
- `CurveInsertPointIntoPath`
- `CurveLengthToPoint`
- `CurveNewPath`
- `CurvePathPointToLength`
- `CurveSetPathPoint`

[Inside Macintosh: QuickTime Reference](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.57.htm) describes a macro provided by vector components, which you can use to convert an integer to a Fixed value.

- [ff](https://developer.apple.com/library/archive/documentation/QuickTime/REF/refVectors.57.htm)

