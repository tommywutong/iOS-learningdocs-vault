---
title: 'RawExpose: Using CIRAWFilter to Decode RAW Images'
apple_id: TP40017310
resource_type: Sample Code
platform: iOS
topic: null
technology: CoreImage
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/RawExpose/Listings/RawExposeEmbedded_ImageViewController_swift.html
archived_at: '2026-07-18T03:21:56.856871Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [RawExpose: Using CIRAWFilter to Decode RAW Images](RawExpose-%20Using%20CIRAWFilter%20to%20Decode%20RAW%20Images.md)


[Next](RawExposeEmbedded-AlbumCollectionViewController.swift.md)[Previous](RawExposeEmbedded-AppDelegate.swift.md)

# RawExposeEmbedded/ImageViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Application Image view controller.
*/

import UIKit
import GLKit
import ImageIO
import Photos
import CoreImage

/**
        This UIViewController displays an image processed using
        the CoreImage CIRawFilter in a GLKView.
        It also allows the user to perform simple edit, like
        adjusting exposure, temperature and tint.
 */
class ImageViewController: UIViewController, GLKViewDelegate {
    // MARK: Properties

    /// Outlet to sliders used to edit the image.
    @IBOutlet weak var exposureSlider : UISlider!
    @IBOutlet weak var tempSlider : UISlider!
    @IBOutlet weak var tintSlider : UISlider!

    /**
        View used to display the CoreImage output produced by the
        CIRawFilter.
     */
    @IBOutlet weak var imageView : GLKView!

    // Asset containing the image to render.
    var asset : PHAsset?

    // Original values of temperature and tint from the image.
    var originalTemp : Float = 0.0
    var originalTint : Float = 0.0

    // CIRawFilter used to process the Raw image
    var ciRawFilter : CIFilter?

    // Size of the processed image.
    var imageNativeSize : CGSize?

    // Context used to render the CIImage to display.
    var ciContext : CIContext?

    // MARK: Image load

    /// On load, construct the CIRawFilter
    override func viewDidLoad() {
        super.viewDidLoad()

        guard let asset = asset else { return }

        // Setup options to request original image.
        let options = PHImageRequestOptions()
        options.version = .original
        options.isSynchronous = true

        // Request the image data and UTI type for the image.
        PHImageManager.default().requestImageData(for: asset, options: options) { imageData, dataUTI, _, _ in
            guard let imageData = imageData, let dataUTI = dataUTI else { return }

            /**
                    Create a CIRawFilter from original image data.
                    UTI type is passed in to provide the CIRawFilter with
                    a hint about the UTI type of the Raw file.
             */
            let rawOptions = [ String(kCGImageSourceTypeIdentifierHint) : dataUTI ]
            self.ciRawFilter = CIFilter(imageData: imageData as Data, options: rawOptions)

            guard let ciRawFilter = self.ciRawFilter else { return }

            // Get the native size of the image produced by the CIRawFilter.
            if let value = ciRawFilter.value(forKey: kCIOutputNativeSizeKey) as? CIVector {
                self.imageNativeSize = CGSize(width: value.x, height: value.y)
            }

            // Record the original value of the temperature, and setup the editing slider.
            if let value = ciRawFilter.value(forKey: kCIInputNeutralTemperatureKey) {
                self.originalTemp = (value as AnyObject).floatValue
                self.tempSlider.setValue((value as AnyObject).floatValue, animated: false)
            }

            // Record the original value of the tint, and setup the editing slider.
            if let value = ciRawFilter.value(forKey: kCIInputNeutralTintKey) {
                self.originalTint = (value as AnyObject).floatValue
                self.tintSlider.setValue((value as AnyObject).floatValue, animated: false)
            }
        }

        // Create EAGL context used to render the CIImage produced by the CIRawFilter to display.
        imageView.context = EAGLContext(api : .openGLES3)
        ciContext = CIContext(eaglContext: imageView.context, options:[ kCIContextWorkingFormat : Int(kCIFormatRGBAh) ])
    }

    // MARK: Image edit actions

    /// Resets the CIRawFilter to the original values.
    @IBAction func resetSettings(_ sender: UIBarButtonItem) {
        guard let ciRawFilter = ciRawFilter else { return }

        ciRawFilter.setValue(0.0, forKey: kCIInputEVKey)
        exposureSlider.setValue(0.0, animated: false)

        ciRawFilter.setValue(originalTemp, forKey: kCIInputNeutralTemperatureKey)
        tempSlider.setValue(originalTemp, animated: false)

        ciRawFilter.setValue(originalTint, forKey: kCIInputNeutralTintKey)
        tintSlider.setValue(originalTint, animated: false)

        imageView.setNeedsDisplay()
    }

    /// Adjust the exposure of the image
    @IBAction func exposureAdjusted(sender: UISlider) {
        guard let ciRawFilter = ciRawFilter else { return }

        ciRawFilter.setValue(sender.value, forKey: kCIInputEVKey)
        imageView.setNeedsDisplay()
    }

    /// Adjust the temperature of the image
    @IBAction func temperatureAdjusted(sender: UISlider) {
        guard let ciRawFilter = ciRawFilter else { return }

        ciRawFilter.setValue(sender.value, forKey: kCIInputNeutralTemperatureKey)
        imageView.setNeedsDisplay()
    }

    /// Adjust the tint of the image
    @IBAction func tintAdjusted(sender: UISlider) {
        guard let ciRawFilter = ciRawFilter else { return }

        ciRawFilter.setValue(sender.value, forKey: kCIInputNeutralTintKey)
        imageView.setNeedsDisplay()
    }

    /// Update the image when the device is rotated.
    override func viewWillTransition(to size: CGSize, with coordinator: UIViewControllerTransitionCoordinator) {
        self.imageView.setNeedsDisplay()
    }

    /// Render image to display.
    func glkView(_ view: GLKView, drawIn rect: CGRect) {
        guard let context = ciContext, let ciRawFilter = ciRawFilter, let imageNativeSize = imageNativeSize else { return }

        // OpenGLES drawing setup.
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GLbitfield(GL_COLOR_BUFFER_BIT))

        // Set the blend mode to "source over" so that CI will use that.
        glEnable(GLenum(GL_BLEND))
        glBlendFunc(GLenum(GL_ONE), GLenum(GL_ONE_MINUS_SRC_ALPHA))

        // Calculate scale to show the image at.
        let contentScaledRect = rect.applying(CGAffineTransform(scaleX: view.contentScaleFactor, y: view.contentScaleFactor))
        let scale = min(contentScaledRect.width / imageNativeSize.width, contentScaledRect.height / imageNativeSize.height)

        // Set scale factor of the CIRawFilter to size it correctly for display.
        ciRawFilter.setValue(scale, forKey: kCIInputScaleFactorKey)

        // Calculate rectangle to display image in.
        var displayRect = CGRect(x:0, y:0, width:imageNativeSize.width, height:imageNativeSize.height).applying(CGAffineTransform(scaleX: scale, y: scale))

        // Ensure the image is centered.
        displayRect.origin.x = (contentScaledRect.width - displayRect.width) / 2.0
        displayRect.origin.y = (contentScaledRect.height - displayRect.height) / 2.0

        guard let image = ciRawFilter.outputImage else { return }

        // Display the image scaled to fit.
        context.draw(image, in:displayRect, from:image.extent)
    }
}
```

[Next](RawExposeEmbedded-AlbumCollectionViewController.swift.md)[Previous](RawExposeEmbedded-AppDelegate.swift.md)

