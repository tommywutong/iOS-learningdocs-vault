---
title: ZoomingPDFViewer
apple_id: DTS40010281
resource_type: Sample Code
platform: iOS
topic: Graphics & Animation
technology: CoreGraphics
published: '2017-04-27'
source_url: https://developer.apple.com/library/archive/samplecode/ZoomingPDFViewer/Listings/ZoomingPDFViewerSwift_ZoomingPDFViewer_ModelController_swift.html
archived_at: '2026-07-18T03:28:45.315511Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZoomingPDFViewer](ZoomingPDFViewer.md)


[Next](ZoomingPDFViewerSwift-ZoomingPDFViewer-TiledPDFScrollView.swift.md)[Previous](ZoomingPDFViewerSwift-ZoomingPDFViewer-RootViewController.swift.md)

# ZoomingPDFViewerSwift/ZoomingPDFViewer/ModelController.swift

```swift
/*
Copyright (C) 2017 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
This view controller manages the display of a set of view controllers by way of implementing the UIPageViewControllerDataSource protocol.
*/



import UIKit

/*
 A controller object that manages a simple model -- a collection of month names.

 The controller serves as the data source for the page view controller; it therefore implements pageViewController:viewControllerBeforeViewController: and pageViewController:viewControllerAfterViewController:.
 It also implements a custom method, viewControllerAtIndex: which is useful in the implementation of the data source methods, and in the initial configuration of the application.

 There is no need to actually create view controllers for each page in advance -- indeed doing so incurs unnecessary overhead. Given the data model, these methods create, configure, and return a new view controller on demand.
 */


class ModelController: NSObject, UIPageViewControllerDataSource {


    var pdf: CGPDFDocument!

    var numberOfPages: Int = 0



    override init()
    {
        super.init()

        if let pdfURL:URL = Bundle.main.url(forResource: "input_pdf.pdf", withExtension: nil)
        {
            let documentURL:CFURL = pdfURL as CFURL
            pdf = CGPDFDocument(documentURL)
            numberOfPages = pdf.numberOfPages as Int
            if numberOfPages % 2 == 1
            {
                numberOfPages += 1
            }
        }
        else
        {
            // missing pdf file, cannot proceed.
            print("missing pdf file input_pdf.pdf")
            abort() /* as per Technical Q&A QA1561: How do I programmatically quit my iOS application?*/
        }
    }



    func viewControllerAtIndex(_ index: Int, storyboard: UIStoryboard) -> DataViewController
    {
        // Create a new view controller and pass suitable data.
        let theViewController:UIViewController = storyboard.instantiateViewController(withIdentifier: "DataViewController")

        let dataViewController:DataViewController = theViewController as! DataViewController
        dataViewController.pageNumber = index + 1
        dataViewController.pdf = pdf
        return dataViewController
    }



    func indexOfViewController(_ viewController: DataViewController) -> Int
    {
        // Return the index of the given data view controller.
        // For simplicity, this implementation uses a static array of model objects and the view controller stores the model object; you can therefore use the model object to identify the index.
        return viewController.pageNumber - 1
    }



    func pageViewController(_ pageViewController: UIPageViewController, viewControllerBefore viewController: UIViewController) -> UIViewController?
    {
        var index = self.indexOfViewController(viewController as! DataViewController)

        if index == 0 || index == NSNotFound
        {
            return nil
        }

        index -= 1
        return self.viewControllerAtIndex(index, storyboard: viewController.storyboard!)
    }



    func pageViewController(_ pageViewController: UIPageViewController, viewControllerAfter viewController: UIViewController) -> UIViewController?
    {
        var index = self.indexOfViewController(viewController as! DataViewController)

        if index == NSNotFound
        {
            return nil
        }

        index += 1

        if index == numberOfPages
        {
            return nil
        }

        return self.viewControllerAtIndex(index, storyboard: viewController.storyboard!)
    }


}
```

[Next](ZoomingPDFViewerSwift-ZoomingPDFViewer-TiledPDFScrollView.swift.md)[Previous](ZoomingPDFViewerSwift-ZoomingPDFViewer-RootViewController.swift.md)

