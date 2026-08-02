---
title: 'Color Gamut Showcase: Using wide color gamut in Cocoa and Cocoa Touch applications
  with SceneKit'
apple_id: TP40017308
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: SceneKit
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/ColorGamutShowcase/Listings/Common_Controller_swift.html
archived_at: '2026-07-18T03:03:56.185970Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Color Gamut Showcase: Using wide color gamut in Cocoa and Cocoa Touch applications with SceneKit](Color%20Gamut%20Showcase-%20Using%20wide%20color%20gamut%20in%20Cocoa%20and%20Cocoa%20Touch%20applicatio.md)


[Next](Common-composite.metal.md)[Previous](OS%20X-AppDelegate.swift.md)

# Common/Controller.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A class used by the view controllers to create and display a SceneKit scene showing different techniques.
 */

import SceneKit
import ImageIO

#if os(OSX)
    typealias Color = NSColor
#elseif os(iOS) || os(tvOS)
    typealias Color = UIColor
#endif

class Controller {
    private var sceneView: SCNView
    private var imageScene: SCNScene!
    private let showLeftRightTechnique: SCNTechnique

    enum VisualizationType : Int {
        case gamutClamp
        case wideGamutHighlight
    }

    enum SceneDescription {
        case image(title: String, path: String)
        case scene(title: String, path: String)
    }

    let sceneTitles: [String]
    private let descriptions = [SceneDescription.image(title: "Baby", path: "Baby.jpg"),
                                SceneDescription.image(title: "Iceland", path: "Iceland.jpg"),
                                SceneDescription.image(title: "Italy", path: "Italy 1.jpg"),
                                SceneDescription.image(title: "Piazza", path: "Italy 2.jpg")]

    init(view: SCNView) {
        sceneView = view
        sceneView.scene = SCNScene()
        sceneView.antialiasingMode = .none

        sceneTitles = descriptions.map {
            switch $0 {
            case let .image(title, _):
                return title
            case let .scene(title, _):
                return title
            }
        }

        // The technique.json file describes a technique that splits the result of
        // SceneKit's rendering into wide gamut and small gamut regions.
        // The `composite` pass takes the contents of the wide gamut framebuffer (`COLOR`)
        // and clamps colors in the [0,1] range for the `splitFraction`-th pixels located
        // on the left of the screen.

        let techniquePath = Bundle.main.url(forResource: "technique", withExtension: "json")!
        let techniqueData = try! Data(contentsOf: techniquePath)
        let techniqueDescription = try! JSONSerialization.jsonObject(with: techniqueData, options: []) as! [String : AnyObject]
        showLeftRightTechnique = SCNTechnique(dictionary: techniqueDescription)!
        showLeftRightTechnique.setObject(NSNumber(value: splitFraction), forKeyedSubscript: "splitFraction" as NSCopying)
        showLeftRightTechnique.setObject(NSNumber(value: visualizationType.rawValue), forKeyedSubscript: "visualizationType" as NSCopying)
        sceneView.technique = showLeftRightTechnique
    }

    /// Displays the `index`-th scene
    func selectScene(at index: Int) {
        switch descriptions[index] {
        case let .image(_, path):
            displayImage(named: path)
        case let .scene(_, path):
            displayScene(named: path)
        }
    }

    private func displayImage(named name: String) {
        if let scene = sceneView.scene {

            let stringName = name as NSString
            let resourceName = stringName.deletingPathExtension
            let resourceExtension = stringName.pathExtension
            let url = Bundle.main.url(forResource: resourceName, withExtension: resourceExtension)!
            let source = CGImageSourceCreateWithURL(url as CFURL, nil)!

            if let properties = CGImageSourceCopyPropertiesAtIndex(source, 0, nil) as Dictionary? {
                var width = CGFloat(0)
                var height = CGFloat(0)

                if let number = properties[kCGImagePropertyPixelWidth] as! CFNumber? {
                    CFNumberGetValue(number, .cgFloatType, &width)
                }
                if let number = properties[kCGImagePropertyPixelHeight] as! CFNumber? {

                    CFNumberGetValue(number, .cgFloatType, &height)
                }

                let imageSize = CGPoint(x: width, y: height)
                #if os(OSX)
                let imageSizeValue = NSValue(point: imageSize)
                #elseif os(iOS)
                let imageSizeValue = NSValue(cgPoint: imageSize)
                #endif

                showLeftRightTechnique.setObject(imageSizeValue, forKeyedSubscript: "imageSize" as NSCopying)
            }

            scene.background.contents = name as NSString
        }
    }

    private func displayScene(named name: String) {
    }

    /// Controls the positon of the handle in the split view.
    /// A `splitFraction` of 0 indicates that the smaller gamut image is fully visible
    /// while a `splitFraction` of 1 indicates that the wide gamut image is fully visible.
    var splitFraction: Float = 0.5 {
        didSet {
            showLeftRightTechnique.setObject(NSNumber(value: splitFraction), forKeyedSubscript: "splitFraction" as NSCopying)
        }
    }

    /// Controls how the left side of the split visualizes the displayed image.
    /// `.gamutClamp` clamps the colors to sRGB
    /// `.wideGamutHighlight` fully displays the colors outside of sRGB and grayscales those within.
    var visualizationType: VisualizationType = .gamutClamp {
        didSet {
            showLeftRightTechnique.setObject(NSNumber(value: visualizationType.rawValue), forKeyedSubscript: "visualizationType" as NSCopying)
        }
    }
}
```

[Next](Common-composite.metal.md)[Previous](OS%20X-AppDelegate.swift.md)

